#!/usr/bin/env python3
"""Generate evidence-only route rows from explicit output language in the queue.

This is deliberately conservative. It reads only the stored primary-supported
summary and assay fields; it never infers intracellular intermediates, TFs, or
target genes. Records that contain only binding/structure language remain
unresolved for manual review.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


RULES: tuple[tuple[str, str], ...] = (
    (
        "reporter_readout",
        r"\b(?:luciferase|reporter(?: assay| activity| construct)|beta.?galactosidase)\b",
    ),
    (
        "gene_expression_or_transcription",
        r"\b(?:gene expression|transcription(?:al)?|transcript(?:ion)?|mRNA|qRT.?PCR|RT.?PCR|promoter|target gene|RNA-seq)\b",
    ),
    (
        "cleavage_or_processing_readout",
        r"\b(?:cleavage|cleaved|proteolysis|processing|deacylation|shedding)\b",
    ),
    (
        "phagocytosis_or_engulfment",
        r"\b(?:phagocytosis|phagocytic|engulfment|engulf)\b",
    ),
    (
        "secreted_protein_or_release",
        r"\b(?:secretion|secret(?:ed|ion)|release(?:d)?|extracellular release)\b",
    ),
    (
        "translocation_or_localization_readout",
        r"\b(?:translocation|localization|localized|internalization|internalized|trafficking|endocytosis|endocytic|nuclear import|nuclear export|surface expression)\b",
    ),
    (
        "phosphorylation_or_activation_readout",
        r"\b(?:phosphorylat(?:e|ed|ion)|autophosphorylat(?:e|ed|ion)|activation|activates|activated|signaling|signalling|kinase|NF.?k.?B|ERK(?:1/2)?|JNK(?:1/2)?|p38|STAT\d*|SMAD\d*|MYD88|PI3K|AKT|G.?protein|GTPase|GTP.?gamma.?S|Rho|ROS|reactive oxygen|autophagy|ubiquitin(?:ation)?|aggregation|channel opening|NMDAR|excitotoxicity|cross.?talk|HIV p24|activin.?antagonism)\b",
    ),
    (
        "cellular_functional_readout",
        r"\b(?:chemotaxis|chemotactic|migration|migrat(?:e|ion)|proliferat(?:e|ion)|mitogenic|growth|survival|apoptosis|apoptotic|differentiation|differenti(?:ate|ation)|adhesion|rolling|repulsion|repulsive|neurite|axon|growth.?cone|contraction|injury|inflammation|inflammatory|tolerance|cytotoxic|cytotoxicity|lysis|killing|homeostasis|plasticity|myelination|scaveng(?:e|ing)|uptake|cellular response|cell response|barrier|permeability|degranulation|osteoclast|osteoblast|osteogenic|alkaline phosphatase|ALP|morphogenesis|organogenesis|synap(?:se|tic|togenesis)|angiogenesis|vascular|wound|regeneration|branching|spreading|lamellipodia|costimulation|immune response|cytokine|antiviral|antiproliferative|antimicrobial|pathogen|infection|infectivity|viral entry|disease resistance|platelet aggregation|thrombosis|hemostasis|electrophysiolog|membrane current|cell death|death response|hemolysis|clotting|anticoagulant|thrombus|entry|clearance|degradation|recruitment|sorting|turnover|depletion|inhibition|inhibitory|suppression|suppresses|neutraliz|blockade|blocked|antagon|phenotype|phenotypic|functional|function|bioactivity|potency|response|readout|outcome|developmental activity|organizer activity|neural induction|dorsalization|ganglion assembly|osteoclastogenesis|hepcidin|FSH|transformation|immune suppression|T-cell response|NKT|induction|production|modulatory activity|externalization|transport|cofactor activity|decay activity|convertase|complement deposition|serum resistance|mechanosensitivity|mechanotransduction|cointernalization|transmigration|physiological response|BMP response|developmental assay|antigen-specific response|receptor-specific activity|enzymatic activity|protease activity|ligand-induced|agonist response|sensitivity|LTP|hemisynapse clustering|surface/stability|stability and insertion|motor recovery|perineuronal-net architecture|AChR.?clustering|fibrillogenesis|receptor availability|NK-cell stimulation)\b",
    ),
    (
        "generic_functional_readout",
        r"(?:\b(?:calcium|adenylyl|adenylate|beta.?arrestin|arrestin|second messenger|functional assay|functional response|bioactivity|biological.?activity|receptor response|ligand response|phosphatidylinositol|phosphoinositide|inositol.?phosphate|IP1|IP3|agonist.?evoked|evoked response|evoked currents|desensitization|patch.?clamp|voltage.?clamp|cytokine|interleukin|TSLP|externalization|lipase activity|specific activity|activity reduction|chylomicron|receptor pharmacology|peptide activity|complement evasion|complement resistance|complement.?regulatory|MAC deposition|C3 deposition|C4b deposition|C4b.?C4dg|C9 deposition|serum bactericidal|adherence|axonal Nav delivery|cotransport|genetic interaction|antigen-specific responses|BMP responses|developmental assays|plasminogen.?activator|uPA|PAI.?1|surface stabilization|dendritic targeting|excitability|cross.?presentation|channel.?gating|electroretinograph|visual.?adaptation|perineuronal.?net|architecture readout|AChR.?clustering|cell.?death|deacetylation|nucleocytoplasmic shuttling|cell.?surface organization|Schwann.?cell organization)\b|(?-i:\bcAMP\b)|\bCa2\+|\b(?:inward current|outward current|chloride current|whole.?cell current|ion current|conductance|electrophysiolog))",
    ),
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def suffix(value: str) -> int:
    match = re.search(r"(\d+)$", value)
    return int(match.group(1)) if match else 0


def has_positive_match(text: str, pattern: str) -> bool:
    for match in re.finditer(pattern, text, flags=re.IGNORECASE):
        prefix = text[max(0, match.start() - 35) : match.start()]
        if not re.search(
            r"(?:no|not|without|lack(?:s|ing)?|absence of|failed to|did not|does not)\s+[^.]{0,25}$",
            prefix,
            flags=re.IGNORECASE,
        ):
            return True
    return False


def classify(row: dict[str, str]) -> str:
    text = " ".join(row.get(field, "") for field in ("evidence_summary", "assay_or_perturbation"))
    for output_class, pattern in RULES:
        if has_positive_match(text, pattern):
            return output_class
    return ""


def read_historical_rows(bundle: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(bundle.parent.glob("mechanism_graph_module20_24_v2026_09_21_literature_expansion*/mechanism_literature_expansion.tsv")):
        rows.extend(read_tsv(path))
    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--start-queue-suffix", type=int, default=0)
    parser.add_argument(
        "--exclude-queue-id",
        action="append",
        default=[],
        help="Exclude a specific queue record when its language is structural or binding-only.",
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    bundle = args.bundle_dir.resolve()
    queue = read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")
    evidence = read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")
    prior = read_historical_rows(bundle)
    already_curated = {row.get("source_queue_id", "") for row in prior}
    records_by_queue: dict[str, list[dict[str, str]]] = {}
    for record in evidence:
        records_by_queue.setdefault(record["source_queue_id"], []).append(record)

    eligible = []
    for row in queue:
        if row["queue_id"] in already_curated:
            continue
        if row["queue_id"] in set(args.exclude_queue_id):
            continue
        if row.get("output_class") != "unknown":
            continue
        if row.get("evidence_status") != "validated_primary_exact_layer":
            continue
        if row.get("evidence_scope") not in {"direct_edge", "contextual_support", "pathway_membership"}:
            continue
        if not row.get("source_locator") or not row.get("evidence_summary"):
            continue
        if suffix(row["queue_id"]) < args.start_queue_suffix:
            continue
        output_class = classify(row)
        if output_class:
            eligible.append((row, output_class))
    eligible.sort(key=lambda item: (item[0].get("curation_priority", "P9"), suffix(item[0]["queue_id"])))
    selected = eligible[: args.limit] if args.limit > 0 else eligible

    counts: dict[str, int] = {}
    for _, output_class in eligible:
        counts[output_class] = counts.get(output_class, 0) + 1
    preview = {
        "eligible_rows": len(eligible),
        "selected_rows": len(selected),
        "eligible_output_classes": dict(sorted(counts.items())),
        "selected_queue_ids": [row["queue_id"] for row, _ in selected],
    }
    if args.dry_run:
        print(json.dumps(preview, indent=2, sort_keys=True))
        return 0

    if not selected:
        raise ValueError("No explicit output-supported unknown records found")

    next_id = max((suffix(row.get("expansion_id", "")) for row in prior), default=0) + 1
    output: list[dict[str, str]] = []
    for index, (row, output_class) in enumerate(selected):
        records = records_by_queue.get(row["queue_id"], [])
        if not records:
            raise ValueError(f"No downstream evidence record for {row['queue_id']}")
        record = records[0]
        evidence_ids = [row["edge_id"], *filter(None, row.get("source_evidence_ids", "").split(";")), record["record_id"], *filter(None, row.get("source_locator", "").split(";"))]
        limitations = row.get("limitations", "").rstrip()
        topology_boundary = "Ligand-receptor topology remains unresolved; output evidence is retained without assigning source or target roles. Output class was assigned from explicit output/readout language in the stored primary-supported summary."
        if topology_boundary not in limitations:
            limitations = f"{limitations} {topology_boundary}".strip()
        expansion = f"M21B-LITEXP-{next_id + index}"
        output.append(
            {
                "expansion_id": expansion,
                "source_queue_id": row["queue_id"],
                "route_status": "retained_evidence_route",
                "path_expression": "????>????>????>????>output",
                "route_tier": "downstream_output_annotation_unlinked_topology",
                "known_layers": "output",
                "missing_layers": "ligand_receptor_pair|receptor|intracellular_continuation|transcription_factor",
                "intracellular_status": "not_mapped",
                "ligand_node_id": "",
                "ligand_label": "",
                "ligand_receptor_edge_id": "",
                "receptor_node_id": "",
                "receptor_label": "",
                "transcription_factor_node_id": "",
                "transcription_factor_label": "",
                "target_gene_node_id": "",
                "target_gene_label": "",
                "output_label": f"{row['source_label']}-{row['target_label']} documented {output_class}",
                "pathway_name": row.get("pathway_name", ""),
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_documented_output_unlinked_topology",
                "evidence_ids": ";".join(dict.fromkeys(evidence_ids)),
                "source_chain_id": expansion,
                "source_evidence_record_id": record["record_id"],
                "route_linkage_status": "literature_expansion:output_supported_topology_unresolved",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": row.get("evidence_polarity", "supports"),
                "negative_evidence_status": row.get("negative_evidence_status", "not_evaluated"),
                "evidence_directness": row.get("evidence_directness", "source_claim"),
                "output_class": output_class,
                "primary_locator": row["source_locator"],
                "citation_note": row.get("citation_note", ""),
                "evidence_summary": row["evidence_summary"],
                "limitations": limitations,
                "curation_status": "curated_primary_route",
                "species_context": row.get("species_context", ""),
                "cell_type_context": row.get("cell_type_context", ""),
                "assay_or_perturbation": row.get("assay_or_perturbation", ""),
                "effect_polarity": row.get("effect_polarity", ""),
                "source_scope": row.get("source_scope", row.get("evidence_scope", "direct_edge")),
            }
        )
    args.output.resolve().write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    preview["output"] = str(args.output.resolve())
    print(json.dumps(preview, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
