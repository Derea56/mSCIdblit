# Module 21A batch 024 review

Scope: 25 exact frozen Module20A priority-7 low/uncertain rows, M20A-EXT-0521 and M20A-EXT-0523 through M20A-EXT-0546. The frozen queue rows were read directly before review.

## Disposition

- 25/25 `reviewed_unresolved`
- 0 relay candidates
- 0 function-only promotions
- 0 binding-only promotions
- 0 no-downstream promotions
- 0 terminal TF assignments

The conservative result reflects the exact-pair rule. The literature contains relevant family- or matrix-level observations, but no qualifying exact chain/receptor assay or exact-pair perturbation was recovered for these rows. Those observations are retained in the TSV as limitations and were not promoted.

## Evidence boundaries

- Cholesterol/sterol intermediates and RORgamma activity are supported in ligand-binding, coactivator, and reporter systems, but DHCR24 was not demonstrated as part of the exact frozen Cholesterol-DHCR24-Rorc entity. See PMID 19965867 and the RORgamma sterol-ligand work: https://pubmed.ncbi.nlm.nih.gov/19965867/ and https://pubmed.ncbi.nlm.nih.gov/25637936/.
- SDC4 studies establish general ECM/HSPG adhesion or SDC4-intrinsic JNK/p53 and HIF-1/PHD2 signaling, but they do not establish the listed collagen-chain ligand. See PMID 9148893, PMID 32071547, and PMID 24558194: https://pubmed.ncbi.nlm.nih.gov/9148893/, https://pubmed.ncbi.nlm.nih.gov/32071547/, and https://pubmed.ncbi.nlm.nih.gov/24558194/.
- Native collagen-I, collagen-II, collagen-IV, and collagen-VI receptor studies were treated as matrix/family boundaries only. They were not reassigned to isolated COL1A2, COL2A1, COL4A1–COL4A6, or COL6A1–COL6A4 chains.
- The primary Col6a4 Hirschsprung model demonstrates Col6a4-dependent ECM deposition and enteric neural crest migration phenotypes, but it did not test CD44, GPVI, integrin, or SDC4 engagement. See PMID 26571399 and PMCID PMC4665793: https://pubmed.ncbi.nlm.nih.gov/26571399/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC4665793/.
- Collagen-VI receptor evidence for integrins and other receptors was retained only as a non-exact boundary; the search did not establish any listed COL6A4 receptor pair. Relevant primary/context sources include PMID 8387021 and PMCID PMC10462164: https://pubmed.ncbi.nlm.nih.gov/8387021/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC10462164/.
- Reactome was used for pathway/entity context. It shows SDC4 HS-glycan, PKC-alpha, and ECM interaction nodes and collagen-VI assembly entities, but does not provide exact COL4A/COL6A4-SDC4 or COL6A4-integrin pair evidence. See https://reactome.org/content/detail/R-HSA-2076670 and https://reactome.org/content/detail/R-MMU-2187500.

Search boundaries included exact gene-symbol and protein-name queries across PubMed, PMC, publisher pages, Reactome/KEGG context, and ECM/collagen receptor resources. Database co-membership, reviews, family-level receptor assignments, intact multichain matrix material, and noncognate receptor studies were not promoted to exact molecular or pathway edges.

## Files changed

- `module21a_batch024_review.tsv` — 25 validated review rows with the requested 13-column schema.
- `module21a_batch024_summary.md` — this batch summary.

Module20A ledgers, the frozen Module20A manifest, and shared Module21A registers were not modified.
