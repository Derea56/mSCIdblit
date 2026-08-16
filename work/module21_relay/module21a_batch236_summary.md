# Module 21A batch 236 review summary

Batch 236 covers exactly the 25 queued pairs supplied for IDs `0512` through
`0536`, in the supplied order. Evidence was restricted to primary PubMed,
PMC, and publisher records, with stable PMID, PMCID, DOI, or URL identifiers
only. The frozen Module20A LR manifest SHA-256 is
`02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Disposition

| status | rows |
|---|---:|
| `no_evidence_boundary` | 12 |
| `reviewed_unresolved` | 8 |
| `reviewed_function_only` | 4 |
| `reviewed_relay_candidate` | 1 |
| `reviewed_no_downstream_evidence` | 0 |
| **total** | **25** |

Confidence counts are `low`: 22 and `medium`: 3; no row was assigned high
confidence. Every `terminal_TF` value is the literal `null`.

## Evidence boundaries

- The primary WNT7B receptor study resolves WNT7B binding and cooperative
  canonical activation with FZD1/FZD10 and LRP5, not the queued FZD5-FZD9
  composites (PMID:15923619; PMCID:PMC1140585; DOI:10.1128/MCB.25.12.5022-5030.2005).
  A multiplex primary map reports WNT7B-FZD5/FZD8 functional activity, but it
  does not establish the requested LRP5- or LRP6-specific ternary composites
  (PMID:28733458; PMCID:PMC5636703; DOI:10.1096/fj.201700144R). Those rows are
  therefore unresolved where one receptor component is supported and
  `no_evidence_boundary` where no exact FZD result was recovered.
- Holmen et al. directly tested Xenopus XWnt8 fused to FZD3, FZD4, FZD5,
  FZD6, or FZD7 with LRP5/6 in 293T reporter and beta-catenin assays. FZD4
  and FZD5 produced strong LRP6 activity; FZD3 and FZD6 were weak; FZD7 was
  intermediate. The full XWnt8-FZD5 construct also physically associated with
  LRP6 and activated reporter output (PMID:12121999;
  DOI:10.1074/jbc.M204989200). Because these are fusion constructs, the TSV
  distinguishes exact construct-level function from native WNT8A ternary
  binding and relay claims.
- Natural WNT8A-LRP6 association and synaptogenic function were reported in
  primary neurons, and WNT8A-FZD5/FZD8 activity was mapped in a separate
  primary receptor-rescue study (PMCID:PMC3924421; PMID:28733458). These
  results were used as context and were not allowed to upgrade an unmatched
  FZD/LRP composite.
- Human hESC work linking WNT8A/FZD7 to canonical mesoderm induction and
  zebrafish work showing Wnt8a/Fzd7a/Ror2 source-cell context do not establish
  WNT8A-FZD7-LRP5 stoichiometry or a native exact composite (PMID:27641648;
  PMCID:PMC5063467; DOI:10.1016/j.stemcr.2016.08.008; PMID:30060804;
  PMCID:PMC6086664; DOI:10.7554/eLife.36953).

Binding/activation, receptor-proximal relay, and downstream pathway/function
are separated in `evidence_layer`. TOP/TOPFLASH reporter activity and
beta-catenin stabilization were retained as pathway outputs and were not
converted into terminal TF annotations. No family-level FZD/LRP result,
generic beta-catenin result, expression result, or unrelated WNT ligand was
transferred to an exact composite.

## Validation

- TSV header exactly matches the requested 13-column schema.
- TSV contains exactly 25 data rows; IDs and pairs match the supplied order.
- All rows contain 13 populated fields; no tabs occur inside fields and no
  row has missing or extra columns.
- `confidence` is restricted to `high`, `medium`, or `low`; observed values
  are only `low` and `medium`.
- `stable_citations` contains only PMID, PMCID, and DOI identifiers.
- All `terminal_TF` fields are literal `null`.
- Frozen manifest SHA-256 matches the required value.
- Only `work/module21_relay/module21a_batch236_review.tsv` and this summary
  were written; shared registers, Module20A files, the manifest, SQL, and
  existing unrelated files were not modified.
