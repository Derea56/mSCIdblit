#!/usr/bin/env python3
"""Export first-pass cross-module synthesis from the consensus register."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTER = ROOT / "data" / "processed" / "consensus_review_register.json"
DEFAULT_JSON = ROOT / "data" / "processed" / "cross_module_synthesis.json"
DEFAULT_MD = ROOT / "docs" / "CROSS_MODULE_SYNTHESIS.md"


@dataclass(frozen=True)
class Theme:
    theme_id: str
    title: str
    aim_alignment: str
    module_keys: tuple[str, ...]
    core_consensus_ids: tuple[str, ...]
    synthesis_statement: str
    evidence_ladder: tuple[str, ...]
    boundaries: tuple[str, ...]
    experimental_implications: tuple[str, ...]
    confidence_label: str


THEMES = (
    Theme(
        theme_id="CMS-T001",
        title="Anatomy-First Reconstruction Logic",
        aim_alignment="Aim 2 and Aim 3",
        module_keys=("1b", "2b", "6b", "8b", "10b"),
        core_consensus_ids=("M1B-S001", "M1B-S005", "M1B-S007", "M2B-S005", "M6B-S001", "M6B-S008", "M8B-S005", "M10B-S005"),
        synthesis_statement=(
            "SCI reconstruction should begin from lesion anatomy rather than from a generic repair intervention. "
            "Chronic lesions contain separable fibrotic, astrocytic, immune, white-matter, cavitary, bridge, and human imaging/pathology compartments, "
            "and scaffold or surgical strategies only become interpretable when matched to those compartments."
        ),
        evidence_ladder=(
            "Observations: Module 1 and Module 6 define local and human lesion compartments; Module 8 defines model-system fields needed to preserve lesion architecture.",
            "Author claims: scaffold and clinical rows repeatedly frame feasibility or targeting around lesion geometry, chronicity, and completeness.",
            "Consensus: Module 1 and Module 6 support anatomy-specific representation; Module 2 and Module 10 caution against generic efficacy claims.",
        ),
        boundaries=(
            "Scar resection alone is distinct from resection plus reconstruction.",
            "Human imaging, pathology, and registry rows support selection and feasibility more strongly than efficacy.",
            "Rodent transection, contusion, and hemisection lesions should not be pooled without lesion-topology fields.",
        ),
        experimental_implications=(
            "Represent each proposed reconstruction experiment with explicit lesion compartment, chronicity, resection status, scaffold geometry, and endpoint family.",
            "Use human imaging/pathology boundaries to define candidacy logic before translating scaffold or cell claims.",
        ),
        confidence_label="high for ontology and boundary logic; medium for intervention selection",
    ),
    Theme(
        theme_id="CMS-T002",
        title="Host State Is a Modifiable Repair Variable",
        aim_alignment="Aim 1, Aim 1C, Aim 2, and Aim 3",
        module_keys=("3b", "7b", "11b", "12b"),
        core_consensus_ids=("M3B-S001", "M3B-S002", "M3B-S005", "M7B-S007", "M7B-S008", "M11B-S008", "M12B-S001", "M12B-S008"),
        synthesis_statement=(
            "The host response is not merely damage to suppress; it is a timing-, cell-state-, and tissue-context-dependent variable that can be conditioned. "
            "Immune, vascular, stromal, and innate-adaptor programs can support containment, debris handling, tolerance-like protection, or repair permissiveness, "
            "but the same broad intervention class can be harmful or uninformative when timing and cell identity are lost."
        ),
        evidence_ladder=(
            "Observations: immune/myeloid rows separate depletion, corralling, metabolism, pyroptosis, debris handling, and delivery contexts.",
            "Author claims: host-conditioning analogs from implants, flaps, islets, organ tolerance, ischemia, and LPS support pre-challenge state modification.",
            "Consensus: Modules 3, 7, 11, and 12 converge on state-specific conditioning while rejecting broad anti-inflammatory or direct clinical LPS framing.",
        ),
        boundaries=(
            "Low-dose LPS is a discovery platform for endogenous protection, not a proposed clinical conditioning agent.",
            "Perioperative ischemic conditioning is an analog for timing and host-state logic, not direct evidence for traumatic chronic reconstruction.",
            "Cross-field host-conditioning evidence requires route, dose, timing, tissue, endpoint, and field-to-SCI distance labels.",
        ),
        experimental_implications=(
            "Build candidate-node tables for TLR4/adaptor routing, IL-1/IL-1R1, IL-10, monocyte/endothelial state, and myeloid metabolic competence.",
            "Design conditioning experiments around pre-specified windows: pre-injury conditioning, peri-implant conditioning, and post-injury remodeling are separate questions.",
        ),
        confidence_label="medium-high for biological logic; medium for SCI reconstruction translation",
    ),
    Theme(
        theme_id="CMS-T003",
        title="Biomaterial and Cell Effects Are System-Level Claims",
        aim_alignment="Aim 1B and Aim 3",
        module_keys=("2b", "3b", "4b", "5b", "7b", "9b", "12b"),
        core_consensus_ids=("M2B-S002", "M2B-S003", "M2B-S007", "M3B-S007", "M4B-S006", "M5B-S006", "M7B-S008", "M9B-S006", "M12B-S007"),
        synthesis_statement=(
            "Most biomaterial, cell, cargo, vesicle, and stimulation strategies should be treated as combined repair systems unless experiments isolate each component. "
            "The database should therefore preserve material architecture, cell identity, payload, release kinetics, lesion preparation, host state, and validation model before making causal claims."
        ),
        evidence_ladder=(
            "Observations: scaffold, cell-transplant, immune-delivery, and axon-repair rows often combine architecture, cells, trophic cargo, immunomodulation, and stimulation.",
            "Author claims: many papers interpret bundled interventions as repair-promoting, but component attribution is often not isolated.",
            "Consensus: Modules 2, 4, and 5 agree that scaffold-cell-graft-regeneration claims require component and endpoint separation.",
        ),
        boundaries=(
            "Histological improvement does not guarantee functional recovery.",
            "Carrier effects must be separated from payload biology where possible.",
            "In vitro biomaterial compatibility supports validation, not standalone in vivo repair efficacy.",
        ),
        experimental_implications=(
            "Use factorial or staged designs where feasible: scaffold-only, cell-only, cargo-only, host-conditioning-only, and combined arms.",
            "Before in vivo reconstruction, validate cytocompatibility, inflammatory response, release behavior, and guidance effects in Module 9-style systems.",
        ),
        confidence_label="high for attribution boundary; medium for specific component prioritization",
    ),
    Theme(
        theme_id="CMS-T004",
        title="Repair Endpoints Must Remain Orthogonal",
        aim_alignment="Aim 2 and Aim 3",
        module_keys=("1b", "2b", "4b", "5b", "6b", "8b", "10b"),
        core_consensus_ids=("M1B-S006", "M2B-S003", "M4B-S002", "M4B-S004", "M5B-S001", "M5B-S003", "M5B-S004", "M6B-S005", "M8B-S006", "M10B-S007"),
        synthesis_statement=(
            "SCI repair cannot be summarized by a single recovery axis. Axon growth, sprouting, remyelination, white-matter preservation, graft integration, relay formation, electrophysiology, imaging biomarkers, and behavior are related but non-interchangeable endpoint families."
        ),
        evidence_ladder=(
            "Observations: modules preserve separate histology, imaging, behavior, electrophysiology, graft, myelin, and circuit readouts.",
            "Author claims: many studies infer repair from selected endpoints, but consensus records repeatedly flag endpoint mismatch.",
            "Consensus: Module 5 provides the strongest endpoint taxonomy, with Modules 2, 4, 6, 8, and 10 reinforcing context-specific interpretation.",
        ),
        boundaries=(
            "Sprouting, regeneration, relay engagement, spared-tract plasticity, and behavioral association should not be collapsed.",
            "Clinical registry endpoints need results linkage before efficacy synthesis.",
            "Remote neurodegeneration and local lesion-bed repair are linked but distinct evidence layers.",
        ),
        experimental_implications=(
            "Predefine primary endpoint family for each proposed experiment and treat secondary endpoints as mechanistic support rather than proof of efficacy.",
            "Map in vivo behavioral assays to tract, level, injury severity, and lesion architecture before comparing across studies.",
        ),
        confidence_label="high for endpoint ontology; medium for cross-endpoint causal inference",
    ),
    Theme(
        theme_id="CMS-T005",
        title="Model Systems Are Evidence Filters",
        aim_alignment="Aim 1A, Aim 1B, Aim 2, and Aim 3",
        module_keys=("8b", "9b", "10b", "11b", "12b"),
        core_consensus_ids=("M8B-S001", "M8B-S002", "M8B-S004", "M8B-S008", "M9B-S001", "M9B-S003", "M9B-S008", "M10B-S003", "M11B-S003", "M12B-S007"),
        synthesis_statement=(
            "Model choice is not background metadata; it filters what any observation can mean. In vivo, in vitro, registry, ischemia-conditioning, and innate-stimulation systems answer different questions and should be used as a ladder from discovery to validation to translation."
        ),
        evidence_ladder=(
            "Observations: Module 8 and 9 define in vivo and in vitro model fields; Modules 10-12 define clinical, ischemia, and innate-conditioning evidence roles.",
            "Author claims: model-system claims are often broad, but the consensus layer converts them into operational model-selection rules.",
            "Consensus: model modules support structured evidence use rather than pooled model-agnostic conclusions.",
        ),
        boundaries=(
            "In vitro injury stimuli isolate mechanisms but do not reproduce full lesion architecture.",
            "Animal ischemia conditioning informs protection timing but differs from traumatic SCI and chronic reconstruction.",
            "Registry records identify translational activity but require publication/results linkage for outcome synthesis.",
        ),
        experimental_implications=(
            "Use model systems sequentially: discovery in conditioning datasets, mechanism validation in vitro, anatomy-appropriate in vivo testing, and clinical translation only through safety-feasibility frames.",
            "Record species, injury mechanism, level, severity, chronicity, culture format, maturity, stimulus, and endpoint for every cross-module synthesis claim.",
        ),
        confidence_label="high for model-selection rules; medium for translational extrapolation",
    ),
    Theme(
        theme_id="CMS-T006",
        title="Preconditioning Hypothesis for SCI Reconstruction",
        aim_alignment="Integrated aims logic",
        module_keys=("1b", "2b", "3b", "4b", "5b", "7b", "9b", "11b", "12b"),
        core_consensus_ids=("M1B-S008", "M2B-S005", "M3B-S008", "M4B-S008", "M5B-S008", "M7B-S008", "M9B-S008", "M11B-S008", "M12B-S008"),
        synthesis_statement=(
            "The most defensible project-level hypothesis is that conditioning can improve SCI reconstruction only if it creates a host state compatible with the target lesion anatomy, implanted material or graft, and desired endpoint family. "
            "The evidence supports a conditioning-discovery and validation program, not an immediate universal conditioning therapy claim."
        ),
        evidence_ladder=(
            "Observations: all core modules now provide experiment-level rows and B-layer observations suitable for cross-module tracing.",
            "Author claims: repair, conditioning, graft, biomaterial, and immune claims are strongest when narrowed to model, timing, and endpoint.",
            "Consensus: Modules 1-12 collectively support an aim-aligned logic of endogenous protective programs, host response modification, and host-biomaterial interaction testing.",
        ),
        boundaries=(
            "Conditioning should not be framed as simply anti-inflammatory.",
            "Pre-injury conditioning, perioperative conditioning, and post-injury remodeling are distinct intervention classes.",
            "Clinical translation must route through safer analogs and trial-readiness logic rather than direct LPS or unvalidated host priming.",
        ),
        experimental_implications=(
            "Aim 1 should identify protective regulatory programs and candidate nodes, with full source confidence labels retained.",
            "Aim 2 should test whether conditioning changes acute/subacute lesion response using anatomy- and endpoint-defined in vivo models.",
            "Aim 3 should test whether conditioning improves scaffold/graft integration through host-state, biomaterial, immune, and repair endpoint readouts.",
        ),
        confidence_label="medium-high as a project synthesis hypothesis",
    ),
)


def load_register(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def index_rows(register: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    modules = {row["module_key"]: row for row in register["module_rows"]}
    consensus = {row["consensus_id"]: row for row in register["consensus_rows"]}
    return modules, consensus


def summarize_theme(theme: Theme, modules: dict[str, dict[str, Any]], consensus: dict[str, dict[str, Any]]) -> dict[str, Any]:
    missing_modules = [key for key in theme.module_keys if key not in modules]
    missing_consensus = [cid for cid in theme.core_consensus_ids if cid not in consensus]
    if missing_modules or missing_consensus:
        raise ValueError(
            f"{theme.theme_id} has missing modules={missing_modules} missing_consensus={missing_consensus}"
        )

    consensus_rows = [consensus[cid] for cid in theme.core_consensus_ids]
    module_rows = [modules[key] for key in theme.module_keys]
    confidence_tally: dict[str, int] = {}
    for row in consensus_rows:
        for label, count in row.get("observation_confidence", {}).items():
            confidence_tally[label] = confidence_tally.get(label, 0) + count
    return {
        **asdict(theme),
        "module_labels": [row["module"] for row in module_rows],
        "module_counts": {
            "observations": sum(row["observations"] for row in module_rows),
            "author_claims": sum(row["author_claims"] for row in module_rows),
            "evidence_links": sum(row["evidence_links"] for row in module_rows),
            "boundary_records": sum(row["boundary_records"] for row in module_rows),
            "consensus_drafts": sum(row["consensus_drafts"] for row in module_rows),
        },
        "core_consensus": [
            {
                "consensus_id": row["consensus_id"],
                "module": row["module"],
                "topic_id": row["topic_id"],
                "statement": row["statement"],
                "observation_count": row["observation_count"],
                "claim_count": row["claim_count"],
                "boundary_count": row["boundary_count"],
                "review_action": row["review_action"],
            }
            for row in consensus_rows
        ],
        "observation_confidence_tally": dict(sorted(confidence_tally.items())),
    }


def build_synthesis(register: dict[str, Any]) -> dict[str, Any]:
    modules, consensus = index_rows(register)
    themes = [summarize_theme(theme, modules, consensus) for theme in THEMES]
    all_theme_consensus = sorted({cid for theme in THEMES for cid in theme.core_consensus_ids})
    return {
        "status": "first-pass cross-module synthesis",
        "generated_from": str(DEFAULT_REGISTER.relative_to(ROOT)),
        "theme_count": len(themes),
        "core_consensus_count": len(all_theme_consensus),
        "source_module_count": register["module_count"],
        "source_consensus_count": register["consensus_count"],
        "themes": themes,
        "global_boundaries": [
            "Do not pool across lesion anatomy, model system, timing, or endpoint family.",
            "Keep empirical observations, author claims, consensus statements, and project hypotheses separated.",
            "Treat medium/low-confidence abstract rows as synthesis-supporting but not quantitative proof.",
            "Route clinical interpretation through registry/publication/results linkage before efficacy claims.",
        ],
        "next_actions": [
            "Use this synthesis as the scaffold for a grant-facing significance/innovation narrative.",
            "Build an Aim 1C regulatory-node table from Modules 3B, 7B, 11B, and 12B.",
            "Perform full-text upgrades for direct LPS, host-conditioning, immune-myeloid, and scaffold/graft anchor rows before quantitative claims.",
            "Run PostgreSQL fresh-load validation when psql/createdb are available.",
        ],
    }


def render_markdown(synthesis: dict[str, Any]) -> str:
    lines: list[str] = [
        "# Cross-Module Synthesis",
        "",
        "**Status**: first-pass synthesis from the consensus review register.",
        "",
        "**Scope**: Modules 1B-12B, organized around the revised preconditioning and reconstruction aims.",
        "",
        "**Use**: grant-facing logic layer and database navigation aid; not a final quantitative meta-analysis.",
        "",
        "## Executive Synthesis",
        "",
        (
            "The cross-module evidence supports an anatomy- and host-state-centered model of SCI reconstruction. "
            "Chronic SCI repair should not be framed as whether scaffolds, cells, immune modulation, or conditioning work in isolation. "
            "The stronger synthesis is that lesion anatomy, host immune/stromal state, biomaterial or graft design, model system, and endpoint family must be co-specified before any repair claim is interpretable."
        ),
        "",
        (
            "The preconditioning logic is therefore defensible as a discovery and validation program: identify endogenous protective programs, "
            "test whether conditioning changes the host response to anticipated injury or reconstruction, and evaluate whether that conditioned host state improves material/graft integration. "
            "The current corpus supports this logic qualitatively, with confidence labels and boundaries retained; it does not yet support a universal clinical conditioning claim."
        ),
        "",
        "## Synthesis Themes",
        "",
    ]
    for theme in synthesis["themes"]:
        counts = theme["module_counts"]
        confidence = ", ".join(f"{k}: {v}" for k, v in theme["observation_confidence_tally"].items()) or "not linked"
        lines.extend(
            [
                f"### {theme['theme_id']}: {theme['title']}",
                "",
                f"**Aim alignment**: {theme['aim_alignment']}",
                "",
                f"**Modules**: {', '.join(theme['module_labels'])}",
                "",
                f"**Core consensus IDs**: {', '.join(theme['core_consensus_ids'])}",
                "",
                f"**Evidence footprint**: {counts['observations']} observations / {counts['author_claims']} claims / {counts['evidence_links']} links / {counts['boundary_records']} boundaries / {counts['consensus_drafts']} consensus drafts across participating modules.",
                "",
                f"**Observation confidence in core consensus**: {confidence}.",
                "",
                f"**Synthesis statement**: {theme['synthesis_statement']}",
                "",
                "**Evidence Ladder**",
                "",
            ]
        )
        lines.extend(f"- {item}" for item in theme["evidence_ladder"])
        lines.extend(["", "**Boundaries**", ""])
        lines.extend(f"- {item}" for item in theme["boundaries"])
        lines.extend(["", "**Experimental Implications**", ""])
        lines.extend(f"- {item}" for item in theme["experimental_implications"])
        lines.extend(["", f"**Confidence**: {theme['confidence_label']}", ""])

    lines.extend(
        [
            "## Global Boundary Rules",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in synthesis["global_boundaries"])
    lines.extend(["", "## Next Actions", ""])
    lines.extend(f"- {item}" for item in synthesis["next_actions"])
    lines.extend(
        [
            "",
            "## Core Consensus Matrix",
            "",
            "| Theme | Consensus | Module | Topic | Observation Count | Claim Count | Boundary Count | Review Action |",
            "|---|---|---|---|---:|---:|---:|---|",
        ]
    )
    for theme in synthesis["themes"]:
        for row in theme["core_consensus"]:
            lines.append(
                f"| {theme['theme_id']} | {row['consensus_id']} | {row['module']} | {row['topic_id']} | "
                f"{row['observation_count']} | {row['claim_count']} | {row['boundary_count']} | {row['review_action']} |"
            )
    return "\n".join(lines) + "\n"


def write_outputs(synthesis: dict[str, Any], json_output: Path, md_output: Path) -> None:
    json_output.parent.mkdir(parents=True, exist_ok=True)
    md_output.parent.mkdir(parents=True, exist_ok=True)
    json_output.write_text(json.dumps(synthesis, indent=2) + "\n")
    md_output.write_text(render_markdown(synthesis))


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-output", type=Path, default=DEFAULT_MD)
    parser.add_argument("--check", action="store_true", help="Validate without writing outputs.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    synthesis = build_synthesis(load_register(args.register))
    if args.check:
        print(
            "PASS cross-module synthesis: "
            f"{synthesis['theme_count']} themes, "
            f"{synthesis['core_consensus_count']} core consensus statements"
        )
        return 0
    write_outputs(synthesis, args.json_output, args.md_output)
    print(f"Wrote {args.json_output.relative_to(ROOT)}")
    print(f"Wrote {args.md_output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
