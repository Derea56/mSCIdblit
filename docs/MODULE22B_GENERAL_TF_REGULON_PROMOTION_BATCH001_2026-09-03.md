# Module 22B general TF/regulon promotion batch 001

**Date:** 2026-09-03  
**Scope:** standalone general TF-to-target regulation  
**Status:** materialized in the Module 22B working registers; frozen SQL/database materialization was not performed

This batch adds 37 exact source-verified TF-to-target relationships to the
Module 22B register. The promotion claim is that the named TF regulates the
named target in the recorded species and comparator context. SCI or spinal-cord
validation is not required for this standalone relationship, and its absence
is retained as a limitation rather than used as an exclusion.

The batch does not infer that any Module 22A ligand/receptor handoff activates
the TF in SCI. Upstream signaling and downstream TF/regulon membership remain
separate evidence layers. Cooperative promoter records are described as
cooperative rather than as TF-only mechanisms, and source-reported direction
conflicts remain visible in the evidence provenance.

## Results

| Measure | Result |
|---|---:|
| Source-verified input rows | 37 |
| General TF/regulon edges added | 37 |
| New high-confidence edges | 37 |
| Target-gene edges after batch | 117 |
| High-confidence edges after batch | 129 |
| Exportable Module 22B edges after batch | 811 |
| Upstream SCI activation inferred | No |
| Frozen SQL/database materialization | No |

The source rows are the previously materialized `priority_tf_agent_promoted`
records from the public TF curation. They include exact primary-reference
verification for direct binding, promoter, or perturbation-supported
relationships. The register-level audit is
`work/module22b_tf_regulon_promotion_audit/module22b_general_tf_regulon_promotion_batch001.tsv`.

The added edges retain source species, comparator cell/model, primary and
corroborating PMIDs, public source-record keys, direction, and explicit
limitations. They are therefore usable as general TF/regulon evidence without
being presented as SCI-specific pathway activation.
