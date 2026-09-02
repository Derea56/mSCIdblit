#!/usr/bin/env python3
"""Promote a conservative exact-pair subset from Module 21A lanes 5311-5410."""

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
    RELAY / "module21a_pair_relay_review_batches216_217.tsv",
    RELAY / "module21a_pair_relay_review_batches218_219.tsv",
    RELAY / "module21a_pair_relay_review_batches220_221.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch115.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch115_summary.json"

PACKET = [
    (5312, "M20A-EXT-1984", "M21A-REUSE-2484"),
    (5318, "M20A-EXT-2011", "M21A-REUSE-2486"),
    (5321, "M20A-EXT-2028", "M21A-REUSE-2489"),
    (5323, "M20A-EXT-2030", ""),
    (5324, "M20A-EXT-2031", ""),
    (5325, "M20A-EXT-2033", "M21A-REUSE-2490"),
    (5331, "M20A-EXT-2081", "M21A-REUSE-2495"),
    (5336, "M20A-EXT-2089", ""),
    (5337, "M20A-EXT-2090", ""),
    (5339, "M20A-EXT-2096", ""),
    (5344, "M20A-EXT-2108", "M21A-REUSE-2501"),
    (5346, "M20A-EXT-2113", ""),
    (5347, "M20A-EXT-2114", ""),
    (5351, "M20A-EXT-2123", ""),
    (5357, "M20A-EXT-2139", ""),
    (5363, "M20A-EXT-2165", ""),
    (5364, "M20A-EXT-2167", ""),
    (5365, "M20A-EXT-2174", ""),
    (5392, "M20A-EXT-2320", ""),
    (5393, "M20A-EXT-2321", ""),
    (5394, "M20A-EXT-2324", ""),
    (5395, "M20A-EXT-2329", ""),
    (5396, "M20A-EXT-2332", ""),
    (5400, "M20A-EXT-2354", ""),
    (5402, "M20A-EXT-2357", "M21A-REUSE-2541"),
    (5404, "M20A-EXT-2360", ""),
    (5406, "M20A-EXT-2363", "M21A-REUSE-2544"),
    (5409, "M20A-EXT-2369", ""),
]

NOTE = (
    "Module 21A qualified-relay promotion batch115 (2026-09-02): exact MHC-I/CD8, "
    "orexin receptor, scavenging, integrin adhesion, IGF2R clearance, inhibitory "
    "Wnt modulation, Hedgehog antagonism, cytokine decoy, extracellular adhesion, "
    "galectin/endoglin, and LGI/ADAM23 complex evidence is raised to high only at "
    "the recorded supported layer. Ligand-form, heterodimer, receptor-complex, "
    "scavenging, antagonist, species/model, assay, and no-SCI boundaries remain "
    "explicit; no terminal-TF claim or SQL signaling edge is created."
)

BASIS = {
    5312: "MHC-I/H2-K1 engagement with the CD8alpha-beta coreceptor and TCR-proximal Lck function supports high at the pMHC-I/CD8 complex layer; CD8beta-only binding is not inferred.",
    5318: "Orexin/hypocretin receptor 2 activation with receptor-selective perturbation and neuronal function supports high at the HCRTR2 GPCR layer; coupling and behavioral branches remain model-dependent.",
    5321: "Hemoglobin-haptoglobin complex binding and CD163-dependent endocytosis support high at the exact scavenging/clearance layer; free Hp alone and canonical intracellular relay are not claimed.",
    5323: "Direct haptoglobin binding to purified Mac-1 supports high at the alphaM-beta2 receptor-complex binding layer; autonomous ITGAM and an intracellular relay are not inferred.",
    5324: "Direct haptoglobin binding to purified Mac-1 with beta2-sensitive inhibition supports high at the beta2-containing receptor-complex binding layer; autonomous ITGB2 is not inferred.",
    5325: "Hemopexin-heme binding and LRP1/CD91-dependent uptake support high at the exact scavenging/transport layer; apo-Hpx alone and a kinase relay are not claimed.",
    5331: "ICAM1 binding to Mac-1 with activation-dependent adhesion and myeloid function supports high at the complete alphaM-beta2 adhesion/relay layer; subunit-only and TF claims are excluded.",
    5336: "Direct ICAM4 binding to alphaM-containing beta2 integrin complexes supports high at the exact adhesion-binding layer; autonomous ITGAM and a unique intracellular relay are not inferred.",
    5337: "Direct ICAM4 binding to alphaV-containing integrin complexes supports high at the recorded alphaV-complex binding layer; autonomous ITGAV and a unique beta partner are not inferred.",
    5339: "ICAM5 binding to complete LFA-1/CD11a-CD18 supports high at the beta2-containing adhesion-binding layer; autonomous ITGB2 and a beta2-specific relay are not inferred.",
    5344: "IGF2 binding to IGF2R/CI-MPR with receptor internalization and lysosomal clearance supports high at the exact clearance/trafficking layer; no kinase or direct TF relay is claimed.",
    5346: "Direct IGFBP4-LRP6 interaction in an inhibitory FZD8-LRP6 Wnt context supports high at the exact binding/inhibitory-complex layer; no activating LRP6 relay or TF claim.",
    5347: "SPR-validated extracellular IGFBPL1-DCC binding supports high at the exact extracellular PPI layer; DCC signaling, axon guidance, and downstream relay are not inferred.",
    5351: "IHH-HHIP antagonist binding and Hedgehog sequestration support high at the exact extracellular antagonist-binding layer; HHIP is not promoted as an activating relay receptor.",
    5357: "IL13 binding to IL13RA1-containing type-II receptor complexes supports high at the exact receptor-component binding layer; autonomous IL13RA1 signaling is not inferred.",
    5363: "IL1A binding to the IL1R2/IL1RAP decoy complex supports high at the exact inhibitory binding layer; IL1R2 lacks a productive TIR relay and canonical IL1R1 signaling is not transferred.",
    5364: "IL1B binding to the IL1R2/IL1RAP decoy complex supports high at the exact inhibitory binding layer; IL1R2 lacks a productive TIR relay and canonical IL1R1 signaling is not transferred.",
    5365: "IL-36Ra/IL1F5 binding to IL1RL2 and inhibition of IL1RAP assembly support high at the exact antagonist receptor-complex layer; productive MyD88 relay is not claimed.",
    5392: "Direct RGD-dependent L1CAM binding to alpha5-beta1 supports high at the exact integrin adhesion-binding layer; no unique L1CAM-specific kinase cascade is inferred.",
    5393: "Direct RGD-dependent L1CAM binding to alphaV-beta3 supports high at the exact integrin adhesion-binding layer; integrin-family signaling is not collapsed into a pair-specific TF relay.",
    5394: "Laminin-alpha1 material binding to alpha1-beta1 supports high at the exact matrix-adhesion layer; isolated ITGA1 and intracellular relay claims are excluded.",
    5395: "Laminin-alpha2 domain VI binding to alpha1-beta1 with neurite adhesion supports high at the exact matrix-adhesion layer; downstream kinase signaling is not resolved.",
    5396: "Laminin-alpha5/laminin-511-521 binding to BCAM/Lutheran supports high at the exact extracellular adhesion-binding layer; no defined intracellular kinase relay is claimed.",
    5400: "Recombinant and cell-based assays support direct LGALS3-ENG association at the exact glycoprotein-binding layer; endoglin/TGF-beta signaling is not transferred to an LGALS3-specific relay.",
    5402: "LGALS3BP beta1-dependent adhesion and ITGB1-silencing functional evidence support high at the exact ITGB1-containing adhesion/function layer; alpha partner and purified affinity remain unresolved.",
    5404: "Direct LGI1-ADAM23 binding within the trans-synaptic complex supports high at the exact adhesion-complex layer; ADAM23-only intracellular signaling is not inferred.",
    5406: "LGI2 association with ADAM23-containing complexes and ADAM23-dependent Kv1 organization support high at the exact neuronal complex/function layer; LGI3 redundancy and lack of standalone affinity remain explicit.",
    5409: "Direct LGI4-ADAM23 receptor-complex association supports high at the exact binding layer; ADAM22-dominant developmental function and an ADAM23-specific relay are not inferred.",
}


def read(path):
    with path.open(encoding="utf-8", newline="") as handle:
        r = csv.DictReader(handle, delimiter="\t")
        return list(r.fieldnames or []), list(r)


def write(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        w = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def index(rows, key):
    out = {}
    for row in rows:
        value = row.get(key, "")
        if value and value in out:
            raise SystemExit(f"duplicate {key}: {value}")
        if value:
            out[value] = row
    return out


def tokens(value):
    return {x.strip() for x in value.split(";") if x.strip()}


def once(value):
    return value if NOTE in value else f"{value} {NOTE}".strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    detail_fields, detail_rows = read(DETAIL)
    reuse_fields, reuse_rows = read(REUSE)
    pair_fields, pair_rows = read(PAIRS)
    review_tables = [read(path) for path in REVIEW_FILES]
    reviews = index([row for _, rows in review_tables for row in rows], "review_id")
    detail = index(detail_rows, "evidence_id")
    reuse = index(reuse_rows, "pathway_reuse_key")
    coverage = {}
    audit = []

    for number, review_id, reuse_key in PACKET:
        evidence_id = f"M21A-PAIR-EVID-{number}"
        row = detail.get(evidence_id)
        review = reviews.get(review_id)
        if row is None or row.get("confidence_tier") not in {"medium", "medium-high"}:
            raise SystemExit(f"detail tier mismatch: {evidence_id}")
        if not tokens(row.get("evidence_layer", "")) & {
            "binding_activation", "ligand_receptor_binding_or_activation",
            "receptor_proximal_relay", "downstream_pathway_function",
        }:
            raise SystemExit(f"detail layer mismatch: {evidence_id}")
        if row.get("pathway_reuse_key", "") != reuse_key:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        if review is None or review.get("evidence_id") != evidence_id:
            raise SystemExit(f"review identity mismatch: {evidence_id}")
        if review.get("pathway_reuse_key", "") != reuse_key or review.get("source_locators") != row.get("source_locators"):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if review.get("review_status") not in {
            "reviewed_relay_candidate", "reviewed_binding_only", "reviewed_function_only", "reviewed_scavenging_only",
        }:
            raise SystemExit(f"review status mismatch: {evidence_id}")
        if reuse_key and (reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id):
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        matching = [
            pair for pair in pair_rows
            if evidence_id in tokens(pair.get("module21a_evidence_ids", ""))
            and pair.get("pair_key") == review.get("pair_key")
        ]
        if len(matching) != 1:
            raise SystemExit(f"coverage mapping mismatch: {evidence_id}")
        pair = matching[0]
        coverage[evidence_id] = pair
        if pair.get("module21a_status") != review.get("review_status"):
            raise SystemExit(f"coverage status mismatch: {evidence_id}")
        if pair.get("module22a_status") != "no_terminal_tf_evidence":
            raise SystemExit(f"TF-boundary mismatch: {evidence_id}")
        hits = []
        for path in RELAY.glob("module21a_relay_promotion_batch*.tsv"):
            if path == AUDIT:
                continue
            for candidate in read(path)[1]:
                if candidate.get("evidence_id") == evidence_id or candidate.get("pair_key") == review["pair_key"]:
                    hits.append(path.name)
                    break
        if hits:
            raise SystemExit(f"promotion overlap for {evidence_id}: {hits}")
        audit.append({
            "evidence_id": evidence_id,
            "review_id": review_id,
            "pair_key": review["pair_key"],
            "pathway_reuse_key": reuse_key,
            "previous_tier": row["confidence_tier"],
            "new_tier": "high",
            "source_locators": row["source_locators"],
            "decision_basis": BASIS[number],
            "upstream_lr_confidence_unchanged": "true",
            "terminal_tf_status_unchanged": "true",
            "sql_materialization": "false",
        })

    if not args.apply:
        print(json.dumps({"validated": len(audit), "apply": False, "evidence_ids": [x["evidence_id"] for x in audit]}, indent=2))
        return

    for number, review_id, reuse_key in PACKET:
        evidence_id = f"M21A-PAIR-EVID-{number}"
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = once(detail[evidence_id]["limitations"])
        reviews[review_id]["confidence_tier"] = "high"
        reviews[review_id]["curator_note"] = once(reviews[review_id]["curator_note"])
        if reuse_key:
            reuse[reuse_key]["validation_status"] = "promoted_high_batch115"
            reuse[reuse_key]["limitations"] = once(reuse[reuse_key]["limitations"])
        coverage[evidence_id]["curator_notes"] = once(coverage[evidence_id]["curator_notes"])

    write(DETAIL, detail_fields, detail_rows)
    write(REUSE, reuse_fields, reuse_rows)
    write(PAIRS, pair_fields, pair_rows)
    for path, (fields, rows) in zip(REVIEW_FILES, review_tables):
        write(path, fields, rows)
    audit_fields = [
        "evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier",
        "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged",
        "terminal_tf_status_unchanged", "sql_materialization",
    ]
    write(AUDIT, audit_fields, audit)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-local-register-exact-pair-batch115-2026-09-02",
        "records_promoted": len(audit),
        "evidence_ids": [x["evidence_id"] for x in audit],
        "promotion_note": NOTE,
        "upstream_module20a_lr_confidence_changed": False,
        "terminal_tf_assignments_created": False,
        "sql_signaling_edges_created": False,
        "malformed_legacy_rows_touched": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit), "applied": len(audit), "evidence_ids": [x["evidence_id"] for x in audit]}, indent=2))


if __name__ == "__main__":
    main()
