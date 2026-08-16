# Module 21A batch 226 review summary

## Scope

Batch 226 reviews exactly the 25 currently queued Module20A pairs supplied for
this batch. Ligand and receptor labels are preserved exactly, and the TSV uses
the required 13-column schema. Binding or activation, receptor-proximal relay,
and downstream pathway or function are represented as separate evidence
layers. Pathway-level or functional observations were not used to infer a
direct molecular interaction.

## Disposition

- 25 data rows in the exact requested order and labels.
- 20 `reviewed_relay_candidate` rows.
- 2 `reviewed_unresolved` rows: Pros1-Axl and Psap-Gpr37l1.
- 1 `reviewed_binding_only` row: Pth2-Pth1r.
- 1 `reviewed_no_downstream_evidence` row: Pthlh-Pth2r.
- 1 `reviewed_scavenging_only` row: Psap-Sort1.
- 20 literal `terminal_TF=null` values.
- 5 provisional terminal-TF annotations supported by explicit endpoint evidence:
  `RELA` for the PROS1-AXL glioblastoma model, `CTNNB1` for the PTH-PTH1R/LRP6
  complex, `SOX9` for TIP39-PTH2R chondrocyte signaling, `ERF` for a
  PTPRZ1-dependent PTN hematopoietic model, and `STAT3;STAT5` for
  holo-RBP4-STRA6 signaling.

## Evidence highlights

The three PROK rows are supported by primary receptor binding and signaling
assays for both prokineticins at PROKR1/PROKR2, with Gq/11, Gi/o, calcium,
ERK, and arrestin branches kept context-specific. PROK2-PROKR2 also has a
mouse genetic migration phenotype, but no terminal TF was inferred from that
pathway-level result.

PROS1 activates MERTK and TYRO3 in receptor-isolated or native-cell studies,
with PtdSer, gamma-carboxylation, ERK/AKT, efferocytosis, and survival
limitations retained. PROS1-AXL is explicitly unresolved because a GBM model
reported PROS1-dependent AXL phosphorylation and NF-kappaB/p65 activation,
whereas purified-receptor and MEF activation profiling found PROS1 inactive
as an AXL agonist.

PSAP-GPR37 is supported by binding, Gi/o-sensitive cAMP inhibition, ERK
phosphorylation, and astrocyte protection. PSAP-GPR37L1 retains both the
positive deorphanization study and a later negative ligand-rechallenge study,
so it is not promoted beyond unresolved context. PSAP-SORT1 is kept as
lysosomal sorting/uptake evidence only; sortilin is not treated as a canonical
signal-transducing receptor in this row.

PTH-PTH1R and PTHrP-PTH1R have direct class-B GPCR activation evidence. PTH-
PTH2R is supported by human-receptor pharmacology with species dependence.
TIP39/PTH2 activates PTH2R but binds PTH1R without productive activation and
can antagonize PTH/PTHrP signaling. PTHrP-PTH2R is retained as an explicit
negative/selectivity boundary. PTH-LRP6 is recorded as a receptor-complex
relay: PTH binds PTH1R, which recruits and phosphorylates LRP6; no direct
PTH-LRP6 ligand-binding claim is made.

PTN-ALK has direct receptor binding and kinase-pathway evidence. PTN-
alpha-v-beta-3 is a receptor-complex/adhesion edge with PTPRZ1-dependent
beta3/Src signaling and migration, not a standalone integrin kinase claim.
PTN-PTPRZ1 retains phosphatase inhibition, Src/ALK/RAS-MEK-ERK, and
cellular-function evidence with isoform and chondroitin-sulfate limitations.

PYY activates Y1, Y2, and Y5 receptor systems, but the strength and depth of
evidence differ: Y1 has an EGFR/PKC/ERK epithelial-growth relay, Y2 has
heterologous cAMP/Ca2+ evidence, and Y5 has receptor-interface and chimeric
G-protein calcium-flux evidence without a resolved native-cell output. QRFP-
QRFPR and RARRES2-CMKLR1 have primary GPCR binding and G-protein/second-
messenger or ERK evidence. RBP4-STRA6 is a transporter-signaling receptor
edge with holo-RBP4/retinol, CRBP1/LRAT, JAK2, STAT3/STAT5, and SOCS3
dependencies preserved.

## Search boundaries and validation

Searches covered exact symbols and aliases across PubMed, PMC, publisher
pages, DOI records, and relevant pathway/receptor resources, prioritizing
primary research. Stable PMIDs, PMCIDs, DOIs, or a stable JCI URL are retained
in the TSV. No terminal TF was assigned unless a cited study explicitly
measured a downstream TF or transcriptional endpoint. Engineered receptor,
chimeric-G-protein, species, peptide-processing, and co-receptor limitations
are recorded in the row-level limitations.

- Confirmed exactly 25 data rows and the exact 13-column header.
- Confirmed 25 unique review IDs and 25 unique pair labels.
- Confirmed all required fields are populated and no embedded tabs or extra
  columns are present.
- Confirmed confidence values use the existing Module 21A vocabulary.
- Confirmed `terminal_TF` is literal `null` except for the five explicit
  endpoint annotations listed above.
- Confirmed the frozen Module20A manifest SHA-256 remains
  `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.
- Only this summary and `module21a_batch226_review.tsv` were written; no
  shared Module21A register, Module20A ledger, frozen manifest, SQL file, or
  commit was modified.
