# Module 20B–24B Cross-Module Synthesis

This is a conservative audit-layer synthesis. Shared node names identify
candidate convergence only; they do not establish a complete ligand→TF
path without exact source-backed relay linkage.

Canonical materialization status: **blocked_pending_canonical_schema_and_source_anchor_resolution**.

## Module coverage

| Module | Edges | Evidence | Boundaries | Exportable edges | Non-exportable edges |
|---|---:|---:|---:|---:|---:|
| 20B | 5,906 | 5,906 | 4,780 | 1,126 | 4,780 |
| 21B | 8,171 | 8,120 | 0 | 8,171 | 0 |
| 22B | 5,733 | 5,906 | 5,047 | 723 | 5,010 |
| 23B | 1,230 | 1,630 | 289 | 1,229 | 1 |
| 24B | 151 | 200 | 31 | 151 | 0 |

Boundary counts are evidence-register boundary records; they are not
identical to the number of non-exportable edges when one boundary record
covers multiple edges or when an edge has non-boundary context.

## Candidate convergence nodes

The following entities occur as targets in 21B and as source TF entities in 22B:

`BETA-CATENIN`, `CREB1`, `CSL`, `CTNNB1`, `FOXH1`, `FOXO1`, `GLI1`, `HES1`, `HEY1`, `HIF1A`, `IRF3`, `IRF7`, `JUN`, `LEF1`, `NFATC1`, `NFATC4`, `NFKB2`, `NRF2`, `P65`, `RBPJ`, `RELA`, `RELB`, `SMAD1`, `SMAD2`, `SMAD3`, `SMAD4`, `SMAD5`, `SMAD8`, `STAT1`, `STAT2`, `STAT3`, `STAT4`, `STAT5`, `STAT5B`, `STAT6`

The strict token overlap contains **35** labels. An alias/composite-aware audit expands this to **19** candidate groups:

| Candidate group | 21B relay edges | 22B TF/program edges | Normalization basis | Status |
|---|---:|---:|---|---|
| `CSL` | 1/1 | 3/3 | exact token overlap | candidate_convergence_only |
| `RBPJ` | 2/2 | 3/3 | exact token overlap | candidate_convergence_only |
| `HES1` | 1/1 | 3/3 | exact token overlap | candidate_convergence_only |
| `HES5` | 1/1 | 3/3 | exact token overlap | candidate_convergence_only |
| `HEY1` | 1/1 | 2/2 | exact token overlap | candidate_convergence_only |
| `NFKB2` | 2/2 | 1/1 | explicit token in NFKB2-p100/p52 and NFKB2;RELB labels | candidate_convergence_only |
| `RELA / NF-kB p65` | 7/7 | 34/42 | curated alias group with bounded RELA matching | candidate_convergence_only |
| `SMAD1` | 4/4 | 21/31 | exact token plus composite-branch match | candidate_convergence_only |
| `SMAD2` | 8/8 | 12/14 | exact token overlap | candidate_convergence_only |
| `SMAD3` | 8/8 | 13/15 | exact token overlap | candidate_convergence_only |
| `SMAD4` | 5/5 | 10/12 | exact token overlap | candidate_convergence_only |
| `SMAD5` | 2/2 | 14/22 | exact token plus composite-branch match | candidate_convergence_only |
| `SMAD8` | 2/2 | 11/18 | exact token plus composite-branch match | candidate_convergence_only |
| `SMAD9` | 2/2 | 4/5 | explicit compact composite-branch match | candidate_convergence_only |
| `STAT1` | 20/20 | 8/14 | exact token overlap | candidate_convergence_only |
| `STAT2` | 2/2 | 2/3 | exact token overlap | candidate_convergence_only |
| `STAT3` | 38/38 | 21/25 | exact token overlap | candidate_convergence_only |
| `STAT5B` | 1/1 | 4/5 | exact token overlap | candidate_convergence_only |
| `YAP` | 1/1 | 1/2 | exact token overlap | candidate_convergence_only |

The expanded groups add HES5, NFKB2, RELA/NF-kB p65, YAP, and SMAD9 as a composite-branch candidate while preserving the SMAD1/5/8/9 label. These are review conveniences only; they do not create molecular edges or split unresolved labels.

Counts in the convergence table are shown as **exportable/total audit edges**. Boundary or no-evidence rows remain visible in the denominator but cannot support a traversable path.

These are routing candidates, not asserted end-to-end paths. STAT and SMAD
branches require exact receptor-complex, species, cell-model, perturbation,
and TF evidence alignment before they can be used in simulator traversal.

The overlap includes composite labels such as `RBPJ/CSL` and `SMAD1/5/8`;
these are not silently split into independent molecular edges.

## Cross-module themes

### CMS20-24-T001: Extracellular Handoff Is the Entry Layer, Not a Complete Mechanism

20B defines a large ligand-receptor candidate universe, but its LR evidence does not by itself establish receptor-proximal relay, downstream TF, or cellular-function outcomes.

Boundary: Only the 1,110 high/medium rows pass the conservative 20B export gate. The 183 uncertain direct candidates remain queryable but non-exportable; low, no-evidence, and non-LR classifications remain explicit boundaries.

### CMS20-24-T002: Receptor Complexes Converge on a Limited Relay Vocabulary

21B shows convergence onto JAK/STAT, NF-kappaB/MAPK, GPCR, RTK, TGF-beta/SMAD, WNT, and Notch branches while retaining receptor-complex and ligand-context distinctions.

Boundary: Shared relay nodes such as STAT3 or SMAD4 are candidate convergence points, not proof that every upstream ligand uses the same receptor complex or branch.

### CMS20-24-T003: Terminal TF Evidence Is More Selective Than Pathway Evidence

22B contains many pathway/program and phenotype records, but only the exportable subset should support receiver-state traversal; direct TF binding, target regulation, program association, and phenotype evidence remain separate.

Boundary: Most 22B records are non-exportable or boundary-limited, so pathway presence must not be converted into a terminal TF-target claim.

### CMS20-24-T004: Matrix and Noncanonical Extracellular Systems Are Parallel Inputs

23B and 24B add matrix/adhesion/mechanotransduction and complement/coagulation/lipid/protease records as candidate extracellular inputs alongside soluble cytokine signaling.

Boundary: Exportable means source-backed at the audit layer, not SCI-specific applicability or a complete intracellular route. These layers require explicit receptor, sensor, fragment, compartment, timing, and perturbation evidence before being merged into a shared mechanism.

## Linkage rules

- 20B ligand-receptor edges are not automatically connected to 21B relay edges; exact ligand, receptor complex, species, cell model, and assay context must match.
- 21B relay targets and 22B TF sources define candidate convergence nodes only; shared names do not prove a ligand-to-TF path.
- 23B and 24B matrix, adhesion, complement, coagulation, lipid, and protease edges remain parallel extracellular/contextual layers unless an explicit receptor-to-relay link is source-backed.
- Boundary and no-evidence records remain queryable but are excluded from supported path claims.
- Exportability is a provenance gate, not a claim of universal biology, SCI receiver-cell relevance, or end-to-end pathway completion.

## Required next work

- Resolve stable PMID/PMCID/DOI/URL citations to canonical Paper rows.
- Attach each exportable evidence record to a canonical paper, observation, or author-claim anchor.
- Materialize only after source-anchor and entity/pathway deduplication checks pass.
