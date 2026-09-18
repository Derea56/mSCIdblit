# mSCIdblit v1.9.49

This release adds ten selective primary-literature route annotations focused on
synaptic adhesion and receptor organization, with additional immune,
developmental and Wnt-related continuations. The evidence layer now retains
LRRTM4–GPC4–PTPσ, Netrin-G1–NGL1, Netrin-G2–NGL2, MDGA1–Neuroligin-2–gephyrin,
MDGA1–Neuroligin-2–collybistin, CD99–PILRα–CD8α,
P-cadherin–E-cadherin–KLRG1, E-cadherin–DSG2–DSC1, PD-L2–RGMb, and
WNT3A–GPC3–Unc5D continuations.

These annotations preserve the distinction between an existing ligand–receptor
input edge and the separately curated receptor-proximal primary evidence. The
routes remain bounded by species, cell context, assay type and the limitations
recorded for each source; they do not assert that the downstream primary assay
used the upstream ligand as its initiating stimulus. Transcription-factor and
terminal target-gene layers remain unassayed for this batch; no causal graph
edges or confidence scores are created.

- Route evidence: 17,211 → 17,221 records
- Graph topology: 11,952 nodes and 14,722 edges, unchanged
- Downstream queue candidates covered: 1,134 → 1,144
- Remaining downstream queue candidates: 2,187
- Remaining P1 candidates: 1,155
- Primary locators: PMID:25624497; PMID:25411505; PMID:19755106; PMID:35617401; PMID:16461340; PMID:19654330; PMID:27298358; PMID:24381170; PMID:36240740

All route annotations remain evidence-layer records and are not causal graph
edges. The corresponding bundle is
`mechanism_graph_module20_24_v2026_09_16_literature_expansion144`.
