# Module 21A relay/function promotion batch 001

This packet raises two exact Module 21A audit-layer evidence records from
`medium-high` to `high` for the receptor-complex relay/function layer.

| Evidence | Exact pair | Promotion basis | Boundaries retained |
|---|---|---|---|
| M21A-PAIR-EVID-4743 | IL17A → IL17RA/IL17RC | Primary studies support IL-17 receptor-complex participation, IL17RC/IL17RA-dependent signaling, ACT1/SEFIR proximal logic, and inflammatory readouts. | Receptor stoichiometry and relative subunit contributions remain context-dependent; no SCI receiver or terminal TF assignment. |
| M21A-PAIR-EVID-4751 | IL33 → IL1RL1/ST2–IL1RAP | Structural studies support IL-33/ST2/IL1RAP assembly, and reconstitution/blockade studies support ST2-dependent inflammatory signaling. | ST2L versus soluble ST2 remains explicit; the models are engineered or comparator systems; no terminal TF assignment. |

The source set is unchanged and remains traceable in the detail and review
TSVs. The upstream Module 20A LR confidence is not changed, because it is a
different evidence layer. No SQL `SignalingEdge` rows or Module 22A TF
assignments are created. The promotion script validates exact pair, evidence,
reuse-key, source-locator, and coverage lineage before writing.

Primary-source anchors reviewed for this decision include [IL-17RC receptor
identification](https://pubmed.ncbi.nlm.nih.gov/17911633/), [IL-17RC
signaling-domain/reconstitution evidence](https://pubmed.ncbi.nlm.nih.gov/20554964/),
[IL-17RA/IL-17RC-dependent IL-17A response](https://pubmed.ncbi.nlm.nih.gov/18097068/),
[IL-33/ST2/IL1RAcP structural analysis](https://pubmed.ncbi.nlm.nih.gov/19836339/),
[IL-33 receptor structural analysis](https://pubmed.ncbi.nlm.nih.gov/23980170/),
and [ST2 reconstitution and IL-33 signaling](https://pubmed.ncbi.nlm.nih.gov/27031441/).
