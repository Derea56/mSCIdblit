# Module 21A all-pair relay review — batch 001

Date: 2026-08-14

## Scope

Four independent read-only reviews covered 95 exact Module 20A pairs from the
highest-priority portion of the frozen 5,906-pair queue. The assigned ranges
were checked against the source queue; the BMP5/BMP6/BMP7/BMP8 batch contained
23 rows, and the BTC/ACKR/complement batch contained 22 rows.

## Triage outcome

- 47 pair rows: reviewed relay candidate
- 16 pair rows: reviewed no downstream evidence
- 16 pair rows: reviewed scavenging/transport only
- 11 pair rows: reviewed binding-only or structural-only evidence
- 3 pair rows: reviewed functional/adhesion-only evidence
- 2 pair rows: unresolved receptor/pathway assignment
- 30 reusable pathway/evidence candidates entered once in the reuse registry
- 42 terminal TF candidates handed to Module 22A as candidates only

The TF candidates are not TF-target-program claims. They require separate
Module 22A validation. The strongest measured TF activation in this batch is
BDNF–NTRK2-associated CREB phosphorylation. Many BMP and Activin rows retain
SMAD candidates at pathway-terminal resolution without assigning target
programs.

## Important boundaries

- ACKR1/ACKR2/ACKR4 rows are primarily binding, scavenging, transport, or
  chemokine-availability contexts; they were not converted into canonical
  GPCR-to-TF pathways.
- BMP receptor-component binding was not promoted to downstream signaling
  unless a matched cellular receptor-use or pSMAD assay existed.
- GDF15–TGFBR2 remains unresolved because GDF15–GFRAL/RET and TGFBR2-related
  evidence were not shown to be the same receptor mechanism.
- C3–CR3/CR4 evidence concerns processed iC3b binding, not intact C3-driven
  downstream TF signaling.
- Reused pathways preserve pair-specific rows and limitations; deduplication
  does not merge ligand identity, receptor complex, model, or TF outcome.

## Audit files

- `module21a_pair_relay_review_batch001.tsv`
- `module21a_pair_relay_evidence_register.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`

No Module20A ledger, classification, or frozen manifest was modified.
