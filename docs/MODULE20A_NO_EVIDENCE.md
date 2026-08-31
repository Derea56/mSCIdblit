# Module 20A no-evidence disposition

The low-confidence recovery work records a separate
`no_evidence_after_search` category at:

`work/module20_db_seed/evidence_escalation_router/module20a_no_evidence_registry.tsv`

This means that the exact ligand–receptor pair was searched in the recorded
literature passes and no qualifying direct primary evidence was recovered. It
is not a claim that the interaction is biologically impossible or absent.
Related family evidence, database presence, expression, pathway membership,
noncognate pairs, and unresolved receptor-complex notation remain in the row
limitations.

The canonical queue intentionally retains these rows at `low` for schema and
reproducibility compatibility. The separate registry is the revisit queue.
Revisit a row only when a new primary binding, receptor-activation,
receptor-dependent-function, or species-resolved receptor-complex source is
identified.

The companion
`work/module20_db_seed/evidence_escalation_router/module20a_non_ligand_receptor_registry.tsv`
contains candidates classified as non-ligand-receptor relationships or
wrong-pair annotations. Those rows are not counted as no-evidence rows.

The registries were refreshed by
`scripts/finalize_module20a_agent_batch007.py` after the disjoint agent search
batch and prior audited iterative worker records. No confidence tier, pair
index row, or `SignalingEdge` was changed by the no-evidence disposition alone.

## 2026-08-13 batch 008 update

Five workers completed `1,000` new exact-pair searches in packets of `200`.
The curator added `66` additional `no_evidence_after_search` rows and `63`
additional non-ligand-receptor rows. The cumulative registries now contain
`1,295` and `326` rows, respectively. The canonical queue remains low for
these dispositions so the registry, rather than queue status alone, is the
authoritative revisit/exclusion record.

The batch also produced `171` curator-approved medium decisions. Those rows
are source-backed but remain below high confidence and were not converted to
`SignalingEdge` records.

## 2026-08-13 residual batch 009 update

The final `46` unreviewed low-confidence rows were searched. `15` were added
to `no_evidence_after_search` and `6` to the non-ligand-receptor registry;
`13` source-backed candidates were approved at medium confidence. No
unreviewed low rows remain outside a search, manual-review, or registry
disposition.

## 2026-08-13 batches 010–011 final disposition

All remaining low rows outside terminal registries were reassessed in batch
010 (`772` rows) and final batch 011 (`457` unresolved rows). Exact
source-backed candidates were moved to medium; every other low row was
recorded as either `no_evidence_after_search` or non-ligand-receptor.
Boundary calls with family-only, fragment-mismatched, unresolved subunit,
complex-only, or contextual evidence were placed in no-evidence for the
submitted exact pair, with limitations preserved.

The canonical queue retains low for compatibility, but there are now `0` low
rows outside a terminal registry or approved evidence decision. The cumulative
registries contain `1,796` no-evidence rows and `450` non-LR rows.
