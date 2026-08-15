# Module 21A Batch 171 review summary

Batch 171 is a bounded review of the 25 authoritative queue rows supplied for
filtered queue ordinals 3726-3750. The canonical IDs and pair labels were
checked against `work/module21_relay/module21a_all_pair_relay_coverage.tsv`
and the Module 20A external review queue. The requested Module 20A row
`M20A-EXT-3524 Wnt7a Reck` was not included because it was not in the supplied
25-row batch.

## Output contract

- Raw output: `module21a_batch171_review.tsv`
- Exact columns: `review_id`, `pair`, `status`, `stable_citations`, `species`,
  `cell_type_model`, `assay_or_perturbation`, `relation_type`,
  `evidence_layer`, `pathway_branch`, `confidence`, `limitations`,
  `terminal_TF`
- Exact data rows: 25
- Every row has a populated limitations field.
- `terminal_TF` is literal `null` unless a primary study measured a defensible
  terminal TF output. Batch 171 assigns `JUN` for BDNF/p75NTR and
  `SMAD1;SMAD5;SMAD9` for the BMP8A receptor-combination rows with direct
  p-SMAD1/5/8 pathway readouts.

## Evidence posture

| Review posture | Rows |
|---|---:|
| `reviewed_relay_candidate` | 5 |
| `reviewed_function_only` | 10 |
| `reviewed_unresolved` | 1 |
| `no_evidence_boundary` | 9 |
| Total | 25 |

The strongest bounded relay candidates are ZP3–CHRNA7 and ZP3–EGFR in mouse
sperm, ANXA2–TLR2 in primary receptor/mesothelial models, BDNF/proBDNF–p75NTR
with the required ligand-form/co-receptor caveat, and ANGPT1–integrin-beta-1
context with alpha5beta1-complex and FAK/PI3K-AKT support. BMP3–ACVR2B and
selected BMP8A receptor-combination rows are retained as receptor-dependent
functional evidence, not as purified binding claims.

## Layer boundaries

Binding or activation claims are separated from receptor-proximal relay and
downstream function in `evidence_layer`. Pathway/function readouts were not
used to infer direct interaction. In particular:

- WNT5B–FZD9_LRP6, WNT5B–KLRG2, WNT7A–LDLR, ZP3–MERTK, APP–LRP6, and the
  unresolved BMP composites remain explicit no-evidence boundaries.
- ANGPTL2–TLR4 is retained only as a TLR4-associated inflammatory feedback
  context; LPS/TLR4 perturbation does not establish ANGPTL2 as a direct TLR4
  ligand.
- WNT7B–TMED5 is an intracellular trafficking/pathway association from a
  source that was retracted in 2025; it is not promoted to an extracellular
  ligand-receptor relay.
- ALCAM–NRP1 is a trans-heterophilic adhesion/substrate relationship, not a
  secreted ligand-receptor edge.
- Composite BMP receptor labels are recorded as component-wise functional
  compatibility when supported. A component-wise receptor requirement is not
  treated as proof of one stable ligand-bound heterocomplex.

## Scope limitations

Most positive rows are comparator systems (sperm, neuronal, tumor,
mesothelial, bone, or adipocyte models), not SCI receiver astrocytes. No row
should be assigned an SCI-specific relay weight without a matched receiver
model. No shared registers, Module 20A files, or materialized SQL were
modified, and no commit was made.
