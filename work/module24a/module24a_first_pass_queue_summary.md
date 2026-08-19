# Module 24A First-Pass Queue Summary

Date: 2026-08-18

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

- `module24a_evidence_register.tsv` — 169 supported evidence records plus 31 explicit no-evidence boundaries;
- `module24a_edge_register.tsv` — 151 supported context, receptor, relay, or function edges;
- `module24a_perturbation_register.tsv` — remains empty pending perturbation normalization;
- `module24a_saturation_matrix.tsv` — 189 reviewed audit rows, including 18 legacy Module 18 reuse anchors, 21 B004 rows, all 50 B001 rows, all 50 B002 rows, and all 50 B003 rows, with unresolved receptor and processing gaps preserved.

## Controlled SQL staging materialization

The validated audit registers now have a dedicated staging materialization at
`work/module24a/module24a_signaling_staging.sql`. It creates only
`module24a_*` staging tables and preserves queue provenance, pathway/complex/
functional edge rows, edge-to-evidence links, explicit binding/proximal-relay/
downstream layer labels, and no-evidence boundaries. It does not write the
Module 20A LR tables, core simulator-facing `SignalingEdge` rows, or any prior
module ledger.

Preflight results before materialization:

- exact TSV widths: pass for queue, batch plan, edge, evidence, perturbation, and matrix registers;
- unique IDs: 171 queue, 151 edge, 200 evidence, and 189 matrix IDs;
- edge keys: no duplicates;
- evidence coverage: all 151 edges have at least one qualifying non-boundary evidence record, with 169 edge/evidence associations;
- unresolved cases: all 31 no-evidence boundaries remain explicit and unlinked to edges;
- SQL assertions: encoded for 171 queue rows, 4 batches, 151 edges, 200 evidence records, 189 matrix rows, zero perturbation rows, and complete cross-register coverage.

The staging SQL was materialized successfully in an isolated local PostgreSQL
16.14 database named `mscitdb_module24a` on port `55433`, using the fresh
validation cluster at `/private/tmp/mscitdb_module24a_pg_batch008`. The transaction loaded all seven
`module24a_*` staging tables and passed the embedded integrity assertions. The
database contains only the Module 24A audit-layer staging tables; Module 20A
tables were not touched.

## Saturation tranche 013

The duplicate/read-only synchronization tranche is documented in
`module24a_saturation_batch013_summary.md`. It promoted 10 rows linked to
existing validated edges without creating duplicate evidence or edge records.

## Saturation tranche 012

The evidence-disposition tranche is documented in
`module24a_saturation_batch012_summary.md`. It promoted 16 existing,
evidence-backed SCI or comparator-context rows to
`REVIEWED_SUPPORTED_WITH_PAIR_LIMIT` without adding duplicate edges or
evidence records.

## Saturation tranche 011

The matrix-disposition tranche is documented in
`module24a_saturation_batch011_summary.md`. It promoted the validated PGE2
EP2/EP4 and S1P S1PR1/2/3 branches to `REVIEWED_SUPPORTED_WITH_PAIR_LIMIT`
without creating duplicate edges or evidence records.

## Saturation tranche 010

The targeted resolution-lipid tranche is documented in
`module24a_saturation_batch010_summary.md`. It added a rat FPR2/ALX spinal
anti-nociceptive comparator while preserving the SCI, human GPR32, C4b-CR2,
and Hc-C5aR1 boundaries.

## Saturation tranche 009

The targeted complement-fragment tranche is documented in
`module24a_saturation_batch009_summary.md`. It added direct human iC3b-CR4
binding evidence while preserving the intact C3-to-CR4, C4b-to-CR2, and Hc-
C5aR1 boundaries.

## Saturation tranche 008

The targeted SCI/comparator tranche is documented in
`module24a_saturation_batch008_summary.md`. It added LTB4 release/PMN
functional context, direct iC3b-CR3 fragment binding, rat SCI C3/CR3
neuropathic-pain association, and mouse SCI MMP2/MMP9 pathway/function. BLT2,
C5aR2 in SCI, intact C3 receptor assignments, and exact MMP-to-receptor
activation remain explicit boundaries.

## Saturation tranche 007

The targeted SCI-specific tranche is documented in
`module24a_saturation_batch007_summary.md`. It added distinct Klk6/neurosin-
PAR2 receptor-proximal and astrocyte-function records, SCII kinin-receptor
induction context, and bradykinin-B2R pharmacology and neuroprotective
function. Generic proteases, direct BDKRB1 binding, and endogenous kallikrein
processing remain explicit boundaries.

## Saturation tranche 005

The targeted second-pass tranche is documented in
`module24a_saturation_batch005_summary.md`. It added six layer-separated edges
and six primary-paper evidence records for BDKRB1/des-Arg9-bradykinin after SCI,
the C3a/C3aR1-NF-kB p65/Nrf2/UCHL1 neural-stem-cell relay, and human
RvD1-GPR32 pharmacology/function. BDKRB1 and GPR32 boundaries were narrowed,
not erased; purified binding, endogenous processing, SCI-specific receptor
causality, and rodent orthology remain explicit limits. The Nrf2-to-UCHL1 ChIP
finding remains a Module 22A TF-context handoff rather than a direct 24A edge.

## Saturation tranche 006

The targeted comparator tranche is documented in
`module24a_saturation_batch006_summary.md`. It added C5a/C5a-desArg to
C5L2/C5aR2 binding and ligand-clearance function, C3d-to-CR2 structural
binding, and factor Xa/PAR2 activation under tissue-factor/cofactor
conditions. These additions resolve comparator evidence only; C5aR2/C5L2
SCI causality, intact C3-to-CR2 activation, and the SCI factor Xa activating
protease remain explicit boundaries.

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

These are recorded in `module24a_evidence_register.tsv` and `module24a_edge_register.tsv`. The new B001 tranche promotes APC-EPCR/PAR1, bradykinin-BDKRB2, C3a-C3aR1, C5a-C5aR1, and thrombin-PAR1; thrombin-PAR3/PAR4 remains comparator-only. Factor Xa-to-PAR2, BDKRB1, and noncognate complement assignments remain explicit no-evidence boundaries.

The follow-on B001 tranche validated hemokinin/tachykinin receptor pharmacology, substance P/Tacr1 SCI function, UDP-sugar/P2Y14 comparator pharmacology, and FAM3D/TAFA5 FPR1/FPR2 comparator relays. Tac1/Tac4 precursor rows were normalized to peptide-derived records; Hc-to-C5aR1 remains unresolved. These comparator edges are retained with low SCI-scope posture and are not silently promoted to SCI-specific function. B001 is complete with all 50 queue candidates reviewed.

## Batch 002 and 003 evidence disposition

Batch 002 added engineered CR2-Crry fragment-targeting and CR2-associated injury-function context while explicitly retaining intact C3-to-CR2, intact C3-to-CR3, intact C3-to-CR4, and C4b-to-CR2 as unresolved. Batch 003 added HMGB1/TLR and S100A8/TLR receptor-proximal boundary relays, ATP/P2X4 pharmacology, CCL2/CCR2 and CCL28/CCR10 downstream function, CCL3/CCR1 context, tenascin-C/TLR4 boundary context, decorin/protease adjacency, and reverse-direction TLR4-to-MMP9 ECM pathway context. Batch 004 added CX3CL1/CX3CR1, CXCL1/CXCR2, CXCL10/CXCR3, CXCL3/CXCR2, and CCN1/SDC4 evidence while retaining comparator-only and unresolved chemokine cases separately. Eighteen explicit no-evidence records now cover the original kinin/PAR/protease gaps plus complement-fragment, DAMP/chemokine, Batch 004, Hc, and B001 duplicate-seed boundaries. These additions do not alter Module 20A LR classifications; chemokine and TLR overlaps are retained as downstream or boundary context. The integrated first pass contains 66 supported edges. PAR1 is supported, PAR3/PAR4 remains comparator-only, factor Xa-to-PAR2 remains unresolved, and tachykinin/P2Y14/FPR comparator edges remain explicitly low SCI-scope where applicable.
Batch 002 added engineered CR2-Crry fragment-targeting and CR2-associated injury-function context while explicitly retaining intact C3-to-CR2, intact C3-to-CR3, intact C3-to-CR4, and C4b-to-CR2 as unresolved. The B002 opening tranche additionally validated PGE2-EP2/EP4, S1P-S1PR1/2/3, and Klk6-PAR1/PAR2 while retaining generic MMP/receptor, BLT2, GPR32, and generic protease substitutions as boundaries. Batch 003 added DAMP/TLR and purinergic/chemokine context, and Batch 004 added chemokine and CCN1/SDC4 evidence while retaining comparator-only and unresolved cases separately. The completed B002 tranche validated Gal-9/TIM-3, resistin-TLR4, ApoC3 particle-level clearance, C1QL2-NRXN3, C1QTNF5-MFRP, Cripto receptor-complex context, CYTL1-CCR2, FLRT3 homophilic adhesion, IL17D-CD93, IL-1/IL1R1:IL1RAP and IL-36/IL1RL2:IL1RAP complexes, LEAP2-GHSR antagonism, and PCDHGC3 barrier function. Existing Module23A FLRT3-ADGRL3/UNC5B and ApoC3-LRP1 boundary records were reused read-only. Twenty-eight explicit no-evidence records preserve direct-pair and accessory-chain limits, including ANGPTL2-TLR4 direct binding, ATP-KCNJ8/TRPM4 extracellular activation, Cripto-ACVR2A, FLRT3-ADGRL1/UNC5C/UNC5D, IL1RAP-PTPRD, and PCDHGC3 self-binding. These additions do not alter Module 20A LR classifications; B002 is complete and the integrated first pass contains 100 supported edges.
Batch 002 added engineered CR2-Crry fragment-targeting and CR2-associated injury-function context while explicitly retaining intact C3-to-CR2, intact C3-to-CR3, intact C3-to-CR4, and C4b-to-CR2 as unresolved. The B002 opening tranche additionally validated PGE2-EP2/EP4, S1P-S1PR1/2/3, and Klk6-PAR1/PAR2 while retaining generic MMP/receptor, BLT2, GPR32, and generic protease substitutions as boundaries. Batch 003 added DAMP/TLR and purinergic/chemokine context, and Batch 004 added chemokine and CCN1/SDC4 evidence while retaining comparator-only and unresolved cases separately. The completed B002 tranche validated Gal-9/TIM-3, resistin-TLR4, ApoC3 particle-level clearance, C1QL2-NRXN3, C1QTNF5-MFRP, Cripto receptor-complex context, CYTL1-CCR2, FLRT3 homophilic adhesion, IL17D-CD93, IL-1/IL1R1:IL1RAP and IL-36/IL1RL2:IL1RAP complexes, LEAP2-GHSR antagonism, and PCDHGC3 barrier function. Existing Module23A FLRT3-ADGRL3/UNC5B and ApoC3-LRP1 boundary records were reused read-only. B003 then validated PCDHGC5, PIANP/PILRA, PTPRD/IL1RAP synaptic complex, WNT5A-ROR2-VANGL2 complex, ANXA2-TLR2, CIRBP-TLR4, decorin-TLR2, DEFB2-TLR4, ficolin-A/TLR4 pathway, HMGB1-TIM-3/TLR2, galectin-9/TLR4 modulation, S100/TLR read-only reuses, and comparator chemokine receptor pharmacology. Thirty-one explicit no-evidence records preserve direct-pair, domain, processing, and species limits. These additions do not alter Module 20A LR classifications; B002 and B003 are complete and the integrated first pass contains 130 supported edges.
Batch 004 queue synchronization is complete. Q0151-Q0164 reuse the existing chemokine receptor comparator, SCI-context, or explicit no-evidence records; Q0165-Q0171 reuse the Module18-derived CCN1/SDC4, LL37/P2X7R, C1q/lipid, P2X7R, P2Y12R/adenosine, and TREM2/debris records. No duplicate edges were created. All 171 Module 24A queue candidates now have reviewed audit dispositions, while the 31 explicit no-evidence boundaries remain preserved.
