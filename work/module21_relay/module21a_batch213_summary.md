# Module 21A batch 213 summary

## Scope

Batch 213 contains exactly the 25 requested currently queued Module20A pairs
`M20A-EXT-1703` through `M20A-EXT-1727`, in the submitted order. Pair labels
are preserved exactly, including the two multi-component Fraser/NPNT labels
and the FSHB subunit label. Only the batch-213 review TSV and this summary
were written; no Module20A or Module21A ledgers were modified and no commit was
created.

## Disposition

- 5 reviewed relay candidates: Fn1-Itga9, Fn1-Robo4, Fn1-Tshr,
  Fras1_Frem2_Npnt-Itga8_Itgb1, and Frs3-Fgfr1. The SDC2-dependent
  matrix-context record is kept function-only rather than promoted to a
  direct FN1-SDC2 edge.
- 2 reviewed binding-only records: Fn1-Mag and Fshb-Fshr.
- 2 reviewed function-only records: Fn1-Plaur and Fn1-Sdc2.
- 1 reviewed unresolved composite boundary: Fras1_Frem1_Npnt-Itga8_Itgb1.
- 15 explicit no-evidence boundaries: Fn1-Flt4, Fn1-Il17rc, Fn1-Itga2,
  Fn1-Itga6, Fn1-Nt5e, Fn1-Tnfrsf11b, and Fshb paired with Adcyap1r1,
  Adrb2, Adrb3, Gpr20, Gpr84, Pth1r, Ramp2, Ramp3, or Tshr.

No terminal TF endpoint is assigned. FSH-induced CREB literature was not
transferred to isolated FSHB, and the FN/ROBO4, FN/TSHR, Fraser/NPNT, and
FGFR1/FRS3 records do not contain a validated exact-pair terminal-TF assay.

## Evidence handling

Direct molecular associations, receptor-proximal intracellular relays, and
downstream functional outputs are separated in `relation_type` and
`evidence_layer`. Positive primary anchors include FN-EIIIA-alpha9beta1
matrix assembly and lymphatic valve morphogenesis (PMID:19686679), FN-MAG
affinity association (PMID:11423128), FN-Robo4 endothelial co-complex and
c-Src/barrier context (PMIDs:16481322 and 22241990; PMCID:PMC3252370),
FN-TSHR extracellular-matrix association (PMID:11981027),
TG2-FN/SDC2-dependent matrix deposition (PMID:20929862), Fraser-complex/
NPNT-alpha8beta1 ligand presentation (DOI:10.1083/jcb.201203065;
PMCID:PMC3365501), FGFR1-FRS3 docking/relay context (PMID:16421190), and
the intact FSH-FSHR complex in which the FSH-specific beta subunit contributes
to the binding interface (PMID:15662415; PMCID:PMC5514322).

The FN1-Itga2 and FN1-Itga6 rows retain primary integrin-specificity
comparators showing collagen-alpha2beta1 or laminin-alpha6beta1 rather than
an exact FN1 edge. The FSHB-Adcyap1r1 row retains a reverse-direction
PACAP/ADCYAP1R1-to-Fshb transcription study as a boundary, not as ligand
evidence. The two Fraser composites are not conflated: the primary study
tests Fras1/Frem2/QBRICK with NPNT, while the submitted Fras1/Frem1/Npnt
composite remains unresolved.

Searches covered exact symbols and aliases across PubMed, PMC, publisher
pages, Europe PMC, Reactome/KEGG leads, and relevant receptor-family or ECM
comparators. Search URLs are retained on no-evidence rows. Expression,
co-occurrence, generic family signaling, reverse-direction regulation, and
pathway-only findings were not promoted to direct molecular edges.

## Validation targets

The TSV must contain exactly 25 data rows and the exact 13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model,
assay_or_perturbation, relation_type, evidence_layer, pathway_branch,
confidence, limitations, terminal_TF`

Validation targets are exact requested row order and labels, unique review IDs
and pairs, populated required fields, allowed confidence vocabulary, and
literal `null` in every `terminal_TF` cell. No ledgers, frozen LR release,
or Module20A manifest are modified by this batch.
