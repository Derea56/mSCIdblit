# Module 21A Batch 180 Summary

Batch 180 reviewed exactly the 25 filtered priority-8 low/uncertain queue rows for ordinals 3951–3975: `M20A-LIANA-REMAINING-0223` through `M20A-LIANA-REMAINING-0247`.

## Outcomes

- 8 reviewed receptor-relay candidates: TGFB1–ACVRL1, TNF–TNFRSF1A, TNF–TNFRSF1B, TRAIL–DR5, RANKL–LGR4, APRIL–TACI, APRIL–BCMA, and BAFF–TACI, with binding/activation, receptor-proximal relay, and downstream function kept as separate evidence layers.
- 5 reviewed unresolved exact-pair or receptor-complex boundaries: Sema6B–PLXNA4, SPON2–ITGA4, SPON2–ITGA5, SPON2–ITGB1, and TGFA–EGFR_ERBB2.
- 3 reviewed binding/function boundaries: SPARC–ENG, TAC1–TACR1, and RANKL–TNFRSF11B; the latter is a soluble decoy/neutralization edge rather than an intracellular receptor relay.
- 3 reviewed function-only boundaries: TAC1–TACR2, TNFSF11–TNFRSF11A, and TWEAK–TNFRSF12A; each is supported by receptor-dependent function or perturbation rather than a clean purified binding assay.
- 6 explicit no-evidence boundaries: TGFB1/2/3 with ACVR1B_TGFBR2 or ACVR1C_TGFBR2; TGFB1–ACVRL1 is separately supported as an ACVRL1-containing receptor-complex relay.

## Evidence boundaries

The Sema6B, SPON2, TAC1, and TGFA rows preserve processed-ligand, cis/trans, heterodimer, and composite-receptor limitations. Integrin evidence is assigned to alpha4beta1/alpha5beta1 complexes and is not converted into binding to a free ITGA4, ITGA5, or ITGB1 chain. TAC1 evidence is assigned to its processed substance-P or neurokinin-A products rather than the precursor as an undifferentiated ligand.

The TGFB composite rows remain explicit no-evidence boundaries: TGFBR2 component evidence, ACVR1B/ACVR1C activin evidence, and generic TGF-beta pathway membership were not combined into direct binding or activation of the submitted composites. TGFB1–ACVRL1 is retained only as an ACVRL1-containing receptor-complex relay with type-II/accessory-receptor caveats.

TNF-family rows distinguish direct binding, receptor-dependent function, decoy neutralization, receptor-proximal signaling, and downstream outputs. No terminal TF was assigned; every `terminal_TF` value is the literal `null`.

Only the batch180 TSV and summary were written. Module20A and shared Module21A ledgers were not modified, and no commit was created.
