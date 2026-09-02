# Module 21A relay/function promotion batch 004

This packet raises four exact Module 21A audit-layer evidence records from
`medium-high` to `high` for the receptor-complex relay/function layer.

| Evidence | Exact pair | Promotion basis | Boundaries retained |
|---|---|---|---|
| M21A-PAIR-EVID-4777 | PDGFD/PDGF-DD → PDGFRB | Protease-activated PDGF-DD specificity plus receptor phosphorylation, perturbation, ERK/AKT/PLC-gamma, and smooth-muscle outputs. | Only processed/active PDGF-DD is promoted; latent PDGFD and PDGFR-alpha/beta heterodimer usage are not generalized. |
| M21A-PAIR-EVID-4783 | SEMA7A → ITGA1/ITGB1 | Alpha1beta1 integrin receptor evidence plus FAK/MAPK and neural/immune functional outputs. | The receptor is the alpha1beta1 heterodimer; membrane/GPI anchoring and neural/immune context remain explicit. |
| M21A-PAIR-EVID-4790 | TGFB2 → TGFBR1/TGFBR2 | Isoform-specific receptor binding/crosslinking, complex assembly, kinase/SMAD signaling, and growth-function evidence. | Betaglycan/coreceptor capture, receptor stoichiometry, and context-dependent potency remain explicit. |
| M21A-PAIR-EVID-4792 | TGFB3 → TGFBR1/TGFBR2 | Receptor-complex structural/reconstitution, crosslinking, SMAD2/3, and growth-function evidence. | TGFBR2/TGFBR1 complex and variable betaglycan/stoichiometry are retained; no SCI or terminal-TF claim. |

Upstream Module 20A LR confidence is unchanged. No SQL `SignalingEdge` rows or
new Module 22A TF assignments are created. The promotion script validates exact
pair, evidence, reuse-key, source-locator, review-status, and coverage lineage
before writing.

Primary-source anchors include [PDGF-DD/PDGFRB specificity](https://pubmed.ncbi.nlm.nih.gov/11331881/)
and [SEMA7A/alpha1beta1 integrin evidence](https://pubmed.ncbi.nlm.nih.gov/17377534/).
