# Module 21A batch 038 review summary

## Scope

Reviewed the 25 exact Module20A priority-8 queue rows `M20A-CELLCHAT-REMAINING-0305` through `-0329` and wrote one validated row per exact pair to `module21a_batch038_review.tsv`.

The batch contains CEACAM1/CEACAM2 immune-adhesion composites, the CGA_TSHB–Tshr endocrine pair, and cholesterol/CEL or cholesterol/DHCR7 composites linked to Rora/Rorc. Sterol enzyme labels were treated as source-context annotations, not as ligands or receptors.

## Classification

| status | count | disposition |
|---|---:|---|
| `reviewed_relay_candidate` | 5 | Ceacam1 homophilic signaling; CGA_TSHB–Tshr; cholesterol–Rora/Rorc nuclear-receptor activation |
| `reviewed_binding_only` | 1 | Ceacam1–Ceacam5 heterophilic adhesion |
| `reviewed_unresolved` | 19 | Exact Ceacam1/Ceacam2 pairings with mouse CD1d, CD209 paralogs, Cd8a, Ceacam2, Psg20, or Sele lacked qualifying exact evidence |

Direct terminal TF assignments were retained only where the exact queued ligand–receptor context was experimentally connected to a TF node: `ATF2` for TSHR-associated p38 signaling, `RORA` for cholesterol–RORα, and `RORC` for cholesterol/sterol–RORγ.

## Key validated evidence

- CEACAM1 homophilic binding and receptor-proximal signaling are supported by membrane/ectodomain binding, SPR, dimerization, cross-linking, FRET, and SHP-2/c-Src recruitment studies (PMIDs `19948502`, `19948503`; PMCIDs `PMC2779236`, `PMC2779222`). This was retained as a receptor-proximal relay, without assigning a terminal TF.
- Human CEACAM1–CD209 binding is supported through Lewis-x glycans in granulocyte/DC models (PMID `16282604`; DOI `10.1093/glycob/cwj057`). This was not transferred to mouse `Cd209a`–`Cd209e` paralogs.
- CEACAM5, not CEACAM1, was the CEACAM member shown to bind CD1d and CEACAM5 also bound CD8α in the primary intestinal study (PMCID `PMC3981948`; DOI `10.1038/mi.2013.80`). This was used as a negative/family boundary for the queued CEACAM1/2–CD1d and –Cd8a rows.
- TSH binds and activates TSHR with Gs and Gq/11 branches, cAMP/PKA signaling, and p38/MAPK output. ATF2 phosphorylation was directly measured in TSHR-expressing cells (PMID `11006268`; DOI `10.1074/jbc.M002097200`).
- Cholesterol was structurally identified in the human RORα ligand-binding pocket and RORα transcriptional activity was cholesterol-sensitive (PMID `12467577`; DOI `10.1016/S0969-2126(02)00912-7`). Cholesterol and hydroxycholesterols promoted RORγ coactivator recruitment and receptor-reporter activity (PMID `20203100`; PMCID `PMC2870936`; DOI `10.1210/me.2009-0507`). CEL and DHCR7 were not manipulated in these receptor assays.

## Search boundaries and limitations

Searches covered exact gene-symbol pairs and aliases across PubMed, PMC, publisher pages, and pathway/family context. Family-level CEACAM, human CD209, CD1d, CD8α, E-selectin, and pregnancy-specific glycoprotein evidence was retained only as a boundary or limitation when it did not resolve the exact queued pair. No direct interaction was inferred from co-expression, knockout phenotype, pathway membership, or sterol-enzyme annotation.

## Validation

- 25 rows written; 25 unique review IDs.
- Output IDs exactly match queue IDs `0305–0329`; canonical pair labels match the frozen queue.
- Required evidence fields are non-empty for every row.
- Evidence layers are limited to `ligand_receptor_binding_or_activation` and `receptor_proximal_relay`; no downstream claim was promoted without direct support.
- Module20A ledgers, shared Module21A registers, and the frozen LR manifest were not modified.
- Frozen manifest SHA256 remains `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.
