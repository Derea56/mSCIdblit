# Module 21A LR handoff and extraction scope

Generated from frozen LR manifest `module20a-lr-release-2026-08-14` at
`2026-08-14T13:01:57+00:00`.

## Frozen Module 20A boundary

- Comparison universe: **6116** rows
- Source-backed LR union: **5906** unique pairs
- Comparison-only rows excluded from LR release: **210**
- CellChat-full pairs: **3379**
- LIANA-consensus pairs: **3989**
- Source commit: `83cef801a7e0436916f0623e0c33a46df9050908`

The frozen LR release is an input boundary for Module 21A. It does not imply
that a ligand–receptor pair activates every downstream relay edge. Module 21A
must separately extract intracellular evidence and preserve assay, species,
cell-model, branch, and perturbation context.

## Existing seed

The first-pass Module 21A packet contains 57 relay edges, 14 grouped evidence
records, and 17 perturbation records across nine priority families. It remains
an audit-layer seed until node identity and branch semantics are reconciled.

## Extraction order

1. Reconcile receptor-complex names in the Module 20A release with Module 21A
   receptor entry nodes.
2. Extract primary evidence for the explicit family gaps in
   `module21a_extraction_queue.tsv`.
3. Keep direct molecular edges separate from pathway-complex and functional
   output edges.
4. Record negative or boundary evidence explicitly; do not fill gaps by
   pathway analogy.
5. Materialize SQL only after the evidence and node-identity audit passes.

The queue is intentionally family-level for this pass. Each extracted edge
should retain a stable evidence ID and link back to the LR snapshot only as
its upstream receptor/ligand context.

## Current extraction progress

After batch 231, all 5,906 frozen Module20A pairs remain represented in
the audit coverage and Module22A handoff tables. The current audit layer has
2,740 reusable pathway groups and 5,647 detailed evidence records. Exactly
5,690 pairs have been reviewed and 216 remain queued; 257 pair-level rows
carry provisional terminal-TF candidates for separate Module22A validation.

Batches 176–177 added 50 reviewed rows: 34 relay candidates, 2 binding-only
rows, 8 explicit no-evidence boundaries, and 6 unresolved rows. Batches 178–179
added a further 50 reviewed rows: 36 relay candidates, 5 binding-only rows,
1 function-only row, 7 explicit no-evidence boundaries, and no unresolved rows.
Eight
provisional TF handoffs are now represented in these two batch windows:
STAT3 for IL10–IL10RA/IL10RB; RELA/p65 for RETN–TLR4, S100A8–TLR4,
S100A9–TLR4, and SAA1–TLR2; TCF/LEF for RSPO1/3–FZD8; and NFATC1 for
SEMA6A–PLXNA2. Batches 180–181 added a further 50 reviewed rows: 20 relay candidates, 3
binding-only rows, 3 function-only rows, 11 explicit no-evidence boundaries,
and 10 unresolved rows. No new terminal-TF assignment was added. The batch
evidence includes FGF receptor-specificity, FGG–integrin, irisin–integrin,
GDF/BMP/Activin receptor-complex, GDF15–GFRAL, HGF–MET, IL-10/IL-17/IL-20/IL-1/
IL-25, TNF/TNFSF, VEGF/WNT, and INHBC boundary cases. Receptor-complex,
pathway, and functional outputs remain distinct, and no direct molecular edge
was inferred from a pathway-only or functional-only result.

Batches 182–183 added a further 50 WNT-family rows: 3 bounded relay
candidates, 1 unresolved case, and 46 explicit no-evidence boundaries. The
positive rows are restricted to WNT1–FZD8/LRP6 receptor-complex/function
precedent, WNT1–RYK Frizzled-coupled coreceptor evidence, and WNT10B–FZD6/LRP6
receptor-proximity/function evidence. Generic WNT pathway, beta-catenin,
FZD-family, or LRP-family results were not transferred to untested composite
edges, and no terminal TF was assigned.

Batches 184–185 added a further 50 WNT-family rows: 4 bounded receptor-proximal
relay candidates and 46 explicit no-evidence boundaries. The positive rows are
restricted to WNT11–FZD4, WNT11–FZD7, WNT11–MuSK/Unplugged, and WNT16B–FZD5/LRP6
contexts with species, isoform, receptor-association, and model limitations
preserved. No terminal TF was assigned, and generic WNT pathway or component
evidence was not transferred to unresolved composites.

Batches 186–187 added a further 50 WNT-family rows: 38 explicit no-evidence
boundaries and 12 unresolved FZD-level relay boundaries. None of these rows
supports an isolated WNT–FZD–LRP5/6 ternary claim or a terminal TF endpoint;
component and comparator evidence remains documented only as a search boundary.

Batches 188–189 added a further 50 WNT-family rows: 6 bounded relay candidates,
1 binding-only row, 11 unresolved cases, and 32 explicit no-evidence boundaries.
The positive evidence is limited to WNT3A–FZD8–LRP6 soluble-fragment ternary
complex precedent and WNT5A receptor-context relay or binding observations;
WNT4/WNT6 composite and WNT3A/WNT4/WNT6 FZD/LRP boundaries remain unresolved
or unassigned. No terminal TF was assigned, and generic WNT pathway,
beta-catenin, receptor-family, or comparator evidence was not transferred to
untested exact composites.

Batches 190–191 added 50 broader external-review records: 18 relay candidates,
7 binding-only rows, 9 function-only rows, 13 unresolved cases, and 3 explicit
no-evidence boundaries. Thirty-six of these records had pre-existing Module21A
coverage; their prior evidence and pathway-reuse references were retained
alongside the new review records. Fourteen previously queued pairs advanced to
reviewed status (6 relay candidates, 4 function-only, 3 binding-only, and 1
unresolved). The batch evidence covers SST/SSTR pharmacology, tachykinin
receptor signaling, transcobalamin uptake, Cripto/Nodal receptor complexes,
CXCR4-linked functional outputs, TFPI uptake/inhibitory branches, thyroglobulin
handling, and TGF-beta/integrin boundaries. No terminal TF was assigned, and
pathway or functional observations were not used to infer direct molecular
interactions.

Batches 192–193 advanced 50 previously queued CellChat-remaining pairs: 20
relay candidates, 10 binding-only rows, 1 function-only row, 3 unresolved
cases, and 16 explicit no-evidence boundaries. The reviewed families include
adenosine transporter/receptor contexts, BMP receptor complexes, chemokine and
atypical-chemokine receptors, CNTN/CNTNAP2, CSF1R, and EGFR. Receptor-family,
expression, pathway, uptake, and phenotype evidence was retained only at its
appropriate layer; no terminal TF was assigned.

Batches 194–195 added 50 previously queued pairs: 33 relay candidates, 3
binding-only rows, 3 function-only rows, and 11 unresolved receptor-context
cases. The review covered EREG/ERBB, FLRT/UNC5 and ADGR guidance receptors,
GDF/BMP/Nodal receptor complexes, IL-17/IL-20/IL-22-family cytokine complexes,
IL-36, IL-5/IL-6, activin/inhibin, NGF-receptor aliases, LGALS9–HAVCR2, MSTN,
and NRXN–ADGR adhesion. Twelve provisional terminal-TF handoffs (STAT-family
and SMAD2/3 candidates) were added for Module22A validation; no TF was inferred
from pathway or phenotype evidence alone.

Batches 198–199 added 50 previously queued external-review pairs: 34 relay
candidates, 7 binding-only rows, 3 function-only rows, 4 scavenging-only rows,
and 2 explicit no-evidence boundaries. The review covered ADAM/adhesion and
protease contexts, adrenomedullin and adenosine GPCRs, adiponectin receptors,
agrin/LRP4/MuSK, melanocortin receptors, albumin uptake, ALK/AMH, angiopoietin
and ANGPTL branches, and integrin or endothelial outputs. Two provisional
terminal-TF handoffs (SMAD1/5/8 and CTNNB1) were added for Module22A review;
uptake, scavenging, and extracellular adhesion findings remain distinct from
intracellular relay evidence.

Batches 200–201 added 50 previously queued external-review pairs: 24 relay
candidates, 6 scavenging-only rows, 6 function-only rows, 6 binding-only rows,
2 unresolved cases, and 2 explicit no-evidence boundaries. The review covered
ANGPTL4/integrin and syndecan branches, annexin/FPR and ROBO4 contexts,
adrenomedullin and apelin GPCRs, apolipoprotein uptake and LRP/TREM2 receptors,
AVP, BMP2/BMP10, calcitonin/CCK, chemokine receptors, CD200/CD200R, and CD22.
One provisional STAT3 handoff was added for Module22A validation; scavenging,
uptake, and Fc/receptor-complex observations remain separate from intracellular
relay evidence.

Batches 202–203 added 50 previously queued immune-adhesion, guidance, and
matrix-receptor pairs: 27 relay candidates, 18 binding-only rows, 1
function-only row, and 4 explicit no-evidence boundaries. The review covered
PD-L1/CD80 and PD-1, CD28/CD80-CD86, CD47/SIRPA, CD200/CD200R, cadherin and
integrin adhesion, CLCF1 receptor complexes, CNTN/NRP/PTPR guidance systems,
and collagen–integrin or collagen–proteoglycan contexts. One provisional STAT3
handoff was added for Module22A validation; extracellular adhesion and matrix
binding were not promoted to intracellular relay evidence without supporting
perturbation.

Batches 196–197 added 50 previously queued pairs: 24 relay candidates, 8
binding-only rows, 4 function-only rows, 8 unresolved cases, and 6 explicit
no-evidence boundaries. The review covered PDGF/PDGFR, prostaglandin and
VEGF-receptor branches, TGF-beta complexes, SEMA7A-integrin, TAC4/TACR1,
WNT5B/FZD, A2M/LRP1, ADAM-family adhesion or protease contexts, and related
guidance-receptor pairs. ATF2 and CREB were recorded as provisional terminal-TF
handoffs for separate Module22A validation; no direct TF endpoint was inferred
from pathway or phenotype evidence alone.

Batches 204–205 added 50 previously queued matrix, adhesion, neuropeptide, and
GPCR-context pairs: 13 relay candidates, 13 binding-only rows, 1 function-only
row, and 23 explicit no-evidence boundaries. The review covered DDR/collagen
and collagen–integrin branches, COLQ–MuSK, COMP–ITGA5, COPA receptor-context
rows, cortistatin receptor families, Cp/CRH signaling, and CRHR1/CRHR2. Two
provisional terminal-TF handoffs (PEA3 and CREB) were added for Module22A
validation; matrix binding, receptor-family pharmacology, and phenotype-only
findings were not promoted to direct intracellular edges.

Batches 206–207 added 50 previously queued pairs: 23 relay candidates, 7
binding-only rows, 1 scavenging-only row, and 19 explicit no-evidence
boundaries. The review covered CRH receptor alternatives, CRISP2/CATSPER1,
CRP/OLR1, CSF1/CSF2/CSF3 receptor branches, CSPG4–integrin, CTF1/gp130-LIFR,
CTHRC1/FZD/ROR2, CXCL12–SDC4, decorin–EGFR/MET, DHH coreceptors, and
DKK/Kremen/LRP contexts. One provisional STAT3 handoff was added for Module22A
validation; family-level WNT/DKK, pathway, and extracellular matrix evidence was
not transferred to untested direct intracellular edges.

Batches 208–209 added 50 previously queued pairs: 19 relay candidates, 18
binding-only rows, 7 function-only rows, 4 unresolved cases, 1 scavenging-only
row, and 2 explicit no-evidence boundaries. The review covered DKK4/LRP6,
DCC/desmosomal cadherin adhesion, IL-35/IL-27 receptor complexes, endothelin
and Eph receptor families, EGF accessory contexts, ENTPD1/purinergic branches,
EPO, EREG/ERBB3, F10/F3, and related signaling or extracellular handling. Five
provisional terminal-TF handoffs (STAT1/STAT4, STAT1/STAT3, NANOG, STAT3, and
STAT5) were added for Module22A validation; adhesion, binding-only, and
functional output evidence remain separated from direct intracellular edges.

Batches 210–211 added 50 previously queued coagulation, lipid, FADD/FAS,
adhesion, semaphorin, FGF, and receptor-context pairs: 12 relay candidates, 8
binding-only rows, 4 scavenging-only rows, 15 unresolved cases, and 11 explicit
no-evidence boundaries. The review covered F10/F11/F12/F13/F2/F7/F8,
FABP5/RXRA, FADD death-receptor branches, FAM3 ligands, FARP2/PLXNA, FASL,
FAT4/DCHS1, fibulin/fibrillin integrin contexts, and FGF1/FGF10. One
provisional STAT3 handoff was added for Module22A validation; coagulation,
uptake, matrix binding, and death-complex evidence remain layer-separated.

Batches 212–213 added 50 previously queued FGF, FGG, fibronectin, FSHB, and
receptor-context pairs: 15 relay candidates, 10 binding-only rows, 3
function-only rows, 2 unresolved cases, and 20 explicit no-evidence
boundaries. The review covered FHF/FGFR1 and endocrine FGF branches,
FGL1/EGFR/LAG3, FLT3L/FLT3, FN1 receptor contexts, FSHR and FSHB receptor
alternatives, Fraser/NPNT–integrin complexes, and FGF receptor-specificity
boundaries. No terminal TF was assigned; receptor-family, matrix-binding, and
functional evidence remained separate from exact intracellular relay claims.

Batches 214–215 added 50 previously queued FSHB, follistatin, galanin,
GAS6/TAM, gastrin, Gc/LRP2, and GDF receptor-complex pairs: 21 relay
candidates, 1 binding-only row, 1 scavenging-only row, 5 unresolved cases, and
22 explicit no-evidence boundaries. The review covered FST/FSTL5, galanin
receptor alternatives, GAS6/AXL/MERTK/TYRO3, GDF1/GDF10/GDF11/GDF2/GDF3
receptor complexes, and Gc-mediated uptake. Two provisional terminal-TF
handoffs (CREB and SMAD1/5/8) were added for Module22A validation; receptor
family, uptake, and matrix or complex evidence remain layer-separated.

Batches 216–217 added 50 previously queued GDF, GDNF, GH/GHR, GHRH, GIP,
GPC3, HLA/MHC, orexin, HGF, and haptoglobin contexts: 25 relay candidates,
4 binding-only rows, 3 scavenging-only rows, 1 function-only row, 10
unresolved cases, and 7 explicit no-evidence boundaries. Three provisional
terminal-TF handoffs (STAT5, CREB, and HHEX) were added for Module22A
validation; MHC presentation, uptake, receptor-family, and complex evidence
remain distinct from direct intracellular relay claims.

Batches 218–219 added 50 previously queued haptoglobin/HSPG2, IAPP, ICAM,
ICOSL, IGF/IGFBP, Hedgehog, and IL-11 through IL-21 receptor-complex pairs:
27 relay candidates, 18 binding-only rows, 2 scavenging-only rows, 1
function-only row, and 2 unresolved cases. Nine provisional cytokine TF
handoffs (STAT3, STAT4, STAT3/STAT4, STAT6, and STAT5 candidates) were added
for Module22A validation; uptake, adhesion, receptor-family, and complex
evidence remain separated from direct intracellular relay claims.

Batches 220–221 added 50 previously queued cytokine, growth-factor, hormone,
adhesion, and extracellular-matrix pairs: 33 relay candidates, 11 binding-only
rows, and 6 function-only rows. The review covered IL-4/5/6/7/9/11/33/34,
INS/INSL/RXFP, JAG1/CD46, KISS1/KISS1R, KITL/KIT, L1CAM/laminin, LEP/LEPR,
galectin/LGI, LHB/LHCGR, LIF, LTA/LTB, LTF, MATN1, and MDK receptor branches.
Ten provisional STAT handoffs were added for Module22A validation; hormone,
adhesion, matrix-binding, and receptor-complex evidence remain layer-separated.

Batches 222–223 added 50 previously queued midkine, MFG-E8, MIF, MMRN2,
NCAM/NLGN/NRXN, Nodal, neuropeptide, natriuretic, NPY, and NRG2 receptor pairs:
32 relay candidates, 6 binding-only rows, 11 function-only rows, and 1
explicit no-evidence boundary. JUN and STAT1/RELA were added as provisional
Module22A handoffs; neuronal adhesion, matrix binding, receptor-family, and
functional output evidence remain separate from direct intracellular relay
claims.

Batches 224–225 added 50 previously queued NRG2, neurexin/neuroligin,
neurotrophin, netrin, neurotensin, OSM/OXT, PCSK9, PD-L2, plasminogen,
prolactin, and prokineticin pairs: 25 relay candidates, 9 binding-only rows, 6
function-only rows, 9 scavenging-only rows, and 1 unresolved case. Four
provisional terminal-TF handoffs (STAT3, STAT5, and CREB candidates) were added
for Module22A validation; neuronal adhesion, uptake, receptor-family, and
functional output evidence remain distinct from direct intracellular relay
claims.

Batches 226–227 added 50 previously queued prokineticin, TAM/PSAP, PTH/PTHLH,
pleiotrophin, PYY, RARRES2/RBP4/REN1, RGMA/RGMB, relaxin, RPS19, and RSPO
contexts: 41 relay candidates, 3 binding-only rows, 2 function-only rows, 1
scavenging-only row, 2 unresolved cases, and 1 no-downstream-evidence case.
Provisional terminal-TF handoffs were added for RELA, CTNNB1, SOX9, ERF,
STAT3/STAT5, CREB, and TCF/LEF-family reporter endpoints for separate Module22A
validation; receptor-complex, uptake, species-specific, and functional-output
evidence remain distinct from direct intracellular relay claims.

Batches 228–229 added 50 previously queued RSPO, RTN4, S100/SAA, SCUBE2,
SECTM1, selectin, semaphorin, SERPINE1/SERPINF1, SFRP2, SFTPA/SFTPD, and SHH
contexts: 35 relay candidates, 4 binding-only rows, 6 function-only rows, 4
unresolved cases, and 1 explicit no-evidence boundary. Provisional terminal-TF
handoffs were added for TCF/LEF family, RELA, EGR1, MYC/YAP, NFATC3, GLI1, and
NKX2-2/OLIG2 endpoints for separate Module22A validation. RSPO/WNT, semaphorin
receptor-complex, scavenger/inhibitory TLR, and SHH coreceptor evidence remain
layer-separated and were not generalized across receptor families.

Batch 231 added 25 previously queued SPP1/integrin, TGFB1/2/3 receptor-complex,
TGM2, and THBS1 contexts: 8 relay candidates, 2 binding-only rows, 5
function-only rows, 1 scavenging-only row, 8 no-downstream-evidence rows, and 1
unresolved case. No terminal-TF handoff was added. Canonical TGFBR1/TGFBR2
complexes, accessory TGFBR3/ENG/SDC2/VASN branches, latent-TGF-beta integrin
activation, matrix adhesion, and uptake remain separate evidence layers; queued
subunit labels were not promoted to standalone receptors.
