# Module 21A batch 194 review summary

## Scope

This packet covers exactly 25 currently queued Module 20A CellChat-remaining
pairs: EREG/EGFR and ERBB4; FLRT2/UNC5D; FLRT3/ADGRL3 and UNC5B;
GDF1/GDF11/GDF2/GDF3; GDF5; GDF6; GDF7; IL-17A/AF/F; IL-38; and IL-20.
The review searched PubMed, PMC, publisher pages, and primary receptor or
pathway studies using exact ligand/receptor-complex names, aliases, species,
and assay terms. Module 20A ledgers, Module 21A ledgers, and the frozen LR
manifest were not edited.

## Disposition

- 25 rows written and queue-aligned.
- 11 `reviewed_relay_candidate` rows.
- 3 `reviewed_function_only` rows, primarily FLRT adhesion/guidance systems
  where extracellular binding and cellular output were shown without a defined
  intracellular relay.
- 11 `reviewed_unresolved` rows for exact composite receptor assemblies that
  were not isolated, despite family-level or comparator pathway evidence.
- 1 `no_evidence_boundary` layer: IL-38/IL1RL2-IL1RAP, where a recent primary
  binding and antagonism study did not support efficient activity in the tested
  IL-36R systems.
- All 25 `terminal_TF` values are literal `null`; no terminal TF was assigned
  without an explicit exact-pair endpoint.

## Evidence additions

Direct or receptor-dependent signaling support was retained for EREG/EGFR and
EREG/ERBB4, GDF2/ACVRL1-ACVR2A, the three submitted GDF5 complexes,
GDF6/BMPR1A-ACVR2A, IL-17A/AF/F with IL17RA-IL17RC, and IL-20 with the
IL22RA1-IL20RB type-II receptor. The FLRT rows retain direct extracellular
interaction and functional adhesion/guidance outputs as distinct from relay
evidence. GDF1 and GDF3 retain bounded Nodal/EGF-CFC comparator evidence, but
the submitted ACVR1C-containing complexes were not promoted to exact direct
edges.

## Limitations and unresolved boundaries

GDF6/BMPR1A-ACVR2B, GDF6/BMPR1B-ACVR2A, GDF6/BMPR1B-ACVR2B, and all four
GDF7 composites have pathway-family or type-II receptor comparator evidence,
but no exact ternary receptor assay or pair-selective perturbation sufficient
to distinguish the submitted complex. GDF11/TGFBR1-ACVR2A is similarly bounded
because the strongest exact comparator evidence used ACVR2B with ALK5. IL-17F
may also signal through IL17RC-only assemblies in some models, so the submitted
heteromeric receptor is not treated as the only possible branch.

## Validation

The TSV has the exact 13-column schema, 25 data rows, unique review IDs and
pairs, populated required fields, valid confidence values, and literal
`null` terminal-TF values. No SQL or ledger materialization was performed.
