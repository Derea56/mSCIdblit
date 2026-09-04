"""Strict curation and context gating for the public-TF evidence layer.

The public-TF layer is an evidence inventory, not a route table.  This module
keeps that distinction executable: only rows in the explicit validated overlay
can receive a curation tier, and every promoted row remains conditional on an
explicit context mode.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Iterable, Mapping


CURATION_TIERS = (
    "candidate_only",
    "general_mouse_validated",
    "neural_context_validated",
    "sci_context_validated",
    "unresolved",
)
CONTEXT_MODES = ("general_mouse", "neural", "sci")
VALIDATED_EVIDENCE_TIERS = {
    "A_independent_literature_corroborated",
    "B_independent_literature_single_source",
}
VALID_CONTEXT_LEVELS = {
    "L0_no_context_evidence",
    "L1_non_CNS_context",
    "L2_CNS_context",
    "L3_spinal_cord_tissue_context",
    "L4_SCI_context",
}


def text(row: Mapping[str, object] | None, *keys: str) -> str:
    if row is None:
        return ""
    for key in keys:
        value = str(row.get(key, "") or "").strip()
        if value:
            return value
    return ""


def pair_key(regulator: str, target: str) -> tuple[str, str]:
    """Normalize case and whitespace only; do not infer aliases or direction."""

    return " ".join(regulator.split()).casefold(), " ".join(target.split()).casefold()


def join_values(values: Iterable[object]) -> str:
    return ";".join(str(value).strip() for value in values if str(value or "").strip())


def source_locator_status(row: Mapping[str, object]) -> str:
    has_citation = any(
        text(row, key)
        for key in (
            "primary_citation",
            "corroborating_citation",
            "additional_corroborating_citation",
            "primary_and_corroborating_citations",
        )
    )
    has_record = any(text(row, key) for key in ("source_record_id", "source_record_ids"))
    has_locator = any(text(row, key) for key in ("tflink_source_url", "tflink_raw_snapshot_path"))
    if has_citation and has_record:
        return "citation_and_source_record"
    if has_citation:
        return "citation_only"
    if has_record or has_locator:
        return "source_record_or_locator_only"
    return "missing_source_locator"


def validate_promotable_overlay_row(row: Mapping[str, object]) -> None:
    """Reject an overlay row that does not meet the strict promotion contract."""

    row_id = text(row, "layer_record_id") or "<missing layer_record_id>"
    errors: list[str] = []
    if text(row, "layer_membership") != "validated_mechanism_edge":
        errors.append("layer_membership is not validated_mechanism_edge")
    if text(row, "traversal_status") != "validated_edge_candidate":
        errors.append("traversal_status is not validated_edge_candidate")
    if text(row, "evidence_confidence_tier") not in VALIDATED_EVIDENCE_TIERS:
        errors.append("evidence tier is not independent literature evidence")
    if not text(row, "exact_pair_status").startswith("functional_direct_binding"):
        errors.append("exact-pair status is not a strict functional/direct-binding status")
    if text(row, "mechanism_evidence_type") != "direct_sequence_specific_tf_binding":
        errors.append("mechanism evidence type is not direct sequence-specific TF binding")
    if text(row, "species_scope") not in {"mouse", "both"}:
        errors.append("species scope is not mouse-compatible")
    if not text(row, "primary_citation"):
        errors.append("primary citation is missing")
    if not text(row, "validation_basis"):
        errors.append("validation basis is missing")
    if text(row, "validated_effect_polarity") not in {"activating", "inhibitory", "unknown"}:
        errors.append("validated effect direction is missing or invalid")
    context = text(row, "context_level_exact_pair")
    if context and context not in VALID_CONTEXT_LEVELS:
        errors.append(f"unknown context level: {context}")
    if errors:
        raise ValueError(f"Unsupported public-TF promotion for {row_id}: " + "; ".join(errors))


def validated_tier(row: Mapping[str, object]) -> str:
    validate_promotable_overlay_row(row)
    context = text(row, "context_level_exact_pair")
    if context == "L4_SCI_context":
        return "sci_context_validated"
    if context in {"L2_CNS_context", "L3_spinal_cord_tissue_context"}:
        return "neural_context_validated"
    return "general_mouse_validated"


def classify_row(row: Mapping[str, object], validated_by_id: Mapping[str, Mapping[str, object]]) -> str:
    row_id = text(row, "layer_record_id")
    if row_id in validated_by_id:
        return validated_tier(validated_by_id[row_id])
    if text(row, "evidence_confidence_tier") in {
        "C_tflink_source_table_only",
        "D_database_only_no_pair_evidence",
    }:
        return "candidate_only"
    return "unresolved"


def traversal_flags(status: str, row: Mapping[str, object]) -> dict[str, object]:
    if status not in CURATION_TIERS:
        raise ValueError(f"Unknown curation tier: {status}")
    validated = status in {
        "general_mouse_validated",
        "neural_context_validated",
        "sci_context_validated",
    }
    context = text(row, "context_level_exact_pair")
    general = validated and text(row, "species_scope") in {"mouse", "both"}
    neural = validated and context in {
        "L2_CNS_context",
        "L3_spinal_cord_tissue_context",
        "L4_SCI_context",
    }
    sci = validated and context == "L4_SCI_context"
    return {
        "traversal_eligibility": "context_gated" if validated else "not_traversable",
        "traversable_general_mouse": general,
        "traversable_neural": neural,
        "traversable_sci": sci,
    }


def eligible_for_mode(row: Mapping[str, object], mode: str) -> bool:
    if mode not in CONTEXT_MODES:
        raise ValueError(f"Unknown context mode: {mode}")
    field = {
        "general_mouse": "traversable_general_mouse",
        "neural": "traversable_neural",
        "sci": "traversable_sci",
    }[mode]
    return str(row.get(field, "")).casefold() == "true"


def duplicate_metadata(rows: Iterable[Mapping[str, object]]) -> dict[str, dict[tuple[str, str], object]]:
    by_pair: defaultdict[tuple[str, str], list[Mapping[str, object]]] = defaultdict(list)
    for row in rows:
        by_pair[pair_key(text(row, "regulator_symbol"), text(row, "target_symbol"))].append(row)
    return {
        "row_counts": {key: len(value) for key, value in by_pair.items()},
        "module_counts": {
            key: len({module for row in value for module in text(row, "module").split(";") if module})
            for key, value in by_pair.items()
        },
    }


def graph_indexes(
    nodes: Iterable[Mapping[str, object]], edges: Iterable[Mapping[str, object]]
) -> tuple[dict[tuple[str, str], list[str]], dict[str, list[str]]]:
    node_by_id = {text(row, "node_id"): row for row in nodes}
    symbols: defaultdict[str, list[str]] = defaultdict(list)
    for row in node_by_id.values():
        symbol = text(row, "gene_symbol", "canonical_name")
        if symbol:
            symbols[symbol.casefold()].append(text(row, "node_id"))
    pairs: defaultdict[tuple[str, str], list[str]] = defaultdict(list)
    for row in edges:
        source = node_by_id.get(text(row, "source_node_id"))
        target = node_by_id.get(text(row, "target_node_id"))
        if not source or not target:
            continue
        source_symbol = text(source, "gene_symbol", "canonical_name")
        target_symbol = text(target, "gene_symbol", "canonical_name")
        if source_symbol and target_symbol:
            pairs[pair_key(source_symbol, target_symbol)].append(text(row, "edge_id"))
    return dict(pairs), dict(symbols)


def build_ledger_rows(
    candidate_rows: list[Mapping[str, object]],
    validated_rows: list[Mapping[str, object]],
    *,
    active_pair_edges: Mapping[tuple[str, str], list[str]] | None = None,
    active_node_symbols: Mapping[str, list[str]] | None = None,
) -> list[dict[str, object]]:
    validated_by_id = {text(row, "layer_record_id"): row for row in validated_rows}
    duplicates = duplicate_metadata(candidate_rows)
    active_pair_edges = active_pair_edges or {}
    active_node_symbols = active_node_symbols or {}
    ledger: list[dict[str, object]] = []
    for source in candidate_rows:
        source_id = text(source, "layer_record_id")
        overlay = validated_by_id.get(source_id)
        status = classify_row(source, validated_by_id)
        regulator = text(source, "raw_tf_symbol", "regulator_symbol")
        target = text(source, "target_symbol")
        graph_pair = pair_key(regulator, target)
        display_pair = pair_key(text(source, "regulator_symbol"), target)
        graph_edges = active_pair_edges.get(graph_pair, [])
        regulator_in_graph = graph_pair[0] in active_node_symbols
        target_in_graph = graph_pair[1] in active_node_symbols
        source_text = " ".join(
            text(source, key)
            for key in (
                "source_record_id",
                "source_record_ids",
                "primary_citation",
                "corroborating_citation",
                "tflink_source_url",
            )
        )
        validation_basis = text(overlay, "validation_basis") if overlay else ""
        citation = join_values(
            (
                text(overlay, "primary_citation") if overlay else "",
                text(source, "primary_citation"),
                text(source, "corroborating_citation"),
                text(source, "additional_corroborating_citation"),
                text(source, "source_record_ids"),
                text(source, "source_record_id"),
                text(source, "tflink_source_url"),
                text(source, "tflink_raw_snapshot_path"),
            )
        ) or "unknown"
        context_row = overlay or source
        flags = traversal_flags(status, context_row)
        tissue_context = text(
            source,
            "tissue_cell_context",
            "tissue_context",
            "cell_type_context",
            "tissue",
            "cell_type",
        ) or "unknown_not_structured_in_candidate_layer"
        limitations = join_values(
            (
                text(overlay, "limitations") if overlay else "",
                text(source, "near_match_exclusions"),
                "candidate-only rows are non-traversable" if status == "candidate_only" else "",
                "not in validated overlay; retained unresolved pending exact-pair adjudication"
                if status == "unresolved"
                else "",
            )
        ) or "unknown"
        ledger.append(
            {
                "source_row_id": source_id or "unknown",
                "source_layer_membership": text(source, "layer_membership") or "unknown",
                "source_traversal_status": text(source, "traversal_status") or "unknown",
                "regulator": text(source, "regulator_symbol") or "unknown",
                "raw_regulator": text(source, "raw_tf_symbol") or "unknown",
                "target": target or "unknown",
                "module": text(source, "module") or "unknown",
                "module_route": text(source, "module_route") or "unknown",
                "target_graph_modules": text(source, "target_graph_modules") or "unknown",
                "curation_status": status,
                **flags,
                "evidence_basis": join_values(
                    (
                        validation_basis,
                        text(source, "decision_basis"),
                        text(source, "evidence_tier_basis"),
                        text(source, "exact_pair_status"),
                        text(source, "mechanism_evidence_type"),
                    )
                )
                or "unknown",
                "evidence_confidence_tier": text(source, "evidence_confidence_tier") or "unknown",
                "evidence_type": text(source, "mechanism_evidence_type") or "unknown",
                "assay_type": text(source, "tflink_detection_method") or "unknown",
                "independent_literature_support_status": text(
                    source, "independent_literature_support_status"
                )
                or "unknown",
                "independent_literature_source_count": text(
                    source, "independent_literature_source_count"
                )
                or "unknown",
                "exact_pair_status": text(source, "exact_pair_status") or "unknown",
                "binding_or_association_status": text(source, "binding_or_association_status") or "unknown",
                "species": text(source, "species_scope") or "unknown",
                "tissue_cell_context": tissue_context,
                "context_level_regulator": text(source, "context_level_regulator") or "unknown",
                "context_level_target": text(source, "context_level_target") or "unknown",
                "context_level_exact_pair": text(context_row, "context_level_exact_pair") or "unknown",
                "sci_context": text(source, "sci_context_status") or "unknown",
                "context_evidence_scope": text(source, "context_evidence_scope") or "unknown",
                "context_evidence_basis": text(source, "context_evidence_basis") or "unknown",
                "context_promotion_lane": text(source, "context_promotion_lane") or "unknown",
                "effect_direction": text(overlay, "validated_effect_polarity")
                or text(source, "effect_polarity")
                or "unknown",
                "confidence": text(overlay, "promotion_confidence")
                or text(source, "promotion_confidence")
                or text(source, "evidence_confidence_tier")
                or "unknown",
                "source_locator_status": source_locator_status(source),
                "citation_provenance": citation,
                "limitations": limitations,
                "reviewer_notes": text(source, "review_notes") or "unknown",
                "source_materialization_status": text(source, "materialization_status") or "unknown",
                "source_module_materialization_allowed": text(
                    source, "module_materialization_allowed"
                )
                or "unknown",
                "source_canonical_materialization_allowed": text(
                    source, "canonical_materialization_allowed"
                )
                or "unknown",
                "source_screening_decision": text(source, "screening_decision") or "unknown",
                "source_registry": text(source, "source_registry") or "unknown",
                "source_record_id": text(source, "source_record_id") or "unknown",
                "source_record_ids": text(source, "source_record_ids") or "unknown",
                "active_graph_pair_status": "exact_pair_in_active_graph"
                if graph_edges
                else "regulator_and_target_nodes_present"
                if regulator_in_graph and target_in_graph
                else "not_found_in_active_graph",
                "active_graph_edge_ids": join_values(graph_edges) or "unknown",
                "active_graph_node_resolution": "both_endpoint_symbols_present"
                if regulator_in_graph and target_in_graph
                else "one_endpoint_symbol_present"
                if regulator_in_graph or target_in_graph
                else "no_matching_active_graph_node_symbol",
                "duplicate_pair_row_count": duplicates["row_counts"].get(display_pair, 1),
                "duplicate_module_count": duplicates["module_counts"].get(display_pair, 1),
                "method_label_adjudication_status": "queue_not_created_dependency_metadata_required"
                if status in {
                    "general_mouse_validated",
                    "neural_context_validated",
                    "sci_context_validated",
                }
                else "not_eligible_without_independent_evidence_and_dependency_metadata",
                "source_text_for_validation": source_text or "unknown",
            }
        )
    return ledger


def summarize_ledger(ledger: Iterable[Mapping[str, object]]) -> dict[str, object]:
    rows = list(ledger)
    summary: dict[str, object] = {
        "rows": len(rows),
        "curation_status": dict(Counter(str(row.get("curation_status", "unknown")) for row in rows)),
        "source_locator_status": dict(Counter(str(row.get("source_locator_status", "unknown")) for row in rows)),
        "active_graph_pair_status": dict(
            Counter(str(row.get("active_graph_pair_status", "unknown")) for row in rows)
        ),
        "context_level_exact_pair": dict(
            Counter(str(row.get("context_level_exact_pair", "unknown")) for row in rows)
        ),
        "regulator_target": {},
        "context_modes": {},
    }
    pair_counts = Counter(
        pair_key(str(row.get("regulator", "")), str(row.get("target", ""))) for row in rows
    )
    summary["regulator_target"] = {
        f"{regulator}->{target}": count
        for (regulator, target), count in sorted(
            pair_counts.items(), key=lambda item: (-item[1], item[0])
        )
    }
    for mode, field in (
        ("general_mouse", "traversable_general_mouse"),
        ("neural", "traversable_neural"),
        ("sci", "traversable_sci"),
    ):
        eligible = [row for row in rows if eligible_for_mode(row, mode)]
        pairs = {pair_key(str(row.get("regulator", "")), str(row.get("target", ""))) for row in eligible}
        summary["context_modes"][mode] = {"row_count": len(eligible), "unique_pair_count": len(pairs)}
    return summary
