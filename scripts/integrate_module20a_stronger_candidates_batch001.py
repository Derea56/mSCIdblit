#!/usr/bin/env python3
"""Integrate a small, source-adjudicated Module 20A stronger-candidate batch.

This batch is intentionally narrow.  It promotes only exact pairs for which a
primary paper can be named, keeps every decision at medium confidence, and
does not create Module 21A relay edges or any SCI-context claim.  The source
queue and low-evidence registry are updated together so the release manifest
does not continue to classify promoted rows as low evidence.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "work" / "module20_db_seed" / "evidence_escalation_router"
STARTER = ROOT / "work" / "module20_db_seed" / "evidence_escalation_starter"
QUEUE = ROUTER / "module20a_external_review_queue.tsv"
LOW = ROUTER / "module20a_low_evidence_registry.tsv"
EVIDENCE = STARTER / "module20a_stronger_candidates_batch001_evidence_register.tsv"
DECISIONS = STARTER / "module20a_stronger_candidates_batch001_decision_register.tsv"
SUMMARY = STARTER / "module20a_stronger_candidates_batch001_summary.json"

EVIDENCE_FIELDS = [
    "evidence_item_id", "review_id", "pair_key", "pair_label", "source_kind",
    "source_locator", "support_kind", "species_support", "source_scope",
    "confidence_tier", "citation_note", "evidence_summary", "limitations",
]
DECISION_FIELDS = [
    "review_id", "pair_key", "pair_label_canonical", "review_status",
    "confidence_decision", "mouse_confidence", "mouse_confidence_rank",
    "human_confidence", "human_confidence_rank", "human_evidence_present",
    "receptor_state", "receptor_role", "directness", "species_posture",
    "decision_basis", "evidence_register_ids", "next_action",
]


CASES = {
    "M20A-EXT-1505": {
        "pair_key": "efemp1 egfr",
        "label": "Efemp1 Egfr",
        "source": "https://pubmed.ncbi.nlm.nih.gov/19804359/",
        "support_kind": "direct_binding_and_receptor_activation",
        "species": "human EFEMP1/EGFR; human pancreatic carcinoma cells",
        "mouse": ("uncertain", "0"),
        "human": ("medium", "2"),
        "summary": "Purified EFEMP1 binds EGFR and induces EGFR autophosphorylation with downstream Akt and MAPK phosphorylation; an EGFR kinase inhibitor blocks the downstream response.",
        "limitations": "The source is a human pancreatic-carcinoma comparator and does not establish SCI relevance or universal EGFR-ligand behavior. A later local triage packet had retained this row at low, so this decision supersedes that conservative hold only because the exact PMID 19804359 abstract was rechecked.",
    },
    "M20A-EXT-1934": {
        "pair_key": "gpc3 igf1r",
        "label": "Gpc3 Igf1r",
        "source": "https://pubmed.ncbi.nlm.nih.gov/18413366/",
        "support_kind": "direct_binding_and_receptor_dependent_function",
        "species": "human HCC cells; mouse NIH3T3 cells; HEK293 heterologous assays",
        "mouse": ("medium", "2"),
        "human": ("medium", "2"),
        "summary": "GPC3 binds IGF1R through its N-terminal proline-rich region and enhances IGF-II-dependent IGF1R and ERK phosphorylation; GPC3 knockdown reduces the same signaling readouts in HCC cells.",
        "limitations": "The study is tumor-cell centered and includes heterologous expression systems; it does not establish universal tissue behavior or SCI relevance. The ligand/cofactor relationship is IGF-II-dependent and should not be represented as autonomous GPC3 agonism.",
    },
    "M20A-EXT-2528": {
        "pair_key": "ngf sorcs2",
        "label": "Ngf Sorcs2",
        "source": "https://pubmed.ncbi.nlm.nih.gov/30061605/",
        "support_kind": "structural_and_biophysical_direct_binding",
        "species": "recombinant mammalian SorCS2 and NGF-family proteins",
        "mouse": ("uncertain", "0"),
        "human": ("uncertain", "0"),
        "summary": "The primary study resolves a SorCS2–NGF complex and validates direct neurotrophin binding at the SorCS2 beta-propeller site using structural and biophysical assays.",
        "limitations": "The evidence is structural/biophysical and does not by itself establish endogenous tissue signaling, downstream coupling, or SCI relevance. The paper also examines processed NGF-family forms; the exact mature-versus-proNGF species must remain explicit in downstream use.",
    },
    "M20A-EXT-1536": {
        "pair_key": "efna5 epha3",
        "label": "Efna5 Epha3",
        "source": "https://pubmed.ncbi.nlm.nih.gov/15901737/",
        "support_kind": "direct_binding_interface_and_receptor_activation",
        "species": "human EphA3/ephrin-A5 recombinant and transfected-cell systems",
        "mouse": ("uncertain", "0"),
        "human": ("medium", "2"),
        "summary": "Primary mutational and structural work identifies ephrin-A5 residues required for high-affinity EphA3 signaling-complex assembly and shows that the corresponding interfaces control ephrin-induced EphA3 phosphorylation.",
        "limitations": "Functional signaling depends on ligand presentation and higher-order oligomerization; the row does not establish a free soluble-ligand mechanism, SCI relevance, or a mouse-specific context.",
    },
    "M20A-EXT-3071": {
        "pair_key": "sema3f nrp1",
        "label": "Sema3f Nrp1",
        "source": "https://pubmed.ncbi.nlm.nih.gov/24079887/;https://pubmed.ncbi.nlm.nih.gov/23145112/",
        "support_kind": "direct_processed_ligand_binding_and_receptor_function",
        "species": "human/mouse semaphorin and NRP1 systems; furin-processed Sema3F constructs",
        "mouse": ("medium", "2"),
        "human": ("medium", "2"),
        "summary": "Primary biochemical and cell-based studies show furin-processed Sema3F engages NRP1 through defined binding motifs and inhibits NRP1/VEGF-A-dependent endothelial activation.",
        "limitations": "The strongest assays use furin-processed C-terminal constructs and endothelial or heterologous systems; processing state and receptor-complex context must be retained. No SCI-specific evidence is asserted.",
    },
    "M20A-EXT-3086": {
        "pair_key": "sema4a plxnd1",
        "label": "Sema4a Plxnd1",
        "source": "https://pubmed.ncbi.nlm.nih.gov/17318185/",
        "support_kind": "direct_binding_and_receptor_dependent_function",
        "species": "mouse endothelial cells and angiogenesis models",
        "mouse": ("medium", "2"),
        "human": ("uncertain", "0"),
        "summary": "Binding and functional experiments identify Plexin-D1 as a Sema4A receptor on endothelial cells, with Sema4A suppressing VEGF-mediated migration, proliferation, and angiogenesis in vitro and in vivo.",
        "limitations": "The source is endothelial/angiogenesis-focused and does not establish SCI relevance or transfer to human tissue. Sema4A has other receptor contexts, so this row is specifically Plexin-D1 scoped.",
    },
}


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    queue_rows = read(QUEUE)
    low_rows = read(LOW)
    queue = {row["review_id"]: row for row in queue_rows}
    low = {row["review_id"]: row for row in low_rows}
    expected = set(CASES)
    if expected - set(queue):
        raise SystemExit(f"selected rows missing from queue: {sorted(expected - set(queue))}")
    if expected - set(low):
        raise SystemExit(f"selected rows missing from low registry: {sorted(expected - set(low))}")
    if any(low[rid]["agent_verdict"] != "promote_candidate" for rid in expected):
        raise SystemExit("stronger batch requires the pre-existing promote_candidate verdict for every row")

    evidence_rows, decision_rows = [], []
    for index, rid in enumerate(sorted(CASES), start=1):
        case = CASES[rid]
        evidence_id = f"M20A-STRONG01-EVID-{index:04d}"
        decision_basis = "Exact primary source rechecked against the candidate pair; promoted to medium only. This is ligand/receptor evidence, not SCI context, not a relay edge, and not a high-confidence canonical mechanism claim."
        evidence_rows.append({
            "evidence_item_id": evidence_id,
            "review_id": rid,
            "pair_key": case["pair_key"],
            "pair_label": case["label"],
            "source_kind": "primary_literature",
            "source_locator": case["source"],
            "support_kind": case["support_kind"],
            "species_support": case["species"],
            "source_scope": "stronger_candidate_exact_pair_adjudication_batch001",
            "confidence_tier": "medium",
            "citation_note": case["summary"],
            "evidence_summary": case["summary"],
            "limitations": case["limitations"],
        })
        decision_rows.append({
            "review_id": rid,
            "pair_key": case["pair_key"],
            "pair_label_canonical": case["label"],
            "review_status": "reviewed",
            "confidence_decision": "medium",
            "mouse_confidence": case["mouse"][0],
            "mouse_confidence_rank": case["mouse"][1],
            "human_confidence": case["human"][0],
            "human_confidence_rank": case["human"][1],
            "human_evidence_present": "yes" if case["human"][0] == "medium" else "no",
            "receptor_state": "membrane_bound_or_receptor_complex_context",
            "receptor_role": "ligand_receptor_or_receptor_complex_context",
            "directness": case["support_kind"],
            "species_posture": "species_scoped_to_primary_source; no_unlisted_species_inference",
            "decision_basis": decision_basis,
            "evidence_register_ids": evidence_id,
            "next_action": "retain_medium; preserve_context; no_SignalingEdge_until_SCI_relevance_and_relay_review",
        })

    write(EVIDENCE, EVIDENCE_FIELDS, evidence_rows)
    write(DECISIONS, DECISION_FIELDS, decision_rows)

    for rid in sorted(expected):
        row = queue[rid]
        row["confidence_decision"] = "medium"
        prior = row.get("evidence_register_ids", "").strip()
        eid = f"M20A-STRONG01-EVID-{sorted(CASES).index(rid) + 1:04d}"
        row["evidence_register_ids"] = ";".join(x for x in (prior, eid) if x)
        row["curator_notes"] = (row.get("curator_notes", "") + " Stronger-candidate batch001: exact primary pair evidence rechecked; medium only; no SCI or relay inference.").strip()
    write(QUEUE, list(queue_rows[0]), queue_rows)

    remaining_low = [row for row in low_rows if row["review_id"] not in expected]
    write(LOW, list(low_rows[0]), sorted(remaining_low, key=lambda row: row["review_id"]))

    summary = {
        "generated_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "batch_id": "module20a_stronger_candidates_batch001",
        "rows_reviewed": len(CASES),
        "rows_promoted_to_medium": len(CASES),
        "rows_promoted_to_high": 0,
        "rows_removed_from_low_evidence_registry": len(CASES),
        "signaling_edges_created": 0,
        "selected_review_ids": sorted(CASES),
        "support_kind_counts": dict(sorted(Counter(case["support_kind"] for case in CASES.values()).items())),
        "policy": "Exact primary-pair evidence is required; medium is the ceiling for this batch; SCI context and intracellular relay claims remain unasserted.",
    }
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
