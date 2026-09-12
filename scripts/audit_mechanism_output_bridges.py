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
EDGE_REGISTER_MODULES = ("21b", "22b", "23b", "24b")
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
    "review_source_namespace",
    "review_evidence_id",
    "source_edge_ids",
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
VALIDATED_OUTPUT_FIELDS = [
    "bridge_id", "source_edge_ids", "review_evidence_ids", "discovery_ids",
    "source_namespace", "source_label", "output_label", "output_product_labels",
    "relation_type", "evidence_layer", "review_trace", "primary_citations",
    "species", "cell_type_model", "assay_or_perturbation", "output_observation",
    "product_form_ids", "transition_ids", "validation_status", "causal_status",
    "traversal_status", "context_limitations",
]
PRIMARY_VALIDATION_OVERLAY = (
    ROOT / "work" / "cross_module_synthesis"
    / "mechanism_output_bridge_primary_validations.tsv"
)
OUTPUT_PATTERNS = (
    ("target_proximal_conditioned_medium_language", re.compile(r"conditioned\s+medium", re.I)),
    ("target_proximal_supernatant_language", re.compile(r"supernatant", re.I)),
    ("target_proximal_secretion_language", re.compile(r"secretion|secreted", re.I)),
    ("target_proximal_release_language", re.compile(r"release|released", re.I)),
    ("target_proximal_extracellular_language", re.compile(r"extracellular", re.I)),
    ("target_proximal_production_language", re.compile(r"production|produced", re.I)),
)
KNOWN_PRODUCT_TOKENS = {
    "adp", "atp", "bdnf", "ccl2", "ccl3", "ccl5", "csf2", "cxcl10",
    "cxcl12", "fgf2", "gaba", "glutamate", "ifna", "ifnb1", "ifng",
    "il1a", "il1b", "il6", "il8", "il10", "il12", "il15", "il22", "lif",
    "mif", "ngf", "pge2", "shh", "tgfb", "timp1", "tnf", "vegfa", "opg",
    "tslp", "nodal", "gdf1", "wnt5a", "adenosine", "nitricoxide", "ros",
    "reactiveoxygenspecies", "prongf",
    "adamts1", "adamts9", "cspg", "histone", "insulin", "tgfb3",
}
# Only include aliases where the output token identifies one intact, already
# typed ligand form. Generic cytokine, matrix, danger-signal, and hormone
# labels remain unresolved when multiple molecular forms are possible.
OUTPUT_PRODUCT_FORM_ALIASES = {
    "pge2": "pge2/prostaglandin e2",
    "opg": "opg/tnfrsf11b",
    "hmox1ho1": "hmox1/ho1",
    "uchl1": "uchl1/uchl1",
    "gja1": "gja1/cx43",
    "sdc1syndecan1": "sdc1 ectodomain; itga2:itgb1 context",
    "mmp9": "mmp9/matrix metalloproteinase-9",
    "acan": "acan/aggrecan",
    "ncan": "ncan/neurocan",
}
# These outputs can be real extracellular mediators, but they are not
# translated protein products.  Do not use their ligand-role form records as
# evidence for a gene-to-protein transition.
NON_PROTEIN_PRODUCT_KEYS = {
    "adenosine",
    "adp",
    "atp",
    "gaba",
    "glutamate",
    "insulin",
    "nitricoxide",
    "pge2",
    "reactiveoxygenspecies",
    "ros",
    "steroid",
    "testosterone",
}
PRODUCT_PATTERNS = (
    ("Adp", re.compile(r"\bADP\b", re.I)),
    ("Atp", re.compile(r"\bATP\b", re.I)),
    ("Bdnf", re.compile(r"\bBDNF\b", re.I)),
    ("Ccl2", re.compile(r"\bCCL2\b|\bMCP-?1\b", re.I)),
    ("Ccl3", re.compile(r"\bCCL3\b|\bMIP-?1(?:alpha|α)\b", re.I)),
    ("Ccl5", re.compile(r"\bCCL5\b|\bRANTES\b", re.I)),
    ("Csf2", re.compile(r"\bCSF-?2\b|\bGM-?CSF\b", re.I)),
    ("Cxcl10", re.compile(r"\bCXCL10\b|\bIP-?10\b", re.I)),
    ("Cxcl12", re.compile(r"\bCXCL12\b|\bSDF-?1\b", re.I)),
    ("Fgf2", re.compile(r"\bFGF-?2\b", re.I)),
    ("Gaba", re.compile(r"\bGABA\b", re.I)),
    ("Glutamate", re.compile(r"\bglutamate\b", re.I)),
    ("Ifna", re.compile(r"\bIFN-?alpha\b|\bIFNA\b", re.I)),
    ("Ifnb1", re.compile(r"\bIFN-?beta\b|\bIFNB1?\b", re.I)),
    ("Ifng", re.compile(r"\bIFN-?gamma\b|\bIFNG\b", re.I)),
    ("Il1a", re.compile(r"\bIL-?1(?:alpha|α|a)\b", re.I)),
    ("Il1b", re.compile(r"\bIL-?1(?:beta|β|b)\b", re.I)),
    ("Il6", re.compile(r"\bIL-?6\b|\bIL6\b", re.I)),
    ("Il8", re.compile(r"\bIL-?8\b|\bIL8\b|\bCXCL8\b", re.I)),
    ("Il10", re.compile(r"\bIL-?10\b|\bIL10\b", re.I)),
    ("Il12", re.compile(r"\bIL-?12(?:p70)?\b|\bIL12\b", re.I)),
    ("Il15", re.compile(r"\bIL-?15\b|\bIL15\b", re.I)),
    ("Il22", re.compile(r"\bIL-?22\b|\bIL22\b", re.I)),
    ("Lif", re.compile(r"\bLIF\b", re.I)),
    ("Mif", re.compile(r"\bMIF\b", re.I)),
    ("Ngf", re.compile(r"\bNGF\b", re.I)),
    ("Opg", re.compile(r"\bOPG\b|\bosteoprotegerin\b", re.I)),
    ("Pge2", re.compile(r"\bPGE2\b|\bPGE-?2\b|\bprostaglandin\s+E2\b", re.I)),
    ("Shh", re.compile(r"\bSHH\b|\bsonic hedgehog\b", re.I)),
    ("Tgfb", re.compile(r"\bTGF-?(?:beta|β|b)\b", re.I)),
    ("Tgfb3", re.compile(r"\bTGFB3\b|\bTGF-?β3\b|\bTGF-?beta3\b", re.I)),
    ("Timp1", re.compile(r"\bTIMP-?1\b|\bTIMP1\b", re.I)),
    ("Tnf", re.compile(r"\bTNF(?:-?(?:alpha|α))?\b", re.I)),
    ("Vegfa", re.compile(r"\bVEGF(?:-?A)?\b", re.I)),
    ("Tslp", re.compile(r"\bTSLP\b", re.I)),
    ("Nodal", re.compile(r"\bNODAL\b", re.I)),
    ("Gdf1", re.compile(r"\bGDF1\b", re.I)),
    ("Wnt5a", re.compile(r"\bWNT5A\b", re.I)),
    ("Immunoglobulin", re.compile(r"\bimmunoglobulin(?:s)?\b|(?<![-\w])Ig[AGMDE]\b", re.I)),
    ("Steroid", re.compile(r"\bsteroid(?:s)?\b|\bsteroidogenesis\b", re.I)),
    ("Testosterone", re.compile(r"\btestosterone\b", re.I)),
    ("Hormone", re.compile(r"\bhormone(?:s)?\b", re.I)),
    ("Adenosine", re.compile(r"\badenosine\b", re.I)),
    ("NitricOxide", re.compile(r"\bnitric[\s-]+oxide\b|\bNO\b", re.I)),
    ("ReactiveOxygenSpecies", re.compile(r"\breactive\s+oxygen\s+species\b|\bROS\b", re.I)),
    ("ProNgf", re.compile(r"\bpro-?NGF\b", re.I)),
    ("Adamts1", re.compile(r"\bADAMTS-?1\b", re.I)),
    ("Adamts9", re.compile(r"\bADAMTS-?9\b", re.I)),
    ("Cspg", re.compile(r"\bCSPG(?:s)?\b", re.I)),
    ("Histone", re.compile(r"\bhistone(?:s)?\b", re.I)),
    ("Insulin", re.compile(r"\binsulin\b", re.I)),
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


def write_rows(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def public_stable_locators(value: str) -> str:
    """Keep public citations while excluding local repository paths."""
    stable = []
    for token in value.split(";"):
        token = token.strip()
        if token.startswith(("PMID:", "PMCID:", "DOI:", "http://", "https://")):
            stable.append(token)
    return "; ".join(dict.fromkeys(stable))


def normalized_label(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    return re.sub(r"[^a-z0-9]", "", normalized)


def merge_id_values(*values: str) -> str:
    """Merge semicolon-delimited identifiers without retaining duplicates."""
    return ";".join(
        dict.fromkeys(
            part.strip()
            for value in values
            for part in value.split(";")
            if part.strip()
        )
    )


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
                r"\s*(?:-|/)?(?:dependent|receptor|receptor-deficient|stimulation|stimulated|treatment|treated|priming|primed|conditioned\s+medium|supernatant)\b",
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
    product_aliases = {
        "ros": "ReactiveOxygenSpecies",
        "reactiveoxygenspecies": "ReactiveOxygenSpecies",
        "nitricoxide": "NitricOxide",
    }
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
            canonical_label = product_aliases.get(normalized_label(label), label)
            products_by_key.setdefault(normalized_label(canonical_label), canonical_label)
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


def forms_for_product_label(
    product_label: str,
    forms_by_label: dict[str, list[dict[str, str]]],
) -> list[dict[str, str]]:
    """Resolve a product token only to an exact or explicitly safe alias."""
    key = normalized_label(product_label)
    alias_key = normalized_label(OUTPUT_PRODUCT_FORM_ALIASES.get(key, product_label))
    return forms_by_label.get(alias_key, [])


def product_form_ids_for_labels(
    output_product_labels: str,
    forms_by_label: dict[str, list[dict[str, str]]],
    existing_form_ids: str = "",
) -> str:
    """Resolve only unambiguous translated-product forms.

    Output bridges may name small molecules, matrix material, or generic
    cytokine classes.  A unique typed ligand form is useful for continuation,
    but it does not by itself justify a gene/product transition.  The
    transition field is therefore intentionally not populated here.
    """
    form_ids = [value for value in existing_form_ids.split(";") if value]
    for label in output_product_labels.split(";"):
        key = normalized_label(label)
        if not key or key in NON_PROTEIN_PRODUCT_KEYS:
            continue
        forms = [
            form for form in forms_for_product_label(label, forms_by_label)
            if form["form_type"] in {"protein_ligand", "protein_output"}
        ]
        unique_ids = list(dict.fromkeys(form["entity_form_id"] for form in forms))
        if len(unique_ids) == 1:
            form_ids.append(unique_ids[0])
    return ";".join(dict.fromkeys(form_ids))


def enrich_validated_product_forms(
    row: dict[str, str],
    forms_by_label: dict[str, list[dict[str, str]]],
) -> None:
    """Fill typed product forms without inferring gene expression or secretion."""
    form_ids = product_form_ids_for_labels(
        row.get("output_product_labels", ""),
        forms_by_label,
        row.get("product_form_ids", ""),
    )
    if form_ids:
        row["product_form_ids"] = form_ids


GENE_LEVEL_OUTPUT_MARKERS = re.compile(
    r"\b(?:mRNA|transcript|promoter|enhancer|gene\s+expression|transcription|expression)\b",
    re.I,
)


def filter_output_transition_ids(
    row: dict[str, str],
    transitions_by_source: dict[str, list[dict[str, str]]],
) -> None:
    """Retain gene/product transitions only when this output names both levels.

    A measured secreted protein is already a valid conditional product
    continuation.  A gene-product transition additionally requires local
    gene-level evidence (for example mRNA, promoter, or expression) in the
    same bridge.  This prevents an unrelated BDNF-release observation from
    inheriting the Bdnf promoter-IV mapping merely because both end at BDNF.
    """
    transition_by_id = {
        transition["transition_id"]: transition
        for transitions in transitions_by_source.values()
        for transition in transitions
    }
    output_keys = {
        normalized_label(label)
        for label in row.get("output_product_labels", "").split(";")
        if label
    }
    # Keep this test on the assay/perturbation description.  The observation
    # can mention expression in a downstream receiver (for example AQP4),
    # which must not be mistaken for expression of the named output product.
    evidence_text = row.get("assay_or_perturbation", "")
    if not output_keys or not GENE_LEVEL_OUTPUT_MARKERS.search(evidence_text):
        row["transition_ids"] = ""
        return
    retained: list[str] = []
    for transition_id in row.get("transition_ids", "").split(";"):
        transition = transition_by_id.get(transition_id)
        if not transition:
            continue
        target_key = normalized_label(transition.get("target_label", ""))
        if target_key and target_key in output_keys:
            retained.append(transition_id)
    row["transition_ids"] = ";".join(dict.fromkeys(retained))


def load_source_edge_map(bundle: Path | None) -> dict[tuple[str, str], list[str]]:
    if bundle is None:
        return {}
    edges_path = bundle / "mechanism_edges.tsv"
    if not edges_path.exists():
        return {}
    _, edges = read_tsv(edges_path)
    edge_map: dict[tuple[str, str], list[str]] = {}
    for edge in edges:
        source_label = edge.get("source_label", "")
        target_label = edge.get("target_label", "")
        for source_key in label_lookup_keys(source_label):
            for target_key in label_lookup_keys(target_label):
                edge_map.setdefault((source_key, target_key), []).append(edge["edge_id"])
    return edge_map


def label_lookup_keys(label: str) -> list[str]:
    """Return conservative exact keys for common register label variants."""
    label = label.strip()
    if not label:
        return []
    keys = {normalized_label(label.split()[0])}
    keys.add(normalized_label(label))
    for part in re.split(r"[/;|]", label):
        normalized = normalized_label(part)
        if normalized:
            keys.add(normalized)
    return sorted(keys)


def resolve_source_edges(target: str, edge_map: dict[tuple[str, str], list[str]]) -> str:
    parts = target.split(None, 1)
    if len(parts) != 2:
        return ""
    return ";".join(edge_map.get((normalized_label(parts[0]), normalized_label(parts[1])), []))


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


def transition_ids_for_products(
    product_form_ids: str,
    transitions_by_source: dict[str, list[dict[str, str]]],
) -> str:
    """Link named output forms to conditional gene-product transitions."""
    product_ids = {value for value in product_form_ids.split(";") if value}
    if not product_ids:
        return ""
    transition_ids = [
        transition["transition_id"]
        for rows in transitions_by_source.values()
        for transition in rows
        if transition["target_form_id"] in product_ids
    ]
    return ";".join(dict.fromkeys(transition_ids))


def audit(review_root: Path, graph_bundle: Path | None) -> list[dict[str, object]]:
    forms_by_label, transitions_by_source = load_typed_forms(graph_bundle)
    source_edge_map = load_source_edge_map(graph_bundle)
    candidate_by_key: dict[tuple[str, str, str, str, str, str], dict[str, object]] = {}
    review_paths = sorted(review_root.glob("*_review.tsv"))
    for review_path in review_paths:
        fields, records = read_tsv(review_path)
        if fields == REVIEW_FIELDS:
            namespace = "module22a"
        elif {"review_id", "pair", "assay_or_perturbation"}.issubset(fields):
            namespace = "module21a"
        else:
            continue
        relative_path = str(review_path.relative_to(ROOT)) if review_path.is_relative_to(ROOT) else str(review_path)
        for raw_record in records:
            if namespace == "module22a":
                record = raw_record
                review_status = record.get("review_status", "")
                target = record.get("target_or_program", "").strip()
                target_class = record.get("target_class", "")
                review_evidence_id = record.get("module22a_evidence_id", "")
                review_handoff_ids = record.get("module22a_handoff_ids", "")
                tf_entity = record.get("tf_entity", "")
                stable_citations = record.get("stable_citations", "")
                species = record.get("species", "")
                cell_type_model = record.get("cell_type_model", "")
                context_limitations = record.get("context_limitations", "")
            else:
                record = raw_record
                review_status = record.get("status", "")
                target = (
                    record.get("pair_label_canonical", "")
                    or record.get("pair", "")
                    or record.get("pair_key", "")
                ).strip()
                target_class = "source_edge_output"
                review_evidence_id = record.get("review_id", "")
                review_handoff_ids = record.get("evidence_id", "")
                tf_entity = record.get("terminal_TF", "")
                stable_citations = record.get("stable_citations", "") or record.get("source_locators", "")
                species = record.get("species", "")
                cell_type_model = record.get("cell_type_model", "")
                context_limitations = record.get("limitations", "")
            review_status_normalized = review_status.casefold()
            if "no_evidence" in review_status_normalized or "unresolved" in review_status_normalized:
                continue
            if not target or target.casefold() in {"null", "none_identified"}:
                continue
            output_class, output_language, output_products = output_matches(
                target, record.get("assay_or_perturbation", "")
            )
            if namespace == "module21a" and output_class == "target_proximal_extracellular_language":
                continue
            if not output_class:
                continue
            key = (
                normalized_label(target),
                tf_entity,
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
                    for form in forms_for_product_label(product_label, forms_by_label)
                    if form["form_type"] in {"protein_ligand", "protein_output"}
                ]
                if named_product_forms:
                    product_form = named_product_forms[0]["entity_form_id"]
            product_form_ids = product_form_ids_for_labels(
                ";".join(output_products),
                forms_by_label,
            )
            if product_form_ids:
                product_form = product_form_ids.split(";", 1)[0]
            transition_ids = transition_id
            candidate = {
                "candidate_id": "",
                "review_record_path": relative_path,
                "review_source_namespace": namespace,
                "review_evidence_id": review_evidence_id,
                "source_edge_ids": resolve_source_edges(target, source_edge_map),
                "review_handoff_ids": review_handoff_ids,
                "review_status": review_status,
                "tf_entity": tf_entity,
                "target_or_program_label": target,
                "target_class": target_class,
                "relation_type": record.get("relation_type", ""),
                "evidence_layer": record.get("evidence_layer", ""),
                "stable_citations": stable_citations,
                "species": species,
                "cell_type_model": cell_type_model,
                "assay_or_perturbation": record.get("assay_or_perturbation", ""),
                "output_evidence_class": output_class,
                "output_language": output_language,
                "output_product_labels": ";".join(output_products),
                "gene_form_id": gene_form,
                "product_form_id": product_form,
                "product_form_ids": product_form_ids,
                    "transition_id": transition_id,
                "transition_ids": transition_ids,
                "traversal_status": traversal_status,
                "causal_status": "not_asserted",
                "candidate_status": "review_required",
                "context_limitations": context_limitations,
            }
            filter_output_transition_ids(candidate, transitions_by_source)
            candidate["transition_id"] = (
                candidate["transition_ids"].split(";", 1)[0]
                if candidate["transition_ids"] else ""
            )
            existing = candidate_by_key.get(key)
            if existing is None:
                candidate_by_key[key] = candidate
            else:
                for field in (
                    "review_record_path", "review_source_namespace", "review_evidence_id", "source_edge_ids", "review_handoff_ids",
                    "stable_citations", "species", "cell_type_model", "context_limitations",
                    "output_language", "product_form_ids", "transition_ids",
                ):
                    values = [existing[field], candidate[field]]
                    existing[field] = ";".join(dict.fromkeys(value for value in values if value))
                if existing["product_form_ids"]:
                    existing["product_form_id"] = existing["product_form_ids"].split(";", 1)[0]
                existing["transition_ids"] = merge_id_values(existing["transition_ids"])
                if existing["transition_ids"]:
                    existing["transition_id"] = existing["transition_ids"].split(";", 1)[0]
    rows = list(candidate_by_key.values())
    for index, row in enumerate(rows, start=1):
        row["candidate_id"] = f"OUT:{index:05d}"
    return rows


def audit_edge_register_outputs(
    source_root: Path,
    graph_bundle: Path | None,
) -> list[dict[str, object]]:
    """Find named secreted/released products in validated downstream edges.

    These are compressed output bridges: the edge register already records a
    source mechanism and its downstream product output, but the output label
    does not by itself prove a gene-to-protein transition. The resulting rows
    therefore remain review-required and non-causal.
    """
    forms_by_label, transitions_by_source = load_typed_forms(graph_bundle)
    rows: list[dict[str, object]] = []
    for module in EDGE_REGISTER_MODULES:
        module_dir = source_root / f"module{module}"
        edge_path = module_dir / f"module{module}_edge_register.tsv"
        evidence_path = module_dir / f"module{module}_evidence_register.tsv"
        if not edge_path.exists() or not evidence_path.exists():
            continue
        _, edges = read_tsv(edge_path)
        _, evidence = read_tsv(evidence_path)
        evidence_by_edge: dict[str, list[dict[str, str]]] = {}
        for record in evidence:
            for edge_id in record.get("b_edge_ids", "").split(";"):
                if edge_id.strip():
                    evidence_by_edge.setdefault(edge_id.strip(), []).append(record)
        for edge in edges:
            if edge.get("exportable") != "true":
                continue
            target = edge.get("target_entity", "").strip()
            output_class, output_language, output_products = output_matches(target, target)
            if not output_class or not output_products:
                continue
            linked_evidence = evidence_by_edge.get(edge.get("b_edge_id", ""), [])
            stable_citations = "; ".join(
                dict.fromkeys(
                    citation
                    for record in linked_evidence
                    for citation in [public_stable_locators(record.get("source_locator", ""))]
                    if citation
                )
            )
            if not stable_citations:
                continue
            product_form_ids = product_form_ids_for_labels(
                ";".join(output_products),
                forms_by_label,
            )
            # A product-form match is not evidence that the upstream edge
            # measured transcription, translation, or secretion from a gene.
            # Keep gene/product transitions empty unless the source label is
            # itself resolved to a supported transition.
            transition_ids = ""
            species = edge.get("species_context", "")
            cell_type_model = edge.get("cell_type_context", "")
            context_limitations = "; ".join(
                dict.fromkeys(
                    value
                    for value in (
                        edge.get("context_scope", ""),
                        edge.get("compartment_context", ""),
                        edge.get("injury_context", ""),
                        *(record.get("limitations", "") for record in linked_evidence),
                    )
                    if value
                )
            )
            evidence_summary = "; ".join(
                dict.fromkeys(
                    record.get("evidence_summary", "")
                    for record in linked_evidence
                    if record.get("evidence_summary", "")
                )
            )
            rows.append(
                {
                    "candidate_id": "",
                    "review_record_path": str(edge_path.relative_to(ROOT)),
                    "review_source_namespace": f"module{module}_edge_register",
                    "review_evidence_id": ";".join(
                        record.get("b_evidence_id", "")
                        for record in linked_evidence
                        if record.get("b_evidence_id", "")
                    ),
                    "source_edge_ids": edge.get("b_edge_id", ""),
                    "review_handoff_ids": ";".join(
                        record.get("source_a_evidence_id", "")
                        for record in linked_evidence
                        if record.get("source_a_evidence_id", "")
                    ),
                    "review_status": "edge_register_output_candidate",
                    "tf_entity": "",
                    "target_or_program_label": target,
                    "target_class": "edge_register_output",
                    "relation_type": edge.get("relation_type", ""),
                    "evidence_layer": edge.get("evidence_layer", ""),
                    "stable_citations": stable_citations,
                    "species": species,
                    "cell_type_model": cell_type_model,
                    "assay_or_perturbation": evidence_summary,
                    "output_evidence_class": output_class,
                    "output_language": output_language,
                    "output_product_labels": ";".join(output_products),
                    "gene_form_id": "",
                    "product_form_id": product_form_ids.split(";", 1)[0] if product_form_ids else "",
                    "product_form_ids": product_form_ids,
                    "transition_id": transition_ids.split(";", 1)[0] if transition_ids else "",
                    "transition_ids": transition_ids,
                    "traversal_status": "requires_output_evidence",
                    "causal_status": "not_asserted",
                    "candidate_status": "review_required",
                    "context_limitations": context_limitations,
                }
            )
    for index, row in enumerate(rows, start=1):
        row["candidate_id"] = f"EDGEOUT:{index:05d}"
    return rows


def _extract_trace(value: str, prefix: str) -> str:
    match = re.search(rf"(?:^|;\s*){re.escape(prefix)}=(.*?)(?=;\s*(?:review|primary|no SCI|discovery_id)=|$)", value)
    return match.group(1).strip() if match else ""


def audit_validated_output_bridges(
    source_root: Path,
    graph_bundle: Path | None,
) -> list[dict[str, object]]:
    """Export registered primary-validated output observations as gated bridges.

    This is deliberately separate from ``mechanism_edges.tsv``. A registered
    output observation can support a conditional continuation from an upstream
    mechanism to a named extracellular product, but it does not prove the
    gene-to-product, secretion, transport, or receiver-cell steps needed for a
    traversable intercellular path.
    """
    forms_by_label, transitions_by_source = load_typed_forms(graph_bundle)
    candidates = audit_edge_register_outputs(source_root, graph_bundle)
    evidence_by_id: dict[str, dict[str, str]] = {}
    edge_by_id: dict[str, dict[str, str]] = {}
    for module in EDGE_REGISTER_MODULES:
        edge_path = source_root / f"module{module}" / f"module{module}_edge_register.tsv"
        evidence_path = source_root / f"module{module}" / f"module{module}_evidence_register.tsv"
        if not evidence_path.exists() or not edge_path.exists():
            continue
        _, edge_rows = read_tsv(edge_path)
        edge_by_id.update({row.get("b_edge_id", ""): row for row in edge_rows})
        _, evidence_rows = read_tsv(evidence_path)
        evidence_by_id.update({row.get("b_evidence_id", ""): row for row in evidence_rows})

    rows: list[dict[str, object]] = []
    for candidate in candidates:
        evidence_ids = [value for value in candidate["review_evidence_id"].split(";") if value]
        linked = [evidence_by_id[evidence_id] for evidence_id in evidence_ids if evidence_id in evidence_by_id]
        primary_linked = [
            row for row in linked
            if row.get("exportable") == "true"
            and row.get("support_kind", "") != "review_statement"
            and (
                "primary" in row.get("support_kind", "").casefold()
                or "primary" in row.get("source_kind", "").casefold()
            )
        ]
        if not primary_linked:
            continue
        review_traces: list[str] = []
        for row in primary_linked:
            extracted_review = _extract_trace(row.get("consolidation_note", ""), "review")
            if extracted_review:
                review_traces.append(extracted_review)
            elif "review" in row.get("source_kind", "").casefold():
                review_traces.append(row.get("citation_note", ""))
        review_trace = "; ".join(dict.fromkeys(trace for trace in review_traces if trace))
        discovery_ids = ";".join(dict.fromkeys(
            match.group(1)
            for row in primary_linked
            for match in [re.search(r"discovery_id=([^;\s]+)", row.get("consolidation_note", ""))]
            if match
        ))
        output_observation = "; ".join(dict.fromkeys(
            row.get("evidence_summary", "") for row in primary_linked if row.get("evidence_summary", "")
        ))
        limitations = "; ".join(dict.fromkeys(
            value for value in (
                candidate.get("context_limitations", ""),
                *(row.get("limitations", "") for row in primary_linked),
            ) if value
        ))
        rows.append(
            {
                "bridge_id": "",
                "source_edge_ids": candidate["source_edge_ids"],
                "review_evidence_ids": candidate["review_evidence_id"],
                "discovery_ids": discovery_ids,
                "source_namespace": candidate["review_source_namespace"],
                "source_label": edge_by_id.get(candidate["source_edge_ids"].split(";", 1)[0], {}).get("source_entity", ""),
                "output_label": candidate["target_or_program_label"],
                "output_product_labels": candidate["output_product_labels"],
                "relation_type": candidate["relation_type"],
                "evidence_layer": candidate["evidence_layer"],
                "review_trace": review_trace,
                "primary_citations": candidate["stable_citations"],
                "species": candidate["species"],
                "cell_type_model": candidate["cell_type_model"],
                "assay_or_perturbation": candidate["assay_or_perturbation"],
                "output_observation": output_observation,
                "product_form_ids": candidate["product_form_ids"],
                "transition_ids": candidate["transition_ids"],
                "validation_status": "validated_primary_output",
                "causal_status": "bounded_output_only",
                "traversal_status": "conditional_product_continuation",
                "context_limitations": limitations,
            }
        )
    # These rows are manually reviewed output observations whose review lead
    # and cited primary paper were checked outside the edge-register evidence
    # schema. They remain conditional output continuations and never become
    # ordinary mechanism edges. Keep the overlay schema identical so the
    # release validator can audit it like register-derived rows.
    if PRIMARY_VALIDATION_OVERLAY.exists():
        overlay_fields, overlay_rows = read_tsv(PRIMARY_VALIDATION_OVERLAY)
        if overlay_fields != VALIDATED_OUTPUT_FIELDS:
            raise ValueError(
                "primary validation overlay header mismatch: "
                f"expected {VALIDATED_OUTPUT_FIELDS}, got {overlay_fields}"
            )
        for row in overlay_rows:
            enrich_validated_product_forms(row, forms_by_label)
            filter_output_transition_ids(row, transitions_by_source)
        rows.extend(overlay_rows)
    rows.sort(key=lambda row: (str(row["source_namespace"]), str(row["source_edge_ids"]), str(row["output_label"])))
    for index, row in enumerate(rows, start=1):
        row["bridge_id"] = f"BRIDGE:{index:05d}"
    return rows


def main() -> None:
    args = parse_args()
    graph_bundle = args.graph_bundle.resolve() if args.graph_bundle else None
    rows = audit(args.review_root.resolve(), graph_bundle)
    write_tsv(args.output.resolve(), rows)
    print(f"review_required_output_candidates={len(rows)}")


if __name__ == "__main__":
    main()
