# Public TF union: agent lane curation v1

This artifact records the completed evidence review for the 16 priority TFs:

`TP53`, `JUN`, `FOS`, `MYC`, `STAT1`, `HIF1A`, `SP1`, `ETS1`, `RUNX1`,
`GATA3`, `CEBPB`, `IRF1`, `ATF2`, `EGR1`, `KLF4`, and `NFKB2`.

The five disjoint evidence lanes were merged only after pair-level validation:
human and mouse rows remain separate, every promoted row has a primary PMID,
cross-module promotions have an independent corroborating PMID, and duplicate
species/TF/target pairs are rejected. The frozen graph and canonical database
were not modified.

## Final disposition

| Artifact | Rows |
|---|---:|
| Distinct TF-pair dispositions | 9,094 |
| Promoted evidence rows | 37 |
| Exact-pair holds | 78 |
| Direction-conflict holds | 86 |
| Database-only/unverified rows | 8,893 |
| Cross-module review rows | 63 |
| Boundary-audit rows | 49 |
| Primary/corroborating/public provenance links | 10,829 |

All 37 promotions are staged to Module 22B, the TF-to-target/downstream
program layer. No row was promoted directly to Modules 20B, 21B, 23B, or 24B.
Rows with ligand, receptor, adhesion, ECM, or complement relevance remain in
the cross-module review queue; the evidence is not transferred to another
model solely because a paper is shared. Seven promoted rows also carry an
actual cross-module note and each has independent corroboration.

| TF | Pair rows | Promoted | Exact hold | Direction hold | Database-only |
|---|---:|---:|---:|---:|---:|
| TP53 | 1,088 | 5 | 3 | 19 | 1,061 |
| JUN | 394 | 3 | 5 | 12 | 374 |
| FOS | 883 | 2 | 1 | 5 | 875 |
| MYC | 843 | 1 | 5 | 5 | 832 |
| STAT1 | 766 | 3 | 3 | 7 | 753 |
| HIF1A | 433 | 4 | 4 | 6 | 419 |
| SP1 | 805 | 2 | 0 | 23 | 780 |
| ETS1 | 1,041 | 1 | 2 | 2 | 1,036 |
| RUNX1 | 294 | 1 | 0 | 2 | 291 |
| GATA3 | 945 | 1 | 3 | 0 | 941 |
| CEBPB | 143 | 0 | 3 | 1 | 139 |
| IRF1 | 137 | 4 | 10 | 1 | 122 |
| ATF2 | 73 | 2 | 10 | 0 | 61 |
| EGR1 | 1,134 | 3 | 21 | 1 | 1,109 |
| KLF4 | 70 | 3 | 6 | 0 | 61 |
| NFKB2 | 45 | 2 | 2 | 2 | 39 |

## Evidence safeguards

- Human and mouse assertions are adjudicated independently.
- A paper reused across several targets is retained as a shared primary only
  when the paper supports those exact targets; an independent paper was sought
  for at least one member of each reused evidence group.
- Target mismatches remain holds (for example, CEBPB→CSF3R/IL3/IL5 where the
  cited paper concerns CSF2RB).
- The retracted PMID 21398698 is excluded from TP53→DDR1 support.
- Cross-module observations are kept separate from TF-target promotion, with
  the exact pair, species, and module boundary recorded in the review queue.

## Output artifacts

- `data/processed/public_tf_union_v1/module_curation/agent_merged/priority_tf_agent_merged.tsv`
- `data/processed/public_tf_union_v1/module_curation/agent_merged/priority_tf_agent_boundary_audit.tsv`
- `data/processed/public_tf_union_v1/module_curation/agent_materialized/priority_tf_agent_promoted.tsv`
- `data/processed/public_tf_union_v1/module_curation/agent_materialized/priority_tf_agent_hold_queue.tsv`
- `data/processed/public_tf_union_v1/module_curation/agent_materialized/module_specific_review_queue.tsv`
- `data/processed/public_tf_union_v1/module_curation/agent_materialized/boundary_audit_queue.tsv`
- `data/processed/public_tf_union_v1/module_curation/agent_materialized/priority_tf_agent_source_links.tsv`
- `data/processed/public_tf_union_v1/module_curation/agent_materialized/priority_tf_agent_materialization_manifest.json`

The merge gate and the public TF union validator both pass for this artifact.
