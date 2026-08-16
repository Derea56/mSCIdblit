# Module 21A batch 218 review summary

Batch 218 reviews exactly the 25 user-specified queued Module20A pairs in the
requested order, preserving the submitted ligand and receptor labels. The TSV
is the authoritative row-level artifact. No Module20A ledger, Module21A
ledger, frozen manifest, SQL table, shared register, or commit was modified;
only the batch-218 TSV and this summary were written.

## Disposition

- 11 `reviewed_relay_candidate` rows: HSPA1A-TLR4, IAPP-CALCR/RAMP3,
  ICAM1-LFA-1/Mac-1, ICAM2-LFA-1, ICOSL-ICOS, IGF1-IGF1R/INSR, and
  IGF2-IGF1R/INSR.
- 10 `reviewed_binding_only` rows: HP-Mac-1 subunit records, ICAM4-integrin
  records except the unresolved alpha4 row, ICAM5-LFA-1 subunit records,
  IGFBP4-LRP6, and IGFBPL1-DCC.
- 2 `reviewed_scavenging_only` rows: HPX-LRP1 and IGF2-IGF2R.
- 2 `reviewed_unresolved` rows: HSPG2-FGFR1 and ICAM4-ITGA4.

## Evidence-layer handling

Binding or activation, receptor-proximal relay, and downstream pathway or
cellular function are encoded separately in the `evidence_layer` column.
Haptoglobin-Mac-1 and ICAM4/ICAM5 records retain complete integrin-complex
binding without inventing autonomous subunit signaling. Hemopexin-LRP1 and
IGF2-IGF2R are retained as scavenging/trafficking relationships rather than
canonical kinase relays. HSPG2-FGFR1 retains the perlecan-bound FGF2/FGFR1
ternary context but is unresolved for a direct autonomous HSPG2-FGFR1 edge.
IGFBP4-LRP6 is an extracellular Wnt-receptor-complex inhibitory interaction,
not a direct activating relay. IGFBPL1-DCC is an extracellular PPI without a
validated DCC signaling output.

## Search boundaries and primary anchors

Searches covered exact symbols and aliases across PubMed, PMC, publisher pages,
and Reactome/pathway leads. Primary anchors include haptoglobin-Mac-1 binding
(PMID:8786317), hemopexin-heme-LRP1 scavenging (PMID:15947085), extracellular
Hsp70-TLR4 signaling (PMID:23043959), perlecan-FGF/FGFR1 ternary signaling
(PMID:11847221; PMID:24509440), AMY3 receptor signaling (PMID:32219220),
ICAM/integrin binding and outside-in studies (PMID:15355350; PMID:19050286;
PMID:8993013), ICOS costimulation (PMID:19915142), IGF receptor isoform
signaling (PMID:10207053; PMID:16239300), IGFBP4-LRP6 inhibition
(PMID:18528331), and IGFBPL1-DCC extracellular interactome validation
(PMID:32822567; PMCID:PMC7440162).

Generic integrin-family, Wnt, IGF, or ICOS pathway evidence was not transferred
to untested exact subunit edges. No terminal transcription factor was assigned:
all 25 `terminal_TF` values are the literal `null` because no pair-specific
endpoint met the Module 22A promotion threshold.

## Validation

- Exactly 25 data rows in the requested order and with the requested labels.
- Exactly 13 tab-separated columns per row.
- Review IDs and pair labels are unique.
- Required fields are populated and contain no embedded tabs.
- Confidence values use the established vocabulary.
- Every `terminal_TF` value is literal `null`.
- No ledgers, registers, SQL outputs, Module20A classifications, or frozen
  manifest files were changed.
