# Module 22B signed public TF promotion — batch 002

On 2026-09-03, we expanded the Module 22B working edge and evidence
registers with signed TF→target relationships from the Module 22 public TF
review queue. This batch uses exact simple TF and target symbols, excludes
self-loops and conflicting signed effects, and requires OmniPath/DoRothEA
level A or B evidence. Existing target-gene pairs were not duplicated when
already represented in the Module 22B register.

The batch added 3,589 target-gene edges: 3,172 high-confidence edges for
groups with at least one level A record and 417 medium-high edges supported by
level B records without level A support. Each edge has one corresponding
database-curated evidence row and an audit row. The resulting Module 22B
working registers contain 3,301 high-confidence edges, 547 medium-high edges,
3,706 target-gene edges, and 4,400 exportable edges.

These promotions represent general signed inferred regulatory capacity: the
source databases support an activating or repressing TF→target relationship,
but the DoRothEA level does not by itself prove direct DNA binding. The batch
does not require that the relationship was studied in spinal cord injury or a
spinal-cord sample, and it makes no claim that a particular ligand/receptor
route activates the TF in SCI. Species context, source registries, external
record keys, and available PMID references are retained in the evidence and
audit registers.

This is a working-register promotion only. The shared all-module generated
bundle and frozen SQL/database materialization were not regenerated, so other
module outputs—including Module 21—were not touched.

The source interpretation follows the repository’s public TF union
documentation:

- [PUBLIC_TF_UNION_EXPANSION_V1.md](PUBLIC_TF_UNION_EXPANSION_V1.md)
- [PUBLIC_TF_UNION_V1_RELEASE.md](PUBLIC_TF_UNION_V1_RELEASE.md)

