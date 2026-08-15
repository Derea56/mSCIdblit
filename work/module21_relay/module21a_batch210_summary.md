# Module 21A batch 210 summary

## Scope

Batch 210 contains exactly the corrected 25-row scope requested by the user:
`M20A-EXT-1578` through `M20A-EXT-1602`, ending with `F8 Lrp2`. The excluded
pair `M20A-EXT-1603 F8 Lrp4` is not present in this batch or summary.

## Disposition

- 7 reviewed relay candidates: F11r–ITGAL_ITGB2, F2–F2r, F2–F2rl1,
  F2–F2rl2, F2–F2rl3, F2–Thbd, and F7–F3.
- 5 reviewed binding-only records: F10–Itgam, F13a1–Itga4, F13a1–Itga9,
  F8–Asgr2, and F8–Lrp2.
- 2 reviewed scavenging-only records: F8–Ldlr and F8–Lrp1.
- 9 reviewed unresolved records: F11–Gp1bb/Gp5/Gp9, F12–Gp1bb/Gp5/Gp9,
  F13a1–Itgb1, and F2–Gp1bb/Gp9.
- 2 explicit no-evidence boundaries: F12–Cd93 and F2–Itga2b.

The TSV is authoritative for row-level disposition. Receptor-complex evidence
is retained as a complex/pathway record and is not promoted to a direct
subunit interaction. No terminal TF endpoint is assigned in this batch.

## Evidence and search boundary

Searches covered exact submitted symbols and principal aliases across PubMed,
PMC, publisher pages, Reactome, and related pathway pages. Primary anchors
include FXI–platelet GPIb-IX-V binding, JAM-A/F11R–LFA-1, FXIII–alpha4beta1 and
alpha9beta1 adhesion, thrombin–PAR1/PAR2/PAR3/PAR4, thrombin–thrombomodulin,
FVIIa–tissue factor, and FVIII interactions with LDLR-family receptors.

Binding, receptor-complex/proximal relay, downstream pathway/function, and
endocytic/scavenging evidence are separated in the TSV. Platelet activation,
ERK, calcium, PKC, protein C activation, adhesion, and clearance outputs are
not treated as terminal TF evidence. Where a primary paper supported only a
receptor complex or a neighboring subunit, the exact submitted pair remains
`reviewed_unresolved` or `no_evidence_boundary`.

## Validation target

The review file must contain exactly 25 data rows, the exact 13-column schema
`review_id,pair,status,stable_citations,species,cell_type_model,assay_or_perturbation,relation_type,evidence_layer,pathway_branch,confidence,limitations,terminal_TF`, unique IDs and pair labels, populated required fields, allowed confidence values, and literal `null` for every terminal-TF field. Only the two batch-210 files are written; no ledgers or commits are created.
