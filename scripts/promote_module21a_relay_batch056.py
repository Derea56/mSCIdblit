#!/usr/bin/env python3
"""Promote independently verified Module 21A receptor-activation packets."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
DETAIL = RELAY / "module21a_pair_relay_evidence_detail.tsv"
REUSE = RELAY / "module21a_pathway_reuse_registry.tsv"
PAIRS = RELAY / "module21a_all_pair_relay_coverage.tsv"
REVIEW_FILES = [
    RELAY / "module21a_pair_relay_review_batches028_029.tsv",
    RELAY / "module21a_pair_relay_review_batches032_033_034_035.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch056.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch056_summary.json"

PACKET = {
    "M21A-PAIR-EVID-562": (
        "5-ht-tph1_slc18a1 htr1a", "M21A-REUSE-0303", "M20A-CELLCHAT-REMAINING-0029",
        "PMID:1436121; DOI:10.1007/BF00171076; PMID:1448178",
        "5-HT-dependent HTR1A inhibition of adenylyl cyclase with pertussis-toxin-sensitive Gi/o placement supports qualified-high promotion at the receptor-proximal relay layer. Preserve recombinant human-receptor and rat/mouse cell contexts, with Ca2+/PLC and ERK branches treated as context-dependent; no terminal TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-564": (
        "5-ht-tph1_slc18a1 htr1d", "M21A-REUSE-0305", "M20A-CELLCHAT-REMAINING-0031",
        "PMID:8878051; DOI:10.1007/BF00171052; PMID:8717154; DOI:10.1007/BF00168751",
        "Direct HTR1D pharmacology, Gi/o-linked inhibition of forskolin-stimulated cAMP, antagonist blockade, and receptor-dependent growth output support qualified-high promotion. Preserve human HTR1D expression and C6-glial/NIH-3T3/Y-1 model boundaries; growth is a function readout rather than a terminal-TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-565": (
        "5-ht-tph1_slc18a1 htr1e", "M21A-REUSE-0306", "M20A-CELLCHAT-REMAINING-0032",
        "PMID:7984278; DOI:10.1016/0028-3908(94)90070-1; PMCID:PMC46050",
        "Direct 5-HT/HTR1E coupling to Gi/o-linked adenylyl-cyclase inhibition supports qualified-high promotion at the receptor-proximal relay layer. Preserve human HTR1E and transfected-cell context, limited native rodent expression, and receptor-density-dependent alternate coupling; no terminal TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-566": (
        "5-ht-tph1_slc18a1 htr1f", "M21A-REUSE-0307", "M20A-CELLCHAT-REMAINING-0033",
        "PMID:8380639; PMCID:PMC45671; DOI:10.1073/pnas.90.2.408",
        "High-affinity 5-HT binding and dose-dependent inhibition of forskolin-stimulated cAMP at cloned human HTR1F support qualified-high promotion at the Gi/o/adenylyl-cyclase receptor-proximal relay layer. Preserve recombinant-cell and human brain-expression context; no terminal TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-567": (
        "5-ht-tph1_slc18a1 htr2a", "M21A-REUSE-0308", "M20A-CELLCHAT-REMAINING-0034",
        "PMID:10498829; PMID:20717650; DOI:10.1016/j.neuroscience.2010.06.052; PMCID:PMC3380724; DOI:10.1186/1471-2202-13-25",
        "Direct HTR2A stimulation with Gq/11-PLC-Ca2+/calmodulin and receptor-dependent ERK readouts supports qualified-high promotion at the receptor-proximal relay/function layer. Preserve recombinant HTR2A and rodent cell contexts and the use of DOI in some downstream experiments; no terminal TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-568": (
        "5-ht-tph1_slc18a1 htr2b", "M21A-REUSE-0309", "M20A-CELLCHAT-REMAINING-0035",
        "PMID:10498829; PMID:11930908; DOI:10.1023/A:1014862808126",
        "Direct 5-HT-dependent HTR2B Ca2+ signaling and receptor-linked astrocyte glycogenolytic function support qualified-high promotion at the Gq/11-PLC-Ca2+ relay/function layer. Preserve human recombinant HTR2B versus primary mouse astrocyte contexts and no terminal TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-569": (
        "5-ht-tph1_slc18a1 htr2c", "M21A-REUSE-0310", "M20A-CELLCHAT-REMAINING-0036",
        "PMID:10498829; PMCID:PMC3380724; DOI:10.1186/1471-2202-13-25",
        "Direct 5-HT-dependent HTR2C Ca2+ and ERK signaling supports qualified-high promotion at the Gq/11-PLC receptor-proximal relay layer. Preserve recombinant HTR2C and mouse/rat comparator contexts and no terminal TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-650": (
        "ach-chat_slc10a4 chrna7", "M21A-REUSE-0390", "M20A-CELLCHAT-REMAINING-0117",
        "PMID:20100906; PMCID:PMC2872959; DOI:10.1124/jpet.109.164566; PMID:16184187; PMCID:PMC1751230; DOI:10.1038/sj.bjp.0706403",
        "Direct ACh activation of the alpha7 homomeric nicotinic receptor and rapid cation/Ca2+ influx support qualified-high promotion at the receptor-proximal ion-channel activation layer. Preserve mouse/human receptor expression in Xenopus oocytes, homomeric assembly and desensitization context, and the untested CHAT/SLC10A4 release branch; no terminal TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-661": (
        "ach-chat_slc5a7 chrm1", "M21A-REUSE-0401", "M20A-CELLCHAT-REMAINING-0128",
        "PMID:11181437; PMCID:PMC1572629; DOI:10.1038/sj.bjp.0703892; PMID:8382764; DOI:10.1016/0024-3205(93)90303-K",
        "Human M1 receptor activation with Gq/11 coupling and phosphoinositide turnover supports qualified-high promotion at the muscarinic receptor-proximal relay layer. Preserve recombinant CHO context and methacholine/standard agonist semantics; endogenous CHAT/SLC5A7 release and terminal TF were not tested.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-662": (
        "ach-chat_slc5a7 chrm2", "M21A-REUSE-0402", "M20A-CELLCHAT-REMAINING-0129",
        "PMID:11181437; PMCID:PMC1572629; DOI:10.1038/sj.bjp.0703892; PMID:11250872; PMCID:PMC1572666",
        "Human M2 receptor activation with direct Gi/o-linked cAMP inhibition supports qualified-high promotion at the receptor-proximal relay layer. Preserve the high-receptor-density Gs component as context-dependent and retain recombinant CHO/agonist boundaries; no terminal TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-663": (
        "ach-chat_slc5a7 chrm3", "M21A-REUSE-0403", "M20A-CELLCHAT-REMAINING-0130",
        "PMID:11181437; PMCID:PMC1572629; DOI:10.1038/sj.bjp.0703892; PMID:8441327",
        "Human M3 receptor activation with Gq/11 coupling and phosphoinositide signaling supports qualified-high promotion at the receptor-proximal relay layer. Preserve recombinant CHO/agonist context, and do not infer endogenous ACh release or a terminal TF.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-664": (
        "ach-chat_slc5a7 chrm4", "M21A-REUSE-0404", "M20A-CELLCHAT-REMAINING-0131",
        "PMID:11181437; PMCID:PMC1572629; DOI:10.1038/sj.bjp.0703892; PMID:8441327",
        "Human M4 receptor activation with Gi/o coupling and adenylyl-cyclase inhibition supports qualified-high promotion at the receptor-proximal relay layer. Preserve recombinant CHO/agonist context and no endogenous ACh-release or terminal-TF inference.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-668": (
        "ach-chat_slc5a7 chrn_a3b4", "M21A-REUSE-0408", "M20A-CELLCHAT-REMAINING-0135",
        "PMID:9104590; DOI:10.1111/j.1460-9568.1997.tb01625.x; PMID:25180076",
        "Direct ACh-evoked currents through the complete alpha3beta4 nicotinic receptor support qualified-high promotion at the ligand-gated receptor activation layer. Preserve heterologous receptor-complex and antagonist/pharmacology context; no CHAT/SLC5A7 release or terminal TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-669": (
        "ach-chat_slc5a7 chrn_a4b2", "M21A-REUSE-0409", "M20A-CELLCHAT-REMAINING-0136",
        "PMID:8987816; DOI:10.1016/S0006-8993(96)01158-0; PMID:9104590; DOI:10.1111/j.1460-9568.1997.tb01625.x",
        "Direct ACh-evoked currents and nicotine/Ca2+ responses through the complete alpha4beta2 nicotinic receptor support qualified-high promotion at the ligand-gated receptor activation layer. Preserve heterologous receptor-complex context and no CHAT/SLC5A7 release or terminal TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-670": (
        "ach-chat_slc5a7 chrna7", "M21A-REUSE-0410", "M20A-CELLCHAT-REMAINING-0137",
        "PMID:22593058; PMCID:PMC3387736; PMID:24349346; PMCID:PMC3857818",
        "Alpha7-dependent Ca2+ responses with alpha-bungarotoxin blockade/knockout and CaMKII/PLC/IP3R perturbation support qualified-high promotion at the receptor-proximal ion-channel/function layer. Preserve rat interneuron and choline/nicotine stimulation context; endogenous ACh release and terminal TF were not tested.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-681": (
        "ado-nt5e_slc29a1 adora1", "M21A-REUSE-0418", "M20A-CELLCHAT-REMAINING-0148",
        "PMID:19244482; DOI:10.1152/ajpcell.00290.2008; PMID:15302686; PMCID:PMC1575922",
        "Adenosine-linked A1 receptor Gi/o signaling with adenylyl-cyclase inhibition supports qualified-high promotion at the receptor-proximal relay layer. Preserve weak/context-dependent A1 coupling, selective-analogue use, adult rat cardiac-fibroblast and recombinant-receptor contexts, and the untested NT5E/SLC29A1 metabolism branch; no terminal TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-682": (
        "ado-nt5e_slc29a1 adora2a", "M21A-REUSE-0419", "M20A-CELLCHAT-REMAINING-0149",
        "PMID:14751870; PMID:16429616; PMCID:PMC1325961; PMID:19244482",
        "Adenosine/A2A stimulation with Gs-cAMP signaling, receptor-linked ERK output, pharmacologic pathway perturbation, and Schwann-cell function support qualified-high promotion at the receptor-proximal relay/function layer. Preserve rat cardiac-fibroblast, Schwann-cell, and recombinant contexts, selective-agonist boundaries, and no terminal TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-683": (
        "ado-nt5e_slc29a1 adora2b", "M21A-REUSE-0420", "M20A-CELLCHAT-REMAINING-0150",
        "PMID:15862176; PMID:26416848; PMID:24383849; PMCID:PMC3909477",
        "Adenosine/A2B receptor-linked Gs-cAMP/ERK-Akt function with A2B perturbation supports qualified-high promotion at the receptor-proximal relay/function layer. Preserve human, bovine, and rat tissue contexts, use of NECA/2-chloroadenosine in some assays, and CREB as a measured phosphorylation endpoint rather than a terminal TF claim.",
        "reviewed_relay_candidate",
    ),
}

PROMOTION_NOTE = (
    "Module 21A relay/function promotion batch056 (2026-09-02): evidence tier raised to high for the exact, context-bounded receptor activation/relay packet; upstream Module 20A confidence, evidence-layer scope, terminal-TF status, and SCI transfer remain unchanged."
)


def read_tsv(path: Path):
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path: Path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def index(rows, key):
    result = {}
    for row in rows:
        value = row.get(key, "")
        if value and value in result:
            raise SystemExit(f"duplicate {key}: {value}")
        if value:
            result[value] = row
    return result


def append_once(value, note):
    return value if note in value else f"{value} {note}".strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    detail_fields, detail_rows = read_tsv(DETAIL)
    reuse_fields, reuse_rows = read_tsv(REUSE)
    pair_fields, pair_rows = read_tsv(PAIRS)
    review_tables = [read_tsv(path) for path in REVIEW_FILES]
    review_fields = [fields for fields, _ in review_tables]
    review_rows_by_file = [rows for _, rows in review_tables]
    detail = index(detail_rows, "evidence_id")
    reuse = index(reuse_rows, "pathway_reuse_key")
    reviews = index([row for rows in review_rows_by_file for row in rows], "review_id")
    coverage = {
        evidence_id: next(
            (row for row in pair_rows if row.get("module21a_evidence_ids") == evidence_id), None
        )
        for evidence_id in PACKET
    }

    for evidence_id, (pair_key, reuse_key, review_id, citations, _basis, review_status) in PACKET.items():
        row = detail.get(evidence_id)
        if (
            row is None
            or row.get("confidence_tier") not in {"medium", "medium-high"}
            or row.get("pathway_reuse_key") != reuse_key
            or row.get("source_locators") != citations
        ):
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        if not any(layer in row.get("evidence_layer", "") for layer in ("receptor_proximal_relay", "ligand_receptor_binding_or_activation")):
            raise SystemExit(f"{evidence_id} lacks activation or receptor-proximal layer")
        review = reviews.get(review_id)
        if (
            review is None
            or review.get("evidence_id") != evidence_id
            or review.get("pair_key") != pair_key
            or review.get("source_locators") != citations
            or review.get("confidence_tier") not in {"medium", "medium-high"}
            or review.get("review_status") != review_status
        ):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        if coverage[evidence_id] is None or coverage[evidence_id].get("pair_key") != pair_key or coverage[evidence_id].get("module21a_status") != review_status:
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")

    audit_fields = [
        "evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier",
        "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged",
        "terminal_tf_status_unchanged", "sql_materialization",
    ]
    audit_rows = [
        {
            "evidence_id": evidence_id,
            "review_id": packet[2],
            "pair_key": packet[0],
            "pathway_reuse_key": packet[1],
            "previous_tier": detail[evidence_id]["confidence_tier"],
            "new_tier": "high",
            "source_locators": detail[evidence_id]["source_locators"],
            "decision_basis": packet[4],
            "upstream_lr_confidence_unchanged": "true",
            "terminal_tf_status_unchanged": "true",
            "sql_materialization": "false",
        }
        for evidence_id, packet in sorted(PACKET.items())
    ]
    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return

    for evidence_id, packet in PACKET.items():
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        review = reviews[packet[2]]
        review["confidence_tier"] = "high"
        review["curator_note"] = append_once(review["curator_note"], PROMOTION_NOTE)
        reuse[packet[1]]["validation_status"] = "promoted_high_batch056"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage[evidence_id]["curator_notes"] = append_once(coverage[evidence_id]["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(
        json.dumps(
            {
                "promotion_id": "module21a-relay-function-batch056-2026-09-02",
                "records_promoted": len(audit_rows),
                "evidence_ids": sorted(PACKET),
                "promotion_note": PROMOTION_NOTE,
                "upstream_module20a_lr_confidence_changed": False,
                "terminal_tf_assignments_created": False,
                "sql_signaling_edges_created": False,
                "malformed_legacy_rows_touched": False,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
