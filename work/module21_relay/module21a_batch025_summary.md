# Module 21A batch 025 summary

Date: 2026-08-14

## Scope

Reviewed the 25 exact Module20A priority-7 low/uncertain rows supplied for
COL9A2/COL9A3/COMP–SDC4, DSPP–ITGAV_ITGB6, laminin–SV2A/B/C, and
laminin–ITGA1_ITGB1 evidence.

## Results

- 25 unique exact Module20A rows reviewed.
- 8 rows retained as `reviewed_binding_only`:
  DSPP–ITGAV_ITGB6 at the integrin-beta6-subunit scope, LAMA1–SV2A/B/C,
  and LAMB1–ITGA1_ITGB1 plus LAMB1–SV2A/B/C at intact-material or
  family-level scope.
- 18 rows retained as `reviewed_unresolved`.
- No exact receptor-proximal relay or downstream functional-output edge was
  promoted for the queued pair as written.
- No terminal TF was assigned. SMAD1/5/8 activation was directly measured in
  the DSP–beta6 study, but the queued alphaVbeta6 heterodimer was not directly
  reconstituted or perturbed.

## Evidence-layer handling

The DSP result was kept separate from the exact alphaVbeta6 pair because the
primary study demonstrated binding to the beta6 subunit and downstream
ERK1/2-p38-SMAD1/5/8 signaling, not the alphaVbeta6 heterodimer. The classic
SV2 study demonstrated SV2H binding to purified laminin-1 and association with
an alpha5/beta1-containing synaptic laminin complex, but did not resolve
vertebrate SV2A/B/C isoforms for the supplied rows. The LAMB1-alpha1beta1
result used intact laminin-111, so it remains material-level binding evidence
and not an isolated beta1-chain interaction.

Reactome, KEGG, STRING, PubMed searches, PMC, and publisher records were used
for context and search-boundary documentation. Pathway/database co-membership,
family-level laminin or collagen results, and noncognate chain/isoform evidence
were not promoted to exact molecular relays.

## Files changed

- `module21a_batch025_review.tsv`
- `module21a_batch025_summary.md`

Module 20A ledgers, the frozen Module20A release manifest, and shared Module
21A registers were not modified.
