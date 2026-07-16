# Repository-Wide Full-Text Upgrade Audit

## Purpose

This audit prevents abstract-only or source-page-only records from being treated as full-text curated evidence. A record is upgraded only after the complete article has been reviewed at experiment level and the corresponding observations, claims, links, boundaries, consensus profiles, and generated exports have been refreshed.

## Upgrade standard

A paper may be labeled `PASS 3 COMPLETE` only when all applicable items are complete:

- Full article obtained from an authoritative source or user-supplied copy.
- Experimental groups, controls, species, injury model, timing, dose, route, and sample size extracted.
- Figure/table/results provenance recorded for each observation.
- Quantitative results and statistics extracted where reported.
- Author claims kept separate from empirical observations.
- Contradictory, neutral, and adverse findings retained.
- Abstract-derived placeholder rows replaced rather than merely relabeled.
- B-module evidence links and consensus boundaries refreshed.
- Processed JSON and SQL exports regenerated and validation rerun.

`SOURCE-PAGE`, `ABSTRACT-LEVEL`, and generated `Abstract / saturated A tracker` rows remain explicitly lower confidence until these requirements are met.

## Initial repository audit

### Module 1A / 1B — lesion architecture

Status: mixed full-text and lower-access evidence.

Known lower-access records include abstract-level chronic lesion-zone, MRI, white-matter, scaffold-repair, and other legacy papers. Module 1B correctly labels abstract/source-page contributions and should retain those boundaries until individual full texts are reviewed.

Priority: upgrade the remaining abstract-level papers that directly support consensus statements, especially lesion compartments, white matter, chronic resection/reconstruction, and human imaging.

### Module 2A / 2B — biomaterials and scaffold repair

Status: substantial abstract-level backlog.

Module 2A contains many `PASS 3 ABSTRACT-LEVEL` records. Module 2B explicitly states that its extraction confidence is mostly abstract-level first pass. These records must not be upgraded by status substitution alone because combination therapies require experiment-level separation of scaffold, cell, cargo, lesion preparation, and outcome effects.

Priority: full-text upgrade the translational anchors, scaffold-only comparators, negative/neutral functional studies, and papers carrying the eight Module 2B consensus profiles.

### Module 3A / 3B — immune and myeloid modulation

Status: consensus-ready first pass, but many Module 3B rows were generated from abstract-level tracker metadata.

Priority: upgrade all papers supporting timing-sensitive depletion, myeloid corralling versus fibrosis, polarization markers, inflammasome/cell-death pathways, debris/lipid handling, and immune-delivery systems. Marker, cell-identity, route, timing, and phase fields are mandatory.

### Module 4A / 4B — cell transplantation and graft integration

Status: consensus-ready first pass with broad abstract-level limitations.

Priority: clinical and large-animal studies; neural graft connectivity experiments; product identity/manufacturing; graft survival versus host-graft relay; remyelinating versus neuronal products; and scaffold/cell combination comparators. Safety and adverse-event extraction must be completed before raising clinical confidence.

### Module 5A / 5B — axon regeneration, remyelination, and white-matter repair

Status: substantial abstract-metadata first pass.

Module 5B explicitly warns that its rows preserve evidence direction and topic placement rather than quantitative effects. Full-text upgrades must distinguish regeneration, sprouting, spared fibers, remyelination, debris clearance, relay formation, compensation, and behavioral recovery.

Priority: papers carrying tract-regeneration claims and the remyelination boundary, especially experiments requiring axon tracing, lesion-completeness controls, electron microscopy/g-ratio, lineage evidence, conduction, and circuit necessity.

### Module 6A — human chronic SCI pathology and translational imaging

Status: active corpus-building module; no 6B consensus layer yet.

Priority: full-text human pathology and imaging extraction with cohort selection, injury chronicity, neurological level/severity, acquisition protocol, lesion metric, tract/segment, and outcome association. Consensus drafting should wait for linked full-text evidence.

## Required completion report

For each module, the final upgrade report should provide:

| Module | Total primary papers | Full-text complete | Source-page only | Abstract only | Inaccessible | B-layer refreshed | Exports validated |
|---|---:|---:|---:|---:|---:|---|---|
| 1 |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |  |

## Integrity rule

A full-text upgrade is a scientific re-curation pass, not a global search-and-replace operation. When a full article cannot be legally or technically accessed, the record must remain labeled with its actual access level and be placed in an explicit retrieval queue.