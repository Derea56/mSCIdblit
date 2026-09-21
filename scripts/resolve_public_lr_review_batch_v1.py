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
