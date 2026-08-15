# Module 21A batch 022 summary

Date: 2026-08-14

## Scope

Reviewed only the 12 specified frozen Module20A pairs M20A-EXT-0474 through
M20A-EXT-0493. The frozen queue rows were read first. Searches covered exact
gene/protein symbols and aliases across PubMed, PMC, publisher pages,
Reactome, KEGG, and tenascin/thrombospondin ECM resources. Primary research
was used where available; pathway resources were retained as context only.

## Results

- 3 reviewed_relay_candidate rows: Tnc-ITGA9_ITGB1, Tnc-ITGAV_ITGB3,
  and Tnc-ITGAV_ITGB6.
- 1 reviewed_binding_only row: Tnc-ITGA2B_ITGB3 has tenascin adhesion and
  receptor-identification evidence for alpha2beta1/alphaVbeta3 comparators,
  but no exact alphaIIbbeta3 downstream relay.
- 8 reviewed_unresolved rows: all THBS3/THBS4 entries except none promoted,
  Tnc-Sdc1, and all TNN entries.
- No reviewed_function_only, reviewed_no_downstream_evidence, or terminal-TF
  assignments were recorded.

## Evidence handling

The three TNC relay candidates retain receptor-specific perturbation and
downstream measurements: ITGA9-linked FAK/Akt and migration; ITGAV/ITGB3-linked
EGF-receptor phosphorylation and smooth-muscle-cell growth; and ITGAV/ITGB6-
linked FAK/ERK1/2 activation and epithelial-mesenchymal transition. These are
receptor-proximal/pathway edges, not direct ligand-to-TF claims.

TNN was searched as tenascin-N/tenascin-W. Its primary studies support
splice-variant neurite effects and alpha8- or alphaVbeta1/alpha4beta1-related
motility in comparator systems, but do not establish the queued TNN receptor
pairs. Similarly, thrombospondin-family CD36, alpha3beta1, alphaVbeta3, and
syndecan evidence was not transferred to THBS3/THBS4 exact pairs. Reactome and
KEGG/ECM pathway membership was used only to define search boundaries and
pathway context.

## Files changed

- `module21a_batch022_review.tsv`
- `module21a_batch022_summary.md`

No Module20A ledgers, frozen manifest, or shared Module21A registers were
modified.
