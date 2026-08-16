# Module 21A batch 222 review summary

Batch 222 reviews exactly the 25 currently queued Module20A pairs specified by
the request, preserving the submitted IDs and ligand/receptor labels exactly.
The TSV uses the required 13-column schema and separates ligand-receptor
binding or activation, receptor-proximal relay, and downstream pathway or
cellular function evidence.

## Disposition

- 25 data rows; exact requested order and labels; 13 columns per row.
- 11 `reviewed_relay_candidate` rows: MDK-SDC4, MFAP5-NOTCH1,
  MFGE8-ITGB3/ITGB5/PDGFRB, MIF-CD44/CD74 and MIF-EGFR, MST1-MST1R,
  NCAM1-GFRA1, NDP-LGR4, and NELL2-ROBO3.
- 7 `reviewed_function_only` rows: MDK-PTPRZ1, MEPE-PHEX,
  MMRN2-CLEC14A, MYL9-CD69, NCAN-SDC3, and NLGN1-NRXN1/NRXN2.
- 6 `reviewed_binding_only` rows: MDK-SDC1, MMRN2-CD248, MMRN2-CD93,
  NCAM1-ROBO3, NGF-SORCS3, and NID1-PTPRF.
- 1 `no_evidence_boundary` row: NCAM1-FGFR2.

The reviewed total is therefore 24 plus one explicit no-evidence boundary.

## Evidence and search boundary

Searches used exact symbols and aliases across PubMed, PMC, publisher pages,
and structural records, with primary research prioritized. Strong exact or
complex-resolved anchors include MDK-PTPRZ1 and MDK-syndecan binding,
MEPE-ASARM-PHEX inhibition, MFAP5-NOTCH1 co-immunoprecipitation and Notch
outputs, MFGE8-integrin and PDGFRB cross-talk, the MIF-CD74/CD44 complex,
MIF-EGFR antagonism, MMRN2 binding to CD248/CD93/CLEC14A, MSP/MST1R/RON
activation, MYL9-CD69 recruitment, NCAM1-GFRA1 and NCAM1-ROBO3 receptor
associations, NCAN-SDC3 binding, NDP-LGR4 activation, NELL2-ROBO3 activation,
NGF-SORCS3 binding, the laminin-NID1-PTPRF complex, and NLGN1-neurexin
adhesion. Stable PMID, PMCID, DOI, and search-boundary URLs are retained in
the TSV.

NCAM1-FGFR2 is intentionally recorded as `no_evidence_boundary`: the primary
NCAM signaling work resolves an FGFR-dependent pathway without identifying
FGFR2, while the exact FGFR2 study concerns NEGR1 rather than NCAM1. No
family-level NCAM or FGFR result was transferred to the exact pair.

## Relay and terminal-TF handling

Direct binding, receptor-complex organization, receptor-proximal signaling,
and functional output remain distinct in the `relation_type`, `evidence_layer`,
`pathway_branch`, and `limitations` fields. Proteoglycan, adhesion, sorting,
and extracellular-matrix findings were not forced into canonical kinase
relays. The MMRN2, MYL9, NCAN, and neuroligin/neurexin rows therefore retain
functional or complex-level outputs without inventing cytosolic receptor
mechanisms.

Two terminal-TF candidates are retained only where the cited primary studies
measure those downstream endpoints: `JUN` for the inhibitory MIF-EGFR/c-JUN
branch and `STAT1;RELA` for the context-specific MSP/MST1R modulation of
IFN-gamma/LPS responses in primary macrophages. These are downstream endpoint
annotations for Module 22A validation, not claims of direct receptor-TF
interaction. All other rows use literal `null`.

## Validation and file scope

- Confirmed the header has the exact requested 13 columns.
- Confirmed exactly 25 data rows, unique review IDs, unique submitted pairs,
  exact order, populated required fields, and no embedded tabs or extra
  columns.
- Confirmed status values are drawn from the existing Module 21A vocabulary
  and confidence values are valid (`low`, `medium`, `medium-high`, or `high`).
- Confirmed every positive edge has stable supporting evidence and the
  NCAM1-FGFR2 unresolved boundary is explicitly documented.
- Confirmed `terminal_TF` is literal `null` except for the two explicitly
  measured downstream endpoint annotations.

Only `module21a_batch222_review.tsv` and this summary were written. No Module
20A ledger, frozen manifest, shared Module 21A register, SQL materialization,
or commit was modified.
