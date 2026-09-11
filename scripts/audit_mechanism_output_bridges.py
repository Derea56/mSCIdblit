#!/usr/bin/env python3
"""Find review-record candidates for target-gene-to-secreted-product bridges.

This is a discovery/audit tool, not a promotion tool. It scans Module 22A
review records for target-gene entries whose assay text explicitly mentions a
measured or transferred extracellular output. It preserves the local review
record and its cited locators so a reviewer can validate the primary paper.
No causal graph edge is written by this script.
"""

from __future__ import annotations

import argparse
import csv
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW_FIELDS = [
    "module22a_evidence_id",
    "module22a_handoff_ids",
    "review_status",
    "tf_entity",
    "target_or_program",
    "target_class",
    "relation_type",
    "evidence_layer",
    "stable_citations",
    "species",
    "cell_type_model",
    "assay_or_perturbation",
    "confidence",
    "directness",
    "context_limitations",
]
OUTPUT_FIELDS = [
    "candidate_id",
    "review_record_path",
    "review_evidence_id",
    "review_handoff_ids",
    "review_status",
    "tf_entity",
    "target_gene_label",
    "target_class",
    "relation_type",
    "evidence_layer",
    "stable_citations",
    "species",
    "cell_type_model",
    "assay_or_perturbation",
    "output_evidence_class",
    "output_language",
    "gene_form_id",
    "product_form_id",
    "transition_id",
    "traversal_status",
    "causal_status",
    "candidate_status",
    "context_limitations",
]
OUTPUT_PATTERNS = (
    ("target_proximal_conditioned_medium_language", re.compile(r"conditioned\s+medium", re.I)),
    ("target_proximal_supernatant_language", re.compile(r"supernatant", re.I)),
    ("target_proximal_secretion_language", re.compile(r"secretion|secreted", re.I)),
    ("target_proximal_release_language", re.compile(r"release|released", re.I)),
    ("target_proximal_extracellular_language", re.compile(r"extracellular", re.I)),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--review-root",
        type=Path,
        default=ROOT / "work" / "module22a",
        help="Directory containing module22a_batch*_review.tsv files.",
    )
    parser.add_argument(
        "--graph-bundle",
        type=Path,
        default=None,
        help="Optional exported graph bundle used to resolve typed gene/product forms.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="TSV path for the review-required candidate queue.",
    )
    return parser.parse_args()


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return reader.fieldnames or [], list(reader)


def write_tsv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def normalized_label(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    return re.sub(r"[^a-z0-9]", "", normalized)


def target_tokens(target: str) -> list[str]:
    """Extract likely gene symbols without treating prose as a gene."""
    return [
        token
        for token in re.findall(r"[A-Za-z][A-Za-z0-9-]{1,31}", target)
        if any(character.isdigit() for character in token) or token.casefold() in {"il6", "il10", "il1b", "ngf"}
    ]


def output_matches(target: str, assay: str) -> tuple[str, str]:
    # Inspect the assay field only. Relation prose can mention receptor
    # cleavage/release or a secondary phenotype and would create false output
    # bridges if treated as a measurement.
    text = assay
    target_matches = [
        match
        for token in target_tokens(target)
        for match in re.finditer(re.escape(token), text, re.I)
    ]
    output_matches = [
        (name, match)
        for name, pattern in OUTPUT_PATTERNS
        for match in pattern.finditer(text)
    ]
    # Generic secretion or conditioned-medium language is not enough: it can
    # describe an input medium, receptor cleavage, or a secondary metabolite.
    # Require the target symbol to occur nearby, then leave the interpretation
    # for primary-paper review.
    matches = [
        (name, match.group(0))
        for name, match in output_matches
        if any(abs(match.start() - target_match.start()) <= 40 for target_match in target_matches)
    ]
    if not matches:
        return "", ""
    # The most specific terms make the queue easier to triage while preserving
    # every matched phrase in the output-language audit field.
    priority = {
        "target_proximal_conditioned_medium_language": 0,
        "target_proximal_supernatant_language": 1,
        "target_proximal_secretion_language": 2,
        "target_proximal_release_language": 3,
        "target_proximal_extracellular_language": 4,
    }
    selected = min(matches, key=lambda item: priority[item[0]])[0]
    language = "; ".join(f"{name}:{phrase}" for name, phrase in matches)
    return selected, language


def load_typed_forms(bundle: Path | None) -> tuple[dict[str, list[dict[str, str]]], dict[str, dict[str, str]]]:
    if bundle is None:
        return {}, {}
    forms_path = bundle / "mechanism_entity_forms.tsv"
    transitions_path = bundle / "mechanism_entity_transitions.tsv"
    if not forms_path.exists() or not transitions_path.exists():
        raise FileNotFoundError("graph bundle must contain mechanism_entity_forms.tsv and mechanism_entity_transitions.tsv")
    _, forms = read_tsv(forms_path)
    _, transitions = read_tsv(transitions_path)
    by_label: dict[str, list[dict[str, str]]] = {}
    for form in forms:
        by_label.setdefault(normalized_label(form["canonical_name"]), []).append(form)
    return by_label, {row["source_form_id"]: row for row in transitions}


def resolve_forms(
    target: str,
    forms_by_label: dict[str, list[dict[str, str]]],
    transitions_by_source: dict[str, dict[str, str]],
) -> tuple[str, str, str, str]:
    forms = forms_by_label.get(normalized_label(target), [])
    gene_forms = [row for row in forms if row["form_type"] == "gene"]
    product_forms = [row for row in forms if row["form_type"] == "protein_ligand"]
    gene = gene_forms[0] if gene_forms else None
    product = product_forms[0] if product_forms else None
    if gene and not product:
        explicit_transition = next(
            (
                row
                for row in transitions_by_source.values()
                if row["source_form_id"] == gene["entity_form_id"]
                and row["evidence_status"] == "explicit_label_mapping"
            ),
            None,
        )
        if explicit_transition:
            product = next(
                (
                    form
                    for form_list in forms_by_label.values()
                    for form in form_list
                    if form["entity_form_id"] == explicit_transition["target_form_id"]
                ),
                None,
            )
    if gene and product:
        transition = next(
            (
                row
                for row in transitions_by_source.values()
                if row["source_form_id"] == gene["entity_form_id"]
                and row["target_form_id"] == product["entity_form_id"]
            ),
            None,
        )
        return (
            gene["entity_form_id"],
            product["entity_form_id"],
            transition["transition_id"] if transition else "",
            transition["traversal_status"] if transition else "requires_output_evidence",
        )
    return gene["entity_form_id"] if gene else "", product["entity_form_id"] if product else "", "", "requires_output_evidence"


def audit(review_root: Path, graph_bundle: Path | None) -> list[dict[str, object]]:
    forms_by_label, transitions_by_source = load_typed_forms(graph_bundle)
    rows: list[dict[str, object]] = []
    seen: set[tuple[str, str, str]] = set()
    review_paths = sorted(review_root.glob("module22a_batch*_review.tsv"))
    for review_path in review_paths:
        fields, records = read_tsv(review_path)
        if fields != REVIEW_FIELDS:
            continue
        relative_path = str(review_path.relative_to(ROOT)) if review_path.is_relative_to(ROOT) else str(review_path)
        for record in records:
            if record.get("target_class", "").casefold() != "target_gene":
                continue
            if record.get("review_status", "").casefold() in {"no_evidence_boundary", "unresolved"}:
                continue
            target = record.get("target_or_program", "").strip()
            if not target or target.casefold() in {"null", "none_identified"}:
                continue
            output_class, output_language = output_matches(target, record.get("assay_or_perturbation", ""))
            if not output_class:
                continue
            key = (record.get("module22a_evidence_id", ""), normalized_label(target), output_class)
            if key in seen:
                continue
            seen.add(key)
            gene_form, product_form, transition_id, traversal_status = resolve_forms(
                target, forms_by_label, transitions_by_source
            )
            rows.append(
                {
                    "candidate_id": f"OUT:{len(rows) + 1:05d}",
                    "review_record_path": relative_path,
                    "review_evidence_id": record.get("module22a_evidence_id", ""),
                    "review_handoff_ids": record.get("module22a_handoff_ids", ""),
                    "review_status": record.get("review_status", ""),
                    "tf_entity": record.get("tf_entity", ""),
                    "target_gene_label": target,
                    "target_class": record.get("target_class", ""),
                    "relation_type": record.get("relation_type", ""),
                    "evidence_layer": record.get("evidence_layer", ""),
                    "stable_citations": record.get("stable_citations", ""),
                    "species": record.get("species", ""),
                    "cell_type_model": record.get("cell_type_model", ""),
                    "assay_or_perturbation": record.get("assay_or_perturbation", ""),
                    "output_evidence_class": output_class,
                    "output_language": output_language,
                    "gene_form_id": gene_form,
                    "product_form_id": product_form,
                    "transition_id": transition_id,
                    "traversal_status": traversal_status,
                    "causal_status": "not_asserted",
                    "candidate_status": "review_required",
                    "context_limitations": record.get("context_limitations", ""),
                }
            )
    return rows


def main() -> None:
    args = parse_args()
    rows = audit(args.review_root.resolve(), args.graph_bundle.resolve() if args.graph_bundle else None)
    write_tsv(args.output.resolve(), rows)
    print(f"review_required_output_candidates={len(rows)}")


if __name__ == "__main__":
    main()
