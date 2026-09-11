#!/usr/bin/env python3
"""Find review-record candidates for gene/program-to-secreted-product bridges.

This is a discovery/audit tool, not a promotion tool. It scans Module 22A
review records for target-gene, program, or phenotype entries whose assay text
places a named candidate product near explicit secretion/release language. It
preserves the local review record and its cited locators so a reviewer can
validate the primary paper. No causal graph edge is written by this script.
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
    "target_or_program_label",
    "target_class",
    "relation_type",
    "evidence_layer",
    "stable_citations",
    "species",
    "cell_type_model",
    "assay_or_perturbation",
    "output_evidence_class",
    "output_language",
    "output_product_labels",
    "gene_form_id",
    "product_form_id",
    "product_form_ids",
    "transition_id",
    "transition_ids",
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
    ("target_proximal_production_language", re.compile(r"production|produced", re.I)),
)
KNOWN_PRODUCT_TOKENS = {
    "bdnf", "ccl2", "ccl3", "ccl5", "cxcl10", "cxcl12", "il1a", "il1b",
    "il6", "il8", "il10", "il12", "il15", "lif", "mif", "ngf", "shh",
    "tgfb", "tnf", "vegfa", "opg", "tslp", "nodal", "gdf1", "wnt5a",
}
PRODUCT_PATTERNS = (
    ("Bdnf", re.compile(r"\bBDNF\b", re.I)),
    ("Ccl2", re.compile(r"\bCCL2\b|\bMCP-?1\b", re.I)),
    ("Ccl3", re.compile(r"\bCCL3\b|\bMIP-?1(?:alpha|α)\b", re.I)),
    ("Ccl5", re.compile(r"\bCCL5\b|\bRANTES\b", re.I)),
    ("Cxcl10", re.compile(r"\bCXCL10\b|\bIP-?10\b", re.I)),
    ("Cxcl12", re.compile(r"\bCXCL12\b|\bSDF-?1\b", re.I)),
    ("Il1a", re.compile(r"\bIL-?1(?:alpha|α|a)\b", re.I)),
    ("Il1b", re.compile(r"\bIL-?1(?:beta|β|b)\b", re.I)),
    ("Il6", re.compile(r"\bIL-?6\b|\bIL6\b", re.I)),
    ("Il8", re.compile(r"\bIL-?8\b|\bIL8\b|\bCXCL8\b", re.I)),
    ("Il10", re.compile(r"\bIL-?10\b|\bIL10\b", re.I)),
    ("Il12", re.compile(r"\bIL-?12(?:p70)?\b|\bIL12\b", re.I)),
    ("Il15", re.compile(r"\bIL-?15\b|\bIL15\b", re.I)),
    ("Lif", re.compile(r"\bLIF\b", re.I)),
    ("Mif", re.compile(r"\bMIF\b", re.I)),
    ("Ngf", re.compile(r"\bNGF\b", re.I)),
    ("Opg", re.compile(r"\bOPG\b|\bosteoprotegerin\b", re.I)),
    ("Shh", re.compile(r"\bSHH\b|\bsonic hedgehog\b", re.I)),
    ("Tgfb", re.compile(r"\bTGF-?(?:beta|β|b)\b", re.I)),
    ("Tnf", re.compile(r"\bTNF(?:-?(?:alpha|α))?\b", re.I)),
    ("Vegfa", re.compile(r"\bVEGF(?:-?A)?\b", re.I)),
    ("Tslp", re.compile(r"\bTSLP\b", re.I)),
    ("Nodal", re.compile(r"\bNODAL\b", re.I)),
    ("Gdf1", re.compile(r"\bGDF1\b", re.I)),
    ("Wnt5a", re.compile(r"\bWNT5A\b", re.I)),
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
    tokens: list[str] = []
    for token in re.findall(r"[A-Za-z][A-Za-z0-9-]{1,31}", target):
        compact = token.casefold().replace("-", "")
        if compact in KNOWN_PRODUCT_TOKENS:
            tokens.append(token)
    return tokens


def output_matches(target: str, assay: str) -> tuple[str, str, list[str]]:
    # Inspect the assay field only. Relation prose can mention receptor
    # cleavage/release or a secondary phenotype and would create false output
    # bridges if treated as a measurement.
    text = assay
    target_matches = [
        match
        for token in target_tokens(target)
        for match in re.finditer(re.escape(token), text, re.I)
    ]
    output_language_matches = [
        (name, match)
        for name, pattern in OUTPUT_PATTERNS
        for match in pattern.finditer(text)
    ]
    product_matches = [
        (label, match)
        for label, pattern in PRODUCT_PATTERNS
        for match in pattern.finditer(text)
    ]
    # A target-gene label is itself a valid product hint when the assay names
    # only that gene (for example ``Il10 expression and secretion``).
    product_matches.extend(
        (token, match)
        for token in target_tokens(target)
        for match in re.finditer(re.escape(token), text, re.I)
    )
    # Exclude occurrences that identify an input reagent or receptor context
    # rather than a product being measured. This is intentionally local to
    # the occurrence: the same product name can be an input in one clause and
    # an output in another (for example ``TSLP priming ... cytokine production``).
    product_matches = [
        (label, product_match)
        for label, product_match in product_matches
        if not (
            re.search(
                r"(?:recombinant|exogenous|stimulation|stimulated|treatment|treated|addition|added|challenge|exposure|priming|primed)\s*$",
                text[max(0, product_match.start() - 45):product_match.start()],
                re.I,
            )
            or re.match(
                r"\s*(?:-|/)?(?:receptor|receptor-deficient|stimulation|stimulated|treatment|treated|priming|primed|conditioned\s+medium|supernatant)\b",
                text[product_match.end():product_match.end() + 35],
                re.I,
            )
        )
    ]
    target_matches = [
        target_match
        for target_match in target_matches
        if not (
            re.search(
                r"(?:recombinant|exogenous|stimulation|stimulated|treatment|treated|addition|added|challenge|exposure|priming|primed)\s*$",
                text[max(0, target_match.start() - 45):target_match.start()],
                re.I,
            )
            or re.match(
                r"\s*(?:-|/)?(?:receptor|receptor-deficient|stimulation|stimulated|treatment|treated|priming|primed|conditioned\s+medium|supernatant)\b",
                text[target_match.end():target_match.end() + 35],
                re.I,
            )
        )
    ]
    # Generic secretion or conditioned-medium language is not enough: it can
    # describe an input medium, receptor cleavage, or a secondary metabolite.
    # Require the target symbol to occur nearby, then leave the interpretation
    # for primary-paper review.
    matches = [
        (name, match.group(0))
        for name, match in output_language_matches
        if (
            any(abs(match.start() - target_match.start()) <= 40 for target_match in target_matches)
            or any(abs(match.start() - product_match.start()) <= 60 for _, product_match in product_matches)
        )
        and not any(
            product_match.start() < match.start()
            and re.search(
                r"conditioned\s+medium|supernatant",
                text[product_match.end():match.end() + 20],
                re.I,
            )
            and not re.search(
                r"secret|release|production|produced|collected",
                text[max(0, product_match.start() - 30):match.end() + 30],
                re.I,
            )
            for _, product_match in product_matches
        )
    ]
    # ``secreted X binding`` describes an input ligand, not target-product
    # output. Keep it out of this queue even when X is named in the program.
    if re.search(r"(?:secretion|secreted|release|released)\b[^.;]{0,40}\b(binding|competition|association)", text, re.I):
        matches = [
            (name, phrase)
            for name, phrase in matches
            if not re.search(r"(?:secretion|secreted|release|released)\b[^.;]{0,40}\b(binding|competition|association)", text, re.I)
        ]
    if not matches:
        return "", "", []
    # The most specific terms make the queue easier to triage while preserving
    # every matched phrase in the output-language audit field.
    priority = {
        "target_proximal_conditioned_medium_language": 0,
        "target_proximal_supernatant_language": 1,
        "target_proximal_secretion_language": 2,
        "target_proximal_release_language": 3,
        "target_proximal_extracellular_language": 4,
        "target_proximal_production_language": 5,
    }
    selected = min(matches, key=lambda item: priority[item[0]])[0]
    language = "; ".join(f"{name}:{phrase}" for name, phrase in matches)
    products_by_key: dict[str, str] = {}
    for label, product_match in product_matches:
        if any(
            abs(product_match.start() - output_match.start()) <= 60
            and not (
                product_match.start() < output_match.start()
                and re.search(
                    r"(?:stimulation|stimulated|treatment|treated|addition|added|challenge|exposure|priming|primed)",
                    text[product_match.end():output_match.start()],
                    re.I,
                )
            )
            and not (
                product_match.start() < output_match.start()
                and re.search(
                    r"conditioned\s+medium|supernatant",
                    text[product_match.end():output_match.end()],
                    re.I,
                )
                and not re.search(
                    r"secret|release|production|produced|collected",
                    text[max(0, product_match.start() - 30):output_match.end() + 30],
                    re.I,
                )
            )
            for _, output_match in output_language_matches
        ):
            # Prefer the canonical spelling from PRODUCT_PATTERNS over the
            # capitalization used in a free-text target label.
            products_by_key.setdefault(normalized_label(label), label)
    products = sorted(products_by_key.values())
    return selected, language, products


def load_typed_forms(
    bundle: Path | None,
) -> tuple[dict[str, list[dict[str, str]]], dict[str, list[dict[str, str]]]]:
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
    # A single gene form can have both a role-cooccurrence transition and one
    # or more explicit label mappings. Keep all rows: indexing by source alone
    # would silently discard valid alternative product mappings.
    by_source: dict[str, list[dict[str, str]]] = {}
    for transition in transitions:
        by_source.setdefault(transition["source_form_id"], []).append(transition)
    return by_label, by_source


def resolve_forms(
    target: str,
    forms_by_label: dict[str, list[dict[str, str]]],
    transitions_by_source: dict[str, list[dict[str, str]]],
) -> tuple[str, str, str, str]:
    transition_rows = [
        row
        for rows in transitions_by_source.values()
        for row in rows
    ]
    forms = forms_by_label.get(normalized_label(target), [])
    gene_forms = [row for row in forms if row["form_type"] == "gene"]
    product_forms = [row for row in forms if row["form_type"] == "protein_ligand"]
    gene = gene_forms[0] if gene_forms else None
    product = product_forms[0] if product_forms else None
    if gene and not product:
        explicit_transition = next(
            (
                row
                for row in transition_rows
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
                for row in transition_rows
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
    candidate_by_key: dict[tuple[str, str, str, str, str, str], dict[str, object]] = {}
    review_paths = sorted(review_root.glob("module22a_batch*_review.tsv"))
    for review_path in review_paths:
        fields, records = read_tsv(review_path)
        if fields != REVIEW_FIELDS:
            continue
        relative_path = str(review_path.relative_to(ROOT)) if review_path.is_relative_to(ROOT) else str(review_path)
        for record in records:
            if record.get("review_status", "").casefold() in {"no_evidence_boundary", "unresolved"}:
                continue
            target = record.get("target_or_program", "").strip()
            if not target or target.casefold() in {"null", "none_identified"}:
                continue
            output_class, output_language, output_products = output_matches(
                target, record.get("assay_or_perturbation", "")
            )
            if not output_class:
                continue
            key = (
                normalized_label(target),
                record.get("tf_entity", ""),
                output_class,
                record.get("assay_or_perturbation", ""),
                ";".join(output_products),
            )
            gene_form, product_form, transition_id, traversal_status = resolve_forms(
                target, forms_by_label, transitions_by_source
            )
            if output_products:
                named_product_forms = [
                    form
                    for product_label in output_products
                    for form in forms_by_label.get(normalized_label(product_label), [])
                    if form["form_type"] == "protein_ligand"
                ]
                if named_product_forms:
                    product_form = named_product_forms[0]["entity_form_id"]
            product_form_ids = ";".join(dict.fromkeys(
                form["entity_form_id"]
                for product_label in output_products
                for form in forms_by_label.get(normalized_label(product_label), [])
                if form["form_type"] == "protein_ligand"
            ))
            if product_form_ids:
                product_form = product_form_ids.split(";", 1)[0]
            candidate = {
                "candidate_id": "",
                "review_record_path": relative_path,
                "review_evidence_id": record.get("module22a_evidence_id", ""),
                "review_handoff_ids": record.get("module22a_handoff_ids", ""),
                "review_status": record.get("review_status", ""),
                "tf_entity": record.get("tf_entity", ""),
                "target_or_program_label": target,
                "target_class": record.get("target_class", ""),
                "relation_type": record.get("relation_type", ""),
                "evidence_layer": record.get("evidence_layer", ""),
                "stable_citations": record.get("stable_citations", ""),
                "species": record.get("species", ""),
                "cell_type_model": record.get("cell_type_model", ""),
                "assay_or_perturbation": record.get("assay_or_perturbation", ""),
                "output_evidence_class": output_class,
                "output_language": output_language,
                "output_product_labels": ";".join(output_products),
                "gene_form_id": gene_form,
                "product_form_id": product_form,
                "product_form_ids": product_form_ids,
                "transition_id": transition_id,
                "transition_ids": transition_id,
                "traversal_status": traversal_status,
                "causal_status": "not_asserted",
                "candidate_status": "review_required",
                "context_limitations": record.get("context_limitations", ""),
            }
            existing = candidate_by_key.get(key)
            if existing is None:
                candidate_by_key[key] = candidate
            else:
                for field in (
                    "review_record_path", "review_evidence_id", "review_handoff_ids",
                    "stable_citations", "species", "cell_type_model", "context_limitations",
                    "output_language", "product_form_ids", "transition_ids",
                ):
                    values = [existing[field], candidate[field]]
                    existing[field] = ";".join(dict.fromkeys(value for value in values if value))
                if existing["product_form_ids"]:
                    existing["product_form_id"] = existing["product_form_ids"].split(";", 1)[0]
                if existing["transition_ids"]:
                    existing["transition_id"] = existing["transition_ids"].split(";", 1)[0]
    rows = list(candidate_by_key.values())
    for index, row in enumerate(rows, start=1):
        row["candidate_id"] = f"OUT:{index:05d}"
    return rows


def main() -> None:
    args = parse_args()
    rows = audit(args.review_root.resolve(), args.graph_bundle.resolve() if args.graph_bundle else None)
    write_tsv(args.output.resolve(), rows)
    print(f"review_required_output_candidates={len(rows)}")


if __name__ == "__main__":
    main()
