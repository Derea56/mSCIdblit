#!/usr/bin/env python3
"""Stage primary-study TF-target edges found while reviewing 22B holds.

These are standalone general TF-regulon assertions.  They provide reusable
target-gene evidence for named TF leads, but they do not upgrade the original
upstream ligand/receptor handoff or imply that the handoff activates the TF.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch001.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch001_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch001-2026-09-03"

UPDATES = [
    {
        "hold_edges": "M22B-E003745;M22B-E004091",
        "tf": "STAT1", "target": "IRF1", "species": "human",
        "effect": "activating_target", "status": "reviewed_direct_target",
        "locator": "PMID:8621447; DOI:10.1074/jbc.271.10.5790",
        "summary": (
            "Primary promoter and transcription assays showed STAT1 homodimers and STAT1-STAT2 heterodimers at the IRF1 regulatory element; both induced IRF1 transcription, with the heterodimer more potent."
        ),
        "context": "Human interferon-responsive cell systems; general STAT1 target evidence, not SCI-specific.",
        "limitations": "STAT2 contributes to the IFN-alpha heterodimeric mechanism; this edge is a general STAT1-associated activating target claim and does not assign an upstream Module 22A route.",
    },
    {
        "hold_edges": "M22B-E001348;M22B-E001395;M22B-E001396",
        "tf": "NR1I2", "target": "CYP3A4", "species": "human",
        "effect": "activating_target", "status": "reviewed_direct_target",
        "locator": "PMID:12781341; DOI:10.1016/S0006-2952(03)00188-6",
        "summary": (
            "A human CYP3A4 promoter reporter was activated in vivo through PXR/NR1I2 and RXR-dependent xenobiotic response elements; human PXR enhanced rifampicin-induced promoter activity and antisense PXR reduced the response."
        ),
        "context": "Mouse liver in vivo reporter containing the human CYP3A4 promoter with human or mouse PXR manipulation; general PXR target evidence.",
        "limitations": "The experiment uses a promoter reporter and mouse liver context, so it does not establish the exact DHEA- or estradiol-associated upstream handoffs in the reviewed rows.",
    },
    {
        "hold_edges": "M22B-E001359;M22B-E001360;M22B-E001361;M22B-E003552",
        "tf": "AR", "target": "KLK3", "species": "human",
        "effect": "activating_target", "status": "reviewed_direct_target",
        "locator": "PMID:12651911",
        "summary": (
            "DHT treatment increased AR occupancy at the endogenous PSA/KLK3 enhancer and promoter in LNCaP cells, followed by PSA/KLK3 mRNA and protein expression."
        ),
        "context": "Human LNCaP prostate cancer cells; classical androgen-responsive target-gene model.",
        "limitations": "The prostate-cell model and androgen stimulus are not the reviewed DHT-metabolism upstream handoffs in a spinal-cord context; no SCI transfer is inferred.",
    },
    {
        "hold_edges": "M22B-E001359;M22B-E001360;M22B-E001361;M22B-E003552",
        "tf": "AR", "target": "KLK2", "species": "human",
        "effect": "activating_target", "status": "reviewed_direct_target",
        "locator": "PMID:22597536",
        "summary": (
            "Ligand-dependent AR recruitment to androgen-responsive enhancers upregulated endogenous KLK2 expression in LNCaP cells; the same study describes the KLK2/KLK3 androgen-responsive kallikrein locus."
        ),
        "context": "Human LNCaP prostate cancer cells; androgen-responsive enhancer study.",
        "limitations": "The prostate-cell model and androgen stimulus are not the reviewed DHT-metabolism upstream handoffs in a spinal-cord context; no SCI transfer is inferred.",
    },
    {
        "hold_edges": "M22B-E001069;M22B-E001070;M22B-E001072",
        "tf": "RORC", "target": "IL17A", "species": "human",
        "effect": "activating_target", "status": "reviewed_direct_target",
        "locator": "PMID:30214937",
        "summary": (
            "Primary T-cell experiments showed an AhR-RORgamma-t complex binding RORgamma-t and AhR elements in the IL17A promoter and inducing IL17A transcription."
        ),
        "context": "Human and mouse T-cell inflammatory differentiation systems; RORC/RORgamma-t target evidence.",
        "limitations": "The reported mechanism is cooperative with AhR and stimulus-dependent; it does not establish the cholesterol-DHCR/LIPA upstream handoffs in the reviewed rows.",
    },
    {
        "hold_edges": "M22B-E000926;M22B-E000928;M22B-E001717;M22B-E001720",
        "tf": "SMAD1", "target": "ID1", "species": "human",
        "effect": "activating_target", "status": "reviewed_direct_target",
        "locator": "PMID:12296825; DOI:10.1046/j.1365-2443.2002.00573.x",
        "summary": (
            "BMP-responsive element analysis identified a human ID1 promoter element bound by a BMP-induced Smad1-Smad4 complex; BMP signaling and Smad4-dependent activity stimulated ID1 transcription."
        ),
        "context": "BMP-stimulated C2C12 myoblast reporter and endogenous-expression experiments using the human ID1 promoter.",
        "limitations": "Smad4 is required and the assay is BMP-stimulus dependent; this is not evidence for the exact BMP7/BMP8A receptor composite or SCI transfer.",
    },
    {
        "hold_edges": "M22B-E001716;M22B-E001719;M22B-E003913;M22B-E003932;M22B-E003949",
        "tf": "SMAD2", "target": "RORC", "species": "human",
        "effect": "activating_target", "status": "reviewed_direct_target",
        "locator": "PMID:26194464",
        "summary": (
            "In Th17 cells, linker-phosphorylated Smad2 cooperated with STAT3 and p300; Smad2 bound the RORC promoter and the complex transactivated RORC reporter constructs."
        ),
        "context": "Human and mouse Th17 differentiation experiments with promoter reporter, interaction, and ChIP assays.",
        "limitations": "The effect is cooperative and phosphorylation-state dependent; it does not establish the exact GDF/TGF-beta receptor composites in the reviewed rows.",
    },
    {
        "hold_edges": "M22B-E001716;M22B-E001719;M22B-E003913;M22B-E003932;M22B-E003949",
        "tf": "SMAD2", "target": "IL17A", "species": "human",
        "effect": "activating_target", "status": "reviewed_direct_target",
        "locator": "PMID:26194464",
        "summary": (
            "In Th17 cells, linker-phosphorylated Smad2 cooperated with STAT3 and p300; Smad2 bound the IL17A promoter and the complex transactivated IL17A reporter constructs."
        ),
        "context": "Human and mouse Th17 differentiation experiments with promoter reporter, interaction, and ChIP assays.",
        "limitations": "The effect is cooperative and phosphorylation-state dependent; it does not establish the exact GDF/TGF-beta receptor composites in the reviewed rows.",
    },
]

EDGE_FIELDS = [
    "b_edge_id", "source_entity", "relation_type", "target_entity", "pathway_name", "evidence_layer",
    "source_a_edge_id", "edge_status", "context_scope", "cell_type_context", "compartment_context",
    "species_context", "injury_context", "confidence_tier", "export_priority", "exportable", "consolidation_note",
]
EVIDENCE_FIELDS = [
    "b_evidence_id", "source_a_evidence_id", "b_edge_ids", "source_kind", "source_locator", "support_kind",
    "species_support", "source_scope", "confidence_tier", "citation_note", "evidence_summary", "limitations",
    "evidence_layer", "exportable", "consolidation_note",
]
AUDIT_FIELDS = [
    "batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id",
    "new_edge_status", "new_edge_confidence", "new_evidence_confidence", "source_locator",
    "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def next_id(rows: list[dict[str, str]], field: str) -> int:
    values = [int(match.group(1)) for row in rows if (match := re.search(r"(\d+)$", row[field]))]
    return max(values, default=0) + 1


def main() -> int:
    edges = read_tsv(EDGE_PATH)
    evidence = read_tsv(EVIDENCE_PATH)
    existing_pairs = {
        (row.get("species_context", "").casefold(), row.get("source_entity", "").casefold(), row.get("target_entity", "").casefold())
        for row in edges if row.get("pathway_name") == "target_gene"
    }
    edge_number = next_id(edges, "b_edge_id")
    evidence_number = next_id(evidence, "b_evidence_id")
    audit: list[dict[str, str]] = []

    for update in UPDATES:
        pair = (update["species"].casefold(), update["tf"].casefold(), update["target"].casefold())
        if pair in existing_pairs:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id = f"M22B-E{edge_number:06d}"
        evidence_id = f"M22B-EVID-{evidence_number:06d}"
        edge_number += 1
        evidence_number += 1
        source_id = f"M22B-TARGET-SEARCH-{len(audit) + 1:04d}"
        evidence_source_id = f"M22B-TARGET-SEARCH-EVID-{len(audit) + 1:04d}"
        edges.append({
            "b_edge_id": edge_id,
            "source_entity": update["tf"],
            "relation_type": f"{update['tf']} activates the {update['target']} target gene in primary-study evidence",
            "target_entity": update["target"],
            "pathway_name": "target_gene",
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "source_a_edge_id": source_id,
            "edge_status": update["status"],
            "context_scope": update["context"],
            "cell_type_context": update["context"],
            "compartment_context": "unspecified",
            "species_context": update["species"],
            "injury_context": "not_assessed",
            "confidence_tier": "high",
            "export_priority": "medium",
            "exportable": "true",
            "consolidation_note": (
                f"{BATCH_ID}: standalone general TF-target edge found while reviewing {update['hold_edges']}; "
                "does not upgrade the upstream handoff or infer SCI-specific TF activation."
            ),
        })
        evidence.append({
            "b_evidence_id": evidence_id,
            "source_a_evidence_id": evidence_source_id,
            "b_edge_ids": edge_id,
            "source_kind": update["status"],
            "source_locator": update["locator"],
            "support_kind": "primary_experiment",
            "species_support": update["species"],
            "source_scope": "direct_edge",
            "confidence_tier": "high",
            "citation_note": f"Primary-study target-gene evidence identified while reviewing hold rows {update['hold_edges']}; standalone general TF-regulon claim.",
            "evidence_summary": update["summary"],
            "limitations": update["limitations"],
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "exportable": "true",
            "consolidation_note": (
                f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded."
            ),
        })
        audit.append({
            "batch_id": BATCH_ID,
            "hold_edges_reviewed": update["hold_edges"],
            "tf": update["tf"], "target": update["target"], "species": update["species"],
            "b_edge_id": edge_id, "b_evidence_id": evidence_id,
            "new_edge_status": update["status"], "new_edge_confidence": "high", "new_evidence_confidence": "high",
            "source_locator": update["locator"], "upstream_handoff_upgraded": "false",
            "standalone_target_gene_edge": "true",
            "decision_basis": update["summary"],
        })
        existing_pairs.add(pair)

    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    write_tsv(AUDIT_PATH, audit, AUDIT_FIELDS)
    summary = {
        "batch_id": BATCH_ID,
        "standalone_target_gene_edges_added": len(audit),
        "upstream_handoff_edges_upgraded": 0,
        "high_edges_after": sum(row["confidence_tier"] == "high" for row in edges),
        "exportable_edges_after": sum(row["exportable"] == "true" for row in edges),
        "target_gene_edges_after": sum(row["pathway_name"] == "target_gene" for row in edges),
        "audit": str(AUDIT_PATH),
        "upstream_activation_inferred": False,
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
