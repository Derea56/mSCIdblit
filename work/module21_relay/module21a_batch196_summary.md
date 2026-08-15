# Module 21A Batch 196 review summary

Batch 196 reviews exactly the 25 supplied Module20A CellChat-remaining pairs
using the exact 13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

## Disposition

| status | count |
|---|---:|
| `reviewed_relay_candidate` | 14 |
| `reviewed_binding_only` | 2 |
| `reviewed_function_only` | 2 |
| `reviewed_unresolved` | 7 |
| **total** | **25** |

Confidence counts: high 3; medium-high 12; medium 2; low-medium 4; low 4.
All 25 rows use the literal `null` for `terminal_TF`; no explicit terminal-TF
evidence was established in this batch.

## Evidence decisions

- Direct receptor-tyrosine-kinase relays were retained for PDGF-BB-PDGFR-alpha,
  PDGF-BB-PDGFR-beta, processed PDGF-DD-PDGFR-beta, PlGF-FLT1, TGF-alpha-EGFR,
  TGF-beta1/2/3-TGFBR1/TGFBR2 complexes, VEGF-A-KDR, and processed VEGF-C-FLT4.
  Binding/activation, receptor-proximal phosphorylation or adaptor recruitment,
  and downstream ERK, PI3K-AKT, PLC-gamma, SMAD, or cellular-function evidence
  are recorded in distinct layers within each row.
- VEGF-A-FLT1 is retained as a context-dependent relay because FLT1 is often a
  high-affinity modulatory or ligand-sink receptor rather than the dominant
  mitogenic VEGFR. VEGF-B-FLT1 is retained as binding-only: high-affinity
  receptor binding is supported, but efficient downstream FLT1 activation is
  not consistently demonstrated in the strongest comparative primary study.
- SELPLG-SELE is retained as glycoform-dependent binding/adhesion evidence for
  E-selectin-mediated tethering and rolling. It is not promoted to a defined
  intracellular kinase or TF relay. SEMA7A-ITGA1/ITGB1 is retained as an
  alpha1beta1 receptor-complex relay with FAK/MAPK and axon/immune outputs;
  the heterodimer is not collapsed to either integrin subunit alone.
- TAC4-TACR1 and TENM3-ADGRL2 retain functional or cell-recognition evidence
  without a resolved intracellular relay. Hemokinin-1 responses include
  NK1/TACR1-dependent inflammatory evidence but also NK1-independent sensory
  responses, and the strongest TENM3-ADGRL2 evidence is developmental neuronal
  function rather than purified biochemical affinity.
- NRXN3-ADGRL1 and PCDHA4B homophily remain unresolved. PGD2-PTGDS to PTGDR or
  PTGDR2 is an enzyme-to-metabolite/receptor annotation mismatch: the cited
  receptor studies test mature PGD2, not PTGDS protein. These records remain
  explicit no-evidence boundaries rather than direct molecular edges.
- The three ACVR1-containing TGF-beta composite labels remain unresolved. The
  cited studies support canonical TGFBR1/TGFBR2 signaling and receptor-family
  cross-talk or ACVR1 trans-phosphorylation in bounded contexts, but do not
  establish direct ligand binding to the submitted ACVR1-containing
  holoreceptor. Pathway evidence was not promoted to direct binding.

## Search boundary and validation

Exact ligand/receptor and receptor-complex names were searched across PubMed,
PMC, publisher records, and existing Module20A adjudication material. Primary
structural, biochemical, receptor-reconstitution, perturbation, and cellular
function studies were retained where available. Reviews and pathway records
were used only to orient receptor aliases or pathway boundaries. Generic
ligand-family, receptor-family, expression-only, computational, and
phenotype-only results were not used to infer an exact direct molecular edge.

Validation completed before handoff: 25 data rows; exact supplied IDs and pair
labels; exact 13-column schema; unique review IDs and pair labels; populated
required fields; valid confidence values; and `terminal_TF=null` in every row.
Only this TSV and summary are written by Batch 196. Module20A ledgers, Module
21A shared registers, Module22A handoff tables, and the frozen LR manifest were
not modified; no commit was made.
