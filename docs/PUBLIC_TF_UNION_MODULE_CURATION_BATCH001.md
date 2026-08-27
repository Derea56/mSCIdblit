# Public TF union Module 20–24 curation: priority batch 001

This batch is the first pair-level evidence adjudication pass over the public
TRRUST and OmniPath/DoRothEA TF union. It is staged evidence curation only:
the frozen `mSCIdblit-v1.0.0` mechanism graph, the frozen Module 20–24 bundle,
and the local PostgreSQL database were not modified.

## Boundary decision

Public TF→target/regulon assertions are assigned to Module 22B. A shared PMID
with a Module 20B, 21B, 23B, or 24B record is an overlap-review flag, not a new
receptor, intracellular relay, ECM/adhesion, or complement edge. The batch
therefore has no promotions to Modules 20B, 21B, 23B, or 24B.

The staged Module 22B records retain the cross-module overlap and explicitly
state that the existing module evidence was not reused. In particular:

- HIF1A→VEGFA is supported in Module 22B by independent HIF-1/VEGF primary
  literature; the shared Module 20B SCUBE2–KDR citation is not treated as
  evidence for the TF→target pair.
- TP53→DDR1 is supported in Module 22B by PMID 12628922. PMID 21398698,
  which appears in the Module 23B collagen/DDR1 overlap, is retracted and is
  excluded from support.
- SP1→C4A/C4B remains a Module 22B promoter record. It does not create a
  Module 24B complement signaling edge.

## Batch counts

| Disposition | Rows |
|---|---:|
| Pair-level decisions | 49 |
| Evidence-promoted to Module 22B staging | 28 |
| Held for exact-pair review or cross-module reuse | 21 |
| Source/provenance links | 147 |

The 28 promoted rows are still subject to the entity-role gate before any
canonical graph materialization. This is necessary because most newly added
public TFs are not present as frozen TF-role nodes, and several targets lack an
explicit frozen target-gene role.

## Corroboration policy

Shared primary papers were kept pair-scoped. Independent corroboration was
added for at least one member of the main reused-paper groups:

- TP53: BCL2 (PMID 11313951) and MCL1 (PMID 18208354).
- JUN/FOS: JUN→MMP1 (PMID 9178763), FOS→MMP1 (PMID 8785586), and FOS→MMP3
  (PMID 8039503).
- STAT1: STAT1→CCL3 (PMID 38730482).
- HIF1A: HIF1A→VEGFA (PMIDs 8756616 and 15735682), with a mouse Vegfa
  promoter corroboration/primary record at PMID 28686658.

Where an exact second paper was not located, the staged row says so and is
not silently upgraded. The CEBPB rows are held because PMID 10453008 concerns
CSF2RB, not CSF3R, IL3, or IL5. STAT1→CCR1 is held because PMID 16628196
supports CCL3, IRF7, and TLR3 responses but not the CCR1 target claim.

## Files

- `data/processed/public_tf_union_v1/module_curation/batch001/priority_curation_batch001_decisions.tsv`
- `data/processed/public_tf_union_v1/module_curation/batch001/priority_curation_batch001_promoted_22B.tsv`
- `data/processed/public_tf_union_v1/module_curation/batch001/priority_curation_batch001_hold_queue.tsv`
- `data/processed/public_tf_union_v1/module_curation/batch001/priority_curation_batch001_source_links.tsv`
- `data/processed/public_tf_union_v1/module_curation/batch001/priority_curation_batch001_manifest.json`
- `scripts/promote_public_tf_union_module_curation.py`

The script is deterministic and file-based. It does not connect to PostgreSQL,
insert `SignalingEdge` rows, or regenerate a release bundle.
