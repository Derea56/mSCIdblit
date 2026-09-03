# Module 22B low-confidence upgrade batch 001 — 2026-09-02

This batch re-adjudicates exact low-tier Module 22B rows against the
repository's primary-source Phase-2 review records. It promotes only
bounded direct TF/program records to high and exact receptor/pathway or
functional records to medium. It does not create canonical SQL rows.

## Result

- Rows upgraded: 13
- High edge upgrades: 3
- Medium edge upgrades: 10
- Exact low edges before: 5,069
- Exact low edges after: 5,056
- High edges after: 92
- Medium edges after: 433
- Exportable edges after: 723
- Canonical SQL materialization: false

## Boundaries

High rows are direct TF occupancy/target or defined target-program
records in the cited comparator systems. Medium rows are usable
exact-pair receptor/pathway or functional records but are not direct
TF-target evidence. Receptor-complex substitutions, model transfer,
species transfer, and SCI transfer remain explicitly bounded.

Rows with explicit negative evidence, wrong-direction or wrong-pair
evidence, disputed binding, non-native constructs, or no terminal TF
remain low and were not force-promoted.

## Reproduction

- Generator: `scripts/promote_module22b_low_confidence_batch001.py`
- Audit ledger: `work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch001.tsv`
