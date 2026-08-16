# Module 21A batch 227 review summary

## Scope

Reviewed exactly the 25 queued Module20A pairs supplied for this batch, in the
supplied order and with exact ligand/receptor labels. The review preserves the
three evidence layers separately: ligand–receptor binding or activation,
receptor-proximal relay, and downstream pathway or cellular function.

## Disposition

- 21 `reviewed_relay_candidate` rows.
- 2 `reviewed_function_only` rows: RGMB–NEO1 and RSPO3–RNF43.
- 2 `reviewed_binding_only` rows: RSPO2–LGR6 and RSPO3–LGR6.
- 0 unresolved or no-evidence-boundary rows; every submitted pair had at least
  a qualifying exact binding, complex, or pair-specific functional result.
- 25 unique review IDs and 25 unique pair labels.
- Provisional terminal-TF annotations: `CREB` for RLN1–RXFP1 and `TCF/LEF
  family` for the explicitly reporter-supported canonical WNT rows. These are
  handoffs for Module22A validation, not direct receptor–TF edges.

## Evidence highlights

Renin–ATP6AP2 and resistin–CAP1 have direct binding plus receptor-proximal or
intracellular relay evidence. RGMA–NEO1 is supported by direct binding and
RhoA/LARG/FAK or BMP-receptor-complex outputs; RGMB–NEO1 is retained at direct
complex and tissue-specific function because a unique RGMB-specific cytosolic
relay was not isolated. RP S19 was treated as an active cross-linked dimer and
not as monomeric ribosomal protein; its C5AR1 response is agonistic in some
myeloid contexts and antagonistic in others.

The relaxin rows distinguish native and cross-reactive receptor biology. RLN1
supports RXFP1 cAMP/PKA and CREB-linked signaling, while RLN3 supports RXFP3
and RXFP4 activation and lower-affinity RXFP1 cross-reactivity. RXFP3 remains
the native RLN3 receptor; cross-reactivity was not used to promote unrelated
relaxin-family pairs.

The RSPO block separates direct LGR, LRP6, RNF43, ZNRF3, and SDC4 evidence from
generic WNT pathway membership. LGR4/5 rows have direct binding and WNT reporter
or receptor-complex evidence. LGR6 rows are binding-only where a receptor-
specific downstream experiment was not isolated. RSPO1–LRP6 has direct
biochemical binding evidence but its intact-cell detectability is context
dependent. RSPO3–RNF43 is function-only because the exact RSPO3 FU1/RNF43
interaction module is required for WNT potentiation, while the cited exact
study did not provide a principal purified binary binding assay. RSPO3–SDC4 is
kept as a distinct noncanonical WNT/PCP, clathrin-endocytosis branch.

## Search boundaries and validation

Searches covered exact symbols and aliases across PubMed, PMC, publisher pages,
and stable DOI records, with primary biochemical, structural, perturbation, and
functional papers prioritized. Family-level evidence was not used to invent
direct molecular edges. HSPG, LGR-independent RSPO2/3, BMP/GDF ternary, and
generic WNT pathway findings are retained only in the stated context and
limitations.

- Exact 25 data rows and the required 13-column header.
- All rows have populated required fields, stable citations, and no embedded
  tabs or extra columns.
- Review IDs and pair labels are unique.
- Confidence values use the existing Module21A vocabulary.
- `terminal_TF` is literal `null` unless an explicit downstream CREB or TCF/LEF
  reporter/requirement was measured.
- Only `module21a_batch227_review.tsv` and this summary were written; no shared
  Module21A registers, Module20A ledgers, frozen manifest, SQL, or commit was
  modified.
