# Module 21A batch 173 review summary

Reviewed exactly the 25 requested filtered-queue rows in the supplied order
(queue ordinals 3776–3800), retaining the exact Module 20A review IDs and
canonical pair labels. The raw output uses the requested 13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

## Disposition

- 22 rows were retained as primary-source-backed relay or activation records.
- 3 rows were retained as explicit `no_evidence_boundary` records:
  - `M20A-LIANA-REMAINING-0056` — Cxcl10 Ccr3
  - `M20A-LIANA-REMAINING-0060` — Cxcl13 Cxcr3
  - `M20A-LIANA-REMAINING-0063` — Cxcl2 Cxcr1
- `M20A-LIANA-REMAINING-0047` is intentionally `reviewed_binding_only`: the
  primary source directly supports CD40LG/CD40 binding, but this bounded
  review did not add an adaptor/kinase relay.
- No terminal TF was assigned; every row therefore records `terminal_TF=null`.

## Evidence-layer rules applied

Binding/activation, receptor-proximal relay, and downstream pathway/function
were recorded as distinct semicolon-delimited layers. Direct interaction was
not inferred from pathway membership, expression, chemotaxis alone, reporter
function alone, or shared family biology. The CD40LG integrin rows were kept
as separate receptor branches (ITGA2B_ITGB3, ITGA5_ITGB1, and ITGAM_ITGB2),
and the ACKR3 row was kept distinct from canonical CXCR4 G-protein signaling.
DLK1 and DLK2 were recorded as noncanonical inhibitory NOTCH1 interactions,
not as canonical DSL agonists.

## Limitations

All rows retain a populated limitations field. Common limitations are species
and cell-model transfer, recombinant or processed ligand constructs, receptor
complex/conformation dependence, shared chemokine-receptor usage, membrane
presentation/mechanical requirements for Notch, and pathway reporters that do
not identify a unique terminal TF. The three no-evidence boundaries cite
neighboring primary cognate-system studies where useful, but do not promote
those neighboring branches to the submitted exact pair.

## Scope and write boundary

Only these two batch artifacts were written. Module20A files, frozen queues,
shared Module21A registers, coverage tables, pathway-reuse registries, and
integration outputs were not modified. No commit was created.

- `work/module21_relay/module21a_batch173_review.tsv`
- `work/module21_relay/module21a_batch173_summary.md`
