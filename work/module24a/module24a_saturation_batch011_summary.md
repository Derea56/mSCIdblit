# Module 24A saturation tranche 011

This tranche closed matrix dispositions for existing, validated PGE2 and S1P
receptor branches without creating duplicate edges or evidence records.

## Promotions

- `M24A-Q0064` is now `REVIEWED_SUPPORTED_WITH_PAIR_LIMIT`: EP2
  receptor-proximal SCI pain evidence and EP4 spinal inflammatory-culture
  evidence are retained as distinct branches.
- `M24A-Q0066` is now `REVIEWED_SUPPORTED_WITH_PAIR_LIMIT`: S1PR1 spinal
  pain, S1PR3 traumatic-SCI inflammation, and S1PR2 contusive-SCI ferroptosis
  branches are retained separately.

## Limits

- No duplicate PGE2 or S1P edges were created.
- Purified ligand-receptor binding, contusion-specific EP4 causality,
  endogenous S1P source attribution, and complete cell-specific necessity
  remain unresolved.
- The existing EP2, EP4, S1PR1, S1PR2, and S1PR3 evidence records remain in
  their original evidence layers.

## Validation disposition

- No edge or evidence counts changed: 151 edges, 200 evidence records, 169
  associations, 189 matrix rows, and 31 explicit boundaries.
- PostgreSQL staging was reloaded and matrix assertions passed.

## Primary source anchors

The disposition uses the existing primary records for PGE2/EP2 SCI pain
([PMID 17329433](https://pubmed.ncbi.nlm.nih.gov/17329433/)), EP4 spinal
inflammatory feedback, S1PR1 spinal pain, S1PR3 SCI inflammation, and S1PR2
contusive-SCI ferroptosis. These records support receptor-proximal/pathway
branches but do not establish purified binding.
