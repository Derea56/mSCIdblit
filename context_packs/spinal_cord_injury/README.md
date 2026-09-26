# Spinal cord injury context pack

This is the initial scaffold for spinal-cord-injury-specific evidence linked
to the neutral mSCIdblit mechanism graph. It is intentionally a separate
release layer: Module 20B–24B mechanism records remain reusable for other
diseases and are not rewritten with SCI-specific claims.

## Current status

This pack is a contract scaffold, not a populated SCI evidence release. It
contains no study-level observations or mechanism links yet. Empty tables are
kept with their headers so importers and validators can be developed against
the final shape without fabricating identifiers or measurements.

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

## Planned evidence layers

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
