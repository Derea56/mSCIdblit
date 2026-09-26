# Spinal cord injury context pack

This is the first populated spinal-cord-injury evidence overlay for mSCIdblit,
now expanded with context-rich protein-expression records.
It is a separate release layer: the pinned Module 20B–24B mechanism graph is
read only for stable identifier resolution and is not rewritten or duplicated.

## Current status

Release 0.5.24 contains 760 dataset observations from the mSCS evidence stores:

- 110 protein/phosphoprotein observations selected from the curated
  `mSCS/data/derived/phosphorylation_support_observations.tsv` view and joined
  back to exact records in `mSCS/data/flow_protein/flow_protein.sqlite`.
- 633 additional directly measured, source-extracted non-phosphorylated or
  total-protein
  observations selected from the canonical flow-protein store. The selection
  excludes phosphoprotein/active-form duplicates, ambiguous or inaccessible
  extraction states, reporter/activity-only assays, inferred timepoints, and
  records without a measured value or reported direction.
- 17 epigenomics observations from
  `mSCS/data/epigenetic/epigenetic.sqlite`, preserving occupancy, accessibility,
  histone, methylation, and RNA-modification context where reported.

Each observation retains its source record key, artifact SHA-256, source
locator, study/context fields, and dependency group. Context profiles preserve
species, injury model, injury severity, injury level, sex, post-injury
timepoint, tissue, lesion distance, cell population, sample scope, condition,
and perturbation status when reported. Missing values remain unknown or
unreported; they are not converted into negative evidence. The release uses
`dataset_observation` only. It does not fabricate external context-matched
observations or inferred bridges.

There are 382 included exact stable-node links and 378 unresolved staging links.
Unresolved observations are retained at module boundary `21B` solely as a
review scope, with no graph-edge, partial-route, route-confidence, or numeric
modality-weight promotion. Downstream protein measurements support the
measured protein state only; they do not establish upstream ligand/receptor
causality.

This refinement applies 216 study/timepoint protein context curation rows from
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
- `../../scripts/build_sci_context_pack.py` — reproducible importer/curator.
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
