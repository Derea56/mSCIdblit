#!/usr/bin/env python3
"""Export a conservative cross-module synthesis for Modules 20B-24B.

This is an audit-layer synthesis. It reports layer counts and candidate node
convergence, but never creates a ligand-to-TF path unless the source registers
already encode that path explicitly.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "work" / "module_b_consolidation"
OUT_JSON = ROOT / "data" / "processed" / "cross_module_synthesis_20_24.json"
OUT_MD = ROOT / "docs" / "CROSS_MODULE_SYNTHESIS_20_24.md"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def split_entities(value: str) -> set[str]:
    return {
        token.strip().upper()
        for token in re.split(r"[;,/]", value)
        if token.strip()
    }


def contains_entity_alias(value: str, aliases: tuple[str, ...]) -> bool:
    """Match curated aliases without substring false positives."""
    text = value.upper().replace("Κ", "K")
    for alias in aliases:
        pattern = re.escape(alias.upper())
        if re.search(rf"(?<![A-Z0-9]){pattern}(?![A-Z0-9])", text):
            return True
    return False


def edge_ids_matching(
    rows: list[dict[str, str]],
    field: str,
    aliases: tuple[str, ...],
    *,
    extra_patterns: tuple[str, ...] = (),
) -> list[str]:
    """Return stable edge IDs matching an explicit alias/composite rule."""
    matched: list[str] = []
    for row in rows:
        value = row[field]
        if contains_entity_alias(value, aliases) or any(
            re.search(pattern, value.upper()) for pattern in extra_patterns
        ):
            matched.append(row["b_edge_id"])
    return matched


def build_convergence_groups(
    edges21: list[dict[str, str]], edges22: list[dict[str, str]]
) -> list[dict[str, object]]:
    """Build an alias-aware, audit-only convergence candidate registry.

    Composite labels remain intact. This registry supports review and
    triage; it does not create new molecular edges or split unresolved
    receptor/paralog labels.
    """
    definitions = [
        ("CSL", "CSL", ("CSL",), "exact token overlap", "21B uses the RBPJ/CSL composite; CSL is not separately resolved."),
        ("RBPJ", "RBPJ", ("RBPJ",), "exact token overlap", "21B uses the RBPJ/CSL composite; RBPJ is not separately resolved from CSL."),
        ("HES1", "HES1", ("HES1",), "exact token overlap", "22B includes program and phenotype outputs; no shared ligand-to-HES1 route is asserted."),
        ("HES5", "HES5", ("HES5",), "exact token overlap", "21B is a Notch/HES5 SCI-context relay; 22B also contains BMP/HES5 comparator evidence."),
        ("HEY1", "HEY1", ("HEY1",), "exact token overlap", "22B HEY1 records are program/phenotype associations, not a universal Notch output claim."),
        ("NFKB2", "NFKB2", ("NFKB2",), "explicit token in NFKB2-p100/p52 and NFKB2;RELB labels", "21B resolves an alternative NF-kappaB branch but not every p100/p52 processing step."),
        ("RELA_NFKB_P65", "RELA / NF-kB p65", ("RELA", "NF-KB P65", "NFKB P65"), "curated alias group with bounded RELA matching", "RELA and NF-kB p65 are routing aliases, not a new direct edge; 'relay' is excluded."),
        ("SMAD1", "SMAD1", ("SMAD1",), "exact token plus composite-branch match", "21B BMP labels are composite/paralog-unresolved; SMAD1 is not an independent 21B edge."),
        ("SMAD2", "SMAD2", ("SMAD2",), "exact token overlap", "Shared SMAD2 does not establish receptor, species, or cell-model equivalence."),
        ("SMAD3", "SMAD3", ("SMAD3",), "exact token overlap", "Shared SMAD3 does not establish receptor, species, or cell-model equivalence."),
        ("SMAD4", "SMAD4", ("SMAD4",), "exact token overlap", "SMAD4 is a shared complex partner/output node, not proof of one upstream route."),
        ("SMAD5", "SMAD5", ("SMAD5",), "exact token plus composite-branch match", "21B BMP labels are composite/paralog-unresolved; SMAD5 is not an independent 21B edge."),
        ("SMAD8", "SMAD8", ("SMAD8",), "exact token plus composite-branch match", "21B BMP labels are composite/paralog-unresolved; SMAD8 is not an independent 21B edge."),
        ("SMAD9", "SMAD9", ("SMAD9",), "explicit compact composite-branch match", "SMAD9 is represented in 21B by the compact SMAD1/SMAD5/SMAD8/9 label; it is not independently resolved."),
        ("STAT1", "STAT1", ("STAT1",), "exact token overlap", "22B includes STAT1-only and composite STAT/IRF records; no single receptor route is selected."),
        ("STAT2", "STAT2", ("STAT2",), "exact token overlap", "STAT2 may be part of the composite STAT1/STAT2/IRF9 evidence and is not split from it."),
        ("STAT3", "STAT3", ("STAT3",), "exact token overlap", "STAT3 is a candidate convergence point, not a claim that all upstream complexes share one outcome."),
        ("STAT5B", "STAT5B", ("STAT5B",), "exact token overlap", "22B includes STAT5A/STAT5B composite records; those remain composite."),
        ("YAP", "YAP", ("YAP",), "exact token overlap", "The FGF/RHOA/YAP and mechanotransduction records do not establish a universal FGF-to-YAP route."),
    ]
    groups: list[dict[str, object]] = []
    for node_id, display_label, aliases, basis, limitation in definitions:
        extra_patterns = ()
        if node_id in {"SMAD1", "SMAD5", "SMAD8", "SMAD9"}:
            extra_patterns = (r"SMAD1/SMAD5/SMAD8/9", r"SMAD1/SMAD5/SMAD8\s+IN\s+SPINAL")
        target_ids = edge_ids_matching(
            edges21, "target_entity", aliases, extra_patterns=extra_patterns
        )
        source_ids = edge_ids_matching(edges22, "source_entity", aliases)
        target_rows = {row["b_edge_id"]: row for row in edges21}
        source_rows = {row["b_edge_id"]: row for row in edges22}
        groups.append({
            "node_id": node_id,
            "display_label": display_label,
            "normalization_basis": basis,
            "relay_21b_edge_ids": target_ids,
            "tf_22b_edge_ids": source_ids,
            "relay_21b_edge_count": len(target_ids),
            "tf_22b_edge_count": len(source_ids),
            "relay_21b_exportable_edge_count": sum(
                target_rows[edge_id]["exportable"] == "true" for edge_id in target_ids
            ),
            "tf_22b_exportable_edge_count": sum(
                source_rows[edge_id]["exportable"] == "true" for edge_id in source_ids
            ),
            "status": "candidate_convergence_only",
            "limitation": limitation,
        })
    return groups


def module_summary(module: str) -> dict[str, object]:
    directory = BASE / f"module{module}b"
    edges = read_tsv(directory / f"module{module}b_edge_register.tsv")
    evidence = read_tsv(directory / f"module{module}b_evidence_register.tsv")
    boundaries = read_tsv(directory / f"module{module}b_boundary_register.tsv")
    return {
        "module": f"{module}B",
        "edges": len(edges),
        "evidence": len(evidence),
        "boundaries": len(boundaries),
        "exportable_edges": sum(row["exportable"] == "true" for row in edges),
        "edge_layers": dict(sorted(Counter(row["evidence_layer"] for row in edges).items())),
        "nonexportable_edges": sum(row["exportable"] != "true" for row in edges),
        "exportable_evidence_without_locator": sum(
            row["exportable"] == "true" and not row["source_locator"] for row in evidence
        ),
    }


def build() -> dict[str, object]:
    summaries = [module_summary(module) for module in ("20", "21", "22", "23", "24")]
    edges21 = read_tsv(BASE / "module21b/module21b_edge_register.tsv")
    edges22 = read_tsv(BASE / "module22b/module22b_edge_register.tsv")
    relay_targets = {
        token
        for row in edges21
        for token in split_entities(row["target_entity"])
        if token not in {"NONE_IDENTIFIED", "N/A", "NULL"}
    }
    tf_sources = {
        token
        for row in edges22
        for token in split_entities(row["source_entity"])
        if token not in {"NONE_IDENTIFIED", "N/A", "NULL"}
    }
    candidate_convergence_nodes = sorted(
        token for token in relay_targets & tf_sources
        if len(token) >= 3 and not token.isdigit()
    )
    candidate_convergence_groups = build_convergence_groups(edges21, edges22)
    synthesis_themes = [
        {
            "theme_id": "CMS20-24-T001",
            "title": "Extracellular Handoff Is the Entry Layer, Not a Complete Mechanism",
            "statement": "20B defines a large ligand-receptor candidate universe, but its LR evidence does not by itself establish receptor-proximal relay, downstream TF, or cellular-function outcomes.",
            "boundary": "Only the 1,110 high/medium rows pass the conservative 20B export gate. The 183 uncertain direct candidates remain queryable but non-exportable; low, no-evidence, and non-LR classifications remain explicit boundaries.",
        },
        {
            "theme_id": "CMS20-24-T002",
            "title": "Receptor Complexes Converge on a Limited Relay Vocabulary",
            "statement": "21B shows convergence onto JAK/STAT, NF-kappaB/MAPK, GPCR, RTK, TGF-beta/SMAD, WNT, and Notch branches while retaining receptor-complex and ligand-context distinctions.",
            "boundary": "Shared relay nodes such as STAT3 or SMAD4 are candidate convergence points, not proof that every upstream ligand uses the same receptor complex or branch.",
        },
        {
            "theme_id": "CMS20-24-T003",
            "title": "Terminal TF Evidence Is More Selective Than Pathway Evidence",
            "statement": "22B contains many pathway/program and phenotype records, but only the exportable subset should support receiver-state traversal; direct TF binding, target regulation, program association, and phenotype evidence remain separate.",
            "boundary": "Most 22B records are non-exportable or boundary-limited, so pathway presence must not be converted into a terminal TF-target claim.",
        },
        {
            "theme_id": "CMS20-24-T004",
            "title": "Matrix and Noncanonical Extracellular Systems Are Parallel Inputs",
            "statement": "23B and 24B add matrix/adhesion/mechanotransduction and complement/coagulation/lipid/protease records as candidate extracellular inputs alongside soluble cytokine signaling.",
            "boundary": "Exportable means source-backed at the audit layer, not SCI-specific applicability or a complete intracellular route. These layers require explicit receptor, sensor, fragment, compartment, timing, and perturbation evidence before being merged into a shared mechanism.",
        },
    ]
    return {
        "status": "reviewable first-pass cross-module synthesis",
        "source_scope": "Module 20B-24B audit layers",
        "canonical_materialization_status": "blocked_pending_canonical_schema_and_source_anchor_resolution",
        "module_summaries": summaries,
        "candidate_convergence_nodes": candidate_convergence_nodes,
        "candidate_convergence_summary": {
            "strict_exact_label_overlap_count": len(candidate_convergence_nodes),
            "alias_aware_candidate_group_count": len(candidate_convergence_groups),
            "alias_aware_candidate_groups": candidate_convergence_groups,
        },
        "synthesis_themes": synthesis_themes,
        "linkage_rules": [
            "20B ligand-receptor edges are not automatically connected to 21B relay edges; exact ligand, receptor complex, species, cell model, and assay context must match.",
            "21B relay targets and 22B TF sources define candidate convergence nodes only; shared names do not prove a ligand-to-TF path.",
            "23B and 24B matrix, adhesion, complement, coagulation, lipid, and protease edges remain parallel extracellular/contextual layers unless an explicit receptor-to-relay link is source-backed.",
            "Boundary and no-evidence records remain queryable but are excluded from supported path claims.",
            "Exportability is a provenance gate, not a claim of universal biology, SCI receiver-cell relevance, or end-to-end pathway completion.",
        ],
        "next_validation": [
            "Resolve stable PMID/PMCID/DOI/URL citations to canonical Paper rows.",
            "Attach each exportable evidence record to a canonical paper, observation, or author-claim anchor.",
            "Materialize only after source-anchor and entity/pathway deduplication checks pass.",
        ],
    }


def render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# Module 20B–24B Cross-Module Synthesis",
        "",
        "This is a conservative audit-layer synthesis. Shared node names identify",
        "candidate convergence only; they do not establish a complete ligand→TF",
        "path without exact source-backed relay linkage.",
        "",
        f"Canonical materialization status: **{payload['canonical_materialization_status']}**.",
        "",
        "## Module coverage",
        "",
        "| Module | Edges | Evidence | Boundaries | Exportable edges | Non-exportable edges |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in payload["module_summaries"]:
        lines.append(
            f"| {row['module']} | {row['edges']:,} | {row['evidence']:,} | "
            f"{row['boundaries']:,} | {row['exportable_edges']:,} | {row['nonexportable_edges']:,} |"
        )
    lines.extend([
        "",
        "Boundary counts are evidence-register boundary records; they are not",
        "identical to the number of non-exportable edges when one boundary record",
        "covers multiple edges or when an edge has non-boundary context.",
        "",
        "## Candidate convergence nodes",
        "",
        "The following entities occur as targets in 21B and as source TF entities in 22B:",
        "",
        ", ".join(f"`{node}`" for node in payload["candidate_convergence_nodes"])
        or "No exact shared node names were found.",
        "",
        f"The strict token overlap contains **{len(payload['candidate_convergence_nodes'])}** labels. "
        f"An alias/composite-aware audit expands this to **{payload['candidate_convergence_summary']['alias_aware_candidate_group_count']}** candidate groups:",
        "",
        "| Candidate group | 21B relay edges | 22B TF/program edges | Normalization basis | Status |",
        "|---|---:|---:|---|---|",
    ])
    for group in payload["candidate_convergence_summary"]["alias_aware_candidate_groups"]:
        lines.append(
            f"| `{group['display_label']}` | {group['relay_21b_exportable_edge_count']}/"
            f"{group['relay_21b_edge_count']} | {group['tf_22b_exportable_edge_count']}/"
            f"{group['tf_22b_edge_count']} | {group['normalization_basis']} | "
            f"{group['status']} |"
        )
    lines.extend([
        "",
        "The expanded groups add HES5, NFKB2, RELA/NF-kB p65, YAP, and "
        "SMAD9 as a composite-branch candidate while preserving the "
        "SMAD1/5/8/9 label. These are review conveniences only; "
        "they do not create molecular edges or split unresolved labels.",
        "",
        "Counts in the convergence table are shown as **exportable/total audit "
        "edges**. Boundary or no-evidence rows remain visible in the denominator "
        "but cannot support a traversable path.",
        "",
        "These are routing candidates, not asserted end-to-end paths. STAT and SMAD",
        "branches require exact receptor-complex, species, cell-model, perturbation,",
        "and TF evidence alignment before they can be used in simulator traversal.",
        "",
        "The overlap includes composite labels such as `RBPJ/CSL` and `SMAD1/5/8`;",
        "these are not silently split into independent molecular edges.",
        "",
        "## Cross-module themes",
        "",
    ])
    for theme in payload["synthesis_themes"]:
        lines.extend([
            f"### {theme['theme_id']}: {theme['title']}",
            "",
            theme["statement"],
            "",
            f"Boundary: {theme['boundary']}",
            "",
        ])
    lines.extend([
        "## Linkage rules",
        "",
    ])
    lines.extend(f"- {rule}" for rule in payload["linkage_rules"])
    lines.extend([
        "",
        "## Required next work",
        "",
    ])
    lines.extend(f"- {item}" for item in payload["next_validation"])
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    payload = build()
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n")
    OUT_MD.write_text(render_markdown(payload))
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"candidate_convergence_nodes={len(payload['candidate_convergence_nodes'])}")


if __name__ == "__main__":
    main()
