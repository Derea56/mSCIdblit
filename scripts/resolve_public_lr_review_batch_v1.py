#!/usr/bin/env python3
"""Record an evidence-bounded resolution for one public LR review batch.

This is a curation ledger, not a confidence model.  It records why a public
candidate was retained, held, or rejected for graph materialization.  Only
the exact primary-supported candidate named in the batch rules below is
eligible for a later graph build; composite overlaps remain boundary evidence.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / "data/processed/public_database_comparison_v2/candidate_triage_v1/review_batches/batch_001.tsv"
DEFAULT_BUNDLE = ROOT / "data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion243"
DEFAULT_OUTPUT = ROOT / "data/processed/public_database_comparison_v2/candidate_triage_v1/batch_001_review_resolution.tsv"
LOCATOR = re.compile(r"(?:PMID:\d+|PMCID:PMC\d+|DOI:10\.\d{4,9}/[^;\s]+)", re.IGNORECASE)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def locators(value: str) -> list[str]:
    return sorted(set(LOCATOR.findall(value or "")), key=str.casefold)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    batch = read_tsv(args.batch)
    if not batch:
        raise SystemExit("batch is empty")
    edge_sources = read_tsv(args.bundle_dir / "mechanism_edge_sources.tsv")
    sources_by_edge: dict[str, list[dict[str, str]]] = {}
    for source in edge_sources:
        sources_by_edge.setdefault(source.get("edge_id", ""), []).append(source)

    fields = [
        "candidate_unit_id", "review_batch", "normalized_ligand_key", "normalized_receptor_key",
        "disposition", "matched_graph_edge_ids", "supporting_primary_locators", "reviewed_source_locators",
        "evidence_layer", "species_support", "evidence_summary", "limitations", "review_status",
    ]
    output: list[dict[str, str]] = []
    for row in batch:
        candidate = row["candidate_unit_id"]
        ligand = row["normalized_ligand_key"]
        receptor = row["normalized_receptor_key"]
        matched_ids = row.get("matched_graph_edge_ids", "")
        reviewed = locators(row.get("evidence_notes", ""))
        primary = []
        for edge_id in filter(None, matched_ids.split(";")):
            for source in sources_by_edge.get(edge_id, []):
                if "primary" in source.get("source_kind", "").casefold() or source.get("support_kind") == "primary_experiment":
                    primary.extend(locators(source.get("source_locator", "")))
        primary = sorted(set(primary), key=str.casefold)
        species = ""

        if row.get("review_lane") == "alias_adjudication":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            summary = (
                "The public row is a composite or receptor-complex representation with component overlap to "
                "one or more graph edges. The matched component edge(s) are retained as evidence, but the "
                "full public topology is not asserted as one edge."
            )
            limitations = (
                "No new edge is materialized. Co-receptor, ternary-complex, or multi-subunit scope requires "
                "an exact primary study before promotion."
            )
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    species_value = source.get("species_support", "").strip()
                    if species_value:
                        species = "; ".join(sorted(set(filter(None, (species + "; " + species_value).split("; ")))))
        elif ligand == "BST2" and receptor == "PIRA2":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E001953"
            primary = ["PMID:20193018", "PMCID:PMC2919054", "DOI:10.4049/jimmunol.2009.099527"]
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            species = "human"
            summary = "The graph already contains the primary-supported BST2/CD317-to-ILT7/LILRA4 interaction under the PIRA2/ILT7 receptor alias."
            limitations = "Preserve the human pDC and ILT7-Fc-epsilonRI-gamma context; do not duplicate the edge or infer a universal downstream route from the alias match."
        elif ligand == "CADM1" and receptor == "CADM1":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E001387"
            primary = ["PMID:24503895", "PMCID:PMC3913574", "DOI:10.1371/journal.pone.0082894"]
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            species = "human; dog"
            summary = "The graph already contains the primary-supported trans-homophilic CADM1 adhesion edge and its bounded PI3K-associated functional context."
            limitations = "Preserve homophilic CADM1 adhesion and the reported MAGuK-PI3K/Akt/Rac1 assay context; do not infer a universal CADM1 relay or terminal-TF output."
        elif ligand == "CD48" and receptor == "CD244A":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E000670"
            primary = ["PMID:9841922", "PMCID:PMC2212392", "PMID:18523281", "DOI:10.4049/jimmunol.180.12.8159"]
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            species = "human; mouse"
            summary = "The graph already contains the primary-supported CD48-to-CD244/2B4 interaction under the CD244A receptor alias."
            limitations = "Preserve the CD48/2B4 species and immune-cell assay context; do not duplicate the edge or infer a complete signaling chain from receptor engagement alone."
        elif ligand == "CD55B" and receptor == "ADGRE5":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E000945"
            primary = ["PMID:9064337", "PMCID:PMC2192782", "DOI:10.1084/jem.184.3.1185"]
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            species = "human"
            summary = "The graph already contains the primary-supported CD55-to-ADGRE5/CD97 adhesion edge under the CD55B nomenclature."
            limitations = "Preserve CD55/CD97 isoform and adhesion context; do not duplicate the edge or infer a universal G-protein pathway."
        elif ligand == "CD6" and receptor == "ALCAM":
            disposition = "already_present_reverse_orientation"
            matched_ids = "M21B-E000686"
            primary = ["PMID:7760007", "PMCID:PMC2192054", "PMID:16352806", "DOI:10.1182/blood-2005-09-3881"]
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            species = "human; mouse"
            summary = "The graph contains the primary-supported ALCAM/CD166-to-CD6 adhesion relationship in the reverse orientation of the public CD6>ALCAM row."
            limitations = "Preserve ALCAM as the ligand and CD6 as the receptor in the reported adhesion/costimulation context; do not add a duplicate reverse edge."
        elif ligand == "ESAM" and receptor == "ESAM":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E002214"
            primary = ["PMID:11279107", "DOI:10.1074/jbc.M100630200"]
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            species = "human; mouse"
            summary = "The graph already contains the primary-supported homophilic ESAM adhesion edge."
            limitations = "Preserve endothelial and CHO-cell aggregation assay context; do not infer a unique intracellular relay or terminal-TF output."
        elif ligand == "FCER2A" and receptor == "ITGAM+ITGB2":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E011620"
            primary = ["PMID:7621072"]
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            species = "human"
            summary = "The graph now contains primary-supported CD23/FCER2A binding to the Mac-1/ITGAM:ITGB2 integrin complex."
            limitations = "Preserve the heterologous CD23/Mac-1 binding assay and monocyte context; no unique intracellular relay or terminal-TF output is inferred."
        elif ligand == "CSPG4" and receptor == "ITGA3+ITGB1":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E011621"
            primary = ["PMID:15181153", "PMCID:PMC491820"]
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            species = "mouse; human"
            summary = "The graph now contains primary-supported NG2/CSPG4 binding and alpha3beta1 integrin-dependent endothelial response evidence."
            limitations = "Preserve soluble NG2/CSPG4, alpha3beta1 and galectin-3 cofactor context; no unique intracellular kinase sequence or terminal-TF output is inferred."
        elif ligand.startswith("H2") and receptor == "KIR3DL1":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "mouse MHC-I; human KIR comparator"
            summary = "The public row combines mouse H2 class-I nomenclature with human KIR3DL1; the cited locator does not establish an exact species-matched H2-to-KIR3DL1 edge for each paralog row."
            limitations = "Retain exact HLA/KIR3DL1 and other species-matched graph edges; do not infer mouse H2 paralog specificity from cross-species family context."
        elif ligand == "ICAM5" and receptor == "CD209A":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_review_locator"
            summary = "The cited public locator concerns ICAM5 adhesion biology but does not verify an exact ICAM5-to-CD209A binding or receptor-triggering experiment in the current pass."
            limitations = "Retain ICAM5 interactions with exact primary support, including integrin and neural adhesion contexts; do not promote ICAM5/CD209A from family-level or unrelated adhesion evidence."
        elif ligand == "INHA+INHBB" and receptor == "ACVR2B":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "as stated in primary model/assay"
            summary = "The public row encodes an inhibin/activin subunit composite rather than a single mature ligand form; exact alpha-beta composition and ACVR2B complex stoichiometry are not asserted here."
            limitations = "Require exact mature ligand-form and receptor-complex evidence before promotion; do not collapse inhibin and activin family components into one binary edge."
        elif ligand == "INS1" and receptor == "INSR":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E001429"
            primary = ["PMCID:PMC3793637"]
            layer = "ligand_receptor_binding_or_activation"
            species = "human; mouse"
            summary = "The graph already contains primary-supported insulin-to-INSR binding under the Ins1/insulin ligand alias."
            limitations = "Preserve mature insulin and INSR receptor context; do not duplicate the Ins2 or generic insulin aliases or infer a complete downstream route from receptor binding alone."
        elif ligand == "JAM2" and receptor == "ITGA3+ITGB1":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_review_locator"
            summary = "The cited primary locator supports JAM2 engagement of alpha4beta1, not the alpha3beta1 composite receptor in this public row."
            limitations = "Retain exact JAM2-alpha4beta1 evidence separately; do not promote the alpha3beta1 row from a receptor-subunit mismatch."
        elif ligand == "KLK1B4" and receptor == "NTRK1":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            summary = "Klk1b4 is a protease/NGF-complex component label, not an explicitly assayed mature neurotrophin ligand for NTRK1 in this row."
            limitations = "Require mature NGF or another explicitly defined NTRK1 ligand and direct receptor assay; do not materialize a protease-to-NTRK1 edge."
        elif ligand == "L1CAM" and receptor == "L1CAM":
            disposition = "hold_contextual_or_complex_boundary"
            matched_ids = ""
            primary = ["PMID:18701456", "PMCID:PMC2661381"]
            layer = "ligand_receptor_binding_or_activation"
            species = "human; mouse"
            summary = "Primary evidence supports trans-homophilic L1CAM adhesion, but the graph export contract disallows self-loop edges, so this relationship remains a contextual boundary rather than a materialized edge."
            limitations = "Retain the primary homophilic adhesion evidence for traversal/context review; do not encode L1CAM-to-L1CAM as a self-loop or infer an intracellular relay or terminal-TF output."
        elif ligand == "L1CAM" and receptor == "ITGA4+ITGB7":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_review_locator"
            summary = "The cited L1CAM locator supports general integrin-binding or adhesion context but does not verify the exact alpha4beta7 composite receptor in this pass."
            limitations = "Retain exact L1CAM-integrin edges already supported in the graph; require an alpha4beta7-specific primary assay before promotion."
        elif ligand == "LCK" and receptor == "CD8A+CD8B1":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            summary = "LCK is an intracellular kinase associated with CD8 coreceptor signaling, not an extracellular ligand for a ligand-receptor graph edge."
            limitations = "Represent LCK-CD8 association only in an intracellular continuation layer when explicitly modeled; do not materialize it as an extracellular ligand-to-receptor edge."
        elif ligand == "MDK" and receptor == "ITGA4+ITGB1":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "as stated in primary model/assay"
            summary = "Midkine and alpha4beta1 are reported in receptor-complex and migration contexts, but the public locator was not independently verified as an exact pair-level primary experiment in this pass."
            limitations = "Retain the existing midkine receptor-complex evidence and require the exact alpha4beta1 primary assay before adding a duplicate or more specific edge."
        elif ligand == "NAMPT" and receptor == "ITGA5+ITGB1":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            summary = "The cited NAMPT study concerns regulation of integrin expression and adhesion rather than NAMPT acting as the mature extracellular ligand for alpha5beta1."
            limitations = "Keep NAMPT-to-integrin expression/function evidence in a downstream or regulatory layer; do not materialize a direct NAMPT-alpha5beta1 ligand-receptor edge."
        elif ligand == "NECTIN1" and receptor == "CADM3":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_review_locator"
            summary = "The cited Nectin locator does not verify an exact Nectin-1-to-CADM3 interaction; the known primary study instead addresses Nectin family trans-interactions."
            limitations = "Retain exact CADM1/CADM3 and Nectin family pairs separately; require direct Nectin1/CADM3 evidence before promotion."
        elif ligand == "NECTIN3" and receptor == "NECTIN2":
            disposition = "already_present_reverse_orientation"
            matched_ids = "M21B-E002205"
            primary = ["PMID:12121624", "PMID:23027581", "PMCID:PMC3792040"]
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            species = "mouse; human"
            summary = "The graph contains the primary-supported Nectin-2/PVRL2-to-Nectin-3/PVRL3 adhesion relationship in the reverse orientation of the public row."
            limitations = "Preserve the reported heterophilic Nectin-2/Nectin-3 adhesion orientation and endothelial/junctional context; do not add a duplicate reverse edge."
        elif ligand == "NECTIN3" and receptor == "PVR":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E011623"
            primary = ["PMID:23027581", "PMCID:PMC3792040"]
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            species = "human"
            summary = "The graph now contains primary-supported Nectin-3/PVR heterophilic adhesion evidence."
            limitations = "Preserve Nectin-3/PVR endothelial trans-interaction context; no unique intracellular relay or terminal-TF output is inferred."
        elif ligand == "NECTIN3" and receptor == "TIGIT":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_review_locator"
            summary = "The cited locator does not verify Nectin-3 as a direct TIGIT ligand; the established Nectin/TIGIT axis is centered on other PVR-family ligands."
            limitations = "Require direct Nectin-3/TIGIT binding or receptor-triggering evidence before promotion."
        elif ligand == "NODAL" and receptor == "ACVR1C+ACVR2A+CFC1":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "as stated in primary model/assay"
            summary = "The public row is a multi-component Nodal/Cripto receptor-complex representation; component overlap does not establish the full composite topology as one edge."
            limitations = "Retain exact Nodal receptor-complex edges and require primary complex-level evidence before promoting this composite row."
        elif ligand == "NRXN1" and receptor == "DAG1":
            disposition = "already_present_reverse_orientation"
            matched_ids = "M21B-E002387"
            primary = ["PMID:21628410"]
            layer = "ligand_receptor_binding_or_activation"
            species = "mouse; human comparator"
            summary = "The graph contains the primary-supported DAG1-to-NRXN1 interaction in the reverse orientation of the public row."
            limitations = "Preserve the alpha-dystroglycan/neurexin adhesion context; do not add a duplicate reverse edge or infer a complete intracellular route."
        elif ligand == "NRXN2" and receptor == "DAG1":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "mouse; human family comparator"
            summary = "Neurexin/dystroglycan family evidence is present, but the exact NRXN2-to-DAG1 pair was not independently verified as a primary experiment in this pass."
            limitations = "Require exact NRXN2/DAG1 mapping before promotion; preserve the existing DAG1/NRXN1 evidence without extending it across neurexin paralogs."
        elif (ligand, receptor) in {
            ("NRXN1", "LRRTM1"), ("NRXN1", "LRRTM2"),
            ("NRXN2", "LRRTM1"), ("NRXN2", "LRRTM2"),
            ("NRXN3", "LRRTM1"), ("NRXN3", "LRRTM2"),
        }:
            edge_map = {
                ("NRXN1", "LRRTM1"): "M21B-E002365",
                ("NRXN1", "LRRTM2"): "M21B-E002137",
                ("NRXN2", "LRRTM1"): "M21B-E005164",
                ("NRXN2", "LRRTM2"): "M21B-E005166",
                ("NRXN3", "LRRTM1"): "M21B-E005165",
                ("NRXN3", "LRRTM2"): "M21B-E005167",
            }
            disposition = "already_present_reverse_orientation"
            matched_ids = edge_map[(ligand, receptor)]
            primary = ["PMID:20064387", "PMID:20064388", "PMID:20519524"]
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            species = "human; mouse"
            summary = "The graph contains the primary-supported LRRTM/neurexin adhesion relationship in the reverse orientation of the public neurexin-to-LRRTM row."
            limitations = "Preserve neurexin splice-variant and LRRTM paralog context; do not infer a universal synaptic route or terminal-TF output."
        elif ligand.startswith("NRXN") and receptor.startswith("LRRTM"):
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "human; mouse family comparator"
            summary = "The public neurexin-to-LRRTM row overlaps a primary-supported family interaction, but this exact paralog pair is not represented by a verified graph edge in the current release."
            limitations = "Retain exact LRRTM1/2-to-neurexin graph edges and require pair-specific primary mapping before promoting LRRTM3/4 combinations."
        elif ligand == "PGF" and receptor == "FLT1":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M20B-E004506"
            primary = []
            layer = "ligand_receptor_binding_or_activation"
            species = "mouse release scope"
            summary = "The graph already contains the PlGF/PGF-to-FLT1 relationship under the Pgf ligand alias."
            limitations = "Preserve the graph's frozen ligand-receptor scope and do not infer additional PGF receptor complexes from this alias match."
        elif ligand == "POSTN" and receptor in {"ITGAV+ITGB3", "ITGAV+ITGB5"}:
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E000710" if receptor == "ITGAV+ITGB3" else "M21B-E000711"
            primary = ["PMID:19695571", "PMCID:PMC2841688", "DOI:10.1016/j.atherosclerosis.2009.07.046"]
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            species = "human; mouse"
            summary = "The graph already contains primary-supported periostin binding/function through the corresponding alphaV integrin complex."
            limitations = "Preserve the alphaVbeta3/alphaVbeta5 and FAK/migration context; no unique intracellular relay or terminal-TF output is inferred."
        elif ligand == "PTPRC" and receptor == "CD22":
            disposition = "already_present_reverse_orientation"
            matched_ids = "M21B-E005458"
            primary = ["PMID:12115612"]
            layer = "ligand_receptor_binding_or_activation"
            species = "as stated in primary model/assay"
            summary = "The graph contains the primary-supported CD22-to-PTPRC/CD45 interaction in the reverse orientation of the public row."
            limitations = "Preserve the CD22/CD45 cis-sialoglycoprotein context; do not add a duplicate reverse edge or infer a complete B-cell signaling route."
        elif ligand == "SELL" and receptor == "PODXL":
            disposition = "already_present_reverse_orientation"
            matched_ids = "M21B-E000291"
            primary = ["PMID:22814396"]
            layer = "ligand_receptor_binding_or_activation"
            species = "as stated in primary model/assay"
            summary = "The graph contains the primary-supported PODXL/endoglycan-to-SELL/L-selectin adhesion relationship in the reverse orientation of the public row."
            limitations = "Preserve selectin ligand glycoform and leukocyte-adhesion context; do not add a duplicate reverse edge."
        elif ligand.startswith("SEMA3") and ("+" in receptor or "_" in receptor):
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "as stated in primary model/assay"
            summary = "The public semaphorin row is a multi-subunit neuropilin/plexin receptor-complex representation; family or review evidence does not verify every composite paralog combination in this packet."
            limitations = "Retain exact primary-supported semaphorin receptor complexes already in the graph; require exact complex-level evidence before promoting additional combinations."
        elif ligand == "SIGLEC1" and receptor == "SPN":
            disposition = "already_present_reverse_orientation"
            matched_ids = "M21B-E002848"
            primary = ["PMID:11238599"]
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            species = "mouse"
            summary = "The graph contains the primary-supported CD43/SPN-to-SIGLEC1 adhesion relationship in the reverse orientation of the public receptor-to-ligand row."
            limitations = "Preserve sialic-acid-dependent CD43 glycoform and mouse T-cell/macrophage context; do not add a duplicate reverse edge."
        elif ligand.startswith("SIRPB1") and receptor == "CD47":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "human; mouse paralog comparator"
            summary = "The public row assigns CD47 binding to SIRPB1 paralogs, but the cited evidence does not establish the exact SIRPB1A/B/C pair as a primary receptor-ligand interaction in the current pass."
            limitations = "Do not extend CD47/SIRPA evidence to SIRPB1 paralogs without exact binding data; retain SIRPB1-DAP12 and SFTPD-SIRPB1 edges separately."
        elif ligand == "VEGFC" and receptor == "FLT4+KDR":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "as stated in primary model/assay"
            summary = "The public row is a composite FLT4/KDR receptor representation, while the graph stores the primary-supported VEGFC interactions with FLT4 and KDR as separate edges."
            limitations = "Retain the separate VEGFC-FLT4 and VEGFC-KDR edges; do not infer a single composite receptor topology without exact primary complex evidence."
        elif ligand.startswith("WNT") and receptor.startswith("FZD") and "+LRP" in receptor:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "as stated in primary model/assay"
            summary = "The public row is a Frizzled/LRP co-receptor complex representation; the cited locator supports Wnt pathway context but not this exact Wnt/FZD/LRP topology as one primary edge."
            limitations = "Require exact mature Wnt ligand and receptor-complex evidence before promotion; do not collapse pathway membership into a binary composite edge."
        elif ligand.startswith("AKR1C") and "CHRNG" in ligand and receptor == "PTGFR":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            summary = "The public row uses a composite steroid-metabolism and receptor-subunit label rather than a mature prostaglandin ligand directly assayed against PTGFR."
            limitations = "Do not materialize AKR1C/CHRNG composite machinery as a PTGFR ligand; retain mature prostaglandin-to-PTGFR evidence only when the ligand form and receptor assay are explicit."
        elif ligand in {"C4A", "CCL1", "CCL8", "CEACAM2"} or (ligand == "CD200" and receptor == "CD200R3"):
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_review_locator"
            summary = "The public locator was reviewed, but it did not verify an exact primary experiment for this ligand-receptor pair in the current pass."
            limitations = "Retain for targeted primary verification; do not infer C4A/C3AR1, CCL/ACKR1, CEACAM2/SELE, or CD200/CD200R3 from family or receptor-paralog evidence alone."
        elif ligand == "CD52" and receptor == "SIGLECG":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "mouse; human comparator"
            summary = "The cited CD52 evidence supports soluble human CD52 binding to SIGLEC10, whereas the public row uses mouse SIGLECG/Siglec-G; exact paralog and species mapping is unresolved."
            limitations = "Retain human CD52-SIGLEC10 family context without promoting a mouse CD52-SIGLECG edge from orthology alone."
        elif ligand.startswith("CLEC2") and receptor.startswith("KLRB1"):
            disposition = "hold_contextual_or_complex_boundary"
            layer = "candidate_only_review_locator"
            primary = []
            species = "mouse; human family comparator"
            summary = "The cited locator is a family review covering multiple mouse Clr/NKR-P1 paralogs; it does not verify every exact CLEC2-to-KLRB1 paralog row in this packet."
            limitations = "Preserve only exact graph-supported paralog pairs; require a primary binding or receptor-triggering assay before promoting additional CLEC2/KLRB1 combinations."
        elif ligand in {"DDC+SLC18A1", "DDC+SLC18A2", "DDC+SLC6A3"}:
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            summary = "The public row uses dopamine biosynthesis or vesicular transport machinery as a composite ligand label rather than the mature neurotransmitter ligand."
            limitations = "Do not materialize enzyme/transporter-to-dopamine-receptor edges; mature dopamine-to-DRD relationships require an explicit ligand-form and receptor assay."
        elif (
            ("GLS" in ligand and any(token in ligand for token in ("SLC1A", "SLC17A")))
            and (receptor.startswith("GRIK") or receptor.startswith("GRIN"))
        ):
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            summary = "The public row uses glutamate synthesis and vesicular transport machinery as a composite ligand label rather than mature extracellular glutamate."
            limitations = "Do not materialize GLS/SLC17A-to-ionotropic glutamate receptor edges; retain mature glutamate-to-receptor relationships only when the ligand form and receptor assay are explicit."
        elif ligand == "ENTPD1" and receptor == "TMIGD3":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            summary = "ENTPD1/CD39 is an ectonucleotidase that can alter extracellular nucleotide/adenosine availability; it is not itself the mature ligand for TMIGD3."
            limitations = "Retain enzyme-to-metabolite signaling as a separate mechanistic possibility, but do not materialize a direct ENTPD1-to-TMIGD3 ligand-receptor edge without exact biochemical evidence."
        elif ligand in {"DSC1", "DSC2", "DSG1C"} and receptor.startswith("DSG") or (ligand == "DSC2" and receptor == "DSG2"):
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "human; mouse"
            summary = "The public desmosomal row overlaps a graph-supported desmoglein-desmocollin family interaction, but gene/paralog orientation and exact pair mapping are not fully resolved for this row."
            limitations = "Retain exact graph-supported desmosomal pairs and require explicit primary paralog mapping before promoting the remaining orientation or species combinations."
        elif ligand in {"FLRT1", "FLRT2", "FLRT3"} and receptor.startswith("UNC5"):
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "as stated in primary model/assay"
            summary = "The public FLRT-UNC5 family rows overlap several exact graph-supported FLRT/UNC5 interactions, but not every pair in this packet has a verified primary assay or unambiguous paralog mapping."
            limitations = "Keep exact graph-supported FLRT2/3-UNC5B/C/D pairs and hold unsupported FLRT1 or UNC5A combinations until exact primary evidence is located."
        elif ligand in {"BMP8A", "GDF2", "GDF5", "GDF6"} and "+" in receptor:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "as stated in primary model/assay"
            summary = "The public row is a multi-subunit BMP/GDF receptor-complex representation; component overlap does not establish the complete composite topology as one graph edge."
            limitations = "Require exact primary complex-level evidence before promotion; do not split or infer unsupported receptor-subunit combinations."
        elif ligand == "DSG1C" and receptor == "DSC3":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E003154"
            primary = ["PMID:27298358", "PMCID:PMC4932976", "DOI:10.1073/pnas.1606272113"]
            layer = "ligand_receptor_binding_or_activation"
            species = "human; mouse"
            summary = "The graph contains the primary-supported DSG1-to-DSC3 desmosomal interaction under the DSG1C nomenclature."
            limitations = "Preserve desmosomal cadherin paralog and adhesion context; do not infer intracellular signaling from the adhesion edge alone."
        elif ligand == "NTF3" and receptor == "NGFR":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E000751"
            primary = ["PMID:18596692", "PMID:7744005"]
            layer = "ligand_receptor_binding_or_activation"
            species = "as stated in primary model/assay"
            summary = "The graph already contains the primary-supported NT3/NTF3-to-NGFR/p75NTR binding edge under the mature NT3 alias."
            limitations = "Preserve the mature NT3/p75NTR binding form and the reported assay context; do not duplicate the edge or infer a complete intracellular or TF route."
        elif ligand == "TNF" and receptor == "TNFRSF1A":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E000110"
            layer = "ligand_receptor_binding_or_activation"
            species = "human"
            summary = "The graph already contains the TNF-to-TNFR1/p55 edge under the TNFRSF1A receptor alias."
            limitations = "Preserve the TNFR1/p55 nomenclature and receptor-binding context; do not duplicate the edge or infer downstream steps from this alias match alone."
        elif ligand == "TNF" and receptor == "TNFRSF1B":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E000111;M21B-E001764"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
            species = "human"
            summary = "The graph already contains TNF-to-TNFR2 receptor engagement and activation under the TNFRSF1B/TNFR2 alias."
            limitations = "Preserve TNFR2 receptor-complex and membrane/oligomerized-TNF context; do not duplicate an alias edge or collapse receptor engagement into a universal downstream route."
        elif ligand == "PTPRC" and receptor == "MRC1":
            disposition = "already_present_reverse_orientation"
            matched_ids = "M21B-E011617"
            primary = ["PMID:10575006", "DOI:10.1074/jbc.274.49.35211"]
            layer = "ligand_receptor_binding_or_activation"
            species = "as stated in primary model/assay"
            summary = "The primary study supports the reverse MRC1/mannose-receptor cysteine-rich-domain to PTPRC/CD45 counter-receptor orientation."
            limitations = "Preserve the reverse orientation and glycoform/sugar-dependent binding context; do not add a duplicate PTPRC-to-MRC1 edge or infer canonical signaling."
        elif ligand == "APP" and receptor == "SORL1":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E011618"
            primary = ["PMID:16407538", "PMCID:PMC1224625"]
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            species = "as stated in primary model/assay"
            summary = "The graph now contains the primary-supported APP-sorLA/SORL1 interaction and trafficking edge."
            limitations = "This is an APP-sorLA protein-interaction/trafficking relationship rather than a classical secreted ligand route; no unique extracellular relay or terminal-TF output is inferred."
        elif ligand == "LTA" and receptor == "TNFRSF1B":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E011619"
            primary = ["PMID:9552007"]
            layer = "ligand_receptor_binding_or_activation"
            species = "as stated in primary model/assay"
            summary = "The graph now contains the primary-supported soluble LTalpha3/LTA-to-TNFR2/TNFRSF1B binding layer."
            limitations = "Preserve soluble LTalpha3 versus membrane LTalpha1beta2 form distinctions; do not infer LTBR binding, a unique intracellular relay, or terminal-TF output."
        elif ligand in {"INHBA+INHBB"} or (ligand in {"BMP7", "BMP8A"} and "+" in receptor):
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "as stated in primary model/assay"
            summary = "The public row is a multi-subunit ligand or receptor-complex representation. Component-level graph evidence is retained, but the exact composite topology is not asserted as one edge."
            limitations = "The cited public locators do not provide a verified exact primary assay for this complete composite row; preserve component overlap and require exact complex-level evidence before promotion."
        elif ligand in {"TENM1", "TENM3", "UNC5A"} and receptor.startswith("ADGRL"):
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = []
            species = "as stated in primary model/assay"
            summary = "The reviewed citations support latrophilin/teneurin or guidance-receptor family context, but do not verify this exact ligand-receptor pair in a primary assay."
            limitations = "Retain as family-level contextual evidence; require an exact ligand, receptor, species and assay before graph promotion, and do not infer a complete intracellular or TF route."
        elif ligand == "INSL3" and receptor == "RXFP1":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            summary = "The candidate appears to use the wrong relaxin-family receptor: the verified INSL3 receptor literature supports RXFP2 rather than RXFP1."
            limitations = "Do not materialize INSL3-to-RXFP1; retain the row only for future receptor-normalization review and separately verify any INSL3-to-RXFP2 evidence."
        elif ligand in {"KNG1", "KNG2", "PDYN", "PENK", "PMCH", "POMC", "TAC1"}:
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            summary = "The public row uses a precursor gene label rather than a verified mature peptide ligand form for the receptor interaction."
            limitations = "Retain mature peptide-to-receptor relationships only when the ligand form and receptor assay are explicit; do not materialize the precursor label as a direct edge."
        elif ligand == "ENHO" and receptor == "GPR19":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:28476646"]
            species = "as stated in primary model/assay"
            summary = "The cited primary study supports adropin/ENHO-dependent GPR19-associated MAPK/ERK1/2 signaling in the reported model, but the direct ligand-receptor binding topology is not sufficiently resolved for a direct graph edge here."
            limitations = "Retain as receptor-proximal functional/contextual evidence; do not assert purified binding, a universal endogenous ENHO-GPR19 route, intracellular intermediates, or terminal-TF output."
        elif ligand == "ENTPD1" and receptor.startswith("ADORA"):
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            summary = "ENTPD1/CD39 is an ectonucleotidase in the extracellular ATP-to-adenosine pathway, not the adenosine ligand represented by the ADORA receptor rows."
            limitations = "The candidate may reflect a transcellular enzyme-to-metabolite signaling route, but it is not materialized as a direct ENTPD1-to-ADORA ligand-receptor edge; adenosine availability and receptor activation require separate evidence."
        elif ligand == "CD80" and receptor == "CD274":
            disposition = "already_present_reverse_orientation"
            matched_ids = "M21B-E005462"
            primary = ["PMID:17629517", "PMID:18585785", "PMID:20587542", "PMCID:PMC2707944", "DOI:10.1016/j.molimm.2008.05.014"]
            layer = "ligand_receptor_binding_or_activation"
            species = "human"
            summary = "The graph already contains the primary-supported PD-L1/CD274-to-B7-1/CD80 cis interaction in the reverse orientation."
            limitations = "Preserve the cis interaction orientation and human biochemical/cell-adhesion context; do not add a duplicate CD80-to-CD274 edge or infer canonical trans signaling."
        elif row.get("review_batch") == "batch_015":
            # Batch 015 mixes mature-ligand aliases, biosynthetic/transport
            # machinery, receptor-complex encodings, self-loops, and several
            # locator mismatches. Keep those distinctions explicit here so a
            # public-database row is never promoted merely because a pathway
            # database or family annotation names the same components.
            if ligand == "CD1D2" and receptor == "PIRA2":
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E011624"
                primary = ["PMID:42045157", "PMCID:PMC13253836", "DOI:10.1038/s41419-026-08789-9"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse; human"
                summary = "A current primary study directly identifies CD1d1/CD1d2 as PIRA2/LILRA2 ligands, confirms direct interaction, and reports FcRgamma-ITAM and macrophage inflammatory outputs."
                limitations = "Preserve the CD1d1/CD1d2 and murine PIRA2/LILRA2 domain, reporter, macrophage and NAFLD contexts; the edge supports receptor-proximal and functional evidence but does not assert a universal intracellular route or SCI transfer."
            elif ligand == "CD1D1" and receptor == "CEACAM5":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E002921"
                primary = ["PMID:24104458", "PMCID:PMC3981948"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "The primary study supports CEACAM5/CD66e B3-domain binding to CD1d in the reverse orientation of the public CD1D1-to-CEACAM5 row."
                limitations = "Preserve CEACAM5 domain, CD1d and intestinal/T-cell context; do not add a duplicate reverse edge or transfer the result to CEACAM1/CEACAM2 paralogs."
            elif ligand == "CD8A" and receptor == "CEACAM5":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E002920"
                primary = ["PMID:24104458", "PMCID:PMC3981948"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "The primary study supports CEACAM5/CD66e N-domain binding to CD8alpha in the reverse orientation of the public CD8A-to-CEACAM5 row."
                limitations = "Preserve CEACAM5 domain, CD8alpha and intestinal/T-cell context; do not add a duplicate reverse edge or transfer the result to CEACAM1/CEACAM2 paralogs."
            elif ligand == "CD46" and receptor == "JAG1":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E005467"
                primary = ["PMID:23086448"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "The graph contains the primary-supported Jagged1-to-CD46 interaction in the reverse orientation of the public CD46-to-JAG1 row."
                limitations = "Preserve the human CD46/Jagged1 Th1-immunity context; do not add a duplicate reverse edge or infer a complete Notch-like route."
            elif ligand in {"CD99"} and receptor in {"PILRB1", "PILRB2"}:
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E002915"
                primary = ["PMID:18234675", "PMID:18209065", "PMCID:PMC2577149"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "mouse; human comparator"
                summary = "The graph contains the CD99/D4-to-PILRB/PILRbeta interaction under the PILRB1/PILRB2 alias family; the reviewed primary supports O-glycosylated CD99 recognition by paired Ig-like receptors."
                limitations = "Preserve glycoform, paired-receptor, species and cell-assay boundaries; do not infer a universal PILRB paralog assignment or complete signaling route."
            elif ligand == "CEACAM1" and receptor == "CEACAM5":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E005471"
                primary = ["PMID:15905509"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human"
                summary = "The graph contains the primary-supported CEACAM5-to-CEACAM1 heterophilic interaction in the reverse orientation of the public CEACAM1-to-CEACAM5 row."
                limitations = "Preserve CEACAM glycoform and adhesion context; do not add a duplicate reverse edge or infer intracellular signaling from adhesion alone."
            elif ligand == "CGA+TSHB" and receptor == "TSHR":
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E001403"
                primary = ["PMID:12045259"]
                layer = "ligand_receptor_binding_or_activation"
                species = "as stated in primary model/assay"
                summary = "The public CGA+TSHB composite is retained as a TSH ligand-form alias for the existing TSH-to-TSHR edge."
                limitations = "The cited locator is not the primary TSHR ligand study in this release; preserve mature TSH and receptor context and do not treat the CGA/TSHB gene composite as an independently verified ligand form."
            elif ligand in {"ANXA1"} and receptor == "FPR2+FPR3":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000709"
                primary = ["PMID:22610094"]
                layer = "ligand_receptor_binding_or_activation"
                species = "as stated in primary model/assay"
                summary = "ANXA1/FPR2 evidence overlaps the composite FPR2+FPR3 row, but the complete multi-receptor topology is not asserted as one edge."
                limitations = "Retain the exact ANXA1-FPR2 evidence and require a primary FPR3 component assay before promoting the composite."
            elif ligand == "APOA1" and receptor == "TREM2+TYROBP":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E003868;M21B-E001120"
                primary = ["PMID:26374899", "PMCID:PMC4646257", "PMID:11602640", "PMCID:PMC2193511"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human"
                summary = "Primary evidence supports ApoA-I binding to TREM2 and a separate TREM2-DAP12/TYROBP receptor-complex association, but not one ApoA-I-to-TREM2:TYROBP composite edge."
                limitations = "Keep ligand binding and receptor-adaptor assembly as separate traversable evidence layers; do not collapse the complex or infer ligand-specific DAP12 activation without direct evidence."
            elif ligand in {"APOA2", "APP"} and receptor == "TREM2+TYROBP":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The public row is a composite TREM2/TYROBP representation, but its cited locators do not verify the exact APOA2 or APP ligand-to-complex interaction in this pass."
                limitations = "Do not transfer ApoA-I-to-TREM2 evidence to APOA2 or APP; retain each candidate for exact ligand and receptor-complex primary review."
            elif ligand == "CD200" and receptor == "CD200R1L":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000190"
                primary = ["PMID:15557172"]
                layer = "ligand_receptor_binding_or_activation"
                species = "mouse"
                summary = "The cited biology supports canonical CD200-CD200R1, while CD200R1L is a receptor-paralog label not verified as the same primary receptor in the current graph."
                limitations = "Retain the exact CD200-CD200R1 edge; do not extend it to CD200R1L by family membership or alias inference."
            elif ligand == "CD276" and receptor == "TREML2":
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:18650384", "PMID:19544488", "PMID:24328742", "PMID:31044564"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "mouse; human comparator"
                summary = "B7-H3/CD276-TLT2/TREML2 is contested: one primary study reports counter-receptor activity, while other primary studies report no interaction; the cited 31044564 locator is not an interaction study."
                limitations = "Keep as a contested contextual candidate; do not materialize a direct edge until the conflicting primary evidence is reconciled for species, construct and assay context."
            elif ligand in {"CEACAM1", "CEACAM2"} and receptor in {"CD1D1", "CD1D2", "CD8A"}:
                disposition = "no_primary_evidence_found"
                primary = ["PMID:24104458"]
                layer = "candidate_only_review_locator"
                species = "human"
                summary = "The cited CEACAM5 study supports CD1d/CD8alpha interactions for CEACAM5, not the CEACAM1 or CEACAM2 paralog rows."
                limitations = "Do not transfer CEACAM5 domain evidence to CEACAM1/CEACAM2; retain these rows for exact-paralog primary review."
            elif (ligand, receptor) in {("CEACAM1", "CEACAM2"), ("CEACAM2", "CEACAM2")}:
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:21982860"]
                layer = "ligand_receptor_binding_or_activation"
                species = "as stated in primary model/assay"
                summary = "The public locator does not establish the exact CEACAM1-CEACAM2 or CEACAM2 homophilic edge; the graph export contract also disallows self-loop materialization for CEACAM2."
                limitations = "Retain only exact primary-supported CEACAM adhesion pairs; do not encode CEACAM2-to-CEACAM2 as a self-loop."
            elif (ligand, receptor) in {("CEACAM1", "PSG20"), ("CEACAM2", "PSG20")}:
                disposition = "no_primary_evidence_found"
                primary = ["PMID:24743304"]
                layer = "candidate_only_review_locator"
                summary = "The cited locator concerns soluble CEACAM8 interaction with CEACAM1, not CEACAM1/CEACAM2 interaction with PSG20."
                limitations = "Do not infer PSG20 binding from the CEACAM8-CEACAM1 study or family-level database membership."
            elif ligand == "BAG6" and receptor == "NCR3PS":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses the NCR3PS pseudogene/paralog label, whereas the primary BAG6 ligand evidence concerns the NKp30/NCR3 receptor."
                limitations = "Retain the exact BAG6-fragment-to-NCR3/NKp30 edge; do not transfer it to NCR3PS without an exact receptor assay."
            elif ligand == "CDH12" and receptor == "ITGA1+ITGB1":
                disposition = "no_primary_evidence_found"
                primary = ["PMID:34385456"]
                layer = "candidate_only_review_locator"
                summary = "The cited locator did not verify an exact CDH12-to-alpha1beta1 integrin interaction in the current pass."
                limitations = "Require direct CDH12/ITGA1:ITGB1 binding or receptor-proximal evidence before promotion."
            elif ligand == "COL4A1" or (ligand.startswith("COL4A") and receptor == "ADGRG6"):
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E000934"
                primary = ["PMID:25118328", "PMCID:PMC4159047"]
                layer = "ligand_receptor_binding_or_activation"
                species = "mouse; human comparator"
                summary = "The collagen-IV family rows map to the existing collagen-IV-to-ADGRG6/GPR126 edge; the cited public locator is a review-level family record rather than the primary interaction locator."
                limitations = "Preserve collagen-IV family and ADGRG6/GPR126 assay context; do not treat each COL4A paralog as independently resolved from the family alias."
            elif ligand.startswith("COL4A") and receptor == "ADGRG6":
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E000934"
                primary = ["PMID:25118328", "PMCID:PMC4159047"]
                layer = "ligand_receptor_binding_or_activation"
                species = "mouse; human comparator"
                summary = "The collagen-IV family row maps to the existing collagen-IV-to-ADGRG6/GPR126 edge."
                limitations = "Preserve family and assay boundaries; do not treat each COL4A paralog as independently resolved."
            elif ligand in {"ASMT", "CEL", "CYP11B1+CYP11B2", "DAGLA", "DAGLB", "DBH+SLC18A1", "DBH+SLC18A2", "ALOX12", "ALOX5+ALOX5AP+LTC4S", "AKR1C18+AKR1C6+ALOX5+ALOX5AP+LTC4S"} or ligand.startswith("CHAT+"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses biosynthetic, enzymatic or vesicular-transport machinery as the ligand label rather than the mature secreted mediator or neurotransmitter assayed at the receptor."
                limitations = "Retain mature mediator-to-receptor edges separately; do not materialize a gene/enzyme/transporter composite as a direct ligand-receptor edge."
            elif ligand == "BMP8B" and "+" in receptor:
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:26893264"]
                layer = "ligand_receptor_binding_or_activation"
                species = "mouse"
                summary = "The row is a BMP8B multi-subunit receptor-complex prediction from pathway/database context, not an exact primary assay of the complete receptor composite."
                limitations = "Require exact BMP8B receptor-complex binding or activation evidence before promotion; do not split the composite into unsupported subunit edges."
            elif ligand == "ANXA1" and receptor.startswith("FPRRS"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:33082511"]
                layer = "ligand_receptor_binding_or_activation"
                species = "mouse"
                summary = "The public row assigns ANXA1 to an Fpr-rs paralog family, but the exact mouse paralog interaction is not resolved by the current graph evidence."
                limitations = "Retain exact ANXA1-FPR2/FPR1 evidence; require paralog-specific primary receptor assays before promotion."
            elif ligand == "CLDN1" or ligand == "CLDN2" or ligand == "CLDN3":
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:31942240"]
                layer = "ligand_receptor_binding_or_activation"
                species = "as stated in primary model/assay"
                summary = "Primary claudin adhesion evidence is retained as contextual homophilic/junctional evidence, but the graph export contract disallows self-loop edges."
                limitations = "Do not encode claudin self-loops or infer a signaling relay from junctional association alone."
            elif ligand == "CTSG" and receptor == "FPR1":
                disposition = "no_primary_evidence_found"
                primary = ["PMID:26516201"]
                layer = "candidate_only_review_locator"
                species = "human; mouse"
                summary = "The cited primary establishes ANXA1-FPR1-dependent anticancer immunity, not a direct cathepsin-G-to-FPR1 interaction; cathepsin-G/FPR1 is retained only as a future targeted candidate."
                limitations = "Do not promote CTSG-FPR1 from an IUPHAR/family annotation or a locator that names ANXA1; require an exact CTSG ligand assay."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The batch row was reviewed, but no exact primary experiment was verified for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize an edge from database membership, family context, or an unverified locator alone."
        elif row.get("review_batch") == "batch_001":
            if ligand in {"GAD1", "GAD2"} or ligand.startswith(("GAD1+", "GAD2+")):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses GAD1 plus GABA synthesis or transport machinery as the ligand label rather than mature extracellular GABA."
                limitations = "Do not materialize enzyme/transporter-to-GABA-receptor edges; retain mature GABA-to-receptor evidence only when the ligand form and receptor assay are explicit."
            elif ligand in {"FGB", "FGG"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Fibrinogen-chain labels in the public prediction are extracellular structural components, not an explicitly defined mature signaling ligand for the listed receptor."
                limitations = "Require an exact fibrinogen form, receptor identity and primary binding or functional assay before treating this as a ligand-receptor edge."
            elif ligand in {"FGF11", "FGF12", "FGF13", "FGF14"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "FGF11-14 are intracellular FGF homologous factors and are not treated as secreted FGF receptor ligands in this graph layer."
                limitations = "Represent intracellular FGF homologous-factor functions separately; do not materialize an extracellular FGF-to-FGFR edge from the public prediction alone."
            elif ligand == "FGF15" and receptor == "KLB":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                species = "mouse"
                summary = "FGF15 biology requires an FGFR/β-Klotho receptor complex; the public FGF15-to-KLB row alone does not assert the complete receptor topology."
                limitations = "Retain exact FGF15/FGFR/β-Klotho complex evidence when available; do not materialize KLB as a standalone FGF15 receptor."
            elif ligand.startswith("FGF"):
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_unverified"
                summary = "The public database row names a mature FGF family ligand, but no exact primary assay for this ligand-receptor pair was verified in the current pass."
                limitations = "Retain for targeted pair-specific primary review; do not transfer receptor specificity across FGF paralogs or infer a receptor complex from family membership."
            elif ligand in {"FST", "FSTL5"}:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_unverified"
                summary = "The public row names a follistatin-family interaction, but no exact primary ligand-receptor experiment for this pair was verified in the current pass."
                limitations = "Require exact mature ligand, receptor complex, species and assay evidence before promotion; do not transfer activin/BMP family binding across paralogs."
            elif ligand.startswith(("GLS+", "GLS2+")):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses glutamate synthesis and transport machinery as a composite ligand label rather than mature extracellular glutamate."
                limitations = "Do not materialize GLS/SLC-to-glutamate-receptor edges; retain mature glutamate-to-receptor evidence only when the ligand form and receptor assay are explicit."
            elif ligand.startswith("GNA"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "GNAS/GNA-family labels are intracellular G-protein signaling components, not extracellular ligands for the listed receptors."
                limitations = "Represent G-protein coupling in the intracellular continuation layer when directly supported; do not materialize it as a ligand-receptor edge."
            elif ligand.startswith("H2"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                species = "mouse"
                summary = "The public row uses mouse H2/MHC-I paralog labels and KEGG pathway membership; this supports a cell-surface immune-recognition context but not each exact H2-to-receptor pair as one primary edge."
                limitations = "Require exact H2 paralog, receptor, species and assay evidence before promotion; do not infer paralog specificity from MHC-family or pathway membership."
            elif ligand == "IFNA11" and receptor == "IFNAR1+IFNAR2":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E001762"
                primary = ["PMID:10493588", "PMID:23830819"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human; mouse family comparator"
                summary = "IFNA11 is retained as a type-I-interferon family alias for the existing IFN-alpha/beta-to-IFNAR1:IFNAR2 evidence, but the exact IFNA11 paralog and species-specific composite were not independently resolved here."
                limitations = "Preserve subtype, species and receptor-complex boundaries; do not treat family-level IFNAR evidence as an exact IFNA11 edge without subtype-specific primary support."
            elif ligand == "IAPP" and receptor == "RAMP2":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E001562"
                primary = ["PMID:10385705", "PMID:10871296"]
                layer = "ligand_receptor_binding_or_activation"
                species = "as stated in primary model/assay"
                summary = "Primary amylin/IAPP receptor evidence supports CALCR-containing complexes with RAMP subunits, while the public row isolates RAMP2 without asserting the complete receptor complex."
                limitations = "Retain the intact amylin receptor complex and do not materialize RAMP2 as a standalone IAPP receptor."
            elif ligand == "ICAM4" and receptor == "ITGB3":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M23B-E000574"
                primary = ["PMID:12477717", "DOI:10.1074/jbc.M211282200"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human"
                summary = "Primary evidence supports ICAM4 binding to an ITGB3-containing integrin complex, but the public row omits the intact receptor-complex partner composition."
                limitations = "Retain the complete ITGB3-containing integrin context; do not materialize a bare ICAM4-to-ITGB3 subunit edge."
            elif ligand == "GRN" and receptor in {"TNFRSF1A", "TNFRSF1B"}:
                disposition = "hold_contextual_or_complex_boundary"
                primary = []
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human; mouse comparator"
                summary = "PGRN/GRN-to-TNFR1/TNFR2 remains a contested ligand-receptor assignment in the current evidence layer, so the public rows remain contextual rather than direct graph edges."
                limitations = "Preserve the conflicting ligand-form, receptor, species and antagonist/agonist contexts; do not promote a direct GRN-TNFR edge until the primary disagreement is reconciled."
            elif ligand in {"KNG1", "KNG2"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses a kininogen precursor label rather than a defined mature kinin or other extracellular ligand form."
                limitations = "Retain mature peptide-to-receptor evidence only when the processed ligand form and receptor assay are explicit; do not materialize kininogen precursor rows as direct edges."
            elif ligand.startswith(("LAMA", "LAMB")):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                species = "as stated in primary model/assay"
                summary = "The public row overlaps laminin-chain, integrin and dystroglycan evidence, but the exact mature laminin isoform, chain composition and receptor topology are not resolved for this candidate."
                limitations = "Require exact laminin isoform/chain composition and receptor assay before promotion; do not transfer evidence across laminin chains or treat a single chain as the complete mature ligand complex."
            elif ligand == "LTF" and receptor == "TFRC":
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:2166510"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human"
                summary = "Primary lactoferrin uptake work supports a specific lactoferrin-binding receptor on HT29-D4 cells, but the cited experiment does not identify that receptor as TFRC."
                limitations = "Retain as receptor-context evidence only; do not materialize LTF-TFRC until a primary study identifies TFRC/TFR1 or TFR2 as the assayed lactoferrin receptor."
            elif ligand == "LTF":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "No exact primary experiment was verified for this lactoferrin-to-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not transfer LTF evidence from LRP1, DCC-family or IL6R contexts to unrelated receptor candidates."
            elif ligand.startswith("PCDH") and receptor.startswith("PCDH"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "mouse; human family comparator"
                summary = "The cited clustered-protocadherin studies support cell-contact recognition and strict homophilic trans specificity, but the public row is not treated as a soluble ligand route or as a general heterophilic signaling edge."
                limitations = "Preserve cis/trans orientation and isoform-specific recognition; do not promote mismatched paralog pairs or infer a unique intracellular continuation or terminal-TF output from adhesion evidence alone."
            elif ligand == "MSTN" and receptor in {
                "ACVR1B+ACVR2A", "ACVR1B+ACVR2B", "ACVR2A+TGFBR1", "ACVR2B+TGFBR1"
            }:
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:14517293", "PMID:33219121"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse"
                summary = "Primary myostatin studies support signaling through activin type-II receptors with type-I receptor partners ALK4/ACVR1B or ALK5/TGFBR1, and in vivo use of the four listed type-I/type-II combinations."
                limitations = "Preserve the composite receptor topology and muscle-cell context; this is a candidate for graph materialization after exact complex normalization, not four independent binary receptor edges."
            elif ligand == "NRG3" and receptor == "ERBB4":
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:9275162", "PMCID:PMC23218", "DOI:10.1073/pnas.94.18.9562"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human; mouse"
                summary = "Primary work shows the NRG3 EGF-like domain binds ERBB4 and stimulates ERBB4 tyrosine phosphorylation in cells."
                limitations = "Preserve the transmembrane/proteolytically released NRG3 form and neural context; no complete intracellular relay or terminal-TF output is asserted by this edge alone."
            elif ligand == "NRG3" and receptor == "ERBB2+ERBB4":
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:9275162", "PMCID:PMC23218", "DOI:10.1073/pnas.94.18.9562"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human; mouse"
                summary = "Primary NRG3 evidence supports ERBB4 binding and activation, but does not establish the complete ERBB2:ERBB4 composite receptor topology in this row."
                limitations = "Retain NRG3-to-ERBB4 as the supported receptor relationship; require exact heterodimer-complex evidence before promoting the composite row."
            elif ligand == "NRG4" and receptor == "ERBB4":
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:10348342", "DOI:10.1038/sj.onc.1202631"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human"
                summary = "Primary work shows NRG4 activates ERBB4 and not the other tested ERBB receptors or receptor combinations."
                limitations = "Preserve the NRG4 EGF-like ligand and ERBB4 assay context; no complete intracellular relay or terminal-TF output is asserted by this edge alone."
            elif ligand == "NRG4" and receptor == "ERBB2+ERBB4":
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:10348342", "DOI:10.1038/sj.onc.1202631"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human"
                summary = "Primary NRG4 work supports strict ERBB4 specificity, not the complete ERBB2:ERBB4 composite receptor topology in this row."
                limitations = "Retain NRG4-to-ERBB4 as the supported relationship; do not promote the composite receptor from pathway or complex inference."
            elif ligand == "NMB" and receptor == "GRPR":
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:19628633", "PMCID:PMC2766219", "DOI:10.1124/jpet.109.154245"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "Primary receptor-selectivity work shows NMB can interact with GRPR but has much higher affinity for NMBR; the row is retained as a lower-affinity/contextual relationship rather than an unqualified canonical edge."
                limitations = "Preserve NMBR as the preferred receptor and the assay-specific affinity context; do not infer equivalent signaling potency or a complete downstream route through GRPR."
            elif ligand == "NRTN" and receptor == "GFRA3":
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:9576965", "PMID:9407096"]
                layer = "candidate_only_unverified"
                species = "human; mouse"
                summary = "Primary GDNF-family receptor studies identify GFRA3 as an orphan co-receptor and do not establish neurturin as its ligand; neurturin is supported through GFRA1/GFRA2 complexes instead."
                limitations = "Do not transfer neurturin/GFRA1-GFRA2 evidence to GFRA3 by homology; require a direct GFRA3 ligand-binding and Ret-activation study."
            elif ligand == "NTF5" and receptor == "NTRK1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "NTF5/NT-4 is a neurotrophin whose canonical Trk receptor is NTRK2 rather than NTRK1 in the candidate row."
                limitations = "Require a direct NTF5-NTRK1 binding or activation assay before promotion; do not transfer NT-3 or NGF receptor specificity across neurotrophin paralogs."
            elif ligand == "NPPC" and receptor == "NPR1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "NPPC/CNP is canonically associated with NPR2/NPR-B, while NPR1/NPR-A is the receptor class associated with ANP and BNP in this ligand family."
                limitations = "Require a direct NPPC-NPR1 primary assay before promotion; do not infer receptor specificity from natriuretic-peptide family membership."
            elif ligand == "NPS" and receptor != "NPSR1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "NPS is an endogenous ligand of NPSR1, not an established ligand for the unrelated receptor listed in this row."
                limitations = "Require a direct NPS-to-receptor assay before promotion; do not transfer NPSR1 signaling to other GPCRs or RAMP subunits."
            elif ligand in {"MMP1A", "MMP2", "MMP7", "MMP9", "NAMPT", "MFNG"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses an extracellular protease, enzyme, or glycosyltransferase as the ligand label; that molecule is not itself established as the mature ligand for the listed receptor."
                limitations = "Represent proteolysis, substrate processing, receptor shedding, or receptor glycosylation in separate mechanistic layers when directly supported; do not materialize the enzyme-to-receptor row as a ligand-receptor edge."
            elif ligand in {"MBL2", "MDK"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                species = "as stated in primary model/assay"
                summary = "The candidate overlaps known collectin or midkine receptor-family biology, but the exact pair and mature receptor topology were not verified as a primary-supported edge in this pass."
                limitations = "Retain exact graph-supported family members and require a pair-specific primary binding or receptor-triggering assay; do not transfer evidence across receptor families or co-receptor complexes."
            elif ligand in {"MPZ", "NCAM1", "NCAN", "NEGR1", "NFASC", "NRXN3", "OCLN"}:
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "as stated in primary model/assay"
                summary = "The public row is an adhesion, junctional, or homophilic cell-contact relationship; it is retained as contextual traversal evidence rather than treated as a soluble ligand route."
                limitations = "Preserve cell-contact, cis/trans orientation and self-loop boundaries; do not infer a unique intracellular continuation or terminal-TF output from adhesion evidence alone."
            elif ligand == "PCSK9":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human; mouse"
                summary = "PCSK9 is a secreted regulator of LDL-receptor-family trafficking, but the exact candidate receptor and mature extracellular topology were not verified as a direct primary ligand-receptor edge in this pass."
                limitations = "Retain exact PCSK9-LDLR-family binding and trafficking evidence separately; require a receptor-specific primary assay before promoting PCSK9-LRP1, PCSK9-SORT1 or PCSK9-VLDLR as a direct edge."
            elif ligand == "PDGFC" and receptor in {"FLT1", "FLT4", "KDR"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "PDGFC is a PDGF-family ligand whose canonical signaling is through PDGF receptors, not the VEGF receptor tyrosine kinases listed in these rows."
                limitations = "Require a direct PDGFC-to-VEGFR binding or activation study before promotion; do not transfer PDGF-family or VEGF-family receptor specificity across ligand families."
            elif ligand in {"PDYN", "PENK"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses a propeptide precursor label rather than a defined mature opioid peptide ligand."
                limitations = "Retain mature dynorphin or enkephalin-to-opioid-receptor relationships only when the processed ligand form and receptor assay are explicit; do not materialize the precursor label directly."
            elif ligand == "NPB":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "NPB is an endogenous neuropeptide with a cognate NPBW/NmU receptor context, not an established ligand for the unrelated receptors listed in this packet."
                limitations = "Require a direct NPB-to-receptor assay before promotion; do not infer cross-family GPCR specificity from expression or pathway membership."
            elif ligand == "PGF" and receptor in {"NRP1", "NRP2"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                species = "human; mouse"
                summary = "PlGF/PGF neuropilin interactions are isoform- and receptor-context dependent; the current candidate does not resolve the mature PGF isoform or exact neuropilin assay sufficiently for direct promotion."
                limitations = "Require isoform-specific primary binding or receptor-triggering evidence before promotion; preserve VEGFR and neuropilin co-receptor topology rather than treating NRP1/NRP2 as interchangeable standalone receptors."
            elif ligand in {"PF4", "PI16", "PIP", "PLAT"}:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "No exact primary experiment was verified for this candidate ligand-receptor pair in the current pass."
                limitations = "Retain for targeted pair-specific review; do not infer direct receptor binding from chemokine, protease, extracellular-matrix, or expression-family context alone."
            elif ligand == "PIGA":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "PIGA is an intracellular GPI-anchor biosynthesis component, not a mature extracellular ligand for PIGR."
                limitations = "Represent GPI-anchor biosynthesis separately; do not materialize PIGA-to-PIGR as a ligand-receptor edge."
            elif ligand in {"PLAU", "PLG", "PRSS2", "PTDSS1", "PTGES", "PTGES2", "PTGES3", "PTGIS"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses a protease, zymogen, lipid-biosynthesis enzyme, or prostanoid synthase as the ligand label rather than the mature extracellular mediator acting at the listed receptor."
                limitations = "Represent enzyme activity, substrate processing, or mediator production in separate mechanistic layers when directly supported; do not materialize the enzyme-to-receptor row as a ligand-receptor edge."
            elif ligand == "PSEN1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "PSEN1 is a gamma-secretase component that processes receptors such as NOTCH; it is not an extracellular ligand for NOTCH."
                limitations = "Represent gamma-secretase cleavage and receptor-intracellular-domain release separately; do not materialize PSEN1-to-NOTCH as a ligand-receptor edge."
            elif ligand == "PSPN":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Persephin/PSPN does not have verified ligand-binding support for the listed GFRA or syndecan receptors in this pass; GFRA3 is specifically reported as an orphan co-receptor."
                limitations = "Require an exact PSPN receptor-complex binding and Ret-activation study before promotion; do not transfer GDNF-family receptor specificity across GFRA paralogs."
            elif ligand in {"POMC", "PTH", "PTH2", "PTHLH", "PPY", "PYY"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses a precursor or peptide-family label with a receptor that is not the established cognate receptor for this ligand form."
                limitations = "Require the mature peptide identity and direct receptor assay before promotion; do not transfer specificity across PTH/PTH2, pancreatic-polypeptide, NPY or related GPCR families."
            elif ligand == "PROC":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "as stated in primary model/assay"
                summary = "Protein C is a zymogen whose activation depends on thrombin-thrombomodulin and endothelial protein C receptor context; the listed candidate receptors are not asserted as direct mature-ligand receptors here."
                limitations = "Preserve the protein-C activation complex and PAR/EPCR topology when directly supported; do not materialize PROC-to-ITGAM, TEK or THBD as simple binary ligand-receptor edges."
            elif ligand in {"PRN", "PRND", "PTN", "PTN"}:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "No exact primary experiment was verified for this adhesion or prion-family candidate-to-receptor pair in the current pass."
                limitations = "Retain for targeted protein-interaction review; do not infer a classical ligand-receptor route from family membership or pathway context alone."
            elif ligand in {"RAET1A", "RAET1B", "RAET1C", "RAET1D", "RAET1E"} and receptor == "HCST+KLRK1":
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "mouse"
                summary = "Primary work supports the mouse RAE-1 ligand family as activating the NKG2D/KLRK1 receptor complex, but the cited family-level studies do not resolve each individual RAET1 paralog row as a separate exact edge here."
                limitations = "Preserve RAE-1 paralog, species, GPI-anchor and NKG2D/DAP10-DAP12 context; require paralog-specific primary evidence before materializing individual edges."
            elif ligand == "RARRES2" and receptor == "CCRL2":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                species = "human; mouse"
                summary = "Chemerin/RARRES2 biology includes CCRL2 as a ligand-presenting or scavenging context, but this candidate does not resolve a signaling receptor topology equivalent to CMKLR1."
                limitations = "Preserve CMKLR1/GPR1/CCRL2 functional distinctions; do not infer canonical signaling through CCRL2 without an exact primary receptor-activation assay."
            elif ligand in {"PRXL2B", "PTGDS", "PTGIS"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses an enzyme or non-ligand protein label rather than the mature prostanoid ligand for the listed receptor."
                limitations = "Represent prostanoid synthesis and downstream receptor signaling separately; do not materialize the biosynthetic protein as the ligand."
            elif ligand in {"PSAP"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "as stated in primary model/assay"
                summary = "Prosaposin has trophic, lysosomal and receptor-trafficking contexts, but the exact PSAP-to-CELSR1/LRP1 topology was not verified as a direct primary ligand-receptor edge in this pass."
                limitations = "Require exact mature prosaposin or prosaposin-domain ligand form and receptor assay before promotion; do not transfer LRP1 uptake or trophic-family context to a canonical signaling edge."
            elif ligand == "SELL" and receptor == "CD34":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E000290"
                primary = ["PMID:7692600", "PMID:7559783"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human; mouse"
                summary = "The graph contains the primary-supported CD34-to-SELL/L-selectin adhesion relationship in the reverse orientation of this public row."
                limitations = "Preserve CD34 glycoform/PNAd and high-endothelial-venule context; do not add a duplicate reverse edge or infer a canonical intracellular relay from adhesion alone."
            elif ligand == "SIRPA" and receptor == "CD47":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E000179"
                primary = ["PMID:18657508", "PMID:11283158"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse"
                summary = "The graph contains the primary-supported CD47-to-SIRPA/SIRPalpha inhibitory interaction in the reverse orientation of this public row."
                limitations = "Preserve CD47/SIRPA species, cis/trans and phagocytosis-brake context; do not add a duplicate reverse edge or infer a universal macrophage response."
            elif ligand.startswith("RSPO") and receptor in {"FZD8", "LRP6"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human; mouse"
                summary = "R-spondin proteins potentiate Wnt signaling through LGR/heparan-sulfate receptor contexts, but these rows do not establish FZD8 or LRP6 as the complete direct R-spondin receptor topology."
                limitations = "Require isoform-specific primary binding and receptor-complex evidence; do not collapse R-spondin/LGR/co-receptor potentiation into a binary R-spondin-to-FZD/LRP6 edge."
            elif ligand == "SLIT2" and receptor == "ROBO4":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human; mouse"
                summary = "The public row is consistent with Slit/Robo vascular-guidance family biology, but the current graph directly supports other Slit/Robo4 or Slit2/Robo pairings rather than this exact pair as an independently verified primary edge."
                limitations = "Require exact SLIT2-ROBO4 binding or receptor-triggering evidence before promotion; do not transfer SLIT3-ROBO4 or SLIT2-ROBO1/2 evidence across paralogs."
            elif ligand.startswith("SLIT"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Slit guidance ligands are established primarily through Robo-family receptor complexes; the listed non-Robo receptor or co-receptor row is not verified as a direct ligand-receptor edge in this pass."
                limitations = "Require exact Slit paralog, receptor, species and binding or functional assay; do not transfer Slit/Robo or heparan-sulfate context to unrelated receptors."
            elif ligand in {"SAA1", "SAA2"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                species = "human; mouse"
                summary = "Serum amyloid A has receptor-family and inflammatory-context evidence, but the current candidate rows do not resolve a direct mature SAA ligand assay for the listed receptor (including the established FPR2/AGER distinctions)."
                limitations = "Require exact SAA isoform, receptor and activation assay before promotion; do not transfer FPR2, TLR2/4 or RAGE family context to unrelated GPCRs or scavenger receptors."
            elif ligand.startswith("S100A"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human; mouse"
                summary = "S100A-family extracellular danger-signal biology overlaps RAGE, TLR and scavenger-receptor contexts, but the listed candidate receptor is not asserted as an exact primary-supported edge here."
                limitations = "Require S100 paralog-specific mature-protein binding or receptor-triggering evidence; do not transfer S100A8/A9 family context across CD36, CD68, AGER or integrin candidates."
            elif ligand in {"SEMA3A", "SEMA3E", "SEMA3G", "SEMA4F"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                species = "as stated in primary model/assay"
                summary = "The semaphorin candidate overlaps neuropilin/plexin or immune-receptor family biology, but the exact ligand-receptor pair and composite receptor topology were not verified in a primary assay during this pass."
                limitations = "Require exact semaphorin isoform, neuropilin/plexin or immune-receptor composition and assay; do not transfer family-level guidance evidence across paralogs."
            elif ligand.startswith("SERPINA") or ligand.startswith("SERPINC") or ligand.startswith("SERPINE") or ligand == "SERPING1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "as stated in primary model/assay"
                summary = "The serpin candidate may reflect protease inhibition, clearance, or co-receptor/ECM binding rather than a canonical mature ligand-receptor signal; the exact pair was not verified as a direct primary edge here."
                limitations = "Require exact serpin form, receptor topology and direct binding or receptor-triggering evidence; do not transfer LRP1, uPAR, selectin or protease-substrate context across serpin paralogs."
            elif ligand == "SOSTDC1" and receptor == "LRP5":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "mouse; human family comparator"
                summary = "SOSTDC1/USAG1 is a BMP/Wnt antagonist with LRP-family context, but the candidate does not establish the exact SOSTDC1-LRP5 topology as a direct primary-supported edge in this pass."
                limitations = "Preserve SOSTDC1 effects on BMP7 and Wnt receptor complexes; require exact LRP5 binding or functional blockade evidence before promotion."
            elif ligand in {"TAC1", "TAC2", "TAC4"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses a tachykinin precursor label rather than a defined mature tachykinin peptide ligand."
                limitations = "Retain mature substance P, neurokinin A/B or other processed peptide-to-TACR relationships only when the ligand form and receptor assay are explicit; do not materialize precursor labels directly."
            elif ligand == "TG" or ligand == "TGM2":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "TG is a thyroid-hormone precursor and TGM2 is an enzyme; neither is treated as the mature extracellular ligand for the listed receptor."
                limitations = "Represent hormone biosynthesis or transglutaminase activity separately; do not materialize these protein labels as direct ligand-receptor edges."
            elif ligand == "TGFA" and receptor in {"ERBB3", "ERBB4"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "TGF-alpha is a canonical EGFR ligand, but the listed ERBB3/ERBB4 receptors are not supported as direct TGFA receptors by the evidence reviewed here."
                limitations = "Require direct TGFA-to-ERBB3 or TGFA-to-ERBB4 binding/activation evidence before promotion; do not infer receptor specificity from the broader ERBB family."
            elif ligand in {"TGFB2", "TGFB3"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                species = "human; mouse"
                summary = "TGF-beta family receptor and co-receptor biology is strongly complex-dependent; the listed ENG or integrin rows are retained as contextual candidates rather than asserted as direct binary edges."
                limitations = "Require isoform-specific primary binding and complete receptor/co-receptor topology; do not transfer TGFBR2, betaglycan or latent-complex evidence to ENG or integrin subunits without exact assays."
            elif ligand in {"TFPI", "TCN2", "TCTN1", "TFF1", "ST6GAL1", "SLC6A8", "SNX14"}:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "No exact primary experiment was verified for this candidate ligand-receptor pair in the current pass."
                limitations = "Retain for targeted pair-specific review; do not infer direct signaling from enzyme, carrier, ciliary, transporter or intracellular-protein family context alone."
            elif ligand.startswith(("THBS",)) or ligand in {"TNC", "TNN", "TNR", "TNXB", "VCAN"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "as stated in primary model/assay"
                summary = "The extracellular-matrix or matricellular candidate overlaps integrin, syndecan and proteoglycan adhesion biology, but the exact mature ligand and receptor-complex topology were not verified as a direct primary edge in this pass."
                limitations = "Require exact matrix isoform, receptor complex, species and binding or functional assay; do not transfer thrombospondin/tenascin/vacan family evidence across integrin or syndecan subunits."
            elif ligand.startswith("TIMP"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "TIMP proteins are endogenous metalloprotease inhibitors and are not treated as mature ligands for the listed receptor rows."
                limitations = "Represent MMP inhibition, receptor shedding or matrix remodeling separately; do not materialize TIMP-to-receptor edges without an exact direct ligand assay."
            elif ligand.startswith("TNFSF"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The TNFSF candidate is paired with a receptor or adaptor outside the established cognate TNFR-family topology in this row."
                limitations = "Require the exact TNFSF ligand, TNFR-family receptor complex and primary binding/activation assay; do not infer activity at downstream adaptors or unrelated TNFR paralogs."
            elif ligand == "TNF" and receptor == "TNFRSF21":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                species = "human; mouse comparator"
                summary = "TNF is established through TNFRSF1A/TNFR1 and TNFRSF1B/TNFR2, while direct TNF-to-TNFRSF21/DR6 support was not verified in this pass."
                limitations = "Require a direct TNF-TNFRSF21 binding or receptor-triggering study before promotion; do not transfer TNFR1/TNFR2 evidence across TNFR-family paralogs."
            elif ligand in {"TPH1", "TRY10", "TRY4", "TRY5"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses a serotonin-biosynthesis enzyme or trypsin-family protease as the ligand label rather than the mature extracellular mediator."
                limitations = "Represent serotonin production or proteolytic receptor activation separately; do not materialize enzyme-to-receptor rows as direct ligand-receptor edges."
            elif ligand == "TSHB":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "TSHB is a subunit/precursor of thyrotropin, whose cognate receptor is TSHR; the listed non-TSHR receptors are not established direct receptors for this ligand form."
                limitations = "Require mature TSH and direct receptor assay; do not transfer activity to unrelated GPCRs or RAMP subunits."
            elif ligand == "TTR":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "No exact primary experiment was verified for this transthyretin-to-NGFR pair in the current pass."
                limitations = "Retain for targeted protein-transport and neurotrophic-context review; do not infer direct receptor signaling from family or expression overlap."
            elif ligand in {"UCN2", "UCN3"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Urocortin-2 and urocortin-3 are corticotropin-releasing factor-family ligands with CRHR2-family receptor context, not established ligands for IL10RB."
                limitations = "Require exact mature urocortin form and CRHR receptor assay; do not infer cytokine-receptor activity from family membership."
            elif ligand in {"VEGFB", "VEGFC"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The VEGF-family candidate is paired with a receptor outside the established VEGFR topology for this ligand row."
                limitations = "Require exact VEGF isoform, VEGFR/co-receptor complex and primary assay; do not transfer VEGF or unrelated GPCR receptor specificity across paralogs."
            elif ligand == "VGF":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "No exact primary experiment was verified for this VGF-to-NTRK1 candidate in the current pass."
                limitations = "Retain VGF-derived peptide and neurotrophic-family biology for targeted review; do not infer direct NTRK1 binding from expression or pathway context."
            elif ligand == "VTN" and receptor in {"ITGA5", "ITGB6"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human; mouse"
                summary = "Vitronectin is a primary-supported integrin ligand in alphaV-containing receptor complexes, but the public rows isolate receptor subunits and do not assert the complete mature integrin topology."
                limitations = "Retain exact alphaVbeta3/alphaVbeta5 vitronectin complexes; require direct alpha5 or beta6-containing receptor evidence before promotion and do not treat receptor subunits as standalone receptors."
            elif ligand == "WIF1" and receptor == "RYK":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "as stated in primary model/assay"
                summary = "WIF1 is a Wnt-pathway antagonist and RYK is a Wnt-family receptor, but the exact WIF1-RYK binding topology was not verified as a direct primary edge in this pass."
                limitations = "Require direct WIF1-RYK binding or receptor-triggering evidence; do not infer a binary edge from shared Wnt-pathway membership."
            elif ligand.startswith("WNT"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "as stated in primary model/assay"
                summary = "The Wnt candidate overlaps Frizzled, LRP, RYK or noncanonical receptor-family biology, but this exact ligand-receptor pair and complete co-receptor topology were not verified as a primary edge in this pass."
                limitations = "Require exact Wnt isoform, receptor/co-receptor composition, species and binding or activation assay; do not transfer WNT5A-FZD3/ROR2 or WNT11-ROR2 evidence across unrelated FZD/LRP/RYK paralogs."
            elif ligand == "ADM" and receptor == "CALCR+RAMP1":
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:32296767", "PMID:12970090"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human; rat"
                summary = "Primary adrenomedullin receptor work supports CALCRL-containing AM1/AM2 receptor complexes with RAMP2 or RAMP3, whereas this row specifies CALCR:RAMP1 and is not promoted as the complete receptor topology."
                limitations = "Preserve AM1/AM2 receptor-complex boundaries; do not infer that CALCR:RAMP1 is an adrenomedullin receptor from CGRP-receptor family membership."
            elif ligand == "ZP3":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "as stated in primary model/assay"
                summary = "ZP3 candidate rows reflect gamete-recognition and fertilization biology, not a generally established secreted ligand-to-signaling-receptor route for the listed receptors."
                limitations = "Retain species- and assay-specific zona-pellucida binding evidence; do not infer canonical signaling through CHRNA7, EGFR or MERTK without exact primary receptor assays."
            elif ligand == "LAMA2" and receptor == "ADGRG6":
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E000935;M23B-E000609"
                primary = ["PMID:25695270", "PMCID:PMC4335265"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse; zebrafish; human protein comparator"
                summary = "The graph already contains primary-supported laminin-211/LAMA2-containing ligand interaction with ADGRG6/GPR126 and its bounded cAMP/myelination context."
                limitations = "Preserve laminin-211 chain composition, ADGRG6 NTF/CTF and Schwann-cell context; do not duplicate the alias edge or infer a universal intracellular or TF route."
            elif ligand == "NODAL" and receptor == "ACVR1C+ACVR2B+CFC1":
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E000350;M21B-E000354"
                primary = ["PMID:11485994", "PMID:18089557", "PMID:11024047"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse; Xenopus"
                summary = "The graph already contains primary-supported Nodal signaling through ACVR1C/ALK7, ACVR2B/ActRIIB and the CFC1/Cripto co-receptor complex under normalized aliases."
                limitations = "Preserve CFC1/Cripto and type-I/type-II receptor stoichiometry and developmental assay context; do not duplicate the alias edge or infer a universal Nodal route or terminal-TF output."
            elif ligand.startswith("DBH+") or ligand.startswith("PNMT+") or ligand.startswith("NT5E+"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses biosynthetic enzyme and transporter machinery as a composite ligand label rather than the mature extracellular neurotransmitter or adenosine mediator."
                limitations = "Represent mediator production, vesicular transport and extracellular metabolism separately; do not materialize enzyme/transporter composites as direct receptor ligands."
            elif ligand in {"DHCR24", "DHCR7", "DPEP1", "DPEP2", "DPEP3", "GGT1+GGT5", "LIPA", "LTA4H", "PTGR1"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The candidate is an enzyme or metabolic-processing component rather than the mature ligand for the listed receptor."
                limitations = "Represent biosynthesis, degradation or lipid mediator production in a separate mechanistic layer; do not materialize the enzyme-to-receptor row as a direct ligand-receptor edge."
            elif ligand.startswith("FLRT") and receptor == ligand:
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human; mouse"
                summary = "Primary FLRT studies support homophilic cell-contact adhesion, but the graph export contract keeps self-loop adhesion relationships contextual rather than materializing them as signaling edges."
                limitations = "Preserve trans-homophilic and cis/adhesion orientation; do not encode a self-loop or infer a unique intracellular continuation or terminal-TF output from adhesion alone."
            elif ligand == "GAST" and receptor == "ADGRG1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Gastrin is a peptide ligand for the CCK receptor family, whereas ADGRG1/GPR56 has a distinct adhesion-GPCR ligand context; the public row is not supported as a direct pair."
                limitations = "Require a direct gastrin-ADGRG1 binding or activation assay before promotion; do not transfer CCK receptor specificity to ADGRG1."
            elif ligand in {"H2D", "H2K1", "H2T23"}:
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "ligand_receptor_binding_or_activation"
                species = "mouse"
                summary = "The public row reflects mouse MHC-I/NK-receptor recognition family biology, but the cited family-level evidence does not resolve each exact H2 paralog and KLRA/KLRC:KLRD1 composite topology as one graph edge."
                limitations = "Require exact H2 paralog, receptor complex, species and binding/activation assay before promotion; do not infer paralog specificity from MHC-family membership."
            elif ligand.startswith("ICAM5"):
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "No exact primary experiment was verified for this ICAM5-to-CD209F candidate in the current pass."
                limitations = "Retain for targeted neural-adhesion and receptor-paralog review; do not infer direct CD209F binding from ICAM family membership."
            elif ligand.startswith("ITGAV+") or ligand == "LPAR1" or ligand == "LPAR2" or ligand == "LPAR3" or ligand == "SDC1":
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "as stated in primary model/assay"
                summary = "The candidate reflects adhesion-GPCR, integrin or syndecan receptor-complex context, but the exact direct ligand-receptor topology is not resolved for this row."
                limitations = "Require exact receptor-complex composition and pair-specific primary binding or activation evidence; do not treat receptor subunits or co-receptors as standalone ligand targets."
            elif ligand.startswith("KLK"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human"
                summary = "Primary candidate literature supports a protease-activated-receptor mechanism for this kallikrein/PAR row, but proteolytic receptor cleavage is retained as receptor-proximal activation rather than a conventional soluble-ligand binding edge."
                limitations = "Preserve active protease form, PAR cleavage site, cell context and biased signaling; do not infer a canonical ligand-binding affinity or universal PAR1/PAR2 route from family-level evidence."
            elif ligand == "LAIR1":
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human; mouse comparator"
                summary = "LAIR1 and LILRB/PIRA2 are inhibitory immune receptors; this candidate is retained as receptor-family/context evidence, not asserted as a conventional ligand-receptor edge."
                limitations = "Require direct extracellular binding and receptor-triggering evidence for the exact receptor pair; preserve inhibitory ITIM/adaptor boundaries and do not transfer receptor-receptor associations into an extracellular ligand layer."
            elif ligand == "LGALS9":
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse"
                summary = "Galectin-9 has primary-supported receptor and glycan-dependent immune contexts in the graph, but these candidate rows do not resolve a single exact receptor topology beyond the established CD44, TIM-3 and TLR4 branches."
                limitations = "Retain glycoform, receptor and cell-context distinctions; do not transfer LGALS9 evidence to BCR/CD22/PTPRC, IGHM or P4HB without exact pair-specific assays."
            elif ligand in {"LTA4H"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "LTA4H produces leukotriene B4 but is not itself the mature ligand for LTB4R1 or LTB4R2."
                limitations = "Represent leukotriene biosynthesis separately and materialize LTB4 receptor edges only with explicit mature LTB4 ligand evidence."
            elif ligand.startswith("NRXN") and receptor.startswith("CLSTN"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human; mouse"
                summary = "The candidate is a neuronal adhesion or synaptic protein-interaction row, not a soluble ligand route; exact trans/cis orientation and receptor-complex role require pair-specific validation."
                limitations = "Preserve synaptic adhesion and intracellular adaptor context; do not infer a canonical extracellular ligand-receptor signaling route or terminal-TF output."
            elif ligand == "NTN4" and receptor == "NTRK2":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Netrin-4 is supported through DCC, UNC5A, neogenin and integrin contexts, but direct NTRK2/TrkB receptor support was not verified in this pass."
                limitations = "Require a direct NTN4-NTRK2 binding or activation study before promotion; do not transfer BDNF/NTF5-TrkB evidence to netrin-family ligands."
            elif ligand == "PECAM1" and receptor == "CD177":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "No exact primary experiment was verified for this PECAM1-to-CD177 candidate in the current pass."
                limitations = "Retain for targeted leukocyte-endothelial adhesion review; do not infer direct CD177 binding from shared vascular or neutrophil expression."
            elif ligand == "RARRES2" and receptor == "CMKLR2":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Chemerin/RARRES2 is established through CMKLR1/CHEMR23 and related receptor contexts, not the receptor label CMKLR2 in this row."
                limitations = "Require direct RARRES2-CMKLR2 evidence before promotion; do not transfer CMKLR1 receptor specificity across paralogs."
            elif ligand in {"SDC2", "SFTPD"}:
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "as stated in primary model/assay"
                summary = "The candidate reflects syndecan/collectin and adhesion-GPCR family context, but the exact direct ligand-receptor topology was not verified in this pass."
                limitations = "Require exact mature ligand, receptor complex, species and direct binding or activation assay; do not treat a co-receptor or matrix-associated protein as a standalone canonical ligand edge."
            elif ligand.startswith("SHMT+") or ligand.startswith("SLC18A") or ligand.startswith("SLC6A4+"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses amino-acid/monoamine synthesis, vesicular transport or reuptake machinery as a composite ligand label rather than the mature neurotransmitter glycine or serotonin."
                limitations = "Represent neurotransmitter production, packaging and reuptake separately; do not materialize enzyme/transporter composites as direct glycine- or serotonin-receptor edges."
            elif ligand == "TAX1BP3":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "TAX1BP3 is an intracellular adaptor/scaffold label, not a mature extracellular ligand for the listed adhesion-GPCR receptors."
                limitations = "Represent intracellular receptor-associated scaffolding separately; do not materialize TAX1BP3-to-ADGRB1/ADGRB2 as a ligand-receptor edge."
            elif ligand == "TBXAS1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "TBXAS1 synthesizes thromboxane A2 but is not itself the mature ligand for TBXA2R."
                limitations = "Represent thromboxane biosynthesis separately and materialize TBXA2R edges only with explicit mature TXA2 ligand evidence."
            elif ligand == "TULP2" and receptor == "TYRO3":
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "as stated in primary model/assay"
                summary = "The candidate suggests a tubby-like/TAM-receptor family interaction, but the exact TULP2-TYRO3 ligand-receptor topology and mature extracellular form were not independently verified in this pass."
                limitations = "Require direct TULP2-TYRO3 binding or receptor-activation evidence; do not transfer Gas6/Pros1 TAM-ligand specificity to tubby-family candidates by family analogy."
            elif ligand == "UBASH3B":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "UBASH3B is an intracellular signaling/ubiquitin-associated protein, not the mature extracellular ligand for PPARA."
                limitations = "Represent intracellular regulation separately; do not materialize UBASH3B-to-PPARA as a ligand-receptor edge."
            elif ligand == "ULBP1" and receptor == "HCST+KLRK1":
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E002958"
                primary = ["PMID:11239445", "PMID:11777960", "DOI:10.4049/jimmunol.168.2.671"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "The graph already contains the primary-supported ULBP1/RAET1I-to-NKG2D/KLRK1 interaction under the ULBP1 ligand and HCST/KLRK1 receptor-complex aliases."
                limitations = "Preserve GPI-linked ULBP1 and NKG2D/DAP10 receptor context; do not duplicate the alias edge or infer a universal NK-cell transcriptional output."
            elif ligand == "VEGFD" and receptor == "FLT4+KDR":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000360;M21B-E000361"
                primary = ["PMID:11279005", "PMID:15215251"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse"
                summary = "The graph contains primary-supported VEGF-D interactions with FLT4/VEGFR3 and KDR/VEGFR2 as separate edges, while this public row encodes a composite receptor topology."
                limitations = "Retain the separate receptor-specific VEGFD edges and receptor-complex boundaries; do not materialize the composite as one binary edge without an exact heteromeric receptor assay."
            elif ligand == "A2M":
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "receptor_proximal_or_pathway"
                species = "as stated in primary model/assay"
                summary = "Alpha-2-macroglobulin is a protease-binding and clearance factor; the candidate rows do not establish it as a direct mature ligand for KLK1-family receptor targets."
                limitations = "Require exact A2M-protein complex or receptor assay before promotion; do not infer direct signaling from protease inhibition or endocytic clearance context."
            elif ligand in {"PTH", "PTH2", "PTHLH"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The parathyroid-hormone family candidate is paired with receptors outside the established cognate PTH/PTH2 receptor context."
                limitations = "Require a mature ligand-form and direct receptor assay; do not infer activity at unrelated GPCRs or RAMP subunits from family membership."
            elif ligand == "OMG":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "No exact primary experiment was verified for this oligodendrocyte-myelin glycoprotein-to-receptor pair in the current pass."
                limitations = "Retain established myelin-inhibitory receptor-complex evidence separately; do not transfer Nogo-receptor-family context to LINGO1, NGFR or TNFRSF1B as isolated receptors."
            elif "+" in receptor:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                species = "as stated in primary model/assay"
                summary = "The public row encodes a multi-subunit receptor complex or pathway prediction; component overlap does not establish the complete composite topology as one primary graph edge."
                limitations = "Retain the composite as contextual traversal evidence and require exact mature ligand, receptor-subunit composition, species and assay support before promotion."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_unverified"
                summary = "No exact primary experiment was verified for this database-only candidate in the current pass."
                limitations = "Retain for targeted discovery; do not materialize a graph edge from public-database membership alone."
        elif ligand == "POMC" and receptor in {"MC3R", "MC4R"}:
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:11024027"]
            species = "as stated in primary model/assay"
            summary = "POMC is a precursor that gives rise to melanocortin peptides; the cited study does not establish the intact POMC precursor as the direct ligand for this receptor row."
            limitations = "Retain mature peptide-to-melanocortin-receptor relationships only when the ligand form and receptor assay are explicit; do not materialize the precursor label as a direct edge."
        elif ligand in {"MDK"} and receptor == "SDC2":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:28356350"]
            species = "as stated in primary model/assay"
            summary = "The cited literature supports a syndecan-associated role in recombinant midkine responses, but does not resolve a unique direct MDK-SDC2 binding edge and downstream relay in the exact public topology."
            limitations = "Retain as contextual/co-receptor evidence; no unique SDC2 intracellular continuation, TF, or target-gene output is asserted."
        elif ligand in {"FLRT1", "FLRT3"} and receptor == "ADGRL2":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "candidate_only_review_locator"
            primary = ["PMID:25728924", "PMID:27091502", "PMID:34022279", "PMID:35907405"]
            species = "as stated in primary model/assay"
            summary = "The cited primary literature addresses FLRT-latrophilin family interactions, but an exact direct FLRT1/FLRT3-to-ADGRL2 edge is not resolved in the current source register."
            limitations = "Keep as a family-level search candidate and contextual boundary; require an exact ligand, ADGRL2 receptor, species, and assay before graph promotion."
        elif ligand in {"CD209A", "CEACAM1", "CEACAM2"} or receptor.startswith("CD209"):
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = ["PMID:16246332", "PMID:16282604"]
            species = "human"
            summary = "The primary studies support human CEACAM1-Lewis-X interaction with DC-SIGN/CD209 in the reported adhesion context, but the public rows mix direction, species, and mouse CD209/CEACAM paralogs."
            limitations = "Retain family-level adhesion evidence without asserting the exact mouse paralog pair or reversing ligand-receptor direction; exact species/paralog mapping requires primary verification."
        elif ligand in {"JAG1", "JAG2"} and receptor == "NOTCH4":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_review_locator"
            primary = ["PMID:22353464"]
            summary = "The public citation was recorded, but the reviewed primary evidence did not verify an exact Jagged1/2-Notch4 relationship for this row."
            limitations = "Keep as a searchable Notch-family candidate; do not infer Notch4 binding or activation from Notch1/Notch3 evidence."
        elif ligand in {"GHRH", "PDGFA", "PMCH", "SELE", "SEMA5A", "SEMA5B", "VIP"}:
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            summary = "The public citation was reviewed but did not verify an exact primary experiment for this ligand-receptor pair in the current pass."
            limitations = "Retain as a searchable candidate; do not materialize a graph edge from the current citation or family-level context alone."
        elif row.get("review_lane") == "primary_evidence_review":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_review_locator"
            summary = "The row was selected for primary-evidence review, but no exact primary experiment for this ligand-receptor pair was verified in the current pass."
            limitations = "Retain for targeted primary review; do not materialize a graph edge from pathway membership, family context, or an unverified locator alone."
        elif row.get("review_lane") == "discovery_review":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            summary = "No exact primary locator was present in the frozen public snapshot, and no exact primary experiment was verified in this review pass."
            limitations = "Retain for future targeted discovery; do not materialize a graph edge from public-database membership alone."
        elif ligand == "DSC3" and receptor == "DSG3":
            disposition = "already_present_reverse_orientation"
            matched_ids = "M21B-E003160"
            primary = ["PMID:27298358", "PMCID:PMC4932976", "DOI:10.1073/pnas.1606272113"]
            layer = "ligand_receptor_binding_or_activation"
            species = "human; mouse"
            summary = "The graph already contains the primary-supported desmosomal interaction in the reverse adhesion orientation, DSG3 to DSC3."
            limitations = "The reverse orientation is preserved as a cell-adhesion relationship; no duplicate DSC3-to-DSG3 edge is added."
        elif ligand == "EFNA5" and receptor == "EPHA7":
            disposition = "new_primary_supported_edge_candidate"
            matched_ids = ""
            primary = ["PMID:10366629", "PMCID:PMC6782661"]
            layer = "ligand_receptor_binding_or_activation"
            species = "rat"
            summary = "The primary striatal binding study reports selective ephrin-A5 binding and precipitation of EphA7, but not EphA4, in postnatal rat striatal tissue lysates."
            limitations = "Candidate is limited to selective tissue binding; lysate precipitation does not establish purified binary binding, forward signaling, SCI transfer, or terminal-TF activity."
        elif ligand in {"CCL24", "CCL5"} and receptor == "ACKR2":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            summary = "The frozen public citation was recorded, but an exact primary study supporting this ligand-ACKR2 pair was not verified in this review pass."
            limitations = "Retain as a searchable candidate; do not materialize a graph edge from the unverified citation alone."
        elif ligand == "DLK1" or (ligand, receptor) in {("DLL1", "NOTCH4"), ("DLL3", "NOTCH3"), ("DLL3", "NOTCH4")}:
            disposition = "needs_manual_adjudication"
            layer = "candidate_only_review_locator"
            summary = "The cited PMID is a review-level Notch discussion, not an exact primary ligand-receptor experiment for this row."
            limitations = "A primary study with exact ligand, Notch receptor, species, and assay must be identified before graph promotion."
        elif ligand.startswith("EFNA") or ligand.startswith("EFNB"):
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            summary = "The public citation was not verified as an exact primary experiment for this ligand-receptor pair in the current pass; the tissue-binding primary used for family context supports different Eph pairing(s)."
            limitations = "Do not globally reject the family interaction; retain the pair for a context-specific search, but do not materialize it from the current citation."
        else:
            raise SystemExit(f"unhandled batch row: {candidate}")

        output.append(
            {
                "candidate_unit_id": candidate,
                "review_batch": row.get("review_batch", "batch_001"),
                "normalized_ligand_key": ligand,
                "normalized_receptor_key": receptor,
                "disposition": disposition,
                "matched_graph_edge_ids": matched_ids,
                "supporting_primary_locators": "; ".join(primary),
                "reviewed_source_locators": "; ".join(reviewed),
                "evidence_layer": layer,
                "species_support": species,
                "evidence_summary": summary,
                "limitations": limitations,
                "review_status": "reviewed_batch_001",
            }
        )

    if len(output) != len(batch) or {r["candidate_unit_id"] for r in output} != {r["candidate_unit_id"] for r in batch}:
        raise SystemExit("resolution does not cover batch exactly")
    write_tsv(args.output, output, fields)
    from collections import Counter

    print(f"resolved_rows={len(output)} dispositions={dict(sorted(Counter(r['disposition'] for r in output).items()))}")


if __name__ == "__main__":
    main()
