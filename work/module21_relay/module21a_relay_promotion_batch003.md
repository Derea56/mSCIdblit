# Module 21A relay/function promotion batch 003

This packet raises three exact Module 21A audit-layer evidence records from
`medium-high` to `high` for the receptor-complex relay/function layer.

| Evidence | Exact pair | Promotion basis | Boundaries retained |
|---|---|---|---|
| M21A-PAIR-EVID-4775 | PDGFB/PDGF-BB → PDGFRA | Purified or heterologous receptor binding, PDGF-BB-dependent PDGFRA activation, and downstream ERK/Akt/PLC-gamma and cell-response assays. | Alpha/beta receptor stoichiometry and model-specific branch strength remain explicit; no terminal TF assignment. |
| M21A-PAIR-EVID-4780 | PGF/PlGF → FLT1 | PlGF-FLT1 binding, FLT1 phosphorylation, receptor cross-talk, and endothelial/vascular functional assays. | PlGF isoform, soluble versus membrane FLT1, and VEGF/PlGF heterodimer context remain explicit; no terminal TF assignment. |
| M21A-PAIR-EVID-4786 | TGFA/TGF-alpha → EGFR | TGF-alpha-EGFR binding, EGFR tyrosine-phosphorylation/trafficking, kinase dependence, and growth-factor response assays. | Ligand trafficking differs from EGF and ERBB composition affects routing; no terminal TF assignment. |

The upstream Module 20A LR confidence is unchanged. No SQL `SignalingEdge`
rows or new Module 22A TF assignments are created. The promotion script
validates exact pair, evidence, reuse-key, source-locator, review-status, and
coverage lineage before writing.

Primary-source anchors reviewed for this decision include [PDGF-BB/PDGFR
binding](https://pubmed.ncbi.nlm.nih.gov/7679113/), [PlGF-FLT1 receptor
cross-talk](https://pubmed.ncbi.nlm.nih.gov/12796773/), [PlGF-FLT1 signal
transduction](https://pubmed.ncbi.nlm.nih.gov/9467961/), and [TGF-alpha/EGFR
autocrine interaction](https://pubmed.ncbi.nlm.nih.gov/2755700/).
