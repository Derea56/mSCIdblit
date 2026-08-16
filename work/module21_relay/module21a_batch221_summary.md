# Module 21A batch 221 review summary

Batch 221 reviews exactly the 25 currently queued Module 20A pairs specified for this batch, preserving the submitted ligand and receptor labels exactly. The review file uses the required 13-column schema and keeps three evidence layers separate: ligand–receptor binding or activation, receptor-proximal relay, and downstream pathway or cellular function.

## Disposition

- 15 `reviewed_relay_candidate` rows: 2352, 2356, 2357, 2359, 2361, 2363, 2365, 2368, 2375, 2381, 2415, 2418, 2427, 2443, and 2450.
- 4 `reviewed_binding_only` rows: 2354, 2360, 2369, and 2410.
- 6 `reviewed_function_only` rows: 2351, 2437, 2438, 2444, 2447, and 2449.
- 25 total rows; no unresolved/no-evidence row was required because each requested pair had at least a bounded primary or stable pathway-context record. Limitations are retained per row where the exact molecular interface, receptor complex, or downstream relay remains incomplete.

## Evidence and search boundary

Searches used exact symbols and aliases across PubMed, PMC, publisher pages, and Reactome pathway context, with primary research prioritized. Family-level or adjacent-receptor evidence was not transferred as an exact-pair claim unless the cited record tested the submitted pair or the explicitly named receptor complex. Stable PMID, PMCID, DOI, or URL citations are retained in the TSV.

The batch includes direct molecular evidence for examples such as LGALS1–CD69, LGALS1–ITGB1, LGALS3–ENG/MCAM, LGALS3BP–ITGB1, LGI–ADAM/RTN4R, LRRC4B–PTPRF, MATN1 in an alpha1beta1 context, MDK–ALK/GPC2, and LTA1B2–LTBR. The LGALS1–CD69 study supports carbohydrate-dependent receptor binding and a CD69-dependent immune output, while leaving the intracellular CD69 relay unresolved ([primary study](https://pubmed.ncbi.nlm.nih.gov/24752896/)). The LTA/LTB row is explicitly treated as the membrane LTα1β2 heterotrimer binding LTβR rather than isolated LTA or LTB; receptor dimerization and NF-κB signaling are supported by structural and reporter evidence ([primary study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3856818/)).

## Relay and terminal-TF handling

Direct binding, receptor-complex organization, pathway relay, and functional output are kept distinct in `relation_type`, `evidence_layer`, `pathway_branch`, and `limitations`. Pathway-level or phenotype-level evidence was not used to infer a direct molecular interaction. Non-catalytic adhesion/scaffold receptors and proteoglycans are described as receptor-complex or functional edges rather than forced into canonical kinase cascades.

`terminal_TF` is literal `null` for 23 rows. `STAT3` is retained only for LIF–IL6ST/LIFR and MDK–NOTCH2, where the cited studies directly measure the STAT3 branch; the MDK–NOTCH2 pathway is context-specific and includes additional receptor/signaling components ([primary study](https://pubmed.ncbi.nlm.nih.gov/18469519/)). No TF was inferred from AKT, MAPK, NF-κB, synaptic, adhesion, myelination, endocytic, or growth-function evidence alone.

Important bounded interpretations include: LHB is evaluated as part of intact alpha/beta LH or an LHB–CGA construct, not as an independently active isolated beta subunit; LRPAP1/RAP is a receptor-chaperone association with LRP2 rather than an extracellular ligand-triggered relay; LGI/ADAM and LRRC4B/PTPRF outputs require multicomponent synaptic complexes; MATN1–ITGB1 requires an alpha1beta1 context; and the MDK–LRP1 row is limited by source studies using an LRP preparation rather than an LRP1-purified receptor.

## Validation and file scope

- Confirmed the header has the exact requested 13 columns.
- Confirmed exactly 25 data rows, unique review IDs, unique submitted pairs, and the requested pair order/labels.
- Confirmed every row has stable citations, species, cell/model, assay or perturbation, relation type, evidence layer, pathway branch, confidence, and limitations.
- Confirmed confidence values are restricted to `medium`, `medium-high`, or `high`.
- Confirmed `terminal_TF` is `null` except for the two explicitly supported `STAT3` endpoints.
- Confirmed each edge has supporting evidence and that direct, receptor-complex/pathway, and functional claims remain distinguished.

Only these two Module 21A batch files were written in this operation. No Module 20A ledger, frozen manifest, saturation register, SQL materialization, or commit was modified.
