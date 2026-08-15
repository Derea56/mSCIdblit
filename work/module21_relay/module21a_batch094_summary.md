# Module 21A batch 094 review summary

Queue slice reviewed: exact filtered priority-8 ordinal rows 1651–1675 from `module20a_external_review_queue.tsv`.

Review IDs: `M20A-EXT-0674` through `M20A-EXT-0709` for 25 exact queue rows, including the queue gaps.

## Disposition

| Status | Count | Scope |
|---|---:|---|
| `reviewed_relay_candidate` | 2 | ADAMTS3–CCBE1 protease/cofactor processing complex; ADCYAP1–SCTR low-affinity cross-family receptor relay |
| `reviewed_binding_only` | 5 | ADAM28–ITGA4, ADAM7–ITGA4, ADAM7–ITGB7, ADAM9–ITGB5 direct disintegrin/integrin interactions; ADCYAP1–DPP4 direct peptide processing |
| `reviewed_function_only` | 0 | No exact pair had function-only evidence without a qualifying direct molecular or receptor-proximal record |
| `reviewed_unresolved` | 18 | ADAM29–ITGA4; PACAP–ADRB2/3, GPR20/84, PTH1R, RAMP2/3, TSHR; ADIPOQ–ASGR2/CNR2/GPR152/PROKR2; ADM–ADCYAP1R1/ADRB2/3/CALCR/DCLK3 |

## Evidence highlights

- ADAM28 and ADAM7 disintegrin-like domains bound activated alpha4beta1 and alpha4beta7 in primary lymphocyte adhesion assays. The queued ITGA4/ITGB7 nodes are retained as integrin-complex subunits, not as standalone receptor chains.
- ADAM9 directly interacted with alpha(v)beta5 in recombinant and osteoblast/myeloma-conditioned assays. The downstream IL-6 phenotype remains model-specific and was not generalized to all ITGB5 contexts.
- CCBE1 associated with ADAMTS3 and promoted ADAMTS3-dependent processing of pro-VEGFC. The resulting mature VEGFC activated VEGFR2/VEGFR3 and supported lymphangiogenic outputs. ADAMTS3 was treated as a protease and CCBE1 as a processing/cofactor component; this is not a direct ADAMTS3 cleavage claim against CCBE1.
- DPP4 directly cleaved PACAP into inactive N-terminally truncated products and accelerated PACAP clearance in vitro and in DPP4-deficient mice. This is a peptide-processing edge, not receptor activation.
- PACAP–SCTR was retained as a low-confidence/medium-low relay because recombinant receptor studies measured low-affinity PACAP recognition and weak activation relative to secretin. This branch is explicitly separated from canonical PAC1/VPAC signaling.

## Search boundaries and limitations

Primary PubMed, PMC, publisher, and pathway-oriented literature searches were used for exact pair names and receptor-complex variants. For the unresolved PACAP, adiponectin, and adrenomedullin rows, the search located canonical receptor evidence—PAC1/VPAC for PACAP, AdipoR1/AdipoR2/T-cadherin for adiponectin, and CALCRL/CLR-RAMP2/3 for adrenomedullin—but no qualifying exact alternate-pair binding, receptor activation, or subtype-isolated downstream perturbation. Shared class-B GPCR architecture, shared cAMP output, expression correlation, or tissue-level functional effects were not promoted to direct molecular edges.

Terminal TF assignments: none. No evidence in this batch directly demonstrated TF occupancy or an exact ligand-to-TF endpoint.

The review file contains one row per exact queue ID and preserves direct molecular, receptor-proximal, and downstream functional evidence as separate relation/layer annotations. No shared Module21A registers, Module20A ledgers, frozen manifest, or integration outputs were modified.
