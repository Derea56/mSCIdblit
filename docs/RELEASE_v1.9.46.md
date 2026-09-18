# mSCIdblit v1.9.46

This release adds ten selective primary-literature route annotations focused on
receptor-proximal signaling continuations for mSCS plausibility analysis. The
evidence layer now retains supported continuations for Mincle/MCL, MSR1/MERTK,
RAMP2/GCGR, GPR179/mGluR6 and R7-RGS complexes, p75NTR/NgR1, CALR/LRP1, and
BAI1/NgR-family partners.

The annotations preserve important scope limits: accessory-complex and
modulation relationships are not treated as direct ligand occupancy, and the
p75NTR/NgR1 and BAI1/NgR-family records do not assert ligand-specific
activation of the downstream receptor. Transcription-factor and terminal
target-gene layers remain unassayed for this batch; no causal graph edges or
confidence scores are created.

- Route evidence: 17,181 → 17,191 records
- Graph topology: 11,952 nodes and 14,722 edges, unchanged
- Downstream queue candidates covered: 1,104 → 1,114
- Remaining downstream queue candidates: 2,217
- Remaining P1 candidates: 1,185
- Primary locators: PMID:23921530; PMID:18511575; PMID:28586439; PMID:24114537; PMID:22689652; PMID:12422217; PMID:22889139; PMID:31781126; PMID:34758294

All route annotations remain evidence-layer records and are not causal graph
edges. The corresponding bundle is
`mechanism_graph_module20_24_v2026_09_16_literature_expansion141`.
