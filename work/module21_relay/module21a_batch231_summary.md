# Module 21A batch 231 review summary

Batch 231 covers exactly the 25 frozen Module20A queue rows supplied for review, in the supplied order. The frozen Module20A LR release manifest was verified by SHA-256 as `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Disposition

| Status | Count |
|---|---:|
| `reviewed_relay_candidate` | 8 |
| `reviewed_binding_only` | 2 |
| `reviewed_function_only` | 5 |
| `reviewed_scavenging_only` | 1 |
| `reviewed_no_downstream_evidence` | 8 |
| `reviewed_unresolved` | 1 |
| **Total** | **25** |

Confidence calls are 8 high, 16 medium, and 1 low. High confidence is limited to primary direct receptor/composite evidence or a well-resolved uptake edge; medium retains receptor-complex, species, matrix, latent-ligand, or assay-context caveats.

## Evidence boundaries

- SPP1/osteopontin rows are extracellular-matrix adhesion or integrin-dependent function records. The primary studies resolve alphaVbeta3, alphaVbeta5, and alphaVbeta6 heterodimers, not ITGAV or ITGB subunits in isolation. No intracellular relay or terminal TF was assigned.
- Canonical TGFB1/2/3-TGFBR1/TGFBR2 rows are receptor-complex relay candidates. TGFBR3/betaglycan and ENG are retained as accessory ligand-capture/presentation layers without inventing kinase signaling for those proteins.
- TGFB1-ITGB5 and TGFB3-ITGB6 preserve latent-LAP activation by alphaVbeta5/alphaVbeta6; the queued beta-subunit labels do not imply standalone receptors. TGFB1-ITGB8 preserves the MT1-MMP-dependent alphaVbeta8 activation relay.
- SDC2, VASN, TGM2-SDC4, and THBS1-LRP1 are retained as accessory, sequestration, matrix-adhesion, trafficking, or uptake layers. These are not collapsed into generic cytokine signaling.
- The TGFB3-ACVR1_TGFBR1_TGFBR2 composite is unresolved: TGF-beta/ACVR1 cross-phosphorylation and canonical TGFB3 receptor evidence were not combined into an exact four-component ligand-receptor claim.
- THBS1-Itga2b_Itgb3 is function-only at the queued composite level because the primary evidence supports a CD47/IAP-mediated activation bridge to platelet alphaIIbbeta3 rather than direct THBS1-alphaIIbbeta3 binding.

## Downstream and terminal-endpoint posture

Rows marked `reviewed_no_downstream_evidence` have qualifying direct binding or receptor-complex evidence but no pair-specific intracellular relay or downstream endpoint that can be promoted. Rows marked `reviewed_function_only` have receptor-dependent functional output without a fully resolved direct molecular relay. `terminal_TF` is literal `null` for all 25 rows because none of the reviewed primary records measured a pair-specific downstream TF/transcriptional endpoint suitable for this field.

Only the two requested batch231 artifacts were written. Shared registers, Module20A files, the frozen manifest, SQL, and existing files were not modified.
