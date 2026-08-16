# Module 21A batch 225 review summary

## Scope

Batch 225 reviews exactly the 25 currently queued Module20A pairs supplied in
the request. Ligand and receptor labels are preserved exactly, and the review
uses the required 13-column schema. Binding or activation, receptor-proximal
relay, and downstream pathway or function are represented as separate evidence
layers; pathway and functional findings were not used to infer a direct
molecular interaction.

## Disposition

- 25 data rows; exact requested order and labels; 13 columns per row.
- 12 `reviewed_relay_candidate` rows: OSM-gp130/OSMR, OXT-OXTR, PD-L2-PD-1,
  podoplanin-CLEC-2, PGLYRP1-TREM1, PlGF-FLT1, uPA-uPAR, PNOC-OPRL1,
  PRL-PRLR, PRLH-PRLHR, PROC-EPCR, and PROK1-PROKR1.
- 8 `reviewed_scavenging_only` rows: OSTN-NPR3, PCSK9-APLP2, PCSK9-CD36,
  PCSK9-CD81, PCSK9-LDLR, PCSK9-LRP8, PLA2G10-PLA2R1, and PLG-IGF2R.
- 3 `reviewed_binding_only` rows: OXT-AVPR1A, OXT-AVPR1B, and OXT-AVPR2.
- 2 `reviewed_function_only` rows: PLG-PLGRKT and PLTP-ABCA1.
- 0 unresolved rows and 0 no-evidence boundaries.

## Evidence highlights and boundaries

OSM-IL6ST/OSMR is supported by gp130-OSMR receptor-complex experiments with
JAK/STAT and Shc1/MAPK branch evidence, while the murine receptor usage is
explicitly species dependent. PD-L2-PD-1 and PDPN-CLEC1B have direct
receptor-proximal checkpoint or hemITAM/Syk/PLCgamma2 evidence. PGLYRP1-TREM1
is supported by direct ligand-complex evidence and TREM1-DAP12-Syk-ERK/STAT3
signaling, with multimerization or peptidoglycan context retained.

PlGF-FLT1, uPA-PLAUR, PNOC-OPRL1, PRL-PRLR, PRLH-PRLHR, PROC-PROCR, and
PROK1-PROKR1 have pathway-level relay evidence, but their cell and receptor
complex limitations remain in the TSV. STAT3 is retained only for the
PGLYRP1-TREM1 microglial study; STAT5 is retained for the PRL-PRLR mammary
pathway; CREB is retained for the PRLH-PRLHR pituitary pathway. These are
provisional Module22A endpoint annotations, not direct receptor-TF edges.

OSTN-NPR3, PLA2G10-PLA2R1, PCSK9 receptor-family pairs, and PLG-IGF2R are
kept at binding, uptake, clearance, or lysosomal-trafficking level. PLG-PLGRKT
is kept at direct plasminogen binding and extracellular plasmin-activation /
migration function. PLTP-ABCA1 is functional transport evidence only; ABCA1
is not treated as a classical ligand-activated receptor and no direct PLTP-ABCA1
binding is inferred. OXT-AVPR1A/1B/2 are cross-reactive pharmacology records
without exact-pair downstream relay validation, whereas OXT-OXTR has a direct
PLC-Ca2+ receptor assay.

## Search boundaries and validation

Searches covered exact symbols and aliases across PubMed, PMC, publisher pages,
and stable DOI or article URLs, prioritizing primary research. The packet
retains stable PMID, PMCID, DOI, and URL citations. No terminal TF was assigned
without an explicit downstream phosphorylation or transcriptional endpoint.

- Confirmed exactly 25 data rows and the exact 13-column header.
- Confirmed unique review IDs and unique submitted pairs.
- Confirmed all required fields are populated and no embedded tabs or extra
  columns are present.
- Confirmed confidence values use the existing Module 21A vocabulary.
- Confirmed `terminal_TF` is literal `null` except `STAT3`, `STAT5`, and `CREB`
  where the cited studies measured those endpoints.
- Only this summary and `module21a_batch225_review.tsv` were written; no
  Module20A ledger, frozen manifest, shared Module21A register, SQL
  materialization, or commit was modified.
