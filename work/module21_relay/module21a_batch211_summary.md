# Module 21A batch 211 summary

## Scope

Batch 211 contains exactly the corrected 25 currently queued Module20A pairs,
in the requested order:

`M20A-EXT-1603` through `M20A-EXT-1625`, followed by `M20A-EXT-1643` and
`M20A-EXT-1650`. The first row is `F8 Lrp4`; all submitted pair labels are
preserved exactly. There is no count discrepancy in the corrected scope.

## Disposition

- 5 reviewed relay candidates: Fadd-Fas, Fadd-Tradd, Fam3c-Lifr,
  Farp2-Plxna4, and Fat4-Dchs1.
- 3 reviewed binding-only records: Fadd-Abca1, Fbln1-Itgb1, and
  Fgf10-Fgfrl1.
- 2 reviewed scavenging/storage-only records: F9-Lrp1 and Fgf1-Cd44.
- 6 reviewed unresolved complex or comparator boundaries: Farp2-Plxna1,
  Farp2-Plxna2, Farp2-Plxna3, Fbn1-Itga5, Fbn1-Itgb1, and Fbn1-Itgb3.
- 9 explicit no-evidence boundaries: F8-Lrp4, Fabp5-Rxra, Fadd-Traf2,
  Fam3b-Lrp5, Fam3c-Ffar2, Fam3c-Glra2, Fam3c-Lamp1, Fam3c-Pdcd1, and
  Fasl-Tnfrsf1a.

One provisional terminal TF endpoint is recorded: `STAT3` for the exact
FAM3C/ILEI-LIFR breast-cancer-stem-cell signaling study. No TF is inferred
for uptake, adhesion, storage, adaptor, receptor-family comparator, or
pathway-only records. YAP1 is retained as a Hippo effector/coactivator in the
FAT4-DCHS1 limitation text, not promoted as a finalized TF endpoint.

## Evidence handling

Direct molecular associations, receptor-proximal intracellular relays, and
downstream functional outputs are kept in separate `evidence_layer` and
`relation_type` fields. The batch includes several noncanonical Module20A
node-role cases: FADD is an intracellular adaptor, FARP2 is a plexin effector,
FBLN1D-prime is an isoform-specific intracellular binder, and integrin rows
require alpha/beta heterodimer context. These are not represented as ordinary
soluble ligand-receptor signaling edges.

Positive primary anchors include F9/IXa-LRP1 clearance and binding
(DOI:10.1182/blood.V96.10.3459; DOI:10.1074/jbc.M209097200),
FADD-ABCA1 association (PMID:12235128), Fas-FADD and TRADD-FADD adaptor
relays (PMID:12529427; PMID:8565075), FAM3C/ILEI-LIFR-STAT3 signaling
(PMCID:PMC6525020; PMID:30692635), FARP2-PLXNA4-Rac1 signaling
(PMID:32499377), FAT4-DCHS1 binding/function (PMIDs:25355906, 26116666,
28826487), FBN1-integrin heterodimer adhesion (PMID:12807887), FGF1-CD44
storage binding (PMID:29812912), and FGF10-FGFRL1 decoy binding
(PMID:19920134).

Searches covered exact symbols and aliases across the existing Module20A
evidence packets, PubMed, PMC, publisher records, Europe PMC search pages,
and pathway/family leads. Family-level, expression-only, shared-complex,
and comparator evidence was retained only as a limitation. No direct
molecular interaction was inferred from pathway or phenotype evidence.

## Validation

The TSV is required to contain exactly 25 data rows and the exact 13-column
schema:

`review_id, pair, status, stable_citations, species, cell_type_model,
assay_or_perturbation, relation_type, evidence_layer, pathway_branch,
confidence, limitations, terminal_TF`

Validation targets for this batch are unique review IDs, exact requested row
order and labels, populated required fields, allowed confidence vocabulary,
and literal `null` for every unvalidated terminal-TF field. Only the two
batch-211 files are written; no Module20A or Module21A ledgers are modified
and no commit is created.
