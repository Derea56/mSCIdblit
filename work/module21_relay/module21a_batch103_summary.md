# Module 21A batch 103 review summary

## Scope

Reviewed exact filtered priority-8 queue ordinals 1876–1900, review IDs M20A-EXT-0984 through M20A-EXT-1008. The queue mapping was checked against `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`; all 25 IDs and pair labels match exactly.

## Disposition

- 25 exact rows reviewed.
- 5 `reviewed_relay_candidate`: BTC–ERBB3; C1QB–LRP1; C3–CD46; C3–ITGAM/CR3; C3–ITGAX/CR4.
- 4 `reviewed_binding_only`: C1QB–C1QBP; C1QTNF5–MFRP; C4A–CD46; C4A–CR2.
- 2 `reviewed_function_only`: C3–CD19; C3–CD81.
- 14 `reviewed_unresolved`: BST1–CAV1; BTLA–CD247; BTLA–CD79A; BTN1A1–NEGR1; BTN1A1–TARM1; C1QA–CD93; C1QTNF1–AVPR2; C3–ADRA2A; C3–C5AR2; C3–GRM7; C3–LRP1; C3–MTNR1A; C3–NRP1; C4A–C5AR2.
- No terminal TFs assigned.

## Evidence boundaries

- Complement rows were normalized to the biologically tested processed fragments and complexes: C3b/iC3b for CD46/CR3/CR4, C3d/C3dg for the CR2–CD19–CD81 complex, C4b for CD46, and C4d for CR2. No direct interaction with an unprocessed C3/C4A precursor was inferred.
- C3–CD19 and C3–CD81 are retained only as receptor-complex/function edges. The direct complement-binding receptor is CR2/CD21; CD19 and CD81 are coreceptor components.
- C3–ITGAM and C3–ITGAX preserve the complete CR3/CR4 beta2-integrin complexes in the pathway text. ITGAM or ITGAX alone was not treated as a complete receptor.
- C1QA–CD93 remains unresolved because CD93/C1qRp involvement in C1q-mediated phagocytosis is disputed; the stronger C1q uptake branch is calreticulin–CD91/LRP1.
- C1QB–C1QBP is binding-only and low confidence because historical C1q/gC1qR binding evidence conflicts with the predominantly mitochondrial localization of C1QBP.
- No generic complement, adhesion, membrane proximity, or pathway co-occurrence was promoted to a direct molecular edge or terminal TF.

## Search boundary

Searches covered PubMed, PMC, and publisher-indexed primary research for the exact pair and relevant processed complement fragment or receptor complex. For unresolved pairs, stable PubMed query URLs are retained in the TSV to document the negative search boundary. Primary anchors included BTC–ErbB activation (PMID 12475887), C1q–LRP1 binding (PMID 33193398), C1q/CD91 efferocytosis (PMID 11560994), C3b–CD46 (PMID 24321396), CR3 signaling (PMID 33397789), CR4 phagocytosis (PMID 1358992), C3d coreceptor function (PMID 18180801; PMID 19706534), and C5L2 exclusion of C3a binding (PMID 17068344).

## Files

- `work/module21_relay/module21a_batch103_review.tsv`
- `work/module21_relay/module21a_batch103_summary.md`

This batch remains isolated and has not modified shared Module 21A registers, Module20A ledgers, the frozen LR manifest, or integration outputs.

