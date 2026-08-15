# Module 21A Batch 026 summary

Date: 2026-08-14

## Scope

Reviewed the 15 exact Module20A priority-7 low/uncertain rows supplied for
LAMB2/LAMB3/LAMC1/LAMC2 with SV2A/B/C or integrin alpha1beta1. Module20A
ledgers, the frozen release manifest, and shared Module21A registers were not
modified.

## Results

- 15/15 exact queue rows reviewed.
- 3 `reviewed_function_only`: LAMB2-SV2A/B/C. Beta2-laminin knockout caused
  fewer SV2-positive varicosities and altered neuromuscular neurotransmission,
  but the study did not identify SV2 isoform or direct binding.
- 4 `reviewed_binding_only`: LAMC1-SV2A/B/C and LAMC1-ITGA1_ITGB1. These retain
  intact laminin-1/laminin-111 binding evidence while explicitly keeping the
  chain-only contribution unresolved.
- 8 `reviewed_unresolved`: all LAMB3-SV2A/B/C, LAMB3-ITGA1_ITGB1,
  LAMC2-SV2A/B/C, and LAMC2-ITGA1_ITGB1.
- 0 receptor-proximal relay promotions.
- 0 terminal TF assignments. No TF was directly measured for any exact queued
  pair.

## Evidence boundaries

The primary SV2 paper demonstrated electric-organ SV2H association with an
alpha5-beta1-containing laminin complex and high-affinity binding of purified
SV2H to laminin-1 (PMID:10617638; DOI:10.1074/jbc.275.1.451). It did not
resolve SV2A/B/C, LAMB2/LAMB3, or LAMC2. The beta2-laminin knockout study
(PMID:12563004; PMCID:PMC2342580) supports a functional presynaptic
association but not direct LAMB2-SV2 isoform binding.

Alpha1beta1 binding evidence was retained for intact laminin-111/short-arm
material (PMID:7525287; PMID:1827447; Reactome:R-HSA-216048). It was not
transferred to the beta3 or gamma2 chains. The gamma2-chain keratinocyte study
used alpha2beta1 rather than alpha1beta1 (PMID:11171386), so it remains a
negative boundary for LAMC2-ITGA1_ITGB1.

Search boundaries included exact gene-symbol and pair queries across PubMed,
PMC, publisher pages, Reactome laminin interactions, KEGG ECM/integrin
context, laminin trimer/chain aliases, and SV2A/B/C isoform terms. Pathway
database membership and family-level or intact-trimer evidence were retained
as context only and were not promoted to exact direct molecular edges.
