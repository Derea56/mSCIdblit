#!/usr/bin/env python3
"""Stage additional primary-study TF-target edges from the Module 22B hold review.

These are standalone, general TF-target assertions.  They add reusable target
evidence without upgrading the upstream ligand/receptor handoffs that led to
the named TF search.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import (
    EDGE_FIELDS,
    EVIDENCE_FIELDS,
    read_tsv,
    write_tsv,
)

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch003.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch003_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch003-2026-09-03"

UPDATES = [
    {
        "hold_edges": "M22B-E001359;M22B-E001360;M22B-E001361;M22B-E003552",
        "tf": "AR", "target": "TMPRSS2", "species": "human",
        "locator": "PMID:17679089",
        "context": "Human LNCaP and VCaP prostate-cancer models; DHT-responsive AR enhancer/promoter and chromatin-looping evidence; non-SCI comparator.",
        "summary": "Primary prostate-cancer experiments identified a noncanonical androgen-response element and AR occupancy in the TMPRSS2 regulatory region after DHT stimulation, with enhancer-promoter communication and androgen-dependent TMPRSS2 transcription.",
        "limitations": "The prostate-cell androgen model does not establish the reviewed DHT-metabolism handoffs or SCI-specific AR activation.",
    },
    {
        "hold_edges": "M22B-E001359;M22B-E001360;M22B-E001361;M22B-E003552",
        "tf": "AR", "target": "NKX3-1", "species": "human",
        "locator": "PMID:22083957; PMCID:PMC3255774",
        "context": "Human LNCaP prostate-cancer cells; AR/NKX3-1 ChIP-seq, ChIP-qPCR, and AR-silencing model; non-SCI comparator.",
        "summary": "AR and NKX3-1 were co-occupied at the NKX3-1 regulatory locus, and AR silencing reduced NKX3-1 expression in androgen-stimulated LNCaP cells, supporting direct AR regulation in a feed-forward prostate program.",
        "limitations": "The locus is prostate- and androgen-context dependent; this does not establish the reviewed DHT-metabolism handoffs or SCI-specific AR activation.",
    },
    {
        "hold_edges": "M22B-E001348;M22B-E001395;M22B-E001396",
        "tf": "NR1I2", "target": "CYP2B6", "species": "human",
        "locator": "PMID:11502872",
        "context": "Human primary hepatocyte and promoter-enhancer experiments; direct PXR/NR1I2 regulation of drug-metabolism gene; non-SCI comparator.",
        "summary": "Primary human hepatocyte and promoter studies showed that PXR/NR1I2 activates the CYP2B6 phenobarbital-responsive enhancer through PXR-RXR binding motifs, establishing direct CYP2B6 regulation.",
        "limitations": "The xenobiotic/hepatocyte context does not establish the reviewed DHEA- or estradiol-associated handoffs or SCI-specific PXR activation.",
    },
    {
        "hold_edges": "M22B-E001348;M22B-E001395;M22B-E001396;M22B-E004148",
        "tf": "NR1I2", "target": "CD36", "species": "mouse",
        "locator": "PMID:16556603",
        "context": "Mouse liver transgenic and PXR-null experiments with mouse Cd36 promoter analysis; direct PXR/NR1I2 target evidence; non-SCI comparator.",
        "summary": "Activated PXR was necessary and sufficient for hepatic Cd36 activation in transgenic and knockout mice, and promoter analysis identified a PXR response element in the mouse Cd36 promoter.",
        "limitations": "The hepatic lipid-metabolism model does not establish the reviewed DHEA/estradiol or Wnt1 handoffs or SCI-specific PXR activation.",
    },
    {
        "hold_edges": "M22B-E001362",
        "tf": "NR3C2", "target": "ATP1B1", "species": "human",
        "locator": "PMID:9694812; DOI:10.1074/jbc.273.33.20702",
        "context": "Human Na/K-ATPase beta1 promoter reporter and DNA-binding assays with mineralocorticoid receptor; non-SCI comparator.",
        "summary": "Primary promoter, mobility-shift, and transactivation experiments identified an MR/NR3C2-responsive element in the human ATP1B1 promoter and showed aldosterone-dependent MR activation of the promoter.",
        "limitations": "The receptor response is shared with glucocorticoid receptor and depends on steroid/cofactor context; this does not establish the reviewed DOC handoff or SCI-specific MR activation.",
    },
    {
        "hold_edges": "M22B-E001068;M22B-E001071",
        "tf": "RORA", "target": "CYP19A1", "species": "human",
        "locator": "PMID:19439415",
        "context": "Human MCF7/T47D breast-cancer cells with aromatase promoter reporter, in-vitro binding, and ChIP; non-SCI comparator.",
        "summary": "RORalpha/RORA increased CYP19A1 aromatase expression and promoter activity; promoter mutagenesis, in-vitro binding, and ChIP localized a functional ROR response element in the CYP19A1 promoter.",
        "limitations": "The breast-cancer estrogen/aromatase model is tissue-specific and does not establish the reviewed cholesterol-DHCR/LIPA handoffs or SCI-specific RORA activation.",
    },
    {
        "hold_edges": "M22B-E001068;M22B-E001071",
        "tf": "RORA", "target": "CYP2C8", "species": "human",
        "locator": "PMID:19164466; PMCID:PMC2670598",
        "context": "Human HepG2 cells and primary hepatocytes with promoter deletion/mutation, DNA-binding, expression, and knockdown assays; non-SCI comparator.",
        "summary": "RORalpha/RORA activated the human CYP2C8 promoter through a defined ROR response element, induced endogenous CYP2C8 transcripts, and loss of endogenous RORA reduced CYP2C8 expression.",
        "limitations": "The hepatic xenobiotic-metabolism model does not establish the reviewed cholesterol-DHCR/LIPA handoffs or SCI-specific RORA activation.",
    },
    {
        "hold_edges": "M22B-E001069;M22B-E001070;M22B-E001072",
        "tf": "RORC", "target": "CYP2C8", "species": "human",
        "locator": "PMID:19164466; PMCID:PMC2670598",
        "context": "Human HepG2 cells and primary hepatocytes with RORgamma/RORC promoter transactivation and endogenous-expression assays; non-SCI comparator.",
        "summary": "RORgamma/RORC overexpression transactivated the human CYP2C8 promoter through the ROR response element and increased endogenous CYP2C8 expression in human hepatocyte systems.",
        "limitations": "The hepatic model does not establish the reviewed cholesterol-DHCR/LIPA handoffs or SCI-specific RORC activation.",
    },
    {
        "hold_edges": "M22B-E001068;M22B-E001069;M22B-E001070;M22B-E001071;M22B-E001072",
        "tf": "RORA", "target": "Il17a", "species": "mouse",
        "locator": "PMID:18164222; PMCID:PMC2587175",
        "context": "Mouse Th17 differentiation and EL-4 promoter-reporter experiments; RORalpha/RORA binding and activation at the Il17 locus; EAE comparator, not SCI.",
        "summary": "Primary mouse Th17 studies showed RORalpha/RORA binding at a conserved ROR element in the Il17-Il17f locus, RORA-dependent chromatin effects, and enhanced IL-17 promoter reporter transcription.",
        "limitations": "The inflammatory comparator is experimental autoimmune encephalomyelitis rather than SCI, and RORA cooperates with RORC and stimulus-dependent cofactors; no SCI transfer is inferred.",
    },
    {
        "hold_edges": "M22B-E001068;M22B-E001069;M22B-E001070;M22B-E001071;M22B-E001072",
        "tf": "RORC", "target": "Il17a", "species": "mouse",
        "locator": "PMID:18164222; PMCID:PMC2587175",
        "context": "Mouse Th17 differentiation and EL-4 promoter-reporter experiments; RORgamma/RORC activation at the Il17 locus; EAE comparator, not SCI.",
        "summary": "The same primary mouse Th17 study showed RORgamma/RORC overexpression enhanced transcription from an IL-17 promoter reporter containing the conserved locus element, with synergistic RORA/RORC activity.",
        "limitations": "The inflammatory comparator is experimental autoimmune encephalomyelitis rather than SCI, and RORC acts with RORA and stimulus-dependent cofactors; no SCI transfer is inferred.",
    },
    {
        "hold_edges": "M22B-E005382",
        "tf": "ETV5", "target": "RET", "species": "human",
        "locator": "PMID:29321660; PMCID:PMC6168456",
        "context": "Human neuroblastoma cells and heterologous human promoter-reporter experiments with ETV5 ChIP-seq and ETV5 loss-of-function; non-SCI comparator.",
        "summary": "ETV5 loss reduced RET expression, ETV5 activated a human RET promoter reporter, and ETV5 ChIP-seq identified RET regulatory occupancy in neuroblastoma cells.",
        "limitations": "The neuroblastoma ERK-ETV5 context does not establish the reviewed Etv5-ErbB2 handoff or SCI-specific ETV5 activation.",
    },
    {
        "hold_edges": "M22B-E005382",
        "tf": "ETV5", "target": "TERT", "species": "human",
        "locator": "PMID:31452441; PMID:32518154",
        "context": "Human thyroid-cancer and fibroblast chromatinized-promoter models with ETV5 binding, reporter, and expression assays; non-SCI comparator.",
        "summary": "Primary experiments showed ETV5 binding to and stimulating the mutant human TERT promoter in thyroid-cancer cells; a separate chromatinized human TERT reporter and fibroblast study showed ETV5-dependent hTERT promoter activity and expression.",
        "limitations": "TERT activation is promoter-allele-, cofactor-, and cell-context dependent; this does not establish the reviewed Etv5-ErbB2 handoff or SCI-specific ETV5 activation.",
    },
    {
        "hold_edges": "M22B-E005382",
        "tf": "ETV5", "target": "TWIST1", "species": "human",
        "locator": "PMID:30265861",
        "context": "Human papillary-thyroid-cancer cells with ETV5 perturbation and promoter ChIP-qPCR; non-SCI comparator.",
        "summary": "ETV5 was required for and directly upregulated TWIST1 transcription in human papillary-thyroid-cancer cells, with ETV5 occupancy confirmed at the TWIST1 promoter.",
        "limitations": "The BRAF/MAPK thyroid-cancer model does not establish the reviewed Etv5-ErbB2 handoff or SCI-specific ETV5 activation.",
    },
    {
        "hold_edges": "M22B-E004148",
        "tf": "TCF4", "target": "CDX1", "species": "human",
        "locator": "PMID:12446687",
        "context": "Human Wnt/beta-catenin promoter-reporter experiments identifying TCF4/TCF7L2-dependent CDX1 activation; non-SCI comparator.",
        "summary": "Primary promoter experiments showed the TCF4E isoform of TCF7L2 cooperated with beta-catenin and p300 to activate the CDX1 promoter, establishing the TCF4 alias as a context-specific Wnt target regulator.",
        "limitations": "TCF4 here denotes the TCF7L2 protein alias, not the distinct TCF4/TCF7L2 naming ambiguity; activation requires beta-catenin and promoter context and does not establish the reviewed Wnt1-CD36 handoff or SCI activation.",
    },
    {
        "hold_edges": "M22B-E001808;M22B-E001809;M22B-E001827;M22B-E001828;M22B-E001848;M22B-E001849;M22B-E001858;M22B-E001859;M22B-E001870;M22B-E001871;M22B-E001902;M22B-E001903;M22B-E001918;M22B-E001919;M22B-E001935;M22B-E001936;M22B-E001952;M22B-E001953;M22B-E001969;M22B-E001970",
        "tf": "JUN", "target": "CCND1", "species": "human",
        "locator": "PMID:15282324; PMID:10500157; PMCID:PMC479712",
        "context": "Human breast-cancer/heterologous promoter studies with c-Jun/c-Fos/ER and CCND1 promoter assays; non-SCI comparator.",
        "summary": "Primary promoter studies showed c-Jun-containing complexes were recruited to a regulatory element in the human CCND1 locus and were required for estrogen-responsive CCND1 promoter activation in cooperation with c-Fos, ERalpha, and ATF2.",
        "limitations": "The activation is cooperative and hormone/cell-context dependent; it does not resolve the reviewed glutamate transporter-to-GRIK composite handoffs or SCI-specific Jun activation.",
    },
]


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

    for index, update in enumerate(UPDATES, start=11):
        pair = (update["species"].casefold(), update["tf"].casefold(), update["target"].casefold())
        if pair in existing_pairs:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id = f"M22B-E{edge_number:06d}"
        evidence_id = f"M22B-EVID-{evidence_number:06d}"
        edge_number += 1
        evidence_number += 1
        source_id = f"M22B-TARGET-SEARCH-{index:04d}"
        evidence_source_id = f"M22B-TARGET-SEARCH-EVID-{index:04d}"
        edges.append({
            "b_edge_id": edge_id,
            "source_entity": update["tf"],
            "relation_type": f"{update['tf']} activates the {update['target']} target gene in primary-study evidence",
            "target_entity": update["target"],
            "pathway_name": "target_gene",
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "source_a_edge_id": source_id,
            "edge_status": "reviewed_direct_target",
            "context_scope": update["context"],
            "cell_type_context": update["context"],
            "compartment_context": "unspecified",
            "species_context": update["species"],
            "injury_context": "not_assessed",
            "confidence_tier": "high",
            "export_priority": "medium",
            "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: standalone general TF-target edge found while reviewing {update['hold_edges']}; upstream handoff remains separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id,
            "source_a_evidence_id": evidence_source_id,
            "b_edge_ids": edge_id,
            "source_kind": "reviewed_direct_target",
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
            "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded.",
        })
        audit.append({
            "batch_id": BATCH_ID,
            "hold_edges_reviewed": update["hold_edges"],
            "tf": update["tf"], "target": update["target"], "species": update["species"],
            "b_edge_id": edge_id, "b_evidence_id": evidence_id,
            "source_locator": update["locator"],
            "upstream_handoff_upgraded": "false", "standalone_target_gene_edge": "true",
            "decision_basis": update["summary"],
        })
        existing_pairs.add(pair)

    audit_fields = [
        "batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id",
        "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis",
    ]
    write_tsv(AUDIT_PATH, audit, audit_fields)
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {
        "batch_id": BATCH_ID,
        "standalone_target_gene_edges_added": len(audit),
        "upstream_handoff_edges_upgraded": 0,
        "high_edges_after": sum(row["confidence_tier"] == "high" for row in edges),
        "exportable_edges_after": sum(row["exportable"] == "true" for row in edges),
        "target_gene_edges_after": sum(row["pathway_name"] == "target_gene" for row in edges),
        "upstream_activation_inferred": False,
        "audit": str(AUDIT_PATH),
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
