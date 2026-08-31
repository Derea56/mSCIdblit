#!/usr/bin/env python3
"""Assemble staged database leads for Modules 20A/B through 24A/B.

This is deliberately a preparation-layer assembler. It inventories pinned
database snapshots, preserves source record IDs and linked PMID tokens, and
routes records to a module-specific review queue. It never writes canonical
graph/database tables and never promotes a database row to evidence by itself.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "data/processed/module20_24_database_intake_v1/database_registry.tsv"
PMID_RE = re.compile(r"(?<!\d)(?:PMID[:\s-]*)?(\d{5,9})(?!\d)", re.IGNORECASE)
TOKEN_RE = re.compile(r"PMID[:\s-]*(\d{5,9})", re.IGNORECASE)
ENSEMBL_RE = re.compile(r"(?:ENSG|ENSMUSG|ENSRNOG)\d+", re.IGNORECASE)

FIELDS = [
    "lead_id", "database_id", "database_release", "source_record_id", "source_path",
    "source_url", "species", "module_primary", "module_consolidation",
    "module_reason", "layer", "evidence_mode", "database_directness", "entity_a",
    "entity_b", "pathway_or_family", "relationship", "effect", "source_evidence",
    "linked_pmids", "literature_status", "source_locator", "intake_status",
    "review_state", "notes",
]

ECM_TERMS = (
    "collagen", "laminin", "fibronectin", "tenascin", "thrombospondin", "integrin",
    "adhesion", "cadherin", "syndecan", "dystroglycan", "matrix", "extracellular",
    "focal adhesion", "mechanotransduction", "ephrin", "sema", "plexin", "netrin",
    "robo", "slit", "unc5", "dcc", "vcam", "icam", "edil3", "osteopontin",
    "spp1", "thbs", "itga", "itgb", "cd44", "cd47", "ptk2", "paxillin",
)
BOUNDARY_TERMS = (
    "complement", "coagulation", "lipid", "lipoprotein", "eicosanoid", "prostaglandin",
    "leukotriene", "sphingolipid", "protease", "thrombin", "kinin", "bradykinin",
    "anaphylatoxin", "dam p", "purinergic", "c1q", "c1qa", "c1qb", "c1qc", "c2",
    "c3", "c4", "c5", "c5ar", "cf", "properdin", "f2r", "f2rl", "par1", "par2",
    "par3", "par4", "bdkrb", "plg", "pla u", "f3", "f10", "thbd", "procr",
    "ptger", "ptgfr", "tbxa2r", "ltb4r", "cysltr", "s1pr", "scarb", "olr1", "ldlr",
)

RELAY_TERMS = (
    "interleukin", "interferon", "tumor necrosis", "tnf", "tgf", "bmp", "osm", "lif",
    "csf", "chemokine", "egf", "fgf", "pdgf", "vegf", "wnt", "notch", "jak-stat",
    "mapk", "nf-kb", "nfkb", "cytokine", "growth factor",
)

CORE_SIGNAL_SYMBOLS = {
    value.casefold() for value in """
    JAK1 JAK2 JAK3 TYK2 STAT1 STAT2 STAT3 STAT4 STAT5A STAT5B STAT6 MAPK1 MAPK3 MAP2K1
    MAP2K2 AKT1 AKT2 MTOR RPS6KB1 NFKB1 RELA RELB NFKBIA IKBKB IKBKG TRAF2 TRAF6
    MYD88 IRAK1 IRAK4 TLR2 TLR4 TLR7 TLR9 SMAD1 SMAD2 SMAD3 SMAD4 SMAD5 SMAD8 SMAD9
    SRC PTK2 ILK PXN VCL CTNNB1 YAP1 WWTR1 RHOA ROCK1 ROCK2 CAV1 F2R F2RL1 F2RL2
    F2RL3 C3AR1 C5AR1 C5AR2 BDKRB1 BDKRB2 PTGER2 PTGER4 PTGFR TBXA2R LTB4R1 LTB4R2
    CYSLTR1 CYSLTR2 S1PR1 S1PR2 S1PR3 S1PR4 S1PR5 SCARB1 SCARB2 OLR1 LDLR ITGA1 ITGA2
    ITGA3 ITGA4 ITGA5 ITGA6 ITGAV ITGB1 ITGB3 ITGB4 ITGB5 CD44 CD47 CDH1 CDH2 FN1
    COL1A1 COL1A2 COL3A1 COL4A1 COL4A2 LAMA1 LAMA2 LAMB1 LAMC1 THBS1 THBS2 SPP1 VCAM1
    ICAM1 EFNA1 EFNB1 EPHA2 EPHB2 SEMA3A SEMA3F PLXNA1 PLXNB1 ROBO1 ROBO2 NTN1 DCC
    UNC5B
    """.split()
}


def read_delimited(path: Path, delimiter: str = "\t") -> list[dict[str, str]]:
    """Read a delimited file while ignoring leading comment lines."""
    with path.open(newline="", encoding="utf-8-sig", errors="replace") as handle:
        lines = [
            line for line in handle
            if line.strip()
            and not line.lstrip().startswith("#")
            and not line.lstrip().startswith('"#')
        ]
    if not lines:
        return []
    return list(csv.DictReader(lines, delimiter=delimiter))


def read_registry(path: Path) -> list[dict[str, str]]:
    return read_delimited(path)


def clean(value: object) -> str:
    return html.unescape(str(value or "")).strip()


def pmids(value: str) -> list[str]:
    # ConnectomeDB stores Perplexity links whose comma-separated PMID list uses
    # URL-encoded spaces (`%20`). Decode first so the encoding prefix cannot be
    # concatenated with the first digit of the following PMID (for example,
    # `%209883723` must become `9883723`, not `209883723`).
    value = unquote(value or "")
    found = TOKEN_RE.findall(value)
    if found:
        return sorted(set(found), key=int)
    # GtoPdb stores bare PMIDs in a dedicated column. Avoid extracting years or
    # IDs from arbitrary descriptions by requiring 5+ digits here.
    return sorted(set(PMID_RE.findall(value or "")), key=int)


def join_pmids(*values: str) -> str:
    return ";".join(sorted({p for value in values for p in pmids(value)}, key=int))


def explicit_pmids(value: str) -> str:
    value = unquote(value or "")
    return ";".join(sorted(set(TOKEN_RE.findall(value)), key=int))


def norm_text(*values: str) -> str:
    return " ".join(clean(value) for value in values if clean(value)).casefold()


def geneish(value: str) -> str:
    value = clean(value)
    value = re.sub(r"<[^>]+>", "", value)
    return value


def route_by_text(text: str, default: str) -> tuple[str, str, str]:
    """Return A module, B module, and conservative routing reason."""
    lowered = norm_text(text)
    if any(term in lowered for term in ECM_TERMS):
        return "23A", "23B", "ECM/adhesion/mechanotransduction keyword or pathway context"
    if any(term in lowered for term in BOUNDARY_TERMS):
        return "24A", "24B", "complement/coagulation/lipid/protease boundary keyword or pathway context"
    if any(term in lowered for term in RELAY_TERMS):
        return "21A", "21B", "cytokine/chemokine/growth-factor relay keyword or pathway context"
    return default, default.replace("A", "B"), "source default; pair-specific module review still required"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def base_row(reg: dict[str, str], record_id: str, species: str, module: str, module_b: str,
             reason: str, layer: str, evidence_mode: str, directness: str, entity_a: str,
             entity_b: str, family: str, relationship: str, effect: str, source_evidence: str,
             linked: str, locator: str, notes: str = "") -> dict[str, str]:
    source_path = clean(reg.get("local_path", ""))
    source_url = clean(reg.get("source_url", ""))
    status = "database_lead"
    literature_status = "linked_pmids_present" if linked else "no_linked_pmids_in_source_row"
    lead_key = f"{reg['database_id']}::{record_id}::{species}::{module}"
    return {
        "lead_id": lead_key,
        "database_id": reg["database_id"],
        "database_release": clean(reg.get("release", "")),
        "source_record_id": record_id,
        "source_path": source_path,
        "source_url": source_url,
        "species": species,
        "module_primary": module,
        "module_consolidation": module_b,
        "module_reason": reason,
        "layer": layer,
        "evidence_mode": evidence_mode,
        "database_directness": directness,
        "entity_a": entity_a,
        "entity_b": entity_b,
        "pathway_or_family": family,
        "relationship": relationship,
        "effect": effect,
        "source_evidence": source_evidence,
        "linked_pmids": linked,
        "literature_status": literature_status,
        "source_locator": locator,
        "intake_status": status,
        "review_state": "unreviewed_database_lead",
        "notes": notes,
    }


def route_lr(reg: dict[str, str], row: dict[str, str]) -> tuple[str, str, str]:
    text = norm_text(
        row.get("pathway_name", ""), row.get("annotation", ""), row.get("ligand", ""),
        row.get("receptor", ""), row.get("ligand.symbol", ""), row.get("receptor.symbol", ""),
        row.get("Evidence", ""), row.get("AI summary", ""), row.get("Ligand Name", ""),
        row.get("Target Name", ""), row.get("Target systematic name", ""),
    )
    return route_by_text(text, "20A")


def assemble_cellchat(reg: dict[str, str], path: Path) -> list[dict[str, str]]:
    out = []
    for row in read_delimited(path):
        record_id = clean(row.get("interaction_name")) or f"line-{len(out)+2}"
        ligand = geneish(row.get("ligand.symbol") or row.get("ligand"))
        receptor = geneish(row.get("receptor.symbol") or row.get("receptor"))
        module, module_b, reason = route_lr(reg, row)
        out.append(base_row(
            reg, record_id, clean(reg.get("species", "")), module, module_b, reason,
            "intercellular LR", "cellchat_database_annotation", "database LR membership; no directness inferred",
            ligand, receptor, clean(row.get("pathway_name")), "ligand-receptor", clean(row.get("agonist")),
            clean(row.get("evidence")), explicit_pmids(row.get("evidence", "")),
            f"local:{path.relative_to(ROOT)}#{record_id}",
            notes=f"annotation={clean(row.get('annotation'))}; version={clean(row.get('version'))}",
        ))
    return out


def assemble_connectome(reg: dict[str, str], path: Path) -> list[dict[str, str]]:
    out = []
    for row in read_delimited(path, delimiter=","):
        record_id = clean(row.get("Interaction ID")) or f"line-{len(out)+2}"
        ligand = geneish(row.get("Ligand Symbols"))
        receptor = geneish(row.get("Receptor Symbols"))
        module, module_b, reason = route_lr(reg, row)
        linked = join_pmids(row.get("AI summary", ""))
        out.append(base_row(
            reg, record_id, clean(reg.get("species", "")), module, module_b, reason,
            "curated LR", "connectomedb_record_with_linked_literature", clean(row.get("Evidence")) or "curated/inferred LR record",
            ligand, receptor, "", "ligand-receptor", clean(row.get("Evidence")), clean(row.get("Evidence")), linked,
            f"local:{path.relative_to(ROOT)}#{record_id}",
            notes="AI summary URL is retained only as a PMID locator; AI prose is not treated as evidence.",
        ))
    return out


def load_gtopdb_targets() -> dict[tuple[str, str], dict[str, str]]:
    path = ROOT / "work/module20_db_seed/GtoPdb_targets_and_families_2026_2.tsv"
    if not path.exists():
        return {}
    out: dict[tuple[str, str], dict[str, str]] = {}
    for row in read_delimited(path):
        target_id = clean(row.get("Target id"))
        species = "mouse" if clean(row.get("MGI symbol")) else "human"
        symbol = clean(row.get("MGI symbol")) or clean(row.get("HGNC symbol"))
        if target_id and symbol:
            out[(target_id, species)] = row
    return out


def assemble_gtopdb(reg: dict[str, str], path: Path) -> list[dict[str, str]]:
    targets = load_gtopdb_targets()
    out = []
    for index, row in enumerate(read_delimited(path), start=2):
        target_name = geneish(row.get("Target Name"))
        target_species = clean(row.get("Target Species")).casefold() or "unknown"
        species = target_species if target_species in {"human", "mouse", "rat"} else "unknown"
        target = targets.get((clean(row.get("Target ID")), species), {})
        target_symbol = clean(target.get("MGI symbol")) or clean(target.get("HGNC symbol"))
        target_entity = target_symbol or target_name
        ligand = geneish(row.get("Ligand Name"))
        text = norm_text(ligand, target_name, target.get("Family name", ""), target.get("Target systematic name", ""), row.get("List Comment", ""))
        module, module_b, reason = route_by_text(text, "20A")
        record_id = f"{clean(row.get('Ligand ID'))}->{clean(row.get('Target ID'))}:line-{index}"
        linked = join_pmids(
            row.get("Rank Potency Refs(PMIDs)", ""),
            row.get("Rank Potency Refs (PMIDs)", ""),
            row.get("Interaction PubMed IDs", ""),
        )
        out.append(base_row(
            reg, record_id, species, module, module_b, reason, "pharmacology",
            "gtopdb_endogenous_ligand_target", "pharmacology association; no direct binding/SCI transfer inferred",
            ligand, target_entity, clean(target.get("Family name")), "ligand-target", clean(row.get("Rank Potency")),
            clean(row.get("List Comment")), linked, f"local:{path.relative_to(ROOT)}#line-{index}",
            notes=f"target_name={target_name}; target_id={clean(row.get('Target ID'))}; ligand_id={clean(row.get('Ligand ID'))}",
        ))
    return out


def assemble_omnipath(reg: dict[str, str], path: Path) -> list[dict[str, str]]:
    out = []
    focus = load_focus_symbols()
    for index, row in enumerate(read_delimited(path), start=2):
        source = clean(row.get("source_genesymbol")) or clean(row.get("source"))
        target = clean(row.get("target_genesymbol")) or clean(row.get("target"))
        if not source or not target:
            continue
        # Keep only edges in the current module-20–24 entity neighborhood.
        # Without this bounded intake, OmniPath's integrated network would
        # turn the staging queue into a whole-network dump.
        if source.casefold() not in focus or target.casefold() not in focus:
            continue
        text = norm_text(source, target, row.get("sources", ""), row.get("references", ""))
        module, module_b, reason = route_by_text(text, "21A")
        stimulation = clean(row.get("consensus_stimulation"))
        inhibition = clean(row.get("consensus_inhibition"))
        effect = "stimulation" if stimulation == "True" else "inhibition" if inhibition == "True" else "undirected/uncertain"
        linked = join_pmids(row.get("references", ""))
        record_id = f"{source}->{target}:line-{index}"
        out.append(base_row(
            reg, record_id, clean(reg.get("species", "")), module, module_b, reason,
            "intracellular causal signaling", "omnipath_causal_record", "integrated causal/PPI context; not SCI-specific proof",
            source, target, clean(row.get("sources")), "causal-signaling", effect,
            clean(row.get("sources")), linked, f"local:{path.relative_to(ROOT)}#line-{index}",
            notes=f"is_directed={clean(row.get('is_directed'))}; direct={clean(row.get('is_directed'))}; source_provenance_retained",
        ))
    return out


def assemble_reactome(reg: dict[str, str], path: Path) -> list[dict[str, str]]:
    out = []
    for index, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
        if not line.strip() or line.startswith("#"):
            continue
        fields = line.split("\t")
        if len(fields) < 3:
            continue
        pathway_name, pathway_id = fields[0].strip(), fields[1].strip()
        text = norm_text(pathway_name)
        if not any(term in text for term in ECM_TERMS + BOUNDARY_TERMS + RELAY_TERMS):
            continue
        module, module_b, reason = route_by_text(text, "21A")
        out.append(base_row(
            reg, pathway_id, "human", module, module_b, reason, "curated pathway membership",
            "reactome_pathway_context", "pathway context only; no molecular edge promotion",
            pathway_name, "", pathway_name, "pathway-membership", "", pathway_name, "",
            f"local:{path.relative_to(ROOT)}#line-{index}",
            notes="Reactome GMT has no row-level PMID; acquire pathway-linked primary papers during the evidence-search phase.",
        ))
    return out


def load_focus_symbols() -> set[str]:
    """Build a bounded symbol neighborhood from imported LR sources plus core relay nodes."""
    focus = set(CORE_SIGNAL_SYMBOLS)
    source_specs = [
        (ROOT / "data/raw/public_database_snapshots/module20_24_intake_v1/cellchat_human_lr.tsv", "\t", ("ligand.symbol", "receptor.symbol", "ligand", "receptor")),
        (ROOT / "data/raw/public_database_snapshots/module20_24_intake_v1/cellchat_mouse_lr.tsv", "\t", ("ligand.symbol", "receptor.symbol", "ligand", "receptor")),
        (ROOT / "work/module20_db_seed/ConnectomeDB2025_human.csv", ",", ("Ligand Symbols", "Receptor Symbols")),
        (ROOT / "work/module20_db_seed/ConnectomeDB2025_mouse.csv", ",", ("Ligand Symbols", "Receptor Symbols")),
    ]
    for path, delimiter, columns in source_specs:
        if not path.exists():
            continue
        for row in read_delimited(path, delimiter=delimiter):
            for column in columns:
                value = clean(row.get(column))
                for token in re.split(r"[,|;/ _+()]+", value):
                    token = token.strip().casefold()
                    if len(token) > 1 and not token.startswith("http"):
                        focus.add(token)
    return focus


def assemble_sources(registry: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    leads: list[dict[str, str]] = []
    source_rows: list[dict[str, str]] = []
    dispatch = {
        "cellchatdb": assemble_cellchat,
        "connectomedb": assemble_connectome,
        "gtopdb": assemble_gtopdb,
        "omnipath_causal": assemble_omnipath,
        "reactome_pathways": assemble_reactome,
    }
    for reg in registry:
        path_text = clean(reg.get("local_path"))
        path = ROOT / path_text if path_text else None
        exists = bool(path and path.exists())
        row_count = 0
        digest = ""
        if exists and path:
            digest = sha256(path)
            loader = next((fn for prefix, fn in dispatch.items() if reg["database_id"].startswith(prefix)), None)
            if loader:
                source_leads = loader(reg, path)
                leads.extend(source_leads)
                row_count = len(source_leads)
        source_rows.append({
            **reg,
            "resolved_path": str(path) if path else "",
            "exists": "true" if exists else "false",
            "sha256": digest,
            "assembled_lead_rows": str(row_count),
        })
    return leads, source_rows


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "data/processed/module20_24_database_intake_v1")
    args = parser.parse_args()
    registry = read_registry(args.registry)
    leads, sources = assemble_sources(registry)
    leads.sort(key=lambda row: (row["module_primary"], row["database_id"], row["source_record_id"], row["species"]))
    write_tsv(args.output_dir / "database_source_registry_audit.tsv", list(sources[0]) if sources else [], sources)
    write_tsv(args.output_dir / "database_candidate_leads.tsv", FIELDS, leads)
    by_module = Counter(row["module_primary"] for row in leads)
    by_db = Counter(row["database_id"] for row in leads)
    with_pmids = sum(bool(row["linked_pmids"]) for row in leads)
    manifest = {
        "registry": str(args.registry.relative_to(ROOT)) if args.registry.is_relative_to(ROOT) else str(args.registry),
        "output_dir": str(args.output_dir.relative_to(ROOT)) if args.output_dir.is_relative_to(ROOT) else str(args.output_dir),
        "registry_rows": len(registry),
        "imported_sources": sum(row["exists"] == "true" for row in sources),
        "planned_or_missing_sources": sum(row["exists"] != "true" for row in sources),
        "candidate_lead_rows": len(leads),
        "leads_with_linked_pmids": with_pmids,
        "leads_without_linked_pmids": len(leads) - with_pmids,
        "by_module": dict(sorted(by_module.items())),
        "by_database": dict(sorted(by_db.items())),
        "canonical_write_performed": False,
    }
    (args.output_dir / "database_intake_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
