# Module 21A relay-evidence review — Batch 155

Batch 155 reviewed the exact 25 filtered priority-8 queue rows assigned from queue ordinals 3326–3350. The Module 20A ledgers, frozen manifest, shared Module 21A registers, and Module 22A handoff were treated as read-only inputs. No terminal TF assignments were made.

## Outcome

| Evidence posture | Rows |
|---|---:|
| Reviewed unresolved / no-evidence boundary | 17 |
| Reviewed function-only pathway evidence | 1 |
| Reviewed composite receptor-proximal relay candidates | 5 |
| Reviewed binding-only physical-interaction records | 2 |
| **Total** | **25** |

The 17 relaxin-family rows remain unresolved for the submitted exact pairs. Primary RLN3 studies support cognate RXFP3/RXFP4 binding and activation, including Gi/o-linked signaling, but that evidence was not transferred to Rln1-Rxfp2/3/4 or the assigned Rln3 non-RXFP3/4 receptors. Comparator and expression/pathway findings were retained only as boundaries.

RSPO3–LRP6 was retained as downstream pathway/function evidence: recombinant RSPO3 participates in WNT/LRP6-dependent potentiation and LRP6 phosphorylation, but the primary work does not establish direct binary RSPO3–LRP6 binding. The four RSPO4 composite rows were retained as low-confidence composite relay candidates because primary studies support RSPO4 binding to LGR4/LGR5 and LGR-associated FZD/LRP WNT signalosomes, while the exact RSPO4–LGR4/5–LRP5/6 ternary bridge and direct RSPO4–LRP5/6 interaction remain unresolved. RTN4–LINGO1 is the fifth relay-candidate row and is retained only at the Nogo receptor-complex level.

RTN4–CNTNAP1 and RTN4–GJB2 were retained as binding-only records. The former is supported by Nogo-66 binding to the Caspr/F3 paranodal complex; the latter by a primary yeast-two-hybrid report of the RTN4 C-terminal region interacting with Cx26/GJB2. Neither establishes a canonical intracellular relay or terminal TF. RTN4–LINGO1 was retained as a complex-level relay/function candidate: NgR1/RTN4R is the established Nogo-66 ligand-binding subunit, whereas LINGO1 is a required or functional signaling-complex component; direct binary RTN4–LINGO1 binding was not claimed.

## Primary source anchors

- Relaxin-family receptor specificity and RLN3 receptor interaction: [PMID 16411781](https://pubmed.ncbi.nlm.nih.gov/16411781/), [PMID 24802387](https://pubmed.ncbi.nlm.nih.gov/24802387/), and [PMID 40410443](https://pubmed.ncbi.nlm.nih.gov/40410443/).
- RSPO/LRP6 pathway potentiation: [PMID 18400942](https://pubmed.ncbi.nlm.nih.gov/18400942/) / [PMCID PMC2397303](https://pmc.ncbi.nlm.nih.gov/articles/PMC2397303/).
- LGR4/5 binding and association with WNT receptor complexes: [PMID 21727895](https://pubmed.ncbi.nlm.nih.gov/21727895/) / [PMCID PMC3185347](https://pmc.ncbi.nlm.nih.gov/articles/PMC3185347/), with LGR5–LRP5/6 relay context in [PMID 33262293](https://pubmed.ncbi.nlm.nih.gov/33262293/).
- RTN4/Nogo-66–CNTNAP1/Caspr: [PMID 14592966](https://pubmed.ncbi.nlm.nih.gov/14592966/) / [PMCID PMC275427](https://pmc.ncbi.nlm.nih.gov/articles/PMC275427/).
- RTN4 C-terminal region–GJB2/Cx26: [PMID 17029193](https://pubmed.ncbi.nlm.nih.gov/17029193/).
- Nogo receptor complex and LINGO1 relay component: [PMID 14966521](https://pubmed.ncbi.nlm.nih.gov/14966521/) and [PMID 12068310](https://pubmed.ncbi.nlm.nih.gov/12068310/).

## Validation performed

- Output TSV has exactly 25 data rows plus the required header.
- Review IDs are unique and match the 25 assigned Module 20A IDs exactly.
- Pair labels match the canonical labels in `module21a_all_pair_relay_coverage.tsv` exactly, including composite receptor labels.
- All rows contain non-empty status, stable citations, species, model, assay/perturbation, relation type, evidence layer, pathway branch, confidence, limitations, and explicit `null` terminal-TF values.
- No rows outside the assigned set were written, and no Module 20A ledger, frozen manifest, shared register, or Module 22A handoff row was modified.
