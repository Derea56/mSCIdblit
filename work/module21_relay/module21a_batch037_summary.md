# Module 21A batch 037 review summary

## Scope

Reviewed exactly the 25 requested priority-8 rows `M20A-CELLCHAT-REMAINING-0280` through `-0304` against the frozen Module20A external review queue. The queue contained all 25 IDs with the requested canonical labels. This batch writes one validated row per exact pair to `module21a_batch037_review.tsv`.

No Module20A ledger, frozen LR manifest, or shared Module21A register was modified. The frozen manifest SHA256 remained `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Classification

- Exact rows written: 25
- `reviewed_relay_candidate`: 8
- `reviewed_binding_only`: 9
- `reviewed_function_only`: 2
- `reviewed_unresolved`: 6
- Direct terminal TF assignments: 1 row (`Cd46 Jag1`, `RBPJ; HES1` as transcript induction, not direct TF occupancy)

Promoted receptor-proximal or receptor-complex cases include CD276–TREML2, CD46–JAG1, CD48–CD244A, CD52–SIGLECG, CD6–ALCAM, CD80–CD274, CD8A–CEACAM5, and CD99 homophily. Direct CD55/CD55B–ADGRE5 adhesion was kept in the binding layer. Functional-output evidence was kept distinct for CD96–PVR and VE-cadherin junctions. Direct homophilic adhesion was retained separately for CDH1, CDH15, CDH2, CDH3, and CDH4.

## Boundaries and unresolved cases

- CD200R-family papers did not resolve CD200 binding to the exact CD200R1L or CD200R3 paralogs.
- Human CD209/DC-SIGN–CEACAM1 evidence was retained as direct binding with a species/orthology limitation for the mouse-style queued label.
- Murine B7-H3–TREML2 evidence is strong, but a human negative study was retained as a species-specific limitation.
- CD52–SIGLECG was supported by a recent primary murine macrophage/tumor study; no terminal TF was assigned.
- Generic PILR-beta/CD99 evidence did not distinguish Pilrb1 from Pilrb2, so those rows remain unresolved; PILRA/CD99 direct glycan-dependent binding was retained separately.
- Cdh12–ITGA1_ITGB1 and Ceacam1–Cd1d1 remain unresolved. Alpha1beta1 evidence concerns collagen, and CEACAM5—not CEACAM1—was the CEACAM family member directly shown to bind CD1d.
- No TF was inferred from CellChat labels, adhesion alone, pathway diagrams, or functional outputs. RBPJ/HES1 were recorded only because the CD46–JAG1 study directly measured their transcript induction, with the limitation that direct TF occupancy/activity was not assayed.

## Search boundaries

Searches covered exact gene symbols and aliases, receptor-complex notation, ligand/receptor family names, PubMed, PMC, publisher pages, and pathway-context sources. Primary studies were retained when they directly measured binding, cell adhesion, receptor-complex perturbation, proximal signaling, or cellular output. Family-level, orthology-inferred, review-only, noncognate, and pathway-co-membership evidence was retained only as a limitation or negative search boundary.

## File

- `module21a_batch037_review.tsv`
