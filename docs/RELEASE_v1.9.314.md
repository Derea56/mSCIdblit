# mSCIdblit release v1.9.314

Release ID: `module20_24_mechanism_graph:2026-09-24-ifnl-and-il6-route-queue-515`

This release extends the all-ligand evidence layer with 14 source-linked
route annotations: nine type-III interferon routes covering IFN-lambda 2, 3,
and 4 through the IFNLR1/IL10RB receptor, TYK2-dependent STAT signaling,
ISGF3, and ISG15/IFIT1/OAS1 outputs; and five IL-6 routes covering
IL-6→IL-6R/gp130→JAK1→STAT3→SOCS3, MYC, CRP, LCN2, and CEBPB.

The IFN-lambda annotations retain the receptor-proximal-to-ISGF3 handoff as
an explicit missing-link field. The IL-6 annotations use existing
evidence-gated receptor, JAK1, STAT3, and STAT3-target edges. All 14 records
remain evidence-layer routes: no causal graph edge, confidence score, or
unverified traversal permission was created.

The final bundle contains 591,180 route-evidence rows, 25,066 literature
expansion rows, and 15,081 deduplicated full-sequence curation candidates
spanning 1,862 ligands and 1,633 receptors. Coverage remains 182 ligands with
full functional-output routes, 59 with full target-gene routes, 1,568 partial
downstream routes, and 804 ligand–receptor-only entries.

Validation passed with no errors. The remaining warning concerns inherited
evidence sources without stable locators.
