# Module 22B signed TRRUST promotion — batch 003

On 2026-09-03, we completed another pass over the Module 22 public TF review
queue and added 552 exact, simple-symbol TF→target relationships from TRRUST
to the Module 22B working registers. The selection required a single signed
effect (activating or repressing), at least one TRRUST source record, an
explicit PMID, no self-loop, no conflicting signed effect in the combined
queue group, and no existing target-gene edge for the pair.

The batch contains 418 activating and 134 repressing relationships, covering
291 mouse and 261 human-scoped records. Every new relationship is marked high
confidence for the general signed regulatory claim and has a matching
database-curated evidence row plus audit row. After this pass, the working
registers contain 3,853 high-confidence edges, 547 medium-high edges, 4,258
target-gene edges, and 4,952 exportable edges.

TRRUST provides literature-curated signed interactions and PMID provenance,
but its relationship modality remains unresolved in the public TF source
release. Therefore these edges record general regulatory support and do not
claim direct DNA binding, a particular molecular mechanism, or ligand/receptor
activation of the TF in SCI. Species and source-record provenance are retained
in the evidence and audit registers.

This is a working-register promotion only. The shared all-module generated
bundle and frozen SQL/database materialization were not regenerated, so other
module outputs—including Module 21—were not touched.

