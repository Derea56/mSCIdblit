# Module 21A batch091 review summary

## Scope and validation

- Reviewed the exact filtered priority-8 ordinal slice 1576–1600 from `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`.
- The slice contains 25 rows with non-contiguous review IDs: `M20A-CELLCHAT-REMAINING-1725` through `-1765`; the explicit filtered ordinal slice was treated as authoritative.
- Output: `module21a_batch091_review.tsv` with 25 rows, 13 columns, unique review IDs, and all required evidence fields populated.
- No Module 20A ledgers, frozen manifest, shared Module 21A registers, or integration outputs were modified.

## Disposition

| Status | Count | Main findings |
|---|---:|---|
| `reviewed_relay_candidate` | 11 | Testosterone–AR source-context composites; TGM2–ADGRG1; TRH–TRHR2; TSLP–IL7R/CRLF2; TUB/TULP1–MERTK; TXA2–TBXA2R; ULBP1–KLRK1 and KLRK1–HCST. |
| `reviewed_binding_only` | 5 | TENM3–ADGRL3; TENM4–ADGRL1; TULP1–AXL; TULP1–TYRO3; TULP2–TYRO3. |
| `reviewed_function_only` | 2 | Thy-1–ADGRE5 adhesion/trafficking; IGSF11/VSIG3–VSIR/VISTA checkpoint inhibition. |
| `reviewed_unresolved` | 7 | TENM/FLRT composite boundaries, unsupported TENM4 subtype combinations, and the UNC5A–ADGRL3 binary boundary. |

## Evidence decisions

- Teneurin/latrophilin records retain direct adhesion evidence only where the exact subtype was tested. TENM3–ADGRL3 and TENM4–ADGRL1 were promoted to binding; TENM/FLRT composite labels were not promoted from component-level evidence. The primary subtype study is [PMID 24273166](https://pubmed.ncbi.nlm.nih.gov/24273166/), with FLRT evidence in [PMID 22405201](https://pubmed.ncbi.nlm.nih.gov/22405201/) and structural complex boundaries in [PMID 32358586](https://pubmed.ncbi.nlm.nih.gov/32358586/).
- Testosterone rows distinguish mature testosterone–AR activation from enzyme/source labels. AR nuclear activation is supported by [PMID 1730684](https://pubmed.ncbi.nlm.nih.gov/1730684/) and [PMID 16210377](https://pubmed.ncbi.nlm.nih.gov/16210377/); AKR1D1, HSD17B12, and HSD17B3 remain source-processing context rather than direct AR interactors.
- TGM2–ADGRG1 is a receptor-proximal relay with RhoA/ROCK, ADAM17, and EGFR transactivation evidence ([PMID 38397010](https://pubmed.ncbi.nlm.nih.gov/38397010/); [PMCID PMC6916468](https://pmc.ncbi.nlm.nih.gov/articles/PMC6916468/)).
- TSLP–IL7R/CRLF2 is retained as a receptor-complex relay with JAK1/JAK2–STAT5 output ([PMID 10881176](https://pubmed.ncbi.nlm.nih.gov/10881176/); [PMID 22685175](https://pubmed.ncbi.nlm.nih.gov/22685175/)). STAT5A/STAT5B are the only terminal TFs promoted for this row; variable STAT1/3 outputs were retained as limitations.
- TUB and TULP1–MERTK records use direct binding, receptor phosphorylation, and phagocytic output evidence ([PMID 20978472](https://pubmed.ncbi.nlm.nih.gov/20978472/); [PMCID PMC3466361](https://pmc.ncbi.nlm.nih.gov/articles/PMC3466361/)). TULP1–AXL/TYRO3 and TULP2–TYRO3 remain binding-only because receptor-specific phosphorylation or function was not isolated.
- ULBP1–KLRK1 and ULBP1–KLRK1/HCST retain the adaptor-dependent NK-cell relay, supported by [PMID 21464092](https://pubmed.ncbi.nlm.nih.gov/21464092/), [PMID 12740575](https://pubmed.ncbi.nlm.nih.gov/12740575/), and [PMCID PMC7055393](https://pmc.ncbi.nlm.nih.gov/articles/PMC7055393/).
- IGSF11/VSIG3–VSIR/VISTA retains direct binding plus T-cell inhibitory function, but no intracellular relay or terminal TF was inferred ([PMID 30220083](https://pubmed.ncbi.nlm.nih.gov/30220083/); [PMCID PMC8027081](https://pmc.ncbi.nlm.nih.gov/articles/PMC8027081/)).

## Search boundaries and unresolved cases

- Searches covered exact gene/protein aliases across PubMed, PMC, publisher pages, NCBI records, and IUPHAR/Guide to PHARMACOLOGY pages where subtype pharmacology or receptor-complex nomenclature was needed.
- No direct ternary evidence was found for TENM3_FLRT1–ADGRL3, TENM3_FLRT3–ADGRL3, TENM4_FLRT1–ADGRL1, or TENM4_FLRT3–ADGRL1 in the exact composite configurations.
- No exact direct TENM4–ADGRL2, TENM4–ADGRL3, or UNC5A–ADGRL3 binary relay was validated. FLRT-mediated ternary complexes were retained as boundary context only.
- No terminal TF was assigned to adhesion GPCR, TAM phagocytosis, thromboxane, NKG2D, Thy-1/CD97, or VISTA functional outputs without exact pathway evidence.

