#!/usr/bin/env python3
"""Build a provenance-preserving public TF/regulon union.

The importer is intentionally file-based and deterministic.  It does not
connect to PostgreSQL or mutate the frozen mechanism graph.  It writes
tab-separated load files plus a psql script that creates and loads only the
``external_tf_*`` tables defined in ``schema/public_tf_union_integration.sql``.

The two imported TF resources are kept source- and species-specific:
TRRUST and OmniPath/DoRothEA.  Symbol normalization is conservative: simple
symbols receive a case-folded comparison key, while composite labels,
accession-like identifiers, and empty values remain unresolved.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable, Mapping


PRIORITY_TFS = (
    "TP53", "JUN", "FOS", "MYC", "STAT1", "HIF1A", "SP1", "ETS1",
    "RUNX1", "GATA3", "CEBPB", "IRF1", "ATF2", "EGR1", "KLF4", "NFKB2",
)

SOURCE_CONFIG = {
    "trrust": {
        "registry": "TRRUST",
        "version": "TRRUST_v2_snapshot_2026-08-25",
        "resource_class": "tf_regulon",
        "urls": {
            "human": "https://www.grnpedia.org/trrust/data/trrust_rawdata.human.tsv",
            "mouse": "https://www.grnpedia.org/trrust/data/trrust_rawdata.mouse.tsv",
        },
        "upstream_version": "TRRUST_v2 (snapshot version label)",
    },
    "dorothea": {
        "registry": "OmniPath_DoRothEA",
        "version": "OmniPath_DoRothEA_snapshot_2026-08-25",
        "resource_class": "tf_regulon",
        "urls": {
            "human": "https://omnipathdb.org/interactions?genesymbols=yes&datasets=dorothea&organisms=9606&fields=sources,references,curation_effort,dorothea_level",
            "mouse": "https://omnipathdb.org/interactions?genesymbols=yes&datasets=dorothea&organisms=10090&fields=sources,references,curation_effort,dorothea_level",
        },
        "upstream_version": "OmniPath/DoRothEA snapshot version not exposed by endpoint",
    },
}

# These are bounded literature checks, not claims that every public row is
# primary evidence.  The selected PMID must occur in the corresponding public
# record before a record-level verification status is promoted.
VERIFICATION_GUIDES = {
    "TP53": {
        "pmid": "19411072",
        "title": "Ablation of key oncogenic pathways by RITA-reactivated p53 is required for efficient apoptosis.",
        "human_status": "primary_reference_verified",
        "mouse_status": "context_limited_reference",
        "evidence_class": "perturbation_response",
        "verified_effect": "context_dependent",
        "cell_type": "human cancer cell lines; mouse xenograft context",
        "compartment": "nucleus",
        "stimulus": "RITA-mediated p53 reactivation",
        "confidence": "medium",
        "limitations": "The paper supports p53-dependent transcriptional and post-transcriptional responses in cancer models; it does not establish every public TF-target row or a spinal-cord-injury context.",
        "notes": "The paper reports repression of MCL1, BCL2, MAP4, survivin, c-MYC and beta-catenin after p53 reactivation. Treat individual public rows as context-limited unless the exact target and assay are reviewed.",
    },
    "JUN": {
        "pmid": "9334186",
        "title": "The Ets transcription factors interact with each other and with the c-Fos/c-Jun complex via distinct protein domains in a DNA-dependent and -independent manner.",
        "human_status": "primary_reference_verified",
        "mouse_status": "context_limited_reference",
        "evidence_class": "direct_binding",
        "verified_effect": "context_dependent",
        "cell_type": "human promoter/in-vitro interaction systems",
        "compartment": "nucleus",
        "stimulus": "promoter DNA and AP-1/Ets interaction assay",
        "confidence": "medium",
        "limitations": "The paper supports c-Jun/c-Fos/Ets promoter interactions and context-dependent transcriptional effects, not a universal direction for every JUN target.",
        "notes": "The primary paper describes DNA-dependent and DNA-independent interactions and promoter regulation involving c-Jun/c-Fos complexes.",
    },
    "FOS": {
        "pmid": "9334186",
        "title": "The Ets transcription factors interact with each other and with the c-Fos/c-Jun complex via distinct protein domains in a DNA-dependent and -independent manner.",
        "human_status": "primary_reference_verified",
        "mouse_status": "context_limited_reference",
        "evidence_class": "direct_binding",
        "verified_effect": "context_dependent",
        "cell_type": "human promoter/in-vitro interaction systems",
        "compartment": "nucleus",
        "stimulus": "promoter DNA and AP-1/Ets interaction assay",
        "confidence": "medium",
        "limitations": "The primary evidence is a promoter/interacting-complex study and should not be generalized to all public FOS memberships.",
        "notes": "FOS is a real DNA-binding AP-1 component; direction depends on complex composition and promoter context.",
    },
    "MYC": {
        "pmid": "8206526",
        "title": "Transcriptional suppression of HLA-B expression by c-Myc is mediated through the core promoter elements.",
        "human_status": "primary_reference_verified",
        "mouse_status": "context_limited_reference",
        "evidence_class": "direct_binding",
        "verified_effect": "repressing_target",
        "cell_type": "human melanoma cell line and c-MYC transfectants",
        "compartment": "nucleus",
        "stimulus": "c-MYC overexpression",
        "confidence": "medium",
        "limitations": "The selected paper is a human HLA-B promoter study; it does not validate all MYC rows or mouse ortholog effects.",
        "notes": "The paper reports c-MYC-dependent suppression of HLA-B transcription through core promoter elements. This is a useful direction-conflict check against TRRUST rows that label HLA targets as activating.",
    },
    "STAT1": {
        "pmid": "16628196",
        "title": "SOCS1-negative feedback of STAT1 activation is a key pathway in the dsRNA-induced innate immune response of human keratinocytes.",
        "human_status": "primary_reference_verified",
        "mouse_status": "context_limited_reference",
        "evidence_class": "perturbation_response",
        "verified_effect": "activating_target",
        "cell_type": "human keratinocytes",
        "compartment": "nucleus",
        "stimulus": "poly(I:C)/TLR3-induced innate immune response",
        "confidence": "medium",
        "limitations": "Dominant-negative STAT1 and SOCS1 perturbations support pathway-dependent target induction; they do not prove direct STAT1 binding for every public target.",
        "notes": "The paper supports STAT1 mediation of poly(I:C)-induced CCL3/MIP-1alpha and regulation of IRF7/TLR3 responses.",
    },
    "HIF1A": {
        "pmid": "8955077",
        "title": "Hypoxia response elements in the aldolase A, enolase 1, and lactate dehydrogenase A gene promoters contain essential binding sites for hypoxia-inducible factor 1.",
        "human_status": "primary_reference_verified",
        "mouse_status": "context_limited_reference",
        "evidence_class": "direct_binding",
        "verified_effect": "activating_target",
        "cell_type": "mammalian cultured cells and promoter constructs",
        "compartment": "nucleus",
        "stimulus": "hypoxia",
        "confidence": "high",
        "limitations": "The paper establishes HIF-1 binding sites and hypoxia-responsive promoter activity for selected glycolytic genes; it is not a global HIF1A regulon validation.",
        "notes": "Primary promoter and mutagenesis evidence supports HIF-1-dependent activation of ALDOA, ENO1 and LDHA-associated hypoxia response elements.",
    },
    "SP1": {
        "pmid": "9574539",
        "title": "Regulation of transcription of the TATA-less human complement component C4 gene.",
        "human_status": "primary_reference_verified",
        "mouse_status": "context_limited_reference",
        "evidence_class": "direct_binding",
        "verified_effect": "activating_target",
        "cell_type": "human HepG2 and HeLa promoter assays",
        "compartment": "nucleus",
        "stimulus": "basal promoter transcription",
        "confidence": "high",
        "limitations": "The selected promoter assay is human and gene-specific; it does not establish a universal SP1 activation rule.",
        "notes": "EMSA, DNase footprinting and promoter mutagenesis support a critical SP1-binding site in the C4 promoter.",
    },
    "ETS1": {
        "pmid": "18381358",
        "title": "Regulation of hypoxia-inducible genes by ETS1 transcription factor.",
        "human_status": "primary_reference_verified",
        "mouse_status": "primary_reference_verified",
        "evidence_class": "perturbation_response",
        "verified_effect": "context_dependent",
        "cell_type": "human lung epithelial cells and mouse fibroblasts",
        "compartment": "nucleus",
        "stimulus": "high cell density and hypoxia-related gene induction",
        "confidence": "medium",
        "limitations": "The study supports ETS1 involvement in selected CA9/NDRG1 responses and shows cooperation with HIF-1; it does not make ETS1 a universal hypoxia regulator.",
        "notes": "Reporter assays and ETS1 siRNA support context-dependent regulation of hypoxia-inducible genes in both species.",
    },
    "RUNX1": {
        "pmid": "12771199",
        "title": "Transcriptional regulation of the human MIP-1alpha promoter by RUNX1 and MOZ.",
        "human_status": "primary_reference_verified",
        "mouse_status": "context_limited_reference",
        "evidence_class": "direct_binding",
        "verified_effect": "activating_target",
        "cell_type": "human Jurkat T cells",
        "compartment": "nucleus",
        "stimulus": "PMA/PHA promoter activation",
        "confidence": "high",
        "limitations": "RUNX1 binding and promoter activation are shown for MIP-1alpha/CCL3 in human Jurkat cells; the result is not a broad RUNX1 regulon claim.",
        "notes": "In-vitro binding, ChIP and promoter-site mutation support RUNX1-dependent CCL3 promoter activation.",
    },
    "GATA3": {
        "pmid": "22120723",
        "title": "BRCA1 and GATA3 corepress FOXC1 to inhibit the pathogenesis of basal-like breast cancers.",
        "human_status": "primary_reference_verified",
        "mouse_status": "context_limited_reference",
        "evidence_class": "direct_binding",
        "verified_effect": "repressing_target",
        "cell_type": "human basal-like breast cancer cell lines",
        "compartment": "nucleus",
        "stimulus": "BRCA1/GATA3 co-repressor context",
        "confidence": "high",
        "limitations": "The study is a human breast-cancer context and does not validate all GATA3 target rows or spinal-cord-injury cell types.",
        "notes": "The paper identifies a GATA3-binding site at the FOXC1 promoter and supports GATA3/BRCA1-mediated repression.",
    },
    "CEBPB": {
        "pmid": "10453008",
        "title": "A composite C/EBP binding site is essential for the activity of the promoter of the IL-3/IL-5/granulocyte-macrophage colony-stimulating factor receptor beta c gene.",
        "human_status": "primary_reference_verified",
        "mouse_status": "context_limited_reference",
        "evidence_class": "direct_binding",
        "verified_effect": "activating_target",
        "cell_type": "human U937 and HL-60 myeloid cells",
        "compartment": "nucleus",
        "stimulus": "myeloid differentiation/promoter activation",
        "confidence": "medium",
        "limitations": "The paper shows C/EBPbeta binding and enhancer dependence for CSF2RB/cytokine receptor beta regulation; it does not resolve every CEBPB target or context.",
        "notes": "C/EBPalpha and C/EBPbeta binding plus enhancer deletion/mutation support activation of the CSF2RB-associated promoter.",
    },
    "IRF1": {
        "pmid": None,
        "title": None,
        "human_status": "database_curated_unverified",
        "mouse_status": "database_curated_unverified",
        "evidence_class": "unresolved",
        "verified_effect": "unknown",
        "cell_type": "not established in this bounded review",
        "compartment": "not established in this bounded review",
        "stimulus": "not established in this bounded review",
        "confidence": "uncertain",
        "limitations": "The public snapshots contain IRF1 records and PMID leads, but no primary record was independently resolved in this bounded pass.",
        "notes": "Retain as database_curated/unverified_public_record; do not promote to primary evidence.",
    },
    "ATF2": {
        "pmid": None,
        "title": None,
        "human_status": "database_curated_unverified",
        "mouse_status": "database_curated_unverified",
        "evidence_class": "unresolved",
        "verified_effect": "unknown",
        "cell_type": "not established in this bounded review",
        "compartment": "not established in this bounded review",
        "stimulus": "not established in this bounded review",
        "confidence": "uncertain",
        "limitations": "The public snapshots contain ATF2 records and PMID leads, but no primary record was independently resolved in this bounded pass.",
        "notes": "Retain as database_curated/unverified_public_record; do not promote to primary evidence.",
    },
    "EGR1": {
        "pmid": None,
        "title": None,
        "human_status": "database_curated_unverified",
        "mouse_status": "database_curated_unverified",
        "evidence_class": "unresolved",
        "verified_effect": "unknown",
        "cell_type": "not established in this bounded review",
        "compartment": "not established in this bounded review",
        "stimulus": "not established in this bounded review",
        "confidence": "uncertain",
        "limitations": "The public snapshots contain EGR1 records and many PMID leads, but the bounded review did not resolve a target-specific primary record.",
        "notes": "Retain as database_curated/unverified_public_record; do not promote to primary evidence.",
    },
    "KLF4": {
        "pmid": None,
        "title": None,
        "human_status": "database_curated_unverified",
        "mouse_status": "database_curated_unverified",
        "evidence_class": "unresolved",
        "verified_effect": "unknown",
        "cell_type": "not established in this bounded review",
        "compartment": "not established in this bounded review",
        "stimulus": "not established in this bounded review",
        "confidence": "uncertain",
        "limitations": "The public snapshots contain KLF4 records and PMID leads, but the bounded review did not resolve a target-specific primary record.",
        "notes": "Retain as database_curated/unverified_public_record; do not promote to primary evidence.",
    },
    "NFKB2": {
        "pmid": "18504428",
        "title": "Activation of the cyclin D2 and cdk6 genes through NF-kappaB is critical for cell-cycle progression induced by HTLV-I Tax.",
        "human_status": "primary_reference_verified",
        "mouse_status": "context_limited_reference",
        "evidence_class": "perturbation_response",
        "verified_effect": "activating_target",
        "cell_type": "human T cells with HTLV-I Tax; rat comparator context",
        "compartment": "nucleus",
        "stimulus": "HTLV-I Tax-induced NF-kappaB activation",
        "confidence": "medium",
        "limitations": "The study supports p100/NFKB2-dependent activation of CCND2/CDK6 in a viral-T-cell context; it does not establish a general NFKB2 regulon.",
        "notes": "shRNA and promoter assays support NF-kappaB-dependent CCND2/CDK6 induction; preserve the exact NF-kappaB subunit context as a limitation.",
    },
}


@dataclass(frozen=True)
class InputSpec:
    source_kind: str
    species: str
    path: Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def normalize_symbol(value: str | None) -> tuple[str | None, str | None, str, str]:
    """Return display symbol, casefold key, decision, and reason."""

    source = (value or "").strip()
    if not source:
        return None, None, "empty_unresolved", "Source record has no symbol value."
    # Accession-like values occur in a genesymbol column in some OmniPath
    # mouse rows.  They are retained as raw values but are not gene identities.
    if re.fullmatch(r"[OPQ][0-9][A-Z0-9]{4,7}", source):
        return None, None, "non_symbol_identifier_unresolved", (
            "Value matches an accession-like identifier rather than a conservative gene-symbol pattern."
        )
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", source):
        return None, None, "composite_unresolved", (
            "Composite or non-simple label retained without heuristic splitting."
        )
    return source, source.casefold(), "normalized_exact", "Trimmed simple source symbol; no alias expansion applied."


def effect_from_trrust(raw: str) -> str:
    value = raw.strip().casefold()
    if value == "activation":
        return "activating_target"
    if value == "repression":
        return "repressing_target"
    return "unknown"


def effect_from_dorothea(row: Mapping[str, str]) -> str:
    stimulating = row.get("consensus_stimulation", "").strip().casefold() == "true"
    inhibiting = row.get("consensus_inhibition", "").strip().casefold() == "true"
    if stimulating and inhibiting:
        return "context_dependent"
    if stimulating:
        return "activating_target"
    if inhibiting:
        return "repressing_target"
    return "unknown"


def pmids_from_text(value: str) -> list[str]:
    return sorted(set(re.findall(r"(?<![0-9])[0-9]{5,9}(?![0-9])", value or "")))


def reference_rows(reference_text: str, record_key: str, source_url: str) -> list[dict[str, str]]:
    rows: dict[tuple[str, str], dict[str, str]] = {}
    for token in (part.strip() for part in (reference_text or "").split(";")):
        if not token:
            continue
        pmid_match = re.search(r"(?<![0-9])([0-9]{5,9})(?![0-9])", token)
        if pmid_match:
            ref_id = pmid_match.group(1)
            key = ("PMID", ref_id)
            rows[key] = {
                "external_record_key": record_key,
                "reference_namespace": "PMID",
                "reference_id": ref_id,
                "reference_locator": f"https://pubmed.ncbi.nlm.nih.gov/{ref_id}/",
                "reference_status": "database_reference_lead",
            }
        else:
            key = ("source_reference", token)
            rows[key] = {
                "external_record_key": record_key,
                "reference_namespace": "source_reference",
                "reference_id": token,
                "reference_locator": source_url,
                "reference_status": "database_reference_lead",
            }
    return list(rows.values())


def write_tsv(path: Path, columns: list[str], rows: Iterable[Mapping[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(columns)
        for row in rows:
            values = []
            for column in columns:
                value = row.get(column, "")
                if value is None:
                    values.append("\\N")
                elif isinstance(value, (dict, list)):
                    values.append(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
                else:
                    values.append(str(value))
            writer.writerow(values)


def parse_inputs(inputs: list[InputSpec], retrieval_date: str) -> tuple[list[dict], list[dict], list[dict], dict]:
    registry_rows: list[dict] = []
    records: list[dict] = []
    references: list[dict] = []
    mapping_values: dict[tuple[str, str, str, str], dict] = {}
    snapshot_manifest: dict = {}

    for spec in inputs:
        config = SOURCE_CONFIG[spec.source_kind]
        registry = config["registry"]
        version = config["version"]
        source_url = config["urls"][spec.species]
        input_sha = sha256_file(spec.path)
        registry_rows.append({
            "source_registry": registry,
            "source_version": version,
            "species_context": spec.species,
            "retrieval_date": retrieval_date,
            "source_url": source_url,
            "snapshot_path": str(spec.path),
            "snapshot_sha256": input_sha,
            "resource_class": config["resource_class"],
            "upstream_version": config["upstream_version"],
            "notes": "Raw snapshot is retained outside the frozen mechanism bundle; this row records its path and digest.",
        })
        snapshot_manifest[f"{registry}:{spec.species}"] = {
            "path": str(spec.path),
            "sha256": input_sha,
            "line_count": sum(1 for _ in spec.path.open(encoding="utf-8")),
            "source_url": source_url,
            "source_version": version,
            "retrieval_date": retrieval_date,
        }

        if spec.source_kind == "trrust":
            with spec.path.open(encoding="utf-8", newline="") as handle:
                reader = csv.reader(handle, delimiter="\t")
                for line_number, row in enumerate(reader, start=1):
                    if len(row) < 4:
                        continue
                    raw_payload = {"tf": row[0], "target": row[1], "effect": row[2], "pmid": row[3]}
                    tf_display, tf_key, tf_decision, tf_reason = normalize_symbol(row[0])
                    target_display, target_key, target_decision, target_reason = normalize_symbol(row[1])
                    raw_id = f"line:{line_number}"
                    record_id = f"trrust:{spec.species}:{line_number:06d}"
                    record_key = f"{registry}|{version}|{spec.species}|{record_id}"
                    row_hash = sha256_text("\t".join(row))
                    pmids = pmids_from_text(row[3])
                    status = "unverified_public_record"
                    guide = VERIFICATION_GUIDES.get((tf_display or row[0]).upper())
                    if guide and guide.get("pmid") in pmids:
                        status = guide[f"{spec.species}_status"]
                    limitations = (
                        "TRRUST is literature-curated, but the row is retained as a public database assertion; "
                        "database presence is not promoted to direct-binding or perturbation evidence."
                    )
                    if tf_decision != "normalized_exact" or target_decision != "normalized_exact":
                        limitations += f" Identity review: TF={tf_reason} Target={target_reason}"
                    record = {
                        "external_record_key": record_key,
                        "source_registry": registry,
                        "source_version": version,
                        "species_context": spec.species,
                        "external_record_id": record_id,
                        "raw_record_id": raw_id,
                        "raw_record_sha256": row_hash,
                        "raw_payload": raw_payload,
                        "source_tf_symbol": row[0].strip(),
                        "source_target_symbol": row[1].strip(),
                        "tf_normalized_symbol": tf_display,
                        "tf_normalized_symbol_key": tf_key,
                        "target_normalized_symbol": target_display,
                        "target_normalized_symbol_key": target_key,
                        "raw_relationship_effect": row[2].strip(),
                        "effect_polarity": effect_from_trrust(row[2]),
                        "relationship_class": "unresolved",
                        "evidence_basis": "database_curated",
                        "confidence_tier": "uncertain",
                        "dorothea_level": None,
                        "curation_effort": None,
                        "external_sources": "TRRUST",
                        "reference_text": row[3].strip(),
                        "reference_pmids": ";".join(pmids),
                        "source_locator": f"{source_url}#row={line_number}",
                        "verification_status": status,
                        "limitations": limitations,
                        "export_priority": "exclude",
                    }
                    records.append(record)
                    references.extend(reference_rows(row[3], record_key, source_url))
                    add_mapping(mapping_values, registry, version, spec.species, "tf", row[0], tf_display, tf_key, tf_decision, tf_reason)
                    add_mapping(mapping_values, registry, version, spec.species, "target", row[1], target_display, target_key, target_decision, target_reason)
        else:
            with spec.path.open(encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle, delimiter="\t")
                for line_number, row in enumerate(reader, start=2):
                    tf_source = (row.get("source_genesymbol") or "").strip()
                    target_source = (row.get("target_genesymbol") or "").strip()
                    tf_display, tf_key, tf_decision, tf_reason = normalize_symbol(tf_source)
                    target_display, target_key, target_decision, target_reason = normalize_symbol(target_source)
                    raw_payload = {key: row.get(key, "") for key in reader.fieldnames or []}
                    row_text = "\t".join(row.get(key, "") for key in reader.fieldnames or [])
                    row_hash = sha256_text(row_text)
                    record_id = f"omnipath_dorothea:{spec.species}:{line_number:06d}:{row_hash[:12]}"
                    record_key = f"{registry}|{version}|{spec.species}|{record_id}"
                    reference_text = (row.get("references") or "").strip()
                    pmids = pmids_from_text(reference_text)
                    status = "unverified_public_record"
                    guide = VERIFICATION_GUIDES.get((tf_display or tf_source).upper())
                    if guide and guide.get("pmid") in pmids:
                        status = guide[f"{spec.species}_status"]
                    limitations = (
                        "OmniPath/DoRothEA is a consensus/curated resource; source fields and DoRothEA level are "
                        "evidence leads, not automatic proof of direct binding or TF activation."
                    )
                    if tf_decision != "normalized_exact" or target_decision != "normalized_exact":
                        limitations += f" Identity review: TF={tf_reason} Target={target_reason}"
                    record = {
                        "external_record_key": record_key,
                        "source_registry": registry,
                        "source_version": version,
                        "species_context": spec.species,
                        "external_record_id": record_id,
                        "raw_record_id": f"line:{line_number}",
                        "raw_record_sha256": row_hash,
                        "raw_payload": raw_payload,
                        "source_tf_symbol": tf_source,
                        "source_target_symbol": target_source,
                        "tf_normalized_symbol": tf_display,
                        "tf_normalized_symbol_key": tf_key,
                        "target_normalized_symbol": target_display,
                        "target_normalized_symbol_key": target_key,
                        "raw_relationship_effect": (
                            "consensus_stimulation" if row.get("consensus_stimulation") == "True" and row.get("consensus_inhibition") != "True"
                            else "consensus_inhibition" if row.get("consensus_inhibition") == "True" and row.get("consensus_stimulation") != "True"
                            else "consensus_stimulation_and_inhibition" if row.get("consensus_stimulation") == "True" and row.get("consensus_inhibition") == "True"
                            else "consensus_unknown"
                        ),
                        "effect_polarity": effect_from_dorothea(row),
                        "relationship_class": "inferred_regulatory",
                        "evidence_basis": "database_curated",
                        "confidence_tier": "uncertain",
                        "dorothea_level": (row.get("dorothea_level") or "").strip() or None,
                        "curation_effort": int(row["curation_effort"]) if (row.get("curation_effort") or "").isdigit() else None,
                        "external_sources": (row.get("sources") or "").strip(),
                        "reference_text": reference_text,
                        "reference_pmids": ";".join(pmids),
                        "source_locator": f"{source_url}#row={line_number}",
                        "verification_status": status,
                        "limitations": limitations,
                        "export_priority": "exclude",
                    }
                    records.append(record)
                    references.extend(reference_rows(reference_text, record_key, source_url))
                    add_mapping(mapping_values, registry, version, spec.species, "tf", tf_source, tf_display, tf_key, tf_decision, tf_reason)
                    add_mapping(mapping_values, registry, version, spec.species, "target", target_source, target_display, target_key, target_decision, target_reason)

    # Reference status is promoted only for the bounded guide PMID and only for
    # records whose public row actually contains that PMID.
    guide_status: dict[tuple[str, str], str] = {}
    for record in records:
        guide = VERIFICATION_GUIDES.get((record["tf_normalized_symbol"] or record["source_tf_symbol"]).upper())
        if not guide or not guide.get("pmid"):
            continue
        if guide["pmid"] not in (record["reference_pmids"] or "").split(";"):
            continue
        guide_status[(record["external_record_key"], guide["pmid"])] = guide[f"{record['species_context']}_status"]
    for ref in references:
        ref_status = guide_status.get((ref["external_record_key"], ref["reference_id"]))
        if ref_status:
            ref["reference_status"] = (
                "primary_reference_verified" if ref_status == "primary_reference_verified"
                else "context_limited_reference"
            )

    mappings = list(mapping_values.values())
    return registry_rows, records, references, {"mappings": mappings, "snapshots": snapshot_manifest}


def add_mapping(store: dict, registry: str, version: str, species: str, role: str, source_symbol: str,
                normalized_symbol: str | None, normalized_key: str | None, decision: str, reason: str) -> None:
    key = (registry, version, species, role, source_symbol.strip())
    store[key] = {
        "source_registry": registry,
        "source_version": version,
        "species_context": species,
        "identity_role": role,
        "source_symbol": source_symbol.strip(),
        "normalized_symbol": normalized_symbol,
        "normalized_symbol_key": normalized_key,
        "identity_decision": decision,
        "identity_reason": reason,
        "mscidblit_entity_id": None,
        "frozen_entity_match_status": "not_evaluated",
    }


def materialize_regulons(records: list[dict]) -> tuple[list[dict], list[dict]]:
    groups: dict[tuple[str, str, str, str], list[dict]] = defaultdict(list)
    for record in records:
        if not record["tf_normalized_symbol_key"]:
            continue
        groups[(
            record["source_registry"], record["source_version"],
            record["species_context"], record["tf_normalized_symbol_key"],
        )].append(record)

    regulons: list[dict] = []
    members: list[dict] = []
    for key, group in sorted(groups.items()):
        registry, version, species, tf_key = key
        tf_display = sorted({row["tf_normalized_symbol"] for row in group if row["tf_normalized_symbol"]})[0]
        regulon_id = f"{registry}|{version}|{species}|{tf_key}"
        materialized = [row for row in group if row["target_normalized_symbol_key"]]
        regulons.append({
            "external_regulon_id": regulon_id,
            "source_registry": registry,
            "source_version": version,
            "species_context": species,
            "tf_normalized_symbol": tf_display,
            "tf_normalized_symbol_key": tf_key,
            "regulon_name": f"{registry} public regulon: {tf_display} ({species})",
            "definition_status": "candidate",
            "membership_semantics": "public_source_membership",
            "source_record_count": len(group),
            "materialized_member_count": len(materialized),
            "export_priority": "exclude",
            "limitations": "Candidate source grouping only; not an exhaustive or context-specific biological regulon and not part of the frozen mechanism bundle.",
        })
        for record in materialized:
            members.append({
                "external_regulon_id": regulon_id,
                "external_record_key": record["external_record_key"],
                "target_normalized_symbol": record["target_normalized_symbol"],
                "target_normalized_symbol_key": record["target_normalized_symbol_key"],
                "membership_basis": record["relationship_class"],
                "regulatory_effect": record["effect_polarity"],
                "membership_status": "candidate",
                "confidence_tier": "uncertain",
                "export_priority": "exclude",
            })
    return regulons, members


def build_verification_rows(records: list[dict]) -> list[dict]:
    by_tf_species: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for record in records:
        tf = (record["tf_normalized_symbol"] or record["source_tf_symbol"]).upper()
        if tf in VERIFICATION_GUIDES:
            by_tf_species[(tf, record["species_context"])].append(record)

    rows: list[dict] = []
    for tf in PRIORITY_TFS:
        guide = VERIFICATION_GUIDES[tf]
        for species in ("human", "mouse"):
            matching = by_tf_species.get((tf, species), [])
            selected = [
                record for record in matching
                if guide.get("pmid") and guide["pmid"] in (record["reference_pmids"] or "").split(";")
            ]
            status = guide[f"{species}_status"] if matching else "unresolved_reason_recorded"
            if guide.get("pmid") and not selected and matching:
                status = "database_curated_unverified"
            rows.append({
                "verification_id": f"TF_IDENTITY:{tf}:{species}",
                "external_record_key": None,
                "priority_tf_symbol": tf,
                "species_context": species,
                "target_normalized_symbol": None,
                "verification_scope": "tf_identity",
                "reference_pmid": guide.get("pmid"),
                "reference_locator": f"https://pubmed.ncbi.nlm.nih.gov/{guide['pmid']}/" if guide.get("pmid") else None,
                "reference_title": guide.get("title"),
                "verification_status": status,
                "evidence_class": guide["evidence_class"],
                "verified_effect": guide["verified_effect"],
                "cell_type_context": guide["cell_type"],
                "compartment_context": guide["compartment"],
                "stimulus_context": guide["stimulus"],
                "confidence_tier": guide["confidence"],
                "limitations": guide["limitations"],
                "notes": guide["notes"] if matching else guide["notes"] + " No matching imported source TF row was found for this species.",
            })
            # Materialize one target-level verification row for every public
            # row tied to the selected PMID.  All other rows remain explicitly
            # unverified in external_tf_regulon_record.
            for record in selected:
                rows.append({
                    "verification_id": f"RECORD:{record['external_record_key']}",
                    "external_record_key": record["external_record_key"],
                    "priority_tf_symbol": tf,
                    "species_context": species,
                    "target_normalized_symbol": record["target_normalized_symbol"],
                    "verification_scope": "tf_target_record",
                    "reference_pmid": guide.get("pmid"),
                    "reference_locator": f"https://pubmed.ncbi.nlm.nih.gov/{guide['pmid']}/",
                    "reference_title": guide.get("title"),
                    "verification_status": guide[f"{species}_status"],
                    "evidence_class": guide["evidence_class"],
                    "verified_effect": guide["verified_effect"],
                    "cell_type_context": guide["cell_type"],
                    "compartment_context": guide["compartment"],
                    "stimulus_context": guide["stimulus"],
                    "confidence_tier": guide["confidence"],
                    "limitations": guide["limitations"],
                    "notes": guide["notes"],
                })
    return rows


def make_load_sql(output_dir: Path) -> str:
    def q(path: Path) -> str:
        return "'" + str(path).replace("'", "''") + "'"

    tables = [
        "external_tf_evidence_verification",
        "external_tf_regulon_member",
        "external_tf_regulon",
        "external_tf_reference",
        "external_tf_regulon_record",
        "external_tf_identity_mapping",
        "external_tf_source_registry",
    ]
    lines = [
        "\\set ON_ERROR_STOP on",
        "\\i schema/public_tf_union_integration.sql",
        "BEGIN;",
        "TRUNCATE TABLE " + ", ".join(tables) + " RESTART IDENTITY CASCADE;",
    ]
    copy_specs = [
        (
            "external_tf_source_registry", "source_registry.tsv",
            "source_registry, source_version, species_context, retrieval_date, source_url, snapshot_path, snapshot_sha256, resource_class, upstream_version, notes",
        ),
        (
            "external_tf_identity_mapping", "identity_mapping.tsv",
            "source_registry, source_version, species_context, identity_role, source_symbol, normalized_symbol, normalized_symbol_key, identity_decision, identity_reason, mscidblit_entity_id, frozen_entity_match_status",
        ),
        (
            "external_tf_regulon_record", "source_records.tsv",
            "external_record_key, source_registry, source_version, species_context, external_record_id, raw_record_id, raw_record_sha256, raw_payload, source_tf_symbol, source_target_symbol, tf_normalized_symbol, tf_normalized_symbol_key, target_normalized_symbol, target_normalized_symbol_key, raw_relationship_effect, effect_polarity, relationship_class, evidence_basis, confidence_tier, dorothea_level, curation_effort, external_sources, reference_text, reference_pmids, source_locator, verification_status, limitations, export_priority",
        ),
        (
            "external_tf_reference", "source_references.tsv",
            "external_record_key, reference_namespace, reference_id, reference_locator, reference_status",
        ),
        (
            "external_tf_regulon", "source_regulons.tsv",
            "external_regulon_id, source_registry, source_version, species_context, tf_normalized_symbol, tf_normalized_symbol_key, regulon_name, definition_status, membership_semantics, source_record_count, materialized_member_count, export_priority, limitations",
        ),
        (
            "external_tf_regulon_member", "source_regulon_members.tsv",
            "external_regulon_id, external_record_key, target_normalized_symbol, target_normalized_symbol_key, membership_basis, regulatory_effect, membership_status, confidence_tier, export_priority",
        ),
        (
            "external_tf_evidence_verification", "priority_tf_evidence.tsv",
            "verification_id, external_record_key, priority_tf_symbol, species_context, target_normalized_symbol, verification_scope, reference_pmid, reference_locator, reference_title, verification_status, evidence_class, verified_effect, cell_type_context, compartment_context, stimulus_context, confidence_tier, limitations, notes",
        ),
    ]
    for table, filename, columns in copy_specs:
        lines.append(
            f"\\copy {table} ({columns}) FROM {q(output_dir / filename)} WITH (FORMAT csv, DELIMITER E'\\t', HEADER true, NULL '\\N')"
        )
    lines.extend([
        "",
        "-- Resolve only unique case-insensitive exact gene_symbol matches in the frozen graph.",
        "WITH candidates AS (",
        "  SELECT m.mapping_id, count(e.entity_id) AS match_count, min(e.entity_id) AS entity_id",
        "  FROM external_tf_identity_mapping m",
        "  LEFT JOIN signalingentity e",
        "    ON m.normalized_symbol_key IS NOT NULL",
        "   AND lower(btrim(coalesce(e.gene_symbol, ''))) = m.normalized_symbol_key",
        "  GROUP BY m.mapping_id",
        "), resolved AS (",
        "  SELECT mapping_id, match_count, entity_id FROM candidates",
        ")",
        "UPDATE external_tf_identity_mapping m",
        "SET mscidblit_entity_id = CASE WHEN r.match_count = 1 THEN r.entity_id ELSE NULL END,",
        "    frozen_entity_match_status = CASE",
        "      WHEN m.normalized_symbol_key IS NULL THEN 'absent_from_frozen_graph'",
        "      WHEN r.match_count = 1 THEN 'mapped_unique'",
        "      WHEN r.match_count > 1 THEN 'ambiguous_frozen_entity'",
        "      ELSE 'absent_from_frozen_graph' END",
        "FROM resolved r WHERE r.mapping_id = m.mapping_id;",
        "COMMIT;",
        "",
        "-- The external layer is export-gated and must remain separate from the frozen bundle.",
        "SELECT 'external_tf_union_loaded' AS check_name, count(*) AS record_count FROM external_tf_regulon_record;",
        "SELECT 'external_tf_union_exportable_rows' AS check_name, count(*) AS issue_count FROM external_tf_regulon_record WHERE export_priority <> 'exclude';",
    ])
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trrust-human", type=Path, required=True)
    parser.add_argument("--trrust-mouse", type=Path, required=True)
    parser.add_argument("--dorothea-human", type=Path, required=True)
    parser.add_argument("--dorothea-mouse", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--retrieval-date", default="2026-08-25")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    date.fromisoformat(args.retrieval_date)
    inputs = [
        InputSpec("trrust", "human", args.trrust_human),
        InputSpec("trrust", "mouse", args.trrust_mouse),
        InputSpec("dorothea", "human", args.dorothea_human),
        InputSpec("dorothea", "mouse", args.dorothea_mouse),
    ]
    for spec in inputs:
        if not spec.path.is_file():
            raise SystemExit(f"missing input snapshot: {spec.path}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    registry_rows, records, references, auxiliary = parse_inputs(inputs, args.retrieval_date)
    regulons, members = materialize_regulons(records)
    evidence = build_verification_rows(records)
    mappings = auxiliary["mappings"]

    write_tsv(args.output_dir / "source_registry.tsv", [
        "source_registry", "source_version", "species_context", "retrieval_date",
        "source_url", "snapshot_path", "snapshot_sha256", "resource_class",
        "upstream_version", "notes",
    ], sorted(registry_rows, key=lambda row: (row["source_registry"], row["species_context"])))
    write_tsv(args.output_dir / "identity_mapping.tsv", [
        "source_registry", "source_version", "species_context", "identity_role",
        "source_symbol", "normalized_symbol", "normalized_symbol_key",
        "identity_decision", "identity_reason", "mscidblit_entity_id",
        "frozen_entity_match_status",
    ], sorted(mappings, key=lambda row: (
        row["source_registry"], row["species_context"], row["identity_role"], row["source_symbol"]
    )))
    write_tsv(args.output_dir / "source_records.tsv", [
        "external_record_key", "source_registry", "source_version", "species_context",
        "external_record_id", "raw_record_id", "raw_record_sha256", "raw_payload",
        "source_tf_symbol", "source_target_symbol", "tf_normalized_symbol",
        "tf_normalized_symbol_key", "target_normalized_symbol", "target_normalized_symbol_key",
        "raw_relationship_effect", "effect_polarity", "relationship_class", "evidence_basis",
        "confidence_tier", "dorothea_level", "curation_effort", "external_sources",
        "reference_text", "reference_pmids", "source_locator", "verification_status",
        "limitations", "export_priority",
    ], sorted(records, key=lambda row: row["external_record_key"]))
    write_tsv(args.output_dir / "source_references.tsv", [
        "external_record_key", "reference_namespace", "reference_id", "reference_locator", "reference_status",
    ], sorted(references, key=lambda row: (row["external_record_key"], row["reference_namespace"], row["reference_id"])))
    write_tsv(args.output_dir / "source_regulons.tsv", [
        "external_regulon_id", "source_registry", "source_version", "species_context",
        "tf_normalized_symbol", "tf_normalized_symbol_key", "regulon_name", "definition_status",
        "membership_semantics", "source_record_count", "materialized_member_count", "export_priority", "limitations",
    ], regulons)
    write_tsv(args.output_dir / "source_regulon_members.tsv", [
        "external_regulon_id", "external_record_key", "target_normalized_symbol",
        "target_normalized_symbol_key", "membership_basis", "regulatory_effect",
        "membership_status", "confidence_tier", "export_priority",
    ], members)
    write_tsv(args.output_dir / "priority_tf_evidence.tsv", [
        "verification_id", "external_record_key", "priority_tf_symbol", "species_context",
        "target_normalized_symbol", "verification_scope", "reference_pmid", "reference_locator",
        "reference_title", "verification_status", "evidence_class", "verified_effect",
        "cell_type_context", "compartment_context", "stimulus_context", "confidence_tier",
        "limitations", "notes",
    ], evidence)

    manifest = {
        "integration_name": "public_tf_union_v1",
        "integration_status": "additive_discovery_layer",
        "retrieval_date": args.retrieval_date,
        "source_registries": sorted({row["source_registry"] for row in registry_rows}),
        "not_imported_public_snapshots": {
            "omnipath_causal_human_mouse": "Retrieved for comparison context but intentionally excluded from v1 materialization; upstream paths use frozen SignalingEdge only."
        },
        "counts": {
            "source_registry_rows": len(registry_rows),
            "source_records": len(records),
            "source_references": len(references),
            "identity_mapping_rows": len(mappings),
            "source_regulons": len(regulons),
            "materialized_source_regulon_members": len(members),
            "priority_tf_verification_rows": len(evidence),
        },
        "priority_tfs": list(PRIORITY_TFS),
        "normalization_policy": "Case-folded exact comparison key for simple symbols; no alias expansion; composite/accession-like values unresolved.",
        "frozen_graph_policy": "No frozen SignalingEntity, SignalingEntityRole, SignalingEdge, Regulon, RegulonMember, or bundle rows are modified by this importer.",
        "snapshots": auxiliary["snapshots"],
    }
    (args.output_dir / "integration_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (args.output_dir / "load_public_tf_union.sql").write_text(
        make_load_sql(args.output_dir), encoding="utf-8"
    )
    unresolved_rows = [
        row for row in mappings
        if row["identity_decision"] != "normalized_exact"
    ]
    write_tsv(args.output_dir / "unresolved_identity_queue.tsv", [
        "source_registry", "source_version", "species_context", "identity_role",
        "source_symbol", "normalized_symbol", "normalized_symbol_key", "identity_decision",
        "identity_reason", "mscidblit_entity_id", "frozen_entity_match_status",
    ], sorted(unresolved_rows, key=lambda row: (
        row["source_registry"], row["species_context"], row["identity_role"], row["source_symbol"]
    )))
    print(json.dumps(manifest["counts"], sort_keys=True))


if __name__ == "__main__":
    main()
