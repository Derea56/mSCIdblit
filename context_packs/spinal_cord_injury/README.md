# Spinal cord injury context pack

This is the first populated spinal-cord-injury evidence overlay for mSCIdblit,
now expanded with context-rich protein-expression, metabolomics, and
epigenomics records.
It is a separate release layer: the pinned Module 20B–24B mechanism graph is
read only for stable identifier resolution and is not rewritten or duplicated.

## Current status

Release 0.5.30 contains 910 observations: 765 dataset observations from the
mSCS evidence stores, 61 context-matched external observations, and 84
contextual annotations.

- 112 protein/phosphoprotein observations selected from the curated
  `mSCS/data/derived/phosphorylation_support_observations.tsv` view and joined
  back to exact records in `mSCS/data/flow_protein/flow_protein.sqlite`.
- 629 additional directly measured, source-extracted non-phosphorylated or
  total-protein
  observations selected from the canonical flow-protein store. The selection
  excludes phosphoprotein/active-form duplicates, ambiguous or inaccessible
  extraction states, reporter/activity-only assays, inferred timepoints, and
  records without a measured value or reported direction. Explicit metabolite
  and lipid-mediator records are excluded from this protein count.
- 21 context-matched external protein observations from rat SCI
  neuroproteomics study `PXD003473` (primary source `PMCID:PMC4937511`),
  covering severe T9 contusion, rostral spinal cord, and 24-hour or 7-day
  pooled samples. These retain qualitative source-reported direction without
  inventing scalar values or sample IDs.
- 35 metabolomics observations: 5 selected from explicit SCI metabolite assays in
  the canonical flow-protein store: ATP by LC-MS/MS at 6 weeks after SCI,
  PGE2 and LTB4 by spinal-cord ELISA at 24 hours after SCI, and anandamide by
  LC-MS/MS in dorsal-root-ganglion and below-lesion spinal tissue at day 28.
  The ATP and lipid-mediator values are retained as reported qualitative
  comparisons when exact concentration values were not printed. Their exact
  transcription artifact paths and SHA-256 checksums are retained in the
  observation provenance.
- 30 context-matched external metabolomics observations from `MTBLS6350`
  (`PRJNA895603`; primary source `DOI:10.3389/fnins.2022.1066528`), covering
  3-day T10 lateral-hemisection SCI rat spinal-cord samples and table-level
  log2 fold changes.
- 19 epigenomics observations from `mSCS/data/epigenetic/epigenetic.sqlite`,
  preserving occupancy, accessibility, histone, methylation, and
  RNA-modification context where reported. This includes two exact binary
  feature-status records with their processed peak-artifact paths and
  checksums; their quantitative signal is retained without inferring a
  direction versus control.
- 8 context-matched external epigenomics observations from primary SCI
  literature: four 14-day T10 traumatic-SCI m6A records from `PRJNA791459`
  and four chronic 4-week T10 contusion m6A records from `PMCID:PMC11711147`.
  These retain the reported injury model, spinal-cord tissue, assay, timepoint,
  comparator, feature label, and source locator; the source label `IL-18 bp`
  remains unnormalized because an exact feature identifier was not reported.

All 43 reported epigenetic assay contexts in the mSCS store are retained as
context profiles, including contexts for which no observation-level readout was
selected. Sample IDs remain blank when the source reports only a sample unit,
such as `mouse`, `pooled`, or a group-level replicate count, rather than an
exact sample identifier. The external epigenomics observations use dependency
groups at the study/model/timepoint/tissue level so multiple readouts from one
assay cannot be double-counted.

Each observation retains its source record key, artifact SHA-256, source
locator, study/context fields, and dependency group. Context profiles preserve
species, injury model, injury severity, injury level, sex, post-injury
timepoint, tissue, lesion distance, cell population, sample scope, condition,
and perturbation status when reported. Missing values remain unknown or
unreported; they are not converted into negative evidence. External records
are explicitly labeled `context_matched_external_observation`; no inferred
bridges are included.

The metabolomics audit assessed 10 metabolite-oriented records. Five were
imported. Five remain excluded with explicit reasons: two queued anandamide
rows retain an unresolved flow-cytometry-versus-LC-MS/MS mismatch, ATP FRET is
reserved for imaging, ATP microdialysis is reserved for functional evidence,
and the ATP-synthase protein immunoblot remains protein evidence.

There are 385 included exact stable-node links and 517 unresolved staging links.
Unresolved observations are retained at module boundary `21B` solely as a
review scope, with no graph-edge, partial-route, route-confidence, or numeric
modality-weight promotion. Downstream protein measurements support the
measured protein state only; they do not establish upstream ligand/receptor
causality.

This refinement applies 245 study/timepoint protein context curation rows from
exact primary-source locators, including injury model, level, severity, sex,
timepoint, treatment, and sample-scope refinements where the inspected source
explicitly establishes them. The overrides do not replace reported
perturbation or treatment fields, and do not fill sex or injury severity where
the inspected source does not explicitly establish it.
Their source URLs, locators, curation notes, and checksum are retained in
`protein_context_curation_overrides.tsv` and the generated provenance fields.

## Assessed evidence gaps

The current mSCS spatial pilot was assessed but excluded: GSE269377 is a
healthy/mutant-FUS spinal-cord spatial dataset without an explicit SCI injury
model. It is therefore not treated as negative SCI spatial evidence. No
curated transcriptomic, standalone imaging, perturbation-only, or functional
observation table was imported in this release. Perturbation and treatment
fields are preserved when reported in selected protein or epigenetic records;
immunofluorescence remains represented as a protein assay context.

The current generic mechanism dependency is recorded in
[`context_manifest.json`](context_manifest.json). The manifest pins the
mechanism release consumed by the first SCI overlay and records the policy
that context evidence cannot create or promote a generic graph edge.

## Files

- `context_manifest.json` — release metadata, dependency, modality plan, and
  counts.
- `contexts.tsv` — controlled context profiles, from the SCI scope to exact
  study/sample contexts.
- `observations.tsv` — modality-native or explicitly derived SCI observations.
- `mechanism_links.tsv` — reviewed links from observations to stable route,
  node, edge, pathway, or module identifiers in the pinned mechanism release.
- `audit_report.json` — counts by modality, study, injury model, timepoint,
  perturbation, observation status, evidence role, link status, and unresolved
  mapping reason.
- `protein_context_coverage.tsv` — per-context protein coverage and missing
  context fields for refinement.
- `protein_context_gap_audit.json` and `protein_context_gap_candidates.tsv` —
  reproducible accounting of canonical protein records not imported and the
  reason each remains outside the current selection rule.
- `protein_context_curation_overrides.tsv` — exact, study-level context
  refinements with source locators; this is an input to the reproducible
  builder, not a manually edited derived table.
- `external_protein_context_curation.tsv` — source-located external SCI
  neuroproteomic observations used by the reproducible builder.
- `external_metabolomics_context_curation.tsv` — source-located external SCI
  metabolomics observations used by the reproducible builder.
- `external_epigenomics_context_curation.tsv` — source-located external SCI
  epigenomics observations used by the reproducible builder.
- `perturbation_design_curation.tsv` — source-preserving, staged normalization
  of intervention-bearing context profiles. It is generated from the
  perturbation-design audit, is not ingested as evidence, and requires source
  review before any intervention target, route, dose, duration, or comparator
  label is promoted.
- `spatial_localization_audit.tsv` and `spatial_localization_audit.json` —
  source-preserving classification of existing IF/IHC localization,
  co-localization, cell-assignment, structural, and spatial-transcriptomic
  context records. These are audit-only and do not create proximity relations.
- `sci_module_spatial_reconciliation.tsv` and
  `sci_module_spatial_reconciliation.json` — source-preserving reconciliation
  of explicit spinal-cord/SCI context in the canonical Module 20B-24B phase-2
  extraction ledger against the existing SCI context pack. Exact
  PMID/PMCID/DOI matches and module-only candidates are reported; no rows are
  imported by this audit.
- `../../scripts/build_sci_context_pack.py` — reproducible importer/curator.
- `../../scripts/build_sci_perturbation_curation.py` — reproducible generator
  for the staged perturbation-design ledger.
- `../../scripts/audit_sci_spatial_localization.py` — reproducible audit of
  extractable spatial/localization information.
- `../../scripts/audit_sci_module_spatial_reconciliation.py` — reproducible
  crosswalk of module evidence to existing SCI context and spatial audit rows.
- `../../scripts/audit_sci_protein_context_coverage.py` — reproducible protein
  context refinement audit.

Regenerate and validate with:

```bash
python3 scripts/build_sci_context_pack.py
python3 scripts/audit_sci_protein_context_coverage.py
python3 scripts/validate_context_pack.py context_packs/spinal_cord_injury
```

## Evidence-layer policy

| Layer | Intended use | Initial rule |
|---|---|---|
| Protein/proteomics | Receptor abundance, pathway activation, phosphorylation, cleavage, or output protein | Direct observations can support an exact route stage; downstream protein alone does not establish upstream causality |
| Transcriptomics | Ligand/receptor state, target-gene response, differential expression, and temporal association | Dataset observation; not a replacement for protein activity |
| Spatial | Sender/receiver co-localization, neighborhood, and tissue compartment context | Proximity is contextual and does not establish binding or causal direction |
| Epigenomics | TF occupancy, accessibility, motif, histone, methylation, or m6A context | Direct occupancy may support an exact TF-target claim; other assays remain regulatory context |
| Imaging/histology | Protein localization, cell state, lesion or anatomical context | Link only to the measured feature or reviewed context claim |
| Perturbation | Treatment, knockout, inhibition, rescue, or stimulation response | Preserve intervention, comparator, and output; causal interpretation remains context- and design-dependent |
| Functional/behavioral | Cellular, tissue, or organism-level output | Preserve the readout and its relationship to the route; do not silently convert it to a target-gene claim |

The same source can support several route stages, but it must retain one
source identity and dependency group so mSCS can prevent double counting.

## Population order

1. Register exact study, assay, sample, and artifact provenance.
2. Create the context profile, including species, tissue, injury model,
   timepoint, perturbation, and cell scope when reported.
3. Record observations without inferring missing intermediate states.
4. Link observations to stable mechanism identifiers using the pinned release.
5. Review source scope and context match before marking a link included.
6. Export the pack with a manifest and validation report for mSCS.

No numeric route confidence is stored in this pack.
