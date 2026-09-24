#!/usr/bin/env python3
"""Append a bounded primary-evidence JAK-to-STAT handoff batch.

The existing Module 21B registers contain many receptor-to-JAK and
receptor-to-STAT records.  This batch connects only pathway-specific kinase
and STAT readouts that are jointly supported by the cited primary study.  The
edges are ``supports`` pathway-handoff records, not claims of a universal
binary kinase-substrate reaction.  They are intentionally kept in the source
register so the normal graph exporter and provenance audit retain them.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module21b/module21b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module21b/module21b_evidence_register.tsv"


COMMON_LIMITATIONS = (
    "Pathway-handoff evidence from primary cellular signaling assays; this does not assert "
    "a purified binary kinase-substrate reaction, direct catalytic phosphorylation order, "
    "terminal transcription, or SCI receiver-cell transfer."
)


HANDOFFS = [
    # Common-gamma cytokine families with explicit primary JAK/STAT readouts.
    ("JAK1/JAK3", "STAT3", "IL2-JAK1-JAK3-STAT3-relay", "PMID:7568001", "IL-2-responsive human T lymphocytes showed JAK1/JAK3 and STAT3 activation in the intermediate-affinity IL2Rbeta:IL2RG signaling core."),
    ("JAK1/JAK3", "STAT1", "IL21-IL21R-IL2RG-STAT1-relay", "PMID:11418623", "IL-21 receptor/gamma-chain reconstitution supported JAK1/JAK3-associated STAT1 activation."),
    ("JAK1/JAK3", "STAT3", "IL21-IL21R-IL2RG-STAT3-relay", "PMID:11418623", "IL-21 receptor/gamma-chain signaling supported JAK1/JAK3-associated STAT3 activation in receptor-reconstituted lymphoid systems."),
    ("JAK1/JAK3", "STAT5", "IL21-IL21R-IL2RG-STAT5-relay", "PMID:11418623", "IL-21 receptor/gamma-chain signaling supported JAK1/JAK3-associated STAT5 activation in gamma-chain-restored lymphoid systems."),
    ("JAK1", "STAT5", "IL7-IL7RA-IL2RG-JAK1-JAK3-STAT5-relay", "PMID:7489741; PMCID:PMC2865298", "IL-7 stimulation supported JAK1-associated STAT5 recruitment/phosphorylation in primary human and corroborating murine T-cell systems."),
    ("JAK3", "STAT5", "IL7-IL7RA-IL2RG-JAK1-JAK3-STAT5-relay", "PMID:7489741; PMCID:PMC2865298", "IL-7 stimulation supported JAK3-associated STAT5 recruitment/phosphorylation in primary human and corroborating murine T-cell systems."),
    ("JAK1", "STAT3", "IL15-IL15RA-IL2RB-IL2RG-JAK1-JAK3-STAT3-STAT5-relay", "PMID:7568001", "IL-15 stimulation in human T cells jointly measured JAK1 and STAT3 tyrosine phosphorylation and DNA-binding activation."),
    ("JAK3", "STAT3", "IL15-IL15RA-IL2RB-IL2RG-JAK1-JAK3-STAT3-STAT5-relay", "PMID:7568001", "IL-15 stimulation in human T cells jointly measured JAK3 and STAT3 tyrosine phosphorylation and DNA-binding activation."),
    ("JAK1", "STAT5", "IL15-IL15RA-IL2RB-IL2RG-JAK1-JAK3-STAT3-STAT5-relay", "PMID:7568001", "IL-15 stimulation in human T cells jointly measured JAK1 and STAT5 tyrosine phosphorylation and DNA-binding activation."),
    ("JAK3", "STAT5", "IL15-IL15RA-IL2RB-IL2RG-JAK1-JAK3-STAT3-STAT5-relay", "PMID:7568001", "IL-15 stimulation in human T cells jointly measured JAK3 and STAT5 tyrosine phosphorylation and DNA-binding activation."),
    ("JAK1", "STAT1", "IL9-IL9Ralpha-IL2RG-JAK1-JAK3-STAT1-STAT3-STAT5-relay", "PMID:9535918", "IL-9 receptor/gamma-chain reconstitution supported JAK1-associated STAT1 activation in human and murine cell-line systems."),
    ("JAK3", "STAT1", "IL9-IL9Ralpha-IL2RG-JAK1-JAK3-STAT1-STAT3-STAT5-relay", "PMID:9535918", "IL-9 receptor/gamma-chain reconstitution supported JAK3-associated STAT1 activation in human and murine cell-line systems."),
    ("JAK1", "STAT3", "IL9-IL9Ralpha-IL2RG-JAK1-JAK3-STAT1-STAT3-STAT5-relay", "PMID:9535918", "IL-9 receptor/gamma-chain reconstitution supported JAK1-associated STAT3 activation in human and murine cell-line systems."),
    ("JAK3", "STAT3", "IL9-IL9Ralpha-IL2RG-JAK1-JAK3-STAT1-STAT3-STAT5-relay", "PMID:9535918", "IL-9 receptor/gamma-chain reconstitution supported JAK3-associated STAT3 activation in human and murine cell-line systems."),
    ("JAK1", "STAT5", "IL9-IL9Ralpha-IL2RG-JAK1-JAK3-STAT1-STAT3-STAT5-relay", "PMID:9535918", "IL-9 receptor/gamma-chain reconstitution supported JAK1-associated STAT5 activation in human and murine cell-line systems."),
    ("JAK3", "STAT5", "IL9-IL9Ralpha-IL2RG-JAK1-JAK3-STAT1-STAT3-STAT5-relay", "PMID:9535918", "IL-9 receptor/gamma-chain reconstitution supported JAK3-associated STAT5 activation in human and murine cell-line systems."),
    # Additional cytokine receptor families already represented by both sides.
    ("JAK2", "STAT5", "IL5-IL5R-JAK2-STAT5-relay", "PMID:9363920; PMID:7539031", "IL-5 receptor-bearing hematopoietic and eosinophil systems jointly support JAK2 activation and STAT5 activation."),
    ("JAK1", "STAT1", "IFN-type-II-JAK-STAT", "PMID:7673114", "The IFN-gamma receptor complex study supports JAK1 activation together with STAT1 activation in the receptor signaling pathway."),
    ("JAK2", "STAT1", "IFN-type-II-JAK-STAT", "PMID:7673114; PMID:9343425", "The IFN-gamma receptor complex and JAK2-dependence studies support JAK2-associated STAT1 activation in the type-II interferon pathway."),
    ("JAK1", "STAT6", "IL4-type-I-receptor-JAK1-JAK3-STAT6-relay", "PMID:8887542; PMID:9190938", "Type-I IL-4 receptor studies support JAK1-associated STAT6 activation in IL-4-responsive lymphoid systems."),
    ("JAK3", "STAT6", "IL4-type-I-receptor-JAK1-JAK3-STAT6-relay", "PMID:8887542; PMID:9190938", "Type-I IL-4 receptor studies support JAK3-associated STAT6 activation in IL-4-responsive lymphoid systems."),
    ("JAK1", "STAT3", "IL10-IL10R-JAK1-STAT3-relay", "PMID:8910398; PMID:10347215", "IL-10 receptor-tail and macrophage studies support JAK1-associated STAT3 activation and IL-10 response."),
    ("JAK1", "STAT3", "IL6R-gp130-JAK1-STAT3-relay", "PMID:7624343; PMID:9794795", "IL-6 receptor/gp130 studies support receptor-associated JAK1 activation followed by STAT3 phosphorylation and recruitment."),
    ("JAK2", "STAT3", "IL6R-gp130-JAK2-STAT3-relay", "PMID:7537214; PMID:9794795", "IL-6 receptor/gp130 studies support parallel JAK2 activation with the STAT3 receptor-complex output."),
    ("JAK2", "STAT3", "IL23-receptor-JAK2-STAT3-relay", "PMID:12023369", "IL-23 receptor reconstitution supports JAK2 association/activation with STAT3-predominant signaling."),
    ("JAK2", "STAT4", "IL23-receptor-JAK2-STAT4-relay", "PMID:12023369", "IL-23 receptor reconstitution supports a weaker JAK2-associated STAT4 signaling branch alongside STAT3."),
    ("JAK1", "STAT3", "LIF-gp130-JAK1-STAT3-relay", "PMID:22939972", "Primary LIF stimulation studies in cardiac myocytes measured JAK1 activation together with STAT3 activation and STAT3 Y705 phosphorylation."),
    ("JAK1", "STAT3", "OSM-gp130-JAK1-STAT3-relay", "PMID:8625884", "Primary OSM stimulation studies measured JAK1 and STAT3 tyrosine phosphorylation in human and murine osteoblast-lineage systems."),
    ("JAK2", "STAT3", "OSM-gp130-JAK2-STAT3-relay", "PMID:8625884", "Primary OSM stimulation studies measured JAK2 and STAT3 tyrosine phosphorylation in human and murine osteoblast-lineage systems."),
    ("TYK2", "STAT3", "OSM-gp130-TYK2-STAT3-relay", "PMID:8625884", "Primary OSM stimulation studies measured TYK2 and STAT3 tyrosine phosphorylation in human and murine osteoblast-lineage systems."),
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


def next_number(path: Path, field: str, pattern: str) -> int:
    values: list[int] = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            match = re.fullmatch(pattern, row[field])
            if match:
                values.append(int(match.group(1)))
    return max(values, default=0) + 1


def append_rows(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        for row in rows:
            writer.writerow(row)


def main() -> None:
    with EDGE_PATH.open(newline="", encoding="utf-8") as handle:
        existing_edges = list(csv.DictReader(handle, delimiter="\t"))
    with EVIDENCE_PATH.open(newline="", encoding="utf-8") as handle:
        existing_evidence = list(csv.DictReader(handle, delimiter="\t"))

    existing_keys = {
        (row["source_entity"], row["relation_type"], row["target_entity"], row["pathway_name"])
        for row in existing_edges
    }
    edge_number = next_number(EDGE_PATH, "b_edge_id", r"M21B-E(\d+)")
    evidence_number = next_number(EVIDENCE_PATH, "b_evidence_id", r"M21B-EVID-(\d+)")
    new_edges: list[dict[str, str]] = []
    new_evidence: list[dict[str, str]] = []

    for source, target, pathway, locator, summary in HANDOFFS:
        key = (source, "supports", target, pathway)
        if key in existing_keys:
            continue
        edge_id = f"M21B-E{edge_number:06d}"
        evidence_id = f"M21B-EVID-{evidence_number:06d}"
        edge_number += 1
        evidence_number += 1
        existing_keys.add(key)
        context = "primary cytokine receptor signaling systems; pathway-specific JAK and STAT readouts"
        note = (
            "Primary-supported pathway handoff; retained as traversable evidence without asserting "
            "a universal binary kinase-substrate edge. " + COMMON_LIMITATIONS
        )
        new_edges.append({
            "b_edge_id": edge_id,
            "source_entity": source,
            "relation_type": "supports",
            "target_entity": target,
            "pathway_name": pathway,
            "evidence_layer": "receptor_proximal_or_pathway;downstream_or_functional",
            "source_a_edge_id": "",
            "edge_status": "validated_primary_pathway_handoff",
            "context_scope": "Primary pathway handoff; exact kinase/STAT context bounded",
            "cell_type_context": context,
            "compartment_context": "cytoplasmic kinase-to-STAT signaling handoff",
            "species_context": "human; mouse comparator where stated in the primary record",
            "injury_context": "no SCI transfer inferred; primary model context only",
            "confidence_tier": "high",
            "export_priority": "medium",
            "exportable": "true",
            "consolidation_note": note,
        })
        new_evidence.append({
            "b_evidence_id": evidence_id,
            "source_a_evidence_id": "",
            "b_edge_ids": edge_id,
            "source_kind": "primary_article",
            "source_locator": locator,
            "support_kind": "direct_primary_mechanism",
            "species_support": "human; mouse comparator where stated in the primary record",
            "source_scope": "pathway_membership",
            "confidence_tier": "high",
            "citation_note": f"Primary literature locator(s): {locator}; pathway-specific handoff record.",
            "evidence_summary": summary,
            "limitations": COMMON_LIMITATIONS,
            "evidence_layer": "receptor_proximal_or_pathway;downstream_or_functional",
            "exportable": "true",
            "consolidation_note": note,
        })

    append_rows(EDGE_PATH, EDGE_FIELDS, new_edges)
    append_rows(EVIDENCE_PATH, EVIDENCE_FIELDS, new_evidence)
    print({"edges_added": len(new_edges), "evidence_added": len(new_evidence)})


if __name__ == "__main__":
    main()
