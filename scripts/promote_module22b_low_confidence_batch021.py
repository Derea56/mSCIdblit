#!/usr/bin/env python3
"""Recover five bounded Module 22B program/phenotype associations."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch021.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch021_summary.json"
BATCH_ID = "module22b-low-confidence-upgrade-batch021-2026-09-03"

UPDATES = {
    "M22B-E000552": {
        "evidence_id": "M22B-EVID-004988",
        "relation_type": (
            "SPARC modulates FGF2-FGFR1-associated MAPK/DNA-synthesis and "
            "myoblast-differentiation responses; no direct SPARC-FGFR1 binding "
            "or terminal TF-target regulation is assigned"
        ),
        "target_entity": (
            "SPARC -> FGF2-FGFR1 signaling inhibition and PKA/myoblast "
            "differentiation response program"
        ),
        "scope": (
            "Primary studies support SPARC antagonism of FGF2-FGFR1 signaling "
            "downstream or independently of the FGFR1 extracellular ligand-binding "
            "domain. Direct SPARC-FGFR1 binding, the exact intracellular relay, "
            "and a terminal TF remain unresolved; model and SCI transfer limits "
            "remain explicit."
        ),
        "basis": (
            "Primary work supports SPARC-dependent inhibition of FGF2-FGFR1 "
            "signaling and associated myoblast differentiation responses. The "
            "functional mechanism is downstream of or independent from the "
            "FGFR1 extracellular ligand-binding domain, so this is a bounded "
            "program association rather than a direct ligand-receptor edge."
        ),
        "locator": "PMID:14505356; DOI:10.1002/jcb.10645",
        "new_pathway": "cell_state_program",
        "new_status": "reviewed_program_association",
        "new_confidence": "medium",
    },
    "M22B-E000614": {
        "evidence_id": "M22B-EVID-005031",
        "relation_type": (
            "TDGF1/Cripto supports Nodal recruitment to ACVR2B/ACVR1B-containing "
            "receptor complexes and SMAD2/3 signaling; standalone TDGF1-ACVR2B "
            "binding is not assigned"
        ),
        "target_entity": (
            "TDGF1/Cripto-Nodal-ACVR2B/ACVR1B receptor-complex -> SMAD2/3 "
            "developmental transcription program"
        ),
        "scope": (
            "Primary developmental studies support Cripto recruitment of Nodal "
            "to ACVR2B/ACVR1B complexes and SMAD2/3 output. Direct binary "
            "TDGF1/Cripto-ACVR2B binding and receptor stoichiometry remain "
            "unresolved; no direct TF-target claim or SCI context is inferred."
        ),
        "basis": (
            "Primary developmental receptor-complex studies support a "
            "Cripto/Nodal/ACVR2B-ACVR1B complex with SMAD2/3-associated output. "
            "This recovers a bounded receptor-complex program while retaining "
            "the unresolved standalone TDGF1-ACVR2B binary assignment."
        ),
        "locator": "PMCID:PMC312747; PMCID:PMC5354514; PMCID:PMC3160087; PMID:12649175; PMID:25603319",
        "new_pathway": "cell_state_program",
        "new_status": "reviewed_program_association",
        "new_confidence": "medium",
    },
    "M22B-E000620": {
        "evidence_id": "M22B-EVID-005322",
        "relation_type": (
            "P. gingivalis LPS/TLR2-TLR4-associated ANGPTL2 inflammatory program; "
            "direct ANGPTL2-TLR4 binding and ligand-specific activation are not assigned"
        ),
        "target_entity": (
            "P. gingivalis LPS -> TLR2/TLR4 -> ANGPTL2 induction and NF-kB "
            "inflammatory feedback program"
        ),
        "scope": (
            "Primary studies support TLR4-associated inflammatory regulation of "
            "ANGPTL2 under P. gingivalis LPS and related comparator conditions, "
            "with direction and context limitations. No purified ANGPTL2-TLR4 "
            "binding or standalone ANGPTL2 receptor activation is assigned; no "
            "terminal TF-target edge or SCI transfer is inferred."
        ),
        "basis": (
            "Primary inflammatory studies support a P. gingivalis LPS/TLR2-TLR4 "
            "context associated with ANGPTL2 induction and NF-kB-linked output. "
            "The evidence supports a contextual inflammatory program, not a "
            "direct ANGPTL2-TLR4 ligand-receptor claim."
        ),
        "locator": "PMID:28946139; PMCID:PMC5608282; DOI:10.1177/0963689720946663",
        "new_pathway": "cell_state_program",
        "new_status": "reviewed_program_association",
        "new_confidence": "medium",
    },
    "M22B-E000621": {
        "evidence_id": "M22B-EVID-004926",
        "relation_type": (
            "SERPINE1/PAI-1 binds vitronectin and modulates alpha-v integrin/uPAR-"
            "associated matrix adhesion; standalone ITGB5 binding is not assigned"
        ),
        "target_entity": (
            "SERPINE1/PAI-1 -> vitronectin/alpha-v-integrin matrix adhesion and "
            "migration modulation"
        ),
        "scope": (
            "Primary studies support PAI-1 binding to vitronectin and modulation "
            "of alpha-v integrin-mediated adhesion, especially alpha-v-beta-3, "
            "with uPAR/LRP1 context. The queued ITGB5-specific receptor label is "
            "not supported as a standalone interaction; no unique intracellular "
            "relay, terminal TF, or SCI transfer is inferred."
        ),
        "basis": (
            "Primary matrix-adhesion studies support PAI-1/vitronectin binding "
            "and alpha-v integrin-associated adhesion modulation. This recovers "
            "the bounded matrix-function program while excluding an unsupported "
            "standalone PAI-1-ITGB5 receptor assignment."
        ),
        "locator": "PMID:11573201; PMID:8837777; PMID:9175705; DOI:10.1002/jcp.1133; DOI:10.1038/383441a0",
        "new_pathway": "phenotype",
        "new_status": "reviewed_phenotype_only",
        "new_confidence": "medium",
    },
    "M22B-E000670": {
        "evidence_id": "M22B-EVID-004971",
        "relation_type": (
            "SLPI modulates the PLSCR1/4-CD4 membrane-complex and HIV-entry/"
            "transfer phenotype; direct SLPI-CD4 binding is not assigned"
        ),
        "target_entity": (
            "SLPI -> PLSCR1/4-CD4 membrane-complex modulation -> HIV-entry/"
            "transfer phenotype"
        ),
        "scope": (
            "The primary human study identifies PLSCR1/4 as SLPI ligands and "
            "shows PLSCR1/4 association with CD4 and associated HIV-entry/transfer "
            "effects. This supports a bounded membrane-complex modulation "
            "phenotype, not direct SLPI-CD4 binding, a unique CD4 relay, or a "
            "terminal TF; no SCI transfer is inferred."
        ),
        "basis": (
            "Primary human membrane-complex work supports SLPI interaction with "
            "PLSCR1/4 and PLSCR1/4 association with CD4 in HIV-entry/transfer "
            "biology. The recovered edge is a bounded complex-modulation "
            "phenotype and does not assert direct SLPI-CD4 binding."
        ),
        "locator": "PMID:19333378; PMCID:PMC2642901; DOI:10.1371/journal.pone.0005006",
        "new_pathway": "phenotype",
        "new_status": "reviewed_phenotype_only",
        "new_confidence": "medium",
    },
}

EDGE_FIELDS = [
    "b_edge_id", "source_entity", "relation_type", "target_entity", "pathway_name",
    "evidence_layer", "source_a_edge_id", "edge_status", "context_scope",
    "cell_type_context", "compartment_context", "species_context", "injury_context",
    "confidence_tier", "export_priority", "exportable", "consolidation_note",
]
EVIDENCE_FIELDS = [
    "b_evidence_id", "source_a_evidence_id", "b_edge_ids", "source_kind",
    "source_locator", "support_kind", "species_support", "source_scope",
    "confidence_tier", "citation_note", "evidence_summary", "limitations",
    "evidence_layer", "exportable", "consolidation_note",
]
AUDIT_FIELDS = [
    "batch_id", "b_edge_id", "b_evidence_id", "old_edge_confidence",
    "new_edge_confidence", "old_evidence_confidence", "new_evidence_confidence",
    "old_target", "new_target", "old_edge_status", "new_edge_status",
    "decision_basis", "source_locator", "module22b_register_changed",
    "canonical_sql_materialization",
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


def append_once(value: str, addition: str) -> str:
    return value if addition in value else (f"{value}; {addition}" if value else addition)


def main() -> int:
    edges = read_tsv(EDGE_PATH)
    evidence = read_tsv(EVIDENCE_PATH)
    edge_by_id = {row["b_edge_id"]: row for row in edges}
    evidence_by_id = {row["b_evidence_id"]: row for row in evidence}
    audit = []

    for edge_id, update in UPDATES.items():
        edge = edge_by_id.get(edge_id)
        ev = evidence_by_id.get(update["evidence_id"])
        if edge is None or ev is None:
            raise SystemExit(f"missing edge/evidence for {edge_id}")
        if edge["confidence_tier"] != "low":
            raise SystemExit(f"{edge_id}: expected low confidence, found {edge['confidence_tier']!r}")
        if edge_id not in (ev.get("b_edge_ids") or "").split(";"):
            raise SystemExit(f"{edge_id}: evidence link mismatch")

        old_target = edge["target_entity"]
        old_status = edge["edge_status"]
        old_edge_confidence = edge["confidence_tier"]
        old_evidence_confidence = ev["confidence_tier"]
        edge.update({
            "relation_type": update["relation_type"],
            "target_entity": update["target_entity"],
            "pathway_name": update["new_pathway"],
            "edge_status": update["new_status"],
            "context_scope": update["scope"],
            "confidence_tier": update["new_confidence"],
            "exportable": "true",
        })
        edge["consolidation_note"] = append_once(
            edge["consolidation_note"],
            f"Low-confidence recovery {BATCH_ID}: {update['new_confidence']} after bounded exact-source re-review.",
        )
        ev.update({
            "source_locator": update["locator"],
            "confidence_tier": "high",
            "evidence_summary": update["basis"],
            "limitations": update["scope"],
            "exportable": "true",
        })
        ev["consolidation_note"] = append_once(
            ev["consolidation_note"],
            f"Low-confidence recovery {BATCH_ID}: bounded program/phenotype re-adjudication; direct TF-target and exact unresolved assignments remain excluded.",
        )
        audit.append({
            "batch_id": BATCH_ID,
            "b_edge_id": edge_id,
            "b_evidence_id": update["evidence_id"],
            "old_edge_confidence": old_edge_confidence,
            "new_edge_confidence": edge["confidence_tier"],
            "old_evidence_confidence": old_evidence_confidence,
            "new_evidence_confidence": ev["confidence_tier"],
            "old_target": old_target,
            "new_target": edge["target_entity"],
            "old_edge_status": old_status,
            "new_edge_status": edge["edge_status"],
            "decision_basis": update["basis"],
            "source_locator": update["locator"],
            "module22b_register_changed": "true",
            "canonical_sql_materialization": "false",
        })

    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    write_tsv(AUDIT_PATH, audit, AUDIT_FIELDS)
    summary = {
        "batch_id": BATCH_ID,
        "records_upgraded": len(audit),
        "medium_edge_upgrades": len(audit),
        "recovered_boundary_edges": len(audit),
        "low_edges_after": sum(row["confidence_tier"] == "low" for row in edges),
        "medium_edges_after": sum(row["confidence_tier"] == "medium" for row in edges),
        "medium_high_edges_after": sum(row["confidence_tier"] == "medium-high" for row in edges),
        "high_edges_after": sum(row["confidence_tier"] == "high" for row in edges),
        "exportable_edges_after": sum(row["exportable"] == "true" for row in edges),
        "canonical_sql_materialization": False,
        "audit": str(AUDIT_PATH),
    }
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
