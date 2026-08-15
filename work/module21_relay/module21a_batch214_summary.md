# Module 21A batch 214 summary

## Scope

Batch 214 contains exactly the 25 requested currently queued Module20A pairs
`M20A-EXT-1728` through `M20A-EXT-1752`, in the submitted order, with pair
labels preserved exactly. Only the batch-214 review TSV and this summary were
written. No Module20A or Module21A ledgers were modified and no commit was
created.

## Disposition

- 10 reviewed relay candidates: Fstl1-Dip2a, Gal-Galr1, Gal-Galr2,
  Gal-Galr3, Galp-Galr1, Galp-Galr2, Gas6-Axl, Gas6-Mertk, Gas6-Tyro3, and
  Gast-Cckbr.
- 15 explicit no-evidence boundaries: Fshb-Vipr1, Fst-Bmpr1b, Fst-Bmpr2,
  Fstl5-Ceacam19, Fstl5-Chl1, Fstl5-Cntn5, Fstl5-Gp6, Fstl5-Il6ra,
  Fstl5-Sdk2, Gad1-Grm4, Gal-Adra2a, Gal-Gpr151, Gal-Grm7, Gal-Mtnr1a, and
  Galp-Galr3.

The provisional terminal-TF field is `CREB` only for Gast-Cckbr, based on a
gastrin/CCK-B receptor PKC-Raf1-MEK1-ERK1/2 promoter study that measured CREB
phosphorylation and CREB-dependent chromogranin-A transcription. All other
rows retain literal `null`; no TF was inferred from pathway or phenotype
evidence alone.

## Evidence handling

The strongest direct relay evidence is FSTL1-DIP2A: co-immunoprecipitation and
membrane pull-down support physical binding, DIP2A loss reduces FSTL1 binding
and FSTL1-induced Akt phosphorylation, and endothelial/cardiomyocyte assays
support downstream survival, migration, network formation, and protection
(PMID:20054002; PMCID:PMC2844162; DOI:10.1074/jbc.M109.069468).

Galanin-GALR1/2/3 rows retain receptor-subtype-specific primary assays. GALR1
supports Gi/o-sensitive cAMP inhibition and MAPK activity; GALR2 supports
Gq/11-PLC-Ca2+, Gi, and G12/Rho branches; and GALR3 supports galanin binding
and Gi/Go-linked GIRK activation (PMIDs:8750821, 9281594, 9685625, 9722565,
10980593, 9405385; DOI:10.1021/bi9728405). GALP-GALR1/2 retain in-vitro
binding/G-protein activation, while knockout data show that central GALP
feeding and LH phenotypes are not dependent on either receptor alone. No
GALP-GALR3 activation was accepted.

GAS6-AXL/MERTK/TYRO3 rows retain TAM receptor activation and downstream
signaling with receptor-specific context. GAS6-AXL is supported by receptor
phosphorylation and AKT/MAPK readouts; GAS6-MERTK by MERTK phosphorylation,
AKT/MAPK signaling, and macrophage or drug-resistance assays; and GAS6-TYRO3
by TYRO3 phosphorylation with Shc/B-Raf and PLCgamma/PKCalpha readouts
(PMCID:PMC5686386; PMIDs:28878389, 32681075, 35252828, 35708914, 29382817).
Gamma-carboxylation and phosphatidylserine dependence are retained as
limitations.

GAST-CCKBR retains a receptor-proximal PKC-Raf1-MEK1-ERK branch and explicit
CREB/Sp1 transcriptional output in human AGS-B cells (PMID:17889508;
DOI:10.1016/j.cellsig.2007.08.016), with a separate CCKBR-ERK-p65 breast
cancer context (PMID:30115027; PMCID:PMC6097285). CREB remains provisional for
Module22A validation.

The no-evidence rows preserve exact-pair PubMed and Europe PMC search URLs.
Family-level FST/BMP, FSTL5 extracellular annotations, neural adhesion,
GAD1/GRM4 co-expression, shared GPCR coupling, and generic galanin receptor
evidence were not transferred to untested direct edges. GAL-GPR151 is kept as
a negative boundary: the original cloning report described weak activation,
but a later targeted-disruption study found no galanin-induced calcium
response in Gpr151-transfected ND7/23 cells (PMID:15111018; PMCID:PMC5235321).

## Validation

- 25 data rows and the exact 13-column schema are present.
- Review IDs and pair labels are unique and queue-aligned.
- Required fields are populated and confidence values use the established
  Module 21A vocabulary.
- `terminal_TF` is literal `null` for 24 rows and explicitly `CREB` only for
  Gast-Cckbr.
- The frozen Module20A manifest SHA remains
  `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.
