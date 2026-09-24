# mSCIdblit release v1.9.242

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-all-ligand-output-linked-365`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion365/`

## TGFB1 route curation

This release adds four bounded TGFB1 evidence routes:

- TGFB1 → TGFBR1:TGFBR2 → SMAD3 → SMAD3/SMAD4 → COL1A2 expression
- TGFB1 → TGFBR1:TGFBR2 → SMAD3 → SMAD3/SMAD4 → CTGF/CCN2 expression
- TGFB1 → TGFBR1:TGFBR2 → SMAD3 → SMAD3/SMAD4 → JUN expression
- TGFB1 → TGFBR1:TGFBR2 → SMAD3 → SMAD3/SMAD4 → SERPINE1/PAI-1 expression

The routes link existing receptor, SMAD signaling, and target-promoter records.
The TGFBR receptor-complex alias and the missing SMAD3-to-SMAD3/4 complex handoff
are retained explicitly. Where an existing TGFB1 target-output edge is present
(COL1A2 and CTGF/CCN2), it is linked as an output observation; no new graph edge
is created. All routes remain evidence-only and non-causal.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 334,228 |
| Literature-expansion annotations | 560 |
| Full-sequence curation candidates | 7,742 |
| Normalized route nodes | 1,293,192 |
| Normalized route edges | 1,276,042 |

The release validator passed with zero errors. Primary locators include
PMID:20207738, PMID:9311995, PMID:9886263, PMID:18314002, PMID:10022869,
and PMID:10092624.
