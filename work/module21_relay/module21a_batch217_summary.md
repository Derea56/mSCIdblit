# Module 21A batch 217 review summary

This batch reviews exactly the 25 requested queued Module20A pairs, in the
user-supplied order, using the exact 13-column review schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

The search boundary covered exact-symbol queries across PubMed, PMC,
Europe PMC, publisher pages, structural studies, and pathway/context
comparators. Primary research was prioritized. Module20A LR ledgers, the
frozen manifest, shared Module21A registers, and all integration outputs were
left untouched. Only `module21a_batch217_review.tsv` and this summary were
written.

## Disposition

- 25 data rows; exact requested IDs and pair labels; 13 columns per row.
- 12 `reviewed_relay_candidate` rows: GPI1–AMFR, GRP–GRPR, GUCA2A–GUCY2C,
  GUCA2B–GUCY2C, H2-Aa–CD4, H2-Ab1–CD4, H2-K1–CD8a, H2-K1–CD8b1,
  HCRT–HCRTR1, HCRT–HCRTR2, HGF–CD44, and HGF–NRP1.
- 3 `reviewed_binding_only` rows: GPC3–UNC5D, GREM1–KDR, and H2-T23–CD8a.
- 2 `reviewed_scavenging_only` rows: GRN–SORT1 and HP–CD163.
- 2 `unresolved` rows: H2-Eb1–CD4 and H2-T23–CD8b1.
- 6 `no_evidence_boundary` rows: GPHA2–TSHR, GPHB5–TSHR, GZMA–F2R,
  H2-M3–CD8a, H2-M3–CD8b1, and HP–CD22.

The complete disposition is 12 relay candidates, 3 binding-only, 2
scavenging-only, 2 unresolved, and 6 no-evidence boundaries (25 total).

## Evidence-layer handling

Direct or receptor-complex binding/activation, receptor-proximal relay, and
downstream pathway or cellular function are represented separately in the TSV.
GPC3–UNC5D is retained as direct extracellular complex binding with a guidance
output, not as an inferred cytosolic relay. GRN–SORT1 and HP–CD163 are retained
as uptake/scavenging relationships. MHC-II/CD4 and MHC-I/CD8 rows are explicitly
composite coreceptor/TCR contexts; evidence for a full MHC complex was not
treated as proof for an isolated chain. GREM1–KDR retains conflicting and
negative VEGFR2 activation results rather than being promoted as an agonist.

No row contains an inferred terminal TF. Every `terminal_TF` value is the
literal `null` because the reviewed evidence did not provide a sufficiently
pair-specific endpoint for Module22A assignment.

## Validation

The TSV was checked for exactly 25 data rows, unique review IDs and pair
labels, exact alignment to the requested queue subset, populated required
fields, allowed confidence values (`high`, `medium-high`, `medium`,
`low-medium`, `low`), literal `null` terminal-TF values, and no embedded tabs
or extra columns. No SQL or shared register materialization was performed.
