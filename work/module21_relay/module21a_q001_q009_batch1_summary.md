# Module 21A Q001–Q009 bounded extraction batch

Date: 2026-08-14

## Scope and disposition

Q001 through Q009 were reviewed in priority order against the existing Module 21A saturation registers. The batch adds 37 main-register edges (`M21A-E066`–`M21A-E102`), 26 grouped evidence records (`M21A-SAT-EVID-015`–`040`), 28 perturbation records (`M21A-SAT-P018`–`P045`), and one evidence-layer row for each added edge. The separate Q001 IL-6/gp130 seed packet was preserved unchanged.

The Q001–Q009 batch itself brought the main saturation registers to 94 edges, 40 grouped evidence records, and 45 perturbation records. Of the 37 added edges, 25 are high-confidence and 12 medium-confidence; 28 have medium export priority and 9 are low-priority contextual or comparator branches. The subsequent targeted second passes are recorded separately and bring the main registers to 102 edges, 46 evidence records, and 51 perturbation records. No SQL signaling rows were materialized.

## Evidence-layer accounting

- Receptor-proximal relay: 18 edges, including receptor-complex, adaptor, kinase, and noncanonical relay observations.
- Downstream pathway or cellular function: 19 edges, including transcriptional, cellular, tissue, and organismal outputs.
- No new Module 20A ligand–receptor ledger rows were created or altered.
- Direct molecular edges are retained only where the cited experiment supports a molecular association or recruitment. PDGFR–SRC is explicitly retained as a receptor-proximal pathway-complex observation because the cited source does not establish a direct physical interaction.

## Queue disposition

All nine queue items are marked `completed_bounded`. This means the requested first-pass extraction and bounded search were completed; it does not mean every SCI receiver-state branch is resolved.

Resolved at bounded comparator level:

- Q001: CNTFRα/gp130/LIFR and CNTFRα/gp130/OSMR receptor-complex alternatives; SCI astrocyte-specific weighting remains open.
- Q005: comparator ligand-biased CCR4/CCR7/CXCR3A/B signaling; no SCI receiver-state map was found.

Partially resolved or unresolved:

- Q002: IFN-lambda receptor-proximal JAK/TYK and astrocyte IRF/ISG evidence is bounded to non-SCI human astrocyte systems.
- Q003: TNFR2 adaptor, alternative NF-κB, astrocyte CXCL12, and contusive-SCI functional evidence are present, but astrocyte-specific death-versus-survival branch ordering remains open.
- Q004: IL1R2 decoy-complex evidence is distinct from the IL1R1–MyD88 SCI astrocyte branch; direct IL1R2 SCI astrocyte evidence remains open.
- Q006: TGF/BMP noncanonical receptor and pathway evidence is present, but direct contusion-SCI receiver-cell branch validation remains open.
- Q007: PDGFR/FGF comparator and SCI astrocyte evidence are present; FGFR paralog/adaptor and VEGFR-specific SCI branches remain open.
- Q008: WNT5A–ROR2/JNK and SCI neural output evidence is present; receptor-resolved injured-glia branch evidence remains open.
- Q009: Jagged1–Notch1 astrocyte and SCI evidence plus DLL4/DLL1 signal-strength comparison are present; comprehensive Notch paralog glial branch resolution remains open.

The detailed unresolved cases are recorded in `module21a_unresolved_register.tsv`, with stable source identifiers and follow-up boundaries.

## Second-pass update

The targeted second pass added one validated Q001 receptor-context edge (`M21A-E103`) from PMID 8075814. This promotes the CNTFR astrocyte case from unresolved to partially resolved, while preserving the limitation that the study does not distinguish the CNTFRα/gp130/LIFR and CNTFRα/gp130/OSMR configurations in contusive SCI. The TNFR2 search added contusion-SCI GFAP co-localization context (PMCID PMC9220050) but no astrocyte-specific intracellular perturbation edge. The IL1R2 search did not identify direct IL1R2 astrocyte SCI evidence; the existing IL1R2-versus-IL1R1 boundary remains explicit.

## Validation completed

- Main edge IDs, evidence IDs, perturbation IDs, layer-row edge IDs, and unresolved case IDs are unique.
- Edge keys are unique across the main saturation register and the separate Q001 seed register.
- Every main-register edge has supporting evidence; every added edge has a layer assignment and supporting evidence.
- Direct molecular, receptor-complex/pathway, and functional-output classes remain distinct in the evidence-layer register.
- Receptor-complex and pathway nodes were retained as explicit nodes; no pathway-level or functional record was promoted to a direct molecular interaction.
- The frozen Module 20A manifest remains byte-identical with SHA-256 `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Files changed

- `work/module21_relay/module21a_saturation_edge_register.tsv`
- `work/module21_relay/module21a_saturation_evidence_register.tsv`
- `work/module21_relay/module21a_saturation_perturbation_register.tsv`
- `work/module21_relay/module21a_evidence_layer_register.tsv`
- `work/module21_relay/module21a_unresolved_register.tsv`
- `work/module21_relay/module21a_extraction_queue.tsv`
- `work/module21_relay/module21a_first_pass_saturation.md`
- `work/module21_relay/module21a_q001_q009_batch1_summary.md`
