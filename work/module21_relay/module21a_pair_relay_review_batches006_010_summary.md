# Module 21A pair-relay review: batches 006–010

## Scope

Five read-only agents reviewed 125 exact priority-6 pairs from the frozen
Module20A queue:

- Batch006: collagen I/II, agrin, contactin, Notch, DMP1, EPGN and FN
- Batch007: collagen IV/VI, COMP, DLL3/DLL4, DMP1, CD23 and FN
- Batch008: fibronectin, perlecan, IBSP, laminin 1/2/3
- Batch009: laminin 3/4/5 and laminin-chain receptor rows
- Batch010: laminin, NCAM-FGFR1, netrin, Reelin and thrombospondin

All 125 assigned IDs matched the queue exactly once. Batch labels were treated
as external metadata; explicit IDs were authoritative when labels conflicted
with repository manifests.

## Outcome

- 86 reviewed relay candidates
- 28 binding-only rows retained without downstream pathway promotion
- 11 unresolved rows retained explicitly
- 81 reusable pathway candidates created for relay/function evidence
- 6 provisional terminal TF activation candidates were handed to Module22A; only pair-attributable measured
  readouts were retained as provisional handoffs where appropriate

Native collagen, laminin, thrombospondin and perlecan evidence was not relabeled
as isolated-chain binding. Reuse keys retain the tested heterotrimer, isoform,
integrin splice variant, glycosylation, cell model and assay context.

## Important boundaries

COL1A1/COL1A2/COL2A1, COL4A*, COL6A* and LAMA/LAMB/LAMC rows frequently derive
from native multichain matrix preparations. Those records remain distinct from
chain-isolated direct molecular edges. DLL3 cis-inhibition was not promoted to
canonical trans-Notch activation. Netrin receptor branches remain distinct
between DCC, DSCAM and UNC5 complexes. THBS1/2 syndecan evidence is retained as
glycan/proximal evidence rather than core-protein binding. The strongest TF-like
readouts were c-Jun, NF-kB p65 and TAZ/TEAD in context-specific models; target
programs remain Module22A work.

## Files changed/generated

- `module21a_all_pair_relay_coverage.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches006_010.tsv`

Module20A ledgers and the frozen release manifest were not modified. SQL was
not materialized.
