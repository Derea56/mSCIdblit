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
DEFAULT_BUNDLE = ROOT / "data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion256"
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
        elif row.get("review_batch") == "batch_074":
            pair = (ligand, receptor)
            if pair == ("CBLN1+NRXN1", "GRID2"):
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E002141;M21B-E002142"
                primary = ["PMID:20537373", "PMID:22117778", "PMID:27418511", "PMID:29782851"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse; rat"
                summary = "Primary binding, structural and cerebellar synapse studies resolve the CBLN1-β-NRXN1-GRID2 trans-synaptic bridge, while the graph already represents its CBLN1-NRXN1 and CBLN1-GRID2 component edges."
                limitations = "Retain the validated component edges and the multicomponent bridge context; do not materialize the composite as a duplicate binary ligand-receptor edge or infer a universal intracellular/TF chain from synapse-level outputs."
            elif pair == ("EFNB1", "EPHB4"):
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:16840724"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human endothelial-cell assays"
                summary = "Primary endothelial experiments show ephrin-B1-Fc-dependent EphB4 phosphorylation and place EphB4 forward signaling in SDF-1-induced endothelial chemotaxis and branching responses, supporting a bounded EFNB1-EPHB4 receptor-proximal route."
                limitations = "Preserve ephrin-B1-Fc, EphB4 phosphorylation and endothelial chemotaxis/branching context; do not infer a complete intracellular cascade, terminal TF or SCI transfer."
            elif pair == ("EFNB3", "EPHB4"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:17090524"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human ovarian-tumor tissue"
                summary = "The cited primary study reports EFNB3 and EPHB4 coexpression and protein staining in ovarian tumors, but does not directly test EFNB3 binding to or activation of EPHB4."
                limitations = "Retain tumor coexpression as contextual evidence only; require pair-specific binding or receptor-activation data before promotion and do not infer an intracellular or TF route from coexpression."
            elif pair == ("EFNA1", "EPHA7"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:10366629", "PMCID:PMC6782661"]
                layer = "ligand_receptor_binding_or_activation"
                species = "rat striatal tissue"
                summary = "Primary native-receptor binding assays report ephrin-A1 binding to EphA4 but not detectable binding to EphA7 in striatal lysates, so the public EFNA1-EPHA7 row is retained as a specificity boundary rather than promoted."
                limitations = "Preserve tissue- and receptor-specific negative binding evidence; do not transfer broad EphA-family promiscuity to EphA7 or infer a downstream route for this pair."
            elif pair == ("EFNA2", "EPHA1"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:10366629", "PMCID:PMC6782661"]
                layer = "ligand_receptor_binding_or_activation"
                species = "rat striatal tissue"
                summary = "The reviewed primary native-receptor study resolves ephrin-A2 binding preferentially to EphA7 rather than EphA4 in striatal tissue, but does not verify the exact EFNA2-EPHA1 row."
                limitations = "Retain ephrin-A2/EphA receptor-family context with tissue-specific selectivity; require an exact EphA1 assay before promotion and do not infer a complete signaling route from family membership."
            elif pair == ("EFNB3", "EPHB1"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:22103419"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "mouse optic-chiasm development"
                summary = "Primary developmental work supports EphB1 interactions with ephrin-B ligands and identifies ephrin-B2, with lesser ephrin-B1 contribution, in optic-chiasm guidance; it does not establish EFNB3 as the ligand for the listed EphB1 route."
                limitations = "Preserve ephrin-B2/ephrin-B1 versus ephrin-B3 specificity and developmental context; do not transfer EphB-family evidence to EFNB3 without pair-specific binding or activation data."
            elif pair[0].startswith("GJA") or pair[0].startswith("GJC"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human and mouse connexin-family context"
                summary = "Connexin family members form hemichannels and intercellular gap-junction channels; the public pair list does not resolve each listed connexin combination as a conventional ligand-receptor edge or as an independently tested signaling route."
                limitations = "Retain connexin pairings as channel/adhesion context with explicit connexin and cell-junction topology; do not treat them as soluble ligand-receptor inputs or infer a receptor-to-TF cascade from family-level gap-junction evidence."
            elif pair == ("LRRC4C", "PTPRF"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:23916315"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "neural synaptic-adhesion context"
                summary = "The cited LAR-RPTP literature supports synaptic adhesion and receptor-family organization, but the reviewed locator is a review and does not verify an exact LRRC4C-PTPRF primary binding or receptor-activation experiment."
                limitations = "Retain LRRC4C/LAR-RPTP synaptic-organizer context; require exact pair-specific primary evidence before promotion and do not infer an intracellular or TF route from family-level adhesion biology."
            elif pair == ("NECTIN1", "CADM3"):
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The cited Nectin locator does not verify an exact Nectin-1-to-CADM3 interaction; primary Nectin/Necl studies address other family pairings and do not support this specific row."
                limitations = "Retain exact CADM3/Necl and Nectin-family pairs separately; require direct NECTIN1-CADM3 binding or receptor-dependent evidence before promotion."
            elif pair == ("NECTIN3", "TIGIT"):
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator does not establish NECTIN3 as a direct TIGIT ligand; primary TIGIT ligand work centers on PVR/CD155 and NECTIN2/CD112 rather than Nectin-3."
                limitations = "Require direct Nectin-3/TIGIT binding or receptor-triggering evidence before promotion; do not transfer PVR-family membership into a canonical TIGIT edge."
            elif pair == ("PMCH", "MERTK"):
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The cited locator was not verified as an exact PMCH-to-MERTK primary experiment; primary MERTK ligand studies instead establish Gas6 and PROS1 as canonical ligands."
                limitations = "Retain PMCH-MERTK for targeted discovery only; do not transfer TAM-receptor family biology or Gas6/PROS1 evidence to PMCH."
            elif pair == ("SELE", "CEACAM1"):
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The public citation is propagated through database tables, but an exact primary SELE-to-CEACAM1 binding or receptor-dependent functional experiment was not verified in this pass."
                limitations = "Retain E-selectin adhesion evidence for established ligands such as SELPLG and GLG1; require pair-specific SELE-CEACAM1 primary evidence before promotion."
            elif pair in {
                ("APOA2", "TREM2+TYROBP"), ("APP", "TREM2+TYROBP"),
                ("CEACAM1", "CD1D1"), ("CEACAM1", "CD1D2"), ("CEACAM1", "CD8A"),
                ("CEACAM2", "CD1D1"), ("CEACAM2", "CD1D2"), ("CEACAM2", "CD8A"),
                ("CEACAM1", "PSG20"), ("CEACAM2", "PSG20"),
            }:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                if pair[0] in {"APOA2", "APP"}:
                    primary = []
                    summary = "The cited locator does not verify the exact APOA2- or APP-to-TREM2/TYROBP composite interaction; related TREM2 studies concern other apolipoproteins, amyloid-lipoprotein complexes or receptor-complex biology."
                    limitations = "Do not transfer ApoA-I, ApoE, CLU or amyloid-lipoprotein evidence to APOA2 or intact APP; retain the composite row for exact ligand-form and receptor-complex primary review."
                elif pair[1] in {"CD1D1", "CD1D2", "CD8A"}:
                    primary = ["PMID:24104458"]
                    summary = "The cited primary study supports CEACAM5 binding to CD1d and CD8alpha, not the CEACAM1 or CEACAM2 paralog rows."
                    limitations = "Do not transfer CEACAM5 domain or glycan evidence to CEACAM1/CEACAM2; require exact-paralog binding and functional assays before promotion."
                else:
                    primary = ["PMID:24743304"]
                    summary = "The cited primary study concerns soluble CEACAM8 interaction with CEACAM1, not CEACAM1/CEACAM2 interaction with PSG20."
                    limitations = "Do not infer PSG20 binding from CEACAM8-CEACAM1 evidence or CEACAM-family database membership."
            elif pair == ("CEACAM2", "CEACAM2"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:21982860"]
                layer = "ligand_receptor_binding_or_activation"
                species = "mouse CEACAM-family context"
                summary = "The cited locator does not establish the exact CEACAM2 homophilic edge, and the graph export contract disallows self-loop materialization for CEACAM2."
                limitations = "Retain only exact primary-supported CEACAM adhesion pairs; do not encode CEACAM2-to-CEACAM2 as a self-loop or infer downstream signaling from homophilic family context."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_075":
            pair = (ligand, receptor)
            if pair == ("TSHB", "TSHR"):
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:4372620"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "bovine TSH subunit; dog and mouse thyroid assays"
                summary = "Primary subunit-comparison experiments show that the TSH beta subunit binds the thyrotropin receptor and produces a weak but measurable thyroid-stimulation response, while intact TSH is much more active; the beta subunit supplies key receptor-specific determinants."
                limitations = "Represent TSHB as a subunit-level, partial-activity evidence edge rather than the complete physiological TSH heterodimer; preserve the reported species and assay context and do not infer a full intracellular or TF route from the beta-subunit experiment."
            elif pair == ("PPY", "NPY5R"):
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:17204471", "PMID:18457425"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human Y5 receptor in heterologous binding/mutagenesis assays"
                summary = "Primary Y-receptor mutagenesis and binding studies identify pancreatic polypeptide as a ligand for Y5/NPY5R and resolve ligand-contact residues that contribute to binding and signal transduction."
                limitations = "Preserve the human receptor and peptide-family assay context, including the higher pancreatic-polypeptide preference of Y4 relative to Y5; do not infer a unique tissue output or complete intracellular cascade from receptor binding/mutagenesis alone."
            elif pair == ("CCL21A", "CCR7"):
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:20201039", "PMID:20889506", "PMID:41420491"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse Ccl21a; human CCL21/CCR7 comparator assays"
                summary = "Primary mouse genetics and migration studies identify Ccl21a/CCL21 as a functional CCR7 ligand, while receptor-dependent migration studies connect CCL21-CCR7 engagement to PLCγ1 and ERK1/2-associated outputs; Ccl21a is distinguished from the Ccl21b paralog."
                limitations = "Preserve mouse Ccl21a versus Ccl21b gene-form specificity and the human comparator context; do not transfer CCL21 tail/isoform behavior across species or infer a universal terminal-TF route from the reported migration assays."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_076":
            if (ligand, receptor) == ("APOE", "LRP2"):
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:9122201"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "rat megalin; apoE-betaVLDL ligand form"
                summary = "Primary megalin mapping experiments show that apoE-betaVLDL binds the LRP2/megalin receptor and localize the interaction to a ligand-binding repeat cluster, supporting a bounded APOE-containing-particle-to-LRP2 edge."
                limitations = "Preserve the apoE-betaVLDL particle form, rat megalin assay and receptor-binding/internalization context; do not generalize to every APOE isoform or free APOE molecule, and do not infer a complete intracellular or TF route."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_077":
            pair = (ligand, receptor)
            if pair == ("WNT11", "FZD6"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:24873871"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human FZD6 membrane-mobility assay with WNT11 and WNT5B"
                summary = "A primary FZD6 membrane-mobility study found that WNT11 did not alter FZD6 mobility under the tested conditions and concluded that WNT11 did not act through FZD6 in that assay; pathway or co-expression membership is not direct positive pair evidence."
                limitations = "Preserve the assay-specific negative result without claiming that WNT11 can never signal through FZD6 in every cellular context; do not materialize the public WNT11-FZD6 row or infer downstream signaling from family-level Wnt annotations."
            elif pair == ("NECTIN3", "TIGIT"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:23677581", "PMID:22421438", "PMID:28515320"]
                layer = "ligand_receptor_binding_or_activation"
                species = "mouse and human TIGIT/nectin-family binding assays"
                summary = "Primary human studies establish TIGIT binding to PVR/CD155 and Nectin2/CD112, while a primary mouse TIGIT study did not detect mNectin3 and noted that an earlier human Nectin3 assignment was not supported; the public NECTIN3-TIGIT row therefore remains species- and assay-conflicted context rather than a direct edge."
                limitations = "Do not materialize NECTIN3-TIGIT without a reconciled pair-specific primary binding or receptor-triggering study; do not transfer PVR or Nectin2 evidence to Nectin3 or generalize family-level contact annotations."
            elif pair == ("APOA2", "TREM2+TYROBP"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:26374899", "PMCID:PMC4646256"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human and macaque apolipoprotein/TREM2 biochemical assays"
                summary = "Primary TREM2 work establishes the TREM2-TYROBP signaling-complex context and detects ApoA-II in TREM2 immunoprecipitates with weak binding of purified ApoA-II alongside stronger apolipoprotein evidence, but the particle assays cannot fully resolve apolipoprotein-specific binding and do not establish the public APOA2-to-TREM2+TYROBP composite as one direct edge."
                limitations = "Retain weak ApoA-II/component evidence for downstream route evaluation; do not materialize the composite receptor edge, transfer robust ApoE or ApoA-I evidence to APOA2, or infer a complete intracellular or TF route."
            elif pair == ("APP", "TREM2+TYROBP"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:29518356", "PMID:27477018"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human and mouse TREM2 microglia and amyloid-beta assays"
                summary = "Primary studies support mature amyloid-beta oligomers or amyloid-beta-lipoprotein complexes binding TREM2 and engaging the DAP12/TYROBP signaling context, not intact APP precursor as the ligand in the public row."
                limitations = "Represent APP processing and the mature Aβ ligand form explicitly; do not materialize an intact APP-to-TREM2+TYROBP edge or infer that precursor expression alone establishes TREM2 signaling."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_078":
            pair = (ligand, receptor)
            if pair == ("UCN2", "CRHR1"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:11226328"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "mouse UCN2 cloning and CRF-receptor pharmacology"
                summary = "Primary UCN2 characterization identifies selective binding and activity at type-2 CRF receptors, with no appreciable type-1 receptor activity, so the public UCN2-CRHR1 pairing is not supported as a direct edge."
                limitations = "Model UCN2 as a CRHR2/CRHR2A-selective ligand in downstream route evaluation; do not materialize UCN2-CRHR1 or infer CRHR1 signaling from CRF-family membership."
            elif pair == ("UCN3", "CRHR1"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:11416224"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human and mouse UCN3 characterization with CRF-receptor assays"
                summary = "Primary UCN3 identification and receptor characterization identify UCN3 as selective for type-2 CRF receptors, so the public UCN3-CRHR1 pairing is not supported as a direct edge."
                limitations = "Model UCN3 as a CRHR2/CRHR2A-selective ligand in downstream route evaluation; do not materialize UCN3-CRHR1 or infer CRHR1 signaling from CRF-family membership."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_079":
            if (ligand, receptor) == ("LAMC3", "DAG1"):
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:29874128"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "mouse retinal endothelial and vascular basement-membrane assays"
                summary = "Primary retinal arteriogenesis experiments show that laminin gamma-3-containing basement membrane binds dystroglycan and that endothelial Lamc3 or Dag1 loss produces concordant vascular and Notch-target expression phenotypes, supporting a bounded LAMC3-DAG1 ECM-receptor edge with functional output."
                limitations = "Preserve laminin gamma-3-containing matrix, dystroglycan glycosylation and mouse retinal endothelial context; do not expand LAMC3 into an unreported laminin heterotrimer composition or infer a complete intracellular or TF chain from the vascular/Notch output."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_080":
            if ligand in {"H2DMA", "H2DMB1", "H2DMB2", "H2OB"} and receptor == "CD4":
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:12119342", "PMID:32069316", "PMID:34696161"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human HLA-DM biochemical assays; mouse H2-O and H2-M antigen-presentation models"
                summary = "Primary antigen-presentation studies define H2-DM/H2-O components as intracellular MHC class II peptide-loading and editing factors that shape peptide-MHC-II display and CD4 T-cell activation; they do not establish the listed H2 component as an extracellular ligand directly binding CD4."
                limitations = "Represent H2-DM/H2-O as antigen-processing and MHC-II-loading context, with CD4 activation occurring through peptide-MHC-II complexes; do not materialize H2 component-to-CD4 ligand-receptor edges or infer direct CD4 signaling from chaperone function."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_081":
            pair = (ligand, receptor)
            if pair in {("AANAT", "MTNR1A"), ("AANAT", "MTNR1B")}:
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:11313340", "PMID:10696085"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human AANAT melatonin-synthesis system; recombinant human MT1/MT2 receptor assays"
                summary = "Primary studies define AANAT as the intracellular penultimate enzyme in melatonin synthesis, while recombinant MT1 and MT2 assays identify melatonin—not AANAT—as the receptor ligand and measure Gi/o-coupled cAMP responses."
                limitations = "Represent AANAT as a biosynthetic precursor/enzyme that contributes to melatonin availability; do not materialize AANAT-to-MTNR1A or AANAT-to-MTNR1B ligand-receptor edges or infer receptor signaling from enzyme expression alone."
            elif pair == ("ACE", "AGTR2"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:11291769", "PMID:15840019"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "rat and human vascular-cell ACE conversion assays; cloned human/mouse/rat AT2 receptor assays"
                summary = "Primary studies define ACE as the converting enzyme that generates angiotensin II from angiotensin substrates, while AT2 receptor assays identify angiotensin peptides as receptor ligands; ACE itself is not the extracellular ligand for AGTR2."
                limitations = "Represent ACE-dependent peptide production separately from angiotensin-II-to-AGTR2 signaling; do not materialize ACE-to-AGTR2 or infer direct receptor engagement from ACE expression."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_082":
            pair = (ligand, receptor)
            if pair == ("ADAM10", "NOTCH2"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:20156974"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse B-cell ADAM10 conditional-knockout and Notch2 signaling assays"
                summary = "Primary conditional-knockout and rescue studies show that ADAM10 is required for Notch2 receptor-proximal signaling and marginal-zone B-cell development, supporting a proteolytic continuation role rather than an extracellular ligand interaction."
                limitations = "Retain ADAM10-Notch2 as receptor-proximal proteolytic context for Notch signaling; do not materialize ADAM10-to-NOTCH2 as a canonical ligand-receptor edge or infer a universal downstream route outside the tested B-cell context."
            elif pair == ("ADAM17", "NOTCH1"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:19704010", "PMID:33673337"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse embryonic fibroblast and cell-based Notch1 processing assays"
                summary = "Primary processing studies show that ADAM17 can contribute to Notch1 cleavage in ligand-independent or EDTA-triggered settings, whereas ADAM10 is required for Delta-like ligand-induced Notch1 processing; the evidence supports context-dependent receptor-proximal proteolysis, not a soluble ligand edge."
                limitations = "Retain ADAM17-Notch1 as context-dependent proteolytic continuation evidence and preserve ligand-dependent versus ligand-independent conditions; do not materialize ADAM17-to-NOTCH1 as a canonical ligand-receptor edge or infer a universal Notch transcriptional output."
            elif pair == ("ADAM17", "ERBB4"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:10744726"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse fibroblast TACE/ADAM17 loss-and-rescue HER4/ErbB4 shedding assays"
                summary = "Primary loss-and-rescue experiments show that TACE/ADAM17 is required for regulated HER4/ErbB4 ectodomain shedding, supporting a receptor-proximal proteolytic continuation step rather than ADAM17 acting as an extracellular ligand."
                limitations = "Retain ADAM17-ErbB4 as receptor-proximal shedding context for ErbB4 signaling; do not materialize ADAM17-to-ERBB4 as a canonical ligand-receptor edge or infer a complete intracellular or TF route from shedding alone."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_083":
            pair = (ligand, receptor)
            if pair == ("AGRP", "SDC3"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:11461706", "PMID:12851299", "PMID:20923696"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse hypothalamic SDC3 transgenic/knockout and AgRP-melanocortin feeding models"
                summary = "Primary transgenic, knockout and feeding studies show that membrane-bound syndecan-3 and its heparan-sulfate chains potentiate AgRP action and that SDC3 loss changes AgRP-dependent melanocortin feeding responses, supporting a co-receptor context rather than a standalone receptor interaction."
                limitations = "Retain AGRP-SDC3 as heparan-sulfate co-receptor evidence for the MC3R/MC4R pathway; do not assert a purified binary AGRP-SDC3 protein interface, treat SDC3 as the primary signaling receptor, or infer a universal intracellular or TF route outside the hypothalamic models."
            elif pair == ("AREG", "ERBB3"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:8626392", "PMID:32533590"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human T47D mammary epithelial and colon-cancer cell assays"
                summary = "Primary receptor-phosphorylation and cancer-cell studies show that amphiregulin can produce a moderate ERBB3 phosphorylation response and participate in EGFR/ERBB3 crosstalk, but AREG is established as an EGFR ligand and these assays do not establish a purified direct AREG-ERBB3 binding edge."
                limitations = "Retain AREG-ERBB3 as context-dependent functional crosstalk downstream of EGFR or other receptor activation; do not materialize a canonical direct AREG-to-ERBB3 ligand edge or infer a universal ERBB3 route outside the tested cell systems."
            elif pair == ("ARTN", "GFRA2"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:31535977"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human recombinant RET/GFR co-receptor structural and cell-based assays"
                summary = "Primary cryo-EM and cell-based studies resolve ARTN in an ARTN-GFRα3-RET complex and NRTN in an NRTN-GFRα2-RET complex; they do not support the public ARTN-GFRA2 pairing."
                limitations = "Represent ARTN with GFRA3/RET and NRTN with GFRA2/RET; do not transfer the co-receptor assignment across GDNF-family ligands or materialize ARTN-to-GFRA2."
            elif pair == ("BMP10", "BMPR1B"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:35504921", "PMID:28646109"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human recombinant BMP10 receptor-complex structures and human endothelial BMP9/10 receptor perturbation assays"
                summary = "Primary structural and endothelial perturbation studies support BMP10 signaling through BMPR2 with ALK1/ALK2 and ACTR-IIA-associated receptor contexts, not the listed BMPR1B/ALK6 receptor pair."
                limitations = "Represent BMP10 with the reported BMPR2-ALK1/ALK2 receptor contexts and preserve the endothelial/structural assay boundaries; do not materialize BMP10-to-BMPR1B or infer ALK6 specificity from BMP-family homology."
            elif pair == ("BMP15", "BMPR1A"):
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:24140593"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human SVOG and KGN granulosa-cell assays"
                summary = "Primary human granulosa-cell experiments show that BMP15 induces SMAD1/5/8 phosphorylation and suppresses StAR expression and progesterone production, while ALK3/BMPR1A depletion reverses the signaling and output effects, supporting a bounded BMP15-BMPR1A route."
                limitations = "Preserve the human granulosa-cell, BMP15 preparation and ALK3/BMPR1A receptor-specific siRNA context; the study supports receptor dependence and downstream output rather than purified extracellular binding, and does not establish a universal intracellular or terminal-TF chain."
            elif pair == ("BMP15", "TGFBR1"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:18633140"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse BMP15/GDF9 and rat granulosa-cell cooperative-signaling assays"
                summary = "Primary cooperative-signaling studies report that recombinant mouse BMP15 together with GDF9 signals through BMPR2 and ACVR1B/TGFBR1/ACVR1C-associated pathways, but the TGFBR1 contribution is a complex/cooperative context rather than an isolated BMP15-TGFBR1 binary edge."
                limitations = "Retain BMP15-TGFBR1 only as GDF9-dependent receptor-complex context; preserve species and cooperative ligand boundaries and do not materialize a standalone BMP15-to-TGFBR1 edge or infer a universal output route."
            elif pair == ("C3", "C5AR2"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:31274379"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse anaphylatoxin-receptor knockout and human whole-blood infection assays"
                summary = "Primary complement studies identify C5a and C5adesArg—not intact C3—as ligands for C5AR2, while C3 is processed into C3a and other fragments; the public C3-C5AR2 row therefore does not specify the direct ligand form."
                limitations = "Represent C5a/C5adesArg-to-C5AR2 and C3a-to-C3AR1 separately; do not materialize intact C3-to-C5AR2 or infer receptor activation from complement-family membership alone."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_084":
            pair = (ligand, receptor)
            if pair == ("PMCH", "MERTK"):
                disposition = "no_primary_evidence_found"
                primary = ["PMID:30501104"]
                layer = "candidate_only_review_locator"
                species = "review locator is a TYRO3-focused review; no exact PMCH-MERTK primary experiment verified"
                summary = "The public locator is a review focused on TYRO3 rather than an exact primary PMCH-MERTK ligand-receptor experiment, and the current pass did not verify a direct PMCH-MERTK study."
                limitations = "Retain for targeted primary review; do not materialize PMCH-MERTK from a review citation or from MERTK family membership."
            elif pair == ("SELE", "CEACAM1"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:1378450"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human CD66/CEACAM neutrophil adhesion and cytokine-activated endothelial-cell assays"
                summary = "The cited primary study concerns CD66 antigens on neutrophils and E-selectin-dependent adhesion, with sialylated Lewis-x structures as the E-selectin ligands; it does not establish SELE as a ligand for CEACAM1."
                limitations = "Represent the reported E-selectin/vascular-adhesion context with the appropriate CD66 glycoform and direction; do not materialize SELE-to-CEACAM1 from this locator."
            elif pair == ("NECTIN1", "CADM3"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:23027581"]
                layer = "receptor_proximal_or_pathway"
                species = "mammalian nectin-family adhesion review"
                summary = "The cited paper is a review of nectin-family cell-cell adhesion and does not provide an exact primary NECTIN1-CADM3 experiment; CADM3/Necl-1 is a nectin-like molecule rather than one of the canonical nectin family members discussed."
                limitations = "Retain canonical nectin trans-interactions only when the exact partner and primary assay are specified; do not materialize NECTIN1-to-CADM3 from the review citation."
            elif pair in {
                ("CEACAM1", "CD1D1"), ("CEACAM1", "CD1D2"), ("CEACAM1", "CD8A"),
                ("CEACAM2", "CD1D1"), ("CEACAM2", "CD1D2"), ("CEACAM2", "CD8A"),
            }:
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:24104458"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human intestinal epithelial CEACAM5-CD1d/CD8 interaction assays"
                summary = "The cited primary study identifies CEACAM5, not CEACAM1 or CEACAM2, as the CEACAM member interacting with CD1d and CD8alpha; the public rows therefore transfer a family-member interaction to the wrong CEACAM gene."
                limitations = "Represent the reported CEACAM5-CD1d/CD8 context with its intestinal epithelial and glycosylation boundaries; do not materialize CEACAM1/2-to-CD1D1/2 or CEACAM1/2-to-CD8A from this study."
            elif pair in {("CEACAM1", "PSG20"), ("CEACAM2", "PSG20")}:
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:24743304"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human soluble CEACAM8 and membrane CEACAM1 innate-immune assays"
                summary = "The cited primary study reports soluble CEACAM8 interaction with CEACAM1 and inhibition of TLR2-triggered responses; it does not support CEACAM1 or CEACAM2 as a ligand for PSG20."
                limitations = "Represent soluble CEACAM8-to-CEACAM1 interaction separately; do not transfer it to PSG20 or materialize CEACAM1/2-to-PSG20 from the cited study."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_085":
            pair = (ligand, receptor)
            if pair == ("COL1A2", "CD44"):
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:1730778"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human type-I collagen fibrils and isolated CD44 antigen in lymphocyte/HEV adhesion assays"
                summary = "Primary binding assays show that affinity-purified CD44 binds native type-I collagen fibrils; because COL1A2 is a component of the type-I collagen trimer, this supports a bounded collagen-I-component-to-CD44 interaction rather than an isolated alpha-2-chain assay."
                limitations = "Represent COL1A2 as a collagen-I trimer/fibril component and preserve the CD44 glycoform and extracellular-matrix context; do not infer binding by free COL1A2 monomer, a universal CD44 isoform, or a complete intracellular/TF route."
            elif pair == ("COL2A1", "SDC1"):
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:7949658"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human collagen I-VI affinity assays with murine mammary epithelial-cell syndecan-1"
                summary = "Primary affinity co-electrophoresis measurements show that syndecan-1 binds several human collagens, including type II collagen, with a lower affinity than types I, III, IV and V; this supports a bounded collagen-II-to-SDC1 extracellular interaction."
                limitations = "Preserve the collagen-II fibrillar form, syndecan-1 heparan-sulfate chain context and cross-species assay design; do not infer isolated COL2A1-chain binding, a protein-core-only mechanism, or a universal downstream route."
            elif pair == ("TRY4", "F2RL1"):
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:24749982"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse recombinant trypsin-4 and PAR2/F2RL1 calcium-signaling assays"
                summary = "Primary protease assays show that enterokinase-activated mouse trypsin-4 produces concentration-dependent calcium signaling in PAR2/F2RL1-expressing cells but not vector controls, supporting a direct protease-triggered PAR2 route."
                limitations = "Represent activated mouse trypsin-4 rather than the inactive zymogen, preserve the PAR2-expressing cell assay and protease-cleavage mechanism, and do not transfer this evidence to other Try genes or PAR family members."
            elif pair == ("WNT11", "FZD3"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:28916299", "PMID:19232955"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human bone-marrow mesenchymal-stem-cell and cardiac/progenitor Wnt11 signaling assays"
                summary = "Primary studies place Wnt11 among noncanonical Wnts associated with Fzd3/JNK or Fzd-mediated signaling, but the strongest direct Wnt11 receptor-binding and inhibition experiments identify Fzd4 rather than Fzd3; the public WNT11-FZD3 row is therefore contextual rather than an isolated exact-pair binding claim."
                limitations = "Retain WNT11-FZD3 as a plausible noncanonical receptor context with cell-state and co-receptor boundaries; do not materialize a universal direct WNT11-to-FZD3 edge or infer a unique downstream route from expression/co-occurrence alone."
            elif pair == ("RLN3", "RXFP2"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:15956688", "PMID:18434306", "PMID:25761609"]
                layer = "receptor_proximal_or_pathway"
                species = "human relaxin-family receptor pharmacology and peptide-structure assays"
                summary = "Primary relaxin-family pharmacology assigns relaxin-3 primarily to RXFP3, whereas RXFP2 is the cognate receptor for INSL3 and can also respond to relaxin; the cited evidence does not establish the public RLN3-RXFP2 pairing as a direct canonical route."
                limitations = "Represent RLN3-RXFP3 and INSL3-RXFP2 separately; do not transfer relaxin-family cross-reactivity or receptor-family homology into a direct RLN3-to-RXFP2 edge."
            elif pair == ("THBS4", "CD36"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:1371676", "PMID:7504322", "PMID:7688364"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human thrombospondin/CD36 binding and ectodomain-domain assays"
                summary = "Primary studies establish CD36 binding to thrombospondin and map thrombospondin motifs required for CD36 interaction, but they do not identify thrombospondin-4 specifically; the public THBS4-CD36 row is family-member context rather than exact isoform evidence."
                limitations = "Retain CD36-thrombospondin binding with thrombospondin isoform and CSVTCG/SVTCG motif boundaries; do not materialize THBS4-to-CD36 without an isoform-specific primary assay."
            elif pair == ("PRSS2", "F2RL2"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:12604689", "PMID:12463169", "PMID:24749982"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human/rat trypsin and proteinase-activated receptor cleavage/signaling assays"
                summary = "Primary PAR studies support trypsin-triggered PAR2/F2RL1 and broader protease/PAR signaling, while PAR3/F2RL2 is primarily described as a thrombin-responsive/cofactor receptor; no exact PRSS2-to-F2RL2 activation assay was verified."
                limitations = "Retain PRSS2-F2RL2 only as protease/PAR pathway context pending exact PRSS2 and PAR3 cleavage data; do not materialize a direct ligand edge or transfer PAR2/PAR4 evidence to PAR3."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_086":
            pair = (ligand, receptor)
            if pair == ("FGF2", "SDC4"):
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:19581409", "PMCID:PMC2712988"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human FGF2 and syndecan-4 signaling studies in endothelial-cell and epithelial-cell systems"
                summary = "Primary studies support FGF2 association with syndecan-4 and show syndecan-4-dependent PKC-alpha, RhoG/Rac1 and migration/proliferation responses, establishing a bounded FGF2-SDC4 proteoglycan coreceptor route."
                limitations = "Preserve syndecan-4 heparan-sulfate/proteoglycan and cell-context requirements; do not treat SDC4 as the canonical kinase receptor or infer a universal intracellular/TF chain from the reported proximal and functional outputs."
            elif pair == ("FGF2", "CD44"):
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:12697740", "PMCID:PMC152937"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human CD44 variant transfectants and primary rheumatoid-arthritis synovial cells with FGF2/FGFR1 binding assays"
                summary = "Primary experiments show that CD44 variant cells bind FGF2 through associated heparan-sulfate and that a CD44vRA context enhances cell-surface FGF2 presentation to soluble FGFR1 and the resulting mitogenic response, supporting a bounded FGF2-CD44 variant coreceptor route."
                limitations = "Represent CD44 variant/HS-dependent presentation rather than generic CD44 or isolated protein-core binding; preserve the human inflammatory-cell and FGFR1 assay context and do not infer a universal CD44 isoform or complete downstream route."
            elif pair in {("COL4A1", "SDC1"), ("COL6A1", "SDC1")}:
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:7949658"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human collagen IV/VI affinity assays with murine mammary epithelial-cell syndecan-1"
                collagen_type = "type IV" if ligand == "COL4A1" else "type VI"
                summary = f"Primary affinity co-electrophoresis measurements show that syndecan-1 binds human {collagen_type} collagen, supporting a bounded {collagen_type}-component-to-SDC1 extracellular interaction."
                limitations = f"Preserve native fibrillar {collagen_type} presentation, syndecan-1 heparan-sulfate chain context and the cross-species assay design; do not infer isolated {ligand} chain binding, a protein-core-only mechanism, or a universal downstream route."
            elif pair == ("COL4A1", "ITGA3+ITGB1"):
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:11900477"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human neuroblastoma collagen-IV adhesion and integrin-blocking assays"
                summary = "Primary cell-adhesion experiments show binding to intact collagen IV and inhibition by beta-1 and alpha-3 integrin blocking antibodies, supporting a bounded collagen-IV-to-alpha3beta1 receptor-complex interaction with matrix-remodeling outputs."
                limitations = "Represent intact collagen-IV heterotrimer and the alpha3beta1 receptor complex in the tested neuroblastoma context; the study uses blocking/adhesion assays rather than purified binary binding and does not establish a universal intracellular or TF route."
            elif pair == ("HGF", "SDC2"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:26381016"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "rat early-differentiated myoblast HGF/FGF2 and syndecan-2/4 perturbation assays"
                summary = "Primary myoblast experiments identify syndecan-2/4 as plausible HGF-response receptor candidates and show that knockdown or glycosaminoglycan degradation attenuates HGF-induced Sema3A expression, but the study does not isolate a direct HGF-to-SDC2 binding event."
                limitations = "Retain HGF-SDC2 as context-dependent proteoglycan/coreceptor evidence with syndecan-2/4 and glycosaminoglycan boundaries; do not materialize a direct binary edge or transfer the result to SDC2-independent HGF signaling."
            elif pair == ("FGF4", "NRP1"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:9531542", "PMID:10842181"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "mouse limb CD44-variant FGF4 presentation assays and human neuropilin-1 ligand-binding assays"
                summary = "Primary studies support FGF4 presentation by a CD44 splice variant and neuropilin-1 binding to VEGF165, but they do not establish FGF4 as a neuropilin-1 ligand; the public FGF4-NRP1 row therefore conflates distinct growth-factor presentation and neuropilin ligand contexts."
                limitations = "Represent FGF4-CD44 variant presentation and VEGF165-NRP1 separately; do not transfer FGF-family or neuropilin-family membership into a direct FGF4-to-NRP1 edge."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_087":
            pair = (ligand, receptor)
            if pair == ("CXCL10", "SDC4"):
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:20484822"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse bleomycin-induced pulmonary-fibrosis model and primary lung fibroblast assays"
                summary = "Primary studies show direct CXCL10-syndecan-4 interaction by radioligand binding and chemical crosslinking, with syndecan-4-dependent inhibition of fibroblast migration and antifibrotic activity; mutation of the CXCL10 heparin-binding domain reduces the effect."
                limitations = "Represent CXCL10-SDC4 as a heparan-sulfate proteoglycan interaction in the lung fibroblast/fibrosis context, distinct from CXCL10-CXCR3 signaling; do not infer a universal intracellular or terminal-TF route."
            elif pair == ("CXCL13", "ACKR4"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:32480426"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human systematic beta-arrestin screening of 43 chemokines against ACKR4"
                summary = "A systematic primary screening study specifically disproved agonist activity of CXCL13 toward ACKR4 while confirming CCL19, CCL20, CCL21, CCL25 and partial CCL22 activity; the public CXCL13-ACKR4 row should not be materialized."
                limitations = "Represent CXCL13 with its supported receptor context and preserve the negative ACKR4 screen; do not infer ACKR4 binding from the earlier family-level annotation or from CXCL13 homology."
            elif pair == ("CCL24", "CCR2"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:9365122"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human CCL24/eotaxin-2 cloning, CCR3-transfected-cell binding and eosinophil chemotaxis assays"
                summary = "Primary cloning and receptor assays identify CCL24/eotaxin-2 as a CCR3 ligand with eosinophil chemotactic activity; the cited study does not support transfer of the CCL24 pair to CCR2."
                limitations = "Represent CCL24-CCR3 with the tested eosinophil and receptor-transfectant context; do not transfer CCL11/CCL24 family evidence to CCR2 or infer a direct CCL24-CCR2 edge."
            elif pair in {("CCL21B", "ACKR2"), ("CCL25", "ACKR2")}:
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:19632987", "PMID:11981810", "PMID:23341447"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human/mouse atypical-chemokine-receptor ligand panels and CCX-CKR/ACKR4 binding and beta-arrestin assays"
                chemokine = "CCL21" if ligand == "CCL21B" else "CCL25"
                summary = f"Primary atypical-receptor studies place {chemokine} in the homeostatic CCX-CKR/ACKR4 ligand context and define D6/ACKR2 around inflammatory chemokine recognition, but the current evidence does not isolate a direct {chemokine}-to-ACKR2 experiment."
                limitations = f"Retain {ligand}-ACKR2 only as a receptor-family/context boundary with species and chemokine-processing limits; do not materialize a direct ACKR2 edge or transfer CCX-CKR/ACKR4 evidence to ACKR2."
            elif pair in {("CXCL10", "ACKR1"), ("CXCL11", "ACKR1")}:
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:13679391", "PMID:19060902"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse DARC/ACKR1 competitive-binding studies and human/mouse endothelial transcytosis assays"
                chemokine = "CXCL10" if ligand == "CXCL10" else "CXCL11"
                summary = f"Primary DARC/ACKR1 studies establish broad inflammatory-chemokine binding and receptor-mediated transport, but the cited assays do not provide a bounded isolated {chemokine}-ACKR1 experiment sufficient to promote this public row as a new binary edge."
                limitations = f"Retain {chemokine}-ACKR1 as plausible atypical-receptor context with DARC/ACKR1 cell-type and transport boundaries; do not infer exact affinity, scavenging, or canonical intracellular signaling from broad promiscuity."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_088":
            pair = (ligand, receptor)
            if pair == ("IL11", "IL6RA"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:39473075", "PMID:8940087"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human and murine IL-11/IL-11 receptor studies; human IL-6 receptor cross-reactivity study"
                summary = "Primary receptor studies identify IL11RA as the ligand-binding alpha receptor for IL-11 and gp130/IL6ST as the signaling partner; a direct cross-reactivity study reports that IL-11 does not bind IL-6R."
                limitations = "Represent IL11-IL11RA-gp130/IL6ST receptor-complex evidence separately; do not transfer IL-6Ralpha usage to IL-11 or infer an IL11-IL6RA edge from shared gp130 signaling."
            elif pair == ("IL22", "IL10RA"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:18599299"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human IL-22/IL-22R1/IL-10R2 structural and binding assays"
                summary = "Primary structural and binding experiments define IL-22 recognition by IL-22R1 and functional receptor assembly with IL-10R2/IL10RB; they do not support IL-10RA as the IL-22 receptor subunit."
                limitations = "Represent IL22-IL22RA1-IL10RB receptor-complex evidence; do not materialize IL22-IL10RA or conflate IL-10RA with IL-10R2/IL10RB."
            elif pair == ("IL15", "IL2RA"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:8026467", "PMID:8530383", "PMID:23104097"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human IL-15 receptor binding and reconstituted receptor-complex studies"
                summary = "Primary binding and structural studies show that IL-15 uses IL15RA for ligand-specific high-affinity recognition and signals through IL2RB/IL2RG; IL2RA is not the IL-15-specific alpha receptor and is not required for IL-15 binding."
                limitations = "Represent IL15-IL15RA-IL2RB-IL2RG complex evidence; do not transfer IL-2Ralpha usage to IL-15 or materialize IL15-IL2RA as a direct ligand-receptor edge."
            elif pair == ("CSF2", "IL3RA"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:8543766"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human GM-CSF and IL-3 receptor subunit expression and receptor-complex studies"
                summary = "Primary receptor studies distinguish the GM-CSF receptor alpha chain from IL-3Ralpha as separate ligand-specific binding components that share the common beta signaling subunit."
                limitations = "Represent CSF2/GM-CSF with CSF2RA and CSF2RB; do not transfer IL-3Ralpha specificity to GM-CSF or materialize CSF2-IL3RA from shared beta-chain signaling."
            elif pair == ("CNTF", "IL6RA"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:7500350", "PMID:18775332"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human CNTF receptor-complex biochemical and structural studies"
                summary = "Primary biochemical and structural studies define CNTF binding through CNTFRalpha and assembly of a CNTFRalpha-gp130/LIFR signaling complex; IL-6Ralpha is not the CNTF-specific receptor subunit."
                limitations = "Represent CNTF-CNTFR-LIFR/gp130 complex evidence; do not transfer IL-6Ralpha usage to CNTF or infer a direct CNTF-IL6RA edge from shared gp130-family signaling."
            elif pair == ("IL13", "IL2RG"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:18852293", "PMID:25766112"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human and murine IL-4/IL-13 receptor-complex and receptor-knockout studies"
                summary = "Primary receptor-complex and knockout studies show that IL-13 uses the type II IL4RA-IL13RA1 receptor and remains responsive when IL2RG is absent, whereas the common gamma chain is relevant to type I IL-4 signaling."
                limitations = "Represent IL13-IL4RA-IL13RA1 and its tested STAT6/output context; do not materialize IL13-IL2RG or transfer type I IL-4 receptor usage to IL-13."
            elif pair == ("IL21", "IL4RA"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:11418623", "PMID:22235133"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human IL-21 receptor-complex binding, cross-linking and structural studies"
                summary = "Primary studies define the functional IL-21 receptor as IL21R paired with the common gamma chain and demonstrate IL-21 binding to that complex; IL4RA is not identified as an IL-21 receptor subunit."
                limitations = "Represent IL21-IL21R-IL2RG complex evidence; do not transfer IL-4 receptor alpha usage to IL-21 or materialize IL21-IL4RA."
            elif pair == ("IL24", "IL10RB"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:12351624"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human IL-19/IL-20/IL-24 receptor-complex and reporter/signaling assays"
                summary = "Primary receptor-complex assays place IL-24 in the IL20RA-IL20RB and IL22RA1-IL20RB complexes, with reporter and STAT activation readouts; IL10RB is not the receptor subunit identified for IL-24 in these assays."
                limitations = "Represent IL24-IL20RA-IL20RB and IL24-IL22RA1-IL20RB complex evidence; do not conflate IL20RB with IL10RB or materialize IL24-IL10RB."
            elif pair in {("IL18", "IL1RL1"), ("IL18", "IL1RAPL1"), ("IL18", "IL1RL2")}:
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:9325300", "PMID:10227969"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human and murine IL-18 receptor binding and receptor-deficiency studies"
                summary = "Primary receptor purification, expression and receptor-deficiency studies identify IL18R1/IL-1Rrp as the essential IL-18 ligand-binding receptor; the reviewed studies do not support the candidate IL1-family paralog as the IL-18 receptor."
                limitations = "Represent IL18-IL18R1 with IL18RAP as the receptor-complex context; do not transfer IL-18 binding or signaling to IL1RL1, IL1RAPL1 or IL1RL2 without an exact pair-specific primary assay."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_089":
            pair = (ligand, receptor)
            if pair == ("CCL11", "ACKR4"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:32480426"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human systematic beta-arrestin screening of chemokines against ACKR4"
                summary = "A systematic primary screening study tested 43 chemokines against ACKR4 and did not identify CCL11/eotaxin-1 as an ACKR4 agonist, while defining the supported ACKR4 ligand panel."
                limitations = "Preserve the negative ACKR4 screen and CCL11's established CCR3 context; do not infer ACKR4 binding from CC-chemokine family membership or broad receptor promiscuity."
            elif pair == ("CCL20", "CXCR3"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:11373289", "PMID:19305396"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "murine CCL20 structure, receptor-specificity and CCR6-dependent CNS-entry studies"
                summary = "Primary studies define CCL20 as a highly selective CCR6 ligand and link CCL20-CCR6 to cellular recruitment; they do not support CCL20 as a CXCR3 ligand."
                limitations = "Represent CCL20-CCR6 with the reported structural and cell-migration context; do not transfer CCL20 activity to CXCR3 or infer a receptor edge from coexpression of CXCR3-positive cells."
            elif pair == ("CCL21B", "CXCR3"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:11907075"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "murine microglia and CCR7/CXCR3 knockout chemotaxis assays using CCL21-family ligand"
                summary = "Primary microglial experiments show that a CCL21-family ligand can activate CXCR3-dependent chloride current and chemotaxis in brain microglia, while CCR7 mediates the canonical lymphoid context; the study does not resolve the public CCL21B label as a distinct isoform."
                limitations = "Retain CCL21B-CXCR3 as cell-state- and isoform-bounded contextual evidence, especially for CNS microglia; do not generalize it to canonical lymphoid CCL21 signaling or materialize a universal CCL21B-CXCR3 edge without isoform-resolved primary evidence."
            elif pair == ("CCL25", "CCR10"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:17548595"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "murine CCL25-deficient and CCR9-deficient intestinal immune-cell studies"
                summary = "Primary genetic and lymphocyte-trafficking studies define CCL25 and CCR9 as the relevant gut-homing chemokine/receptor pair and report matching phenotypes in CCL25- and CCR9-deficient mice; they do not support CCR10 as the CCL25 receptor."
                limitations = "Represent CCL25-CCR9 with the gut and thymic context tested in the primary study; do not transfer CCL25 activity to CCR10 or infer receptor specificity from chemokine-family relationships."
            elif pair == ("CCL11", "CCR5"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:8642344", "PMID:11559700"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human CCL11/CCR3 cloning and human CCL11/CCR2b partial-agonist studies"
                summary = "Primary studies establish CCR3 as the high-affinity eosinophil receptor for CCL11 and separately report weak, high-concentration partial agonism at CCR2b; they do not verify direct CCL11-to-CCR5 activation."
                limitations = "Retain CCL11-CCR5 only as a bounded unresolved chemokine-family context pending an exact CCR5 assay; represent the demonstrated CCR3 and CCR2b activities separately and do not promote a direct CCR5 edge."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_090":
            pair = (ligand, receptor)
            if pair == ("PMCH", "MERTK"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:25265470", "PMID:11825022"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "murine and rat TAM-receptor biochemical, genetic and phagocytosis studies"
                summary = "Primary studies identify GAS6 and PROS1 as the endogenous TAM ligands and demonstrate GAS6-dependent MERTK activation and phagocytosis; PMCH is not established as a MERTK ligand."
                limitations = "Represent GAS6/PROS1-TAM receptor signaling with phosphatidylserine and efferocytosis context; do not materialize PMCH-MERTK or infer receptor activation from a review locator that discusses TAM biology."
            elif pair == ("TNC", "SDC1"):
                disposition = "reject_precursor_or_non_edge_form"
                primary = ["PMID:11731446"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human and murine glioblastoma/breast-carcinoma cell adhesion assays with tenascin-C and syndecan perturbations"
                summary = "Primary matrix-adhesion experiments identify direct tenascin-C interaction with fibronectin FNIII13 and interference with the fibronectin-syndecan-4 coreceptor mechanism; syndecan-1 overexpression does not restore the adhesion defect."
                limitations = "Represent the tenascin-C/fibronectin/syndecan-4 boundary and do not transfer the reported syndecan-4 mechanism to syndecan-1 or materialize a direct TNC-SDC1 edge."
            elif pair == ("COL2A1", "CD44"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:1730778"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human affinity-purified CD44 binding to native type-I collagen fibrils and other matrix ligands"
                summary = "Primary binding assays show CD44 interaction with native type-I collagen fibrils, laminin and fibronectin, but do not test type-II collagen or isolate the COL2A1 chain; the public COL2A1-CD44 row remains collagen-family context."
                limitations = "Retain CD44 binding to the tested native matrix forms and preserve collagen-trimer/isoform boundaries; do not transfer type-I collagen evidence to type-II collagen or materialize COL2A1-CD44 without a pair-specific assay."
            elif pair == ("LAMC3", "CD44"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:1730778", "PMID:10225960", "PMID:18697739"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human CD44 matrix-binding assays and human/murine laminin-gamma3 characterization"
                summary = "Primary studies show CD44 binding to laminin in a broad matrix assay and separately characterize laminin-gamma3-containing isoforms, but do not establish a direct LAMC3-specific CD44 binding event."
                limitations = "Retain laminin-family/CD44 context with gamma3-chain and isoform boundaries; do not transfer generic laminin binding to LAMC3 or materialize LAMC3-CD44 without an exact assay."
            elif pair in {("THBS2", "SDC1"), ("THBS4", "SDC1")}:
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:11257118"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "murine/human thrombospondin-1 and syndecan-1 cell-spreading/fascin-spike assays"
                thrombospondin = "THBS2" if ligand == "THBS2" else "THBS4"
                summary = f"Primary experiments support syndecan-1-dependent matrix responses to thrombospondin-1, but do not test {thrombospondin} specifically; the public row is retained as thrombospondin-family context rather than an exact isoform edge."
                limitations = f"Preserve the demonstrated THBS1-SDC1 glycosaminoglycan and cytoplasmic-domain context; do not transfer THBS1 evidence to {thrombospondin} or materialize a direct {thrombospondin}-SDC1 edge without isoform-specific primary evidence."
            else:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The reviewed locator was not verified as an exact primary experiment for this ligand-receptor pair in the current pass."
                limitations = "Retain for targeted primary review; do not materialize a graph edge from public-database membership or family-level context alone."
        elif row.get("review_batch") == "batch_091":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The database locator PMID:15114347 is a commentary and is not treated as primary support; "
                "the existing graph edge-source records provide the primary locators and bounded assay context."
            )
            limitations = (
                "Do not add a duplicate edge from the public row or use the commentary as primary evidence. "
                "Preserve each existing edge's receptor, species, topology and downstream-layer boundaries; "
                "the existing edge does not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_092":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The database locator PMID:15207812 is a review and is not treated as primary support; "
                "the existing graph edge-source records provide pair-specific primary locators and bounded assay context."
            )
            limitations = (
                "Do not add a duplicate edge from the public row or use the review as primary evidence. "
                "Preserve each existing PDGF ligand form, receptor-dimer topology, species and assay boundary; "
                "the existing edge does not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_093":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are retained as reviewed context; the existing graph edge-source records "
                "provide pair-specific primary studies for FLRT/ADGRL or TENM4/ADGRL binding and bounded adhesion outputs."
            )
            limitations = (
                "Do not add a duplicate edge from the public row. Preserve FLRT or teneurin ligand form, "
                "ADGRL paralog, trans-cellular adhesion/complex topology and species boundaries; the existing "
                "edge does not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_094":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locator PMID:27533782 is a semaphorin review and is not treated as primary support; "
                "the existing graph edge-source records provide pair-specific primary binding, receptor-complex "
                "or functional studies with bounded species and co-receptor context."
            )
            limitations = (
                "Do not add a duplicate edge from the public row or treat the semaphorin-family review as a pair-specific "
                "primary experiment. Preserve semaphorin ligand form, plexin/neuropilin complex topology and assay "
                "boundaries; the existing edge does not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_095":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators PMID:23916315 and PMID:29674953 are reviews and are not treated as primary support; "
                "the existing graph edge-source records provide pair-specific SALM/LRFN or LRRC4B/NGL3 primary studies "
                "for LAR-RPTP binding and bounded synaptic-organizer outputs."
            )
            limitations = (
                "Do not add a duplicate edge from the public row or treat family-level review text as a pair-specific primary experiment. "
                "Preserve SALM/LRFN isoform aliases, LAR-RPTP paralog, splice-insert and trans-synaptic topology boundaries; "
                "the existing edge does not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_096":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locator PMID:31462748 is an adhesion-GPCR review and is not treated as primary support; "
                "the existing graph edge-source records provide pair-specific studies for CD55/CD97, TG2/ADGRG1, "
                "integrin/ADGRE5, PrP/ADGRG6 or RTN4R/ADGRB1 in their stated assay contexts."
            )
            limitations = (
                "Do not add a duplicate edge from the public row or treat the adhesion-GPCR review as a pair-specific primary experiment. "
                "Preserve ligand form, adhesion-GPCR receptor processing, receptor-complex and species boundaries; "
                "the existing edge does not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_097":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locator PMID:24223577 is an NK-cell receptor/ligand review and is not treated as primary support; "
                "the existing graph edge-source records provide pair-specific studies for CLEC2D/KLRB1-family, CLEC2I/KLRB1F, "
                "H60A/KLRK1 or ULBP1/KLRK1 recognition and bounded NK-cell outputs."
            )
            limitations = (
                "Do not add a duplicate edge from the public row or treat the NK-cell review as a pair-specific primary experiment. "
                "Preserve receptor paralog, species, activating/inhibitory direction and NKG2D or NKRP1 complex boundaries; "
                "the existing edge does not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_098":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators PMID:28873464 and PMID:28190785 are review or review-guided sources and are not treated "
                "as the sole primary support; the existing graph edge-source records provide pair-specific IGF1/IGF2-integrin "
                "binding, integrin/IGF1R ternary-complex and bounded signaling/output studies."
            )
            limitations = (
                "Do not add a duplicate edge from the public row or treat an integrin subunit as a free-standing receptor. "
                "Preserve the ITGA6+ITGB4 or ITGAV+ITGB3 heterodimer, IGF ligand form, IGF1R crosstalk and assay/species "
                "boundaries; the existing edge does not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_099":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locator PMID:28676852 is a CD40L receptor review and is not treated as primary support; "
                "the existing graph edge-source records provide pair-specific CD40L-integrin binding and bounded platelet, "
                "endothelial or leukocyte functional studies."
            )
            limitations = (
                "Do not add a duplicate edge from the public row or treat the CD40L review as a pair-specific primary experiment. "
                "Preserve the alphaIIb-beta3, alpha5-beta1 or alphaM-beta2 heterodimer, soluble versus membrane CD40L form, "
                "biased-adhesive versus signaling behavior and species/cell context; the existing edge does not assert a universal "
                "intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_100":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are review, pathway, or primary-study records and are not treated as a substitute "
                "for pair-specific validation; the existing graph edge-source records provide primary-supported "
                "ligand-receptor binding or activation and bounded receptor-proximal or functional observations."
            )
            limitations = (
                "Do not add a duplicate edge from the public row. Preserve ligand processing or presentation, receptor "
                "complex and paralog boundaries, species and cell-system context, and the distinction between binding, "
                "receptor-proximal signaling and functional output; the existing edges do not assert a universal "
                "intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_101":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway, review, or contextual records and are not treated as a substitute "
                "for pair-specific validation; the existing graph edge-source records provide primary-supported "
                "ligand-receptor binding or activation and bounded receptor-proximal or functional observations."
            )
            limitations = (
                "Do not add a duplicate edge from the public row. Preserve ligand form, receptor complex or paralog "
                "boundaries, species and cell-system context, and the distinction between binding, receptor-proximal "
                "signaling and functional output; the existing edges do not assert a universal intracellular cascade "
                "or terminal TF route."
            )
        elif row.get("review_batch") == "batch_102":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway, review, contextual, or database records and are not treated as a "
                "substitute for pair-specific validation; the existing graph edge-source records provide primary-supported "
                "ligand-receptor binding or activation and bounded receptor-proximal or functional observations."
            )
            limitations = (
                "Do not add a duplicate edge from the public row. Preserve neurotrophin or TNF-superfamily ligand form, "
                "receptor complex, decoy-receptor and paralog boundaries, species and cell-system context, and the "
                "distinction between binding, receptor-proximal signaling and functional output; the existing edges do "
                "not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_103":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records and are not treated as a substitute for pair-specific "
                "validation; the existing graph edge-source records provide primary-supported TNF-superfamily or WNT "
                "ligand-receptor binding and bounded receptor-proximal or functional observations."
            )
            limitations = (
                "Do not add a duplicate edge from the public row. Preserve TNF-superfamily receptor paralogs and decoy or "
                "co-receptor boundaries, WNT-FZD receptor specificity, species and cell-system context, and the distinction "
                "between binding, receptor-proximal signaling and functional output; the existing edges do not assert a "
                "universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_104":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are review, pathway, or contextual records and are not treated as a substitute "
                "for pair-specific validation; the existing graph edge-source records provide primary-supported "
                "ligand-receptor binding and bounded receptor-proximal or functional observations."
            )
            limitations = (
                "Do not add a duplicate edge from the public row. Preserve receptor heterodimers and co-receptor "
                "requirements, chemokine-receptor family boundaries, adhesion or homophilic-complex context, species "
                "and cell-system limits, and the distinction between binding, receptor-proximal signaling and "
                "functional output; the existing edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_105":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are review, pathway, or contextual records and are not treated as a substitute "
                "for pair-specific validation; the existing graph edge-source records provide primary-supported "
                "binding or complex formation and bounded receptor-proximal or functional observations."
            )
            limitations = (
                "Do not add a duplicate edge from the public row or collapse a heterodimer, junctional complex, or "
                "co-receptor requirement to a free subunit. Preserve integrin, JAM, FLRT/UNC5, inhibin/betaglycan, "
                "and MDK receptor-context boundaries, species and cell-system limits, and the distinction between "
                "binding, receptor-proximal signaling and functional output; the existing edges do not assert a "
                "universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_106":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are review, pathway, or contextual records and are not treated as a substitute "
                "for pair-specific validation; the existing graph edge-source records provide primary-supported "
                "ligand-receptor binding or receptor-complex formation and bounded receptor-proximal or functional observations."
            )
            limitations = (
                "Do not add a duplicate edge from the public row. Preserve nectin adhesion specificity, NPR1 receptor "
                "context, GFRA4:RET complex formation, FPR1 family boundaries, VEGF ligand processing and VEGFR/NRP "
                "co-receptor context, species and cell-system limits, and the distinction between binding, receptor-proximal "
                "signaling and functional output; the existing edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_107":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported VEGF binding/activation, protease-disintegrin adhesion, or receptor-complex "
                "observations at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or reinterpret every protease/disintegrin or receptor-cross-talk observation "
                "as a canonical freely secreted ligand. Preserve VEGF processing and receptor context, ADAM disintegrin "
                "domain versus full-length protein, ACE/B2R cross-talk, EphA3 cleavage context, integrin heterodimers, "
                "species and assay limits, and the distinction between binding, receptor-proximal signaling and functional "
                "output; the existing edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_108":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported disintegrin-integrin adhesion, receptor pharmacology or ligand-binding, "
                "and bounded receptor-proximal or functional observations at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or treat every ADAM/AGRN adhesion interaction as a canonical freely secreted "
                "ligand-receptor signaling route. Preserve disintegrin-domain versus full-length protein, integrin "
                "heterodimer, PACAP receptor cross-reactivity, AGRP antagonist pharmacology, AGT receptor subtype and "
                "species/assay limits; the existing edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_109":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported ligand-receptor, accessory-complex or receptor-proximal observations and "
                "bounded functional outputs at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse accessory receptors, integrin heterodimers, lipoprotein uptake "
                "receptors, proteoglycan/TLR complexes, or endoglin/type-II receptor assemblies into a single canonical "
                "receptor. Preserve ANGPT1, apoE, APP, amphiregulin, biglycan and BMP processing/context boundaries, "
                "species and assay limits, and the distinction between binding, receptor-proximal signaling and output; "
                "the existing edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_110":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported ligand-receptor or opsonin/complement-complex binding and bounded "
                "receptor-proximal or functional observations at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or treat precursor and processed complement/antimicrobial forms as interchangeable. "
                "Preserve betacellulin ERBB receptor context, iC3b versus C3b/C4b ligand forms, integrin heterodimers, "
                "calreticulin uptake/opsonin complexes, FPR2/FPRL1 receptor nomenclature, species and assay limits, and "
                "the distinction between binding, receptor-proximal signaling and functional output; the existing edges do "
                "not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_111":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported chemokine-receptor, complement-factor, homophilic-adhesion or integrin-complex "
                "binding and bounded receptor-proximal or functional observations."
            )
            limitations = (
                "Do not add a duplicate edge or collapse chemokine receptor paralogs, complement-factor processing, "
                "homophilic CD99, Osteolectin integrin complexes, or CNTN2/L1CAM neural adhesion complexes into a single "
                "canonical receptor. Preserve ligand form, heterodimer/complex resolution, species and assay limits, "
                "and the distinction between binding, receptor-proximal signaling and functional output; the existing "
                "edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_112":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported collagen or extracellular-matrix binding and bounded receptor-complex or "
                "functional observations at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or treat an isolated collagen gene product as equivalent to the assembled "
                "collagen matrix, NC1/domain fragment, or modification-dependent fibril. Preserve GP6, DDR1, PTPRS, "
                "CD36, CD47 and integrin heterodimer/co-receptor resolution, matrix-processing and species/assay limits, "
                "and the distinction between binding, receptor-proximal signaling and functional output; the existing "
                "edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_113":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported collagen/matrix, co-receptor or chemokine-integrin binding and bounded "
                "receptor-proximal or functional observations at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse assembled collagen matrices, matrix domains, syndecan "
                "co-receptors, CSF1R complexes, or CX3CL1 integrin/CX3CR1 coreceptor branches into a single canonical "
                "receptor. Preserve GP6 and integrin heterodimer resolution, matrix processing, species and assay limits, "
                "and the distinction between binding, receptor-proximal signaling and functional output; the existing "
                "edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_114":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported atypical chemokine-receptor, integrin-complex, matrix-DAMP, noncanonical "
                "Notch, ectodermal-development or DEL-1-integrin binding and bounded receptor-proximal or functional "
                "observations at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse chemokine scavenging receptors, integrin heterodimers, "
                "decorin/TLR2 matrix-DAMP topology, DLK2 noncanonical Notch modulation, EDAR or DEL-1 integrin "
                "complexes into a single canonical receptor. Preserve processed ligand, heterodimer/complex resolution, "
                "species and assay limits, and the distinction between binding, receptor-proximal signaling and "
                "functional output; the existing edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_115":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported ephrin/pseudokinase, ERBB, coagulation-integrin, fibrillin/fibulin, "
                "fibrinogen-integrin or vascular-adhesion binding and bounded receptor-proximal or functional "
                "observations at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse EphB6 pseudokinase binding, ERBB receptor-family usage, "
                "Mac-1 heterodimers, fibrillin/fibulin matrix domains, fibrinogen motifs, or endothelial adhesion "
                "complexes into a single canonical receptor. Preserve processed or recombinant ligand forms, "
                "integrin heterodimer and motif/complex resolution, species and assay limits, and the distinction "
                "between binding, receptor-proximal signaling and functional output; the existing edges do not assert "
                "a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_116":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported intracellular FGF13–SCN5A association, FGF21–KLB binding, syndecan "
                "heparan-sulfate presentation, fibrinogen gamma-motif recognition, irisin–integrin binding, "
                "GDF15–GFRAL/RET complex signaling or GPIbalpha–Mac-1 adhesion observations at the stated molecular "
                "resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse intracellular auxiliary-factor association, beta-Klotho or "
                "GFRAL/RET receptor complexes, syndecan co-receptors, fibrinogen motifs, processed irisin, or "
                "GPIbalpha/Mac-1 adhesion topology into a single canonical receptor. Preserve processed ligand, "
                "heterodimer/complex and motif resolution, donor/reporter and cell-type context, species and assay "
                "limits, and the distinction between binding, receptor-proximal signaling and functional output; the "
                "existing edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_117":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported HGF/syndecan-MET coreceptor, gp96-LRP1 uptake or innate signaling, "
                "perlecan/integrin matrix, amylin receptor-complex, beta-integrin adhesion, IGFBP4–FZD8 WNT "
                "modulation, IL-22 decoy, or IL-25 heteroreceptor binding and bounded functional observations at the "
                "stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse syndecan and MET coreceptor roles, released gp96, perlecan "
                "domains, CALCR:RAMP complexes, beta2-integrin heterodimers, FZD8:LRP6 context, soluble IL22RA2, "
                "or IL17RA:IL17RB heteroreceptor assembly into a single canonical receptor. Preserve processed or "
                "domain-specific ligand forms, heterodimer/complex resolution, cell-type and donor/reporter context, "
                "species and assay limits, and the distinction between binding, receptor-proximal signaling and "
                "functional output; the existing edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_118":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported IL-34/CSF1R, IL-4 receptor-complex, inhibin-A/betaglycan, kininogen–Mac-1, "
                "L1CAM–ERBB cis-association, laminin/syndecan adhesion, LCN2–LRP2 uptake, leptin–ISLR2 binding and "
                "bounded receptor-proximal or functional observations at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse composite ligands, type-I versus type-II IL-4 receptor "
                "complexes, inhibitory betaglycan/ActRII assemblies, Mac-1 heterodimers, L1CAM cis-association, "
                "laminin domains, soluble or endocytic receptor forms, or LEP/ISLR2 versus LEPR branches into a "
                "single canonical receptor. Preserve processed/domain-specific ligand forms, heterodimer/complex and "
                "coreceptor resolution, species and assay limits, and the distinction between binding, receptor-proximal "
                "signaling and functional output; the existing edges do not assert a universal intracellular cascade or "
                "terminal TF route."
            )
        elif row.get("review_batch") == "batch_119":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported galectin-CD45 modulation, lipoprotein-lipase LRP1/megalin clearance, "
                "LRIG1-EGFR inhibition, RAP/LRP1 chaperone association, NGL/netrin trans-synaptic adhesion, "
                "lumican-integrin inhibition, midkine-syndecan association or MFG-E8 integrin-opsonin bridging and "
                "bounded receptor-proximal or functional observations at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse glycan-dependent CD45 modulation, clearance receptors, "
                "soluble LRIG1 ectodomain, intracellular RAP chaperone, NGL/netrin synaptic complexes, matrix-core "
                "domains, syndecan glycosaminoglycan context, or MFG-E8 phosphatidylserine bridges into a single "
                "canonical receptor. Preserve processed/domain-specific ligand forms, heterodimer/complex and "
                "opsonin topology, species and assay limits, and the distinction between binding, receptor-proximal "
                "signaling and functional output; the existing edges do not assert a universal intracellular cascade or "
                "terminal TF route."
            )
        elif row.get("review_batch") == "batch_120":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported MIA–integrin inhibition, MMP protease processing or LRP1 clearance, "
                "MSMP–CCR2 chemotaxis, NCAM1 homophilic adhesion and Norrin–FZD4 WNT activation observations at the "
                "stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse alpha4beta1/alpha5beta1 complexes, protease-substrate "
                "processing, LRP1 endocytic clearance, mature MSMP/CCR2B chemokine-like signaling, NCAM1 homophilic "
                "adhesion, or the Norrin-FZD4-LRP5/6-TSPAN12 multicomponent WNT receptor into a single canonical "
                "receptor. Preserve active/pro-forms, domains and cleavage sites, heterodimer/complex resolution, "
                "species and assay limits, and the distinction between binding, receptor-proximal signaling and "
                "functional output; the existing edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_121":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported nectin-2/CD226 or TIGIT binding, nidogen-integrin matrix adhesion and "
                "survival, pooled neuroligin-neurexin transcellular adhesion/function, or ANP–NPR2 receptor activation "
                "at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse CD112 homodimer/cis-competition, weak TIGIT binding, nidogen "
                "integrin heterodimers, pooled neuroligin/neurexin subtypes, or ANP receptor-subtype differences into "
                "a single canonical receptor. Preserve ectodomain, matrix and heterocomplex resolution, directional "
                "cell-contact topology, species and assay limits, and the distinction between binding, receptor-proximal "
                "signaling and functional output; the existing edges do not assert a universal intracellular cascade or "
                "terminal TF route."
            )
        elif row.get("review_batch") == "batch_122":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide evidence-bounded natriuretic-peptide NPR3 clearance, NPY4R binding, NRG/ERBB3 or ERBB4 "
                "activation, netrin-4/UNC5A binding, OMgp/NgR1 myelin inhibition and bounded receptor-proximal or "
                "functional observations at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse NPR3 clearance versus guanylyl-cyclase receptor branches, "
                "NPY/PP-family receptor pharmacology, NRG EGF-like ligand forms and ERBB heterodimers, integrin/ERBB "
                "ternary complexes, UNC5A nomenclature, or OMgp NgR1-associated receptor complexes into a single "
                "canonical receptor. Preserve ligand form, receptor-complex and co-receptor resolution, species and "
                "assay limits, and the distinction between binding, receptor-proximal signaling and functional output; "
                "the existing edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_123":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported PD-L2/RGMb binding, PDGF-CC/PDGFR heterodimer binding, OGF/OGFR growth "
                "inhibition, PF4/thrombomodulin modulation, tPA or pro-uPA LRP1 clearance/signaling, PODXL2/L-selectin "
                "adhesion, PVR/CD226 or TIGIT checkpoint binding, and PYY/NPY4R binding at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse PD-1 versus RGMb branches, activated PDGF growth-factor-domain "
                "forms, processed OGF versus intact PENK, free tPA versus PAI-1 complexes, pro-uPA versus active uPA, "
                "glycoform-dependent L-selectin ligands, PF4/thrombomodulin GAG context, or PVR competition between "
                "CD226/TIGIT/CD96 into a single canonical receptor. Preserve ligand processing, receptor-complex and "
                "glycoform resolution, species and assay limits, and the distinction between binding, receptor-proximal "
                "signaling and functional output; the existing edges do not assert a universal intracellular cascade or "
                "terminal TF route."
            )
        elif row.get("review_batch") == "batch_124":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            if (ligand, receptor) in {("S100A8", "TLR4"), ("S100A9", "TLR4")}:
                primary = ["PMCID:PMC2671563", "PMCID:PMC4291901"]
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported RGMa/BMPR1B co-receptor binding, S100A10/p11 channel or receptor trafficking, "
                "S100A8/A9 RAGE, TLR4, CD36, CD69 or Mac-1 branches, and bounded receptor-proximal or functional "
                "observations at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse S100 homodimers versus heteromers, arachidonic-acid cargo, "
                "ANXA2/S100A10 auxiliary complexes, TLR4-MD2 or RAGE co-receptor assemblies, Mac-1 heterodimers, "
                "or RGMa/BMP type-I receptor co-receptor topology into a single canonical receptor. Preserve ligand "
                "oligomer and cargo form, glycoform and auxiliary-complex resolution, species and assay limits, and "
                "the distinction between binding, receptor-proximal signaling and functional output; the existing edges "
                "do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_125":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported S100B-RAGE, SAA1-TLR2, secretin-SCTR, syndecan-2-CD148, "
                "semaphorin receptor-complex, surfactant-protein-D-LAIR1, ShhN-megalin, Slit2-glypican and "
                "bounded SAA/SCARB1 interaction or downstream observations at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse S100B oligomer states, SAA preparation and lipid/HDL context, "
                "SCTR second-messenger signaling, syndecan ectodomain binding, Sema3E PlexinD1/NRP1/VEGFR2 topology, "
                "SEMA4B cellular association, SP-D multitrimeric form, ShhN uptake versus PTCH1 signaling, or "
                "Slit2 heparan-sulfate-dependent glypican binding into a single canonical receptor. Preserve ligand "
                "processing, oligomer, glycan, co-receptor and complex resolution, species and assay limits, and the "
                "distinction between binding, receptor-proximal signaling and functional output; the existing edges do "
                "not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_126":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported Slitrk3-PTPRS synaptic adhesion, SPARC-endoglin modulation, "
                "SPON2/mindin-integrin adhesion, TFF2-CXCR4 activation, TGF-alpha-EGFR activation, TGF-beta1 "
                "ALK1 receptor-complex signaling and THBS2-alpha4beta1 adhesion at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse LAR-RPTP splice context, SPARC endoglin-alphaV crosstalk, "
                "mindin matrix-bound activation-state-dependent alpha4beta1 versus alpha5beta1 interactions, "
                "high-dose TFF2-CXCR4 signaling, TGF-alpha EGFR binding versus activation, TGF-beta1 ALK5/TGFBR2 "
                "co-receptor topology, or processed THBS2 N-terminal alpha4beta1 fragments into autonomous binary "
                "receptors. Preserve ligand domain, processed form, receptor heterodimer and co-receptor resolution, "
                "species and assay limits, and the distinction between binding, receptor-proximal signaling and "
                "functional output; the existing edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_127":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported tenascin-C-PTPRB adhesion, TNF-TNFR2 adaptor context, TWEAK-CD163 "
                "scavenging, 4-1BBL-TNFRSF9 assembly, tryptase-PAR2 activation, VEGFA-neuropilin complex evidence, "
                "WFIKKN2-PRTG binding, WNT3A-RYK coreceptor function and WNT5B-FZD2 pathway observations at the "
                "stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse alternatively spliced TNC domains, TNFR2-associated TRAF "
                "adaptor bridges, CD163 scavenging versus Fn14 signaling, 4-1BB receptor oligomerization, proteolytic "
                "PAR2 activation, VEGFA isoform/heparin-dependent neuropilin complexes, WFIKKN2 extracellular binding, "
                "RYK context-dependent FZD coupling, or WNT5B FZD2 versus other FZD binding/pathway contexts into a "
                "single canonical receptor. Preserve ligand processing, isoform, receptor-complex and co-receptor "
                "resolution, species and assay limits, and the distinction between binding, receptor-proximal signaling "
                "and functional output; the existing edges do not assert a universal intracellular cascade or terminal "
                "TF route."
            )
        elif row.get("review_batch") == "batch_128":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported WNT5B-FZD4/5/7/8 CRD binding, Elabela-APLNR activation, CD99-PILRA "
                "glycan-dependent binding, CEACAM1 homophilic adhesion, collagen-III-ADGRG1 engagement, "
                "thyrostimulin-TSHR activation and evidence-bounded IAPP amylin-receptor-complex records at the "
                "stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse WNT5B FZD cysteine-rich-domain binding into full-length "
                "receptor activation, Elabela/proElabela processing, CD99 glycosylation, CEACAM1 homophilic adhesion, "
                "collagen-III matrix presentation and ADGRG1 cleavage, GPHA2:GPHB5 thyrostimulin heterodimer form, "
                "or CALCR/RAMP amylin receptor-complex topology into autonomous binary receptors. Preserve ligand "
                "domain, glycan, processing, heterodimer and receptor-complex resolution, species and assay limits, "
                "and the distinction between binding, receptor-proximal signaling and functional output; frozen IAPP "
                "records remain evidence-bounded and do not assert a primary locator, universal intracellular cascade "
                "or terminal TF route."
            )
        elif row.get("review_batch") == "batch_129":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported IAPP-CALCR/RAMP3 amylin-complex assembly, galectin-9-CD44 and TIM-3 "
                "interactions, LRRTM4-GPC4-PTPRS synaptic organization, NRG1-integrin/ERBB3 crosstalk, PPIA-CD147 "
                "activation, Sema4A-Tim-2, tubby-MerTK and TULP1-AXL interaction or functional observations at the "
                "stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse CALCR/RAMP amylin receptor complexes, galectin glycan and "
                "CD44 isoform context, the LRRTM4-GPC4-PTPRS three-component heparan-sulfate complex, NRG1 "
                "integrin-ErbB3 ternary topology, PPIA secreted/heparan-sulfate-assisted CD147 binding, mouse Tim-2, "
                "tubby MerTK cargo/phagocytosis, or TULP1 TAM-receptor spectrum into autonomous binary receptors. "
                "Preserve ligand processing, glycan, splice, heterodimer and co-receptor resolution, species and assay "
                "limits, and the distinction between binding, receptor-proximal signaling and functional output; the "
                "IAPP-CALCR/RAMP1 row remains evidence-bounded where no stable primary locator is present, and the "
                "existing edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_130":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported TULP1-MerTK/TYRO3 interactions, ADAM15-alphaVbeta3 binding, BAI1-RTN4R "
                "binding, ALKAL1-LTK and ALKAL2-ALK/LTK activation, mature AMH-AMHR2 binding and evidence-bounded "
                "AMH type-I-receptor-complex records at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse TULP1 TAM-receptor spectrum, ADAM15 RGD disintegrin-domain "
                "binding, BAI1 TSR3 glycosylation and RTN4R trans-complexes, ALKAL1/ALKAL2 ligand hierarchy, mature "
                "AMH dimer/prodomain processing, or AMH BMPR1A/ACVR1 type-I co-receptor redundancy into autonomous "
                "binary receptors. Preserve ligand domain, processing, glycosylation, receptor-complex and co-receptor "
                "resolution, species and assay limits, and the distinction between binding, receptor-proximal signaling "
                "and functional output; the frozen AMH type-I rows remain evidence-bounded where no stable primary "
                "locator is present, and the existing edges do not assert a universal intracellular cascade or terminal "
                "TF route."
            )
        elif row.get("review_batch") == "batch_131":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported ANGPT2-integrin, ANGPTL1-alpha1beta1, ANGPTL2-alpha5beta1, "
                "ANGPTL3-alphaVbeta3 and evidence-bounded AMH-BMPR1B or ANGPTL4-alpha5beta1 receptor-complex "
                "observations at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse ANGPT2 alphaVbeta3/alphaVbeta5/alpha5beta1 complexes, "
                "ANGPTL1 alpha1beta1, ANGPTL2 alpha5beta1 versus PIRB, ANGPTL3 alphaVbeta3 fibrinogen-like-domain "
                "binding, AMH type-I receptor redundancy, or ANGPTL4 integrin context into a single canonical receptor. "
                "Preserve ligand domain, integrin heterodimer, co-receptor and context resolution, species and assay "
                "limits, and the distinction between binding, receptor-proximal signaling and functional output; frozen "
                "AMH-BMPR1B and ANGPTL4-alpha5beta1 records remain evidence-bounded where no stable primary locator is "
                "present, and the existing edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_132":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported ANGPTL4-alphaVbeta5/alphaVbeta3 and beta1-associated integrin evidence, "
                "ANPEP/CD13-E-selectin glycoform binding, APP-LRP10 trafficking, ARTN-GFRalpha3-RET signaling, "
                "B2M-HFE complex assembly and evidence-bounded AREG-ERBB2 or ARTN-GFRalpha1 records at the stated "
                "molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse ANGPTL4 integrin heterodimers and glycoforms, ANPEP sLeX "
                "glycoprotein context, APP-LRP10 TGN sorting, ARTN preferred GFRalpha3 versus weak/selectivity-limited "
                "GFRalpha1 topology, B2M-HFE MHC-I-like assembly, or AREG-ERBB2 receptor-family context into a single "
                "canonical receptor. Preserve ligand processing, glycan, heterodimer, co-receptor and intracellular "
                "complex resolution, species and assay limits, and the distinction between binding, receptor-proximal "
                "signaling and functional output; frozen AREG-ERBB2 and ARTN-GFRalpha1 records remain evidence-bounded "
                "where no stable primary locator is present, and the existing edges do not assert a universal "
                "intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_133":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported BMP10 type-II and ALK1 binding/complex evidence, BMP15-BMPR1B/BMPR2 "
                "receptor-complex evidence, BMP2 type-I/type-II receptor assembly, and BMP3-ACVR2A binding at the "
                "stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse BMP ligand dimers, type-I versus type-II receptor roles, "
                "BMP10 ACVR2A/ACVR2B/BMPR2 promiscuity, BMP15 BMPR1B/BMPR2 complex context, or BMP2 receptor "
                "oligomerization into autonomous binary receptors. Preserve ligand form, receptor-complex topology, "
                "species and assay limits, weak-affinity BMP3-ACVR2A behavior, and the distinction between binding, "
                "receptor-proximal signaling and functional output; the existing edges do not assert a universal "
                "intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_134":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported BMP4 type-I receptor binding, BMP6 ACVR1/BMPR1A/BMPR1B receptor "
                "profiles, and BMP7 ACVR1/ACVR2A/ACVR2B/BMPR1A/BMPR1B receptor-complex binding and transcriptional "
                "response observations at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse BMP type-I versus type-II receptor roles, ligand-enhanced "
                "oligomerization, BMP6 weak-versus-strong receptor preferences, or BMP7 receptor cooperation into "
                "autonomous binary receptors. Preserve BMP dimer, receptor-complex and co-receptor topology, species "
                "and assay limits, and the distinction between binding, receptor-proximal signaling and functional "
                "output; the existing edges do not assert a universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_135":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported betacellulin-ERBB2/ERBB3 complex signaling, processed iC3b recognition by "
                "Mac-1 and CR4, C3d/iC3b-NRP1 binding, C4BP-CD40 activation, C4BP-LRP1 clearance, CADM1-CADM3 "
                "adhesion, CALCB-CALCRL/RAMP1 signaling and inhibitory CCL26/CCR2 or CCL7/CCR5 receptor modulation "
                "at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse ERBB2/ERBB3 cooperative receptor topology, processed C3 "
                "fragments versus free C3, Mac-1/CR4 integrin heterodimers, C4BP alpha-chain/heparin context, "
                "CADM IgSF adhesion, CALCRL:RAMP1 complex identity, or antagonist/non-signaling chemokine-receptor "
                "behavior into autonomous canonical receptors. Preserve ligand processing, oligomer, glycoform, "
                "heterodimer and complex resolution, species and assay limits, and the distinction between binding, "
                "receptor-proximal signaling and functional output; the existing edges do not assert a universal "
                "intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_136":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported CCN1/CYR61 adhesion through alphaIIbbeta3, alpha6beta1, alphaDbeta2, "
                "alphaMbeta2, alphaVbeta3 or alphaVbeta5 integrin contexts, plus direct CCN1-TLR2 inflammatory "
                "activation at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse CCN1 motif, RGD/V2 domain, activation-state, platelet, "
                "monocyte, HSPG or integrin-heterodimer contexts into a single canonical receptor. Preserve the "
                "ligand-domain, peptide, matrix and receptor-complex resolution, species and assay limits, and the "
                "distinction between binding, receptor-proximal signaling and functional output; CCN1-TLR2 and the "
                "integrin branches have distinct site and pathway semantics, and the existing edges do not assert a "
                "universal intracellular cascade or terminal TF route."
            )
        elif row.get("review_batch") == "batch_137":
            disposition = "already_present_exact_or_alias"
            layer_values = []
            species_values = []
            for edge_id in filter(None, matched_ids.split(";")):
                for source in sources_by_edge.get(edge_id, []):
                    if source.get("evidence_layer", "").strip():
                        layer_values.extend(filter(None, source["evidence_layer"].split(";")))
                    if source.get("species_support", "").strip():
                        species_values.extend(filter(None, source["species_support"].split(";")))
            layer = ";".join(dict.fromkeys(layer_values)) or "ligand_receptor_binding_or_activation"
            species = "; ".join(dict.fromkeys(species_values))
            summary = (
                f"The public {ligand}-{receptor} row is already represented by graph edge(s) {matched_ids}. "
                "The public locators are pathway or database records, while the existing graph edge-source records "
                "provide primary-supported CCN1-TLR4 activation, CCN2 alpha5beta1/Mac-1 adhesion, LRP1 transport, "
                "TrkA-p75NTR signaling, CCN3-NOTCH1 association and Notch outputs, contextual CCN4-alpha5beta1 "
                "interaction, and LPS-bound CD14 transfer to TLR4-MD2 at the stated molecular resolution."
            )
            limitations = (
                "Do not add a duplicate edge or collapse CCN1 TLR4 versus TLR2 site semantics, CCN2 integrin "
                "heterodimers and HSPG co-receptors, CCN2-LRP1 internalization versus direct binding, CTGF TrkA-"
                "p75NTR complexes, CCN3 Notch1 extracellular mapping, CCN4 assembled alpha5beta1 context, or "
                "LPS-bound CD14 transient transfer into autonomous canonical receptors. Preserve ligand domain, matrix, "
                "co-receptor and receptor-complex resolution, species and assay limits, and the distinction between "
                "binding, receptor-proximal signaling and functional output; the existing edges do not assert a "
                "universal intracellular cascade or terminal TF route."
            )
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
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMCID:PMC5743933"]
            species = "mouse neuronal ICAM5 and microglial adhesion studies"
            summary = "Primary ICAM5 studies support beta-integrin-associated microglial adhesion and phagocytosis contexts, but do not establish CD209A as a direct ICAM5 receptor."
            limitations = "Preserve neuronal ICAM5 and beta-integrin cell-adhesion context; do not transfer ICAM-family or adhesion-network membership into a direct ICAM5-CD209A edge without pair-specific binding or perturbation."
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
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:12070135", "DOI:10.1074/jbc.C200331200"]
            species = "human"
            summary = "Primary JAM2 adhesion work supports engagement of the alpha4beta1 integrin complex, not the alpha3beta1 composite receptor in this public row; the candidate is retained as integrin-family context."
            limitations = "Preserve the exact JAM2-alpha4beta1/JAM3 topology and leukocyte-adhesion context; do not promote JAM2-alpha3beta1 without a pair-specific assay."
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
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:8557754", "PMID:12077189"]
            species = "human; mouse comparator"
            summary = "Primary L1CAM adhesion studies support integrin-dependent migration and identify L1CAM as a ligand for VLA-5/alpha5beta1, but do not verify the alpha4beta7 composite receptor in this public row."
            limitations = "Retain L1CAM-integrin crosstalk and the exact alpha5beta1/VLA-5 context; do not promote L1CAM-alpha4beta7 without a pair-specific assay."
        elif ligand == "L1CAM" and receptor == "ALCAM":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMCID:PMC6703882"]
            species = "mouse primary midbrain neuron cultures"
            summary = "Primary neuronal adhesion experiments support a trans-heterophilic L1cam-ALCAM relationship and show that blocking L1cam or Chl1 antibodies abolishes ALCAM-dependent neurite-growth responses."
            limitations = "Preserve the trans-heterophilic cell-contact and neurite-growth assay context; do not infer a soluble ligand route, a universal intracellular relay or a terminal-TF output from this adhesion experiment."
        elif ligand == "L1CAM" and receptor == "EPHB2":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMCID:PMC4351967"]
            species = "mouse retinocollicular mapping model"
            summary = "Primary EphB studies show EphB2-dependent phosphorylation of L1 during axon mapping, supporting receptor-proximal crosstalk with L1 rather than a direct extracellular L1CAM-to-EPHB2 ligand-receptor interaction."
            limitations = "Retain EphB-L1 phosphorylation as downstream adhesion/receptor crosstalk; do not materialize L1CAM-EPHB2 as a direct binding edge or infer a complete L1CAM signaling cascade."
        elif ligand == "L1CAM" and receptor == "PTPRZ1":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
            primary = ["PMID:7528221", "PMCID:PMC2120309"]
            species = "rat neural cell and biochemical binding assays"
            summary = "Primary phosphacan/PTPRZ1 studies report binding to neural cell-adhesion molecules including Ng-CAM/L1, but the demonstrated orientation is PTPRZ1/phosphacan toward L1-family substrates and does not establish L1CAM as a canonical ligand for PTPRZ1."
            limitations = "Retain the neural adhesion and reverse-orientation binding context; do not materialize L1CAM-PTPRZ1 without an exact orientation-matched receptor assay or infer intracellular signaling from the binding study."
        elif ligand == "L1CAM" and receptor == "CHL1":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMCID:PMC6703882"]
            species = "mouse primary midbrain neuron cultures"
            summary = "Primary neuronal experiments place L1cam and Chl1 in an ALCAM-dependent trans-heterophilic adhesion and neurite-growth context, but do not directly establish L1CAM as a ligand for CHL1."
            limitations = "Retain L1-family and ALCAM-mediated cell-contact context; require pair-specific L1CAM-CHL1 binding or perturbation before promotion and do not infer a soluble signaling route."
        elif ligand == "L1CAM" and receptor == "NCAM1":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:7528221", "PMCID:PMC2120309"]
            species = "rat neural cell and biochemical binding assays"
            summary = "Primary neural adhesion studies report related Ng-CAM/L1 and NCAM interactions with phosphacan/PTPRZ1, supporting neural cell-adhesion network context but not a direct L1CAM-to-NCAM1 receptor pair in the candidate orientation."
            limitations = "Retain the neural adhesion-family context and exact phosphacan/PTPRZ1 binding relationships; require pair-specific L1CAM-NCAM1 evidence before promotion and do not infer a receptor relay or terminal-TF output."
        elif ligand == "L1CAM":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            primary = ["PMID:9396761", "PMID:22815787", "PMID:12925712"]
            species = "human and rat L1CAM adhesion, integrin and receptor-crosstalk assays"
            summary = "Primary studies establish L1CAM heterophilic adhesion through selected integrins, ErbB-family receptor crosstalk and cytoskeletal anchoring, but no exact primary experiment was verified for this remaining L1CAM-to-listed-protein candidate."
            limitations = "Retain L1CAM adhesion, selected integrin and ErbB/cytoskeletal context; do not transfer those results to CD9, EZR, FGFR2, ITGA4, ITGB7, LVRN or PLXNA1 without pair-specific evidence."
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
        elif ligand == "CD200" and receptor == "CD200R3":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:12960329", "PMID:17982101", "PMID:26315370"]
            species = "mouse"
            summary = "Primary CD200-receptor-family work distinguishes the canonical CD200-CD200R interaction from CD200R-related activating receptors, while CD200Fc studies report CD200R3 expression and microglial outputs without establishing direct CD200 binding to CD200R3."
            limitations = "Retain CD200-CD200R1 as the canonical ligand-receptor edge; keep CD200R3 as a receptor-family and functional-context hold until an exact CD200-CD200R3 binding or receptor-dependent ligand assay is identified."
        elif ligand == "CEACAM2" and receptor == "SELE":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:1378450"]
            species = "human"
            summary = "Primary neutrophil-endothelial adhesion work supports CEA-like CD66/NCA molecules as sialyl-Lewis-x presenters participating in E-selectin-dependent adhesion, but does not resolve CEACAM2 as the exact ligand molecule."
            limitations = "Retain as CEACAM-family/selectin adhesion context; do not materialize a CEACAM2-SELE binary edge without paralog-specific binding or perturbation evidence."
        elif ligand == "C4A":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
            primary = ["PMID:14734749", "PMID:8422437", "PMCID:PMC2947992"]
            species = "human complement and CD46/CR1 studies"
            summary = "Primary complement studies support processed C4b interactions with complement regulators and cofactors, but the public rows label the ligand as C4A and mix complement, anaphylatoxin and neuropilin receptors without resolving the mature fragment or exact receptor mechanism."
            limitations = "Retain as complement-fragment and receptor-context evidence pending a direct C4A/C4b-form assay for each target; do not split intact C4A from deposited C4b or infer C3AR1, C5AR2 or NRP1 specificity from complement-family context alone."
        elif ligand == "CXCL2" and receptor == "ACKR1":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:30446388", "PMCID:PMC6303217"]
            species = "mouse in vivo cremaster-microcirculation model"
            summary = "Primary intravital and endothelial-junction studies show that neutrophil-derived CXCL2 is retained and presented by ACKR1 at venular junctions, and that this ACKR1-dependent CXCL2 depot guides paracellular neutrophil transmigration."
            limitations = "Represent ACKR1 as an atypical chemokine presentation/retention route rather than a canonical G-protein signaling receptor; preserve the mouse endothelial-junction and CXCR2-ligand context and do not infer a universal intracellular relay or terminal-TF output."
        elif ligand == "CXCL2" and receptor == "CXCR1":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMCID:PMC3748335"]
            species = "human primary airway smooth-muscle cells"
            summary = "Primary receptor-blockade and knockdown experiments found CXCL2-induced migration to depend on CXCR2 rather than CXCR1; the study notes only weak or high-concentration CXCR1 activity in recombinant receptor comparisons."
            limitations = "Preserve the CXCL2-CXCR2 route and the low-affinity/recombinant-system caveat; do not materialize CXCL2-CXCR1 as a direct functional edge without a pair-specific primary assay."
        elif ligand == "CXCL2":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:30446388", "PMCID:PMC3748335"]
            species = "mouse and human receptor-specificity studies"
            summary = "Primary CXCL2 studies support CXCR2 signaling and ACKR1-mediated endothelial presentation, but do not support the listed ADRA2A, GRM7 or MTNR1A pairings as direct CXCL2 receptors."
            limitations = "Retain CXCL2-CXCR2 and the ACKR1 presentation route with their species and cell-context boundaries; do not transfer chemokine activity to unrelated GPCR families from public database co-membership."
        elif ligand == "PF4" and receptor == "CXCR3":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:18174362", "PMID:24469069", "PMID:15265941"]
            species = "human CXCR3 isoform and lymphocyte/endothelial studies; mouse PF4 comparator"
            summary = "Primary studies support context-dependent PF4/CXCL4 activity through CXCR3 isoforms in human activated T cells and endothelial systems, while other primary work finds no CXCR3B requirement in monocyte oxidative-burst responses."
            limitations = "Keep this as an isoform-, cell-type- and species-bounded contextual route; the normalized CXCR3 gene label does not resolve CXCR3A versus CXCR3B, and mouse systems lack the human CXCR3B splice context."
        elif ligand == "PF4" and receptor == "SDC2":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:36640356", "PMCID:PMC11064100"]
            species = "human and mouse extracellular-matrix/proteoglycan studies"
            summary = "Primary biophysical and in vivo work shows PF4/CXCL4 binding to glycosaminoglycans on endothelial proteoglycans and altering leukocyte adhesion and recruitment, but it does not establish syndecan-2 as a standalone PF4 signaling receptor."
            limitations = "Retain SDC2 as a possible proteoglycan presentation context rather than a direct binary receptor edge; require syndecan-2-specific binding or perturbation before promotion and do not infer canonical intracellular signaling."
        elif ligand == "PF4":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:29930254", "PMID:29540475", "PMID:36640356"]
            species = "human PF4 receptor and proteoglycan studies"
            summary = "Primary PF4 studies support CCR1, Mac-1/integrin and extracellular proteoglycan/GAG contexts, but do not establish the listed non-cognate receptor pair as a direct PF4 edge."
            limitations = "Retain PF4 receptor and matrix-context evidence in its cell, species and receptor-complex boundaries; do not materialize unsupported FGFR2, LDLR, PROCR, ACKR1, ADRA2A, GRM7, LRP1 or MTNR1A rows from pathway co-membership alone."
        elif ligand == "ADM2":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:26423127", "PMID:40817416", "PMID:27784654"]
            species = "rat and mouse CALCRL/RAMP receptor-complex studies"
            summary = "Primary ADM2/intermedin studies place the peptide in CALCRL receptor complexes whose ligand behavior is specified by RAMP1-3, including RAMP3-dependent tissue responses; the listed ADCYAP1R1, ADRB, CALCR, GPR, PTH1R, TSHR and VIPR rows are not direct ADM2 receptor pairings."
            limitations = "Preserve the mature ADM2-CALCRL/RAMP complex and species boundaries; do not treat CALCR or an individual RAMP as a standalone ADM2 receptor or transfer calcitonin-family activity to unrelated GPCRs."
        elif ligand == "GDF11" and receptor in {"ACVR1B+ACVR2B", "ACVR2A+TGFBR1"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMCID:PMC1525155", "PMID:35643319", "PMCID:PMC9234707"]
            species = "mouse developmental assays; human structural/receptor-binding assays"
            summary = "Primary studies support GDF11 binding to type-II activin receptors and recruitment of type-I receptors in receptor complexes, including Acvr2b-dependent type-I receptor engagement and high-affinity GDF11 recognition by ACVR2A; the public composite rows do not resolve one universal ACVR2A/B plus type-I topology."
            limitations = "Retain the complete type-II/type-I receptor complex and preserve the developmental, structural and species boundaries; do not split composite rows into standalone ACVR1B, TGFBR1 or ACVR2A edges or infer a universal SMAD route from complex membership alone."
        elif ligand == "GDF11" and receptor in {"BMPR1A", "BMPR1B"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
            primary = ["PMCID:PMC1525155"]
            species = "mouse receptor-complex assays"
            summary = "Primary GDF11 receptor-complex experiments found no direct type-I receptor binding in isolation but detected type-I receptor association when Acvr2b was coexpressed, leaving BMPR1A/B as complex-dependent context rather than standalone GDF11 receptors."
            limitations = "Require the complete GDF11 type-II/type-I receptor complex and exact receptor-combination assay; do not materialize BMPR1A or BMPR1B as standalone ligand receptors."
        elif ligand == "GDF11" and receptor == "BMPR2":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:35643319", "PMCID:PMC9234707"]
            species = "human structural and receptor-binding assays"
            summary = "Primary comparative receptor-binding work places GDF11 among high-affinity ACVR2A ligands rather than the high-affinity BMPR2 ligand group, and the reviewed structural study does not establish the public GDF11-BMPR2 row as a direct edge."
            limitations = "Retain GDF11-ACVR2A/ACVR2B complex evidence with its type-I receptor context; do not transfer TGF-beta-family receptor overlap into a direct GDF11-BMPR2 edge without an exact primary assay."
        elif ligand == "INSL5" and receptor in {"RXFP1", "RXFP2"}:
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:15525639", "PMID:18582868"]
            species = "human recombinant peptide and receptor-expression assays"
            summary = "Primary receptor-expression and functional studies identify RXFP4/GPCR142 as the high-affinity INSL5 agonist receptor and report no RXFP1/LGR7 activation, while RXFP2 is not established as an INSL5 receptor in the reviewed assays."
            limitations = "Preserve the mature INSL5-RXFP4 route and the weak RXFP3 antagonism boundary; do not transfer relaxin-family receptor specificity to RXFP1 or RXFP2."
        elif ligand == "INSL5":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:15525639", "PMID:18582868"]
            species = "human recombinant peptide and receptor-expression assays"
            summary = "Primary INSL5 pharmacology supports selective RXFP4/GPCR142 agonism, with only weak antagonism at RXFP3 and no support for the listed adrenergic, glutamate or melatonin receptors."
            limitations = "Retain the cognate INSL5-RXFP4 route and its receptor-expression context; do not infer direct INSL5 binding to unrelated GPCRs from public database co-membership."
        elif ligand == "CCL8" and receptor == "CCR8":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:21217759", "PMCID:PMC3863381"]
            species = "mouse CCL8 and CCR8-dependent Th2-cell migration"
            summary = "Primary mouse chemokine and migration studies identify CCL8 as a CCR8 agonist and show that CCR8 is required for CCL8-induced Th2-cell migration in atopic-skin models."
            limitations = "Preserve the mouse CCL8/CCR8 orthology and Th2-cell context; do not transfer this result to human CCL8 receptor promiscuity or infer a universal intracellular relay or terminal-TF output."
        elif ligand == "CCL8" and receptor in {"ACKR1", "ACKR2"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
            primary = ["PMID:21217759", "PMCID:PMC3863381"]
            species = "mouse CCL8/CCR8 study; atypical-receptor context unresolved"
            summary = "Primary mouse work establishes a CCL8-CCR8 functional route, while the public ACKR1/ACKR2 rows remain possible chemokine retention or scavenging contexts rather than directly assayed signaling receptors in that study."
            limitations = "Retain as an atypical-receptor context hold pending direct CCL8-ACKR1/ACKR2 binding or trafficking data; preserve mouse versus human chemokine-receptor boundaries and do not infer canonical G-protein signaling."
        elif ligand == "CCL8":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:21217759", "PMCID:PMC3863381"]
            species = "mouse CCL8 receptor-specificity study"
            summary = "Primary mouse studies support CCL8 activity through CCR8 and report no CCR2 agonism under the tested conditions; the remaining public receptor rows are not established as direct CCL8 receptor edges."
            limitations = "Retain mouse CCL8-CCR8 and the separate atypical-receptor hold; do not transfer receptor promiscuity from human MCP-family chemokines to mouse CCL8 without an exact assay."
        elif ligand == "EFNA4" and receptor in {"EPHA1", "EPHA3", "EPHA5", "EPHA6"}:
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation"
            primary = ["PMCID:PMC3499309", "PMCID:PMC6782661"]
            species = "mouse and human EphA receptor binding assays"
            summary = "Primary Eph receptor profiling and native-neural-tissue binding assays support ephrin-A4 interaction with the listed EphA receptor family members, with receptor- and tissue-dependent affinity differences."
            limitations = "Represent EFNA4 as a membrane-tethered ephrin-A ligand and preserve receptor affinity, glycosylation, cell-contact and species boundaries; this batch asserts binding evidence only, not reverse signaling or a terminal-TF output."
        elif ligand == "EFNA4" and receptor == "EPHA7":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMCID:PMC6782661"]
            species = "mouse native-striatal receptor binding assay"
            summary = "Native striatal ligand-binding assays detected ephrin-A4 binding to EphA4 but not EphA7, despite broader Eph-family promiscuity in recombinant systems."
            limitations = "Retain the tissue- and assay-specific EphA4 context; do not materialize EFNA4-EPHA7 from EphA-family membership alone without a direct pair-specific assay."
        elif ligand == "EFNA5" and receptor in {"EPHA1", "EPHA5", "EPHA6"}:
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation"
            primary = ["PMCID:PMC3499309", "PMCID:PMC6782661"]
            species = "mouse and human EphA receptor binding assays"
            summary = "Primary Eph receptor profiling supports ephrin-A5 binding across the listed EphA receptor contexts, with affinity and native-tissue selectivity varying by receptor and cellular system."
            limitations = "Represent EFNA5 as a membrane-tethered ephrin-A ligand and preserve receptor affinity, cell-contact and species boundaries; this batch asserts binding evidence only and does not infer reverse signaling or a terminal-TF output."
        elif ligand == "EFNA5" and receptor in {"EPHB1", "EPHB6"}:
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMCID:PMC3499309", "PMCID:PMC6782661"]
            species = "mouse and human Eph receptor family binding assays"
            summary = "Primary Eph-family profiling supports EFNA5 interactions with EphA receptors and the recognized cross-subfamily EphB2 exception, but does not establish the listed EphB1 or EphB6 rows as direct EFNA5 edges."
            limitations = "Preserve the EphA family and the separately documented EphB2 cross-interaction boundary; do not transfer EFNA5 activity to EphB1/EphB6 from Eph-family membership alone."
        elif ligand == "ADM" and receptor == "RAMP1":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
            primary = ["PMCID:PMC8222276", "PMID:26423127"]
            species = "human primary cardiovascular cells; rat vascular smooth-muscle cells"
            summary = "Primary ADM pharmacology shows that RAMP proteins determine CALCRL ligand specificity and trafficking, with ADM preferentially acting through CALCRL/RAMP2-3 contexts; RAMP1 alone is an accessory component rather than a standalone ADM receptor."
            limitations = "Retain the complete CALCRL/RAMP receptor complex and ligand-bias context; do not materialize ADM-RAMP1 as a binary receptor edge or infer RAMP1-specific downstream signaling without CALCRL."
        elif ligand == "ADM" and receptor == "GPR182":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMCID:PMC8092405", "PMCID:PMC10157204"]
            species = "mouse GPR182 deorphanization studies"
            summary = "Primary GPR182 studies report that the earlier adrenomedullin-receptor assignment could not be confirmed and instead characterize GPR182/ACKR5 as an atypical chemokine-scavenging receptor."
            limitations = "Do not materialize ADM-GPR182 from the historical ADMR name; retain GPR182 in the atypical chemokine receptor layer and require a direct mature-ADM assay before reconsideration."
        elif ligand == "ADM" and receptor in {"MRGPRB1", "MRGPRX2"}:
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:15823563"]
            species = "human MRGPRX2/PAMP receptor assay"
            summary = "Primary MRGPRX2 work identifies proadrenomedullin N-terminal peptides PAMP-12/PAMP-20, not mature adrenomedullin, as MRGPRX2 agonists; the public mature-ADM-to-MRGPR rows therefore do not define the same ligand form."
            limitations = "Preserve proadrenomedullin peptide processing and MRGPRX2/MrgprB paralog boundaries; do not transfer PAMP activity to mature ADM or infer mouse MrgprB1 specificity without an exact mature-peptide assay."
        elif ligand == "ADM" and receptor == "CALCR":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMCID:PMC8222276", "PMID:26423127"]
            species = "human and rat CALCRL/RAMP receptor-complex studies"
            summary = "Primary ADM studies define the functional adrenomedullin receptor as CALCRL in association with RAMP2 or RAMP3, not standalone CALCR; the public ADM-CALCR row does not specify a validated receptor complex."
            limitations = "Require the complete CALCRL/RAMP2-3 complex and mature ADM assay before promotion; do not transfer amylin/CALCR receptor-family pharmacology to ADM."
        elif ligand == "GDF9" and receptor in {"ACVR1B+BMPR2", "ACVR2A", "BMPR1A", "BMPR1B"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:12135884", "PMCID:PMC2875809"]
            species = "rat granulosa-cell and mouse ovarian receptor-context studies"
            summary = "Primary GDF9 studies identify BMPR2 as a direct binding and functional receptor context and report partial activity through BMPR1A, BMPR1B and ACVR2A ectodomains, indicating a type-II/type-I receptor complex rather than an interchangeable standalone receptor set."
            limitations = "Retain GDF9 with the complete BMPR2/type-I receptor complex and ovarian cell context; do not promote free ACVR2A, BMPR1A or BMPR1B rows as universal receptors or infer a terminal-TF output from receptor-family membership."
        elif ligand == "GDF9":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:12135884"]
            species = "rat GDF9 receptor assays"
            summary = "Primary GDF9 receptor studies support BMPR2 and associated type-I receptor complexes, but do not establish FXYD6 or ORAI2 as direct GDF9 receptor proteins."
            limitations = "Represent FXYD6/ORAI2 only as possible downstream or membrane-excitability context when independently supported; do not materialize them as GDF9 ligand receptors."
        elif ligand == "SLURP1" and receptor in {"CHRNA9", "CHRNA10"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
            primary = ["PMID:29192197", "PMCID:PMC5709491"]
            species = "human and rat nicotinic-receptor assays"
            summary = "Primary SLURP1 electrophysiology and binding studies support activity in selected nicotinic receptor contexts, including α9/α10-related complexes, but the public rows isolate individual subunits rather than asserting the complete pentameric receptor."
            limitations = "Retain the assembled nicotinic receptor topology and assay-specific subunit context; do not treat CHRNA9 or CHRNA10 alone as a standalone SLURP1 receptor or infer a universal intracellular route."
        elif ligand == "SLURP1":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMCID:PMC5837762", "PMID:29192197"]
            species = "human and rat nicotinic-receptor assays"
            summary = "Primary SLURP1 studies support α7-nAChR and selected assembled nicotinic receptor contexts, while affinity testing did not support the listed α3, α4, β2 or β4 subunits as standalone SLURP1 receptors."
            limitations = "Preserve mature SLURP1 and complete nicotinic pentamer context; do not materialize free CHRNA3, CHRNA4, CHRNB2 or CHRNB4 rows from subunit expression or receptor-family membership alone."
        elif ligand == "ICAM5" and receptor == "ITGB2L":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMCID:PMC5743933"]
            species = "mouse neuronal ICAM5 and microglial beta-integrin studies"
            summary = "Primary microglial binding and immunoprecipitation studies show soluble neuronal ICAM5 association with beta-2 integrin-containing complexes and anti-adhesive/phagocytic outputs, but the candidate uses ITGB2L rather than the assayed ITGB2 subunit."
            limitations = "Retain as an integrin-complex/paralog boundary hold; require direct ICAM5-ITGB2L evidence before promotion and do not decompose beta-integrin complexes into a standalone receptor edge."
        elif ligand == "ICAM5":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMCID:PMC5743933"]
            species = "mouse neuronal ICAM5 and microglial adhesion studies"
            summary = "Primary ICAM5 studies support beta-integrin-associated microglial adhesion and phagocytosis contexts, but do not establish the listed CD209, IGDCC4 or PRTG proteins as direct ICAM5 receptors."
            limitations = "Preserve neuronal ICAM5 and beta-integrin cell-adhesion context; do not transfer ICAM-family or adhesion-network membership into direct ICAM5 receptor edges without pair-specific binding or perturbation."
        elif ligand == "EFNB2" and receptor in {"EPHA3", "EPHA6"}:
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMCID:PMC3499309", "PMCID:PMC2170431"]
            species = "mouse and human Eph/ephrin receptor profiling"
            summary = "Primary Eph/ephrin profiling supports ephrin-B2 binding to EphB receptors and the established EphA4 cross-subfamily context, but does not establish the listed EphA3 or EphA6 rows as direct EFNB2 interactions."
            limitations = "Preserve EFNB2-EphB and EFNB2-EphA4 cross-subfamily boundaries; do not transfer ephrin-A receptor promiscuity to EFNB2 or materialize EphA3/EphA6 without an exact assay."
        elif ligand == "EFNB2":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMCID:PMC3499309", "PMCID:PMC2170431"]
            species = "mouse and human Eph/ephrin receptor profiling"
            summary = "Primary Eph/ephrin studies define EFNB2 as a membrane-tethered ephrin-B ligand for Eph receptor contexts, not for the listed glutamate receptors, PECAM1 or RHBDL2 targets."
            limitations = "Represent EFNB2 in the Eph receptor/cell-contact layer; do not materialize unrelated receptor or membrane-protein rows from interaction-network co-occurrence."
        elif ligand in {"CCL1", "CCL8", "CEACAM2"}:
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
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = ["PMID:15649866", "PMID:22973049"]
            species = "human; rat comparator"
            summary = "Primary relaxin-family receptor pharmacology assigns INSL3 to RXFP2 and reports only low-affinity or engineered-chimera behavior at RXFP1-related constructs; the public INSL3-RXFP1 row is retained as a bounded family-context hold."
            limitations = "Do not materialize a canonical INSL3-RXFP1 edge; preserve the exact INSL3-RXFP2 route and distinguish native receptor assays from RXFP1/RXFP2 chimeras."
        elif ligand == "INSL3" and receptor != "RXFP2":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:15649866", "PMID:22973049", "PMID:15956688"]
            species = "human; rat comparator"
            summary = "Primary relaxin-family receptor studies identify RXFP2 as the cognate INSL3 receptor and distinguish RXFP1, RXFP3 and RXFP4 ligand specificity; the listed non-RXFP2 candidate is not supported as a canonical INSL3 receptor edge."
            limitations = "Retain the mature INSL3-RXFP2 route and any explicitly tested low-affinity/chimera behavior separately; do not infer INSL3 signaling through unrelated GPCRs, RAMPs or receptor paralogs."
        elif ligand == "HDC":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:22767596"]
            species = "human enzyme study"
            summary = "HDC is histidine decarboxylase, the enzyme that synthesizes histamine from histidine; histamine, not HDC, is the mature agonist assayed at HRH1-4 receptors."
            limitations = "Retain HDC as an extracellular-mediator biosynthesis node and histamine-HRH1/2/3/4 receptor evidence separately; do not materialize enzyme-to-receptor edges or infer HDC as a secreted ligand."
        elif ligand == "POMC":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:27837406", "PMID:33389463", "PMID:11070427"]
            species = "rat and mouse precursor-processing studies"
            summary = "POMC is a prohormone precursor processed into beta-endorphin and other peptides; opioid-receptor activity is attributed to the processed peptides, not to intact POMC as the direct ligand."
            limitations = "Retain mature beta-endorphin and other processed peptide-to-opioid-receptor relationships when explicitly assayed; do not materialize precursor-gene labels as direct OPRD1, OPRK1 or OPRM1 ligands."
        elif ligand == "AGT" and receptor == "AGTR2":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:12045255", "PMID:15534073"]
            species = "human and rat renin-angiotensin system studies"
            summary = "Angiotensinogen is processed by renin and downstream enzymes into angiotensin peptides; AT2/AGTR2 responds to angiotensin II or related mature peptides, not to intact angiotensinogen as the direct ligand."
            limitations = "Retain the angiotensinogen-to-angiotensin-peptide processing cascade and mature peptide-to-AGTR2 evidence separately; do not materialize AGT-to-AGTR2 as a direct binary edge."
        elif ligand == "AGT":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:12045255", "PMID:15534073"]
            species = "human and rat renin-angiotensin system studies"
            summary = "Angiotensinogen is a precursor processed into angiotensin peptides; the listed receptor rows do not establish intact AGT as the direct mature ligand."
            limitations = "Retain the angiotensinogen-to-angiotensin-peptide processing cascade and receptor-specific mature peptide evidence separately; do not materialize AGT-to-receptor rows from precursor or pathway membership."
        elif ligand == "LTA" and receptor == "TNFRSF14":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:15647361"]
            species = "human and mouse HVEM/LTalpha complex assays"
            summary = "Primary HVEM complex studies place lymphotoxin-alpha among the ligands that can engage TNFRSF14/HVEM, but the reported interaction is within a receptor-complex and ligand-form context rather than a fully resolved standalone LTalpha3-to-HVEM route."
            limitations = "Retain soluble LTalpha3, membrane LTalpha-beta complexes, LIGHT, BTLA and HVEM topology separately; require exact ligand form and pair-specific functional evidence before promoting this row as a standalone binary edge."
        elif ligand == "CXCL1" and receptor == "CXCR1":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:41256520"]
            species = "human receptor biosensor assays"
            summary = "Primary receptor-bias experiments directly compare endogenous CXCL1 at CXCR1 and CXCR2 and measure G-protein, arrestin, kinase-translocation and internalization outputs, supporting CXCL1-CXCR1 activation with partial agonist bias."
            limitations = "Preserve the endogenous human chemokine, receptor-bias and biosensor context; do not infer identical CXCL1 signaling at CXCR1 and CXCR2 or a complete terminal-TF route from the proximal assays."
        elif ligand == "CXCL5" and receptor == "CXCR1":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:33688078"]
            species = "human chemokine, receptor-signaling and primary monocyte/neutrophil assays"
            summary = "Primary studies show that CXCL5 has weak agonist activity at CXCR1 and that N-terminal processing changes CXCR1 calcium and G-protein signaling, with CXCR1/CXCR2-dependent chemotaxis in primary myeloid-cell models."
            limitations = "Preserve mature CXCL5 form, N-terminal processing and weak-CXCR1 versus stronger-CXCR2 activity distinctions; do not infer equivalent receptor potency or a universal downstream/TF route."
        elif ligand == "CD200" and receptor == "CD200R4":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
            primary = ["PMID:12960329", "PMID:15187158"]
            species = "mouse CD200R-family binding studies"
            summary = "Primary CD200R-family studies report CD200 binding across alternate mouse receptor members, including CD200R4-related nomenclature, but later family analyses describe very low or disputed binding to activating CD200RL paralogs."
            limitations = "Retain CD200/CD200R-family evidence with exact mouse paralog and affinity context; do not promote CD200R4 as an unqualified physiological receptor or infer canonical inhibitory signaling from family-level binding alone."
        elif ligand == "PTN" and receptor == "SDC2":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:39285301"]
            species = "human spermatogonial stem-cell assays"
            summary = "Primary human spermatogonial-stem-cell work identifies PTN-SDC2 communication, confirms PTN-SDC2 interaction by immunoprecipitation and colocalization, and shows SDC2-dependent proliferation and GFRA1 output that is rescued by exogenous PTN."
            limitations = "Preserve the human spermatogonial-cell and PTN/SDC2 functional context; do not generalize the edge to every tissue or infer a complete intracellular cascade or terminal-TF route from the reported outputs."
        elif ligand == "ANGPTL2" and receptor == "TLR4":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:22868908", "PMID:26435501"]
            species = "mouse inflammatory-cell and retinal models"
            summary = "Primary studies show ANGPTL2-dependent inflammatory outputs and identify alpha5beta1 integrin as a receptor in an endotoxin model, but they do not establish direct ANGPTL2 binding to TLR4; TLR4 is part of the LPS stimulus context."
            limitations = "Retain ANGPTL2 inflammatory-output and alpha5beta1-integrin context; do not materialize a direct ANGPTL2-TLR4 edge or transfer LPS/TLR4 pathway dependence into receptor-binding evidence."
        elif ligand in {"ANGPTL1", "ANGPTL7"} and receptor == "PIRB":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:22660330", "PMCID:PMC3367397"]
            species = "human LILRB2-positive cord-blood cells; mouse PIRB/HSC context"
            summary = "Primary ANGPTL-receptor work reports ANGPTL1 and ANGPTL7 binding in the human LILRB2-positive hematopoietic-cell context and places ANGPTL-family/PIRB signaling in mouse HSC and leukemia models, but the individual mouse ANGPTL1- or ANGPTL7-to-PIRB binary rows are not resolved as equally direct assays."
            limitations = "Preserve LILRB2/PIRB orthology, ANGPTL member, species, tag and hematopoietic-cell boundaries; do not treat family-level human LILRB2 binding as a fully resolved mouse PIRB edge or infer a universal downstream cascade for either ANGPTL."
        elif ligand == "ANGPTL4" and receptor in {"SDC1", "SDC2", "SDC3"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:29017031", "DOI:10.1016/j.devcel.2017.09.011"]
            species = "human cell/recombinant and Xenopus developmental assays"
            summary = "Primary studies show that secreted ANGPTL4 binds syndecans and participates in a ternary ANGPTL4-syndecan-LRP6 complex that is internalized and attenuates Wnt/beta-catenin signaling; the evidence supports syndecan-family receptor-proximal context but does not establish each isolated SDC1, SDC2 or SDC3 row as a complete receptor."
            limitations = "Preserve the syndecan subtype, LRP6 co-receptor, Wnt-complex and assay context; do not decompose the ternary complex into an isolated ANGPTL4-syndecan signaling edge or infer a terminal TF route from Wnt attenuation alone."
        elif ligand == "C4B" and receptor == "CR2":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:2473114", "PMID:12367531"]
            species = "human and mouse complement-receptor assays"
            summary = "Primary CR2 assays support recognition of C3d/iC3b fragments and show no C4b binding, while structural work states that C4d is not a CR2 ligand; the public C4B-to-CR2 row conflates complement components or fragments."
            limitations = "Retain C3d/iC3b-to-CR2 and C4b-to-CR1 complement relationships separately; do not materialize intact C4B or C4d as a direct CR2 ligand."
        elif ligand == "CADM3" and receptor == "CADM1":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:18003830"]
            species = "rat forebrain and transfected cell adhesion assays"
            summary = "Primary SynCAM work detects a weaker CADM3-CADM1 interaction by affinity chromatography but does not show strong CADM1/CADM3 cell adhesion; the row is retained as bounded adhesion-family context rather than a canonical signaling edge."
            limitations = "Preserve the stronger SynCAM1/2 and SynCAM3/4 adhesion pairs and the reported weak CADM1-CADM3 interaction separately; do not infer a secreted-ligand route, intracellular cascade or terminal-TF output."
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
        elif ligand == "APOB" and receptor == "LRP2":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:10330424", "PMCID:PMC408451"]
            species = "human apoB-containing particles; rabbit and human renal megalin assays"
            summary = "Primary ligand-blot, solid-phase binding and cell-uptake experiments show that apoB-containing particles and apoB-100 fragments bind megalin/LRP2 and that megalin mediates renal uptake of the tested apoB truncation."
            limitations = "Preserve the apoB-100/apoB-truncation, lipoprotein-particle and renal endocytic context; do not generalize the edge to every APOB isoform or infer a canonical transcriptional signaling cascade from uptake."
        elif ligand == "APOB" and receptor == "OLR1":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:9588202", "PMID:18346743", "PMID:18845619"]
            species = "mouse and human oxidized-LDL/LOX-1 studies"
            summary = "Primary studies establish OLR1/LOX-1 recognition of oxidized LDL and measure LOX-1 ligands containing apoB, but the receptor recognizes a modified lipoprotein particle rather than unmodified APOB as an isolated mature ligand."
            limitations = "Retain the oxidized/modified LDL, apoB-particle and endothelial/macrophage scavenger-receptor context; do not materialize unmodified APOB-to-OLR1 as a generic binary edge or infer a route independent of lipoprotein modification state."
        elif ligand == "APOB" and receptor == "VLDLR":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:12870663", "PMID:3670075"]
            species = "human and rat lipoprotein-receptor studies"
            summary = "Primary receptor-specificity studies report that VLDLR binds apoE-containing remnant lipoproteins but not apoB as the direct recognition ligand; the candidate therefore conflates particle composition with receptor ligand specificity."
            limitations = "Retain apoE/VLDLR and apoB/LDLR or megalin relationships separately; do not materialize APOB-VLDLR without an apoB-specific binding assay that resolves the lipoprotein particle and cofactor context."
        elif ligand == "APOB" and receptor in {"TLR4", "TLR6"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:24792928"]
            species = "primary human monocytes and THP-1 macrophage assays"
            summary = "Primary studies show that oxidized LDL or apoB-containing modified lipoprotein preparations induce TLR4/TLR6-dependent PKCdelta-IRAK1-JNK/AP-1 and IL-1beta responses, but do not establish unmodified APOB as the direct TLR4 or TLR6 ligand."
            limitations = "Retain oxidation-specific lipoprotein, TLR4/TLR6 and inflammatory-output context; do not materialize a generic APOB-TLR4/TLR6 edge or infer signaling independent of particle modification and co-receptor composition."
        elif ligand == "APOB":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            primary = ["PMID:24792928", "PMID:19116273"]
            species = "human and mammalian lipoprotein/receptor assays"
            summary = "The current review found primary evidence for apoB-containing particle uptake or oxidation-specific inflammatory signaling, but not an exact mature APOB-to-listed-receptor experiment for this candidate."
            limitations = "Retain apoB-particle, modification-state and receptor-family context; do not transfer evidence for APC, apoE, oxidized LDL or other lipoprotein forms to unmodified APOB without pair-specific testing."
        elif ligand.startswith("GM"):
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_review_locator"
            summary = "The GM-prefixed public identifier was not resolved to a verified mature ligand identity and exact receptor assay in this pass."
            limitations = "Resolve the species-specific identifier and protein form before promotion; do not infer receptor specificity from an unresolved GM label or public-database membership alone."
        elif ligand == "COL4A1" and receptor == "ITGA3+ITGB1":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:19229828"]
            species = "human renal epithelial-cell assays"
            summary = "Primary affinity-chromatography and solid-phase assays show that the alpha1 NC1 domain of type IV collagen binds renal epithelial cells through alpha3beta1 integrin, with an associated matrix-response readout."
            limitations = "Preserve the collagen-IV alpha1 NC1 domain, renal epithelial-cell and integrin-complex context; do not generalize from a collagen-chain NC1 fragment to every mature collagen-IV isoform or infer a universal intracellular/TF route."
        elif ligand == "COL4A3" and receptor == "ITGA2+ITGB1":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:19229828"]
            species = "human glomerular epithelial-cell assays"
            summary = "Primary affinity-chromatography and solid-phase assays show preferential binding of the alpha3 NC1 domain of type IV collagen through alpha2beta1 integrin in human glomerular epithelial cells, with modulation of MMP-2 and MMP-9 expression."
            limitations = "Preserve the collagen-IV alpha3 NC1 domain, glomerular epithelial-cell and alpha2beta1 context; do not generalize to intact alpha3alpha4alpha5 collagen IV without chain-assembly evidence or infer a complete signaling cascade from the MMP readout."
        elif ligand == "COL4A3" and receptor == "ITGA1+ITGB1":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:19229828", "PMID:8344274"]
            species = "human collagen-IV and renal-cell assays"
            summary = "Primary studies establish alpha1beta1 binding to collagen-IV regions and distinguish alpha3-chain NC1 interactions through other integrins, but they do not verify alpha1beta1 as the direct receptor for the isolated alpha3 NC1 candidate."
            limitations = "Retain collagen-IV integrin-family and chain-composition context; require an alpha3 NC1-specific alpha1beta1 assay before promotion and do not transfer generic collagen-IV binding across NC1 chains."
        elif ligand == "FN1" and receptor == "SDC2":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:23333331"]
            species = "human colon-carcinoma cell adhesion assays"
            summary = "Primary cell-spreading and interaction assays show that syndecan-2 extracellular-domain expression regulates cellular attachment, spreading and migration on fibronectin, but do not establish a purified direct FN1-to-SDC2 binding edge."
            limitations = "Retain the fibronectin-matrix and syndecan-2 cell-adhesion context; require direct ligand-binding or receptor-dependent perturbation before promotion and do not infer a canonical intracellular or TF route from matrix adhesion alone."
        elif ligand == "FN1" and receptor == "PLAUR":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:19411312", "PMID:15684035"]
            species = "human fibroblast and tumor-cell adhesion assays"
            summary = "Primary studies place uPAR/PLAUR in integrin-dependent adhesion and signaling on fibronectin, including uPAR modulation of alpha5beta1 fibronectin binding, but the demonstrated interactions are uPAR-integrin and uPAR-uPA mechanisms rather than direct FN1-to-PLAUR receptor binding."
            limitations = "Retain uPAR-integrin, uPA and fibronectin-matrix crosstalk as receptor-proximal context; do not materialize FN1-PLAUR as a direct binary ligand edge or infer a standalone uPAR signaling route from matrix colocalization."
        elif ligand == "FGF1" and receptor == "NRP1":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
            primary = ["PMID:15695515"]
            species = "human recombinant-protein biosensor and solution-binding assays"
            summary = "Primary optical-biosensor and solution-binding assays detect direct interaction of FGF1 with neuropilin-1, in a heparin-sensitive binding context shared with other heparin-binding growth factors."
            limitations = "Represent FGF1-NRP1 as a heparin-sensitive co-receptor or presentation interaction; do not infer canonical NRP1 signaling, a unique intracellular relay or a terminal-TF output from the binding study alone."
        elif ligand == "FGF1" and receptor == "FGFRL1":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:19920134", "PMCID:PMC2804375"]
            species = "human recombinant receptor and Xenopus embryonic assays"
            summary = "Primary ligand-dot-blot, cell-based and surface-plasmon-resonance studies identify FGFRL1 binding to selected FGF ligands but report no binding of FGF1 to FGFRL1-expressing cells under the tested conditions."
            limitations = "Retain the FGFRL1 decoy-receptor and selected-FGF specificity context; do not transfer canonical FGF1 binding to FGFRL1 without a new pair-specific assay or infer kinase signaling from a receptor lacking the canonical tyrosine-kinase domain."
        elif ligand == "CCL2" and receptor in {"ACKR4", "CCR3", "CCR5", "CXCR3"}:
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:24890717", "PMID:35570218"]
            species = "mouse leukocyte and human CCR2 structural/functional studies"
            summary = "Primary receptor-specificity studies identify CCR2 as the conventional CCL2 receptor and ACKR1/ACKR2 as atypical CCL2-binding receptors, while the listed ACKR4, CCR3, CCR5 and CXCR3 candidates were not supported as direct CCL2 receptors."
            limitations = "Retain CCL2-CCR2 and CCL2-ACKR1/ACKR2 with their species and scavenging/signaling boundaries; do not transfer CCL2 activity to other chemokine-receptor paralogs from family membership or shared inflammatory expression."
        elif ligand == "VEGFD" and receptor == "FLT1":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:9435229", "PMID:11279005"]
            species = "human and mouse VEGF-D receptor-specificity assays"
            summary = "Primary receptor-binding and cross-linking studies identify VEGFR2/KDR and VEGFR3/FLT4 as VEGF-D receptors and report that VEGF-D does not bind VEGFR1/FLT1 under the tested conditions."
            limitations = "Retain mature VEGFD-KDR/FLT4 receptor and species boundaries; do not transfer VEGF-A/FLT1 specificity to VEGF-D or infer an FLT1 route from VEGF-family membership."
        elif ligand == "VEGFD" and receptor in {"ITGA1", "ITGA2", "ITGA4", "ITGA5"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:21071450", "PMID:11786413", "PMID:11279005"]
            species = "human and mouse VEGF/VEGF-D endothelial and integrin studies"
            summary = "Primary studies support VEGF-family cooperation with integrin-mediated endothelial migration and signaling, and directly identify alpha9beta1 as a binding partner for VEGF-A/C/D, but they do not establish VEGFD binding to the listed alpha1, alpha2, alpha4 or alpha5 integrins."
            limitations = "Retain VEGFD-KDR/FLT4 and integrin-assisted endothelial signaling as separate contextual layers; require an exact VEGFD-to-integrin binding or receptor-dependent assay before promotion and do not transfer alpha9beta1 evidence across integrin subunits."
        elif ligand in {"COL9A1", "COL9A2", "COL9A3"} and receptor in {"ITGA1+ITGB1", "ITGA2+ITGB1", "ITGA10+ITGB1"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:15383545"]
            species = "human recombinant collagen IX and human chondrocyte/CHO adhesion assays"
            summary = "Primary adhesion, recombinant-integrin and alpha-I-domain studies show collagen IX recognition by alpha1beta1, alpha2beta1 and alpha10beta1, but the public row names one COL9 chain rather than the assembled collagen-IX ligand tested in the primary assays."
            limitations = "Retain collagen-IX integrin adhesion and cartilaginous-matrix context; require chain-assembly and exact isoform evidence before promotion of an individual COL9A1/2/3 row and do not infer a soluble signaling cascade from matrix adhesion alone."
        elif ligand in {"COL4A4", "COL4A5", "COL4A6"} and receptor in {"ITGA1+ITGB1", "ITGA2+ITGB1"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:8344274", "PMID:9326385"]
            species = "human collagen-IV biochemical and skin-basement-membrane assays"
            summary = "Primary studies establish collagen-IV binding sites for alpha1beta1 and alpha2beta1 and show collagen-IV chain/beta1-integrin colocalization during basement-membrane formation, but they do not resolve the exact assembled alpha4, alpha5 or alpha6 collagen-IV network for this individual-chain row."
            limitations = "Retain collagen-IV integrin and basement-membrane context; require chain-composition and exact receptor assay before promotion and do not transfer generic collagen-IV binding across alpha-chain assemblies or infer a complete signaling cascade."
        elif ligand == "COL4A4" and receptor == "ITGB3":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:22539938"]
            species = "human recombinant alpha4(IV) NC1 and melanoma-cell assays"
            summary = "Primary surface-plasmon-resonance and adhesion studies show that recombinant alpha4(IV) NC1/tetrastatin binds the alphaVbeta3 integrin complex, while the public row supplies only the ITGB3 subunit and therefore does not resolve the complete receptor topology."
            limitations = "Retain alpha4(IV) NC1, alphaVbeta3 and matrikine/adhesion context; do not materialize COL4A4-ITGB3 as a standalone receptor edge without the alphaV subunit and exact mature-domain context."
        elif ligand == "ADAM10" and receptor == "AXL":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:27237127"]
            species = "lupus-prone mouse and human PBMC AXL-shedding assays"
            summary = "Primary cleavage and inhibition studies show that ADAM10, together with ADAM17/TACE, mediates AXL ectodomain shedding and thereby changes cellular responsiveness to Gas6."
            limitations = "Retain ADAM10 as a proteolytic regulator of AXL availability rather than an extracellular ligand; do not materialize ADAM10-AXL as a canonical ligand-receptor edge or infer a direct ADAM10-to-TF route."
        elif ligand == "ADAM10" and receptor == "NOTCH1":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:19726682", "PMID:19704010", "PMID:33673337"]
            species = "human and mouse Notch1 cell-based cleavage/signaling assays"
            summary = "Primary protease-dependence studies show that ADAM10 performs ligand-dependent Notch1 S2 cleavage and is required for the receptor-proximal step leading to gamma-secretase release of Notch intracellular domain."
            limitations = "Retain ADAM10-Notch1 as a proteolytic continuation of juxtacrine Notch signaling, not as a soluble ligand edge; preserve ligand-dependent versus ligand-independent ADAM17 context and do not infer a universal TF output outside Notch-specific assays."
        elif ligand == "ADAM10" and receptor in {"TSPAN5", "TSPAN10", "TSPAN14", "TSPAN15", "TSPAN17"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:23035126", "PMID:23091066", "PMID:26668317"]
            species = "human TspanC8/ADAM10 biochemical, cell-based and primary-cell assays"
            summary = "Primary co-immunoprecipitation and trafficking studies show direct ADAM10 association with the listed TspanC8 tetraspanins, which regulate ADAM10 maturation, surface expression and substrate-selective Notch signaling."
            limitations = "Retain the reverse regulatory-complex orientation and TspanC8-specific substrate/trafficking context; do not materialize ADAM10-to-TSPAN as an extracellular ligand-receptor edge or infer that every TspanC8 complex produces the same signaling output."
        elif ligand == "APP" and receptor == "GPC1":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:8940123"]
            species = "mouse brain-derived glypican and chick sympathetic-neuron assays"
            summary = "Primary affinity-column and purified-protein binding assays show that secreted glypican binds recombinant APP with nanomolar affinity, and the glypican-APP interaction inhibits APP-induced neurite outgrowth."
            limitations = "Represent this as a direct APP-glypican interaction with a matrix/co-receptor boundary; preserve the secreted glypican, recombinant APP and neurite-outgrowth context, and do not infer a canonical intracellular or TF cascade from the adhesion readout."
        elif ligand == "APP" and receptor == "NGFR":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:24358169", "PMID:19334058"]
            species = "mouse cortical-neuron and mammalian cell assays; human, mouse and rat tissue interaction evidence"
            summary = "Primary co-immunoprecipitation, pull-down, ELISA, reporter and neuronal perturbation studies support direct interaction of APP or soluble APP fragments with p75/NGFR and link the interaction to neurite outgrowth, APP processing and cell-death or transcriptional readouts."
            limitations = "Preserve the APP form, p75/NGFR context and assay-specific output; distinguish full-length APP or soluble APP-fragment interaction from Aβ or NGF signaling, and do not infer a universal canonical receptor cascade beyond the reported cellular models."
        elif ligand == "APP" and receptor == "NCSTN":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:16096062", "PMID:12805296", "PMID:12716934"]
            species = "mammalian cell and mouse knockout/fibroblast assays"
            summary = "Primary biochemical, imaging and loss-of-function studies show that nicastrin is a gamma-secretase component and substrate-recruitment/docking factor required for processing of APP-derived membrane stubs; this is an enzyme-substrate and proteolytic-complex relationship rather than a conventional extracellular ligand-receptor edge."
            limitations = "Retain APP-NCSTN as receptor-proximal proteolytic machinery and a source of APP-processing output; do not materialize it as a soluble ligand edge or infer an independent NCSTN-initiated TF route."
        elif ligand == "APP" and receptor == "FPR2":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:35365641"]
            species = "human FPR2 structural and functional assays"
            summary = "Primary structure-function studies establish FPR2 recognition and signaling responses for amyloid-beta Aβ42, not for the APP precursor protein represented by this candidate row."
            limitations = "Retain Aβ42-FPR2 as a distinct mature-peptide route; do not transfer its receptor evidence to full-length APP or soluble APP fragments without an APP-form-specific assay."
        elif ligand == "APP" and receptor in {"TREM2+TYROBP", "ADRA2A"}:
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            summary = "The current review pass did not verify an exact primary experiment supporting the APP-to-listed-receptor candidate; related studies may concern APP processing products, receptor complexes or different ligand forms."
            limitations = "Retain for targeted follow-up; do not materialize a graph edge from public-database membership or from evidence about Aβ, APP-processing machinery or receptor-family context alone."
        elif ligand == "LTF" and receptor == "AGER":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:8387541", "PMCID:PMC288218"]
            species = "human mononuclear-phagocyte and rat implant assays"
            summary = "The primary study concerns AGE-albumin recognition by RAGE and a lactoferrin-like cell-surface polypeptide; it does not establish mature lactoferrin/LTF as an AGER/RAGE ligand."
            limitations = "Do not transfer the lactoferrin-like-protein terminology to the LTF gene product or materialize LTF-AGER without an LTF-specific binding assay."
        elif ligand == "LTF" and receptor == "TNFRSF11B":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "downstream_or_functional"
            primary = ["PMID:22902986"]
            species = "bovine lactoferrin-treated ovariectomized-rat bone model"
            summary = "Primary in-vivo treatment experiments show that bovine lactoferrin changes osteoprotegerin/TNFRSF11B and RANKL expression during bone remodeling, but do not establish TNFRSF11B as a direct lactoferrin receptor."
            limitations = "Retain the lactoferrin bone-remodeling and OPG/RANKL/RANK pathway context; do not materialize a direct LTF-TNFRSF11B binding edge or infer that TNFRSF11B is the initiating receptor."
        elif ligand == "LTF":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            summary = "The current review pass did not verify an exact primary experiment for this LTF-to-receptor candidate."
            limitations = "Retain for targeted follow-up; do not materialize an edge from public-database membership or from evidence for an unidentified lactoferrin-binding site alone."
        elif ligand == "CD40LG" and receptor == "TRAF3":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:10984535", "PMID:15708970", "PMID:24391649"]
            species = "human and mouse CD40 signaling studies"
            summary = "Primary structural, mutational and cell-signaling studies place TRAF3 on the cytoplasmic CD40 receptor complex and show CD40L-dependent NF-kB pathway modulation, but TRAF3 is an intracellular adaptor rather than the extracellular CD40LG receptor."
            limitations = "Retain CD40LG-CD40-TRAF3 as a receptor-proximal continuation and intracellular signaling context; do not materialize CD40LG-TRAF3 as a direct ligand-receptor edge or infer a standalone TRAF3 receptor."
        elif ligand == "CD40LG" and receptor == "CD9":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "downstream_or_functional"
            primary = ["PMID:24918051"]
            species = "human germinal-center B-cell assays"
            summary = "Primary cell assays report that CD9-positive germinal-center B cells survive differently in CD40L-containing co-culture conditions, but do not establish CD9 as a direct CD40 ligand receptor or binding partner."
            limitations = "Retain CD40L and CD9 as a cell-state/costimulatory context; require direct pair-specific binding or receptor-dependence before graph promotion and do not infer a CD9-initiated intracellular route."
        elif ligand == "CD40LG":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            summary = "The current review pass did not verify an exact primary experiment for this CD40LG-to-listed-protein candidate."
            limitations = "Retain CD40LG-CD40 and separately supported CD40 receptor-proximal machinery; do not materialize the listed candidate from family membership, co-expression or downstream pathway association alone."
        elif ligand == "RTN4" and receptor in {"LINGO1", "TNFRSF19"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:15694321", "PMID:17189258", "PMID:23438185"]
            species = "mouse and rat neuronal receptor-complex assays"
            summary = "Primary Nogo-receptor studies place LINGO1 and TROY/TNFRSF19 in the NgR receptor complex that mediates cellular responses to myelin inhibitors, while direct ligand-binding assays localize Nogo-66 recognition to NgR1 rather than LINGO1; this is receptor-complex evidence, not a standalone RTN4-to-coreceptor binding edge."
            limitations = "Retain RTN4/NgR1/LINGO1/TROY as a multicomponent inhibitory signaling route with the tested neuronal context; do not materialize RTN4-to-LINGO1 or RTN4-to-TNFRSF19 as independent binary receptor edges or infer a universal intracellular/TF route."
        elif ligand == "RTN4" and receptor == "RTN4RL1":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:17189258", "PMID:22406547"]
            species = "mouse Nogo-receptor-family binding and regeneration assays"
            summary = "Primary ligand-panel and receptor-family studies report RTN4/Nogo-66 binding to NgR1 but not to NgR3/RTN4RL1 under the tested conditions; RTN4RL1 evidence in the cited literature concerns other ligands or receptor-family functions."
            limitations = "Retain the RTN4-NgR1 route and distinguish RTN4RL1/NgR3 from NgR1; do not transfer receptor-family membership or RTN4RL1 binding by other ligands to an RTN4-RTN4RL1 edge."
        elif ligand == "RTN4":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            summary = "The current review pass did not verify an exact primary experiment for this RTN4-to-listed-protein candidate."
            limitations = "Retain the canonical RTN4/NgR1 receptor-complex route and the separately supported LINGO1/TROY context; do not materialize this candidate from Nogo-family membership or neuronal co-expression alone."
        elif ligand in {"COL6A5", "COL6A6"} and receptor in {"ITGA1+ITGB1", "ITGA2+ITGB1"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:8387021", "PMID:10772239", "PMID:1478946"]
            species = "human collagen-VI adhesion assays and mammalian chondrocyte/vascular smooth-muscle models"
            summary = "Primary adhesion, affinity and cell-blocking studies identify alpha1beta1 and alpha2beta1 as receptors for native type-VI collagen substrates and collagen-VI microfibrillar assemblies, with beta1-dependent cell-adhesion outputs."
            limitations = "Retain assembled native collagen-VI and integrin-adhesion context; the candidate names an individual COL6A5/COL6A6 chain not resolved in these native type-VI studies, so do not promote it as a chain-specific direct edge or infer a soluble signaling cascade."
        elif ligand.startswith("COL6"):
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            summary = "The current review pass found primary evidence for native type-VI collagen adhesion through selected integrins, but not an exact chain-specific experiment for this COL6 candidate and receptor pair."
            limitations = "Retain native collagen-VI integrin adhesion as family context; require exact chain, assembled isoform and receptor evidence before graph promotion."
        elif ligand == "HAPLN1":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            summary = "Primary HAPLN1 studies support extracellular-matrix organization and CD44/TGF-beta-receptor-II-associated functional effects, but the current review did not verify any of the listed HAPLN1-to-receptor candidates as the initiating pair."
            limitations = "Retain HAPLN1 matrix and CD44/TGFBR2 context for targeted follow-up; do not materialize the listed candidates from downstream effects, co-expression or matrix association alone."
        elif ligand == "COL4A2":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            primary = ["PMID:8344274", "PMID:9139675", "PMID:19229828"]
            species = "human collagen-IV fragment, integrin-domain and renal-cell assays"
            summary = "Primary studies support collagen-IV CB3 or NC1-domain interactions with selected alpha1beta1/alpha2beta1 integrins and distinguish chain/domain-specific recognition, but no exact primary experiment was verified for this COL4A2-to-listed-receptor candidate."
            limitations = "Retain collagen-IV fragment, chain-assembly and integrin-family context; do not transfer alpha1beta1/alpha2beta1 evidence to unrelated receptors or materialize an isolated COL4A2 edge without exact chain/domain and receptor-complex support."
        elif ligand in {"COL9A1", "COL9A2", "COL9A3"}:
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            primary = ["PMID:15383545"]
            species = "recombinant collagen-IX and human chondrocyte/osteoblast adhesion assays"
            summary = "Primary collagen-IX adhesion studies support alpha1beta1, alpha2beta1 and alpha10beta1 recognition of recombinant collagen IX, but the current candidate uses an individual COL9 chain label and a different receptor assignment that was not verified as an exact pair."
            limitations = "Retain assembled collagen-IX, chain-composition and integrin-specificity context; do not transfer the collagen-IX integrin result to CD44, GP6, MAG, syndecan or unrelated integrin complexes without pair-specific evidence."
        elif ligand == "FSTL5":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            primary = ["PMID:32740091", "PMID:30255547"]
            species = "human hepatocellular-carcinoma tissue and cell/xenograft models"
            summary = "Primary FSTL5 studies support expression-associated effects on epithelial-mesenchymal transition, proliferation, invasion and apoptosis in hepatocellular-carcinoma models, but do not identify any of the listed proteins as a direct FSTL5 receptor."
            limitations = "Retain FSTL5 functional and disease-model outputs as ligand-form and cell-state context; do not infer a follistatin/activin receptor route or materialize a listed FSTL5 receptor from family analogy or expression correlation."
        elif ligand in {"COL4A3", "COL4A4", "COL4A5", "COL4A6"}:
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            primary = ["PMID:8344274", "PMID:9326385", "PMID:19229828"]
            species = "human collagen-IV fragment, NC1-domain and renal-cell assays"
            summary = "Primary studies support collagen-IV fragment or NC1-domain interactions with selected integrins and distinguish chain/domain-specific recognition, but no exact primary experiment was verified for this remaining collagen-IV-chain-to-receptor candidate."
            limitations = "Retain collagen-IV chain assembly, NC1/CB3 fragment and integrin-family context; do not transfer evidence between alpha3, alpha4, alpha5 or alpha6 chains or materialize an unrelated receptor edge without exact chain/domain and receptor-complex support."
        elif ligand == "COL4A1":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            primary = ["PMID:8344274", "PMID:9139675", "PMID:19229828"]
            species = "human collagen-IV fragment, NC1-domain and renal-cell assays"
            summary = "Primary studies support selected collagen-IV CB3 or NC1-domain interactions, including an alpha1 NC1-to-alpha3beta1 result already captured separately, but no exact primary experiment was verified for this remaining COL4A1-to-receptor candidate."
            limitations = "Retain collagen-IV alpha1-chain domain and integrin-family context; do not transfer alpha1 NC1 evidence to other receptors or materialize an isolated COL4A1 edge without exact chain/domain and receptor-complex support."
        elif ligand == "COL2A1":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            primary = ["PMID:10772239", "PMID:8832409", "PMID:9041938"]
            species = "human chondrocyte, collagen-II adhesion and collagen-VI comparator assays"
            summary = "Primary chondrocyte and collagen-adhesion studies support selected alpha1beta1/alpha2beta1 interactions with type-II collagen, but no exact primary experiment was verified for the remaining COL2A1-to-listed-receptor candidates."
            limitations = "Retain assembled collagen-II and beta1-integrin adhesion context; do not transfer it to CD44, syndecan, alpha2beta, alpha3/9 or alphaVbeta8 candidates without pair-specific evidence or infer a soluble signaling cascade from matrix adhesion."
        elif ligand == "CEACAM2":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            primary = ["PMID:8576129"]
            species = "mouse and rat C-CAM/CEACAM cell-adhesion studies"
            summary = "Primary CEACAM/C-CAM work supports CEACAM2-containing homophilic adhesion and cytoplasmic calmodulin regulation, but the current review did not verify any of the listed CEACAM2-to-receptor candidates as an exact ligand-receptor pair."
            limitations = "Retain CEACAM2 homophilic adhesion and paralog-specific context; do not transfer CEACAM1/5, glycan or viral-receptor evidence to CEACAM2 or materialize the listed rows without exact pair-specific testing."
        elif ligand == "COL1A2":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            primary = ["PMID:2156854", "PMID:1396580", "PMID:10713152"]
            species = "human and rat collagen-I adhesion and recombinant integrin assays"
            summary = "Primary collagen-I studies support selected alpha1beta1/alpha2beta1 collagen receptors and distinguish collagen-subtype and conformation-specific recognition, but no exact primary experiment was verified for the remaining COL1A2-to-listed-receptor candidates."
            limitations = "Retain assembled collagen-I, triple-helical conformation and integrin-family context; do not transfer it to CD44, CD93, alpha2beta, alpha3beta1, alpha9beta1 or beta3 candidates without pair-specific chain/domain evidence."
        elif ligand == "CCL27B":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_unverified"
            primary = ["PMID:10725697", "PMID:11821900", "PMID:40975172"]
            species = "human CCL27/CCR10 and CCL27/CCL28 receptor-specificity studies"
            summary = "Primary chemokine studies establish CCL27/CCR10 signaling and distinguish CCL28/CCR3 specificity, but no exact primary experiment was verified for the CCL27B-to-listed-receptor candidates."
            limitations = "Retain mature CCL27-CCR10 and CCL28-CCR3 specificity separately; resolve the CCL27B species/isoform identity before promotion and do not transfer paralog or receptor-family evidence to ACKR2, CCR2, CCR3, GRM7, MTNR1A or ADRA2A."
        elif ligand == "FGFRL1":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:19920134", "PMCID:PMC2804375"]
            species = "human FGFRL1 receptor/decoy and Xenopus embryonic assays"
            summary = "Primary studies characterize FGFRL1 as an FGFR-like membrane receptor or decoy that can bind selected FGF ligands, not as an extracellular ligand for the listed receptor candidates."
            limitations = "Represent FGFRL1 in receptor/decoy and receptor-complex layers; do not materialize FGFRL1-to-FGFR1, GP6, GPC4, NRXN2, NRXN3 or PLVAP as ligand-receptor edges."
        elif ligand == "LOC100861978":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_review_locator"
            summary = "The LOC-prefixed public identifier was not resolved to a verified mature ligand identity and exact receptor assay in this pass."
            limitations = "Resolve the species-specific gene and protein form before promotion; do not infer receptor specificity from an unresolved LOC label or public-database membership alone."
        elif ligand == "BDNF" and receptor == "NGFR":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:9472042"]
            species = "mouse sympathetic-neuron and neuronal apoptosis assays"
            summary = "Primary neuronal studies show that BDNF activates p75/NGFR-dependent apoptosis, with function-blocking p75 antibody and p75-null neurons reducing the response; BDNF also induces c-Jun phosphorylation in the reported model."
            limitations = "Preserve the BDNF/p75-NGFR, neuronal apoptosis and c-Jun context; do not generalize this p75 route to all BDNF responses or infer a unique intracellular cascade beyond the reported model."
        elif ligand == "C3" and receptor == "C3AR1":
            disposition = "reject_precursor_or_non_edge_form"
            layer = "candidate_only_unverified"
            primary = ["PMID:9382922", "PMID:10092660"]
            species = "mouse and human C3a-receptor assays"
            summary = "Primary C3a-receptor studies show that C3a, the proteolytic fragment generated from complement C3, binds C3AR1 and triggers calcium signaling; the intact C3 precursor label is therefore not the direct ligand form."
            limitations = "Retain mature C3a-to-C3AR1 signaling and complement C3 processing separately; do not materialize intact C3 as a direct C3AR1 ligand or infer receptor specificity across C3 fragments."
        elif ligand == "CCL21B" and receptor == "CCR7":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:19451552", "PMID:34586443"]
            species = "mouse and human CCL21/CCR7 studies"
            summary = "Primary CCL21 studies establish CCR7-dependent signaling, T-cell costimulation and chemotaxis, but the candidate uses the CCL21B paralog label and the reviewed studies do not resolve the exact CCL21B isoform in the assayed mature ligand."
            limitations = "Retain CCL21-family-to-CCR7 signaling and the reported DOCK2/Rac/Akt/MEK/ERK outputs; resolve CCL21B isoform and species identity before promoting this exact row."
        elif ligand == "CCL5" and receptor == "CCR4":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation"
            primary = ["PMID:8573157"]
            species = "human and mouse CCR4 transfectant binding assays"
            summary = "Primary transfectant competition-binding experiments show direct CCL5/RANTES binding to human and murine CCR4, supporting a bounded ligand-receptor edge without asserting downstream signaling in that study."
            limitations = "Preserve the CCR4 transfectant and direct-binding context; do not infer canonical CCL5 signaling outputs or substitute CCR4 for the better-established CCL5 receptor contexts without cell-type-specific functional evidence."
        elif ligand == "CXCL13" and receptor == "CXCR3":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:11554781"]
            species = "human CXCR3-transfectant and chemotaxis assays"
            summary = "Primary studies show that CXCL13/BCA-1 competes for CXCR3 binding and induces CXCR3-dependent chemotaxis and GTP-gamma-S signaling in transfected cells."
            limitations = "Preserve the human CXCL13/CXCR3 transfectant and chemotaxis context; do not infer that CXCR3 replaces the canonical CXCR5 route in every tissue or assert a complete intracellular/TF chain from the reported assays."
        elif ligand == "NPPB" and receptor == "NPR3":
            disposition = "already_present_exact_or_alias"
            matched_ids = "M21B-E001702"
            primary = ["PMID:1309330", "PMCID:PMC2939486", "PMID:34919054"]
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            species = "human and rat receptor-binding assays; mouse functional model"
            summary = "The graph already contains the BNP/NPPB-to-NPR3/NPR-C clearance-receptor edge. Primary receptor-selectivity work supports BNP binding to NPR-C, and newer functional work places NPRC in a BNP-dependent receptor context, strengthening the existing alias without asserting a universal NPR3 signaling route."
            limitations = "Preserve NPR3/NPR-C as a clearance-receptor and context-dependent functional route; do not duplicate the graph edge, treat NPR3 as equivalent to NPR1/NPR2, or infer a complete intracellular, TF or terminal-gene chain from the cited assays."
        elif ligand == "ICOSL" and receptor in {"CD28", "CTLA4"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = ["PMID:10744980"]
            species = "human LICOS/ICOSL receptor-family binding assays"
            summary = "Primary receptor-specificity experiments identify ICOS as the physiological LICOS/ICOSL receptor and report only weak CD28 or CTLA4 binding under nonphysiological lower-temperature conditions; the candidate rows therefore retain family-level context but are not canonical signaling edges."
            limitations = "Preserve ICOSL-ICOS costimulatory specificity and the assay-temperature boundary; do not materialize ICOSL-CD28 or ICOSL-CTLA4 as physiological signaling routes or infer downstream output from the weak conditional binding result."
        elif ligand == "PPY" and receptor in {"NPY1R", "NPY2R"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = ["PMID:8641440", "PMID:17204471"]
            species = "NPY-family receptor cloning and ligand-binding assays"
            summary = "Primary NPY-family receptor studies distinguish pancreatic polypeptide preference for the Y4/NPY4R subtype from the Y1/NPY1R and Y2/NPY2R preference for NPY or PYY; the public PPY-to-NPY1R/NPY2R rows are therefore retained as receptor-family context rather than promoted as exact edges."
            limitations = "Resolve mature PPY identity and NPY4R/Y4 specificity before promotion; do not transfer Y4 preference to NPY1R or NPY2R, or infer downstream signaling from NPY-family membership alone."
        elif ligand == "GCG" and receptor == "GCGR":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:23863937", "PMID:29300013", "PMID:23185367"]
            species = "human GCGR structural, mutational and cellular assays"
            summary = "Primary structural, mutational and cellular studies directly resolve glucagon recognition by GCGR and link receptor engagement to receptor activation and cAMP responses, supporting a bounded GCG/glucagon-to-GCGR edge."
            limitations = "Preserve mature glucagon, human GCGR and the reported ligand-binding/second-messenger contexts; do not infer a complete intracellular kinase or TF chain, or transfer glucagon specificity to other class-B peptide receptors."
        elif ligand == "GHRL" and receptor == "GHRHR":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = ["PMID:11314756", "PMID:30686667"]
            species = "human ghrelin receptor-binding and structural assays"
            summary = "Primary studies establish mature, octanoylated ghrelin binding to the growth-hormone-secretagogue receptor GHSR and define its GHSR-binding determinants, but do not establish GHRHR as the receptor for ghrelin; the candidate is retained as a receptor-label boundary rather than promoted."
            limitations = "Resolve GHRHR versus GHSR nomenclature and preserve the mature ghrelin modification requirement; do not transfer GHSR binding or signaling evidence to GHRHR."
        elif ligand == "EFNB3" and receptor == "EPHB2":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:20678574"]
            species = "mouse hippocampal and HEK-cell ephrin-B3/EphB2 assays"
            summary = "Primary studies place ephrin-B3 and EphB2 in a neuronal cis-interaction context and show altered EphB2 and NMDA-receptor phosphorylation when ephrin-B3 is present or absent; this supports receptor-proximal EphB2 context but does not resolve a conventional trans EFNB3-to-EPHB2 ligand edge."
            limitations = "Preserve ephrin-B3/EphB2 cis-versus-trans orientation and neuronal synaptic context; do not materialize a canonical trans edge or infer a universal EphB2 intracellular or TF route from the reported phosphorylation phenotypes."
        elif ligand == "CALCA" and receptor == "RAMP1":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:24115156", "PMID:30209400", "PMID:16776831"]
            species = "human CGRP receptor-complex biochemical, structural and binding assays"
            summary = "Primary studies show that mature CGRP binds and activates the CALCRL/CLR-RAMP1 receptor complex, with RAMP1 determining receptor selectivity and contributing to the ligand-binding pocket; RAMP1 is therefore a required complex component rather than a complete receptor by itself."
            limitations = "Represent mature CGRP/CALCA processing and the CALCRL-RAMP1 complex together; do not materialize CALCA-to-RAMP1 as an isolated binary receptor edge or infer a complete downstream/TF route from complex binding and G-protein activation alone."
        elif ligand == "EFNA3" and receptor == "EPHA4":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:22568954", "PMID:10366629"]
            species = "mouse hippocampal and rat striatal ephrin-A3/Eph receptor assays"
            summary = "Primary pull-down, mass-spectrometry and binding studies identify EphA4 as an ephrin-A3-associated receptor in adult mouse hippocampus and connect the pair to dendritic-spine, astrocyte glutamate-uptake and synaptic-plasticity context, while rat striatal assays show tissue-dependent selectivity toward EphA7; this supports a bounded EFNA3-EPHA4 edge rather than universal EphA4 specificity."
            limitations = "Preserve ephrin-A3 form, EphA4 versus EphA7 tissue selectivity and neuronal context; do not infer identical affinity across EphA paralogs or a complete intracellular/TF route beyond the reported Eph signaling and synaptic outputs."
        elif ligand == "KLK1" and receptor == "F2R":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:20482314", "PMID:24586431"]
            species = "human tissue-kallikrein/PAR1 cell and prostate-cancer assays"
            summary = "Primary studies support tissue kallikrein/KLK1-dependent prostate-cell migration and invasion through PAR1/F2R signaling and show KLK1-associated induction of PAR transcripts and MAPK-linked inflammatory responses; this is proteolytic receptor activation rather than a conventional soluble ligand-binding edge."
            limitations = "Represent KLK1 as a protease-triggered PAR1 receptor-proximal input with cleavage and substrate-form context; do not materialize KLK1-F2R as an ordinary ligand-binding edge or infer a universal TF/target-gene route from the disease-model outputs."
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
            elif ligand == "FGF17" and receptor in {"FGFR1", "FGFR2"}:
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:10381577", "PMID:16597617", "PMCID:PMC2080618"]
                species = "mouse; human recombinant protein"
                summary = "Primary FGF17 studies support receptor-dependent activity through the c-spliced FGFR1 and FGFR2 family: transforming assays identify activation of either receptor c isoform, and a complete FGF-family BaF3 comparison shows FGF17 activity on FGFR1c and FGFR2c with heparin context."
                limitations = "Preserve the c-splice-isoform and heparan-sulfate context; the evidence does not assert an isoform-free receptor edge, a universal intracellular relay or a terminal-TF output."
            elif ligand == "FGF20" and receptor == "FGFR1":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:16597617", "PMCID:PMC2080618", "PMID:19564416", "PMCID:PMC2725704", "DOI:10.1128/MCB.01780-08"]
                species = "human recombinant protein; mouse cell assays"
                summary = "Primary receptor-specificity and structural/functional studies support FGF20 activity through FGFR1c: the complete FGF-family BaF3 comparison detects FGF20 activation of c-spliced receptors, while independent work demonstrates FGF20-FGFR1c binding, mitogenesis and ERK output."
                limitations = "Preserve the FGF20 dimerization, heparin/heparan-sulfate and FGFR1c context; do not generalize across receptor splice isoforms or infer a terminal-TF output."
            elif ligand == "FGF20" and receptor == "FGFR2":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:16597617", "PMCID:PMC2080618"]
                species = "human recombinant protein; mouse BaF3 cell assays"
                summary = "The complete primary FGF-family BaF3 comparison detects FGF20 activity on the c-spliced FGFR2 receptor, with heparin-dependent mitogenic readout under the tested conditions."
                limitations = "Preserve the FGFR2c splice-isoform and heparan-sulfate assay context; the study is semiquantitative and does not establish a universal intracellular relay or terminal-TF output."
            elif ligand == "FGF23" and receptor == "FGFR3":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:37286607", "PMCID:PMC10284700", "DOI:10.1038/s41586-023-06155-9"]
                species = "human structural system; cell-based receptor-complex assays"
                summary = "Primary structural and cell-based studies support an FGF23-FGFR3c-alphaKlotho quaternary signaling complex, but the public row omits the required alphaKlotho co-receptor and therefore is retained as complex-boundary evidence rather than a standalone FGFR3 edge."
                limitations = "Represent FGF23 with the intact alphaKlotho/FGFR3c complex and heparan-sulfate context; do not split the complex into a standalone FGF23-FGFR3 edge or infer a terminal-TF output."
            elif ligand == "FGF3" and receptor in {"FGFR1", "FGFR2"}:
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:7592624", "DOI:10.1074/jbc.270.41.24197"]
                species = "mouse FGF3; receptor isoform assays"
                summary = "Primary receptor-binding competition and BaF3 mitogenic assays show FGF3 binding and activating FGFR1 and FGFR2, with strongest activity at the IIIb isoforms and lower-affinity interaction with FGFR2c."
                limitations = "Preserve the FGFR1/FGFR2 splice-isoform, heparin and potency differences; do not collapse isoform-specific activity into one universal receptor edge or infer a terminal-TF output."
            elif ligand == "FGF8" and receptor == "FGFR1":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:16384934", "PMCID:PMC1356110"]
                species = "human recombinant protein; chick and mouse developmental assays"
                summary = "Primary structural, SPR and developmental assays support FGF8b interaction with FGFR1c and receptor-dependent organizer activity; FGF8b binds FGFR1c as part of the c-isoform receptor profile."
                limitations = "Preserve FGF8 splice-isoform and developmental-context boundaries; the evidence does not justify an isoform-free FGF8-FGFR1 edge, universal intracellular relay or terminal-TF output."
            elif ligand == "FGF7" and receptor in {"FGFR3", "FGFR4"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                primary = ["PMID:10950949", "PMID:16597617", "PMCID:PMC2080618"]
                summary = "Primary receptor-specificity studies restrict FGF7 activity to the FGFR2 IIIb/KGFR receptor context and do not support the listed FGFR3 or FGFR4 pairings."
                limitations = "Retain FGF7-FGFR2b evidence with its splice-isoform boundary; do not transfer FGF-family receptor specificity to FGFR3/FGFR4."
            elif ligand == "FGF10" and receptor in {"FGFR3", "FGFR4"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                primary = ["PMID:12591959", "PMID:16597617", "PMCID:PMC2080618"]
                summary = "Primary structural and receptor-specificity studies restrict FGF10 signaling to the FGFR2 IIIb receptor context and do not support the listed FGFR3 or FGFR4 pairings."
                limitations = "Retain FGF10-FGFR2b evidence with its splice-isoform boundary; do not transfer FGF-family receptor specificity to FGFR3/FGFR4."
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
            elif ligand == "CGA":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                primary = ["PMID:15249700"]
                species = "human alpha-subunit/TSHR assay"
                summary = "CGA encodes the common glycoprotein-hormone alpha subunit rather than a complete mature TSH, FSH, LH or hCG ligand; a primary TSHR assay found no agonist activity for wild-type free alpha, while activity required engineered alpha variants."
                limitations = "Require the complete hormone heterodimer and exact receptor assay; do not materialize CGA alone as a ligand or transfer one beta-subunit-specific route across FSHR, LHCGR and TSHR."
            elif ligand == "CCL1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                primary = ["PMID:9207005", "PMID:9469461"]
                species = "human and mouse CCR8 receptor-expression assays"
                summary = "Primary cloning, binding and chemotaxis studies identify CCL1/I-309 and its mouse homolog TCA-3 as CCR8 ligands; the listed ACKR and CCR1/2/3/5 rows were not established as direct CCL1 receptor pairings."
                limitations = "Preserve the CCL1-CCR8 species and chemokine-processing context; do not transfer receptor promiscuity from other CC chemokines or materialize unsupported ACKR/CCR paralog edges."
            elif ligand == "CCL12":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                primary = ["PMID:8996246", "PMID:18334747"]
                species = "mouse CCL12/MCP-5 receptor-expression assays"
                summary = "Primary murine MCP-5/CCL12 studies show calcium flux and chemotaxis through mouse or human CCR2, with no tested response through CCR1, CCR3 or CCR5; the listed ACKR, CCR1, CCR3, CCR4, CCR5 and CCR10 rows are not supported as direct CCL12 edges."
                limitations = "Preserve mouse-specific CCL12/CCR2 and mature chemokine context; do not transfer human CCL2-family receptor promiscuity to CCL12 or infer ACKR/CCR paralog activity without an exact assay."
            elif ligand == "CORT" and receptor == "MRGPRB2":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:25517090", "PMCID:PMC4359082", "PMID:32038646", "PMCID:PMC6985555"]
                species = "mouse mast-cell models"
                summary = "Primary mouse mast-cell and receptor-expression experiments support cortistatin/CST-14 activation of MrgprB2, the mouse ortholog of human MRGPRX2, with receptor-dependent mast-cell activation and calcium/degranulation outputs."
                limitations = "Preserve mature cortistatin peptide processing, mouse MrgprB2 and mast-cell context; do not transfer the edge to other MRGPR paralogs or infer a universal intracellular relay or terminal-TF output."
            elif ligand == "CORT":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:12915402", "PMID:25517090", "PMID:18243519"]
                species = "human MRGPRX2 and mouse MrgprB2 family studies"
                summary = "Primary cortistatin pharmacology identifies human MRGPRX2 and mouse MrgprB2 as receptor contexts, while the listed MRGPR paralogs and unrelated adrenergic, glutamate or melatonin targets were not verified as exact cortistatin receptors."
                limitations = "Retain as family-level contextual evidence pending an exact ligand, receptor paralog and species assay; preserve the human MRGPRX2/mouse MrgprB2 boundary and do not promote unsupported paralogs or infer a terminal-TF route."
            elif ligand == "IL16" and receptor == "CD9":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:16144798", "PMCID:PMC1895361"]
                species = "human and mouse mast-cell models"
                summary = "Primary mast-cell and CD9-transfectant experiments support IL-16 binding to CD9 as an alternate receptor context, with CD9-dependent chemotaxis, calcium mobilization and PI3K/inositol-phosphate-associated outputs in human and mouse mast-cell systems."
                limitations = "Preserve CD9 as a cell-type-dependent alternate IL-16 receptor alongside the canonical CD4 route; do not generalize this mast-cell context to all IL-16-responsive cells or infer a terminal-TF output."
            elif ligand == "IL16":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                primary = ["PMID:10438516", "PMID:17624801", "PMID:16144798"]
                species = "human and mouse IL-16 receptor studies"
                summary = "Primary IL-16 studies establish CD4 as the principal receptor and CD9 as a cell-type-dependent alternate receptor; the listed glutamate and potassium-channel targets were not established as direct IL-16 receptor proteins."
                limitations = "Preserve mature IL-16 processing and CD4/CD9 receptor contexts; do not materialize ion-channel or unrelated membrane-protein rows from downstream calcium, migration or expression responses."
            elif ligand in {"FSHB", "LHB"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                primary = ["PMID:12773385", "PMID:15249700"]
                species = "human glycoprotein-hormone receptor assays"
                summary = "FSHB and LHB encode beta subunits that require the common alpha subunit to form mature FSH or LH; primary glycoprotein-hormone receptor studies define receptor specificity for complete heterodimeric hormones, not isolated beta-subunit labels."
                limitations = "Require the mature FSH or LH heterodimer and exact FSHR/LHCGR assay before promotion; do not materialize isolated FSHB/LHB rows to unrelated class-B, adrenergic, RAMP or TSH receptors."
            elif ligand == "GHRH" and receptor not in {"VIPR1", "VIPR2"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                primary = ["PMID:1333056", "PMID:7680413"]
                species = "rat; human receptor-expression assays"
                summary = "Primary cloning and expression studies identify GHRHR as the high-affinity, GHRH-specific receptor and show GHRH-dependent cAMP signaling; the listed non-GHRHR targets were not established as direct GHRH receptors."
                limitations = "Preserve the mature GHRH-GHRHR route and distinguish related class-B GPCRs; do not infer direct GHRH binding to unrelated receptors, transporters or signaling components from sequence similarity."
            elif ligand == "VIP" and receptor not in {"VIPR1", "VIPR2", "SCTR"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                primary = ["PMID:8933357"]
                species = "human receptor-expression and cAMP assays"
                summary = "Primary cloning and pharmacology identify VPAC1/VIPR1 and VPAC2/VIPR2 as the high-affinity VIP receptor pair; the listed adrenergic, vasopressin, melatonin, PTH, RAMP and enzyme targets were not established as direct VIP receptors."
                limitations = "Preserve VIPR1/VIPR2 and the separate PACAP/PAC1 specificity boundary; do not materialize VIP-to-unrelated-receptor rows from peptide-family homology or pathway co-occurrence."
            elif ligand == "TNF" and receptor == "LTBR":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:7594541", "PMID:8798772"]
                species = "mouse and human lymphotoxin-receptor studies"
                summary = "Primary LTBR studies establish binding and signaling for lymphotoxin alpha/beta complexes, but the reviewed evidence does not establish a direct TNF-alpha-to-LTBR ligand edge; the public row is retained as a TNF-family boundary hold."
                limitations = "Preserve TNF-alpha/TNFR1-2 and lymphotoxin/LTBR ligand-complex distinctions; require an exact TNF-alpha-LTBR binding or activation assay before promotion and do not infer a terminal-TF route from shared TNF-superfamily membership."
            elif ligand == "TNF":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:2158863", "PMID:21081755"]
                species = "human TNFR1/TNFR2 receptor studies"
                summary = "Primary TNF receptor studies establish direct TNF engagement of TNFR1 and TNFR2, while the listed CELSR2, FAS, FFAR2, FLT4, ICOS, NOTCH1, PTPRS, SEMA4C and TRPM2 rows are retained only as possible downstream or receptor-crosstalk contexts rather than direct TNF receptors."
                limitations = "Preserve the canonical TNF-TNFR1/TNFR2 ligand topology; require an exact TNF-to-target binding or receptor-dependent assay before promoting any noncanonical row, and do not infer a terminal-TF route from downstream expression or pathway crosstalk alone."
            elif ligand == "PRSS2" and receptor in {"F2R", "F2RL1"}:
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:16231009", "PMCID:PMC1751236", "DOI:10.1038/sj.bjp.0706410"]
                species = "human recombinant PRSS2; mouse orthology not directly tested"
                summary = "Primary recombinant-protease experiments show anionic trypsin/PRSS2 activation of human PAR1/F2R and PAR2/F2RL1, with calcium responses and receptor-desensitization controls in epithelial and neural cell models."
                limitations = "Preserve mature trypsin processing, proteolytic receptor activation and the human assay context; do not infer mouse activity, PAR3/PAR4 specificity, intracellular intermediates or a terminal-TF output without pair- and species-specific evidence."
            elif ligand == "PRSS2" and receptor == "F2RL3":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = ["PMID:16231009", "PMID:9618465"]
                species = "human recombinant trypsin/PAR family; exact PRSS2-PAR4 assay not shown"
                summary = "Primary work establishes that trypsin-family proteases can cleave and activate PAR4/F2RL3 and separately shows that recombinant PRSS2 activates epithelial PARs, but the exact PRSS2-PAR4 pairing was not directly assayed in the reviewed study."
                limitations = "Retain as a bounded PAR-family hypothesis only; require a direct PRSS2-PAR4 cleavage or activation assay before promotion and do not transfer PAR1/PAR2 evidence across PAR paralogs."
            elif ligand == "RLN1" and receptor == "RXFP2":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:15649866", "PMID:19416162", "PMID:23024363", "PMID:17623071"]
                species = "human relaxin-family pharmacology; species- and isoform-dependent"
                summary = "Primary relaxin-family pharmacology shows that relaxin can bind and activate RXFP2 in addition to its cognate RXFP1 route, generally with lower affinity or species-dependent activity, and identifies the RXFP2 extracellular binding site."
                limitations = "Preserve mature relaxin isoform, species, affinity and receptor-context boundaries; keep this as cross-reactive/conditional evidence rather than a universal canonical RLN1-RXFP2 edge, and do not infer a terminal-TF output."
            elif ligand == "RLN1" and receptor == "RXFP3":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:20159943"]
                species = "human relaxin-family pharmacology; receptor-expressing cell models"
                summary = "Primary RXFP3 studies detect weaker H2/relaxin-family activity at RXFP3 than the cognate H3-relaxin response, including receptor binding and biased cAMP, ERK1/2, NF-kappaB or AP-1 outputs."
                limitations = "Preserve relaxin isoform, receptor-expression system and biased signaling context; retain as cross-reactive evidence rather than a canonical RLN1-RXFP3 edge, and do not generalize H3-relaxin specificity to all relaxin forms."
            elif ligand == "RLN1" and receptor == "RXFP4":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                primary = ["PMID:27888281"]
                species = "human receptor-expressing cell model"
                summary = "Primary RXFP4 peptide-comparison experiments found no signaling activity or receptor internalization from relaxin-2/RLN1 under the tested conditions, whereas INSL5 and relaxin-3 were active."
                limitations = "Retain the cognate INSL5-RXFP4 and validated relaxin-3 cross-reactive routes; do not materialize RLN1-RXFP4 from relaxin-family membership alone."
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
            elif ligand == "PLAT" and receptor == "ITGB2":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M23B-E000238"
                primary = ["PMCID:PMC3402285", "PMID:22677557", "PMID:25131752"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse; human"
                summary = "Primary macrophage studies support tPA/PLAT signaling through an annexin A2 and Mac-1 context, of which ITGB2 is only one required subunit."
                limitations = "Preserve the complete Mac-1 and annexin-A2 receptor context; do not decompose the relay into direct PLAT-ITGB2 binding or infer a terminal TF route."
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
            elif ligand == "PLAU" and receptor == "ITGA5":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M23B-E000838"
                primary = ["PMID:15684035", "DOI:10.1083/jcb.200404112", "PMID:19411312", "PMCID:PMC2711805"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse comparator"
                summary = "Primary perturbation and receptor-complex studies support a uPA/PLAUR-uPAR to alpha5beta1 conformation and fibronectin-adhesion relay, not direct PLAU binding to ITGA5 alone."
                limitations = "Preserve PLAUR/uPAR, alpha5beta1 and matrix context; do not decompose the complex into a direct PLAU-ITGA5 binary edge or infer a terminal TF."
            elif ligand == "PLAU" and receptor in {"ITGAM", "ITGB1"}:
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M23B-E000840;M23B-E000838"
                primary = ["PMID:8874219", "DOI:10.1182/blood.V88.8.3185.bloodjournal8883185", "PMID:8621779", "PMID:19411312", "PMCID:PMC2711805"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse comparator"
                summary = "Primary studies support uPA/PLAUR-uPAR cooperation with Mac-1 or alpha5beta1 complexes in adhesion, chemotaxis and migration, but not direct PLAU binding to an isolated integrin subunit."
                limitations = "Preserve the complete PLAUR/uPAR-integrin complex and matrix context; do not promote isolated ITGAM or ITGB1 as the complete receptor or infer a terminal TF route."
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
            elif ligand == "SELE" and receptor == "SELPLG":
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E000282"
                primary = ["PMID:8621728", "PMID:9128259", "PMID:11071658"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human; mouse"
                summary = "The graph already contains primary-supported E-selectin/SELE binding to PSGL1/SELPLG with leukocyte rolling and adhesion outputs."
                limitations = "Preserve PSGL1 glycoform, selectin carbohydrate-dependence and flow-adhesion context; no unique intracellular or terminal-TF route is inferred."
            elif ligand == "SELL" and receptor == "SELPLG":
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E000283"
                primary = ["PMID:8892633", "PMID:12403782"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human; mouse"
                summary = "The graph already contains primary-supported L-selectin/SELL binding to PSGL1/SELPLG with leukocyte rolling and adhesion outputs."
                limitations = "Preserve PSGL1 glycoform and selectin-adhesion context; no unique intracellular or terminal-TF route is inferred."
            elif ligand == "SELP" and receptor == "SELPLG":
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E000214"
                primary = ["PMID:9829984", "PMID:7532174"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "The graph already contains primary-supported P-selectin/SELP binding to PSGL1/SELPLG with leukocyte rolling and adhesion outputs."
                limitations = "Preserve PSGL1 glycoform, selectin carbohydrate-dependence and flow-adhesion context; no unique intracellular or terminal-TF route is inferred."
            elif ligand == "SELPLG" and receptor in {"ITGAM", "ITGB2"}:
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M23B-E000260;M23B-E000261"
                primary = ["PMID:1709677", "PMCID:PMC2190843", "DOI:10.1084/jem.173.6.1493", "PMID:15187162", "DOI:10.4049/jimmunol.172.12.7780"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse comparator"
                summary = "Primary selectin-PSGL1 studies support Mac-1/ITGAM:ITGB2 activation and beta2-integrin avidity during firm leukocyte adhesion, but not direct PSGL1 binding to an isolated integrin subunit."
                limitations = "Preserve selectin-PSGL1 to Mac-1 activation context; do not promote isolated ITGAM or ITGB2 as the complete receptor or infer a terminal TF route."
            elif ligand == "SIRPA" and receptor == "CD47":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E000179"
                primary = ["PMID:18657508", "PMID:11283158"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse"
                summary = "The graph contains the primary-supported CD47-to-SIRPA/SIRPalpha inhibitory interaction in the reverse orientation of this public row."
                limitations = "Preserve CD47/SIRPA species, cis/trans and phagocytosis-brake context; do not add a duplicate reverse edge or infer a universal macrophage response."
            elif ligand == "RSPO2" and receptor in {"FZD4", "SDC4"}:
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E003271;M21B-E005577;M21B-E005578;M21B-E006688"
                primary = ["PMID:26123262", "PMID:27328992", "PMID:24225776", "PMID:37402772", "DOI:10.1038/s41598-023-37856-w"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human; mouse"
                summary = "Primary RSPO2 studies support LGR4/LGR5 and RNF43/ZNRF3 Wnt-potentiator complexes, but do not establish FZD4 or SDC4 as complete direct RSPO2 receptors in these rows."
                limitations = "Preserve LGR/E3-ligase/Wnt receptor-complex topology; do not collapse R-spondin potentiation into a binary RSPO2-FZD4 or RSPO2-SDC4 edge."
            elif ligand == "RSPO4" and receptor in {"LGR4+LRP5", "LGR4+LRP6", "LGR5+LRP5", "LGR5+LRP6", "LRP5", "LRP6"}:
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E006587;M21B-E006588"
                primary = ["PMID:21727895", "DOI:10.1038/nature10337"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human; mouse"
                summary = "Primary studies support RSPO4 binding to LGR4/LGR5 and association with Frizzled/LRP Wnt receptor complexes, but the listed composite or isolated LRP rows do not resolve a single direct RSPO4 receptor topology."
                limitations = "Preserve LGR-dependent multicomponent Wnt-potentiator topology and the binding-focused RSPO4 evidence; do not assign RSPO4-specific Wnt activation to isolated LRP5/LRP6."
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
            elif ligand in {"S100A8", "S100A9"} and receptor == "ITGB2L":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M23B-E001157;M23B-E001169;M23B-E000851"
                primary = ["PMID:12626582", "PMCID:PMC3281816", "PMID:22363402", "DOI:10.1371/journal.pone.0029333", "PMID:9570563", "DOI:10.4049/jimmunol.160.3.1427"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse comparator"
                summary = "Primary S100A8/A9 studies support Mac-1/CR3 ITGAM:ITGB2 activation and cell-based complex binding, but the public row contains the incomplete ITGB2L component and does not establish direct binding to that isolated chain."
                limitations = "Preserve S100A8/A9 dimer-state, Mac-1/CR3 and alternate-receptor context; do not decompose the receptor complex into ITGB2L alone or infer a terminal TF route."
            elif ligand == "S100A1" and receptor in {"RYR1", "RYR2", "TRPM3"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "S100A1 is an intracellular calcium-binding protein and these channels are intracellular or membrane-proximal partners, not an extracellular ligand-receptor route."
                limitations = "Represent S100A1 calcium-handling or channel-association mechanisms in intracellular layers; do not materialize them as extracellular ligand edges."
            elif ligand.startswith("S100A"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human; mouse"
                summary = "S100A-family extracellular danger-signal biology overlaps RAGE, TLR and scavenger-receptor contexts, but the listed candidate receptor is not asserted as an exact primary-supported edge here."
                limitations = "Require S100 paralog-specific mature-protein binding or receptor-triggering evidence; do not transfer S100A8/A9 family context across CD36, CD68, AGER or integrin candidates."
            elif ligand == "SEMA3C" and receptor.startswith("PLXNA"):
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E006550"
                primary = ["PMID:29661844"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human"
                summary = "Primary SEMA3C work supports a Plexin-D1:Plexin-A4 receptor complex; the public rows split or substitute Plexin-A paralogs not resolved by that study."
                limitations = "Preserve Plexin-D1:Plexin-A4 topology and neuropilin-enhancement boundary; do not promote SEMA3C-to-PLXNA1/2/3 as isolated direct edges."
            elif ligand == "SEMA3D":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E006621"
                primary = ["PMID:26243191", "PMCID:PMC4811025", "DOI:10.1038/srep23241"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "mouse"
                summary = "Primary SEMA3D work supports PLXND1 binding and invasion/guidance outputs, while the public rows list neuropilin or Plexin-A paralogs not established as the complete direct receptor."
                limitations = "Preserve PLXND1 and NRP1-enhanced context; do not transfer SEMA3D specificity to PLXNA1-4 or NRP1/2 as isolated receptors."
            elif ligand == "SEMA6D" and receptor != "PLXNA1":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000334"
                primary = ["PMID:14977921", "PMID:36156831"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "mouse; chick"
                summary = "Primary SEMA6D work identifies PLXNA1 as the direct receptor and documents broader receptor-panel or co-receptor context; the listed alternative targets are not individually promoted."
                limitations = "Preserve PLXNA1, NRCAM and region-specific co-receptor context; do not transfer SEMA6D binding to KDR, PLXNA4, PLXNC1 or TYROBP without exact pair-level primary evidence."
            elif ligand == "SEMA4A" and receptor.startswith("PLXNA"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The reviewed primary SEMA4A branch supports TIMD2/Tim-2 and other non-Plexin-A contexts, while Plexin-A evidence from SEMA3 ligands cannot be transferred to SEMA4A."
                limitations = "Require exact SEMA4A-Plexin-A binding or activation evidence; do not infer receptor specificity from semaphorin-family membership."
            elif ligand == "SCT":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Secretin/SCT signaling is centered on the secretin receptor SCTR, not the unrelated GPCRs and RAMP/TSHR/PTH-family targets listed here."
                limitations = "Require mature secretin and direct SCTR assay; do not transfer secretin-family specificity across unrelated GPCRs."
            elif ligand == "SHH" and receptor == "SMO":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000204;M22B-E000584"
                primary = reviewed
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human; mouse; rat comparator"
                summary = "The graph assigns direct SHH reception to PTCH1/PTCH2 and represents SMO as the downstream transducer in a composite PTCH1-SMO Hedgehog relay; direct SHH-SMO binding is not asserted."
                limitations = "Preserve PTCH1/PTCH2 ligand-binding and PTCH-SMO coupling topology; do not materialize SHH-SMO as a standalone direct ligand-receptor edge."
            elif ligand == "SHH" and receptor == "GPC5":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M22B-E000585"
                primary = reviewed
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "as stated in primary model/assay"
                summary = "GPC5 is represented as a Hedgehog co-receptor/scaffold that can facilitate SHH engagement with PTCH1, not as the canonical SHH receptor itself."
                limitations = "Preserve GPC5/PTCH1/SMO composite topology and developmental or tumor-model context; do not infer an autonomous GPC5 receptor relay or terminal TF output."
            elif ligand == "ROBO1" and receptor == "NCAM1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "ROBO1 is a guidance receptor and NCAM1 is an adhesion molecule; this row does not establish ROBO1 as a mature extracellular ligand for NCAM1."
                limitations = "Represent SLIT-ROBO and NCAM adhesion mechanisms in their proper orientations; do not invert ROBO receptors into ligand position."
            elif ligand == "SARAF":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "SARAF is an intracellular ER calcium-entry regulator, not a mature extracellular ligand for DAG1."
                limitations = "Represent SARAF-STIM/Orai calcium-homeostasis biology separately; do not materialize SARAF-DAG1 as a ligand-receptor edge."
            elif ligand.startswith("SERPINA") and receptor == "F12":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "SERPINA family proteins inhibit or regulate coagulation proteases such as factor XII; F12 is not a canonical cell-surface receptor in this row."
                limitations = "Represent serpin-protease inhibition separately from ligand-receptor signaling; require a defined membrane receptor and direct assay before promotion."
            elif ligand in {"SEMA3A", "SEMA3E", "SEMA3G", "SEMA4F"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                species = "as stated in primary model/assay"
                summary = "The semaphorin candidate overlaps neuropilin/plexin or immune-receptor family biology, but the exact ligand-receptor pair and composite receptor topology were not verified in a primary assay during this pass."
                limitations = "Require exact semaphorin isoform, neuropilin/plexin or immune-receptor composition and assay; do not transfer family-level guidance evidence across paralogs."
            elif ligand == "SERPINE1" and receptor in {"ITGAV", "PLAT", "PLAU"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "PAI-1/SERPINE1 has protease, vitronectin/integrin and receptor-trafficking contexts, but the listed rows do not resolve a single direct canonical receptor topology in the current graph layer."
                limitations = "Preserve active/cleaved PAI-1, vitronectin, uPA/tPA and LRP1/uPAR context; require exact pair-specific binding or receptor-triggering evidence before promoting ITGAV, PLAT or PLAU as direct signaling receptors."
            elif ligand in {"SIRPB1B", "SIRPB1C"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "SIRPB1B/C are cell-surface immunoreceptor-family proteins, not established soluble ligands for PTPRD in these candidate orientations."
                limitations = "Represent SIRPB1 paralogs in receptor and adaptor-complex orientation; require exact trans-interaction evidence before materializing a SIRPB1B/C-to-PTPRD edge."
            elif ligand in {"SLAMF6", "SLAMF7", "TARM1", "TCTN1", "TCTN3", "TEX101"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The candidate uses a membrane receptor, adhesion/ciliary component or cell-surface protein as the ligand label; the listed target is not established as its direct soluble-ligand receptor in this orientation."
                limitations = "Preserve membrane-protein cis/trans, adhesion and receptor-complex biology separately; require an exact extracellular interaction assay before promotion."
            elif ligand in {"SLURP1", "SLURP2"}:
                disposition = "hold_contextual_or_complex_boundary"
                primary = (
                    ["PMID:29192197", "PMCID:PMC5709491", "DOI:10.1038/s41598-017-16809-0", "PMID:24365495", "DOI:10.1016/j.jneuroim.2013.12.003"]
                    if ligand == "SLURP1" else
                    ["PMID:27485575", "DOI:10.1016/j.biochi.2016.07.011", "PMID:16575903", "PMID:25558396"]
                )
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; rat comparator"
                summary = "Primary studies support SLURP-family modulation of nicotinic acetylcholine receptor activity, but the public rows enumerate many individual subunits rather than a single validated receptor-complex topology."
                limitations = "Preserve SLURP1 alpha7/alpha3-beta4/alpha4-beta4/alpha3-beta2/alpha9-alpha10 and SLURP2 alpha3-beta2 or muscarinic context only where the assay supports it; do not promote every listed free subunit or infer a universal receptor complex."
            elif ligand == "SPINK1" and receptor == "EGFR":
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:36053457"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human"
                summary = "A primary cancer-cell study reports SPINK1-EGFR association and EGFR-linked ERK/p38/JNK and proliferation outputs, but this is not yet bounded as a canonical secreted ligand-binding mechanism in the graph."
                limitations = "Retain the reported cell-line and disease context; require extracellular binding, ligand-dependence and receptor-triggering assays before promoting SPINK1 as a conventional EGFR ligand."
            elif ligand == "SPON2" and receptor == "ITGB2L":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000891;M23B-E000882;M23B-E000883;M23B-E000884"
                primary = ["PMID:30910815", "PMID:16105980", "PMCID:PMC1895097", "DOI:10.1182/blood-2005-04-1658", "PMID:19153605", "PMCID:PMC6484411", "PMID:30869196"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse; human comparator"
                summary = "The graph contains primary-supported mindin/SPON2 binding and Mac-1 signaling, including Syk/MAPK and NF-kappaB-linked phagocytic outputs, but the tested receptor is the ITGAM:ITGB2 Mac-1 heterodimer rather than ITGB2L."
                limitations = "Retain ITGB2L as a receptor-component boundary candidate only; do not substitute ITGB2L for the tested ITGAM:ITGB2 complex or export a free beta subunit."
            elif ligand in {"SOCS2", "SORBS1", "SPTAN1", "SPTBN2", "STX1A", "SYT1"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The candidate ligand is an intracellular scaffold, signaling regulator or vesicle-exocytosis component, not a mature extracellular ligand for the listed membrane target."
                limitations = "Represent intracellular adaptor, trafficking and channel-coupling biology in receptor-proximal or intracellular layers; do not materialize these rows as secreted ligand-receptor edges."
            elif ligand.startswith("SULT") or ligand.startswith("SRD5A"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The candidate ligand is a steroid-metabolizing enzyme paired with a nuclear receptor/transcriptional regulator, not a conventional extracellular ligand-receptor interaction."
                limitations = "Represent steroid biosynthesis and nuclear-receptor activation as intracellular or non-protein signaling; do not materialize enzyme-to-PPAR or enzyme-to-AR rows as cell-surface ligand edges."
            elif ligand == "SST":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Somatostatin signaling is receptor-family specific, while the listed ADRA2A, GRM7 and MTNR1A targets are not established as direct somatostatin receptors in this candidate orientation."
                limitations = "Retain mature somatostatin-to-SSTR relationships only with exact receptor evidence; do not transfer specificity across unrelated GPCR families."
            elif ligand == "ST14" and receptor == "PLAU":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "ST14/matriptase is a membrane serine protease and PLAU/uPA is a protease substrate or pathway component; this row does not establish a mature ligand-receptor interaction."
                limitations = "Represent proteolytic processing and uPA/uPAR signaling separately; require direct extracellular receptor binding before promotion."
            elif ligand == "TDGF1" and receptor in {"LRP5", "LRP6"}:
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000350;M21B-E000351;M23B-E000266"
                primary = ["PMID:18089557", "PMID:11024047", "PMID:12649175"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human; mouse comparator"
                summary = "The graph supports TDGF1/Cripto as a NODAL coreceptor and contains a TDGF1-GPC1 association, but the listed LRP5/LRP6 rows are not established as direct TDGF1 receptor edges."
                limitations = "Preserve the NODAL-CRIPTO-ACVR1B/ACVR2B complex and TDGF1-GPC1 context; require exact TDGF1-LRP5/LRP6 binding or receptor-dependent function before promotion."
            elif ligand == "TFF3" and receptor in {"ACKR3", "CXCR4"}:
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M22B-E000696;M22B-E000697"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human comparator"
                summary = "The graph preserves TFF3-associated epithelial phenotypes and CXCR4/ACKR3 hypotheses, but receptor assignment remains unresolved and the current evidence is phenotype-only rather than a direct ligand-receptor demonstration."
                limitations = "Do not promote TFF3-ACKR3 or TFF3-CXCR4 as direct edges; preserve the negative or unresolved pharmacology and require pair-specific binding and receptor-dependence assays."
            elif ligand == "TFF2" and receptor == "MUC6":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "TFF2 and MUC6 are secreted epithelial products, but this row does not define MUC6 as a signaling receptor or establish a direct ligand-receptor mechanism."
                limitations = "Retain epithelial repair and mucin/trefoil co-expression separately; require a defined receptor and direct assay before graph materialization."
            elif ligand == "TFPI" and receptor == "F10":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "TFPI is a coagulation inhibitor and F10/factor Xa is a protease target, not a cell-surface receptor in this candidate orientation."
                limitations = "Represent protease inhibition and coagulation biochemistry separately from ligand-receptor signaling."
            elif ligand == "TGFA" and receptor in {"ADAM17", "ERBB2", "PTPRD"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "TGF-alpha has primary-supported EGFR binding, but the listed ADAM17, ERBB2 and PTPRD rows do not establish those proteins as direct TGFA signaling receptors."
                limitations = "Preserve TGFA-EGFR as the direct edge; represent ADAM17-mediated shedding and ERBB-family crosstalk separately, and do not infer receptor specificity from family membership."
            elif ligand == "TGFBI" and receptor in {"ITGA1", "ITGA4", "ITGA5", "ITGA6", "ITGA7", "ITGB4"}:
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E003059;M21B-E003060;M21B-E006604;M21B-E006605;M21B-E006606"
                primary = [
                    "PMID:36325910", "DOI:10.1161/CIRCULATIONAHA.121.058615",
                    "PMID:10906123", "DOI:10.1074/jbc.M002752200", "PMID:12074567",
                    "PMID:12270930", "DOI:10.1074/jbc.M207055200", "PMID:16672769", "DOI:10.1038/emm.2006.19",
                    "PMID:23792174", "DOI:10.1016/j.bbamcr.2013.06.012", "PMID:15899806", "DOI:10.1158/0008-5472.CAN-04-2705",
                ]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human; mouse; rat comparator"
                summary = "TGFBI has primary-supported stabilin uptake and integrin-complex adhesion contexts, but the listed free ITGA1/4/5/6/7 or ITGB4 subunits are not the exact receptor complexes tested in the graph."
                limitations = "Preserve STAB1/STAB2, ITGA3:ITGB1, ITGAV:ITGB5 and ITGAV:ITGB3 complex boundaries; do not substitute a free integrin subunit for the tested heterodimer or infer a universal TGFBI integrin receptor."
            elif ligand == "THBS1" and receptor == "SCARB1":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M23B-E000729"
                primary = ["PMID:40772900", "PMCID:PMC12665495", "DOI:10.1016/j.jacbts.2025.05.003"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "mouse; human comparator"
                summary = "The graph contains a primary-supported THBS1-SCARB1-associated endothelial inflammatory/fibrotic program, but the evidence is a receptor-associated functional context rather than a direct binary binding assay."
                limitations = "Retain the pressure-overload and endothelial-model context; do not promote SCARB1 as a universal direct THBS1 receptor or infer a terminal TF route."
            elif ligand == "TIGIT" and receptor == "NECTIN2":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E005461"
                primary = ["PMID:27978489", "PMCID:PMC5220579", "DOI:10.1016/j.molimm.2016.12.003"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human"
                summary = "The graph contains primary-supported Nectin-2/CD112-to-TIGIT binding in the reverse orientation of the public row."
                limitations = "Preserve Nectin-2 as ligand and TIGIT as receptor; do not add the reverse duplicate or infer a complete intracellular cascade from binding alone."
            elif ligand == "TIGIT" and receptor == "NECTIN4":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E006546"
                primary = ["PMID:32503945", "PMCID:PMC7279670"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "The graph contains primary-supported Nectin-4-to-TIGIT immune-checkpoint evidence in the reverse orientation of the public row."
                limitations = "Preserve Nectin-4 as ligand and TIGIT as receptor, including the NK/tumor-cell assay context; do not add a reverse duplicate."
            elif ligand == "TIGIT" and receptor == "PVR":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E000664"
                primary = ["PMID:22421438", "DOI:10.1016/j.molimm.2016.12.003"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human"
                summary = "The graph contains primary-supported PVR/CD155-to-TIGIT checkpoint binding in the reverse orientation of the public row."
                limitations = "Preserve PVR/CD155 as ligand and TIGIT as receptor; do not add the reverse duplicate or infer universal immune-cell outputs."
            elif ligand == "TIGIT":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "TIGIT is an immune checkpoint receptor, not a mature extracellular ligand for the listed targets in these orientations."
                limitations = "Represent PVR, Nectin-2 and Nectin-4 as ligands to TIGIT where directly supported; do not invert TIGIT receptor biology into ligand position."
            elif ligand in {"TIMD2", "TIMD4"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "TIMD2/TIMD4 are cell-surface TIM-family receptors or phagocytic components, not mature soluble ligands for the listed immune targets in these candidate orientations."
                limitations = "Represent TIM-family receptor, phosphatidylserine and phagocytic-complex biology in receptor orientation; require exact trans-ligand evidence before promotion."
            elif ligand == "THY1" and receptor in {"CNTN1", "GM49368", "ITGB2L"}:
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E005515;M21B-E005862;M23B-E000744;M23B-E000746;M23B-E000748"
                primary = ["PMID:22210915", "DOI:10.4049/jimmunol.1003944", "PMID:19723805", "PMCID:PMC2746130", "DOI:10.1242/jcs.034827", "PMID:23481656"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; rat comparator"
                summary = "The graph contains primary-supported THY1/CD90 adhesion and receptor-complex signaling through CD97, SDC4, Mac-1 and alphaVbeta3, but the listed CNTN1, GM49368 and ITGB2L targets are not the exact tested complexes."
                limitations = "Retain THY1 as an extracellular adhesion ligand with exact receptor-complex boundaries; do not substitute CNTN1, GM49368 or ITGB2L for the tested CD97, SDC4, ITGAM:ITGB2 or ITGAV:ITGB3 systems."
            elif ligand == "TNFRSF14" and receptor == "BTLA":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E003112"
                primary = ["PMID:16169851", "DOI:10.1074/jbc.M507629200"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human"
                summary = "The graph contains primary-supported BTLA-to-HVEM/TNFRSF14 binding in the reverse orientation of the public row."
                limitations = "Preserve BTLA as ligand and HVEM/TNFRSF14 as receptor; do not add the reverse duplicate or infer a complete inhibitory relay from extracellular binding alone."
            elif ligand == "TNFRSF14" and receptor == "CD160":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E000695"
                primary = ["PMCID:PMC7477951", "PMID:25179432", "PMCID:PMC4163173", "DOI:10.1186/s12967-014-0217-y"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "The graph contains primary-supported CD160-to-HVEM/TNFRSF14 binding in the reverse orientation of the public row."
                limitations = "Preserve CD160 as ligand and HVEM/TNFRSF14 as receptor, including isoform and cis/trans context; do not add the reverse duplicate."
            elif ligand == "TNFRSF14" and receptor == "TRAF2":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E001806"
                primary = ["PMID:9162022"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human"
                summary = "The graph supports HVEM/TNFRSF14 cytoplasmic recruitment of TRAF2, but the public row reverses a receptor-to-adaptor intracellular relationship into a ligand-receptor edge."
                limitations = "Retain HVEM cytoplasmic-tail and TRAF-adaptor topology; do not materialize TNFRSF14 as a soluble ligand or treat TRAF2 as an extracellular receptor."
            elif ligand == "TNFRSF14":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "TNFRSF14/HVEM is a membrane TNF-receptor-family protein, not a mature soluble ligand for the listed targets in these orientations."
                limitations = "Represent LIGHT, BTLA and CD160 interactions with HVEM/TNFRSF14 in their supported orientations; keep intracellular TRAF recruitment in receptor-proximal layers."
            elif ligand == "TNF" and receptor == "TRADD":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000017"
                primary = ["PMID:8565075", "PMID:16611992"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse comparator"
                summary = "The graph supports TNFR1-associated TRADD recruitment and NF-kappaB/death-branch signaling, but TRADD is an intracellular adaptor downstream of TNF receptor engagement rather than a direct extracellular TNF receptor."
                limitations = "Preserve TNF-TNFR1/TNFR2 and TNFR1-TRADD/TRAF2/FADD topology; do not materialize TNF-TRADD as a direct ligand-receptor edge."
            elif ligand == "TPSAB1" and receptor == "F2RL1":
                disposition = "hold_contextual_or_complex_boundary"
                primary = ["PMID:11606310", "PMID:9354658", "PMID:16470180", "PMID:30219079"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse comparator"
                summary = "Primary studies support mast-cell tryptase activation of PAR2/F2RL1 and calcium, mitogenic or migration outputs, but the public row uses the TPSAB1 gene label rather than a defined mature tryptase form."
                limitations = "Preserve mature tryptase processing, proteolytic PAR2 activation and mast-cell/tissue context; do not treat every TPSAB1 transcript or precursor form as an extracellular ligand without processing evidence."
            elif ligand == "TRAF2" and receptor == "TNFRSF1B":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000065;M21B-E000111"
                primary = ["PMID:7544915", "DOI:10.1126/science.7544915", "PMID:25152365", "PMID:11112773", "PMID:21081755"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse comparator"
                summary = "The graph supports TNFR2/TNFRSF1B-associated TRAF2 recruitment or NF-kappaB relay evidence, but TRAF2 is an intracellular adaptor downstream of TNFR2 rather than an extracellular ligand."
                limitations = "Preserve TNF-TNFR2 membrane/oligomerization context and TRAF2-dependent NF-kappaB branch; do not materialize TRAF2-TNFRSF1B as a direct ligand-receptor edge."
            elif ligand == "TRH" and receptor == "TRHR2":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E001693"
                primary = ["PMID:7487872", "PMID:8838148"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse; rat comparator"
                summary = "The graph contains primary-supported TRH activation of TRHR/type-1 receptor with calcium and PKC-linked outputs, but the public row specifies TRHR2 and the exact subtype assignment is not resolved here."
                limitations = "Preserve TRHR1 nomenclature, receptor subtype and pituitary/heterologous assay context; require exact TRHR2 evidence before promoting the subtype-specific edge."
            elif ligand in {"TSPAN3", "TSPAN33", "TSPAN5", "TXLNA", "TLN1", "TYROBP", "VSIR", "VSTM4", "WBP1"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The candidate ligand is a membrane organizer, intracellular adaptor, cytoskeletal/trafficking protein or immune-receptor adaptor rather than a mature extracellular ligand for the listed target."
                limitations = "Represent membrane-complex, cytoskeletal, vesicle-trafficking and adaptor biology in receptor-proximal or intracellular layers; do not materialize these rows as soluble ligand-receptor edges."
            elif ligand == "TRF":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Transferrin is a soluble carrier whose canonical receptor is TFRC; the listed HFE, LDLR and LRP2 targets do not establish these rows as direct transferrin signaling receptors."
                limitations = "Preserve transferrin-TFRC uptake and iron-transport biology separately; require exact receptor binding before promoting alternate receptor-family rows."
            elif ligand == "TTR" and receptor == "APOA1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "TTR and APOA1 are circulating carrier/apolipoprotein proteins, and this row does not define APOA1 as a cell-surface signaling receptor."
                limitations = "Represent transport, carrier and lipoprotein biology separately from ligand-receptor signaling."
            elif ligand == "VEGFB" and receptor == "FLT1+KDR":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000500"
                primary = ["PMID:9751730"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "Primary evidence supports VEGF-B binding and signaling through FLT1/VEGFR1, but the public row adds KDR as a composite receptor without exact VEGF-B-FLT1:KDR evidence."
                limitations = "Preserve VEGF-B isoform and FLT1 selectivity; do not promote the composite FLT1+KDR row or infer VEGFR2/KDR signaling from VEGF-family membership."
            elif ligand == "VEGFB" and receptor == "KDR":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000500;M21B-E000759"
                primary = ["PMID:9751730", "PMID:10409677"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human"
                summary = "The graph supports VEGF-B interaction with FLT1/VEGFR1 and NRP1 coreceptor context, but direct VEGF-B-to-KDR binding was not established in the reviewed evidence."
                limitations = "Require exact KDR binding or receptor-dependent activation before promotion; do not transfer VEGF-A/KDR evidence to VEGF-B."
            elif ligand == "VCAM1" and receptor in {"EZR", "ITGB2L", "MSN"}:
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000213;M21B-E000582;M21B-E000585;M21B-E000589"
                primary = ["PMID:7511143", "PMCID:PMC2290915", "PMID:8640376", "PMID:9841932", "PMID:10438935", "PMID:10209034"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse; rat comparator"
                summary = "The graph contains primary-supported VCAM1 adhesion through alpha4beta1, alpha4beta7, alphaDbeta2 and alpha9beta1 integrin complexes, but EZR/MSN are intracellular cytoskeletal proteins and ITGB2L is not the tested beta2 integrin complex."
                limitations = "Preserve assembled VCAM1-integrin topology and adhesion-state context; do not export a free beta subunit or treat EZR/MSN as extracellular VCAM1 receptors."
            elif ligand == "VEGFA":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "as stated in primary model/assay"
                summary = "VEGFA has well-established VEGFR and integrin/coreceptor signaling, but the listed EGFR, EPHB2, GRIN2B, RET, SIRPA and TYRO3 rows were not resolved as exact direct VEGFA receptor edges in this pass."
                limitations = "Retain exact VEGFR1/FLT1, VEGFR2/KDR, neuropilin and tested integrin-complex routes; do not transfer VEGFA family evidence to unrelated receptors or downstream targets."
            elif ligand == "VEGFC" and receptor in {"FLT1", "CCBE1", "LYVE1"}:
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M23B-E000781;M23B-E000782;M23B-E000783"
                primary = []
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse comparator"
                summary = "The graph supports VEGFC interaction with alpha9beta1 and a cooperating VEGFR3 branch, but the listed FLT1, CCBE1 and LYVE1 rows are not asserted as direct canonical VEGFC receptors here."
                limitations = "Preserve VEGFC-alpha9beta1 and VEGFR3 cooperation as separate branches; require exact pair-specific binding or activation before promoting the listed targets."
            elif ligand == "WNT10B" and receptor == "FZD6":
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E006146"
                primary = ["PMID:24873871", "DOI:10.1016/j.cellsig.2014.05.012"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human"
                summary = "The graph contains primary-supported WNT10B receptor-level action on FZD6 in a live-cell receptor-mobility assay."
                limitations = "Preserve the FZD6-GFP heterologous assay and mobility-based activation interpretation; do not infer a purified binary complex or terminal TF output."
            elif ligand == "WNT11" and receptor == "FZD1":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E005565;M21B-E006108;M21B-E006601;M21B-E006663"
                primary = ["PMID:29717114", "DOI:10.1038/s41467-018-04042-w", "PMID:39468010", "PMID:22309736", "PMID:10862746"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse; Xenopus comparator"
                summary = "The graph supports WNT11 signaling through FZD8, ROR2, MuSK/LRP4 and FZD7 branches, but the public FZD1 row is not an exact receptor assignment in the reviewed primary evidence."
                limitations = "Preserve the tested WNT11 receptor and complex topology; require direct WNT11-FZD1 evidence before promotion and do not transfer noncanonical WNT receptor specificity across Frizzled paralogs."
            elif ligand == "VWF" and receptor in {"ITGA4", "ITGA9", "ITGB1"}:
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M23B-E000281;M23B-E000453;M23B-E000454;M23B-E000455"
                primary = ["PMID:2104618", "PMCID:PMC1895591", "PMID:7523416"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse comparator"
                summary = "The graph supports VWF binding to the multimeric GPIb-IX-V complex and platelet alphaIIbbeta3 cooperation, but the listed free integrin subunits are not established as independent VWF receptors."
                limitations = "Preserve the multimeric platelet receptor and integrin-cooperation topology; do not export free ITGA4, ITGA9 or ITGB1 edges from platelet-complex evidence."
            elif ligand == "VWF" and receptor in {"ADAMTS13", "F8", "SIRPA"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The listed VWF target is a coagulation protease/cofactor or immune receptor, not an established direct VWF cell-surface receptor in this candidate orientation."
                limitations = "Represent VWF cleavage, factor-VIII carriage and platelet receptor binding separately; require exact receptor-level evidence before promotion."
            elif ligand.startswith("SIGLEC") or ligand in {"SIRPA", "SIRPB1A"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "SIGLEC and SIRP proteins are cell-surface immunoreceptor-family proteins, not mature extracellular ligands for the listed targets in these candidate orientations."
                limitations = "Represent sialylated-ligand/SIGLEC and CD47/SIRP cis/trans interactions in receptor orientation; do not invert SIGLEC or SIRP receptors into ligand position."
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
            elif ligand == "WNT3A":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000155;M21B-E000156;M21B-E003250"
                primary = ["PMID:20093360", "PMCID:PMC2838336"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human; mouse"
                summary = "The graph contains primary-supported WNT3A binding to FZD8 and LRP6, including the ternary WNT-FZD8-LRP6 assembly, but the candidate packet also contains receptor and co-receptor combinations that were not verified as the same complete topology."
                limitations = "Preserve the WNT3A-FZD8-LRP6 complex boundary and ectodomain assay context; do not transfer the exact WNT3A evidence to other Frizzled, LGR5, ROR1 or ATP6AP2 rows without pair-specific evidence."
            elif ligand == "WNT3":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E007082"
                primary = ["PMID:31036956", "DOI:10.1038/s41594-019-0216-z"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human; mouse"
                summary = "The graph contains a primary-supported WNT3-FZD8 ectodomain structure, while the candidate packet includes additional Frizzled and LRP6 rows that were not verified as the same direct binary or productive receptor complex."
                limitations = "Retain the WNT3-FZD8 cysteine-rich-domain and 2:2 structural context; do not infer whole-cell activation, LRP6 recruitment or cross-paralog receptor specificity."
            elif ligand == "WNT5A":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000472;M21B-E000981;M21B-E005445;M21B-E005446;M21B-E005448;M21B-E005449;M21B-E005450"
                primary = [
                    "PMID:12839624",
                    "PMID:17804197",
                    "DOI:10.1016/j.cellsig.2007.07.023",
                    "PMID:26499793",
                    "PMCID:PMC4683276",
                    "PMID:24335906",
                    "DOI:10.1038/ncomms3803",
                    "PMID:16723543",
                    "PMCID:PMC6675257",
                    "PMID:18287027",
                    "PMID:19910923",
                    "PMCID:PMC2808370",
                ]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse; Xenopus"
                summary = "The graph contains primary-supported WNT5A interactions with ROR2, FZD3, FZD2, PTK7, CD146/MCAM, RYK and ROR1, with bounded noncanonical pathway or functional readouts; the candidate packet contains additional receptor rows not verified as those exact edges."
                limitations = "Use the matched WNT5A receptor contexts as bounded evidence only; preserve ROR/PTK7/co-receptor, cell-model and noncanonical pathway distinctions, and do not transfer WNT5A evidence across unrelated receptor paralogs."
            elif ligand == "WNT5B":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M23B-E000282"
                primary = ["DOI:10.1186/s12964-020-00646-2", "PMCID:PMC7487719", "PMID:31907106"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human"
                summary = "Primary evidence in the graph supports a WNT5B-associated FZD7 noncanonical signaling context, but WNT5A/B co-immunoprecipitation does not isolate the WNT5B contribution and the candidate packet expands to many composite FZD-LRP5/6 rows."
                limitations = "Retain the WNT5B-FZD7 contextual boundary and unresolved co-ligand attribution; do not promote composite FZD-LRP5/6 rows or infer a direct WNT5B binary edge without pair-specific evidence."
            elif ligand == "WNT7A":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000955;M21B-E000957"
                primary = ["PMID:30304675", "PMCID:PMC6338448", "PMID:40914247", "PMCID:PMC12514574", "DOI:10.1016/j.jbc.2025.110682"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse; rat"
                summary = "The graph contains primary-supported WNT7A interaction with RECK and the GPR124/RECK/LRP5/6 co-receptor complex, including bounded vascular Wnt signaling readouts; the candidate packet includes receptor rows outside that complete topology."
                limitations = "Preserve RECK and GPR124/ADGRA2 co-receptor composition, LRP5/6 context and vascular model boundaries; do not transfer WNT7A evidence to isolated LDLR, FZD9 or LRP6 rows as standalone receptors."
            elif ligand == "WNT7B":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000956;M21B-E000958;M21B-E007023;M21B-E007024"
                primary = ["PMID:30304675", "PMCID:PMC6338448", "PMID:40914247", "PMCID:PMC12514574", "DOI:10.1016/j.jbc.2025.110682", "PMID:15923619", "PMCID:PMC1140585", "DOI:10.1128/MCB.25.12.5022-5030.2005"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse; rat"
                summary = "The graph contains primary-supported WNT7B interaction with RECK, the GPR124/RECK/LRP5/6 complex, and FZD1/FZD10 with cooperative LRP5-dependent canonical readouts; other packet rows were not verified as the same topology."
                limitations = "Preserve the FZD1/FZD10-LRP5 or GPR124/RECK/LRP5/6 complex boundaries and vascular/developmental model context; do not promote isolated FZD2-FZD7 rows or LDLR/LRP6 substitutions without exact evidence."
            elif ligand == "WNT11":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E005565"
                primary = ["PMID:29717114", "PMCID:PMC5931552", "DOI:10.1038/s41467-018-04042-w"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human"
                summary = "The graph contains primary-supported WNT11-FZD8 association with bounded ATF2/AP-1, migration and invasion readouts, while the candidate packet includes LRP6 and other receptor-family rows without verification of the same receptor topology."
                limitations = "Preserve the WNT11-FZD8 co-immunoprecipitation and prostate-cancer noncanonical context; do not transfer it to LRP6 or unrelated Frizzled paralogs, and do not infer a universal TF route."
            elif ligand == "XCL1" and receptor == "ADGRV1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                species = "as stated in primary model/assay"
                summary = "XCL1 is a chemokine ligand, but ADGRV1 is an adhesion GPCR and an exact XCL1-ADGRV1 binding or receptor-activation experiment was not verified in this pass."
                limitations = "Require direct XCL1-ADGRV1 binding or receptor-dependent function before promotion; do not transfer canonical chemokine-receptor specificity to an adhesion GPCR."
            elif ligand == "YBX1" and receptor == "NOTCH1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "YBX1 is an intracellular RNA/DNA-binding protein and is not treated as a mature extracellular ligand for NOTCH1 in this candidate row."
                limitations = "Represent intracellular YBX1 and Notch pathway biology separately; require an exact extracellular ligand or receptor-proximal assay before materializing a ligand-receptor edge."
            elif ligand == "ZDHHC5" and receptor == "S1PR1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "ZDHHC5 is an intracellular palmitoyltransferase rather than a mature extracellular ligand for S1PR1."
                limitations = "Represent protein palmitoylation and S1PR1 signaling separately; do not materialize enzyme-to-receptor rows as direct ligand-receptor edges."
            elif ligand == "ZNRF3":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "ZNRF3 is a membrane-associated E3 ubiquitin ligase and Wnt-receptor turnover regulator, not a mature secreted ligand for the listed Frizzled or LRP6 rows."
                limitations = "Represent ZNRF3/RNF43 regulation of Wnt receptor availability separately; do not materialize regulator-to-receptor rows as direct ligand-receptor edges."
            elif ligand == "ZPBP2" and receptor == "CD80":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "ZPBP2 is an intracellular/sperm-associated protein and is not treated as a mature extracellular ligand for CD80."
                limitations = "Require an exact extracellular binding or receptor-dependent functional assay before graph promotion; do not infer CD80 activity from co-expression or tissue association."
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
            elif ligand == "KLK5" and receptor == "F2RL1":
                disposition = "new_primary_supported_edge_candidate"
                primary = ["PMID:20703245", "DOI:10.1038/jid.2010.233"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse"
                summary = "Primary Netherton-syndrome mouse work identifies unrestricted KLK5 activity as a direct activator of PAR2/F2RL1 and shows that Par2 deletion reduces the downstream TSLP output."
                limitations = "Promote only as a bounded protease-activated receptor route; the cited study establishes functional activation and a TSLP readout rather than a purified cleavage biochemistry, SCI transfer or a terminal-TF claim."
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
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E005465"
                primary = ["PMID:17580308", "DOI:10.1074/jbc.M701120200"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "The graph already contains the primary-supported CD177-to-PECAM1/CD31 heterophilic adhesion and transmigration relationship in the reverse orientation of the public row."
                limitations = "Preserve CD177/PECAM1 direction and neutrophil-transendothelial context; do not add a duplicate PECAM1-to-CD177 edge or infer a universal intracellular relay."
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
            elif ligand.startswith("SHMT") and receptor == "GLRA2":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row combines serine-hydroxymethyltransferase enzymes with glycine transporters in ligand position; mature glycine, not SHMT/SLC6 composite machinery, is the ligand for GLRA2/glycine-receptor signaling."
                limitations = "Represent glycine biosynthesis and transport separately; do not materialize enzyme/transporter composites as direct GLRA2 ligand edges."
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
            elif ligand == "ADGRE5" and receptor == "CD55":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E000945"
                primary = ["PMID:9064337", "PMCID:PMC2192782", "DOI:10.1084/jem.184.3.1185"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "The graph contains the primary-supported CD55/DAF-to-ADGRE5/CD97 cell-adhesion relationship in the reverse orientation of this public row."
                limitations = "Preserve ADGRE5 EGF-repeat and CD55/DAF adhesion context; do not add a duplicate reverse edge or infer a universal intracellular signaling route."
            elif ligand == "ALCAM" and receptor == "ALCAM":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                primary = []
                species = "as stated in primary model/assay"
                summary = "ALCAM is a cell-adhesion molecule with homophilic and heterophilic binding contexts, but the public self-pair is not materialized as a graph self-loop."
                limitations = "Retain exact ALCAM adhesion and receptor-complex evidence separately; do not encode an ALCAM self-loop or infer a unique intracellular relay from adhesion alone."
            elif ligand.startswith("ALDH1A"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "ALDH1A-family labels are retinoid-metabolizing enzymes; the composite rows with CRABP/RAR/RXR or RORB do not represent a mature extracellular ligand acting on those receptors."
                limitations = "Represent retinoic-acid production and nuclear-receptor activation only when the mature retinoid, receptor and primary assay are explicit; do not materialize enzyme-to-receptor composites as ligand edges."
            elif ligand == "ALKAL1" and receptor == "ALK":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = ["PMID:34646012", "PMID:25331893", "DOI:10.1073/pnas.1412009111"]
                species = "human"
                summary = "Primary structure-function work supports ALKAL1/FAM150A engagement of the ALK-family receptor system, including ALK-complex formation, while an independent extracellular-proteome screen establishes ALKAL1 as a high-affinity activating ligand for the related LTK receptor."
                limitations = "Treat ALKAL1-ALK as a bounded receptor-complex candidate with receptor-preference and assay-context constraints; do not equate it with the stronger ALKAL2-ALK activation route or infer a complete intracellular/TF chain."
            elif ligand == "ALOX5AP" and receptor == "ALOX5":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "ALOX5AP and ALOX5 are intracellular 5-lipoxygenase-complex components, not an extracellular ligand and cell-surface receptor pair."
                limitations = "Represent the 5-lipoxygenase complex and leukotriene production in intracellular or metabolic layers; do not materialize the protein-complex association as a ligand-receptor edge."
            elif ligand.startswith("ANG"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Angiopoietin/angiopoietin-like and angiogenin-family labels are heterogeneous, and the public rows do not resolve the exact mature ligand form and receptor assay for the listed candidates."
                limitations = "Require exact ANG/ANGPTL protein identity, receptor topology, species and primary binding or functional assay; do not transfer evidence across angiopoietin, angiopoietin-like or angiogenin paralogs."
            elif ligand == "ANTXR1" and receptor == "TREML2":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "ANTXR1 is a membrane anthrax-toxin receptor and the current pass did not verify an exact ANTXR1-to-TREML2 ligand-receptor experiment."
                limitations = "Retain ANTXR1 toxin-binding biology and exact TREML2 interactions separately; do not promote the database-only pair without a direct primary assay."
            elif ligand == "ANXA1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Annexin A1 has established FPR1/FPR2 and membrane-associated contexts, but the listed adrenergic, glutamatergic and melatonin receptors were not verified as direct ANXA1 receptor pairs."
                limitations = "Require exact ANXA1 form, receptor, species and primary binding or activation assay; do not transfer FPR-family evidence to unrelated GPCRs."
            elif ligand == "ANXA2":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Annexin A2 participates in plasminogen/tPA, membrane and cofactor interactions, but the public rows do not establish a conventional mature-ligand receptor edge for DYSF, EGFR or PLAT."
                limitations = "Retain exact ANXA2 membrane, plasminogen and receptor-proximal mechanisms; do not materialize enzyme, substrate or cofactor relationships as direct ligand-receptor edges without an exact assay."
            elif ligand == "APLN":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Apelin/APLN receptor biology is centered on APLNR/APJ, not the unrelated adrenergic or melatonin receptors listed in these rows."
                limitations = "Require mature apelin isoform and direct APLNR assay; do not transfer APLN/APLNR specificity to unrelated GPCRs."
            elif ligand == "APOA1" and receptor == "AMN+CUBN":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "APOA1 and the cubilin/amnionless complex are linked to lipoprotein uptake and trafficking contexts, but the public composite does not provide an exact mature-ligand receptor assay for this graph edge in the current pass."
                limitations = "Preserve the intact CUBN:AMN uptake complex and lipoprotein context; do not collapse uptake/cofactor biology into a generic signaling receptor edge without direct primary support."
            elif ligand in {"APOA5", "APOC1", "APOC2", "APOC3", "APOE"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Apolipoprotein-family rows can represent lipoprotein uptake, cofactor, competition or inflammatory contexts, but the exact mature apolipoprotein form and receptor mechanism are not resolved for this candidate."
                limitations = "Require exact apolipoprotein form, receptor or uptake complex, species and primary binding or functional assay; do not transfer APOA/APOC/APOE evidence across receptor families or treat LPL/cofactor interactions as canonical signaling edges."
            elif ligand == "APOB" and receptor == "APOBR":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "APOB/APOBR is a plausible lipoprotein-receptor relationship, but the current candidate row lacks a verified exact primary locator and is retained pending pair-specific confirmation."
                limitations = "Require direct APOB100/APOBR binding or receptor-dependent functional evidence with the mature lipoprotein form; do not promote from family-level apolipoprotein or uptake annotations alone."
            elif ligand == "APOB":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The remaining APOB rows are lipoprotein, enzyme, transporter or receptor-context predictions rather than verified direct APOB ligand-receptor edges in this pass."
                limitations = "Retain exact APOB100/LDLR, APOB/TREM2 and other primary-supported lipoprotein contexts separately; do not transfer them to unrelated candidate targets."
            elif ligand == "APOO":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "APOO is a mitochondrial protein label, not a mature extracellular ligand for IL1RAPL1."
                limitations = "Represent mitochondrial protein interactions separately; do not materialize APOO-to-IL1RAPL1 as a ligand-receptor edge without exact primary support."
            elif ligand == "APP" and receptor == "ADRA2A":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The current pass did not verify an exact APP-to-ADRA2A ligand-receptor or receptor-triggering experiment."
                limitations = "Retain APP processing and exact APP receptor/cofactor evidence separately; do not infer an adrenergic receptor route from database co-membership."
            elif ligand == "APP":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "APP is a membrane protein and proteolytic-adhesion signaling substrate with several binding partners, but the public rows do not establish the listed targets as direct mature-ligand receptors in this pass."
                limitations = "Retain exact APP processing, adhesion and receptor/cofactor evidence separately; do not transfer APP-family interactions across unrelated targets or infer a canonical extracellular ligand route from database membership."
            elif ligand == "AREG" and receptor == "MMP9":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "AREG is an EGFR ligand, whereas MMP9 is a protease and not a receptor in the public row."
                limitations = "Represent EGFR activation and MMP9-mediated shedding or matrix remodeling in their appropriate layers; do not materialize AREG-to-MMP9 as a ligand-receptor edge."
            elif ligand.startswith(("ARF", "ARPC")):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "ARF and ARPC-family labels are intracellular trafficking or actin-complex components, not extracellular ligands for the listed membrane proteins."
                limitations = "Represent intracellular trafficking and cytoskeletal mechanisms separately; do not materialize the database row as a ligand-receptor edge."
            elif ligand == "ARMH4":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The current pass did not verify ARMH4 as a mature extracellular ligand or an exact ARMH4-to-TNFRSF11B receptor interaction."
                limitations = "Retain for targeted primary review; do not promote an edge from public-database membership alone."
            elif ligand == "ARTN" and receptor == "NCAM1":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "Artemin is established in GFRalpha3/RET neurotrophic receptor contexts, but an exact ARTN-to-NCAM1 receptor assay was not verified in this pass."
                limitations = "Require direct ARTN/NCAM1 binding or receptor-dependent functional evidence; do not transfer GFRalpha3/RET specificity to NCAM1."
            elif ligand == "ATP1B1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "ATP1B1 is a membrane Na/K-ATPase subunit, not a mature extracellular ligand for NEGR1."
                limitations = "Represent Na/K-ATPase and adhesion-complex biology separately; do not materialize ATP1B1-to-NEGR1 as a ligand-receptor edge without exact primary support."
            elif ligand == "AU040320":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "AU040320 is an unresolved gene/protein label in this candidate snapshot, and no exact mature-ligand identity or receptor assay was verified."
                limitations = "Resolve the entity identifier and protein form before any evidence promotion; do not infer receptor specificity from the public prediction alone."
            elif ligand == "AVP":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Arginine vasopressin receptor biology is centered on AVPR1A, AVPR1B and AVPR2, not the unrelated receptors listed in these rows."
                limitations = "Require mature AVP and direct AVPR-family assay; do not transfer vasopressin specificity to ADCYAP1R1, adrenergic, PTH, RAMP or transporter candidates."
            elif ligand == "B2M":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "B2M is a class-I MHC component and beta-2-microglobulin-associated extracellular protein, not a generic mature ligand for the listed immune, transporter or T-cell components."
                limitations = "Represent exact MHC-I assembly and immune-recognition interactions separately; do not materialize B2M-to-receptor rows from family or pathway membership alone."
            elif ligand in {"BACE1", "BACE2"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "BACE1/BACE2 are intracellular or membrane-associated proteases; the public rows describe enzyme-substrate or processing contexts rather than mature ligand-receptor edges."
                limitations = "Represent APP and other substrate processing in a receptor-proximal or intracellular layer; do not materialize protease-to-substrate rows as ligand-receptor edges."
            elif ligand == "BC053393":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "BC053393 remains an unresolved public identifier in this pass, with no verified mature extracellular ligand identity or exact receptor assay."
                limitations = "Resolve the identifier and protein form before promotion; do not infer specificity across CD300, IGSF or SIGLEC families."
            elif ligand == "BDNF" and receptor == "GPR152":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "BDNF signaling is established through TrkB/NTRK2 and p75NTR contexts, but an exact BDNF-to-GPR152 receptor experiment was not verified in this pass."
                limitations = "Require direct BDNF/GPR152 binding or receptor-dependent function; do not transfer TrkB/p75NTR specificity to GPR152."
            elif ligand == "BGN":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Biglycan is an extracellular matrix proteoglycan with context-dependent innate-receptor signaling, but the public rows do not resolve an exact BGN-to-FGFR3 or BGN-to-LY96 direct receptor mechanism."
                limitations = "Retain exact biglycan/TLR or matrix-receptor evidence separately; do not transfer proteoglycan-family signaling to unrelated receptor candidates without a direct primary assay."
            elif ligand.startswith("BMP"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "BMP-family rows overlap known type-I/type-II receptor and SMAD signaling, but the public candidates do not resolve the exact mature BMP form, receptor complex and pair-specific primary assay for each listed target."
                limitations = "Retain exact BMP-to-receptor and BMP-to-complex evidence already present in the graph; do not transfer receptor specificity across BMP paralogs or collapse a multi-subunit complex into an unsupported binary edge."
            elif ligand == "BOC":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "BOC is a cell-surface Hedgehog co-receptor/adhesion protein, not a mature extracellular ligand for LILRA6, PTCH1, PTCH2 or SMO."
                limitations = "Represent BOC as a co-receptor in Hedgehog signaling when directly supported; do not materialize BOC-to-receptor rows as ligand edges."
            elif ligand == "BSG":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "BSG/CD147 is a membrane immunoglobulin-superfamily protein and chaperone for monocarboxylate transporters, not a soluble ligand for SLC16A1 or SLC16A7."
                limitations = "Represent BSG-MCT complex biology separately; do not materialize receptor/transporter complex associations as ligand-receptor edges."
            elif ligand == "BST1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "BST1 is an ectoenzyme and cell-surface protein, not a verified soluble ligand for CAV1 in this row."
                limitations = "Require direct BST1/CAV1 binding or receptor-dependent function before promotion; do not infer an edge from membrane co-localization or database membership."
            elif ligand == "BST2":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "BST2/tetherin is a membrane antiviral and immune-regulatory protein, but the public rows do not establish the listed LILRA/PIRA paralogs as its direct receptor pair."
                limitations = "Require exact BST2 receptor identity, species and primary binding or functional assay; do not transfer evidence among LILRA/PIRA paralogs."
            elif ligand == "BTLA":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "BTLA is an immune-checkpoint membrane protein with established HVEM/TNFRSF14 context, but the public rows do not verify CD276 or VTCN1 as its direct receptor pair."
                limitations = "Require exact BTLA ligand/receptor orientation, species and primary binding or functional assay; do not transfer HVEM or B7-family evidence across checkpoint paralogs."
            elif ligand == "BTN1A1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "BTN1A1/JAML is a plausible cell-adhesion or immune-complex relationship, but the current candidate row lacks a verified exact primary locator and is retained as contextual pending pair-specific review."
                limitations = "Require direct BTN1A1/JAML binding or receptor-dependent function with exact orientation and species; do not infer a general butyrophilin-family interaction."
            elif ligand.startswith("BTNL"):
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "Butyrophilin-like family membership does not establish the listed IL6RA or LRFN5 targets as direct receptors for BTNL9 in this pass."
                limitations = "Require exact BTNL9 receptor identity and primary binding or functional assay; do not transfer evidence across butyrophilin-like paralogs."
            elif ligand.startswith("C1Q"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "C1Q-family complement and collectin proteins have context-dependent immune, phagocytic and matrix interactions, but the public rows do not resolve exact mature C1Q-chain forms and receptor mechanisms for each target."
                limitations = "Require exact C1Q isoform or assembled ligand, receptor, species and primary assay; do not transfer C1Q, complement-receptor or collagen-like-domain evidence across paralogs."
            elif ligand in {"C3", "C4A", "C4B"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "C3/C4A/C4B labels are complement precursor or mature-fragment families; the public rows do not specify the processed complement ligand form required for a direct receptor edge."
                limitations = "Require exact mature C3a/C3b/C4a or C4b form, receptor identity and primary assay; do not materialize precursor-to-receptor rows or transfer specificity across complement fragments."
            elif ligand == "C4BP":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "C4BP is a complement-regulatory protein and the current pass did not verify an exact C4BP-to-BMPR2 ligand-receptor experiment."
                limitations = "Retain complement-regulatory and extracellular-matrix context separately; do not promote a database-only BMPR2 pair."
            elif ligand == "C920025E04RIK":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "C920025E04RIK remains an unresolved public identifier in this pass, with no verified mature ligand identity or direct CD8A/CD8B1 receptor assay."
                limitations = "Resolve the identifier and protein form before promotion; do not infer receptor specificity from database membership alone."
            elif ligand.startswith("CADM"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "CADM family rows describe cell-adhesion and trans-interaction contexts, but the public candidates do not establish each exact CADM paralog pair or the listed ERBB3, MAG and unrelated targets as a single direct signaling edge."
                limitations = "Preserve cis/trans orientation and paralog specificity; require exact pair-level primary adhesion or receptor-triggering evidence before promotion, and do not infer a soluble ligand route from adhesion-family membership."
            elif ligand == "CALCB" and receptor in {"CALCR+RAMP1", "CALCR+RAMP2", "CALCR+RAMP3"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:30741933", "PMID:18599553"]
                species = "human"
                summary = "Primary Ewing-sarcoma work supports a secreted CALCB signal through a RAMP1-containing CGRP receptor complex, while receptor-pharmacology work shows that RAMP composition changes family-B receptor coupling; the public CALCR:RAMP composite rows do not resolve the exact CALCRL/CALCR core topology."
                limitations = "Retain CALCB/RAMP1 and receptor-complex evidence as a bounded route; do not promote CALCR:RAMP1/2/3 as one exact binary receptor topology or infer identical signaling across RAMP compositions."
            elif ligand == "CBR1+CBR1B" and receptor == "PTGFR":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "CBR1/CBR1B are carbonyl-reductase enzymes, not mature prostaglandin ligands for the PTGFR receptor."
                limitations = "Represent prostaglandin synthesis and metabolism separately; do not materialize enzyme composites as direct PTGFR ligand edges."
            elif ligand in {"CALCA", "CALCB"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Calcitonin/CGRP-family biology is receptor-complex dependent, while the public rows do not resolve the mature peptide form and complete CALCR, CALCRL or RAMP composition for each listed target."
                limitations = "Require mature CALCA/CALCB peptide, exact receptor-complex composition, species and primary binding or activation assay; do not transfer CGRP, calcitonin or amylin receptor specificity across paralogs and RAMPs."
            elif ligand.startswith("CALM") or ligand == "CALML3":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Calmodulin and calmodulin-like proteins are intracellular signaling components, not extracellular ligands for the listed channels, enzymes or kinases."
                limitations = "Represent calmodulin-dependent intracellular regulation separately; do not materialize protein-complex associations as ligand-receptor edges."
            elif ligand == "CALR":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "CALR/calreticulin is primarily an endoplasmic-reticulum chaperone and immune-surface context protein, not a mature ligand for TAP1/TAP2."
                limitations = "Represent calreticulin, MHC-I assembly and antigen-processing mechanisms in their appropriate layers; do not materialize CALR-to-TAP rows as ligand-receptor edges."
            elif ligand == "CAMP" and receptor == "FPR3":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "Antimicrobial peptide/CAMP signaling has receptor-specific and processed-peptide context, but an exact CAMP-to-FPR3 receptor experiment was not verified in this pass."
                limitations = "Require exact mature CAMP peptide and direct FPR3 binding or activation evidence; do not transfer FPR1/FPR2 or unrelated chemotactic receptor evidence to FPR3."
            elif ligand == "CAR12":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "CAR12/CA12 is a membrane carbonic-anhydrase protein, not a mature extracellular ligand for the listed immune receptors."
                limitations = "Represent carbonic-anhydrase and membrane-complex biology separately; do not materialize CAR12-to-CD33/SIGLEC rows without exact primary support."
            elif ligand.startswith("CCL19PS"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "CCL19PS1 is a pseudogene-like public label and is not treated as a verified mature chemokine ligand for ACKR, CCR or CXCR receptors."
                limitations = "Resolve the expressed chemokine product and mature form before review; do not transfer CCL19/CCR7 evidence to a pseudogene label."
            elif ligand == "CCL5" and receptor == "ACKR2":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = ["PMID:17095748", "PMID:29469612"]
                species = "mouse"
                summary = "Primary ACKR2/D6 studies support a chemokine-scavenging and inflammatory-context relationship for CCL5, but also show concentration- and tissue-dependent effects; this is contextual scavenging evidence, not a canonical G-protein signaling edge."
                limitations = "Preserve ACKR2 as an atypical scavenger receptor and retain the mouse lung/fibrosis context; do not infer conventional chemotaxis, intracellular relay or terminal-TF output from CCL5 abundance changes alone."
            elif ligand == "CCL24" and receptor == "ACKR2":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                primary = ["PMID:17095748", "PMCID:PMC1899265"]
                species = "mouse"
                summary = "Primary D6/ACKR2 work establishes concentration-dependent chemokine scavenging and receptor-family context, but the cited experiments do not verify a direct CCL24-ACKR2 interaction; the candidate remains a bounded search hold."
                limitations = "Require an exact CCL24-D6 binding or internalization assay before promotion; do not transfer CCL17/CCL22 or other CC-chemokine evidence to CCL24 without isoform-specific support."
            elif ligand.startswith("CCL"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Chemokine-family candidates can involve signaling, scavenging or atypical-receptor contexts, but the public rows do not establish the exact mature chemokine form and receptor mechanism for each listed pair."
                limitations = "Require exact CCL isoform, receptor orientation, species and primary binding or functional assay; do not transfer canonical CCR specificity to ACKR, CCRL or CXCR paralogs without pair-specific evidence."
            elif ligand.startswith("CCN"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "CCN matricellular proteins can bind integrins, growth-factor receptors and extracellular-matrix partners, but the public rows do not establish the exact CCN isoform, receptor complex and pair-specific primary mechanism for each candidate."
                limitations = "Require exact CCN form, receptor subunit composition, species and primary binding or functional assay; do not transfer integrin, FGFR, ERBB or LRP-family evidence across CCN paralogs or collapse matrix/co-receptor context into a binary edge."
            elif ligand == "CD14":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "CD14 is a GPI-anchored innate immune co-receptor and pattern-recognition component, not a mature extracellular ligand for the listed integrins, PLXND1, RIPK1 or TLR subunits."
                limitations = "Represent CD14-containing innate receptor complexes and co-receptor function separately; do not materialize CD14-to-target rows as ligand edges without exact primary support."
            elif ligand.startswith("CD209"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "CD209-family proteins are membrane C-type lectin receptors, not soluble ligands for CEACAM-family targets in these rows."
                limitations = "Represent lectin receptor binding and cis/trans immune-complex biology separately; do not materialize CD209-to-CEACAM rows as ligand-receptor edges without direct primary support."
            elif ligand == "CD226":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "CD226 is an immune adhesion/co-receptor with known PVR/CD155 and Nectin-2 context, but the public rows do not resolve the exact trans-interaction orientation or establish MCAM as a direct CD226 ligand/receptor partner."
                limitations = "Preserve CD226/PVR-family orientation and immune-cell context; require exact MCAM or PVR-family primary assay before promotion and do not infer a soluble ligand route."
            elif ligand in {"CD22", "CD244A", "CD24A", "CD274", "CD28"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "The candidate uses a membrane immune-receptor or checkpoint protein as the ligand label, but the listed target does not have a verified exact pair-specific primary interaction in this pass."
                limitations = "Require exact ligand/receptor orientation, receptor-complex composition, species and direct primary assay; do not transfer checkpoint, adhesion or intracellular adaptor evidence across immune-protein paralogs."
            elif ligand == "CD40" and receptor == "CD40LG":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E000679"
                primary = ["PMID:21285457", "PMCID:PMC3064178", "DOI:10.1073/pnas.1016567108", "PMID:7664782"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "human"
                summary = "The graph contains the primary-supported CD40LG/CD154-to-CD40 costimulatory interaction in the reverse orientation of the public row."
                limitations = "Preserve CD40LG as ligand and CD40/TNFRSF5 as receptor; do not add a duplicate reverse edge or infer a complete terminal-TF route from receptor engagement alone."
            elif ligand == "CD96" and receptor == "NECTIN1":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E005534"
                primary = ["PMID:17971293", "PMCID:PMC6373967", "DOI:10.1371/journal.pone.0191588"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "The graph contains primary-supported Nectin-1/CD111-to-CD96/TACTILE immune-adhesion evidence in the reverse orientation of the public row."
                limitations = "Preserve Nectin-1 as the adhesion ligand and CD96 as the receptor; do not add a duplicate reverse edge or infer a unique intracellular relay from adhesion alone."
            elif ligand in {"CD44", "CD59A", "CD59B", "CD79B", "CD82", "CD9"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses a membrane adhesion, complement-regulatory, B-cell-receptor or tetraspanin protein as the ligand label, but the listed target is not established as its direct mature-ligand receptor in this pass."
                limitations = "Represent exact cis/trans adhesion, receptor-complex and membrane-organizer mechanisms separately; do not materialize membrane-protein associations as soluble ligand-receptor edges without exact primary support."
            elif ligand == "CD47":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "CD47 has primary-supported SIRPA/SIRPG and integrin-associated checkpoint contexts, but the public rows target SIRPB paralogs and unrelated proteins for which exact pair-specific evidence was not verified here."
                limitations = "Preserve CD47/SIRPA and CD47/SIRPG orientation and receptor-family specificity; do not transfer evidence to SIRPB or unrelated targets without direct primary support."
            elif ligand == "CD48":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "CD48 is a GPI-anchored immune adhesion ligand with receptor-family-specific interactions, but an exact CD48-to-PDCD1 primary experiment was not verified in this pass."
                limitations = "Require direct CD48/PDCD1 binding or receptor-dependent function; do not transfer CD2-family adhesion evidence to PDCD1."
            elif ligand == "CD6":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "CD6 is an immune receptor with established ALCAM/CD166 and CD318 contexts, but the listed DAG1 and SIGLEC targets were not verified as direct CD6 receptor partners in this pass."
                limitations = "Preserve CD6 receptor orientation and known adhesion/costimulation partners; do not transfer evidence across SIGLEC or dystroglycan families."
            elif ligand == "CD70":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "CD70 is established as the ligand for CD27/TNFRSF7, but the listed TNFRSF13B and TNFRSF17 targets were not verified as direct CD70 receptor pairs."
                limitations = "Require exact CD70 receptor identity and primary binding or activation assay; do not transfer CD27, BAFF-R or BCMA family specificity."
            elif ligand == "CD72":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "CD72 is an immune C-type lectin-like receptor and the public rows may reflect immune adhesion or receptor-family context, but exact CD72-to-NCAM2/SEMA4D pair evidence was not verified."
                limitations = "Require exact ligand/receptor orientation and primary assay; do not transfer CD72 family or SEMA4D signaling evidence across unrelated immune receptors."
            elif ligand == "CDCP1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "CDCP1 is a transmembrane receptor-like protein that can participate in EGFR and Src-family crosstalk, but the public row does not establish a conventional soluble CDCP1-to-EGFR ligand mechanism."
                limitations = "Represent receptor crosstalk and proteolytic processing in receptor-proximal layers; do not materialize CDCP1-to-EGFR as a canonical ligand edge without direct extracellular binding evidence."
            elif ligand == "CDH12" and receptor == "ITGA1+ITGB1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = ["PMID:34385456"]
                species = "human"
                summary = "Primary spatial and single-cell profiling links CDH12-enriched tumor cells with CD49a/ITGA1-positive exhausted T-cell neighborhoods, but the study does not establish direct CDH12 binding to an ITGA1:ITGB1 receptor complex."
                limitations = "Retain as a cell-neighborhood and integrin-context hold; require direct CDH12-ITGA1:ITGB1 binding or receptor-proximal perturbation before promotion as a binary edge."
            elif ligand.startswith("CDH"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Cadherin-family candidates represent homophilic or heterophilic cell-adhesion and crosstalk contexts, but the public rows do not resolve exact trans orientation and pair-specific primary support for each target."
                limitations = "Preserve cadherin isoform, cis/trans orientation and adhesion context; do not infer soluble ligand signaling or transfer evidence across cadherin paralogs without an exact primary assay."
            elif ligand == "CEACAM2" and receptor == "SELE":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = ["PMID:1378450"]
                species = "human"
                summary = "Primary neutrophil-endothelial adhesion work supports CEA-like CD66/NCA molecules as sialyl-Lewis-x presenters participating in E-selectin-dependent adhesion, but does not resolve CEACAM2 as the exact ligand molecule."
                limitations = "Retain as CEACAM-family/selectin adhesion context; do not materialize a CEACAM2-SELE binary edge without paralog-specific binding or perturbation evidence."
            elif ligand.startswith("CHAT+"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses CHAT acetylcholine-synthesis machinery together with SLC10A4, SLC18A3 or SLC5A7 transport components as the ligand label rather than mature extracellular acetylcholine."
                limitations = "Represent acetylcholine synthesis, vesicular loading and release separately; do not materialize enzyme/transporter composites as direct muscarinic or nicotinic ligand-receptor edges."
            elif ligand.startswith("CEACAM"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "CEACAM-family candidates describe cell-adhesion, lectin and immune-checkpoint contexts, but the exact CEACAM paralog, orientation and receptor mechanism for these LILRA, CD209 or selectin rows were not verified in this pass."
                limitations = "Require exact CEACAM paralog, receptor orientation, species and primary binding or functional assay; do not transfer adhesion or checkpoint evidence across CEACAM family members."
            elif ligand in {"CIB1", "CIRBP"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "CIB1 and CIRBP are intracellular signaling or RNA-binding proteins, not mature extracellular ligands for the listed receptors or integrin subunits."
                limitations = "Represent intracellular adaptor, integrin-tail and stress-RNA mechanisms separately; do not materialize protein-association rows as ligand-receptor edges."
            elif ligand in {"CFD", "CFH"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Complement factor and adipokine-family proteins can participate in extracellular immune and protease-regulatory complexes, but the public rows do not resolve the exact mature form and receptor mechanism for these candidates."
                limitations = "Require exact complement-factor form, receptor or complex, species and primary assay; do not transfer complement-regulatory or adipokine evidence across paralogs or treat factor-factor associations as canonical ligand edges."
            elif ligand == "CGN":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "CGN/cingulin is a junctional cytoskeletal scaffolding protein, not a mature extracellular ligand for occludin or TGFBR targets."
                limitations = "Represent tight-junction and intracellular scaffolding mechanisms separately; do not materialize CGN-to-OCLN/TGFBR rows as ligand-receptor edges."
            elif ligand == "CHL1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "CHL1 is a neural cell-adhesion molecule with contactin/co-receptor contexts, but the listed CNTN, SIRPA and TMEM132A targets were not verified as exact primary CHL1 receptor pairs in this pass."
                limitations = "Preserve CHL1/contactin orientation and neural adhesion context; require exact pair-level primary evidence before promotion and do not infer a soluble ligand route."
            elif ligand == "CLEC11A":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "CLEC11A is an extracellular lectin-like protein with osteogenic context, but an exact CLEC11A-to-KIT receptor assay was not verified in this pass."
                limitations = "Require direct CLEC11A/KIT binding or receptor-dependent function; do not infer KIT activation from extracellular localization or family annotation."
            elif ligand.startswith("CLEC"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "C-type lectin-family rows can represent membrane immune receptors or context-dependent trans-interactions, but the exact CLEC isoform, ligand/receptor orientation and primary mechanism for these candidates were not verified."
                limitations = "Require exact CLEC form, receptor orientation, species and direct primary assay; do not transfer KLRB or NCAM-family evidence across CLEC paralogs."
            elif ligand in {"CLMP", "CMTM8", "CNMD"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "The candidate uses a membrane adhesion, tetraspanin-like or junction-associated protein in a receptor/crosstalk context, but no exact mature-ligand receptor experiment was verified for this row."
                limitations = "Represent cell-contact, membrane-organizer and receptor-crosstalk mechanisms separately; do not materialize these candidates as canonical soluble ligand edges without direct primary support."
            elif ligand.startswith("CNTF"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "CNTF signaling is supported through CNTFR-alpha with gp130 and LIFR or OSMR receptor complexes, but the public rows isolate receptor subunits, omit partners or list unrelated EGFR targets."
                limitations = "Retain the intact CNTFR-alpha:gp130:LIFR/OSMR topology and existing CNTF receptor-complex evidence; do not materialize isolated subunits as standalone CNTF receptors or transfer specificity to EGFR."
            elif ligand.startswith("CNTN"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Contactin-family candidates describe neural cell-adhesion and co-receptor contexts, but the exact contactin isoform, trans/cis orientation and receptor mechanism for these rows were not verified in this pass."
                limitations = "Preserve contactin isoform and adhesion orientation; require exact pair-level primary evidence before promotion and do not infer soluble ligand signaling from family membership."
            elif ligand.startswith("COL"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Collagen-family extracellular-matrix proteins can act as receptor ligands through integrins, DDRs or LAIR1, but these broad public rows do not resolve the exact collagen chain, mature trimer/domain and receptor complex for each candidate."
                limitations = "Require exact collagen isoform/domain, receptor subunit composition, species and primary binding or functional assay; do not transfer collagen-X/DDR2 or integrin-family evidence across collagen paralogs and receptor complexes."
            elif ligand == "COMP":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "COMP/thrombospondin-5 is an extracellular-matrix protein with integrin and CD47 adhesion contexts, but the public rows do not resolve the exact receptor complex and pair-specific mechanism for these integrin or syndecan candidates."
                limitations = "Retain exact COMP-CD47 and other primary-supported matrix-receptor relationships; require direct pair-level evidence before promotion and do not transfer COMP interactions across integrin or syndecan subunits."
            elif ligand == "COPA":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "COPA is a coatomer complex component of intracellular vesicle trafficking, not a mature extracellular ligand for NTSR2 or SORT1."
                limitations = "Represent coatomer and intracellular trafficking mechanisms separately; do not materialize COPA-to-receptor rows as ligand edges."
            elif ligand == "CORIN":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "CORIN is a membrane serine protease that processes natriuretic-peptide precursors, not a mature extracellular ligand for KIRREL or LRRC4C."
                limitations = "Represent protease-substrate processing separately; do not materialize CORIN-to-adhesion-receptor rows as direct ligand edges without exact primary support."
            elif ligand == "CORT":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "Cortistatin/neuropeptide-family biology is receptor-specific, but the current pass did not verify exact CORT binding or activation of the listed adrenergic, melatonin or MRGPR targets."
                limitations = "Require mature cortistatin form and direct receptor assay; do not transfer somatostatin or unrelated GPCR-family specificity to MRGPR paralogs."
            elif ligand == "CP":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "CP/ceruloplasmin is a secreted copper-binding enzyme/protein, not a mature Hedgehog receptor ligand for SMO in this row."
                limitations = "Represent ceruloplasmin and copper/oxidase biology separately; do not materialize CP-to-SMO from public-database co-membership."
            elif ligand == "CRB3":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "CRB3 is an epithelial polarity and junctional protein, not a mature extracellular ligand for LIN7C or PATJ."
                limitations = "Represent Crumbs polarity-complex associations separately; do not materialize intracellular/junctional protein complexes as ligand-receptor edges."
            elif ligand == "CRH":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Corticotropin-releasing hormone receptor biology is centered on CRHR1 and CRHR2, not the unrelated GPCR and RAMP targets listed here."
                limitations = "Require mature CRH and direct CRHR-family assay; do not transfer CRH specificity across ADCYAP1R, adrenergic, PTH, RAMP or VIP receptor families."
            elif ligand.startswith("CRISP"):
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "CRISP-family secreted proteins have reproductive and extracellular-matrix contexts, but an exact CRISP1/CRISP3-to-A1BG receptor or binding mechanism was not verified in this pass."
                limitations = "Resolve the mature CRISP protein and direct receptor or binding partner before promotion; do not infer a ligand-receptor edge from secreted-protein status alone."
            elif ligand == "CRLF1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "CRLF1 is a cytokine-receptor-like complex component that acts with CLCF1 and CNTFR-associated receptor complexes; the public CRLF1-to-LIFR row does not establish LIFR as a standalone receptor."
                limitations = "Retain intact CRLF1/CLCF1/CNTFR receptor-complex topology; do not materialize LIFR as an isolated CRLF1 receptor or transfer CNTF-family complex evidence to unrelated receptor forms."
            elif ligand == "CRLF2":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "CRLF2 is a cytokine-receptor subunit, not a mature extracellular ligand for the composite IL7R/TSLP receptor row."
                limitations = "Represent TSLP signaling through the intact CRLF2:IL7R receptor complex when directly supported; do not invert receptor subunits into ligand edges."
            elif ligand == "CRP":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "C-reactive protein and complement-receptor biology are context dependent, but an exact CRP-to-CR1L receptor experiment was not verified in this pass."
                limitations = "Require direct CRP/CR1L binding or receptor-dependent function with exact pentameric or monomeric CRP form; do not infer the edge from complement-family membership."
            elif ligand == "CRTAM":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "CRTAM is an immune cell-adhesion receptor with partner-specific trans-interaction context, but the listed DSC3, ILDR2, MUC15 and NTRK3 targets were not verified as exact primary CRTAM partners."
                limitations = "Require exact CRTAM ligand/receptor orientation and primary assay; do not transfer immune-adhesion or nectin-family evidence across unrelated adhesion proteins."
            elif ligand.startswith("CSF"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "CSF-family cytokines require exact receptor subunit complexes, while the public rows isolate alternate subunits or list integrin targets that were not verified as direct CSF ligand receptors in this pass."
                limitations = "Retain CSF1-CSF1R and CSF2-CSF2RA:CSF2RB receptor-complex boundaries; require exact receptor composition and primary assay before promoting alternate subunit or integrin rows."
            elif ligand == "CTSG" and receptor == "FPR1":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:15210802", "DOI:10.4049/jimmunol.173.1.428"]
                species = "human; rat"
                summary = "Primary chemotaxis and receptor-transfectant experiments identify cathepsin G as an FPR1 agonist: FPR1-dependent migration, receptor internalization, weak MAPK activation and PKCζ-dependent chemotactic signaling were observed."
                limitations = "Promote as a bounded protease-to-FPR1 inflammatory route; the study reports weaker and atypical signaling than fMLP, and does not establish a universal intracellular relay or terminal-TF output."
            elif ligand in {"CTSD", "CTSG"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Cathepsin D/G are proteases, and the public rows describe enzyme-substrate, cleavage or protease-context relationships rather than mature extracellular ligand-receptor edges."
                limitations = "Represent protease processing and receptor shedding in receptor-proximal or intracellular layers; do not materialize protease-to-substrate or protease-to-scaffold rows as ligand edges."
            elif ligand == "CUBN":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "CUBN/cubilin is an endocytic receptor component, not a mature extracellular ligand for LRP2 in this row."
                limitations = "Represent cubilin/amnionless uptake-complex biology separately; do not invert receptor or cargo-uptake components into ligand edges."
            elif ligand == "CXADR":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "CXADR/CAR is a junctional adhesion receptor, not a mature extracellular ligand for JAML in the public row."
                limitations = "Represent CXADR/JAML cell-adhesion orientation and junctional context separately; do not invert the receptor/ligand relationship without exact primary support."
            elif ligand.startswith("CXCL"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Chemokine-family candidates can signal through canonical, atypical or scavenging receptors, but these rows do not resolve the exact mature CXCL isoform and receptor mechanism for each listed target."
                limitations = "Require exact CXCL isoform, receptor orientation, species and primary binding or functional assay; do not transfer CXCR3, CCR or ACKR specificity to adrenergic, melatonin, DPP4 or unrelated targets."
            elif ligand.startswith(("CYP", "DBH", "DDC", "DHCR", "DHRS", "DIO")) or ligand == "DIO3+TG":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses a steroid, retinoid, catecholamine, serotonin or thyroid-hormone metabolic enzyme/composite as the ligand label rather than the mature hormone ligand."
                limitations = "Represent hormone biosynthesis separately; require the mature steroid, retinoid, catecholamine or thyroid hormone and direct nuclear-receptor assay before materializing a signaling edge."
            elif ligand in {"DCHS1", "DCN", "DMP1"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "The candidate represents cadherin, extracellular-matrix proteoglycan or mineralization-protein context, but the exact mature ligand form and receptor mechanism were not verified for this row."
                limitations = "Require exact protein/domain, receptor orientation and primary assay; do not transfer cell-adhesion or matrix-family evidence across paralogs or infer soluble ligand signaling."
            elif ligand == "DLK1":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "DLK1 has Notch and developmental cell-contact context, but an exact DLK1-to-ERBB4 receptor experiment was not verified in this pass."
                limitations = "Require direct DLK1/ERBB4 binding or receptor-dependent function; do not transfer Notch-family ligand evidence to ERBB4."
            elif ligand == "DLL1":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "DLL1 is a canonical Notch ligand, but an exact DLL1-to-MUSK receptor experiment was not verified in this pass."
                limitations = "Require direct DLL1/MUSK binding or receptor-dependent function; do not transfer Notch receptor specificity to MuSK."
            elif ligand == "DNAJB11":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "DNAJB11 is an intracellular/endoplasmic-reticulum chaperone, not a mature extracellular ligand for PRTG."
                limitations = "Represent chaperone and ER quality-control mechanisms separately; do not materialize DNAJB11-to-PRTG as a ligand-receptor edge."
            elif ligand in {"DSCAM", "DSCAML1"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "DSCAM-family candidates describe neuronal cell-adhesion and homophilic or heterophilic recognition contexts, but the exact DSCAM/DSCAML1 paralog, orientation and receptor mechanism for these rows were not verified."
                limitations = "Preserve neuronal adhesion and paralog-specific cis/trans topology; do not infer soluble ligand signaling or transfer evidence across PTPR, Notch or channel targets."
            elif ligand.startswith("DSC"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Desmocollin-family rows describe desmosomal cell-adhesion complexes, but the exact DSC/DSG paralog orientation and direct primary interaction for these candidates were not verified."
                limitations = "Preserve desmosomal cis/trans topology and paralog specificity; do not infer soluble ligand signaling from cadherin-family adhesion membership."
            elif ligand == "DSPP":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "DSPP is a dentin extracellular-matrix protein and the public rows do not establish the exact mature domain and integrin receptor mechanism for the listed candidates."
                limitations = "Require exact DSPP domain, receptor complex, species and primary assay; do not infer a generic integrin signaling edge from matrix localization."
            elif ligand == "DUSP18":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "DUSP18 is an intracellular dual-specificity phosphatase, not a mature extracellular ligand for tetraspanin, integrin or ribosomal targets."
                limitations = "Represent phosphatase and intracellular signaling mechanisms separately; do not materialize DUSP18-to-membrane-protein rows as ligand edges."
            elif ligand in {"EAR11", "EAR5"}:
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "EAR11/EAR5 remain unresolved public protein labels in this pass, and no exact mature-ligand identity or direct TLR2 receptor assay was verified."
                limitations = "Resolve the entity identifiers and protein forms before promotion; do not infer TLR2 specificity from public-database membership alone."
            elif ligand == "ECM1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "ECM1 is a secreted extracellular-matrix protein with context-dependent matrix and receptor interactions, but the listed CACHD1 target was not verified as an exact ECM1 receptor in this pass."
                limitations = "Require direct ECM1/CACHD1 binding or receptor-dependent function; do not transfer ECM1 matrix biology to unrelated adhesion or channel proteins."
            elif ligand == "EDA" and receptor == "IL1RL1":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "EDA/ectodysplasin signaling is established through EDAR and XEDAR-family receptors, but an exact EDA-to-IL1RL1 experiment was not verified in this pass."
                limitations = "Require direct EDA/IL1RL1 binding or receptor-dependent function; do not transfer EDAR/XEDAR specificity to IL1RL1/ST2."
            elif ligand == "EDIL3":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "EDIL3/DEL1 is an extracellular-matrix protein with integrin-binding context, but the public rows do not resolve the exact receptor subunit composition and pair-specific primary mechanism."
                limitations = "Require exact EDIL3 domain, integrin complex, species and primary binding or functional assay; do not transfer integrin-family evidence across free subunits and heterodimers."
            elif ligand.startswith("EDN"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Endothelin-family ligands signal through EDNRA and EDNRB, not the unrelated ADGRL4, ECE1, EGFR or KEL targets listed in these rows."
                limitations = "Require mature endothelin peptide and direct EDNRA/EDNRB assay; do not transfer endothelin receptor specificity to processing enzymes or unrelated GPCRs."
            elif ligand == "EFEMP2":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "EFEMP2/fibulin-4 is an extracellular-matrix protein with elastic-fiber and receptor-associated contexts, but the listed CATSPER1 and LINGO1 targets were not verified as exact primary receptor partners."
                limitations = "Require direct EFEMP2 target binding or receptor-dependent function; do not transfer fibulin-family or extracellular-matrix evidence across unrelated receptors."
            elif ligand == "EFNA3" and receptor == "EPHA5":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:10516308"]
                species = "rat"
                summary = "Primary entorhino-hippocampal development experiments show EphA5 expression and EphA5-AP binding in hippocampal tissue, while ephrin-A3 produces receptor-contextual neurite repulsion and is proposed to interact with EphA5."
                limitations = "Promote as a bounded developmental guidance route; the study uses tissue binding and functional outgrowth/stripe assays rather than purified binary binding, and it does not establish an intracellular relay or terminal-TF output."
            elif ligand == "EFNA5" and receptor == "EPHA8":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:21343910"]
                species = "as stated in primary model/assay"
                summary = "Primary retinocollicular-development experiments stimulate EphA8-expressing cells with clustered ephrin-A5-Fc and measure EphA8-dependent ligand binding and endocytosis of Eph-ephrin complexes."
                limitations = "Promote as a bounded ephrin-A5/EphA8 receptor-proximal route; the study does not establish a complete intracellular cascade, terminal-TF output or SCI transfer."
            elif ligand == "EFNB1" and receptor == "EPHA4":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:19542359", "PMCID:PMC2729353", "DOI:10.1242/dev.034405"]
                species = "mouse"
                summary = "Primary cortical-development experiments demonstrate EphA4/ephrin-B1 binding by cell-based binding assays and co-immunoprecipitation, ephrin-B1-dependent EphA4 phosphorylation, and neighboring-cell proliferation outputs."
                limitations = "Promote as a bounded forward-signaling route in developing cortex; the study does not establish a universal intracellular relay, terminal-TF output or SCI transfer."
            elif ligand == "EFNB1" and receptor == "EPHB3":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = ["PMID:16786562", "PMCID:PMC2637817", "DOI:10.1002/cne.21001"]
                species = "mouse; rat"
                summary = "Primary spinal-cord studies localize ephrin-B1 and EphB3 in complementary developmental domains and characterize EphB3-selective reagents, supporting contact-dependent EphB/ephrin-B developmental context without an exact ephrin-B1-to-EphB3 activation assay."
                limitations = "Retain as contextual developmental evidence only; do not promote a binary EFNB1-EPHB3 edge or infer a complete downstream relay from co-expression, reagent specificity or family-level affinity context."
            elif ligand.startswith("EFNA") or ligand.startswith("EFNB"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Ephrin-family candidates can form contact-dependent Eph receptor interactions, but the public rows do not resolve the exact ephrin isoform, Eph orientation and pair-specific primary evidence for each listed target."
                limitations = "Require exact ephrin/Eph paralog, membrane orientation, species and primary binding or activation assay; do not transfer canonical Eph-family specificity across cross-class or unrelated targets."
            elif ligand == "EGF":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "EGF-family ligand biology is receptor-specific, while the listed AXL, FSHR, LDLR, LRP2, NRP1, PLD2 and RHBDL2 targets were not verified as direct EGF receptor pairs in this pass."
                limitations = "Retain exact EGF/EGFR-family receptor evidence separately; require pair-specific primary binding or activation before promotion and do not transfer EGFR specificity to unrelated targets."
            elif ligand == "EPGN" and receptor == "ERBB4":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Epigen/EPGN is primary-supported as an EGFR ligand in the graph, but the current pass did not verify the listed EPGN-to-ERBB4 pair as an exact primary receptor interaction."
                limitations = "Preserve EPGN-EGFR evidence and ErbB-family receptor boundaries; require direct EPGN/ERBB4 binding or receptor activation before promotion."
            elif ligand == "EPHA4":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "EPHA4 is a membrane Eph receptor, and the public rows represent receptor crosstalk with FGFR-family proteins rather than a conventional soluble ligand-to-receptor edge."
                limitations = "Represent Eph/FGFR receptor crosstalk in receptor-proximal layers; do not invert EPHA4 into a soluble ligand or materialize the rows as canonical ligand-receptor edges without direct assay."
            elif ligand == "EPO" and receptor == "CRLF3":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "EPO signaling is established through EPOR-containing complexes, but an exact EPO-to-CRLF3 receptor experiment was not verified in this pass."
                limitations = "Require direct EPO/CRLF3 binding or receptor-dependent function; do not transfer EPOR specificity to CRLF3 from cytokine-receptor family membership."
            elif ligand == "ERFE":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Erythroferrone/ERFE is a secreted erythroid regulator with hemojuvelin/BMP pathway context, while the public ERFE-to-LRP1 row was not verified as an exact direct receptor mechanism."
                limitations = "Require direct ERFE/LRP1 binding or receptor-dependent function; do not transfer BMP/hemojuvelin regulation or lipoprotein-uptake evidence to LRP1 without pair-specific support."
            elif ligand == "ENG":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "ENG/endoglin is a TGF-beta superfamily co-receptor or accessory membrane protein, not a mature ligand for ACVR2A, ACVRL1, BMPR2, CDH5 or ITGAV."
                limitations = "Represent endoglin-containing receptor complexes and endothelial adhesion separately; do not invert receptor/accessory roles into ligand edges."
            elif ligand == "ESAM":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "ESAM is an endothelial junctional adhesion protein with homophilic and junctional signaling context, but an exact ESAM-to-ROBO3 receptor interaction was not verified in this pass."
                limitations = "Preserve ESAM adhesion orientation and endothelial context; require direct ESAM/ROBO3 primary evidence before promotion."
            elif ligand == "ESM1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "ESM1/endocan is a secreted endothelial proteoglycan with inflammatory and matrix-receptor context, but the listed integrin subunits were not verified as exact ESM1 receptor pairs."
                limitations = "Require exact ESM1 form, receptor complex and primary binding or functional assay; do not transfer endothelial proteoglycan evidence across integrin subunits."
            elif ligand == "ETV5":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "ETV5 is an intracellular transcription factor, not an extracellular ligand for ERBB2."
                limitations = "Represent ETV5 downstream transcriptional regulation separately; do not materialize TF-to-receptor rows as ligand edges."
            elif ligand == "EZR":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "EZR/ezrin is an intracellular membrane-cytoskeletal linker, not a mature extracellular ligand for SLC9A1."
                limitations = "Represent ezrin-dependent intracellular membrane organization separately; do not materialize protein-complex associations as ligand-receptor edges."
            elif ligand in {"F10", "F11"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Coagulation factor labels represent protease cascade components or substrates, not conventional extracellular ligands for the listed coagulation, platelet or immune targets."
                limitations = "Represent coagulation cleavage and platelet-adhesion mechanisms separately; require an exact mature factor-receptor assay before any ligand-edge promotion."
            elif ligand == "F11R":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "F11R/JAM-A is a junctional adhesion protein, not a verified soluble ligand for ITGB2L in the public row."
                limitations = "Preserve JAM-A cis/trans adhesion and junctional context; require direct F11R/ITGB2L evidence before promotion."
            elif ligand in {"F12", "F2", "F5", "F7", "F8", "F9", "FGA", "FGB"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Coagulation-factor and fibrinogen-chain labels represent protease cascade components, substrates or structural precursors rather than conventional ligand-receptor edges for the listed targets."
                limitations = "Represent coagulation cleavage, fibrin assembly and platelet-adhesion mechanisms separately; require an exact mature factor-receptor assay before any ligand-edge promotion."
            elif ligand == "FABP5":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "FABP5 is an intracellular fatty-acid-binding protein, not a mature extracellular ligand for RXRA."
                limitations = "Represent lipid-binding and nuclear-receptor co-regulation separately; do not materialize FABP5-to-RXRA as a ligand-receptor edge."
            elif ligand == "FADD":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "FADD is an intracellular death-domain adaptor, not an extracellular ligand for ABCA1, FAS, TRADD or TRAF2."
                limitations = "Represent DISC and apoptotic adaptor signaling separately; do not materialize intracellular protein associations as ligand-receptor edges."
            elif ligand == "FAM3C":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "FAM3C/ILEI is a secreted cytokine-like protein with context-dependent signaling, but the listed ADGRG5, CLEC2, FFAR3 and KIR targets were not verified as exact FAM3C receptor pairs in this pass."
                limitations = "Require mature FAM3C form, receptor identity and primary binding or functional assay; do not transfer cytokine-like or lectin-family evidence across unrelated targets."
            elif ligand == "FAM3D":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "FAM3D is a secreted protein with proposed chemoattractant activity, but an exact FAM3D-to-FPR3 receptor experiment was not verified in this pass."
                limitations = "Require direct FAM3D/FPR3 binding or receptor-dependent function; do not transfer FPR-family specificity from other chemoattractants."
            elif ligand == "FAP":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "FAP is a membrane serine protease, not a mature extracellular ligand for DPP4 or NPR2."
                limitations = "Represent protease processing and stromal cell-surface biology separately; do not materialize FAP-to-enzyme or FAP-to-receptor rows as ligand edges without exact primary support."
            elif ligand == "FARP2":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "FARP2 is an intracellular guanine-nucleotide exchange factor, not an extracellular ligand for PLXNA receptors."
                limitations = "Represent plexin/Rho-family intracellular regulation separately; do not materialize FARP2-to-plexin rows as ligand-receptor edges."
            elif ligand == "FASL" and receptor == "TNFRSF1A":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "FASL is established through FAS/TNFRSF6, while an exact FASL-to-TNFRSF1A receptor experiment was not verified in this pass."
                limitations = "Require direct FASL/TNFRSF1A binding or receptor-dependent function; do not transfer FAS-family specificity to TNFR1."
            elif ligand == "FCER2A":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "FCER2A/CD23 is a membrane immunoglobulin receptor/adhesion protein with context-dependent integrin and immune interactions, but the listed targets were not verified as exact direct receptor partners in this pass."
                limitations = "Preserve CD23 orientation and receptor-complex context; require exact target, species and primary binding or functional assay before promotion."
            elif ligand == "FCGR4":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "FCGR4 is an Fc receptor, not a mature extracellular ligand for EDA2R."
                limitations = "Represent Fc-receptor and immune-complex biology separately; do not invert receptor identity into a ligand edge."
            elif ligand == "FCNB":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "FCNB/ficolin-B is a complement-recognition protein with extracellular immune-complex context, but the listed LRP1 target was not verified as an exact direct receptor mechanism."
                limitations = "Require exact FCNB form, LRP1 binding or functional assay and species; do not transfer ficolin-family or complement uptake evidence across receptors."
            elif ligand == "FCRL6":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "FCRL6 is an immune receptor-family protein, not a mature ligand for NRP2."
                limitations = "Represent FCRL6 receptor and immune-cell signaling separately; do not invert receptor-family membership into a ligand edge."
            elif ligand == "FGF23":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "FGF23 signaling requires an FGFR/Klotho receptor complex, while the public FGF23-to-PHEX row is a mineral-metabolism relationship rather than a verified direct receptor edge."
                limitations = "Retain exact FGF23/FGFR/Klotho receptor-complex evidence and PHEX regulatory context separately; do not materialize PHEX as a standalone FGF23 receptor."
            elif ligand == "FGFR3":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "FGFR3 is a receptor tyrosine kinase, not an extracellular ligand for EPHA4."
                limitations = "Represent Eph/FGFR receptor crosstalk in receptor-proximal layers; do not invert receptor identity into a ligand edge."
            elif ligand.startswith("FGFR"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "FGFR-family labels are receptor tyrosine kinases or receptor-like proteins, not mature extracellular ligands for the listed targets."
                limitations = "Represent FGFR crosstalk, co-receptor and intracellular signaling separately; do not invert receptor-family identities into ligand edges."
            elif ligand == "FGG":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "FGG is a fibrinogen gamma-chain structural precursor, not an explicitly defined mature ligand for the listed integrin targets."
                limitations = "Require exact fibrinogen form, receptor complex and primary assay before promotion; do not materialize fibrinogen-chain labels as direct ligand edges."
            elif ligand == "FN1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Fibronectin is an extracellular-matrix ligand with integrin and co-receptor interactions, but the public rows do not resolve the exact FN1 domain, receptor complex and primary mechanism for each listed target."
                limitations = "Retain exact fibronectin-integrin and receptor-complex evidence separately; require domain, receptor subunit, species and primary assay before promotion and do not transfer FN1 binding across receptor families."
            elif ligand == "FLRT2":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "FLRT-family proteins have latrophilin and cell-adhesion contexts, but an exact FLRT2-to-FLT4 receptor experiment was not verified in this pass."
                limitations = "Require direct FLRT2/FLT4 binding or receptor-dependent function; do not transfer FLRT/latrophilin family evidence to VEGFR3/FLT4."
            elif ligand == "FRS3":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "FRS3 is an intracellular fibroblast growth factor receptor substrate/adaptor, not an extracellular ligand for FGFR1."
                limitations = "Represent FGFR adaptor signaling separately; do not materialize intracellular FRS3-FGFR associations as ligand-receptor edges."
            elif ligand == "FURIN":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "FURIN is a protease that processes secreted and membrane proteins, not a mature ligand for ADAM, BACE, insulin, LRP or Notch targets."
                limitations = "Represent proteolytic maturation and receptor processing in receptor-proximal or intracellular layers; do not materialize protease-substrate rows as ligand edges."
            elif ligand == "GAL":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Galanin receptor biology is centered on GALR1, GALR2 and GALR3, not the unrelated adrenergic, glutamatergic or melatonin receptors listed here."
                limitations = "Require mature galanin and direct GALR-family assay; do not transfer galanin specificity to unrelated GPCRs."
            elif ligand == "GAST":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "Gastrin receptor biology is receptor- and peptide-form-specific, and an exact GAST-to-CCKAR or GAST-to-GPR152 experiment was not verified in this pass."
                limitations = "Require mature gastrin form and direct CCKAR/CCKBR assay; do not infer activity at GPR152 from peptide-family membership."
            elif ligand == "GCG":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "GCG/glucagon is a peptide hormone and DPP4 is a protease; the public row is not a conventional glucagon ligand-receptor edge."
                limitations = "Represent peptide processing and glucagon-receptor signaling separately; require mature ligand and direct receptor assay before promotion."
            elif ligand.startswith("GDF"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "GDF-family signaling is receptor-complex and paralog specific, but the public rows do not resolve the exact mature GDF form, type-I/type-II receptor composition and primary pair-level assay for each target."
                limitations = "Retain exact GDF/BMP receptor-complex evidence separately; require ligand form, receptor topology, species and direct primary support before promoting component-only or unrelated receptor rows."
            elif ligand == "GDNF":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "GDNF signaling is co-receptor and receptor-complex dependent, while the public rows isolate EDNRB, GFRA3 or NCAM1 without establishing the exact GDNF receptor topology for each candidate."
                limitations = "Retain GDNF/GFRA/RET and NCAM-family receptor-complex boundaries; require exact GDNF form, co-receptor composition and primary assay before promotion."
            elif ligand in {"GGT1", "GJB2", "GJB6", "GLG1"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses an enzyme, gap-junction protein or intracellular Golgi/membrane protein as the ligand label rather than a mature extracellular ligand."
                limitations = "Represent enzymatic, gap-junction and intracellular membrane-complex mechanisms separately; do not materialize these protein associations as ligand-receptor edges."
            elif ligand == "GHRL":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Ghrelin/GHRL receptor biology is centered on GHSR, not the prostacyclin receptor PTGIR."
                limitations = "Require mature ghrelin and direct GHSR assay; do not transfer ghrelin specificity to unrelated GPCRs."
            elif ligand == "GIP":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "GIP receptor biology is centered on GIPR, not the unrelated GPCR, insulin, FAP, PTH or RAMP targets listed here."
                limitations = "Require mature GIP and direct GIPR assay; do not transfer incretin-family specificity to unrelated receptor families."
            elif ligand.startswith("GM"):
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The GM-prefixed public identifier was not resolved to a verified mature ligand identity and exact receptor assay in this pass."
                limitations = "Resolve the species-specific identifier and protein form before promotion; do not infer receptor specificity from an unresolved GM label or public-database membership alone."
            elif ligand == "GNB3":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "GNB3 is an intracellular G-protein beta subunit, not an extracellular ligand for GABBR2 or TGFBR1."
                limitations = "Represent heterotrimeric G-protein coupling in the intracellular continuation layer; do not materialize GNB3-to-receptor rows as ligand edges."
            elif ligand == "GNRH1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "GnRH1 receptor biology is centered on GNRHR, while CAMK2A is an intracellular kinase rather than a GnRH receptor."
                limitations = "Require mature GnRH peptide and direct GNRHR assay; represent CAMK2A downstream signaling separately."
            elif ligand in {"GP1BA", "GP5", "GP49A"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses a platelet or immune membrane receptor/protein as the ligand label, not a mature extracellular ligand for the listed targets."
                limitations = "Represent platelet adhesion and immune receptor complexes separately; do not invert receptor identities into ligand edges without exact primary support."
            elif ligand.startswith("GPC"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Glypican-family proteoglycans can act as co-receptors or extracellular modulators for growth-factor and morphogen pathways, but the public rows do not resolve the exact glypican form, receptor complex and direct primary mechanism for each target."
                limitations = "Require exact glypican isoform, cleavage state, receptor/co-receptor topology and primary assay; do not transfer FGF, Hedgehog or lipoprotein-receptor context across glypican paralogs."
            elif ligand == "GPI1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "GPI1 is an intracellular biosynthetic enzyme/component, not a mature extracellular ligand for NTRK1."
                limitations = "Represent GPI-anchor biosynthesis separately; do not materialize GPI1-to-NTRK1 as a ligand-receptor edge."
            elif ligand == "GRN":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "GRN/progranulin has receptor and proteolytic-fragment context, but the public CD209F/CD209G and NTRK1 rows were not verified as exact mature GRN receptor interactions in this pass."
                limitations = "Preserve the contested GRN receptor and granulin-fragment boundaries; require exact ligand form, receptor, species and primary assay before promotion."
            elif ligand.startswith("GST"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "GST-family labels are intracellular glutathione-transferase enzymes, not mature extracellular ligands for RYR, EGFR or TRAF targets."
                limitations = "Represent detoxification and intracellular redox mechanisms separately; do not materialize enzyme-protein associations as ligand-receptor edges."
            elif ligand == "GUCY2E":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "GUCY2E is a membrane guanylate cyclase receptor/enzyme, not a mature ligand for NECTIN3 or NECTIN4."
                limitations = "Represent membrane guanylate-cyclase and adhesion biology separately; do not invert receptor identity into a ligand edge."
            elif ligand.startswith("GZM"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Granzyme-family labels are intracellular or released proteases, and the public rows do not define them as mature ligands for the listed muscarinic, IGF or anti-apoptotic targets."
                limitations = "Represent protease/substrate and cytotoxic-granule mechanisms separately; do not materialize granzyme-to-receptor or granzyme-to-MCL1 rows as ligand edges."
            elif ligand == "HAPLN1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "HAPLN1 is an extracellular-matrix link protein with matrix and adhesion context, but the listed ADGRA2 and MPIG6B targets were not verified as exact HAPLN1 receptor partners in this pass."
                limitations = "Require direct HAPLN1 target binding or receptor-dependent function; do not transfer extracellular-matrix or adhesion-family evidence across unrelated receptors."
            elif ligand in {"HAS1", "HAS2"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "HAS1/HAS2 are hyaluronan-synthesizing enzymes; the public rows do not represent the mature hyaluronan ligand or an exact receptor mechanism."
                limitations = "Represent hyaluronan production separately and use mature hyaluronan-to-CD44 or other receptor evidence when directly supported; do not materialize synthase-to-receptor rows."
            elif ligand == "HAVCR1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "HAVCR1/KIM-1 is a membrane immune/uptake receptor, not a mature extracellular ligand for CD300, IGSF, SIGLEC or TIMD targets."
                limitations = "Represent receptor orientation and uptake/immune-complex biology separately; do not invert HAVCR1 into a ligand edge."
            elif ligand == "HBEGF":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "HB-EGF is an EGFR-family ligand, but the listed CD6, ERBB2, MOG and PRLR rows do not resolve the exact mature HB-EGF form and receptor topology as direct primary-supported pairs."
                limitations = "Retain exact EGFR/ERBB-family receptor-complex evidence; require direct pair-specific assay before promoting ERBB2 or unrelated target rows and do not infer signaling from receptor-family membership alone."
            elif ligand == "HC":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "HC is an unresolved or ambiguous public ligand label in this pass, and no exact mature protein identity or receptor assay was verified for the listed targets."
                limitations = "Resolve the source identifier and protein form before promotion; do not infer receptor specificity from the normalized label alone."
            elif ligand == "HEBP1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "HEBP1 is a heme-binding intracellular protein, not a mature extracellular ligand for the listed GPCRs."
                limitations = "Represent intracellular heme and stress biology separately; do not materialize HEBP1-to-receptor rows as ligand edges."
            elif ligand == "HGF":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "HGF signaling is centered on MET and can involve integrin co-receptor context, but the public HGF-to-ITGB1 row does not establish the exact receptor topology as a standalone direct ligand edge."
                limitations = "Retain HGF/MET and exact integrin co-receptor evidence separately; require direct ITGB1-specific primary support before promotion."
            elif ligand == "HHIPL2":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "HHIPL2 is a Hedgehog-related extracellular protein, but an exact HHIPL2-to-CACHD1 receptor or binding experiment was not verified in this pass."
                limitations = "Require direct HHIPL2/CACHD1 binding or receptor-dependent function; do not transfer Hedgehog-family context to CACHD1."
            elif ligand == "HP":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Haptoglobin is a secreted hemoglobin-binding protein with receptor and uptake context, but the listed APOA1, GM49368 and integrin targets were not verified as exact direct HP receptors in this pass."
                limitations = "Require exact HP form, receptor or uptake complex, species and primary assay; do not transfer CD163 or lipoprotein-uptake evidence to unrelated targets."
            elif ligand == "HRAS":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "HRAS is an intracellular small GTPase, not an extracellular ligand for AGTR1A, CAV1, INSR or TLR9."
                limitations = "Represent Ras-family intracellular continuation separately; do not materialize HRAS-to-receptor rows as ligand edges."
            elif ligand == "HRG":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "HRG is an ambiguous normalized label that may refer to distinct protein families, and the exact mature ligand identity and ERBB/FCGR receptor assay were not resolved in this pass."
                limitations = "Resolve the source database identifier and protein form before promotion; do not transfer heregulin/NRG or histidine-rich glycoprotein evidence across unrelated meanings."
            elif ligand.startswith("HSD"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "HSD-family labels are steroid-metabolizing enzymes, not mature extracellular ligands for androgen, estrogen, bile-acid or ion-channel receptors."
                limitations = "Represent steroid biosynthesis separately; require the mature steroid and direct nuclear-receptor assay before materializing a signaling edge."
            elif ligand == "HSP90AA1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "HSP90AA1 is an intracellular chaperone with possible extracellular stress context, but the listed CFTR and EGFR rows do not establish an exact mature-ligand receptor mechanism."
                limitations = "Represent chaperone, receptor-complex and extracellular stress mechanisms separately; require direct HSP90AA1 target binding or receptor-dependent function before promotion."
            elif ligand.startswith("HSP90"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "HSP90-family chaperones can have intracellular and extracellular stress-associated functions, but the listed receptor targets do not establish exact mature-ligand receptor edges in this pass."
                limitations = "Require exact HSP90 isoform, extracellular form, receptor, species and primary binding or functional assay; do not transfer chaperone or TLR context across isoforms."
            elif ligand == "HSPG2":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "HSPG2/perlecan is an extracellular-matrix proteoglycan with growth-factor and matrix-binding context, but the public HSPG2-to-COL13A1 row was not verified as a direct receptor or ligand mechanism."
                limitations = "Require exact perlecan domain, partner and primary assay; do not transfer matrix proteoglycan context to collagen-chain candidates without direct evidence."
            elif ligand.startswith("HSP"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "HSP-family labels are intracellular chaperones or stress proteins, not mature extracellular ligands for the listed receptor targets."
                limitations = "Represent chaperone and stress-response mechanisms separately; do not materialize HSP-to-receptor rows without exact extracellular ligand evidence."
            elif ligand == "IAPP":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "IAPP/amylin signaling is receptor-complex dependent and primarily uses CALCR-containing RAMP complexes, while the listed GPCR targets are not verified as direct mature IAPP receptors in this pass."
                limitations = "Retain exact amylin receptor-complex topology and do not transfer CALCR/RAMP evidence to unrelated ADCYAP1R, adrenergic, PTH, RAMP or VIP receptors."
            elif ligand.startswith("ICAM"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "ICAM-family proteins are cell-adhesion and immune-interaction molecules with integrin and lectin contexts, but the public rows do not resolve exact ICAM isoform, receptor orientation and pair-specific primary mechanisms for each target."
                limitations = "Preserve ICAM isoform, cis/trans orientation and integrin/lectin complex context; require exact primary assay before promotion and do not infer a soluble ligand route from adhesion-family membership."
            elif ligand == "ICOSL":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "ICOSL is an immune costimulatory ligand with established ICOS receptor context, but an exact ICOSL-to-NTM receptor experiment was not verified in this pass."
                limitations = "Require direct ICOSL/NTM binding or receptor-dependent function; do not transfer ICOS-family specificity to unrelated adhesion molecules."
            elif ligand == "IFITM6":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "IFITM6 is a membrane-associated interferon-induced protein, not a mature ligand for CD81."
                limitations = "Represent IFITM and tetraspanin membrane-complex biology separately; do not materialize IFITM6-to-CD81 as a ligand edge without direct primary support."
            elif ligand.startswith("IFNA"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Type-I interferon signaling requires subtype- and species-specific IFNAR1:IFNAR2 receptor-complex evidence, while the public rows do not resolve the exact IFNA paralog and binary/composite topology for each candidate."
                limitations = "Preserve IFNA subtype, species and IFNAR1/IFNAR2 complex boundaries; do not transfer family-level interferon evidence across paralogs or materialize isolated receptor subunits as complete edges."
            elif ligand == "IFNG":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "IFNG signaling is established through IFNGR1/IFNGR2, but the IFNG-to-MPL row was not verified as an exact primary receptor interaction."
                limitations = "Require direct IFNG/MPL binding or receptor-dependent function; do not transfer IFNGR specificity to the thrombopoietin receptor MPL."
            elif ligand == "IFNE":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "IFNE is a type-I interferon family ligand with IFNAR context, but an exact IFNE-to-ADGRV1 receptor experiment was not verified in this pass."
                limitations = "Require direct IFNE/ADGRV1 binding or receptor-dependent function; do not transfer IFNAR specificity to an adhesion GPCR."
            elif ligand in {"IGF1", "IGF2"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "IGF-family signaling is receptor- and binding-protein dependent, but the listed IGF1/IGF2 candidates do not resolve exact mature ligand, receptor-complex and pair-specific primary support in this pass."
                limitations = "Retain exact IGF1R/IGF2R and IGFBP contexts separately; do not transfer IGF-family specificity to TRPV, GPR or unrelated receptor targets."
            elif ligand.startswith("IGFBP"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "IGF-binding proteins can modulate IGF availability and have context-dependent receptor interactions, but the listed target pairs were not verified as exact direct IGFBP receptor mechanisms in this pass."
                limitations = "Require exact IGFBP form, receptor or co-receptor, species and primary assay; do not transfer IGF1R/IGF2R or matrix-family evidence across IGFBP paralogs."
            elif ligand.startswith("IGSF"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "IGSF-family candidates describe immune or cell-adhesion proteins, but exact paralog, trans orientation and pair-specific primary support for these rows were not verified."
                limitations = "Require exact IGSF paralog, ligand/receptor orientation, species and primary assay; do not transfer immune-adhesion evidence across IGSF, CD or CLEC family members."
            elif ligand in {"IL1RAPL1", "ILDR2"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses an interleukin-receptor-family or membrane receptor protein as the ligand label, not a mature extracellular cytokine ligand for the listed targets."
                limitations = "Represent receptor orientation and receptor-complex biology separately; do not invert IL1RAPL1 or ILDR2 into ligand edges."
            elif ligand == "IL18BP":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "IL18BP is a soluble IL-18-binding protein/decoy regulator rather than a canonical cytokine receptor ligand, and the listed targets were not verified as direct IL18BP receptors."
                limitations = "Retain IL18 sequestration and cytokine-availability context separately; do not materialize IL18BP-to-receptor rows without an exact primary receptor assay."
            elif ligand == "ILTIFB":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "ILTIFB remains an unresolved or noncanonical interleukin-family label in this pass, and no exact mature ligand identity or direct receptor assay was verified."
                limitations = "Resolve the source identifier, mature protein form and receptor before promotion; do not transfer IL-family specificity from the normalized label alone."
            elif ligand.startswith("IL"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Interleukin-family rows require exact cytokine subtype, species and multi-subunit receptor-complex assignment; the public candidates include isolated subunits and targets not verified as direct receptor pairings in this pass."
                limitations = "Retain exact interleukin receptor-complex evidence separately; require mature cytokine form, receptor composition and primary binding or activation assay before promotion, and do not transfer specificity across IL paralogs."
            elif ligand.startswith("INH"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Inhibin/activin-family candidates are mature-ligand and receptor-complex dependent, but the public rows do not resolve exact alpha-beta composition, type-I/type-II receptor topology and pair-specific primary support for each candidate."
                limitations = "Require exact inhibin or activin ligand form, receptor-complex composition, species and primary assay; do not collapse subunit composites into unsupported binary edges or transfer specificity across INH paralogs."
            elif ligand == "IRAK4":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "IRAK4 is an intracellular innate-immune kinase, not an extracellular ligand for TLR4, TLR6 or TLR7."
                limitations = "Represent TLR-to-IRAK4 intracellular continuation separately; do not materialize IRAK4-to-TLR rows as ligand edges."
            elif ligand == "ITGA4+ITGB1" and receptor == "VCAM1":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E000213"
                primary = ["PMID:7511143", "PMCID:PMC2290915"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human; mouse"
                summary = "The graph contains the primary-supported VCAM1-to-alpha4beta1 adhesion relationship in the reverse orientation of the public row."
                limitations = "Preserve VCAM1 as ligand and ITGA4:ITGB1 as the receptor complex; do not add a duplicate reverse edge or treat ITGA4/ITGB1 as an extracellular ligand."
            elif ligand == "ITGA4+ITGB7" and receptor == "VCAM1":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E000582"
                primary = ["PMID:8640376"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "The graph contains the primary-supported VCAM1-to-alpha4beta7 adhesion relationship in the reverse orientation of the public row."
                limitations = "Preserve VCAM1 as ligand and ITGA4:ITGB7 as the receptor complex; do not add a duplicate reverse edge."
            elif ligand == "ITGA9+ITGB1" and receptor == "VCAM1":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E000589"
                primary = ["PMID:10209034"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human; rat"
                summary = "The graph contains the primary-supported VCAM1-to-alpha9beta1 adhesion relationship in the reverse orientation of the public row."
                limitations = "Preserve VCAM1 as ligand and ITGA9:ITGB1 as the receptor complex; do not add a duplicate reverse edge."
            elif ligand in {"ITGA4", "ITGA9"} and receptor == "VCAM1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                primary = []
                species = "as stated in primary model/assay"
                summary = "VCAM1 evidence supports heterodimeric alpha4beta1 or alpha9beta1 integrin complexes, not isolated ITGA4 or ITGA9 subunits as complete receptors in the public row."
                limitations = "Retain the intact integrin heterodimer orientation and do not materialize free integrin alpha-subunit rows."
            elif ligand == "ITGAM" and receptor == "ICAM1":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E000599"
                primary = ["PMID:1980124"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "The graph contains the primary-supported ICAM1-to-Mac-1/ITGAM:ITGB2 adhesion relationship in the reverse orientation of the public row."
                limitations = "Preserve ICAM1 as ligand and ITGAM:ITGB2 as the receptor complex; do not add a duplicate reverse edge or treat free ITGAM as the complete receptor."
            elif ligand in {"ITGAV", "ITGB1", "ITGB2", "ITGB2L"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                primary = []
                species = "as stated in primary model/assay"
                summary = "The public row places a free integrin subunit or unresolved beta2-like label in ligand position, while the relevant adhesion relationships require an intact heterodimeric receptor complex and a defined extracellular ligand orientation."
                limitations = "Retain exact integrin heterodimer composition and ligand orientation; do not materialize free-subunit rows or transfer alpha/beta integrin evidence across complexes."
            elif ligand == "ITM2B":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "ITM2B is a membrane-associated protein with intracellular and processing context, not a mature extracellular ligand for ROR2."
                limitations = "Represent ITM2B processing and membrane biology separately; do not materialize ITM2B-to-ROR2 as a ligand edge without exact primary support."
            elif ligand == "IZUMO1":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "IZUMO1 is a gamete-fusion membrane protein, but an exact IZUMO1-to-LILRA5 receptor experiment was not verified in this pass."
                limitations = "Require direct IZUMO1/LILRA5 binding or receptor-dependent function; do not transfer gamete-adhesion or immune-receptor family evidence."
            elif ligand == "JAML":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "JAML is a junctional adhesion membrane protein/receptor partner, not a mature soluble ligand for CD320 or other membrane targets in these rows."
                limitations = "Represent JAML/CXADR and related adhesion-complex orientation separately; do not invert JAML into a ligand edge without exact primary support."
            elif ligand.startswith("JAM"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "JAM-family candidates describe junctional cell-adhesion and trans-interaction contexts, but the exact JAM paralog, orientation and receptor mechanism for these rows were not verified as primary-supported direct edges."
                limitations = "Preserve JAM family, cis/trans orientation and adhesion context; require exact pair-level primary assay before promotion and do not infer soluble ligand signaling."
            elif ligand.startswith("KCN"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "KCNA1 is an ion-channel protein, not a mature extracellular ligand for contactin, RTN4 or related membrane targets."
                limitations = "Represent channel and membrane-complex biology separately; do not materialize KCNA1-to-receptor rows as ligand edges."
            elif ligand in {"KIRREL", "KIRREL3"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "KIRREL-family proteins are cell-adhesion receptors with homophilic or heterophilic contact context, but the exact KIRREL paralog and target orientation for these rows were not verified."
                limitations = "Preserve KIRREL paralog and adhesion orientation; do not encode self-loops or infer a soluble ligand route from adhesion-family membership."
            elif ligand == "KISS1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "KISS1 receptor biology is centered on KISS1R, not MMP24 in the public row."
                limitations = "Require mature kisspeptin form and direct KISS1R assay; represent MMP24 protease biology separately."
            elif ligand == "KL":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Klotho/KL is a co-receptor or context-dependent extracellular regulator for FGF23 and related pathways, but the public rows do not resolve the complete KL/FGFR or KL/IGF receptor topology for each target."
                limitations = "Retain intact Klotho-containing receptor complexes and exact co-receptor roles; do not materialize KL as a generic standalone ligand for FGFR, IGF1R, INSR or TRPV channels."
            elif ligand.startswith("KLK"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "KLK-family labels are serine proteases, not mature extracellular neurotrophin, erythropoietin or coagulation ligands for the listed receptors."
                limitations = "Represent protease processing and protease-activated receptor mechanisms separately; do not materialize KLK-to-EPOR/NTRK/NGFR rows without exact mature-ligand evidence."
            elif ligand.startswith(("LAMA", "LAMB", "LAMC")):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Laminin-chain rows represent extracellular-matrix isoforms and receptor complexes, but the public candidates do not resolve the complete mature laminin composition, domain and integrin/syndecan/SV2 receptor topology for each pair."
                limitations = "Require exact laminin heterotrimer or domain, receptor complex, species and primary assay; do not treat a single laminin chain as the complete ligand or transfer specificity across laminin isoforms."
            elif ligand == "LAYN":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "LAYN is a membrane immune-cell protein, not a mature extracellular ligand for GP5 or LY6G6F."
                limitations = "Represent LAYN cell-surface and immune-adhesion biology separately; do not invert membrane protein identity into a ligand edge without direct primary support."
            elif ligand.startswith("LCN"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Lipocalin-family proteins can be secreted transport or immune-modulatory factors, but the listed PTPRC and FCGR2B targets were not verified as exact direct LCN11/LCN2 receptor mechanisms in this pass."
                limitations = "Require exact lipocalin isoform, receptor or uptake complex, species and primary binding or functional assay; do not transfer LCN2/LCN-family context across immune receptors."
            elif ligand == "LFNG":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "LFNG is a glycosyltransferase that modifies Notch receptors, not a mature extracellular ligand for NOTCH1 or NOTCH2."
                limitations = "Represent Fringe-dependent Notch receptor modification in the receptor-proximal layer; do not materialize LFNG-to-Notch rows as ligand edges."
            elif ligand == "LGALS3":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Galectin-3 is a secreted and intracellular lectin with glycan-dependent adhesion and receptor-clustering context, but the listed ANXA2 and PTPRK targets were not verified as exact direct LGALS3 receptor pairs."
                limitations = "Require exact LGALS3 form, glycan/receptor context, species and primary assay; do not transfer galectin family binding across unrelated membrane proteins."
            elif ligand == "LGALS3BP":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "LGALS3BP is a secreted matrix/immune-associated protein, but an exact LGALS3BP-to-CD33 receptor experiment was not verified in this pass."
                limitations = "Require direct LGALS3BP/CD33 binding or receptor-dependent function; do not infer CD33 activation from secreted-protein or lectin-family context."
            elif ligand.startswith("LGI"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "LGI-family proteins have synaptic and ADAM-family receptor contexts, but the public rows do not resolve exact LGI isoform, mature domain and direct target mechanism for these candidates."
                limitations = "Require exact LGI isoform, receptor orientation, species and primary binding or functional assay; do not transfer LGI1/ADAM22/23 evidence across paralogs or unrelated membrane proteins."
            elif ligand.startswith("LILR"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "LILR/LILRA/LILRB-family labels are immune receptor proteins, not mature extracellular ligands for CNTFR, FGFR, LAIR1 or other listed targets."
                limitations = "Represent LILR receptor orientation and immune-complex signaling separately; do not invert receptor-family identities into ligand edges or transfer specificity across LILR paralogs."
            elif ligand.startswith("LIN7"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "LIN7A/LIN7B are intracellular polarity and membrane-trafficking scaffold proteins, not mature extracellular ligands for the listed channels or transporters."
                limitations = "Represent scaffold and intracellular membrane-complex biology separately; do not materialize LIN7-to-receptor rows as ligand edges."
            elif ligand == "LINGO4":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "LINGO-family proteins are neural membrane co-receptors/adhesion proteins, but an exact LINGO4-to-NFASC receptor interaction was not verified in this pass."
                limitations = "Require direct LINGO4/NFASC binding or receptor-dependent function; do not transfer LINGO1 receptor-complex evidence to LINGO4."
            elif ligand == "LIPA":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "LIPA is a lysosomal acid lipase, not a mature extracellular ligand for RORC."
                limitations = "Represent lipid metabolism separately; do not materialize LIPA-to-nuclear-receptor rows as ligand edges."
            elif ligand == "LMAN1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "LMAN1 is an intracellular cargo receptor/chaperone, not a mature extracellular ligand for MCFD2."
                limitations = "Represent ER cargo trafficking separately; do not materialize LMAN1-MCFD2 as a ligand-receptor edge."
            elif ligand.startswith("LOC"):
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "The LOC-prefixed public identifier was not resolved to a verified mature ligand identity and exact receptor assay in this pass."
                limitations = "Resolve the species-specific identifier and protein form before promotion; do not infer receptor specificity from an unresolved LOC label."
            elif ligand == "LPL":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "LPL is a lipase enzyme and the public row does not define it as a mature signaling ligand for CD44."
                limitations = "Represent lipoprotein metabolism and enzyme/cofactor interactions separately; do not materialize LPL-to-CD44 as a ligand edge without exact primary support."
            elif ligand.startswith("LRCH") or ligand.startswith("LRFN") or ligand.startswith("LRIT"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "LRCH/LRFN/LRIT-family rows describe adhesion, synaptic or immune cell-surface proteins, but the exact paralog, orientation and direct receptor mechanism for these candidates were not verified."
                limitations = "Preserve family and cis/trans orientation; require exact pair-level primary evidence before promotion and do not infer soluble ligand signaling from adhesion-family membership."
            elif ligand == "LRIG1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "LRIG1 is a membrane receptor regulator and ligand-like EGFR-family modulator, but the public rows do not establish the listed ERBB or MOG targets as exact direct LRIG1 ligand-receptor edges."
                limitations = "Represent LRIG1-EGFR/ERBB regulation and receptor trafficking separately; do not invert receptor-regulatory context into a generic soluble ligand edge."
            elif ligand == "LRPAP1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "LRPAP1 is a receptor-associated protein/chaperone for LDL-receptor family trafficking, not a mature extracellular ligand for CD320, LDLR, LRP8 or SIRPA."
                limitations = "Represent receptor-chaperone and lipoprotein-uptake biology separately; do not materialize LRPAP1-to-receptor rows as ligand edges."
            elif ligand.startswith(("LRRC", "LRRN", "LRRTM", "LRTM")):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "LRRC/LRRN/LRRTM/LRTM-family rows describe neuronal or immune cell-surface adhesion proteins, but the exact paralog, orientation and direct receptor mechanism for these candidates were not verified."
                limitations = "Preserve cell-adhesion and synaptic receptor-complex context; require exact pair-level primary evidence before promotion and do not infer soluble ligand signaling from family membership."
            elif ligand == "LSAMP":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "LSAMP is a neural cell-adhesion protein with contactin/OPCML-family context, but the listed NEGR1 and OPCML pairs were not verified as exact direct LSAMP receptor interactions in this pass."
                limitations = "Require exact LSAMP partner, orientation, species and primary assay; do not transfer neural adhesion-family evidence across L1/OPCML/NEGR paralogs."
            elif ligand == "LTA":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "Lymphotoxin-alpha signaling is receptor- and complex-specific, while the LTA-to-RIPK1 row does not represent a direct extracellular receptor edge because RIPK1 is an intracellular kinase."
                limitations = "Retain LTA/TNFR and LTBR complex biology separately; represent RIPK1 as intracellular continuation, not as the extracellular receptor."
            elif ligand.startswith("LY6"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "LY6-family labels are GPI-anchored or membrane-associated proteins, not mature soluble ligands for the listed receptors and adhesion proteins."
                limitations = "Represent LY6 family membrane and immune-complex biology separately; do not invert membrane-protein identities into ligand edges without exact primary support."
            elif ligand == "LY9":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "LY9 is an immune receptor, not a mature ligand for TNFRSF17/BCMA."
                limitations = "Represent LY9 receptor signaling separately; do not invert receptor-family identity into a ligand edge."
            elif ligand == "LYPD3":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "LYPD3 is a membrane GPI-anchored protein with adhesion and protease-associated context, but the listed AGR2 and IL20RA targets were not verified as exact direct LYPD3 receptor mechanisms."
                limitations = "Require direct LYPD3 target binding or receptor-dependent function; do not transfer GPI-anchored adhesion context across unrelated targets."
            elif ligand == "MADCAM1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "MAdCAM1 is an endothelial adhesion ligand with integrin and lectin context, but the listed CD44 and SIGLEC targets were not verified as exact direct MADCAM1 receptor pairs in this pass."
                limitations = "Retain exact MAdCAM1-integrin and adhesion-complex evidence separately; require pair-specific primary support before promotion and do not infer receptor binding from endothelial expression."
            elif ligand == "MANSC1":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "MANSC1 remains an unresolved extracellular protein label in this pass, and no exact MANSC1-to-GPR55 receptor experiment was verified."
                limitations = "Resolve the protein form and direct receptor assay before promotion; do not infer GPR55 specificity from public-database membership alone."
            elif ligand == "MCAM":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "MCAM/CD146 is a membrane adhesion receptor/coreceptor, not a mature ligand for CD226, FGFR4 or TMEM132A."
                limitations = "Represent MCAM adhesion and receptor-crosstalk orientation separately; do not invert MCAM into a ligand edge without exact primary support."
            elif ligand == "MDK":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Midkine is an extracellular growth-factor-like protein with integrin, PTP and lipoprotein-receptor co-receptor contexts, but the exact MDK-to-ITGA4/PTPRB/SORL1 mechanisms were not resolved as binary direct edges in this pass."
                limitations = "Retain exact MDK receptor-complex and co-receptor evidence separately; require ligand form, receptor topology and primary assay before promotion."
            elif ligand == "MELTF":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "MELTF/MTF1 is a membrane iron-transport receptor/protein, not a mature ligand for TFRC."
                limitations = "Represent iron-uptake receptor orientation and membrane complex biology separately; do not invert MELTF into a ligand edge."
            elif ligand == "MFAP3L":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "MFAP3L is an extracellular-matrix microfibril-associated protein, but the listed CEACAM and MPZL2 targets were not verified as exact direct MFAP3L receptor interactions."
                limitations = "Require exact MFAP3L domain, receptor or adhesion partner, species and primary assay; do not transfer matrix-family evidence across CEACAM or immunoglobulin-superfamily proteins."
            elif ligand.startswith("MIF"):
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "MIF has established CD74/CXCR4 and inflammatory signaling contexts, but the listed TNFRSF14 target was not verified as an exact direct MIF receptor in this pass."
                limitations = "Require direct MIF/TNFRSF14 binding or receptor-dependent function; do not transfer CD74/CXCR4 specificity to TNFRSF14."
            elif ligand.startswith("MILL"):
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "MILL1/MILL2 remain unresolved immune-family labels in this pass, and no exact mature ligand identity or direct HCST/KLRK1 receptor assay was verified."
                limitations = "Resolve the source identifiers and protein forms before promotion; do not infer NKG2D-ligand specificity from unresolved MILL labels."
            elif ligand.startswith("MMP"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "MMP-family labels are extracellular proteases that process matrix, receptor or ligand substrates; the public rows do not establish conventional mature ligand-receptor edges."
                limitations = "Represent proteolytic cleavage, shedding and receptor-proximal remodeling separately; do not materialize MMP-to-substrate or MMP-to-receptor rows as ligand edges without exact primary support."
            elif ligand == "MPDZ":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "MPDZ is an intracellular polarity and tight-junction scaffold, not a mature extracellular ligand for claudin or JAM-family targets."
                limitations = "Represent tight-junction scaffolding separately; do not materialize MPDZ-to-junction-protein rows as ligand edges."
            elif ligand == "MPIG6B":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "MPIG6B is a membrane/platelet-associated protein with immune and adhesion context, but the listed AGER, BOC, IL1RL1, OSCAR, ROBO or UNC5 targets were not verified as exact direct MPIG6B receptors."
                limitations = "Require exact MPIG6B orientation, receptor, species and primary assay; do not transfer platelet or adhesion-family evidence across unrelated targets."
            elif ligand == "MPZ":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "MPZ/P0 is a myelin adhesion protein with neural cell-surface context, but the listed immune-receptor and cytokine targets were not verified as exact direct MPZ receptor pairs."
                limitations = "Require exact MPZ ectodomain, receptor orientation and primary assay; do not transfer myelin adhesion or immune-family evidence across paralogs."
            elif ligand.startswith("MPZL"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "MPZL-family labels are membrane immunoglobulin-superfamily proteins, not mature soluble ligands for the listed targets."
                limitations = "Represent MPZL adhesion and receptor-complex orientation separately; do not invert membrane proteins into ligand edges without direct primary support."
            elif ligand == "MSMB":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "MSMB is a secreted prostate-associated protein, but an exact MSMB-to-GPR55 receptor experiment was not verified in this pass."
                limitations = "Require direct MSMB/GPR55 binding or receptor-dependent function; do not infer GPR55 specificity from secreted-protein status."
            elif ligand == "MSN":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "MSN/moesin is an intracellular membrane-cytoskeletal linker, not a mature extracellular ligand for SLC9A1."
                limitations = "Represent ezrin-radixin-moesin cytoskeletal mechanisms separately; do not materialize MSN-to-transporter rows as ligand edges."
            elif ligand == "MSTN":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:11459935", "PMID:14517293", "PMID:33219121"]
                species = "mouse; human comparator"
                summary = "Primary myostatin evidence supports activin type-II receptor engagement and type-I receptor-complex signaling, but the public single-subunit rows do not establish each component as an independent binary receptor edge."
                limitations = "Retain mature MSTN and intact ACVR2A/ACVR2B with ACVR1B or TGFBR1 receptor-complex topology; do not collapse complex evidence into unsupported free-subunit edges."
            elif ligand.startswith("MUC"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Mucin-family rows can represent membrane glycoprotein, secreted-mucus or glycan-mediated interactions, but the exact mucin form, glycan context and direct receptor mechanism for these targets were not verified."
                limitations = "Require exact mucin isoform/domain, glycosylation state, receptor orientation and primary assay; do not transfer MUC1/MUC2/MUC4 biology across lectin, AGR2 or ERBB-family targets."
            elif ligand.startswith("MUG"):
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "MUG1/MUG2 remain unresolved public protein labels in this pass, and no exact mature ligand identity or direct MMP/SCTR receptor assay was verified."
                limitations = "Resolve the source identifiers and protein forms before promotion; do not infer receptor specificity from unresolved MUG labels."
            elif ligand == "MXRA8":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "MXRA8 is a cell-surface adhesion/immune protein, but the listed JAM3 target was not verified as an exact direct MXRA8 receptor interaction in this pass."
                limitations = "Require direct MXRA8/JAM3 binding or receptor-dependent function; do not infer an adhesion edge from shared membrane localization."
            elif ligand.startswith("NAALAD"):
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "NAALADL1 remains an unresolved membrane/enzyme-family label for this candidate, and no exact mature ligand identity or direct CD96 assay was verified."
                limitations = "Resolve the source identifier and protein form before promotion; do not infer CD96 specificity from database membership alone."
            elif ligand == "NAMPT":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "NAMPT is an intracellular enzyme and extracellular cytokine-like factor in some contexts, but these free integrin rows describe expression or adhesion regulation rather than a verified mature NAMPT-integrin ligand edge."
                limitations = "Retain exact extracellular NAMPT receptor evidence separately; do not materialize NAMPT-to-ITGA5/ITGB1 from integrin-expression or adhesion context alone."
            elif ligand.startswith("NCAM"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "NCAM-family candidates describe neural cell-adhesion and co-receptor contexts, but the exact NCAM isoform, cis/trans orientation and direct mechanism for the listed targets were not verified in this pass."
                limitations = "Preserve NCAM family, polysialylation/isoform state and adhesion orientation; require exact pair-level primary evidence before promotion and do not infer soluble ligand signaling."
            elif ligand == "NDP" and receptor == "LRP5":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Norrin/NDP signaling requires the FZD4-LRP5/6 receptor complex and often TSPAN12, so the public NDP-to-LRP5 row is retained as a component-level receptor context rather than a standalone binary edge."
                limitations = "Preserve the intact NDP/FZD4/LRP5/6/TSPAN12 topology and do not infer LRP5 as a complete standalone NDP receptor."
            elif ligand.startswith("NECTIN"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Nectin-family rows describe homophilic/heterophilic adhesion and immune-checkpoint interactions, but the exact Nectin paralog, receptor orientation and pair-specific primary support for these candidates were not all resolved in this pass."
                limitations = "Preserve Nectin isoform, cis/trans orientation and known CD96, CD226, TIGIT, PVRIG or CADM context; do not encode self-loops or transfer evidence across Nectin paralogs."
            elif ligand.startswith("NEGR") or ligand.startswith("NEO1"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "NEGR/Neogenin-family candidates describe neural adhesion and guidance contexts, but the exact receptor or co-receptor topology for these rows was not verified as a direct primary-supported ligand edge."
                limitations = "Require exact paralog, orientation and primary assay; do not transfer neural guidance or morphogen co-receptor evidence across NEGR/NEO1 targets."
            elif ligand.startswith("NETO") or ligand.startswith("NFASC"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "NETO/NFASC-family candidates describe neuronal adhesion or ion-channel co-receptor contexts, but the exact receptor complex and pair-specific primary mechanism were not verified."
                limitations = "Preserve neural adhesion and co-receptor topology; require direct pair-level primary evidence before promotion and do not infer soluble ligand signaling."
            elif ligand == "NGF":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "NGF signaling is centered on NTRK1 and p75NTR; the listed ERBB2, TRPV1 and other targets may reflect crosstalk or sensitization rather than direct canonical ligand-receptor binding."
                limitations = "Retain exact NGF/NTRK1/NGFR receptor-complex evidence and distinguish TRPV1 sensitization from direct binding; do not promote unrelated target rows without pair-specific primary support."
            elif ligand == "NLGN1" and receptor == "NRXN3":
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E005169"
                primary = ["PMID:20519524"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "as stated in primary model/assay"
                summary = "The graph already contains the primary-supported neuroligin-1 to beta-neurexin-3 transsynaptic adhesion relationship."
                limitations = "Preserve splice-isoform and synaptic adhesion context; do not duplicate the edge or infer a universal intracellular or terminal-TF route from adhesion alone."
            elif ligand == "NMU":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Neuromedin U receptor biology is centered on NMUR1/MLNR and NMUR2/MLN2R, not the adrenergic receptor listed here."
                limitations = "Require mature NMU and direct NMUR-family assay; do not transfer neuromedin-U specificity to unrelated GPCRs."
            elif ligand == "NODAL":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Nodal signaling is receptor-complex and Cripto/CFC1 dependent, while the public rows do not resolve the complete NODAL type-I/type-II receptor topology as a single binary edge."
                limitations = "Retain exact NODAL/ACVR/ACVR2/CFC1 complex evidence; do not materialize isolated or composite subunits without exact primary complex-level support."
            elif ligand == "NOG":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Noggin is a secreted BMP antagonist that binds BMP ligands and modulates receptor access, but the public NOG-to-BMPR rows do not establish NOG as a conventional activating ligand for those receptors."
                limitations = "Represent Noggin-BMP sequestration and receptor-access modulation separately; do not materialize NOG-to-BMPR as an activating ligand edge."
            elif ligand == "NPFF":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "NPFF receptor biology is centered on NPFFR1/NPFFR2, not MAS1/GPRC6-family receptor labels in this row."
                limitations = "Require mature NPFF peptide and direct NPFFR-family assay; do not transfer neuropeptide specificity to unrelated GPCRs."
            elif ligand == "NPHS1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "NPHS1/nephrin is a membrane slit-diaphragm adhesion protein, not a mature ligand for TRPC6."
                limitations = "Represent nephrin-podocyte adhesion and channel-complex biology separately; do not invert membrane adhesion proteins into ligand edges."
            elif ligand == "NPPB":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "NPPB/BNP receptor biology is centered on NPR1/NPR2, while DPP4 and FAP are proteases rather than canonical NPPB receptors."
                limitations = "Require mature natriuretic peptide and direct NPR-family assay; represent DPP4/FAP protease biology separately."
            elif ligand == "NPY":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "NPY signaling is receptor-family and peptide-form specific; the public rows mix canonical NPY-family receptors with unrelated GPCRs and protease targets, so exact receptor assignment is not asserted here."
                limitations = "Require mature NPY form and direct NPY receptor assay; do not transfer NPY-family specificity across adrenergic, melatonin, glutamate, DPP4 or orphan receptor targets."
            elif ligand == "NRG1" and receptor == "ERBB2+ERBB3":
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E000363;M21B-E001759"
                primary = ["PMID:34759323", "PMID:9693119"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "as stated in primary model/assay"
                summary = "The graph already contains primary-supported NRG1/NRG1-beta engagement of the ERBB2:ERBB3 receptor complex."
                limitations = "Preserve ERBB2:ERBB3 heterodimer topology and NRG1 isoform context; do not collapse the complex into an ERBB2-alone edge."
            elif ligand.startswith("NRG"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Neuregulin-family signaling is ErbB-paralog and receptor-complex dependent; the graph contains exact NRG1-to-ERBB3, ERBB4 and ERBB2:ERBB3 evidence, but the public rows also include isolated ERBB2 or other unverified ErbB targets."
                limitations = "Preserve NRG isoform, EGF-like ligand form and ERBB receptor-complex topology; do not transfer NRG1 specificity to NRG2-4 or collapse ERBB2 heterodimer evidence into an ERBB2-alone edge."
            elif ligand == "NRP1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "NRP1/neuropilin-1 is a membrane co-receptor, not a mature ligand for FLT1, KDR, PDGF receptors, PLXNA1 or the listed targets."
                limitations = "Represent neuropilin co-receptor complexes and VEGF/semaphorin orientation separately; do not invert NRP1 into ligand position."
            elif ligand.startswith("NRXN"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Neurexin-family rows describe transsynaptic adhesion and splice-dependent partner recognition, but the exact neurexin isoform, splice state and receptor orientation for these candidates were not all resolved."
                limitations = "Preserve neurexin splice isoform and transsynaptic orientation; require exact pair-level primary evidence before promotion and do not transfer NLGN/NRXN specificity across paralogs."
            elif ligand == "NT5E":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "NT5E/CD73 is an ectoenzyme that generates extracellular adenosine, not a mature ligand for FCRL1."
                limitations = "Represent adenosine production and ectoenzyme signaling separately; do not materialize NT5E-to-receptor rows as ligand edges without exact support."
            elif ligand.startswith("NTM"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "NTM/neurtrimin-family rows describe neural and immune cell-adhesion contexts, but the exact partner and receptor topology for these candidates were not verified as direct primary-supported ligand edges."
                limitations = "Preserve NTM family, GPI/membrane orientation and adhesion context; require exact pair-level primary evidence before promotion."
            elif ligand == "NTNG1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Netrin-G1/NTNG1 is a neural GPI-anchored adhesion ligand with receptor-family context, but the listed CD300 and SIGLEC targets were not verified as exact direct NTNG1 receptors."
                limitations = "Require direct NTNG1 target binding or receptor-dependent function; do not transfer neural adhesion evidence to unrelated lectin receptors."
            elif ligand == "NTS":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "Neurotensin receptor biology is centered on NTSR1/NTSR2, not NGFR in the public row."
                limitations = "Require mature neurotensin and direct NTSR-family assay; do not transfer neurotensin specificity to p75NTR/NGFR."
            elif ligand in {"NXPH1", "NXPH3"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Neurexophilin-family proteins have synaptic neurexin-binding contexts, but the exact isoform and NRXN3 interaction for this row were not independently verified in this pass."
                limitations = "Require exact NXPH/NRXN isoform, splice state and primary binding assay; do not transfer synaptic adhesion evidence across paralogs."
            elif ligand == "OCLN":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "OCLN/occludin is a tight-junction membrane protein, not a mature extracellular ligand for claudins or TGFBR receptors."
                limitations = "Represent tight-junction and receptor-crosstalk biology separately; do not invert junctional membrane proteins into ligand edges."
            elif ligand == "OGN":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "OGN/osteoglycin is an extracellular-matrix proteoglycan, but the public OGN-to-H2EB2 row was not verified as an exact direct receptor mechanism."
                limitations = "Require exact OGN domain, partner, species and primary assay; do not infer immune receptor binding from matrix localization."
            elif ligand == "OIT1":
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "OIT1 remains an unresolved public protein label in this pass, and no exact mature ligand identity or direct FPR1/FPR2 assay was verified."
                limitations = "Resolve the source identifier and protein form before promotion; do not infer formyl-peptide receptor specificity from an unresolved OIT1 label."
            elif ligand == "OPCML":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "OPCML is a GPI-anchored neural adhesion protein with homophilic/heterophilic partner context, but the listed NEGR1, NTM and OPCML rows do not establish a complete direct receptor topology for each candidate."
                limitations = "Preserve OPCML orientation and homophilic self-interaction boundary; do not encode self-loops or transfer neural adhesion specificity across paralogs."
            elif ligand.startswith("ORM"):
                disposition = "no_primary_evidence_found"
                layer = "candidate_only_review_locator"
                summary = "ORM1/ORM3 are secreted acute-phase glycoproteins, but exact direct ORM-to-CCR5 receptor evidence was not verified in this pass."
                limitations = "Require mature ORM form and direct CCR5 binding or activation assay; do not infer chemokine-receptor activity from secreted glycoprotein status."
            elif ligand in {"P4HB", "PAM", "PATJ"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses an intracellular chaperone/enzyme or junctional scaffold as the ligand label, not a mature extracellular ligand for the listed target."
                limitations = "Represent ER, enzymatic and tight-junction mechanisms separately; do not materialize intracellular protein associations as ligand edges."
            elif ligand == "PAPLN":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "PAPLN/papilin is an extracellular-matrix protein, but the listed CD200, Nectin4 and SIRPA targets were not verified as exact direct PAPLN receptor mechanisms."
                limitations = "Require exact PAPLN domain, receptor or adhesion partner, species and primary assay; do not transfer matrix-family evidence across immune and adhesion receptors."
            elif ligand in {"PRSS1", "PRSS3", "PRSS3L"} and receptor in {"F2R", "F2RL1", "F2RL2", "F2RL3"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Trypsin-family proteases can activate protease-activated receptor family members by proteolytic unmasking, but the current graph release records thrombin and factor-Xa branches rather than an exact PRSS1/PRSS3/PRSS3L pair for every listed PAR."
                limitations = "Require mature protease, cleavage-site, receptor-paralog and assay-specific primary evidence before promotion; preserve PAR1-4 proteolytic activation and do not infer a generic protease-to-PAR edge across paralogs."
            elif ligand == "PVR" and receptor == "NECTIN3":
                disposition = "already_present_reverse_orientation"
                matched_ids = "M21B-E011623"
                primary = ["PMID:23027581", "PMCID:PMC3792040"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "The graph contains the primary-supported Nectin-3-to-PVR heterophilic adhesion relationship in the reverse orientation of this public row."
                limitations = "Preserve Nectin-3/PVR adhesion and endothelial transendothelial-migration context; do not add a duplicate reverse edge or infer a soluble ligand route."
            elif ligand == "PVR" and receptor == "PVRIG":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "PVR/CD155 is a ligand for TIGIT, CD226 and CD96, whereas PVRIG/CD112R is the receptor for Nectin-2/CD112 rather than an established PVR ligand target."
                limitations = "Preserve the PVR checkpoint/adhesion branches and the separate Nectin-2-PVRIG axis; do not transfer specificity between PVR and PVRIG."
            elif ligand == "QRFP" and receptor == "QRFPRL":
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E005549"
                primary = ["PMID:12714592", "DOI:10.1074/jbc.M302945200"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "The graph already contains primary-supported mature QRFP/26RFa activation of QRFPR under the QRFPRL receptor alias."
                limitations = "Preserve mature RF-amide peptide processing, QRFPR alias and heterologous GPCR assay context; no SCI or terminal-TF inference is asserted."
            elif ligand == "RAET1E" and receptor == "KLRK1":
                disposition = "already_present_exact_or_alias"
                matched_ids = "M21B-E005632"
                primary = ["PMID:12732206", "DOI:10.1016/S0006-291X(03)00714-9"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "human"
                summary = "The graph already contains primary-supported ULBP4/RAET1E binding to NKG2D/KLRK1 with NK-cell cytotoxicity output."
                limitations = "Preserve ULBP4 transmembrane/shedding and NKG2D-DAP10 context; no SCI or terminal-TF inference is asserted."
            elif ligand == "RET" and receptor in {"GFRA1", "GFRA2", "GFRA3", "GFRA4"}:
                disposition = "already_present_reverse_orientation"
                matched_ids = {"GFRA1": "M21B-E000322", "GFRA2": "M21B-E000328", "GFRA3": "M21B-E000329", "GFRA4": "M21B-E000989"}[receptor]
                primary = {"GFRA1": ["PMID:15722196", "PMID:10545102"], "GFRA2": ["PMID:31392261", "PMID:29414779"], "GFRA3": ["PMID:9883723", "PMID:17013378", "PMID:16765900"], "GFRA4": ["PMID:11116144"]}[receptor]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                species = "as stated in primary model/assay"
                summary = "The graph contains the corresponding GDNF-family ligand to GFRA:RET receptor-complex relationship; this public row reverses the signaling orientation by placing RET in ligand position."
                limitations = "Preserve the tripartite GDNF-family/GFRA/RET topology and RET kinase role; do not add a duplicate RET-to-GFRA ligand edge."
            elif ligand == "RGMB" and receptor in {"BMPR1B", "BMPR2"}:
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000832"
                primary = ["PMID:25938661"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human"
                summary = "Primary structural work supports RGMB binding to BMP2 and an RGMB-BMP2-NEO1 bridging architecture, but not direct RGMB binding to the listed BMPR subunits as isolated receptors."
                limitations = "Preserve RGMb-mediated BMP2 co-receptor topology and require exact BMPR-containing complex evidence before promotion; do not decompose the bridge into a direct RGMB-BMPR1B/BMPR2 edge."
            elif ligand == "RLN3":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E007105;M21B-E007106"
                primary = ["PMID:24802387", "DOI:10.1111/febs.12830"]
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human"
                summary = "Primary relaxin-3 studies support cognate/cross-reactive signaling at RXFP3 and RXFP1/RXFP4, while the listed public receptors are not those validated relaxin-family targets."
                limitations = "Preserve mature relaxin-3 processing and RXFP receptor selectivity; do not transfer RXFP1/RXFP4 evidence to unrelated GPCRs."
            elif ligand in {"PTGS2", "PTPN6", "PTPRC", "PTPRK", "PTPRM", "PTPRZ1", "RIMS1", "RIMS2"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses an intracellular enzyme, phosphatase, receptor-family protein or presynaptic scaffold in ligand position rather than a mature extracellular ligand."
                limitations = "Represent phosphatase, receptor, adhesion and synaptic-scaffold mechanisms in their appropriate layers; do not invert receptor or intracellular proteins into ligand position."
            elif ligand == "PLTP" and receptor == "APOA1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "PLTP is a phospholipid-transfer protein and APOA1 is an apolipoprotein, not a plasma-membrane receptor in this candidate orientation."
                limitations = "Retain the primary-supported PLTP-ABCA1 lipid-efflux interaction separately; do not invert lipoprotein-transfer or apolipoprotein associations into a canonical ligand-receptor edge."
            elif ligand.startswith("PLXNA"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "PLXNA1/PLXNA2 are plexin receptor-family proteins, not mature extracellular ligands for the listed targets; the public rows invert receptor-ligand orientation or omit the required semaphorin complex."
                limitations = "Represent semaphorin-plexin and neuropilin-plexin complexes in receptor orientation; do not materialize plexin proteins as ligands without exact noncanonical primary support."
            elif ligand == "POSTN" and receptor in {"ITGAV", "ITGB3", "ITGB5"}:
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000710;M21B-E000711;M23B-E000243;M23B-E000244"
                primary = ["PMID:19695571", "PMCID:PMC2841688", "DOI:10.1016/j.atherosclerosis.2009.07.046"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse"
                summary = "Primary periostin studies support alphaVbeta3 and alphaVbeta5 integrin-complex signaling and migration, while these public rows split the complexes into individual subunits."
                limitations = "Preserve alphaVbeta3/alphaVbeta5 complex topology and FAK/migration context; do not promote isolated ITGAV, ITGB3 or ITGB5 as complete receptors or infer a terminal TF."
            elif ligand == "PPBP":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "PPBP is a platelet chemokine precursor associated with processed CXCL7/chemokine biology, not a verified mature ligand for the unrelated receptors listed here."
                limitations = "Require the processed chemokine form and direct receptor assay; preserve the graph's CXCL7-CXCR2 evidence and do not transfer it to ACKR1, opioid, adrenergic, glutamate or melatonin receptors."
            elif ligand.startswith("PRL"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Placental-lactogen/prolactin-family candidates are biologically plausible at PRLR, but the current graph directly supports canonical prolactin-PRLR binding and does not verify each listed paralog or ERBB2 row."
                limitations = "Require exact prolactin-family paralog, species, mature form and PRLR or ERBB assay before promotion; do not transfer canonical prolactin evidence across placental-lactogen paralogs."
            elif ligand.startswith("PCDH"):
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = reviewed
                species = "as stated in primary model/assay"
                summary = "Protocadherin-family rows describe isoform-specific neuronal cell-adhesion recognition, but the exact paralog, cis/trans orientation and direct primary evidence for these integrin or protocadherin candidates were not resolved."
                limitations = "Preserve protocadherin isoform and adhesion orientation; do not promote mismatched paralog pairs or infer soluble ligand signaling from adhesion-family membership."
            elif ligand == "PDGFB" and receptor == "PDGFRA+PDGFRB":
                disposition = "new_primary_supported_edge_candidate"
                matched_ids = "M21B-E000182;M21B-E000761"
                primary = ["PMID:20534510", "PMID:7679113"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human"
                summary = "The graph contains primary-supported PDGF-BB binding to PDGFRB and PDGFRA receptor dimers; together these support a PDGFR-alpha/beta complex candidate without asserting a single unbounded binary subunit edge."
                limitations = "Preserve PDGF-BB dimerization and PDGFRA/PDGFRB receptor-complex topology; materialize only after exact heterodimer normalization and do not infer a terminal TF or SCI-specific output."
            elif ligand == "PDGFB" and receptor == "ITGAV":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M23B-E000229"
                primary = ["PMID:12881526"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "human; mouse"
                summary = "Primary glioblastoma work supports PDGFB-stimulated PDGFRB cooperation with alphaV-integrin adhesion during migration, but not direct PDGFB binding to ITGAV alone."
                limitations = "Preserve the alphaVbeta3/PDGFRB complex and migration context; do not decompose alphaVbeta3 into ITGAV alone or promote this as a canonical ligand-receptor binding edge."
            elif ligand == "PDGFD" and receptor == "PDGFRA+PDGFRB":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E000521"
                primary = ["PMID:11331881", "DOI:10.1038/35074588"]
                layer = "ligand_receptor_binding_or_activation"
                species = "human"
                summary = "Primary PDGF-DD studies support protease-activated PDGFRB specificity; the listed PDGFRA/PDGFRB complex row is retained as a topology question rather than promoted as direct dual-subunit binding."
                limitations = "Require exact PDGF-DD/PDGFRA-containing complex evidence before promotion; preserve proteolytic activation and PDGFRB-specificity boundaries."
            elif ligand == "PDCD1LG2" and receptor in {"PDCD2", "TNFRSF11A"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "PDCD1LG2/PD-L2 is a ligand for PDCD1/PD-1, not for PDCD2 or TNFRSF11A in the listed rows."
                limitations = "Retain the primary-supported PDCD1LG2-PDCD1 checkpoint relationship; do not transfer PD-L2 specificity to paralogous or unrelated receptors."
            elif ligand == "PDGFA" and receptor == "PDGFRB":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "ligand_receptor_binding_or_activation"
                primary = ["PMID:7679113", "PMID:2842148", "PMID:1318231"]
                species = "human"
                summary = "Primary isoform-specific binding studies show PDGF-AA/PDGFA binding predominantly to PDGFRA, whereas high-affinity PDGFRB binding is mediated by PDGF-BB or PDGF-AB; the public PDGFA-to-PDGFRB row is therefore not promoted as a direct canonical edge."
                limitations = "Preserve PDGF-AA versus PDGF-AB/BB isoform and PDGFRA/PDGFRB receptor-subtype boundaries; require a direct PDGF-AA-PDGFRB study before reconsideration."
            elif ligand == "PDGFA" and receptor == "FURIN":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "PDGFA/PDGF-AA is a secreted growth-factor ligand, whereas FURIN is a proprotein convertase rather than its canonical signaling receptor."
                limitations = "Represent proteolytic processing separately and require a direct PDGFA-FURIN assay before any noncanonical edge is considered."
            elif ligand == "PDX1" and receptor == "SLC2A2":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "PDX1 is a transcription factor and SLC2A2/GLUT2 is a target gene or transporter context; this is not a ligand-receptor relationship."
                limitations = "Represent PDX1-dependent gene regulation in the transcriptional layer; do not materialize intracellular TF-to-gene relationships as extracellular ligand edges."
            elif ligand == "PECAM1" and receptor in {"ITGAV", "ITGB3"}:
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M23B-E000012;M21B-E006569"
                primary = ["PMID:7542249", "PMCID:PMC2199946", "DOI:10.1083/jcb.130.2.451", "PMID:8838667", "DOI:10.1242/jcs.109.2.437"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "mixed mammalian"
                summary = "Primary adhesion studies support PECAM1 interaction with the alphaVbeta3 integrin complex, while the public rows split that heteromer into ITGAV or ITGB3 components."
                limitations = "Preserve alphaVbeta3 complex topology and adhesion context; do not promote isolated ITGAV or ITGB3 as complete receptors or infer a soluble signaling route."
            elif ligand == "PLAT" and receptor == "ITGB2":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M23B-E000238"
                primary = ["PMCID:PMC3402285", "PMID:22677557", "PMID:25131752"]
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "mouse; human"
                summary = "Primary macrophage studies support tPA/PLAT signaling through an annexin A2 and Mac-1 context, of which ITGB2 is only one required subunit."
                limitations = "Preserve the complete Mac-1 and annexin-A2 receptor context; do not decompose the relay into direct PLAT-ITGB2 binding or infer a terminal TF route."
            elif ligand in {"PDAP1", "PKM"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses an intracellular adaptor or metabolic enzyme as the ligand label rather than a mature extracellular signaling ligand."
                limitations = "Represent intracellular adaptor or metabolic mechanisms in their appropriate layers; do not materialize them as ligand-receptor edges without exact extracellular evidence."
            elif ligand.startswith("PIRA") or ligand == "PIRB":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "PIRA/PIRB proteins are immunoreceptor-family membrane proteins, not mature extracellular ligands for CNTFR or LAIR1 in the listed rows."
                limitations = "Preserve immunoreceptor orientation and ligand-binding context; do not invert receptor-family proteins into ligand position."
            elif ligand.startswith("ADAM"):
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "receptor_proximal_or_pathway;downstream_or_functional"
                species = "as stated in primary model/assay"
                summary = "ADAM-family sheddases can process receptors, adhesion molecules or ligands and thereby alter signaling, but the public row is not a conventional extracellular ligand-receptor binding edge."
                limitations = "Retain exact substrate cleavage, shedding and receptor-processing evidence as receptor-proximal mechanism; do not materialize ADAM-to-substrate rows as direct ligand edges or infer a unique downstream TF route."
            elif ligand in {"ABCA1", "ACE2", "ACP4", "ACTR2", "ADGRF5", "ADAM11", "ADAM20", "ADAM21", "ADAM23", "ADAM25", "ADAM39"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The public row uses a transporter, enzyme, intracellular cytoskeletal component or receptor-family protein as the ligand label rather than a mature extracellular ligand for the listed target."
                limitations = "Represent transporter, enzymatic, intracellular or receptor-receptor mechanisms in their appropriate layers; do not materialize the row as a direct ligand-receptor edge without exact primary support."
            elif ligand == "ADCYAP1":
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "PACAP/ADCYAP1 is established through PAC1/ADCYAP1R1 and VPAC-family receptor contexts, not the unrelated receptors listed in these rows."
                limitations = "Require mature PACAP isoform and direct receptor assay before promotion; do not transfer PAC1/VPAC specificity to adrenergic, RAMP or orphan GPCR candidates."
            elif ligand == "ADIPOQ":
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                species = "human; mouse; rat comparator"
                summary = "Adiponectin has primary-supported AdipoR1/AdipoR2 and LAIR1 receptor contexts, but the listed ASGR2, FFAR3, GPR152 or PROKR2 candidates were not verified as direct receptor pairings in this pass."
                limitations = "Require isoform/form-specific adiponectin binding or activation evidence; do not transfer AdipoR1/2 or LAIR1 biology to unrelated receptor families."
            elif ligand in {"ADM", "ADM2"}:
                disposition = "hold_contextual_or_complex_boundary"
                primary = reviewed
                layer = "ligand_receptor_binding_or_activation"
                species = "human; mouse; rat comparator"
                summary = "Adrenomedullin-family signaling is receptor-complex dependent, principally involving CALCRL with RAMP2/RAMP3; the listed non-CALCRL receptor rows were not verified as direct mature-ligand pairings."
                limitations = "Require exact ADM/ADM2 form, CALCRL/RAMP composition, species and receptor assay; do not infer activity at unrelated GPCRs or DCLK/MRGP receptor paralogs."
            elif ligand in {"AGRP", "AGT"}:
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "The peptide-family candidate is paired with receptors outside its established cognate receptor context: AGRP with melanocortin receptors and angiotensin peptides with AGTR receptors."
                limitations = "Require mature peptide form and direct receptor assay; do not transfer AGRP/AGTR receptor specificity to SDC, adrenergic, glutamatergic or metabolic enzymes."
            elif ligand.startswith("AKR1") or ligand.startswith("AKR1C"):
                disposition = "reject_precursor_or_non_edge_form"
                layer = "candidate_only_unverified"
                summary = "AKR-family labels are steroid or prostanoid metabolic enzymes/composites, not mature extracellular ligands for the listed receptor."
                limitations = "Represent steroid/prostanoid metabolism separately; do not materialize AKR-family enzyme composites as direct receptor ligands."
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
            elif ligand == "ALKAL1" and receptor == "ALK":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = ["PMID:34646012", "PMID:25331893", "DOI:10.1073/pnas.1412009111"]
                species = "human"
                summary = "Primary structure-function work supports ALKAL1/FAM150A engagement of the ALK-family receptor system, including ALK-complex formation, while an independent extracellular-proteome screen establishes ALKAL1 as a high-affinity activating ligand for the related LTK receptor."
                limitations = "Treat ALKAL1-ALK as a bounded receptor-complex candidate with receptor-preference and assay-context constraints; do not equate it with the stronger ALKAL2-ALK activation route or infer a complete intracellular/TF chain."
            elif ligand == "CTSG" and receptor == "FPR1":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:15210802", "DOI:10.4049/jimmunol.173.1.428"]
                species = "human; rat"
                summary = "Primary chemotaxis and receptor-transfectant experiments identify cathepsin G as an FPR1 agonist: FPR1-dependent migration, receptor internalization, weak MAPK activation and PKCζ-dependent chemotactic signaling were observed."
                limitations = "Promote as a bounded protease-to-FPR1 inflammatory route; the study reports weaker and atypical signaling than fMLP, and does not establish a universal intracellular relay or terminal-TF output."
            elif ligand == "CDH12" and receptor == "ITGA1+ITGB1":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = ["PMID:34385456"]
                species = "human"
                summary = "Primary spatial and single-cell profiling links CDH12-enriched tumor cells with CD49a/ITGA1-positive exhausted T-cell neighborhoods, but the study does not establish direct CDH12 binding to an ITGA1:ITGB1 receptor complex."
                limitations = "Retain as a cell-neighborhood and integrin-context hold; require direct CDH12-ITGA1:ITGB1 binding or receptor-proximal perturbation before promotion as a binary edge."
            elif ligand == "CEACAM2" and receptor == "SELE":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = ["PMID:1378450"]
                species = "human"
                summary = "Primary neutrophil-endothelial adhesion work supports CEA-like CD66/NCA molecules as sialyl-Lewis-x presenters participating in E-selectin-dependent adhesion, but does not resolve CEACAM2 as the exact ligand molecule."
                limitations = "Retain as CEACAM-family/selectin adhesion context; do not materialize a CEACAM2-SELE binary edge without paralog-specific binding or perturbation evidence."
            elif ligand == "H60A" and receptor == "HCST+KLRK1":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E002967"
                primary = ["PMID:11520456", "PMCID:PMC3900321"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "mouse"
                summary = "Primary H60a-NKG2D studies support direct ligand binding and NK-cell activation, and the graph already represents the KLRK1 component; the public HCST+KLRK1 row is retained as a receptor-adaptor composite rather than a single asserted edge."
                limitations = "Preserve H60a-KLRK1 and the HCST/DAP10 adaptor assembly as separate traversable layers; do not promote the full composite without exact complex-level topology evidence."
            elif ligand == "H60B" and receptor == "HCST+KLRK1":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E006718"
                primary = ["PMID:18209064"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "mouse"
                summary = "Primary H60b-NKG2D studies support direct ligand binding and NK-cell lysis, and the graph already represents the KLRK1 component; the public HCST+KLRK1 row is retained as a receptor-adaptor composite."
                limitations = "Preserve H60b-KLRK1 and HCST/DAP10 adaptor assembly separately; do not promote the complete composite as one edge without exact complex-level evidence."
            elif ligand == "H60C" and receptor == "HCST+KLRK1":
                disposition = "hold_contextual_or_complex_boundary"
                matched_ids = "M21B-E002969"
                primary = ["PMID:19342629", "PMCID:PMC3001286"]
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                species = "mouse"
                summary = "Primary H60c-NKG2D studies support direct ligand binding and cytotoxic/co-stimulatory outputs, and the graph already represents the KLRK1 component; the public HCST+KLRK1 row is retained as a receptor-adaptor composite."
                limitations = "Preserve H60c-KLRK1 and HCST/DAP10 adaptor assembly separately; do not promote the complete composite as one edge without exact complex-level evidence."
            elif "+" in receptor:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                species = "as stated in primary model/assay"
                summary = "The public row encodes a multi-subunit receptor complex or pathway prediction; component overlap does not establish the complete composite topology as one primary graph edge."
                limitations = "Retain the composite as contextual traversal evidence and require exact mature ligand, receptor-subunit composition, species and assay support before promotion."
            elif ligand == "JAG1" and receptor == "NOTCH4":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:36044575", "PMCID:PMC9432841", "DOI:10.1126/sciadv.abo7958"]
                species = "human; mouse; pig"
                summary = "Primary endothelial, mouse-artery and human coronary-cell experiments support a JAG1-NOTCH4 mechanosensing route: disturbed flow increases NOTCH4 activation, JAG1 blockade reduces N4ICD, and endothelial Jag1 deletion changes atherosclerotic and endothelial-state outputs."
                limitations = "Retain the contact-dependent Notch and disturbed-flow context; the study supports receptor-dependent pathway function rather than purified JAG1-NOTCH4 binding, and it does not assert a universal terminal-TF or SCI route."
            elif ligand == "SEMA5A" and receptor == "PLXNA3":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:25313870", "DOI:10.7554/eLife.04390"]
                species = "mouse"
                summary = "Primary Sema5A binding and neuronal-function experiments tested PlexA paralogs and found selective binding/function through PlexA1 and PlexA2, not a verified direct Sema5A-PlexA3 edge."
                limitations = "Retain the Sema5A-PlexA1/PlexA2 specificity and neuronal context; do not transfer it to PLXNA3 or infer a complete downstream route from semaphorin-family membership."
            elif ligand == "SEMA5B" and receptor == "PLXNA3":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
                primary = ["PMID:21835343"]
                species = "mouse"
                summary = "Primary retinal-development experiments support a Sema5B-PlexinA3 functional route: Sema5A/Sema5B constrain neurite outgrowth through PlexinA1/PlexinA3 in vitro and in vivo, with retinal lamination and response outputs."
                limitations = "Promote only as a bounded transmembrane-semaphorin functional route; the study establishes receptor-dependent neurite effects rather than purified binary binding, intracellular relay or a terminal-TF output."
            elif ligand == "JAG2" and receptor == "NOTCH4":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = ["PMID:23530123", "PMID:21372153"]
                species = "human"
                summary = "Primary Jagged2 studies support Notch1/Notch3 activation and lineage outputs, but do not verify the exact Jagged2-Notch4 pair represented by this public candidate."
                limitations = "Retain Jagged2-Notch1/Notch3 specificity and contact-dependent Notch context; do not transfer those results to NOTCH4 or infer a complete downstream route without pair-specific evidence."
            elif ligand == "CD200" and receptor == "CD200R3":
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = ["PMID:12960329", "PMID:17982101", "PMID:26315370"]
                species = "mouse"
                summary = "Primary CD200-receptor-family work distinguishes the canonical CD200-CD200R interaction from CD200R-related activating receptors, while CD200Fc studies report CD200R3 expression and microglial outputs without establishing direct CD200 binding to CD200R3."
                limitations = "Retain CD200-CD200R1 as the canonical ligand-receptor edge; keep CD200R3 as a receptor-family and functional-context hold until an exact CD200-CD200R3 binding or receptor-dependent ligand assay is identified."
            elif ligand == "GHRH" and receptor in {"VIPR1", "VIPR2"}:
                disposition = "hold_contextual_or_complex_boundary"
                layer = "ligand_receptor_binding_or_activation"
                primary = ["PMID:10655511"]
                species = "rat"
                summary = "Primary peptide-antagonist and receptor-binding studies distinguish GHRH-receptor activity from VPAC1/VPAC2 activity; the tested GHRH-related analogs do not establish intact GHRH as a canonical VIPR1 or VIPR2 ligand."
                limitations = "Retain GHRH-GHRHR and VIP/PACAP-VIPR specificity; do not materialize GHRH-to-VIPR1/2 from structural similarity or analog cross-antagonism alone."
            elif ligand == "VIP" and receptor == "SCTR":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
                primary = ["PMID:7782300"]
                species = "human"
                summary = "Primary chimeric-receptor pharmacology detects weak VIP responsiveness at the secretin receptor, with much lower potency than the cognate VIP-receptor response, supporting a bounded cross-family functional route."
                limitations = "Treat as low-potency cross-reactivity rather than canonical VIP-SCTR signaling; the study does not establish physiological relevance, a complete intracellular relay or a terminal-TF output."
            elif ligand == "RAET1A" and receptor == "KLRK1":
                disposition = "new_primary_supported_edge_candidate"
                layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
                primary = ["PMID:19197141", "PMID:20484740"]
                species = "mouse"
                summary = "Primary mouse studies support a RAET1A-KLRK1/NKG2D functional route: inducible Raet1a expression activates NKG2D-dependent cytotoxic pathology, and RAET1-expressing trophoblast systems elicit KLRK1-dependent IFNG responses."
                limitations = "Promote as a bounded NKG2D ligand-to-immune-output route; the cited studies do not resolve DAP10/DAP12 adaptor choice, a complete intracellular cascade or a terminal-TF output."
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
        elif ligand == "JAG1" and receptor == "NOTCH4":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:36044575", "PMCID:PMC9432841", "DOI:10.1126/sciadv.abo7958"]
            species = "human; mouse; pig"
            summary = "Primary endothelial, mouse-artery and human coronary-cell experiments support a JAG1-NOTCH4 mechanosensing route: disturbed flow increases NOTCH4 activation, JAG1 blockade reduces N4ICD, and endothelial Jag1 deletion changes atherosclerotic and endothelial-state outputs."
            limitations = "Retain the contact-dependent Notch and disturbed-flow context; the study supports receptor-dependent pathway function rather than purified JAG1-NOTCH4 binding, and it does not assert a universal terminal-TF or SCI route."
        elif ligand == "JAG2" and receptor == "NOTCH4":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:23530123", "PMID:21372153"]
            species = "human"
            summary = "Primary Jagged2 studies support Notch1/Notch3 activation and lineage outputs, but do not verify the exact Jagged2-Notch4 pair represented by this public candidate."
            limitations = "Retain Jagged2-Notch1/Notch3 specificity and contact-dependent Notch context; do not transfer those results to NOTCH4 or infer a complete downstream route without pair-specific evidence."
        elif ligand == "SEMA5B" and receptor == "PLXNA3":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:21835343"]
            species = "mouse"
            summary = "Primary retinal-development experiments support a Sema5B-PlexinA3 functional route: Sema5A/Sema5B constrain neurite outgrowth through PlexinA1/PlexinA3 in vitro and in vivo, with retinal lamination and response outputs."
            limitations = "Promote only as a bounded transmembrane-semaphorin functional route; the study establishes receptor-dependent neurite effects rather than purified binary binding, intracellular relay or a terminal-TF output."
        elif ligand == "CD200" and receptor == "CD200R3":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:12960329", "PMID:17982101", "PMID:26315370"]
            species = "mouse"
            summary = "Primary CD200-receptor-family work distinguishes the canonical CD200-CD200R interaction from CD200R-related activating receptors, while CD200Fc studies report CD200R3 expression and microglial outputs without establishing direct CD200 binding to CD200R3."
            limitations = "Retain CD200-CD200R1 as the canonical ligand-receptor edge; keep CD200R3 as a receptor-family and functional-context hold until an exact CD200-CD200R3 binding or receptor-dependent ligand assay is identified."
        elif ligand == "GHRH" and receptor in {"VIPR1", "VIPR2"}:
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = ["PMID:10655511"]
            species = "rat"
            summary = "Primary peptide-antagonist and receptor-binding studies distinguish GHRH-receptor activity from VPAC1/VPAC2 activity; the tested GHRH-related analogs do not establish intact GHRH as a canonical VIPR1 or VIPR2 ligand."
            limitations = "Retain GHRH-GHRHR and VIP/PACAP-VIPR specificity; do not materialize GHRH-to-VIPR1/2 from structural similarity or analog cross-antagonism alone."
        elif ligand == "VIP" and receptor == "SCTR":
            disposition = "new_primary_supported_edge_candidate"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway"
            primary = ["PMID:7782300"]
            species = "human"
            summary = "Primary chimeric-receptor pharmacology detects weak VIP responsiveness at the secretin receptor, with much lower potency than the cognate VIP-receptor response, supporting a bounded cross-family functional route."
            limitations = "Treat as low-potency cross-reactivity rather than canonical VIP-SCTR signaling; the study does not establish physiological relevance, a complete intracellular relay or a terminal-TF output."
        elif ligand in {"JAG1", "JAG2"} and receptor == "NOTCH4":
            disposition = "no_primary_evidence_found"
            layer = "candidate_only_review_locator"
            primary = ["PMID:22353464"]
            summary = "The public citation was recorded, but the reviewed primary evidence did not verify an exact Jagged1/2-Notch4 relationship for this row."
            limitations = "Keep as a searchable Notch-family candidate; do not infer Notch4 binding or activation from Notch1/Notch3 evidence."
        elif ligand == "SEMA5A" and receptor == "PLXNA3":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;receptor_proximal_or_pathway;downstream_or_functional"
            primary = ["PMID:25313870", "DOI:10.7554/eLife.04390"]
            species = "mouse"
            summary = "Primary Sema5A binding and neuronal-function experiments tested PlexA paralogs and found selective binding/function through PlexA1 and PlexA2, not a verified direct Sema5A-PlexA3 edge."
            limitations = "Retain the Sema5A-PlexA1/PlexA2 specificity and neuronal context; do not transfer it to PLXNA3 or infer a complete downstream route from semaphorin-family membership."
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
        elif ligand == "CCL5" and receptor == "ACKR2":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation;downstream_or_functional"
            primary = ["PMID:17095748", "PMID:29469612"]
            species = "mouse"
            summary = "Primary ACKR2/D6 studies support a chemokine-scavenging and inflammatory-context relationship for CCL5, but also show concentration- and tissue-dependent effects; this is contextual scavenging evidence, not a canonical G-protein signaling edge."
            limitations = "Preserve ACKR2 as an atypical scavenger receptor and retain the mouse lung/fibrosis context; do not infer conventional chemotaxis, intracellular relay or terminal-TF output from CCL5 abundance changes alone."
        elif ligand == "CCL24" and receptor == "ACKR2":
            disposition = "hold_contextual_or_complex_boundary"
            layer = "ligand_receptor_binding_or_activation"
            primary = ["PMID:17095748", "PMCID:PMC1899265"]
            species = "mouse"
            summary = "Primary D6/ACKR2 work establishes concentration-dependent chemokine scavenging and receptor-family context, but the cited experiments do not verify a direct CCL24-ACKR2 interaction; the candidate remains a bounded search hold."
            limitations = "Require an exact CCL24-D6 binding or internalization assay before promotion; do not transfer CCL17/CCL22 or other CC-chemokine evidence to CCL24 without isoform-specific support."
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
                "review_status": f"reviewed_{row.get('review_batch', 'batch_001')}",
            }
        )

    if len(output) != len(batch) or {r["candidate_unit_id"] for r in output} != {r["candidate_unit_id"] for r in batch}:
        raise SystemExit("resolution does not cover batch exactly")
    write_tsv(args.output, output, fields)
    from collections import Counter

    print(f"resolved_rows={len(output)} dispositions={dict(sorted(Counter(r['disposition'] for r in output).items()))}")


if __name__ == "__main__":
    main()
