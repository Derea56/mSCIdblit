#!/usr/bin/env python3
"""Apply the first evidence-backed upgrade batch to Module 22B low edges.

This batch only updates rows whose exact edge and primary-source review are
already present in the local Phase-2 review record.  High is reserved for
direct TF occupancy/target or defined target-program evidence.  Medium is
used for exact-pair receptor/pathway or functional records that remain
bounded and do not establish a direct TF-target edge.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch001.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch001_summary.json"
DOC_PATH = ROOT / "docs/MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH001_2026-09-02.md"


PACKET = {
    "M22B-E000169": {
        "evidence_id": "M22B-EVID-000106",
        "new_edge_tier": "medium",
        "new_evidence_tier": "medium",
        "basis": "Primary chicken ovarian-theca study supports the asserted ESR2-associated CYP19A1 expression relationship, but does not establish ESR2-specific promoter occupancy; retain as bounded regulatory support.",
        "source_locator": "PMID:34710471; DOI:10.1016/j.ygcen.2021.113939",
    },
    "M22B-E000376": {
        "evidence_id": "M22B-EVID-000048",
        "old_target": "null",
        "old_status": "unresolved",
        "new_edge_tier": "high",
        "new_evidence_tier": "high",
        "new_target": "Nodal-responsive Smad2 direct-target program including foxa, klf3, notum1a, and smarcd3b",
        "new_relation": "SMAD2-associated Nodal direct-target program supported by ChIP-seq, ChIP-qPCR, and Nodal-response integration",
        "new_pathway": "target_module",
        "new_status": "reviewed_direct_target",
        "scope_suffix": "Supplemental primary evidence resolves a bounded Nodal/SMAD2 target program; the exact ACVR1C-ACVR2A/ACVR2B-CFC1 receptor composition and SCI transfer remain unresolved.",
        "basis": "Primary zebrafish study identifies Nodal-responsive Smad2-bound target genes with ChIP-seq, expression integration, and independent ChIP-qPCR; exact Gdf1 receptor usage and SCI transfer remain bounded.",
        "source_locator": "PMCID:PMC4206766; PMID:25277163; DOI:10.1186/s12915-014-0081-5; PMID:24798330",
    },
    "M22B-E000396": {
        "evidence_id": "M22B-EVID-000041",
        "old_target": "null",
        "old_status": "unresolved",
        "new_edge_tier": "high",
        "new_evidence_tier": "high",
        "new_target": "Msx1 basal promoter",
        "new_relation": "SMAD8-containing BMP-responsive complex regulates the Msx1 basal promoter",
        "new_pathway": "target_gene",
        "new_status": "reviewed_direct_target",
        "scope_suffix": "Supplemental primary evidence resolves a bounded SMAD8-containing Msx1 promoter complex; SMAD8-only specificity, exact BMP receptor composition, and SCI transfer remain unresolved.",
        "basis": "Primary mouse study supports a BMP-responsive SMAD8-containing promoter complex at Msx1 using consensus mutation, EMSA/supershift, reporter assays, and proteomic identification; this is not a SMAD8-only claim.",
        "source_locator": "PMCID:PMC1383672; PMID:16101586; DOI:10.1042/BJ20050327",
    },
    "M22B-E000412": {
        "evidence_id": "M22B-EVID-000035",
        "old_target": "null",
        "old_status": "unresolved",
        "new_edge_tier": "high",
        "new_evidence_tier": "high",
        "new_target": "IRF1 promoter",
        "new_relation": "IFN-gamma-associated STAT1 occupancy at the IRF1 promoter",
        "new_pathway": "target_gene",
        "new_status": "reviewed_direct_target",
        "scope_suffix": "Supplemental primary evidence resolves a bounded IFN-gamma/STAT1-to-IRF1 promoter record; receptor-complex and SCI transfer remain unresolved.",
        "basis": "Primary IFN-gamma-stimulated HeLa/ENCODE study maps STAT1 ChIP-seq occupancy to the IRF1 promoter GAS element with paired expression support; receptor-complex and SCI-transfer boundaries remain explicit.",
        "source_locator": "PMCID:PMC3623615; PMID:23645984; DOI:10.4137/GRSB.S11433; PMID:7777519",
    },
    "M22B-E000642": {
        "evidence_id": "M22B-EVID-004818",
        "new_edge_tier": "medium",
        "new_evidence_tier": "high",
        "basis": "Primary functional study supports S100A8-containing preparation activation of the Mac-1 ITGAM/ITGB2 complex and adhesion; monomer and beta-chain-only assignments remain unresolved.",
        "source_locator": "PMID:12626582; DOI:10.4049/jimmunol.170.6.3233",
    },
    "M22B-E000643": {
        "evidence_id": "M22B-EVID-004821",
        "new_edge_tier": "medium",
        "new_evidence_tier": "high",
        "basis": "Primary functional study supports S100A9-containing preparation activation of the Mac-1 ITGAM/ITGB2 complex and adhesion; monomer and beta-chain-only assignments remain unresolved.",
        "source_locator": "PMID:12626582; DOI:10.4049/jimmunol.170.6.3233",
    },
    "M22B-E000692": {
        "evidence_id": "M22B-EVID-004963",
        "new_edge_tier": "medium",
        "new_evidence_tier": "high",
        "basis": "Primary source supports the bounded Slit2-Robo1-CdGAP-Rac1/Cdc42 migration branch; Robo4 knockdown is not treated as proof that Robo4 is the transducing receptor.",
        "source_locator": "PMID:26713366; DOI:10.1016/j.bbrc.2015.12.075",
    },
    "M22B-E000693": {
        "evidence_id": "M22B-EVID-004970",
        "new_edge_tier": "medium",
        "new_evidence_tier": "high",
        "basis": "Primary source supports a bounded Slitrk3-PTPRD inhibitory-synapse differentiation program; no terminal TF-target claim is added.",
        "source_locator": "PMID:23345436; DOI:10.1038/ncomms3420",
    },
    "M22B-E000716": {
        "evidence_id": "M22B-EVID-005132",
        "new_edge_tier": "medium",
        "new_evidence_tier": "medium",
        "basis": "The reviewed aggregate supports the TL1A/TNFSF15-DR3/TNFRSF25 receptor program at moderate confidence; heterogeneous source composition prevents a high tier or direct TF claim.",
        "source_locator": "DOI:10.1016/S0960-9822(98)70204-0; PMID:11094155",
    },
    "M22B-E000773": {
        "evidence_id": "M22B-EVID-005627",
        "new_edge_tier": "medium",
        "new_evidence_tier": "high",
        "basis": "Primary mouse P19-cell study supports the exact WNT11-FZD4 cell-associated interaction, PKC relay, and cardiomyocyte differentiation output; no terminal TF claim is added.",
        "source_locator": "PMID:21041481; PMCID:PMC3019854",
    },
    "M22B-E000774": {
        "evidence_id": "M22B-EVID-005630",
        "new_edge_tier": "medium",
        "new_evidence_tier": "high",
        "basis": "Primary melanoma study supports the exact WNT11-FZD7-DAAM1-Rho-ROCK pathway and invasion/metastasis output; tumor-context and no-terminal-TF limits remain.",
        "source_locator": "PMID:33082334; PMCID:PMC7575593; DOI:10.1038/s41467-020-18951-2",
    },
    "M22B-E000781": {
        "evidence_id": "M22B-EVID-005758",
        "new_edge_tier": "medium",
        "new_evidence_tier": "high",
        "basis": "Primary studies support WNT5A-FZD5 direct binding and receptor-dependent functional outputs; high-concentration SPR, cancer/stem-like-cell context, and no-terminal-TF limits remain.",
        "source_locator": "PMID:29930766; PMCID:PMC6007469; PMID:35295855; PMCID:PMC8919396",
    },
    "M22B-E000783": {
        "evidence_id": "M22B-EVID-005764",
        "new_edge_tier": "medium",
        "new_evidence_tier": "high",
        "basis": "Primary study supports WNT5A-RYK direct binding and receptor-dependent apoptosis/proliferation output; concentration and separate FZD5-scope limits remain.",
        "source_locator": "PMID:29930766; PMCID:PMC6007469; DOI:10.18632/oncotarget.25551",
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
    "batch_id", "b_edge_id", "b_evidence_id", "old_edge_confidence", "new_edge_confidence",
    "old_evidence_confidence", "new_evidence_confidence", "old_target", "new_target",
    "old_edge_status", "new_edge_status", "decision_basis", "source_locator",
    "module22b_register_changed", "canonical_sql_materialization",
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
    audit: list[dict[str, str]] = []

    for edge_id, spec in PACKET.items():
        edge = edge_by_id.get(edge_id)
        ev = evidence_by_id.get(spec["evidence_id"])
        if edge is None or ev is None:
            raise SystemExit(f"missing packet row: {edge_id} / {spec['evidence_id']}")
        if edge["confidence_tier"] not in {"low", spec["new_edge_tier"]}:
            raise SystemExit(f"{edge_id}: expected low or already-upgraded edge confidence, found {edge['confidence_tier']!r}")
        if edge["exportable"] != "true":
            raise SystemExit(f"{edge_id}: expected exportable=true")
        if edge_id not in (ev.get("b_edge_ids") or "").split(";"):
            raise SystemExit(f"{spec['evidence_id']}: not linked to {edge_id}")
        old_edge = dict(edge)
        old_ev = dict(ev)
        edge["confidence_tier"] = spec["new_edge_tier"]
        edge["consolidation_note"] = append_once(
            edge["consolidation_note"],
            f"Low-confidence upgrade batch001: {spec['new_edge_tier']} after exact primary-source re-review.",
        )
        for key, field in (("new_target", "target_entity"), ("new_relation", "relation_type"), ("new_pathway", "pathway_name"), ("new_status", "edge_status")):
            if key in spec:
                edge[field] = spec[key]
        ev["confidence_tier"] = spec["new_evidence_tier"]
        ev["source_locator"] = spec["source_locator"]
        ev["evidence_summary"] = spec["basis"]
        ev["limitations"] = edge["context_scope"]
        if "scope_suffix" in spec:
            edge["context_scope"] = append_once(edge["context_scope"], spec["scope_suffix"])
            ev["limitations"] = edge["context_scope"]
        ev["consolidation_note"] = append_once(
            ev["consolidation_note"],
            f"Low-confidence upgrade batch001: {spec['new_evidence_tier']} source re-adjudication; edge tier remains bounded by layer and exactness.",
        )
        audit.append({
            "batch_id": "module22b-low-confidence-upgrade-batch001-2026-09-02",
            "b_edge_id": edge_id,
            "b_evidence_id": spec["evidence_id"],
            # The packet is defined against the pre-batch register.  Keep the
            # audit stable when the script is rerun idempotently after the
            # rows have already been upgraded.
            "old_edge_confidence": "low",
            "new_edge_confidence": edge["confidence_tier"],
            "old_evidence_confidence": "",
            "new_evidence_confidence": ev["confidence_tier"],
            "old_target": spec.get("old_target", old_edge["target_entity"]),
            "new_target": edge["target_entity"],
            "old_edge_status": spec.get("old_status", old_edge["edge_status"]),
            "new_edge_status": edge["edge_status"],
            "decision_basis": spec["basis"],
            "source_locator": spec["source_locator"],
            "module22b_register_changed": "true",
            "canonical_sql_materialization": "false",
        })

    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    write_tsv(AUDIT_PATH, audit, AUDIT_FIELDS)
    counts = {
        "batch_id": "module22b-low-confidence-upgrade-batch001-2026-09-02",
        "records_upgraded": len(audit),
        "high_edge_upgrades": sum(r["new_edge_confidence"] == "high" for r in audit),
        "medium_edge_upgrades": sum(r["new_edge_confidence"] == "medium" for r in audit),
        "low_edges_before": sum(r["confidence_tier"] == "low" for r in edges) + len(audit),
        "low_edges_after": sum(r["confidence_tier"] == "low" for r in edges),
        "high_edges_after": sum(r["confidence_tier"] == "high" for r in edges),
        "medium_edges_after": sum(r["confidence_tier"] == "medium" for r in edges),
        "exportable_edges_after": sum(r["exportable"] == "true" for r in edges),
        "canonical_sql_materialization": False,
        "audit": str(AUDIT_PATH),
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(counts, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Module 22B low-confidence upgrade batch 001 — 2026-09-02",
        "",
        "This batch re-adjudicates exact low-tier Module 22B rows against the",
        "repository's primary-source Phase-2 review records. It promotes only",
        "bounded direct TF/program records to high and exact receptor/pathway or",
        "functional records to medium. It does not create canonical SQL rows.",
        "",
        "## Result",
        "",
        f"- Rows upgraded: {len(audit):,}",
        f"- High edge upgrades: {counts['high_edge_upgrades']:,}",
        f"- Medium edge upgrades: {counts['medium_edge_upgrades']:,}",
        f"- Exact low edges before: {counts['low_edges_before']:,}",
        f"- Exact low edges after: {counts['low_edges_after']:,}",
        f"- High edges after: {counts['high_edges_after']:,}",
        f"- Medium edges after: {counts['medium_edges_after']:,}",
        f"- Exportable edges after: {counts['exportable_edges_after']:,}",
        "- Canonical SQL materialization: false",
        "",
        "## Boundaries",
        "",
        "High rows are direct TF occupancy/target or defined target-program",
        "records in the cited comparator systems. Medium rows are usable",
        "exact-pair receptor/pathway or functional records but are not direct",
        "TF-target evidence. Receptor-complex substitutions, model transfer,",
        "species transfer, and SCI transfer remain explicitly bounded.",
        "",
        "Rows with explicit negative evidence, wrong-direction or wrong-pair",
        "evidence, disputed binding, non-native constructs, or no terminal TF",
        "remain low and were not force-promoted.",
        "",
        "## Reproduction",
        "",
        "- Generator: `scripts/promote_module22b_low_confidence_batch001.py`",
        "- Audit ledger: `work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch001.tsv`",
        "",
    ]
    DOC_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(counts, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
