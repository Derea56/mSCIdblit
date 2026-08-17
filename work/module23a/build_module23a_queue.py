#!/usr/bin/env python3
"""Build the Module 23A review queue from read-only candidate inventories.

The output is intentionally a queue, not an evidence register. Database rows
are retained as candidate provenance only; primary-paper validation is required
before any 23A edge is promoted.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
CC = ROOT / "work/module20_db_seed/cellchatdb_module20_priority_seeds/cellchatdb_mouse_module20_priority_ecm_receptor.tsv"
CONNECTOME = ROOT / "work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/by_family/guidance_ecm_family.tsv"
M21A_REUSE = ROOT / "work/module21_relay/module21a_pathway_reuse_registry.tsv"
M21A_DETAIL = ROOT / "work/module21_relay/module21a_pair_relay_evidence_detail.tsv"


FIELDS = [
    "queue_id",
    "batch_id",
    "priority",
    "candidate_class",
    "upstream_feature_or_ligand",
    "receptor_or_adhesion_system",
    "receptor_complex_status",
    "receptor_proximal_branch_to_validate",
    "downstream_tf_or_program_target",
    "evidence_layers_to_extract",
    "species_context",
    "cell_type_or_model_context",
    "source_origin",
    "source_record_id",
    "stable_source_locator",
    "search_boundary",
    "status",
    "notes",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def pair_key(ligand: str, receptor: str) -> str:
    return f"{norm(ligand)}|{norm(receptor)}"


def branch_for_receptor(receptor: str, ligand: str = "") -> str:
    text = f"{receptor} {ligand}".lower()
    if "itga" in text or "itgb" in text:
        return "integrin-focal-adhesion-FAK-SRC-ILK;validate-YAP-TAZ-TEAD"
    if "cd44" in text:
        return "CD44-cytoskeletal-RHO/ERK;validate-mechanotransduction"
    if "sdc1" in text or "sdc4" in text:
        return "syndecan-integrin-FAK/SRC;validate-RHO/YAP"
    if "dag1" in text:
        return "dystroglycan-laminin-actin;validate-FAK/ILK/YAP"
    if "gp6" in text:
        return "GP6-SYK-PLCgamma;validate-cell-context"
    if "cd36" in text:
        return "CD36-SRC/JNK/NF-kB;validate-cell-context"
    if "eph" in text:
        return "Eph-ephrin-bidirectional-adhesion;validate-trans-versus-cis"
    if "nrp" in text or "plxn" in text:
        return "semaphorin-neuropilin/plexin;validate-obligate-co-receptor"
    if "lrp" in text:
        return "LRP-family-adhesion/ERK;validate-direct-binding-versus-colocalization"
    return "receptor-specific relay to validate"


def priority_for_cc(row: dict[str, str]) -> str:
    receptor = row["receptor_symbol"].lower()
    if any(token in receptor for token in ("itga", "itgb", "cd44", "sdc1", "sdc4", "dag1", "cd36")):
        return "P1"
    if "gp6" in receptor or "gp1ba" in receptor or "cd47" in receptor:
        return "P2"
    return "P3"


def priority_for_connectome(row: dict[str, str]) -> str:
    text = f"{row['lr_pair']} {row['matched_families']}".lower()
    if any(token in text for token in ("itga", "itgb", "lrp1", "ccn4", "angpt1", "angptl2", "edil3", "spp1", "egfl7", "mfge8", "npnt", "tnc", "thbs", "postn")):
        return "P1"
    if "epha" in text or "ephb" in text or "nrp" in text or "plxn" in text:
        return "P2"
    return "P3"


def priority_for_reuse(row: dict[str, str]) -> str:
    text = " ".join([row["source_entity"], row["pathway_name"], row["target_entities"], row["terminal_tf_entities"], row["ligand_pair_keys"]]).lower()
    if any(token in text for token in ("fak", "src", "ilk", "yap", "taz", "tead")):
        return "P1"
    if any(token in text for token in ("integrin", "collagen", "laminin", "tenascin", "cadherin", "thbs", "spp1", "vcam", "matrix", "adhesion")):
        return "P2"
    return "P3"


def join_nonempty(values: list[str]) -> str:
    seen: list[str] = []
    for value in values:
        value = value.strip()
        if value and value not in seen:
            seen.append(value)
    return "; ".join(seen)


def split_pair(value: str) -> tuple[str, str]:
    ligand, receptor = value.split(" ", 1)
    return ligand, receptor


def main() -> None:
    cc_rows = read_tsv(CC)
    connectome_rows = read_tsv(CONNECTOME)
    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    def add(row: dict[str, str]) -> None:
        key = (row["candidate_class"], pair_key(row["upstream_feature_or_ligand"], row["receptor_or_adhesion_system"]))
        if key in seen:
            return
        seen.add(key)
        rows.append(row)

    for source in cc_rows:
        ligand = source["ligand_symbol"]
        receptor = source["receptor_symbol"]
        add({
            "queue_id": "",
            "batch_id": "",
            "priority": priority_for_cc(source),
            "candidate_class": "matrix_receptor_candidate",
            "upstream_feature_or_ligand": ligand,
            "receptor_or_adhesion_system": receptor,
            "receptor_complex_status": "CellChatDB complex candidate; exact heterodimer/co-receptor requires primary validation",
            "receptor_proximal_branch_to_validate": branch_for_receptor(receptor, ligand),
            "downstream_tf_or_program_target": "not asserted; extract YAP/TAZ/TEAD only when directly measured",
            "evidence_layers_to_extract": "ligand-receptor binding or activation;receptor-proximal relay;downstream pathway or cellular function",
            "species_context": "mouse database candidate; experimental species unresolved",
            "cell_type_or_model_context": "SCI-relevant receiver state unresolved; extract exact primary model",
            "source_origin": "CellChatDB.mouse ECM-Receptor priority seed",
            "source_record_id": source["source_record_id"],
            "stable_source_locator": "local:work/module20_db_seed/cellchatdb_module20_priority_seeds/cellchatdb_mouse_module20_priority_ecm_receptor.tsv",
            "search_boundary": "Database/KEGG seed only; do not promote direct binding, relay, TF, or function without primary evidence",
            "status": "queued",
            "notes": f"Pathway label={source['pathway_name']}; matched family={source['matched_families']}",
        })

    for source in connectome_rows:
        ligand, receptor = split_pair(source["lr_pair"])
        add({
            "queue_id": "",
            "batch_id": "",
            "priority": priority_for_connectome(source),
            "candidate_class": "connectome_adhesion_candidate",
            "upstream_feature_or_ligand": ligand,
            "receptor_or_adhesion_system": receptor,
            "receptor_complex_status": "ConnectomeDB direct seed; exact complex, directionality, and activation state require primary validation",
            "receptor_proximal_branch_to_validate": branch_for_receptor(receptor, ligand),
            "downstream_tf_or_program_target": "not asserted; extract a TF/program only when directly measured",
            "evidence_layers_to_extract": "ligand-receptor binding or activation;receptor-proximal relay;downstream pathway or cellular function",
            "species_context": source["species_note"],
            "cell_type_or_model_context": "SCI-relevant receiver state unresolved; extract exact primary model",
            "source_origin": "ConnectomeDB mouse priority guidance/ECM review slice",
            "source_record_id": source["interaction_id"],
            "stable_source_locator": "local:work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/by_family/guidance_ecm_family.tsv",
            "search_boundary": "ConnectomeDB seed only; reuse Module 20A LR evidence when present, but validate 23A relay/function separately",
            "status": "queued_boundary_review" if source["module20a_bucket"] == "boundary_review" else "queued",
            "notes": f"Module20A bucket={source['module20a_bucket']}; next action={source['next_action']}; matched family={source['matched_families']}",
        })

    reuse_rows = read_tsv(M21A_REUSE)
    detail_rows = read_tsv(M21A_DETAIL)
    details_by_reuse: dict[str, list[dict[str, str]]] = {}
    for detail in detail_rows:
        details_by_reuse.setdefault(detail["pathway_reuse_key"], []).append(detail)
    reuse_terms = re.compile(r"integrin|focal|FAK|SRC|ILK|YAP|TAZ|TEAD|cadherin|collagen|laminin|tenascin|THBS|SPP1|VCAN|EDIL3|periostin|matrix|adhesion", re.I)
    for source in reuse_rows:
        searchable = " ".join([source["source_entity"], source["pathway_name"], source["target_entities"], source["terminal_tf_entities"], source["limitations"], source["ligand_pair_keys"]])
        if not source["ligand_pair_keys"].strip() or not reuse_terms.search(searchable):
            continue
        details = details_by_reuse.get(source["pathway_reuse_key"], [])
        pair_key_value = source["ligand_pair_keys"].strip()
        ligand = pair_key_value.split(" ", 1)[0]
        receptor = pair_key_value.split(" ", 1)[1] if " " in pair_key_value else "receptor complex unresolved"
        source_locators = join_nonempty([d["source_locators"] for d in details])
        species = join_nonempty([d["species"] for d in details]) or "Module21A source species unresolved"
        cell_models = join_nonempty([d["cell_type_model"] for d in details]) or "Module21A source model unresolved"
        assay = join_nonempty([d["assay_or_perturbation"] for d in details]) or "See Module21A detail register and cited primary sources"
        evidence_layers = join_nonempty([d["evidence_layer"] for d in details]) or "Module21A layer unresolved"
        relation_types = join_nonempty([d["relation_type"] for d in details]) or "Module21A relation type unresolved"
        limitations = join_nonempty([source["limitations"]] + [d["limitations"] for d in details])
        add({
            "queue_id": "",
            "batch_id": "",
            "priority": priority_for_reuse(source),
            "candidate_class": "module21a_reuse_candidate",
            "upstream_feature_or_ligand": ligand,
            "receptor_or_adhesion_system": receptor,
            "receptor_complex_status": "Module21A reuse candidate; preserve exact receptor complex, fragment, co-receptor, and matrix-presentation limits",
            "receptor_proximal_branch_to_validate": source["pathway_name"],
            "downstream_tf_or_program_target": source["terminal_tf_entities"].strip() or "not asserted; no terminal TF transfer",
            "evidence_layers_to_extract": "ligand-receptor binding or activation;receptor-proximal relay;downstream pathway or cellular function",
            "species_context": species,
            "cell_type_or_model_context": cell_models,
            "source_origin": "Module21A pathway reuse registry and pair-relay detail (read-only reuse seed)",
            "source_record_id": source["pathway_reuse_key"],
            "stable_source_locator": source_locators or f"local:work/module21_relay/module21a_pathway_reuse_registry.tsv; {source['evidence_ids']}",
            "search_boundary": f"Reuse only when exact ligand/receptor complex, branch, species, model, assay, and evidence scope match. {limitations}",
            "status": "queued_21a_reuse_review",
            "notes": f"Existing Module21A relation={relation_types}; existing evidence layer={evidence_layers}; 23A does not alter the Module21A record",
        })

    mechanism_targets = [
        ("M1A-P027", "matrix_stiffness_feature", "chronic SCI lesion/rim stiffness", "beta1-integrin/ILK;FAK/SRC;YAP/TAZ/TEAD", "GFAP astrocyte reactivity and scar-mechanics program", "PMID:31516087; PMCID:PMC6978780", "P1", "Mouse contusion; primary mouse and hESC-derived human astrocytes", "SCI stiffness paper measured beta1-integrin/ILK and GFAP; TF relay still requires targeted extraction"),
        ("M1A-P027", "matrix_stiffness_feature", "200 Pa versus 2000 Pa substrate stiffness", "beta1-integrin/ILK;actin mechanosensing", "astrocyte morphology, actin stress fibers, GFAP", "PMID:31516087; PMCID:PMC6978780", "P1", "Primary mouse astrocytes; hESC-derived human astrocytes", "Substrate-stiffness response is not equivalent to a direct ligand-receptor interaction"),
        ("M1A-P003", "cell_contact_adhesion_feature", "scar-forming astrocyte contact", "beta1-integrin/N-cadherin adhesion relay", "astrocyte scar recruitment/persistence program", "PMID:36336030; DOI:10.1016/j.expneurol.2022.114264", "P1", "Mouse SCI; scar-forming astrocytes", "Tracker records the beta1-integrin/N-cadherin question and immunostaining; exact relay and causal perturbation must be extracted"),
        ("M1A-P007", "matricellular_ligand_feature", "fibronectin EDA-positive chronic fibrotic scar", "integrin/focal-adhesion relay to validate", "fibrotic scar ECM program", "PMID:29705186; PMCID:PMC5995671; DOI:10.1016/j.nbd.2018.04.014", "P1", "Mouse contusive SCI; fibrotic scar", "FN-EDA abundance or loss does not itself prove a receptor-proximal relay"),
        ("M1A-P008", "matrix_cell_state_feature", "perivascular fibroblast ECM deposition", "integrin/focal-adhesion relay to validate", "fibrotic scar and fibroblast-state program", "PMID:23966707; PMCID:PMC3755723; DOI:10.1523/JNEUROSCI.2524-13.2013", "P2", "Mouse contusive SCI; perivascular fibroblasts", "Cell-of-origin evidence is not direct ECM-receptor or mechanotransduction evidence"),
        ("M1A-P009", "matrix_cell_state_feature", "type A pericyte-derived fibrotic scar ECM", "integrin/focal-adhesion relay to validate", "scar reduction and axon-regeneration function", "PMID:29502968; PMCID:PMC5871719; DOI:10.1016/j.cell.2018.02.004", "P2", "Mouse dorsal hemisection/dorsal funiculus incision; pericyte-derived scar", "Intervention/function evidence must remain distinct from direct adhesion binding"),
        ("M1A-P026", "matrix_mechanics_feature", "chronic hemisection scar softening with ECM/GAG dysregulation", "mechanical-state relay unresolved", "cavitation, ECM composition, and chronic tissue mechanics", "PMID:32957245; PMCID:PMC7509206; DOI:10.1016/j.jmbbm.2020.103953", "P2", "Rat lateral hemisection; chronic scar", "Contradicts the direction of stiffness reported in M1A-P027; retain as model/time-dependent boundary"),
        ("M1A-P010", "matricellular_ligand_feature", "periostin-associated pericyte/macrophage scar interaction", "periostin-integrin or adhesion relay to validate", "pericyte/macrophage scar-formation program", "DOI:10.1016/j.ajpath.2016.11.010", "P2", "SCI mouse context; pericytes and infiltrating monocytes/macrophages", "Tracker status is queued pass; do not treat the citation as already extracted evidence"),
        ("M5A-P015", "integrin_activation_feature", "activated alpha9 integrin plus kindlin-1", "integrin activation;laminin-111/tenascin-C bridge interaction", "sensory axon regeneration and pathway reconstruction", "PMID:40317093", "P1", "Rat dorsal-column crush; sensory axons/DRG", "Primary paper supports a regeneration intervention; separate matrix bridge, integrin activation, relay, and function"),
        ("M5A-P038", "matrix_glycan_feature", "GlcNAc6ST1/4-dependent glycan sulfation and ECM program", "matrix glycan-dependent relay unresolved", "fibronectin/collagen ECM and myeloid recruitment program", "PMID:40876929", "P2", "Mouse T10 contusion; myeloid and lesion tissue", "ECM transcript changes and phenotype do not establish a direct receptor interaction"),
        ("M5A-P040", "matricellular_ligand_feature", "osteopontin plus treadmill intervention", "OPN-integrin versus IGF1R branch must be separated", "IGF1R-AKT-mTOR and axon-regeneration function", "PMID:38015348", "P2", "Mouse cervical crush; corticospinal neurons/lesion", "OPN is a matricellular ligand, but the reported pathway is IGF1R/Akt/mTOR; do not infer integrin relay"),
    ]
    for source_id, cls, feature, branch, target, locator, priority, context, boundary in mechanism_targets:
        add({
            "queue_id": "",
            "batch_id": "",
            "priority": priority,
            "candidate_class": cls,
            "upstream_feature_or_ligand": feature,
            "receptor_or_adhesion_system": "to extract from primary paper",
            "receptor_complex_status": "not asserted; mechanism target only",
            "receptor_proximal_branch_to_validate": branch,
            "downstream_tf_or_program_target": target,
            "evidence_layers_to_extract": "ligand-receptor binding or activation;receptor-proximal relay;downstream pathway or cellular function",
            "species_context": context.split(";", 1)[0],
            "cell_type_or_model_context": context,
            "source_origin": "SCI primary-paper anchor from prior module",
            "source_record_id": source_id,
            "stable_source_locator": locator,
            "search_boundary": boundary,
            "status": "queued_primary_first",
            "notes": "Mechanism target is not an evidence record; promote only after exact assay/perturbation extraction",
        })

    priority_rank = {"P1": 1, "P2": 2, "P3": 3}
    rows.sort(key=lambda row: (priority_rank[row["priority"]], row["candidate_class"], row["upstream_feature_or_ligand"].lower(), row["receptor_or_adhesion_system"].lower(), row["source_record_id"]))
    for index, row in enumerate(rows, start=1):
        row["queue_id"] = f"M23A-Q{index:04d}"
        row["batch_id"] = f"M23A-B{((index - 1) // 50) + 1:03d}"

    queue_path = OUT / "module23a_extraction_queue.tsv"
    with queue_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    batches = []
    for batch_id in sorted({row["batch_id"] for row in rows}):
        subset = [row for row in rows if row["batch_id"] == batch_id]
        batches.append({
            "batch_id": batch_id,
            "queue_start": subset[0]["queue_id"],
            "queue_end": subset[-1]["queue_id"],
            "candidate_count": str(len(subset)),
            "priority_counts": ";".join(f"{p}={sum(row['priority']==p for row in subset)}" for p in ("P1", "P2", "P3") if any(row["priority"] == p for row in subset)),
            "review_status": "queued",
            "write_scope": "23A queue/audit files only",
        })
    batch_path = OUT / "module23a_batch_plan.tsv"
    with batch_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(batches[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(batches)

    print(f"queue_rows={len(rows)}")
    print(f"queue_unique_keys={len(seen)}")
    print(f"batches={len(batches)}")
    print("priority_counts=" + ";".join(f"{p}={sum(row['priority']==p for row in rows)}" for p in ("P1", "P2", "P3")))
    print("class_counts=" + ";".join(f"{cls}={sum(row['candidate_class']==cls for row in rows)}" for cls in sorted({row['candidate_class'] for row in rows})))


if __name__ == "__main__":
    main()
