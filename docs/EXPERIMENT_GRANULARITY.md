# Experiment Granularity Guide

The experiment is the fundamental evidence unit. Use this guide when deciding whether source material should become one `Experiment`, multiple `Experiment` records, or multiple `Observation` records inside one experiment.

## Default Rule

Create one `Experiment` for one interpretable comparison:

- one control condition
- one intervention or contrast condition
- one injury context
- one experimental paradigm
- one figure/table/results locus when possible

Multiple measured outcomes from that comparison become multiple `Observation` records.

## Timepoints

Use one experiment when the design is the same and only the measurement time changes. Store each timepoint as a separate observation with `timepoint_postinjury_days`.

Create separate experiments when the timepoint changes the biological intervention or cohort definition, such as acute treatment versus chronic treatment.

## Dose Groups

Use separate experiments for each dose when each dose is compared directly against the same control and interpreted independently.

Use observations within one experiment only when the paper presents dose as a continuous measurement series and does not treat each dose as a separate comparison.

## Sex, Strain, or Species Stratification

Create separate experiments when sex, strain, or species is a primary comparison or changes the experimental cohort.

Use notes or controlled vocabulary links when sex/strain is background metadata and not analyzed separately.

## Multi-Arm Studies

Split multi-arm studies into pairwise experiments when the paper makes distinct claims for each arm. Reuse the same control description, and make the intervention description specific to each arm.

Example:

- vehicle versus scaffold
- vehicle versus scaffold plus cells
- scaffold versus scaffold plus cells

## Figure Panels

A figure panel is not automatically an experiment. It becomes an experiment only if it represents a distinct comparison.

Use `figure_panel_reference` on `Experiment` or `Observation` to preserve exact source location.

## Qualitative Observations

Qualitative findings are valid observations when the source explicitly reports them. Record the literal phrase in `raw_observation_text` or `source_quote`, use `observation_value` for the shortest faithful statement, and set `extraction_confidence`.

Do not infer a quantitative value from an image unless the paper reports it.
