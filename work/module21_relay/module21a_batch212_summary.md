# Module 21A batch 212 summary

## Scope

Batch 212 contains exactly the 25 requested currently queued Module20A pairs,
in the submitted order, from `M20A-EXT-1651` through `M20A-EXT-1702`.
Submitted pair labels are preserved exactly. No Module20A or Module21A ledger,
frozen manifest, or SQL materialization was modified.

## Disposition

- 10 reviewed relay candidates: FGF11/12/13/14-FGFR1, FGF2-NRP1, FGF21-FGFR4, FGF22-FGFR1, FGF23-FGFR2, FGL1-EGFR, and FLT3L-FLT3.
- 8 reviewed binding-only records: FGF2-FGFRL1, FGF2-GPC4, FGF22-FGFRL1, FGF3-FGFRL1, FGF4-FGFRL1, FGF8-FGFRL1, FGL1-LAG3, and FN1-DPP4.
- 1 reviewed function-only record: FGF2-SDC3.
- 1 reviewed unresolved receptor-complex case: FGG-TLR4.
- 5 explicit no-evidence boundaries: FGF21-FGFR2, FGF3-FGFR3, FGF3-FGFR4, FN1-C5AR1, and FN1-CD79A.

No terminal TF endpoint is assigned in this batch. FGF23-FGFR2 reaches PKA/Rap1
and FGF22-FGFR1 reaches presynaptic functional outputs; neither is a measured
terminal TF. FGF2-SDC3 remains functional-only because the cited study did not
isolate direct FGF2-SDC3 molecular binding.

## Evidence handling

The batch keeps the three evidence layers separate. Direct binding or receptor
activation is recorded in `ligand_receptor_binding_or_activation`; measured
proximal relay is recorded in `receptor_proximal_relay`; and pathway or cellular
outputs are recorded in `downstream_pathway_function`. FGF2-GPC4, FGF2-SDC3,
and FGG-TLR4 are deliberately not promoted to direct molecular edges beyond
what their assays establish. FGFRL1 records preserve its kinase-deficient
decoy-receptor role and are not treated as canonical FGFR kinase relays.

Primary anchors include the FHF-FGFR1 study (PMID 37342898), FGFRL1 ligand
binding and decoy work (PMID 19920134), GPC4-FGF2 binding (PMID 11066092),
FGF2-NRP1 proteoglycan-coreceptor work (PMID 39704408), SDC3/FGF2/FGFR1
functional studies (PMID 24937430), endocrine FGF receptor-complex studies
(PMIDs 17452648, 22442730, 35513431), FGF22 receptor-specificity and neuronal
studies (PMIDs 16597617, 27605441, 25926357), FGF23-FGFR2 neutrophil signaling
(PMID 26878171), FGL1-EGFR signaling (PMID 41967236), FGL1-LAG3 binding/function
(PMID 30580966), FLT3L-FLT3 studies (PMIDs 8618433, 8637235, 8816402), and
FN1-DPP4 binding (PMID 2573346).

Search boundaries covered exact symbols and aliases across the existing
Module20A evidence packets, PubMed, PMC, publisher pages, Europe PMC/pathway
leads, and comparator receptor-family literature. For FGF21-FGFR2, FN1-C5AR1,
and FN1-CD79A, no qualifying exact record was retained. For FGG-TLR4, whole
fibrinogen/TLR4 inflammatory evidence was retained only as a receptor-complex
boundary because isolated FGG-chain contact was not demonstrated.

## Validation targets

The TSV contains exactly 25 data rows and the exact 13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

Validation targets are exact requested order and labels, unique review IDs and
pairs, populated required fields, allowed confidence vocabulary, and literal
`null` in every unvalidated terminal-TF field. Only the two Batch 212 files are
written; no commit was created.
