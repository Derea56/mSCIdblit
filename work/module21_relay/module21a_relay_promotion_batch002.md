# Module 21A relay/function promotion batch 002

This packet raises four exact Module 21A audit-layer evidence records from
`medium-high` to `high` for the receptor-complex relay/function layer.

| Evidence | Exact pair | Promotion basis | Boundaries retained |
|---|---|---|---|
| M21A-PAIR-EVID-4753 | IL36A → IL1RL2/IL1RAP | Quantitative receptor-binding and pathway studies support IL-36α engagement of IL1RL2 and ligand-dependent IL1RAP recruitment. | Agonist processing and cell context affect potency; soluble-domain biophysics is not an SCI receiver assay; no terminal TF assignment. |
| M21A-PAIR-EVID-4754 | IL36B → IL1RL2/IL1RAP | IL-36β is supported as an agonist of the IL1RL2/IL1RAP pathway in the processed-ligand and receptor-complex source packet. | Receptor-complex and processing context remain explicit; no terminal TF assignment. |
| M21A-PAIR-EVID-4755 | IL36G → IL1RL2/IL1RAP | IL-36γ is supported as an agonist of the IL1RL2/IL1RAP pathway in the processed-ligand and receptor-complex source packet. | Receptor-complex and processing context remain explicit; no terminal TF assignment. |
| M21A-PAIR-EVID-4759 | INHBA/Activin A → ACVR1B/ACVR2B | Primary receptor studies support ACVR2B binding, ACVR1B recruitment/activation, and SMAD2/3-associated functional signaling. | ACVR2A/B redundancy and non-native receptor systems limit quantitative extrapolation; no SCI receiver weighting is assigned. |

The upstream Module 20A LR confidence is unchanged. No SQL `SignalingEdge`
rows or new Module 22A TF assignments are created. The promotion script
validates exact pair, evidence, reuse-key, source-locator, review-status, and
coverage lineage before writing.

Primary-source anchors reviewed for this decision include [quantitative
IL-36 ligand/receptor binding](https://pubmed.ncbi.nlm.nih.gov/29180446/),
[IL-36 processing and receptor-complex recruitment](https://pubmed.ncbi.nlm.nih.gov/21965679/),
[Activin receptor-complex activation](https://pubmed.ncbi.nlm.nih.gov/8622651/),
[Activin A receptor-dependent SMAD2 signaling](https://pubmed.ncbi.nlm.nih.gov/24886203/),
and [Activin A interaction with type-II receptors](https://pubmed.ncbi.nlm.nih.gov/26047946/).
