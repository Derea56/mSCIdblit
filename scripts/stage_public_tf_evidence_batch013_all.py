#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 013 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_013/"
    "public_tf_evidence_collection_batch_013.tsv"
)
TF_LINK_URL = "https://tflink.net/download/#interaction-gmt"
GTRD_URL = "https://pubmed.ncbi.nlm.nih.gov/30445619/"
PAIR_FIELDS = [
    "review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol", "species_scope",
    "source_registry", "source_record_id", "raw_tf_symbol", "target_symbol", "target_graph_modules",
    "candidate_membership_status", "exact_pair_search_url", "exact_pair_status", "regulator_general_evidence_status",
    "target_cell_presence_status", "binding_or_association_status", "downstream_expression_or_perturbation_status",
    "downstream_activation_status", "upstream_relay_status", "disposition", "primary_citation",
    "corroborating_citation", "near_match_exclusions", "review_notes", "exportable", "canonical_write_performed",
]
EVIDENCE_FIELDS = [
    "evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer", "support_kind",
    "cell_or_model", "assay_or_perturbation", "observation", "effect_direction", "primary_citation",
    "corroborating_citation", "route_or_module_relevance", "target_pair_scope", "exportable",
    "canonical_write_performed", "limitations",
]

# Separate regulator-level records are not used to promote unrelated queued edges.
REGULATORS = {
    "neurod2": ("NEUROD2", "https://humantfs.ccbr.utoronto.ca/all.php", "", "authoritative_identity_catalog", "human TF catalog", "TF identity/catalog record", "NEUROD2 is cataloged as a human TF; no queued target was functionally validated."),
    "znf302": ("ZNF302", "https://pubmed.ncbi.nlm.nih.gov/33326746/", "https://www.encodeproject.org/experiments/ENCSR567XAM/", "primary_literature_regulator_level", "human ChIP and synthetic-reporter models", "ChIP-seq and regulator-function assays", "ZNF302 has regulator-level occupancy/function evidence, but no queued target was functionally validated."),
    "znf416": ("ZNF416", "https://pubmed.ncbi.nlm.nih.gov/33326746/", "https://www.encodeproject.org/experiments/ENCSR567XAM/", "primary_literature_regulator_level", "human ChIP/synthetic-reporter models", "ChIP-seq and regulator-function assays", "ZNF416 has regulator-level binding evidence, but no queued target was functionally validated."),
    "znf670": ("ZNF670", "https://www.encodeproject.org/experiments/ENCSR233MWH/", "https://doi.org/10.17989/ENCSR233MWH", "authoritative_binding_dataset_only", "human HEK293 ChIP-seq", "preferred IDR peak analysis", "ZNF670 has a human ChIP-seq record; only CASC3 had a conservative queued promoter overlap."),
    "sp6": ("SP6", "https://www.uniprot.org/uniprotkb/Q3SY56/entry", "https://humantfs.ccbr.utoronto.ca/all.php", "authoritative_identity_catalog", "human TF identity records", "protein/gene identity review", "SP6 is distinct from KLF14/BTEB5 in current records; KLF14 evidence for TGFBR2/SPHK1 was not transferred."),
    "znf473": ("ZNF473", "https://pubmed.ncbi.nlm.nih.gov/33326746/", "https://www.encodeproject.org/experiments/ENCSR567XAM/", "primary_literature_regulator_level", "human synthetic-reporter and ChIP models", "ChIP-seq and regulator-function assays", "ZNF473 has regulator-level ChIP/function evidence, but no queued target effect was established."),
    "znf658": ("ZNF658", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4333095/", "", "primary_literature_regulator_level", "human zinc-responsive models", "ZTRE binding and repression assays", "ZNF658 directly regulates nonqueued zinc-responsive targets; no queued target was validated."),
    "hoxb9": ("HOXB9", "https://pubmed.ncbi.nlm.nih.gov/1347944/", "https://pubmed.ncbi.nlm.nih.gov/32015336/", "primary_literature_regulator_level", "Xenopus/mouse promoter and human tumor models", "promoter reporter and expression/phenotype studies", "HOXB9 has regulator-level evidence, but the NCAM1 finding is cross-species/model-mismatched and not an exact human edge."),
    "znf747": ("ZNF747", "https://www.ncbi.nlm.nih.gov/gene/65988", "https://pubmed.ncbi.nlm.nih.gov/18976975/", "authoritative_identity_catalog", "human annotation and siRNA phenotype", "domain annotation and unrelated phenotype study", "ZNF747 identity/phenotype records do not validate STAT6."),
    "sox3": ("SOX3", "https://pubmed.ncbi.nlm.nih.gov/8111369/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7174399/", "primary_literature_regulator_level", "human and mouse developmental models", "identity, expression, and developmental regulator studies", "SOX3 has regulator-level developmental evidence, but no queued target was functionally validated."),
    "rax2": ("RAX2", "https://pubmed.ncbi.nlm.nih.gov/32015336/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6997171/", "primary_literature_regulator_level", "human glioblastoma model", "DLG5 promoter binding and activation", "RAX2 directly regulates DLG5 in a nonqueued context; this does not validate the queued targets."),
    "rxrg": ("Rxrg", "https://pubmed.ncbi.nlm.nih.gov/7988448/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3634743/", "primary_literature_regulator_level", "mouse RXR binding/retinoid models", "DNA-binding specificity and agonist response", "Rxrg has regulator-level binding/response evidence, but no queued target was functionally validated."),
    "zfp82": ("ZFP82", "https://pubmed.ncbi.nlm.nih.gov/41053060/", "https://pubmed.ncbi.nlm.nih.gov/30211622/", "primary_literature_regulator_level", "human cancer and inflammatory models", "HDAC3/NF-kB mechanism and phenotype studies", "ZFP82 evidence involves nonqueued HDAC3/NF-kB relationships, not the queued targets."),
    "znf502": ("ZNF502", "https://pubmed.ncbi.nlm.nih.gov/37902191/", "", "primary_literature_regulator_level", "human oral-cancer model", "VIM-axis perturbation", "ZNF502 evidence involves a nonqueued VIM axis, not the queued targets."),
    "foxr2": ("FOXR2", "https://pubmed.ncbi.nlm.nih.gov/24599127/", "https://pubmed.ncbi.nlm.nih.gov/35802025/", "primary_literature_regulator_level", "human neural/tumor models", "transcriptional programs and chromatin occupancy", "FOXR2 has regulator-level evidence at other genes, not the queued targets."),
    "yy2": ("Yy2", "https://pubmed.ncbi.nlm.nih.gov/27191592/", "https://pubmed.ncbi.nlm.nih.gov/15087442/", "primary_literature_regulator_level", "mouse ChIP and regulatory models", "ChIP-seq and regulator-function assays", "Yy2 has regulator-level evidence at other loci, but no queued target was validated."),
    "znf501": ("ZNF501", "https://pubmed.ncbi.nlm.nih.gov/35688290/", "https://remap.univ-amu.fr/target_page/ZNF501%3A9606", "primary_literature_regulator_level", "human glioblastoma and ChIP models", "perturbation, rescue, and ChIP resources", "ZNF501 evidence involves FZD6 and regulator-level occupancy, not the queued targets."),
    "znf454": ("ZNF454", "https://pubmed.ncbi.nlm.nih.gov/41522747/", "", "primary_literature_regulator_level", "human colorectal-cancer model", "ChIP, luciferase, overexpression, and rescue", "ZNF454 directly regulates nonqueued FSTL3; no queued target was validated."),
    "znf431": ("Znf431", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3044984/", "https://www.ncbi.nlm.nih.gov/gene/69504", "primary_literature_regulator_level", "mouse Zfp932/Znf431 model", "motif/EMSA, ChIP, shRNA, and repression", "Mouse Znf431/Zfp932 evidence involves Ptch1, not the queued targets."),
    "znf626": ("ZNF626", "https://www.encodeproject.org/experiments/ENCSR588MQZ/", "https://pubmed.ncbi.nlm.nih.gov/40002911/", "authoritative_binding_dataset_only", "human HEK293 and estrogen-response models", "ChIP-seq and phenotype studies", "ZNF626 has regulator-level binding/phenotype evidence, but no queued target was validated."),
    "znf445": ("Znf445", "https://pubmed.ncbi.nlm.nih.gov/30602440/", "https://www.ncbi.nlm.nih.gov/gene/235682", "primary_literature_regulator_level", "mouse imprinting-control models", "imprinting-region binding and epigenetic repression", "Znf445/Zfp445 evidence concerns imprinting-control regions, not the queued targets."),
    "mnx1": ("MNX1", "https://pubmed.ncbi.nlm.nih.gov/41099694/", "", "primary_literature_regulator_level", "human neuronal models", "occupancy and neuronal gene regulation", "MNX1 evidence involves other neuronal loci, not the queued targets."),
    "zbtb49": ("ZBTB49", "https://www.encodeproject.org/experiments/ENCSR924GRG/", "", "authoritative_binding_dataset_only", "human HEK293 ChIP-seq", "regulator-level ChIP-seq", "ZBTB49 has regulator-level occupancy evidence; only two queued target memberships had independent supporting reports."),
    "znf837": ("ZNF837", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink candidate set", "species-matched target-set membership", "No qualifying regulator-level functional evidence was verified in this bounded pass."),
    "myt1": ("MYT1", "https://pubmed.ncbi.nlm.nih.gov/24828497/", "https://pubmed.ncbi.nlm.nih.gov/30312684/", "primary_literature_regulator_level", "human neural/cancer models", "repression/binding and perturbation studies", "MYT1 evidence involves PTEN, YAP1, and Notch-associated genes, not the queued targets."),
}

SET_URL = {
    "neurod2": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/NEUROD2_TARGET_GENES",
    "znf302": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF302_TARGET_GENES",
    "znf416": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF416_TARGET_GENES",
    "znf473": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF473_TARGET_GENES",
    "sox3": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/SOX3_TARGET_GENES",
    "rax2": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/RAX2_TARGET_GENES",
    "rxrg": "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/RXRG_TARGET_GENES",
    "zfp82": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZFP82_TARGET_GENES",
    "znf502": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF502_TARGET_GENES",
    "foxr2": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/FOXR2_TARGET_GENES",
    "znf501": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF501_TARGET_GENES",
    "znf454": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF454_TARGET_GENES",
    "znf626": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF626_TARGET_GENES",
    "mnx1": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/MNX1_TARGET_GENES",
    "zbtb49": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZBTB49_TARGET_GENES",
}

BINDING_KEYS = set(SET_URL)
DATABASE_ONLY_KEYS = {"znf658", "znf747", "yy2", "znf431", "znf445", "znf837", "myt1"}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def search_url(regulator: str, target: str, species: str) -> str:
    return "https://pubmed.ncbi.nlm.nih.gov/?term=" + quote_plus(f'"{regulator}" AND "{target}" AND {species}')


def classify(row: dict[str, str]) -> dict[str, str]:
    key = row["regulator_key"]
    target = row["target_symbol"].lower()
    symbol, general_primary, general_corr, kind, model, assay, observation = REGULATORS[key]
    status = "binding_dataset_only_not_promotable" if key in BINDING_KEYS else "database_membership_only_not_promotable"
    primary = SET_URL.get(key, TF_LINK_URL)
    corr = GTRD_URL if key in BINDING_KEYS else ""
    binding = "species_matched_GTRD_or_ENCODE_promoter_occupancy_lead" if key in BINDING_KEYS else "TFLink_snapshot_membership_only"
    notes = "The species-matched target-set or occupancy result is retained as a search lead only; it does not establish causal direction, target-cell presence, downstream activation, or upstream relay. No exact target-specific functional validation was located in this bounded pass."
    status_override = None
    exclusions = "Regulator-level evidence at nonqueued targets, orthologs, reverse-direction relationships, unrelated isoforms, and cross-species models was not transferred to queued edges."
    downstream = "not_found_for_exact_pair"
    disposition = "retain_as_staging_search_lead_only"
    cell = "not_established_for_exact_pair"

    if key == "neurod2" and target == "cdkn2a":
        status_override = "database_membership_only_not_promotable"
        primary = TF_LINK_URL
        corr = SET_URL[key]
        binding = "TFLink_membership_only_target_absent_from_exact_GTRD_set"
        notes = "TFLink lists the candidate, but CDKN2A was not present in the exact human NEUROD2 GTRD set and no pair-specific record was found."
    elif key == "znf670" and target in {"stat6", "tmem255a"}:
        status_override = "no_exact_pair_support_found_in_bounded_search"
        primary = TF_LINK_URL
        corr = "https://www.encodeproject.org/experiments/ENCSR233MWH/"
        binding = "conservative_ZNF670_IDR_peaks_did_not_overlap_canonical_target_promoter"
        notes = "TFLink lists the candidate, but conservative human ZNF670 IDR peaks did not overlap the canonical target promoter and no exact pairwise primary record was found."
        disposition = "retain_bounded_negative_only"
    elif key == "sp6" and target in {"tgfbr2", "sphk1"}:
        status_override = "contextual_near_match_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/19088080/" if target == "tgfbr2" else "https://pubmed.ncbi.nlm.nih.gov/24759103/"
        corr = "https://www.uniprot.org/uniprotkb/Q8TD94/entry"
        binding = "direct_KLF14_BTEB5_evidence_not_canonical_SP6"
        downstream = "KLF14_BTEB5_promoter_effect_not_SP6"
        notes = "The direct promoter evidence is for KLF14/BTEB5, a distinct current protein/gene record from canonical SP6; the evidence was not transferred."
        disposition = "retain_contextual_near_match_separately"
        exclusions = "KLF14/BTEB5 was not treated as canonical SP6; evidence from the distinct current record cannot support the queued SP6 pair."
    elif key == "hoxb9" and target == "ncam1":
        status_override = "contextual_near_match_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/1347944/"
        corr = "https://pubmed.ncbi.nlm.nih.gov/32015336/"
        binding = "cross_species_Xenopus_Hox_mouse_NCAM_reporter_and_human_association"
        downstream = "cross_species_reporter_or_human_association_not_exact_human_HOXB9_NCAM1_regulation"
        notes = "A Xenopus Hox-2.5/mouse N-CAM promoter reporter and human association findings are cross-species/model-mismatched; they do not establish the exact human HOXB9-NCAM1 edge."
        disposition = "retain_contextual_near_match_separately"
        cell = "cross_species_or_association_context_not_SCI_target_cell"
    elif key == "zbtb49" and target in {"lgal s2", "pnkp"}:
        status_override = "database_membership_only_not_promotable"
        primary = TF_LINK_URL
        corr = ""
        binding = "TFLink_membership_only_no_independent_pair_record"
    if key == "zbtb49" and target in {"galm", "psmd9"}:
        primary = SET_URL[key]
        corr = "https://www.encodeproject.org/experiments/ENCSR924GRG/"

    return {
        "symbol": symbol, "general_primary": general_primary, "general_corr": general_corr, "kind": kind,
        "model": model, "assay": assay, "observation": observation, "status": status_override or status,
        "primary": primary, "corr": corr, "cell": cell, "binding": binding, "downstream": downstream,
        "disposition": disposition, "exclusions": exclusions, "notes": notes,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_BATCH.parent)
    args = parser.parse_args()
    rows = read_tsv(args.batch)
    if len(rows) != 87:
        raise SystemExit(f"expected 87 rows, found {len(rows)}")
    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in rows:
        key = row["regulator_key"]
        if key not in REGULATORS:
            raise SystemExit(f"missing evidence map for {key}")
        info = classify(row)
        pairs.append({
            "review_id": f"public_tf_evidence_batch013_pair_{int(row['batch_rank']):02d}_{row['target_rank']}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(info["symbol"], row["target_symbol"], row["species_scope"]),
            "exact_pair_status": info["status"], "regulator_general_evidence_status": "supported_general_or_authoritative_regulator_evidence",
            "target_cell_presence_status": info["cell"], "binding_or_association_status": info["binding"],
            "downstream_expression_or_perturbation_status": info["downstream"], "downstream_activation_status": "not_established_for_SCI_target_cell",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": info["disposition"],
            "primary_citation": info["primary"], "corroborating_citation": info["corr"], "near_match_exclusions": info["exclusions"],
            "review_notes": info["notes"] + " " + info["observation"], "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch013_regulator_{key}", "regulator_key": key, "regulator_symbol": info["symbol"],
                "species_scope": row["species_scope"], "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"],
                "cell_or_model": info["model"], "assay_or_perturbation": info["assay"], "observation": info["observation"],
                "effect_direction": "queued-pair direction not established", "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"],
                "route_or_module_relevance": "regulator-level evidence only", "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false", "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation, or upstream relay.",
            })
        seen.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch013_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch013_regulator_register.tsv"
    summary_path = args.output_dir / "batch_013_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH013.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(item["regulator_key"], item["target_symbol"], item["species_scope"], item["source_record_id"]) for item in pairs}
    near = sum(v for k, v in status_counts.items() if "near_match" in k)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_013", "source_set_ranks_reviewed": list(range(1, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys),
        "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "exact_pair_support_rows": 0, "promotion_candidate_rows": 0,
        "partial_or_near_match_rows": near, "binding_dataset_only_not_promotable_rows": status_counts.get("binding_dataset_only_not_promotable", 0),
        "database_membership_only_not_promotable_rows": status_counts.get("database_membership_only_not_promotable", 0),
        "bounded_negative_rows": status_counts.get("no_exact_pair_support_found_in_bounded_search", 0), "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True,
        "limitations": ["TFLink/GTRD/ENCODE/MSigDB membership or occupancy is not causal regulation.", "Exact pair negatives are bounded-search results, not global absence.", "Near matches across genes, paralogs, isoforms, species, and regulatory directions were retained separately and not transferred.", "Target-cell presence, downstream activation, and upstream relay remain unestablished for all queued pairs.", "No canonical or Module 22B write was performed."],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join([
        "# Evidence review: public TF batch 013", "", "Reviewed 87 exact regulator-target-species pairs across 25 selected TFLink source sets.", "",
        f"- **{len(pairs)} / 87** pairs were reviewed.", f"- **{summary['binding_dataset_only_not_promotable_rows']}** pairs had occupancy/binding leads.",
        f"- **{summary['database_membership_only_not_promotable_rows']}** pairs remained database-membership-only leads.",
        f"- **{summary['partial_or_near_match_rows']}** near matches were kept separate.", f"- **{summary['bounded_negative_rows']}** pairs were bounded-search negatives.",
        "- **0** rows are exportable; no canonical or Module 22B writes were performed.", "",
        "No exact queued pair had target-level functional validation sufficient for promotion in this bounded pass. SP6/KLF14, HOXB9 cross-species NCAM1, and other near matches were explicitly excluded from exact-edge evidence.", "",
    ]), encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
