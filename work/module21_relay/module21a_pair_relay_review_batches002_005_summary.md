# Module 21A pair-relay review: batches 002–005

## Scope

Four read-only agents reviewed 76 exact, untouched Module20A priority-2
high/medium-confidence pairs:

- Batch002: 12 chemokine, GDF, CSF2, EGF and EREG rows
- Batch003: 25 early FGF rows
- Batch004: 22 late FGF rows
- Batch005: 17 GDNF, interferon, MIF, SLITRK and WNT5A rows

All 76 assigned review IDs were present exactly once in the frozen source
queue. The queue gap at `M20A-EXT-0076` was not silently included.

## Outcome

- 43 reviewed relay candidates
- 1 reviewed function-only case
- 2 reviewed scavenging-only cases
- 24 binding/activation-only cases; no downstream pathway edge promoted
- 4 unresolved cases
- 2 explicit no-downstream-evidence cases
- 46 reusable pathway candidates were created only for relay, functional, or
  scavenging evidence; binding-only and unresolved rows do not receive a
  reusable downstream pathway key
- 20 terminal TF activation candidates were handed to Module22A as candidates
  only; no TF-target program or phenotype claim was materialized

## Important boundaries

FGFR rows retain splice-isoform and endocrine-cofactor limitations. FGF15/19,
FGF21, FGF23 and Klotho-dependent branches are not interchangeable. IFNα9 and
IFNβ are unresolved at the exact subtype level where the primary evidence was
family-level. MIF composite receptor rows distinguish component binding from
direct binding to the full composite. SLITRK and ACKR rows are adhesion or
scavenging outputs, not automatically canonical kinase-to-TF pathways. WNT5A
FZD6 retains its beta-catenin and PCP contexts as non-interchangeable branches.

## Files changed/generated

- `module21a_all_pair_relay_coverage.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches002_005.tsv`

Module20A ledgers and the frozen release manifest were not modified. SQL was
not materialized.
