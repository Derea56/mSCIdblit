# Module 21A batch 109 review

Batch 109 covers the exact filtered priority-8 queue ordinal slice 2026–2050. All 25 requested review IDs are present exactly once, with the queue’s intervening ID gaps preserved: `M20A-EXT-1175` through `M20A-EXT-1215`.

The current queue snapshot was validated by the explicit requested review IDs and canonical pair labels. All 25 selected IDs are still marked priority 8. Because the queue has accumulated later status updates, reconstructing the historical ordinal solely by applying a fresh filter to the current snapshot does not reproduce the prior ordinal numbering; no substitute rows were used.

## Disposition

- 8 `reviewed_relay_candidate`: CIRBP–TREM1, CLCF1–SORL1, CLEC11A–ITGA10, CLEC11A–ITGB1, CNTF–CNTFR_IL6ST, CNTF–IL6RA, CNTF–IL6ST_LIFR, and COL11A1–DDR1.
- 2 `reviewed_function_only`: CGN–TGFBR1 and CGN–TGFBR2.
- 4 `reviewed_binding_only`: CGN–OCLN, CNTN2–CNTN1, CNTN2–NRCAM, and COL10A1–ITGA10_ITGB1.
- 11 `reviewed_unresolved`: CGA–VIPR1; CKLF–LRP6; CLEC1B–KLRB1A/B/C; CLEC3A–CLEC10A/MGL2; CNTF–CRLF1; CNTF–EGFR; COL10A1–ITGA11_ITGB1; and COL10A1–ITGA1_ITGB1.
- Terminal TF assignments: 3, all exact CNTF relay rows, ending in `STAT3`. No terminal TF was inferred for adhesion, matrix, sorting, or pathway-only rows.

## Evidence notes

- CIRBP–TREM1 is supported as extracellular CIRBP/eCIRP binding and activating TREM1, with DAP12/TYROBP and SYK receptor-proximal relay evidence. The TREM1 cytoplasmic signaling dependency was preserved; no direct CIRBP–DAP12 edge was inferred.
- CLCF1–SORL1 is retained as a complex-context relay candidate. The evidence supports CLCF1-moiety-dependent sorLA/SORL1 binding within the CLCF1–CRLF1–CNTFRα complex and SORL1-mediated capture/turnover/presentation. SORL1 was not treated as the standalone signal-transducing cytokine receptor.
- CLEC11A–ITGA10 and CLEC11A–ITGB1 are receptor-complex rows. Osteolectin/CLEC11A binds α10β1 and α11β1, but the strongest functional receptor assignment is α11β1. ITGA10 and ITGB1 were not interpreted as independent standalone receptors, and Wnt/β-catenin was not converted into a terminal TF without exact endpoint evidence.
- CNTF rows preserve exact receptor composition. Canonical CNTF signaling requires CNTFRα plus the gp130/IL6ST–LIFR beta heterodimer; an alternative CNTF–IL6Rα route is retained only where exact receptor-reconstitution evidence supports it. CRLF1 was not promoted because it is a cofactor in the distinct CLCF1–CRLF1 composite cytokine branch, and EGFR was not promoted because no qualifying exact CNTF–EGFR relay was found. LIF/OSM-family pathways were not transferred to CNTF rows without exact receptor support.
- CNTN2–CNTN1 and CNTN2–NRCAM are direct neuronal cell-adhesion bindings with guidance/adhesion consequences, not intracellular kinase relays. Their GPI-anchored CAM topology and cis/trans context were preserved.
- COL10A1–ITGA10_ITGB1 is direct collagen X–α10β1 binding. COL10A1–ITGA11_ITGB1 and COL10A1–ITGA1_ITGB1 remain unresolved because the reviewed primary evidence supports other collagen X receptors/complexes, not these exact heterodimers; pathway annotations were not used to infer direct binding.
- COL11A1–DDR1 is retained as collagen XI fibril binding/activation of DDR1 with Shc/MAPK relay context. The source studies do not provide a unique COL11A1 motif or an exact terminal TF, so no TF was assigned.
- CGN–OCLN is a direct cytoplasmic tight-junction plaque interaction. CGN–TGFBR1/2 remain function-only: TGF-β treatment and junction/EMT pathway observations support an output association, not direct CGN binding to either receptor subunit.
- CGA–VIPR1, CKLF–LRP6, CLEC1B–KLRB1A/B/C, CLEC3A–CLEC10A/MGL2, CNTF–CRLF1, CNTF–EGFR, and the two unresolved COL10A1 integrin rows document explicit no-evidence boundaries. Closest cognate family or pathway evidence was recorded only to prevent mistaken transfer.

## Search boundary

Searches covered exact-pair and receptor-complex queries across PubMed, PMC full text, publisher pages, and Reactome boundary annotations, with primary research preferred. The review explicitly separated: cytokine receptor-complex composition and JAK/STAT relay; lectin/immune receptor family distinctions; neuronal CAM adhesion; collagen–integrin heterodimers; collagen–DDR1 activation; and EGFR/TGFBR pathway branches. For unresolved rows, the TSV records the closest relevant branch and why it does not support the exact pair. No pathway-level or functional observation was converted into a direct molecular interaction.

## Validation and scope controls

- 25 data rows and 13 columns; exact requested header.
- Review IDs are unique, explicitly present in the current queue snapshot, marked priority 8, and match the requested canonical pair labels for ordinal rows 2026–2050.
- Each row contains stable citation identifiers or a stable search URL, an evidence layer, relation type, pathway branch, confidence, limitations, and terminal-TF disposition.
- Direct binding, receptor-proximal relay, downstream function, and no-evidence boundaries remain distinct.
- This batch did not modify shared saturation registers, Module 20A LR ledgers, the frozen manifest, SQL materialization, or integration outputs. Existing unrelated worktree modifications were preserved.

## Files changed

- `work/module21_relay/module21a_batch109_review.tsv`
- `work/module21_relay/module21a_batch109_summary.md`
