# Module 22B low-confidence upgrade and recovery batches 001–022

This document consolidates the 22 Module 22B low-confidence upgrade and
recovery notes issued on 2026-09-02 and 2026-09-03. The original batch files
remain the detailed audit records; this document provides one navigable
release-facing account of the decisions, evidence boundaries, and
reproduction pointers.

The batches enumerate 90 row-level upgrades or recoveries. They do not all
have the same confidence transition: the early batches promote exact
low-confidence rows, while the later recovery batches move selected
no-evidence boundaries into bounded medium program or phenotype associations.
None of these notes authorizes an unsupported terminal TF claim, an inferred
SCI-specific mechanism, or a canonical SQL write.

## Batch index

| Batch | Date | Rows described | Main outcome | Original note |
|---:|---|---:|---|---|
| 001 | 2026-09-02 | 13 | 3 high and 10 medium upgrades | [batch 001](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH001_2026-09-02.md) |
| 002 | 2026-09-02 | 1 | WNT5A–FZD7 bounded functional relay to medium | [batch 002](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH002_2026-09-02.md) |
| 003 | 2026-09-02 | 6 | Five GDF/BMP or GDF1/Nodal rows to medium; one WNT3A ternary-complex row to medium-high | [batch 003](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH003_2026-09-02.md) |
| 004 | 2026-09-02 | 2 | CD30L–CD30 and OX40L–OX40 receptor-pair anchors to medium | [batch 004](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH004_2026-09-02.md) |
| 005 | 2026-09-02 | 1 | SPON2/Mindin–α4β1 integrin complex to medium | [batch 005](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH005_2026-09-02.md) |
| 006 | 2026-09-03 | 1 | WNT10B-dependent FZD6–LRP6 receptor-complex function to medium | [batch 006](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH006_2026-09-03.md) |
| 007 | 2026-09-03 | 2 | S100A8–RAGE and TGF-beta–integrin-αVβ5 functional dependence to medium | [batch 007](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH007_2026-09-03.md) |
| 008 | 2026-09-03 | 1 | Inverse YBX1–NOTCH1 functional relationship to medium | [batch 008](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH008_2026-09-03.md) |
| 009 | 2026-09-03 | 1 | TGF-beta1-induced integrin-β1/αβ1 matrix-adhesion branch to medium | [batch 009](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH009_2026-09-03.md) |
| 010 | 2026-09-03 | 1 | TFF3-induced epithelial-migration branch to medium | [batch 010](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH010_2026-09-03.md) |
| 011 | 2026-09-03 | 1 | GABA-A agonist/antagonist-sensitive MAPK–CREB–BDNF/TrkB function to medium | [batch 011](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH011_2026-09-03.md) |
| 012 | 2026-09-03 | 3 | 5-HT receptor subtype–PKA/CREB program associations to medium | [batch 012](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH012_2026-09-03.md) |
| 013 | 2026-09-03 | 2 | AREG–EGFR-family and BTC–EGFR/ERBB4 signaling to medium | [batch 013](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH013_2026-09-03.md) |
| 014 | 2026-09-03 | 7 | BTLA/HVEM, CD70/CD27, FGF, GDF15, JAG1/NOTCH1, and PDGF-C receptor functions to medium | [batch 014](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH014_2026-09-03.md) |
| 015 | 2026-09-03 | 8 | CXCL12, EFNB2, FGF17b, GDF2, LEAP2, SHH, and VEGF-C receptor functions to medium | [batch 015](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH015_2026-09-03.md) |
| 016 | 2026-09-03 | 8 | CCL28, CD40L, FGF21, GLG1, JAG1, and C3d/C3dg receptor functions to medium | [batch 016](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH016_2026-09-03.md) |
| 017 | 2026-09-03 | 5 | SEMA4D, PEDF, and TGFB1/2/3–TGFBR1/TGFBR2-complex functions to medium | [batch 017](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH017_2026-09-03.md) |
| 018 | 2026-09-03 | 4 | SEMA4A–plexin and PEDF–PLXDC2 receptor functions to medium | [batch 018](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH018_2026-09-03.md) |
| 019 | 2026-09-03 | 8 | SHH, Sema3B, TIMP2, UCN1, UTS2, and VEGF165 receptor functions to medium | [batch 019](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH019_2026-09-03.md) |
| 020 | 2026-09-03 | 6 | SFTPD, SHBG, VEGF-B, and VIP receptor functions to medium | [batch 020](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH020_2026-09-03.md) |
| 021 | 2026-09-03 | 5 | SPARC, TDGF1, LPS/TLR, SLPI, and SERPINE1 bounded associations to medium | [batch 021](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH021_2026-09-03.md) |
| 022 | 2026-09-03 | 4 | BMP6/7, TNF-alpha/WNT, and WNT7A–FZD9/ERK5 program associations to medium | [batch 022](MODULE22B_LOW_CONFIDENCE_UPGRADE_BATCH022_2026-09-03.md) |

## Consolidated evidence policy

Across all batches, the reviewed primary records are used to re-anchor an
exact receptor, receptor-complex, pathway, functional, program, or phenotype
association. The records do not automatically establish:

- purified ligand–receptor binding when the experiment only shows
  receptor-dependent function or proximity;
- a unique receptor subunit or complex stoichiometry when multiple assemblies
  remain possible;
- a complete intracellular relay or terminal TF occupancy;
- transfer from a comparator model, species, tissue, or cell state to SCI; or
- a canonical SQL materialization.

Negative, wrong-direction, wrong-pair, disputed-binding, non-native-construct,
and no-terminal-TF cases remain bounded rather than being force-promoted.
Processing, isoform, co-receptor, presentation, dosing, model, and
cell-state limitations are retained in the underlying edge and evidence
registers.

## Batch details

### Batch 001 — exact low-tier adjudication

Batch 001 re-adjudicated exact low-tier rows against primary-source Phase-2
review records. It upgraded 13 rows: 3 to high and 10 to medium. Its reported
snapshot was 5,069 exact low edges before and 5,056 after, with 723 exportable
edges after the batch. The batch explicitly kept receptor-complex
substitutions, model/species/SCI transfer, negative evidence, disputed
binding, non-native constructs, and rows without terminal TF evidence bounded.

Historical batch-specific generator scripts were moved to the local archive
described in the repository retention inventory; the original batch notes
retain the generator names used at the time of each run.
Audit ledger: `work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch001.tsv`

### Batch 002 — WNT5A–FZD7

`M22B-E000782` was promoted from low to medium. The cited human
pancreatic-cancer study supports a WNT5A–FZD7 receptor-dependent functional
relay through ABCG2 expression and gemcitabine resistance. The evidence does
not establish purified binding, context-independent generalization, or a
terminal TF-target edge. Source confidence was upgraded to high because the
primary study directly tested the perturbation relationship.

### Batch 003 — GDF/BMP, GDF1/Nodal, and WNT3A

Six exact receptor/program rows were promoted. Five GDF/BMP or GDF1/Nodal rows
move to medium on receptor-panel, reconstitution, or co-receptor-dependent
signaling. The WNT3A–FZD8–LRP6 row moves to medium-high because purified
extracellular fragments reconstitute a ternary complex and directly measure
binding. Native stoichiometry, cellular context, terminal TF claims, and SCI
transfer remain unresolved.

### Batch 004 — TNFSF/TNFRSF receptor-pair anchors

`M22B-E000518` (CD30L/TNFSF8–CD30/TNFRSF8) and `M22B-E000619`
(OX40L/TNFSF4–OX40/TNFRSF4) were promoted to medium. The primary survey
supports the exact receptor-pair anchors in human and mouse reagent panels,
but not the complete TRAF/NF-kappaB relay or a terminal TF target.

### Batch 005 — SPON2/Mindin–α4β1

`M22B-E000673` was promoted to medium using primary mouse immune-cell studies
of the native SPON2/Mindin–α4β1 integrin complex. The row does not assert
standalone ITGA4 binding, purified affinity, a unique intracellular relay, or
a terminal TF target.

### Batch 006 — WNT10B–FZD6–LRP6

`M22B-E000772` was promoted from low-medium to medium. A primary human
prostate-cancer study supports WNT10B-dependent FZD6–LRP6 receptor-complex
association and early canonical beta-catenin activation. The evidence is
proximity/function rather than purified ternary-complex reconstitution, and
receptor stoichiometry, cancer context, SCI transfer, and terminal TF output
remain unresolved.

### Batch 007 — S100A8–RAGE and TGF-beta–integrin-αVβ5

`M22B-E000641` and `M22B-E000706` were promoted to medium. RAGE
neutralization supports S100A8-dependent modulation of PDGF-induced airway
smooth-muscle migration, while integrin-beta5 depletion and rescue support
TGF-beta-dependent ventral stress-fiber and focal-adhesion organization.
Both remain functional-dependence records rather than purified binding or
terminal TF-target edges.

### Batch 008 — YBX1–NOTCH1

`M22B-E000802` was promoted from low-medium to medium. A primary human THP-1
study under 1,4-benzoquinone exposure supports an inverse YBX1–NOTCH1
functional relationship linked to BCL2/BCL3 expression and apoptosis. Direct
binding, TF occupancy, chemical-context generalization, and SCI transfer are
not established.

### Batch 009 — TGF-beta1 and integrin-beta1

`M22B-E000703` was promoted from low-medium to medium. Primary human WI-38
and A549 studies support the TGF-beta1-induced integrin-beta1/alpha-beta1
surface-expression and matrix-adhesion branch. The row does not claim direct
TGFB1–ITGB1 binding, a universal heterodimer assignment, a resolved SMAD
relay, or a terminal TF target.

### Batch 010 — TFF3 epithelial migration

`M22B-E000697` was promoted from low-medium to medium. CXCR4 and/or CXCR7
blockade suppressed migration in the cited human ocular-surface model, while
TFF3-induced ERK1/2 activation was receptor-independent in that model. The
single-receptor attribution, conflicting later pharmacology, direct-binding
status, and SCI-transfer limits remain unresolved.

### Batch 011 — GABA-A–MAPK/CREB/BDNF/TrkB

`M22B-E000051` was promoted from low to medium. Primary developing-neuron
studies support GABA-A agonist/antagonist-sensitive MAPK and CREB activation,
BDNF induction, and TrkB-dependent CREB phosphorylation. The row does not
claim a specific GABA-A subunit assembly, a universal mature-neuron response,
or a direct CREB target locus.

### Batch 012 — 5-HT receptor–PKA/CREB programs

Three low no-evidence boundaries were recovered as medium program associations:

- `M22B-E000111`: 5-HT1A–PKA/CREB hippocampal neuronal signaling;
- `M22B-E000112`: 5-HT4–PKA/CREB enteric neuronal survival and neurogenesis;
- `M22B-E000113`: 5-HT7–G12/PKA/CREB neuronal transcriptional signaling.

The primary studies establish receptor-dependent CREB pathway function, not
direct CREB occupancy at a target locus. Receptor subtype, tissue/cell state,
dosing, and SCI-transfer limits remain explicit.

### Batch 013 — AREG/BTC EGFR-family signaling

Two low no-evidence boundaries were recovered as medium program associations:
`M22B-E000007` (AREG–EGFR-family ERK/AKT immediate-early growth signaling)
and `M22B-E000008` (BTC–EGFR/ERBB4 receptor activation). The submitted
EGFR–ERBB2 composite is not treated as uniquely resolved, and the studies do
not establish direct AP-1 occupancy or SCI-specific activity.

### Batch 014 — receptor and receptor-complex recovery

Seven rows were recovered as medium program associations:

- `M22B-E000598`: BTLA–HVEM/TNFRSF14 inhibitory immune function;
- `M22B-E000605`: CD70–CD27 T-cell costimulation;
- `M22B-E000611`: FGF1–FGFR4 heparan-sulfate-dependent signaling;
- `M22B-E000616`: FGF8b–FGFR1c splice-form-specific signaling;
- `M22B-E000617`: GDF15–GFRAL–RET receptor-complex signaling;
- `M22B-E000622`: JAG1–NOTCH1 canonical Notch signaling;
- `M22B-E000629`: processed PDGF-C–PDGFRA receptor signaling.

The primary records establish receptor engagement and/or receptor-dependent
function, not terminal TF occupancy. Processing, presentation, complex
composition, model, and SCI-transfer limits remain preserved.

### Batch 015 — vascular, developmental, and scavenging receptors

Eight rows were recovered as medium program associations:

- `M22B-E000606`: CXCL12–ACKR3 atypical beta-arrestin/scavenging function;
- `M22B-E000607`: EFNB2–EPHB4 bidirectional vascular signaling;
- `M22B-E000613` and `M22B-E000614`: FGF17b–FGFR1c/FGFR2c signaling;
- `M22B-E000618`: GDF2–ACVRL1/ALK1 endothelial signaling in a BMPR2 context;
- `M22B-E000624`: LEAP2–GHSR antagonism;
- `M22B-E000630`: SHH–PTCH2–SMO developmental signaling;
- `M22B-E000632`: processed VEGF-C–NRP2/VEGFR3 lymphatic signaling.

Processing, co-receptor, splice-form, topology, model, and SCI-transfer
limitations remain explicit.

### Batch 016 — immune adhesion and endocrine signaling

Eight rows were recovered as medium program associations:

- `M22B-E000601`: CCL28–CCR3 inflammatory receptor function;
- `M22B-E000602`–`M22B-E000604`: CD40L binding/function through three integrin assemblies;
- `M22B-E000615`: FGF21–beta-Klotho–FGFR endocrine signaling;
- `M22B-E000619`: GLG1/ESL-1–E-selectin leukocyte adhesion;
- `M22B-E000623`: JAG1–NOTCH4 endothelial Notch signaling;
- `M22B-E000631`: processed C3d/C3dg–CR2 B-cell coreceptor function.

The records establish engagement and/or receptor-dependent function without
asserting terminal TF occupancy; processing, presentation, co-receptor, model,
and SCI-transfer limits are retained.

### Batch 017 — SEMA4D, PEDF, and TGFBR complex

Five low no-evidence boundaries were recovered as medium program associations:
SEMA4D–CD72, PEDF–PLXDC1, and TGFB1/2/3 through the canonical
TGFBR1/TGFBR2 complex. The records establish receptor or receptor-complex
engagement and function, not terminal TF occupancy or unresolved complex
stoichiometry.

### Batch 018 — SEMA4A and PEDF receptor function

Four low no-evidence boundaries were recovered as medium program associations:
SEMA4A through PLXNB1/2/3 and PEDF–PLXDC2. The records support receptor
engagement and receptor-proximal function, while plexin/RND1, membrane-context,
oligomerization, model, and SCI-transfer limitations remain explicit.

### Batch 019 — developmental, inflammatory, and vascular receptors

Eight low no-evidence boundaries were recovered as medium program associations:
SHH–GPC1, Sema3B–NRP2/Plexin-A1, TIMP2–α3β1, UCN1–CRHR2,
UTS2/UTS2B–UTS2R, and VEGF165–NRP2. The primary records establish exact
receptor or receptor-complex engagement and function, not terminal TF
occupancy. Coreceptor, processing, isoform, complex, model, and SCI-transfer
limits remain explicit.

### Batch 020 — collectin, endocrine, and neuropeptide receptors

Six low no-evidence boundaries were recovered as medium program associations:
SFTPD–SIRPA, SHBG–GPRC6A, SFTPD–LAIR1, VEGF-B–NRP1, and VIP–PAC1/VPAC1
receptor function. Collectin presentation, receptor-complex, isoform, model,
and SCI-transfer boundaries are preserved.

### Batch 021 — bounded program and phenotype associations

Five low-confidence rows were recovered as bounded medium program/phenotype
associations: SPARC–FGF2/FGFR1 signaling, TDGF1/Cripto–Nodal receptor-complex
signaling, *P. gingivalis* LPS/TLR2-TLR4–ANGPTL2 inflammatory context,
SLPI–PLSCR1/4–CD4 membrane-complex modulation, and SERPINE1/PAI-1
matrix-adhesion modulation. The batch notes report a historical post-batch
working-register snapshot of 4,995 low-confidence, 505 medium, 547
medium-high, and 3,853 high-confidence edges; those counts are retained here
as batch history rather than asserted as current release counts.

### Batch 022 — BMP, WNT, and WNT7A–FZD9 programs

Four bounded program associations were recovered from low to medium:

| Edge | Recovered bounded claim | Primary source |
|---|---|---|
| `M22B-E000499` | BMP6/7 uses ACVR1A, ACVR2A, and BMPR2-associated signaling for ID1/DLX5/IBSP osteoblastic output; the BMPR1B–BMPR2 composite is removed. | PMID 18436533; PMCID PMC3258927 |
| `M22B-E000728` | TNF-alpha/Msx2-associated WNT7A/WNT3A paracrine signaling is linked to beta-catenin/TCF osteogenic output; LDLR is model context only. | PMID 17932314; PMID 15841209; PMCID PMC1077175 |
| `M22B-E000789` | WNT7A–FZD9 activates an ERK5-dependent PPARgamma antitumor program; the LRP5 composite is removed. | PMID 16835228 |
| `M22B-E000790` | WNT7A–FZD9 activates an ERK5-dependent PPARgamma antitumor program; the LRP6 composite is removed. | PMID 16835228 |

The unsupported receptor-composite interpretations remain excluded. The
batch records that canonical SQL materialization was not performed.

## Reproduction and audit trail

Each original batch note records its generator and, where applicable, its
audit ledger. The batch generators are named in the original notes and write
to the corresponding `work/module22b_low_confidence_upgrade_audit/` paths.
The consolidated document is a documentation index and does not replace
those machine-readable ledgers or the Module 22B edge and evidence registers.

All original notes state that canonical SQL materialization was unchanged or
not performed. Any future canonical materialization must rerun the applicable
register-level validation and preserve the evidence and context boundaries
described above.
