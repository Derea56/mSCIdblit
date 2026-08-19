# Module 22A: Transcription-Factor Target Programs and Cell-State Effector Architecture - Regulatory-Effector Corpus Building Tracker

## Overview

This module curates the receiver-side logic linking transcription factors to target programs, effector genes, and state outcomes. It is the mechanism layer that lets `mSCS` move from upstream signaling hypotheses to predicted receiver-cell changes.

**Status**: FIRST PASS COMPLETE / READY FOR CURATION AUDIT.

## Current first-pass checkpoint

- All 274 provisional Module 21A TF handoffs plus all 5,632 no-terminal-TF
  handoffs reviewed across 61 focused batches, four large partitions, and
  validated retry sub-batches.
- 5,906 validated evidence records retained with stable citations.
- 5,733 deduplicated TF-to-target/program edge keys, with supporting evidence and
  upstream handoff IDs joined at the edge layer.
- 85 direct-TF-binding, 50 TF-target-regulation, 2,048 program-association, 275
  phenotype-association, and 3,448 downstream-pathway/function boundary records.
- No Module 22A handoffs remain queued; every edge retains supporting evidence
  and every handoff is represented in the evidence register.

## Core Questions

- Which TFs are known to regulate which injury-relevant target programs?
- Which TF-target relationships are direct versus broader program associations?
- Which target programs are most relevant for astrocytes, endothelial cells, microglia, fibroblasts, and oligodendroglial states?
- Which TF-program links are species-specific or context-restricted?

## Priority Receiver Programs

- reactive astrocyte programs
- inflammatory astrocyte programs
- complement-associated glial programs
- stress-response / AP-1 programs
- IFN/IRF programs
- STAT3-associated wound-repair or border-forming programs
- endothelial barrier and inflammatory relay programs
- fibroinflammatory ECM programs
- oligodendrocyte / OPC survival-differentiation programs

## Required Extraction Objects

- TF identity
- target gene or target program label
- direct binding/support versus program association
- cell-type and context scope
- phenotype linkage where available
- species support and evidence tier

## Handoff Goal

Produce a curated TF-to-program layer so `mSCS` can answer not just “which TF changed?” but “what state outcome would that TF shift plausibly drive?”
