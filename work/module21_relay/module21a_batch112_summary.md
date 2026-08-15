# Module 21A batch 112 review

Batch 112 covers the 25 exact requested priority-8 queue rows `M20A-EXT-1283` through `M20A-EXT-1314`, preserving the queue’s intervening ID gaps and canonical pair labels.

## Disposition

- 4 `reviewed_relay_candidate`: COL4A2–ITGB3, COL4A2–ITGB5, COL4A3–CD47, and COL4A3–ITGB3.
- 2 `reviewed_binding_only`: COL2A1–MAG and COL3A1–MAG.
- 19 `reviewed_unresolved`: COL24A1–ITGA2/ITGB1; all 12 COL26A1/COL27A1/COL28A1 collagen-binding integrin rows; COL2A1–ITGA2B and COL2A1–TNFRSF10B; COL4A1–CD47/CD93; COL4A2–CD93; and COL4A3–CD93.
- Terminal TF assignments: none. All `terminal_TF` fields are `null`.

## Evidence notes

- Soluble MAG directly binds collagen types II and III in the primary biochemical study using radiolabeled MAG, inhibition, and denaturation controls. These are retained as direct extracellular binding-only edges; no intracellular MAG relay was inferred.
- COL4A2 evidence is for the NC1 matricryptin canstatin, not necessarily intact collagen IV. Primary work supports binding to the complete alphaVbeta3 and alphaVbeta5 receptor complexes and an integrin-dependent mitochondrial/apoptotic branch involving FAK/PI3K/Akt suppression and caspase activation. The individual ITGB3 and ITGB5 queue labels remain represented as receptor-complex edges, not standalone beta-subunit receptors.
- COL4A3 evidence is chain-specific alpha3(IV) NC1 peptide/tumstatin-family evidence. CD47/IAP receptor capture and receptor-blocking studies support a CD47-associated cAMP/antiproliferative output, while independent work supports alphaVbeta3 binding and FAK/PI3K phosphorylation. The CD47 row retains co-receptor ambiguity; the ITGB3 row retains the alphaVbeta3 complex identity.
- COL24A1 was not assigned to alpha2beta1 because the primary COL24A1 study supports interaction with beta3 and TGF-beta/Smads-related osteoblast effects, not the requested alpha2beta1 complex.
- Type XXVII collagen was kept unresolved for every requested integrin because the primary pericellular-matrix study reports no proven integrin-binding sites; putative motif homology was not promoted. COL26A1 and COL28A1 likewise remain unresolved because no exact collagen–integrin primary assay was found in the bounded search.
- COL2A1–ITGA2B remains unresolved: collagen II comparator studies support collagen-binding alpha2beta1/alpha10beta1-family receptors and platelet GPVI/FcRgamma responses, not the alphaIIb receptor requested here. COL2A1–TNFRSF10B has no qualifying exact-pair evidence.
- COL4A1–CD47 was not transferred from alpha3(IV) evidence. COL4A1/COL4A2/COL4A3–CD93 rows remain unresolved; CD93 extracellular-matrix panels do not establish collagen IV binding, and no alpha-chain-specific positive assay was located.

## Search boundary

Searches covered exact gene/protein pair and receptor-complex queries across PubMed, PMC, publisher pages, Reactome, and NCBI Gene records, with primary biochemical, cell-adhesion, receptor-capture, and perturbation studies prioritized. Comparator evidence was retained only to define boundaries: collagen-family receptor specificity, alpha3-versus-alpha1/alpha2/alpha3 chain resolution, full-length collagen versus NC1 matricryptin fragments, and alphaVbeta3/alphaVbeta5 versus individual beta-subunit labels. No pathway annotation, expression correlation, motif prediction, or functional phenotype was converted into a direct molecular interaction.

## Validation and scope controls

- 25 data rows plus the exact 13-column header.
- Review IDs are unique and match the requested queue IDs exactly.
- Pair labels match the queue’s canonical labels exactly.
- No embedded tabs or newlines occur in data fields.
- Every row includes stable citations or stable search/resource URLs, species, model, assay/search boundary, relation type, evidence layer, pathway branch, confidence, limitations, and terminal-TF disposition.
- Direct binding, receptor-complex/proximal relay, and no-evidence boundaries remain distinct.
- This batch did not modify shared saturation registers, Module 20A ledgers, the frozen manifest, SQL materialization, or integration outputs.

## Files changed

- `work/module21_relay/module21a_batch112_review.tsv`
- `work/module21_relay/module21a_batch112_summary.md`
