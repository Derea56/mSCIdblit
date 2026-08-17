#!/usr/bin/env python3
"""Build the Module 24A audit-layer queue from local candidate inventories."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent

CONNECTOME_COMPLEMENT = ROOT / "work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/by_family/complement_family.tsv"
CONNECTOME_DAMP = ROOT / "work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/by_family/damp_purinergic_tlr_family.tsv"
CELLCHAT_COMPLEMENT = ROOT / "work/module20_db_seed/overnight_runs_v2/review_slices_consolidated/by_family/complement_family.tsv"
CELLCHAT_DAMP = ROOT / "work/module20_db_seed/overnight_runs_v2/review_slices_consolidated/by_family/damp_purinergic_tlr_family.tsv"
GTOPDB = ROOT / "work/module20_db_seed/gtopdb_module20_priority_seeds/gtopdb_endogenous_module20_priority_mouse.tsv"

FIELDS = [
    "queue_id",
    "batch_id",
    "priority",
    "candidate_class",
    "upstream_signal_or_release_feature",
    "target_or_receptor_system",
    "protease_activation_or_processing_logic",
    "proximal_relay_to_validate",
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


def pair_key(source: str, target: str) -> str:
    return f"{norm(source)}|{norm(target)}"


def branch_for_target(source: str, target: str, family: str = "") -> str:
    text = f"{source} {target} {family}".lower()
    if any(x in text for x in ("c3ar", "c5ar", "c1q", "complement")):
        return "complement-cleavage-product-receptor;validate-C3/C5-convertase-and-anaphylatoxin-context"
    if any(x in text for x in ("p2x", "p2y", "adenosine", "atp", "udp")):
        return "purinergic-ectonucleotidase-receptor-relay;validate-ATP-release-versus-receptor-activation"
    if any(x in text for x in ("tacr", "substance p", "neurokinin")):
        return "tachykinin-NK-receptor-G-protein-relay;validate-neurogenic-inflammation-context"
    if any(x in text for x in ("fpr", "fam3d")):
        return "formyl-peptide-receptor-G-protein-relay;validate-ligand-processing"
    if any(x in text for x in ("tlr", "rage", "hmgb1", "s100", "dcn")):
        return "DAMP-sensor-NF-kB/MAPK-relay;retain-Module18/17-boundary"
    return "target-specific relay to validate"


def priority_for_database(source: str, target: str, family: str = "") -> str:
    text = f"{source} {target} {family}".lower()
    if any(x in text for x in ("c3ar", "c5ar", "p2x7", "p2y12", "p2ry14", "tacr", "fpr", "protease", "par1", "par2", "par4")):
        return "P1"
    if any(x in text for x in ("complement", "purinergic", "trem2", "c1q", "hmgb1", "rage", "s100", "lipid")):
        return "P2"
    return "P3"


def priority_for_gap(category: str) -> str:
    return "P1" if category in {"coagulation_PAR", "complement_anaphylatoxin", "kinin_B1_B2"} else "P2"


def add_source_row(rows: list[dict[str, str]], seen: set[tuple[str, str, str]], row: dict[str, str]) -> None:
    key = (row["candidate_class"], pair_key(row["upstream_signal_or_release_feature"], row["target_or_receptor_system"]), row["proximal_relay_to_validate"].lower())
    if key in seen:
        return
    seen.add(key)
    rows.append(row)


def main() -> None:
    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str, str]] = set()

    def add(**kwargs: str) -> None:
        add_source_row(rows, seen, kwargs)

    for path, origin, family_class in [
        (CONNECTOME_COMPLEMENT, "ConnectomeDB mouse priority complement review slice", "complement"),
        (CONNECTOME_DAMP, "ConnectomeDB mouse priority DAMP/purinergic/TLR review slice", "damp_purinergic"),
    ]:
        for source in read_tsv(path):
            ligand, target = source["lr_pair"].split(" ", 1)
            add(
                queue_id="", batch_id="", priority=priority_for_database(ligand, target, source["matched_families"]),
                candidate_class=f"connectome_{family_class}_candidate",
                upstream_signal_or_release_feature=ligand, target_or_receptor_system=target,
                protease_activation_or_processing_logic="not asserted; inspect cleavage/processing only if relevant",
                proximal_relay_to_validate=branch_for_target(ligand, target, source["matched_families"]),
                downstream_tf_or_program_target="not asserted; extract only if directly measured",
                evidence_layers_to_extract="ligand/release identity or receptor engagement;receptor-proximal relay;downstream pathway or cellular function",
                species_context=source["species_note"], cell_type_or_model_context="SCI-relevant cell/compartment unresolved; extract exact primary model",
                source_origin=origin, source_record_id=source["interaction_id"],
                stable_source_locator=f"local:{path.relative_to(ROOT)}",
                search_boundary="ConnectomeDB seed only; do not promote complement/DAMP receptor engagement or downstream relay without primary validation",
                status="queued_boundary_review" if source["module20a_bucket"] == "boundary_review" else "queued",
                notes=f"Module20A bucket={source['module20a_bucket']}; next action={source['next_action']}; matched family={source['matched_families']}",
            )

    for path, origin, family_class in [
        (CELLCHAT_COMPLEMENT, "CellChatDB.mouse consolidated complement-family slice", "cellchat_complement"),
        (CELLCHAT_DAMP, "CellChatDB.mouse consolidated DAMP/purinergic slice", "cellchat_damp_purinergic"),
    ]:
        for source in read_tsv(path):
            # Chemokine-only rows belong to the cytokine/chemokine layer; retain
            # only complement or DAMP/purinergic rows for 24A.
            if family_class == "cellchat_complement" and source["matched_families"] != "complement_family":
                continue
            ligand, target = source["pair_label"].split(" ", 1)
            add(
                queue_id="", batch_id="", priority=priority_for_database(ligand, target, source["matched_families"]),
                candidate_class=f"{family_class}_candidate",
                upstream_signal_or_release_feature=ligand, target_or_receptor_system=target,
                protease_activation_or_processing_logic="not asserted; distinguish complement fragment identity from generic ligand annotation",
                proximal_relay_to_validate=branch_for_target(ligand, target, source["matched_families"]),
                downstream_tf_or_program_target="not asserted; extract only if directly measured",
                evidence_layers_to_extract="ligand/release identity or receptor engagement;receptor-proximal relay;downstream pathway or cellular function",
                species_context=source["species_note"], cell_type_or_model_context="SCI-relevant cell/compartment unresolved; extract exact primary model",
                source_origin=origin, source_record_id=source["source_record_id"],
                stable_source_locator=f"local:{path.relative_to(ROOT)}",
                search_boundary="CellChat/KEGG seed only; chemokine-only overlap routed out; direct binding, activation, and relay require primary evidence",
                status="queued",
                notes=f"Module20A bucket={source['module20a_bucket']}; next action={source['next_action']}; matched family={source['matched_families']}",
            )

    for source in read_tsv(GTOPDB):
        family = source["target_family_name"]
        matched = source["matched_families"]
        relevant = (
            "complement_family" in matched
            or "damp_purinergic_tlr_family" in matched
            or family in {"Tachykinin receptors", "P2Y receptors", "P2X receptors", "Transient Receptor Potential channels (TRP)"}
        )
        if not relevant:
            continue
        ligand, target = source["pair_label"].split(" ", 1)
        add(
            queue_id="", batch_id="", priority=priority_for_database(ligand, target, matched),
            candidate_class="gtopdb_noncanonical_receptor_candidate",
            upstream_signal_or_release_feature=ligand, target_or_receptor_system=target,
            protease_activation_or_processing_logic="not asserted; pharmacology source may describe agonism without endogenous release or cleavage",
            proximal_relay_to_validate=branch_for_target(ligand, target, matched),
            downstream_tf_or_program_target="not asserted; extract only if directly measured",
            evidence_layers_to_extract="ligand identity/receptor pharmacology;receptor-proximal relay;downstream pathway or cellular function",
            species_context=source["species_note"], cell_type_or_model_context="species/cell context from primary interaction papers unresolved",
            source_origin="Guide to Pharmacology endogenous mouse priority seed", source_record_id=source["source_record_id"],
            stable_source_locator=f"local:{GTOPDB.relative_to(ROOT)}",
            search_boundary="GtoPdb pharmacology seed only; interaction PMIDs may be absent; verify endogenous ligand, species, receptor activation, and downstream function in primary sources",
            status="queued_primary_first" if source["interaction_pmids"] or source["rank_potency_pmids"] else "queued",
            notes=f"family={family}; matched={matched}; interaction_pmids={source['interaction_pmids'] or 'none'}",
        )

    module18_targets = [
        ("M18B-E002", "extracellular ATP", "P2X7R", "ATP release/purinergic ion-channel activation", "calcium overload and neuronal death", "PMID:15258577", "Rat impact SCI", "acute SCI neurons/peritraumatic tissue", "Extracellular ATP can establish receptor engagement only where antagonists/agonists are specific; retain channel versus inflammasome outputs"),
        ("M18B-E003", "P2X7R", "microglial/gliotic inflammation", "P2X7R inflammatory relay", "microglial activation, gliosis, neutrophils, functional deficit", "PMCID:PMC2718350", "Mouse traumatic SCI", "microglia, astrocytes, neutrophils", "Systemic BBG is not perfectly receptor-specific; keep phenotype separate from direct ATP binding"),
        ("M18B-E011", "C1q", "synaptic engulfment", "complement-linked phagocytic/synaptic relay", "synaptic loss and motor recovery", "local:modules/Module_18B_TRACKER.md", "Mouse SCI and BMDM", "foam-cell macrophages, microglia, synaptic compartment", "C1q was measured downstream of lipid accumulation; direct complement receptor assignment remains separate"),
        ("M18B-E017", "foam-cell lipid accumulation", "C1q", "lipid/debris-to-complement induction", "C1q-associated synaptic engulfment", "local:modules/Module_18B_TRACKER.md", "Mouse SCI and macrophage culture", "foam-cell and lesion macrophage states", "Bazedoxifene target specificity and causal lipid species remain unresolved"),
        ("M18B-E020", "TREM2", "PI3K-AKT/DAM debris program", "debris-sensor phagocytic relay", "debris clearance, fibrosis/inflammation tradeoff", "local:modules/Module_18B_TRACKER.md", "Mouse SCI", "microglia/macrophages and myelin debris", "TREM2 activation is timing-dependent; do not collapse early clearance and late fibrosis"),
        ("M18B-E030", "P2Y12R", "CD39/CD73 -> adenosine/A1R", "ATP-to-adenosine ectonucleotidase relay", "neuronal PINK1/Parkin/LC3 mitophagy", "local:modules/Module_18B_TRACKER.md", "Microglia-neuron co-culture", "microglia and neurons", "P2Y12R, CD39/CD73, A1R, and mitophagy blockade must remain separate causal steps"),
        ("M18B-E031", "P2Y12R/adenosine", "PINK1/Parkin neuronal mitophagy", "purinergic-mitochondrial repair relay", "myelin, axon, neuronal, and locomotor repair", "local:modules/Module_18B_TRACKER.md", "Mouse SCI", "neurons, axons, myelin, injured cord", "Long-term function is not proof of a direct P2Y12R-to-mitophagy molecular edge"),
        ("M18B-E015", "extracellular traps", "LL37/P2X7R/NF-kappaB", "trap-product purinergic inflammatory relay", "M1-like macrophage/microglia polarization", "local:modules/Module_18B_TRACKER.md", "Rat SCI and human serum", "extracellular traps, macrophages/microglia", "Human serum correlations are not intervention evidence; receptor necessity is unresolved"),
        ("M18B-E032", "astrocyte CCN1", "microglial SDC4/lipid buffering", "matricellular-lipid/debris relay", "debris handling and repair-associated buffering", "local:modules/Module_18B_TRACKER.md", "Mouse SCI and human CNS comparator", "lesion-remote astrocytes and microglia", "CCN1-SDC4 is a cross-module adhesion/lipid relay; preserve the Module 23A boundary"),
        ("M18B-E043", "CCN1 loss", "SDC4 relay", "CCN1-SDC4 microglial repair relay", "neurologic recovery and debris clearance", "local:modules/Module_18B_TRACKER.md", "Mouse SCI", "astrocyte-microglia lesion context", "Causal depletion evidence does not establish a purified CCN1-SDC4 binding assay"),
    ]
    for source_id, source, target, relay, function, locator, species, context, boundary in module18_targets:
        add(
            queue_id="", batch_id="", priority="P1" if source_id in {"M18B-E002", "M18B-E011", "M18B-E030"} else "P2",
            candidate_class="module18_24a_reuse_candidate", upstream_signal_or_release_feature=source,
            target_or_receptor_system=target, protease_activation_or_processing_logic="not asserted; extract release, cleavage, oligomerization, or enzymatic conversion only when measured",
            proximal_relay_to_validate=relay, downstream_tf_or_program_target=function,
            evidence_layers_to_extract="release/identity;receptor or sensor engagement;proximal relay;downstream pathway or cellular function",
            species_context=species, cell_type_or_model_context=context,
            source_origin="Module 18B read-only cross-module reuse seed", source_record_id=source_id,
            stable_source_locator=locator, search_boundary=boundary,
            status="queued_18_reuse_review", notes="Module18 evidence is reused as a 24A seed only; no Module18 record is altered",
        )

    gap_targets = [
        ("complement_anaphylatoxin", "C3a/C5a cleavage products", "C3aR/C5aR1/C5aR2", "convertase cleavage -> anaphylatoxin receptor", "NF-kB/MAPK, neutrophil/endothelial/glial state", "primary complement cleavage and SCI-context search required"),
        ("coagulation_PAR", "thrombin", "PAR1/PAR3/PAR4", "proteolytic receptor tethered-ligand unmasking", "Rho/ERK/NF-kB, vascular and glial response", "primary thrombin-PAR search required"),
        ("coagulation_PAR", "factor Xa", "PAR2", "protease cleavage of PAR2", "ERK/NF-kB and vascular permeability", "primary factor-Xa/PAR2 search required"),
        ("coagulation_PAR", "activated protein C", "PAR1/EPCR", "protease-activated cytoprotective PAR1 signaling", "endothelial barrier, NF-kB, neuroprotection", "primary APC-PAR1/EPCR search required"),
        ("kinin_B1_B2", "bradykinin", "BDKRB1/BDKRB2", "kallikrein-kinin generation and receptor activation", "Gq/PLC/Ca2+/ERK, vascular pain/inflammation", "primary kinin receptor and SCI-context search required"),
        ("lipid_eicosanoid", "PGE2", "EP2/EP4", "COX-derived lipid mediator generation", "cAMP/PKA/EPAC and glial/vascular function", "primary PGE2 receptor branch search required"),
        ("lipid_eicosanoid", "LTB4", "BLT1/BLT2", "5-LOX-derived leukotriene generation", "G-protein/NF-kB and neutrophil recruitment", "primary LTB4 receptor branch search required"),
        ("lipid_sphingolipid", "sphingosine-1-phosphate", "S1PR1/S1PR2/S1PR3", "sphingolipid kinase/export and receptor activation", "Gi/Gq/Rho, endothelial barrier and immune trafficking", "primary S1P receptor branch search required"),
        ("lipid_resolution", "resolvin/pro-resolving lipid mediators", "FPR2/ALX/GPR32", "specialized pro-resolving mediator generation", "resolution, efferocytosis, NF-kB suppression", "primary resolvin receptor and SCI-context search required"),
        ("protease_matrix", "MMP2/MMP9", "ECM substrates and protease-sensitive receptors", "extracellular proteolysis and ligand release", "vascular permeability, matrix remodeling, inflammation", "separate proteolysis from receptor activation; primary SCI search required"),
        ("protease_PAR", "trypsin/plasmin/kallikrein", "PAR2/PAR1", "protease-specific PAR cleavage", "ERK/NF-kB, pain and neurogenic inflammation", "primary protease-PAR specificity search required"),
    ]
    for category, source, target, logic, function, boundary in gap_targets:
        add(
            queue_id="", batch_id="", priority=priority_for_gap(category), candidate_class="category_gap_target",
            upstream_signal_or_release_feature=source, target_or_receptor_system=target,
            protease_activation_or_processing_logic=logic, proximal_relay_to_validate=logic,
            downstream_tf_or_program_target=function,
            evidence_layers_to_extract="ligand/mediator identity or proteolytic processing;receptor engagement;proximal relay;downstream pathway or cellular function",
            species_context="not yet resolved", cell_type_or_model_context="SCI vascular, glial, immune, and lesion contexts to search",
            source_origin="Module 24A category gap from tracker scope", source_record_id=f"M24A-GAP-{category}",
            stable_source_locator="none identified; targeted PubMed/PMC/primary-paper search required",
            search_boundary=boundary, status="queued_search_gap", notes="Explicit no-evidence/search-gap target; not an inferred edge",
        )

    rank = {"P1": 1, "P2": 2, "P3": 3}
    rows.sort(key=lambda r: (rank[r["priority"]], r["candidate_class"], r["upstream_signal_or_release_feature"].lower(), r["target_or_receptor_system"].lower(), r["source_record_id"]))
    for i, row in enumerate(rows, 1):
        row["queue_id"] = f"M24A-Q{i:04d}"
        row["batch_id"] = f"M24A-B{((i - 1) // 50) + 1:03d}"

    with (OUT / "module24a_extraction_queue.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    batches = []
    for batch_id in sorted({r["batch_id"] for r in rows}):
        subset = [r for r in rows if r["batch_id"] == batch_id]
        batches.append({
            "batch_id": batch_id,
            "queue_start": subset[0]["queue_id"],
            "queue_end": subset[-1]["queue_id"],
            "candidate_count": str(len(subset)),
            "priority_counts": ";".join(f"{p}={sum(r['priority']==p for r in subset)}" for p in ("P1", "P2", "P3") if any(r["priority"] == p for r in subset)),
            "review_status": "queued",
            "write_scope": "24A queue/audit files only",
        })
    with (OUT / "module24a_batch_plan.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(batches[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(batches)

    print(f"queue_rows={len(rows)}")
    print(f"queue_unique_keys={len(seen)}")
    print(f"batches={len(batches)}")
    print("priority_counts=" + ";".join(f"{p}={sum(r['priority']==p for r in rows)}" for p in ("P1", "P2", "P3")))
    print("class_counts=" + ";".join(f"{c}={sum(r['candidate_class']==c for r in rows)}" for c in sorted({r['candidate_class'] for r in rows})))


if __name__ == "__main__":
    main()
