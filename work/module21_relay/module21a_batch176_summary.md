# Module 21A evidence review — batch 176

## Scope and deliverables

This review is bounded to filtered queue ordinals 3851–3875 and contains exactly the 25 requested queue rows, in the supplied order. The raw review is in [module21a_batch176_review.tsv](/Users/derea/Documents/SCI/mSCIdblit/work/module21_relay/module21a_batch176_review.tsv).

The TSV header is exactly:

```text
review_id	pair	status	stable_citations	species	cell_type_model	assay_or_perturbation	relation_type	evidence_layer	pathway_branch	confidence	limitations	terminal_TF
```

Queue order reviewed:

```text
M20A-LIANA-REMAINING-0122 Fgf20 Fgfr1
M20A-LIANA-REMAINING-0123 Fgf20 Fgfr2
M20A-LIANA-REMAINING-0124 Fgf21 Klb
M20A-LIANA-REMAINING-0125 Fgf23 Fgfr3
M20A-LIANA-REMAINING-0126 Fgf3 Fgfr1
M20A-LIANA-REMAINING-0127 Fgf3 Fgfr2
M20A-LIANA-REMAINING-0128 Fgf8 Fgfr1
M20A-LIANA-REMAINING-0129 Fgf9 Fgfr2
M20A-LIANA-REMAINING-0130 Fgf9 Fgfr3
M20A-LIANA-REMAINING-0131 Fgg Itga2b
M20A-LIANA-REMAINING-0132 Fgg Itgb3
M20A-LIANA-REMAINING-0133 Fndc5 Itgav
M20A-LIANA-REMAINING-0134 Fndc5 Itgb5
M20A-LIANA-REMAINING-0135 Gdf1 Acvr1b_acvr2a_cfc1
M20A-LIANA-REMAINING-0136 Gdf1 Acvr1b_acvr2b_cfc1
M20A-LIANA-REMAINING-0137 Gdf1 Acvr1c_acvr2a_cfc1
M20A-LIANA-REMAINING-0138 Gdf10 Acvr1b_acvr2a
M20A-LIANA-REMAINING-0139 Gdf11 Acvr1b_acvr2b
M20A-LIANA-REMAINING-0140 Gdf15 Gfral
M20A-LIANA-REMAINING-0141 Gdf2 Acvrl1_bmpr2
M20A-LIANA-REMAINING-0142 Gdf3 Acvr1b_acvr2a_cfc1
M20A-LIANA-REMAINING-0143 Gdf3 Acvr1b_acvr2b_cfc1
M20A-LIANA-REMAINING-0144 Gdf3 Acvr1c_acvr2a_cfc1
M20A-LIANA-REMAINING-0145 Gdf5 Bmpr1a_bmpr2
M20A-LIANA-REMAINING-0147 Gdf5 Ror2
```

Validation: 25 data rows, 13 columns per row, unique review IDs, populated stable-citation and limitations fields, and `terminal_TF=null` for all rows. No Module20A file, shared register, or Git history was modified.

## Outcome counts

- `reviewed_relay_candidate`: 18
- `reviewed_binding_only`: 2
- `reviewed_unresolved`: 2
- `no_evidence_boundary`: 3

The three no-evidence rows are Fgf23–Fgfr3, Gdf10–Acvr1b_acvr2a, and Gdf5–Ror2. Their `evidence_layer` value is the normalized literal `no_evidence_boundary`, consistent with the raw TSV.

## Evidence-layer handling

Binding/activation, receptor-proximal relay, and downstream pathway/function were recorded as separate semicolon-delimited layers. Of the 25 rows, 14 contain all three layers, four contain binding plus receptor-proximal relay only, four contain binding only, and three are explicit no-evidence boundaries.

Pathway descriptions are contextual consequences of the cited perturbation or functional studies; they were not used to infer a direct ligand–receptor edge. Composite queue labels were preserved as composite biology:

- FGF receptor rows distinguish FGFR splice forms, especially c versus b isoforms.
- KLB is recorded as an FGF21 specificity co-receptor; the signaling kinase is an FGFR.
- FGG rows are supported for the intact alphaIIb-beta3 heterodimer and gamma-chain motif, not an autonomous ITGA2B or ITGB3 receptor.
- FNDC5 rows refer to processed irisin and the complete alphaV-beta5 heterodimer, not intact FNDC5 or an isolated integrin subunit.
- Activin/Nodal and BMP/GDF rows retain type-I/type-II receptor-complex and CFC1/coreceptor requirements.
- Gdf5–Ror2 remains unresolved because ROR2 modulation of BMPR1B/GDF5 signaling is not direct GDF5–ROR2 binding.

No terminal transcription factor was assigned. SMAD, MAPK, FAK/SRC, RET, or other downstream pathway activity was not promoted to a terminal TF assignment.

## Primary evidence anchors

The review uses stable primary-research identifiers in the TSV, including:

- FGF receptor specificity and developmental signaling: PMCID:PMC2080618; DOI:10.1016/j.devcel.2004.12.002; PMID:7592624; PMID:8619928; PMID:8576175; PMID:16384934; PMCID:PMC2582917.
- FGF21/KLB and FGF23 receptor discrimination: PMID:17452648; PMID:18064602; PMID:18187602; PMID:18753255; PMCID:PMC3135830; DOI:10.1007/s00223-011-9501-5.
- Fibrinogen gamma-chain and alphaIIb-beta3: PMID:6460044; PMID:3584243; PMID:16051597; PMCID:PMC2518716; DOI:10.1083/jcb.104.6.1655; DOI:10.1074/jbc.M506289200.
- Irisin/integrin signaling: PMID:30550785; PMCID:PMC6298040; DOI:10.1016/j.cell.2018.10.025.
- GDF1/GDF3 Activin/Nodal complexes: PMID:12514096; PMCID:PMC195969; DOI:10.1101/gad.1041203; PMID:24798330; PMCID:PMC4067217; DOI:10.1242/dev.02210; PMID:40360531; PMCID:PMC12075709; DOI:10.1038/s41467-025-59673-7.
- GDF11, GDF15, GDF2/BMP9, GDF5, and the GDF5–ROR2 boundary: PMCID:PMC187472; PMID:28257634; PMID:31315975; PMID:28846097; PMID:28953886; PMID:31535977; PMID:22622516; PMCID:PMC3409742; PMID:17311849; PMID:8702914; PMID:15890363; PMID:17989347; DOI:10.1016/j.jmb.2005.04.015; DOI:10.1111/j.1365-2443.2004.00799.x.

All limitations are recorded row-by-row in the TSV, including splice-form dependence, composite-receptor assignment, model/species transfer, redundancy, incomplete exact-pair reconstitution, and the absence of a validated terminal TF.
