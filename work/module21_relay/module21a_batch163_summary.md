# Module 21A evidence review — Batch 163

Scope: exact filtered queue rows 3526–3550, reviewed in the supplied order. The companion TSV is raw and uses exactly the required 13-column schema:

`review_id`, `pair`, `status`, `stable_citations`, `species`, `cell_type_model`, `assay_or_perturbation`, `relation_type`, `evidence_layer`, `pathway_branch`, `confidence`, `limitations`, `terminal_TF`

## Disposition

- 25 exact queue rows reviewed; 25 unique review IDs and pair strings.
- 4 `reviewed_binding_only`: Tfpi–Vldlr, Tg–Asgr1, Tgfb3–Itgb3, Thbs1–Tnfrsf11b.
- 3 `reviewed_relay_candidate`: Tgfb1–Cav1, Tgm2–Itgb3, Thbs2–Itga4.
- 2 `reviewed_function_only`: Tgfb1–Cxcr4, Thbs1–Scarb1.
- 15 `reviewed_unresolved` plus 1 `no_evidence_boundary`.
- Every row has an explicit limitation; every `terminal_TF` is `none_found` because no pair-specific terminal transcription-factor assignment was established.

## Evidence-layer rules applied

Binding/activation, receptor-proximal relay, and downstream pathway/function were recorded as separate layers. A pathway, expression, interactome, co-occurrence, or perturbation result was not promoted to direct binding. In particular:

- Tfpi–Vldlr has primary binding evidence, with functional VLDLR context but no clean pair-specific proximal relay.
- Tg–Asgr1 has thyroid-cell recognition and endocytic uptake evidence; this is an uptake route, not a canonical signaling claim.
- Tgfb1–Cav1 is receptor-proximal CAV1–TGFBR1 scaffolding, not direct Tgfb1–Cav1 ligand binding.
- Tgfb1–Cxcr4 is TGF-beta1-driven CXCR4 induction/crosstalk; CXCL12/SDF-1 remains the CXCR4 ligand.
- Tgfb3–Itgb3 is latent TGF-beta3 LAP binding to alpha-v-beta3, not mature TGF-beta3 binding to ITGB3 alone.
- Tgm2–Itgb3 is a TG2/integrin-beta3 phagocytic scaffold/relay context, not a canonical soluble ligand-receptor edge.
- Thbs1–Scarb1 is a receptor-dependent functional association from interactome and perturbation evidence; direct biochemical binding was not isolated.
- Thbs2–Itga4 is conditional TSP2-fragment/alpha4-beta1 adhesion and chemotaxis evidence; the cited assay uses a fragment and the alpha4-beta1 heterodimer.

## Main unresolved boundaries

- Tgfa–Erbb3 and Tgfa–Erbb4: primary binding evidence supports EGFR/ERBB1; ErbB3/4 heterodimer or family context does not establish the exact pair.
- The Tgfb1/Tgfb2/Tgfb3 composite ACVR1-containing receptor rows remain unresolved. Canonical TGFBR1/TGFBR2 evidence does not validate the composite notation; ACVR1/ALK2 must not be conflated with ACVRL1/ALK1.
- Tgfb2–Eng remains unresolved because the primary endoglin receptor study reports binding to TGF-beta1/3 but failure to bind TGF-beta2; ENG is distinct from TGFBR3/betaglycan.
- Tgfb3–Itgb1 and Tgfb3–Itgb5 remain unresolved because latent-LAP form, ligand isoform, and alpha-v integrin heterodimer assignments do not transfer across rows.
- Tfpi–Sdc4, Tg–Tpo, Tgfb1–Lpp, Tgm2–Tbxa2r, Tgs1–Rxra, and Thbs1–Lrp5 retain explicit no-evidence boundaries rather than inferred edges.

## Primary-source anchors

The TSV records stable PMID/PMCID/DOI or stable exact-pair search URLs per row. Key primary anchors include PMID:11278667 (TFPI–VLDLR binding), PMID:14580721 (thyroid RHL-1/ASGR1 thyroglobulin uptake), PMID:11102446 (CAV1–TGFBR1 modulation), PMCID:PMC1782104 (TGF-beta1/CXCR4 functional crosstalk), PMID:1326540 (endoglin isoform binding boundary), PMID:12358597/PMCID:PMC1223078 (latent TGF-beta LAP–integrin binding), PMID:19643138 (TG2/integrin-beta3 phagocytic function), PMCID:PMC12665495/PMID:40772900 (THBS1–SCARB1 functional association), PMID:15799029 (THBS1–OPG association), and PMID:11980922/PMCID:PMC2173289 (TSP2/alpha4-beta1 fragment evidence).

No Module20A file, shared register, or other module artifact was modified, and no commit was made.
