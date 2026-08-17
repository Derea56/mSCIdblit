# Module 24A First-Pass Queue Summary

Date: 2026-08-17

## Scope

Module 24A curates complement, coagulation, kinin, lipid mediator, purinergic/DAMP-adjacent, and extracellular protease relay systems. It must preserve activators, cleavage products, receptors, inhibitors, compartments, and context rather than flattening them into cytokine-style edges.

## Candidate inventory

| Source stream | Targets | Treatment |
|---|---:|---|
| ConnectomeDB complement review slice | 31 | Candidate provenance only; direct activation and downstream relay require primary validation |
| ConnectomeDB DAMP/purinergic/TLR review slice | 26 | Boundary candidates; TLR overlap is retained only for independently supported non-TLR danger routes |
| CellChatDB complement and DAMP/purinergic slices | 38 | Chemokine-only overlap excluded; direct receptor/mediator evidence still required |
| Guide to Pharmacology noncanonical receptor seeds | 55 | Pharmacology candidates; endogenous release, species, receptor activation, and function require primary-paper checks |
| Module 18 read-only reuse candidates | 10 | Existing C1q/lipid, TREM2/debris, ATP/P2X7, P2Y12/adenosine, LL37/P2X7, and CCN1/SDC4 branches |
| Explicit category search gaps | 11 | Coagulation/PAR, kinin, complement anaphylatoxin, eicosanoid, sphingolipid, resolution-lipid, and protease searches |
| **Total** | **171** | **4 batches; maximum 50 targets per batch** |

## Evidence-layer boundary

Every target is reviewed separately for:

1. mediator identity, release, cleavage, or processing;
2. receptor or sensor engagement;
3. receptor-proximal relay or protease-activated signaling;
4. downstream pathway, cellular function, and perturbation-linked phenotype.

Elevated complement, ATP, lipid, DAMP, or protease abundance does not establish receptor engagement. A cleavage product is not interchangeable with its precursor, and a pharmacologic agonist/antagonist is not automatically evidence of endogenous release in SCI.

## Search boundary

Database rows are candidate generators. Module 18 rows are read-only reuse seeds. Primary research papers and exact assays/perturbations are required before promotion. The explicit gap targets document categories not yet supported by a local source anchor; they are not inferred edges.

## Audit-layer registers

The following schemas were initialized before source review and now contain the validated first-pass records:

- `module24a_evidence_register.tsv` — 24 supported evidence records plus 9 explicit no-evidence boundaries;
- `module24a_edge_register.tsv` — 24 supported context, receptor, relay, or function edges;
- `module24a_perturbation_register.tsv` — remains empty pending perturbation normalization;
- `module24a_saturation_matrix.tsv` — 18 reviewed queue rows, with unresolved receptor and processing gaps preserved.

## Batch 001 evidence disposition

The first 24A source audit retained 13 context, receptor, relay, or functional edges from primary SCI and comparator studies:

- C1q/lipid-debris synaptic engulfment;
- myelin debris/TREM2 with timing-dependent PI3K-AKT/DAM outcomes;
- ATP/P2X7R and P2X7R blockade;
- P2Y12R/CD39/CD73/adenosine/A1R/mitophagy;
- extracellular traps/LL37/P2X7R/NF-kB;
- LTB4/BLT1 and leukotriene pharmacology;
- RvD1/RvD3 resolution-function context;
- activated protein C/histone protease adjacency.

These are recorded in `module24a_evidence_register.tsv` and `module24a_edge_register.tsv`. No direct PAR edge was promoted. Three explicit no-evidence boundary records document unresolved kinin, PAR, and protease-to-PAR searches.

## Batch 002 and 003 evidence disposition

Batch 002 added engineered CR2-Crry fragment-targeting and CR2-associated injury-function context while explicitly retaining intact C3-to-CR2, intact C3-to-CR3, intact C3-to-CR4, and C4b-to-CR2 as unresolved. Batch 003 added HMGB1/TLR and S100A8/TLR receptor-proximal boundary relays, ATP/P2X4 pharmacology, CCL2/CCR2 and CCL28/CCR10 downstream function, CCL3/CCR1 context, tenascin-C/TLR4 boundary context, decorin/protease adjacency, and reverse-direction TLR4-to-MMP9 ECM pathway context. Nine explicit no-evidence records now cover the original kinin/PAR/protease gaps plus complement-fragment and DAMP/chemokine candidate boundaries. These additions do not alter Module 20A LR classifications; chemokine and TLR overlaps are retained as downstream or boundary context. No PAR edge was promoted.
