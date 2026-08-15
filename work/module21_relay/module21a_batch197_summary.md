# Module 21A Batch 197 review summary

Batch 197 reviews exactly the 25 supplied currently queued Module20A pairs
using the established 13-column schema in
`module21a_batch197_review.tsv`. Only this TSV and this summary are written by
the batch; shared Module20A/21A ledgers and the frozen LR manifest are
untouched.

## Disposition

| status | count |
|---|---:|
| `reviewed_relay_candidate` | 10 |
| `reviewed_binding_only` | 6 |
| `reviewed_function_only` | 2 |
| `reviewed_unresolved` | 1 |
| `no_evidence_boundary` | 6 |
| **total** | **25** |

Confidence counts: high 2; medium-high 12; medium 3; medium-low 1; low 7.
Two rows carry provisional terminal-TF evidence: `ATF2` for the explicit
WNT5B-FZD3-JNK reporter branch and `CREB` for the alpha2M-LRP1-ERK-dependent
neuronal transcriptional output. All other rows use literal `null`.

## Evidence decisions

- VEGFC-KDR, VEGFD-FLT4, and VEGFD-KDR were promoted only where processed
  ligand binding/receptor phosphorylation and downstream endothelial or
  survival outputs were directly studied. VEGFD-FLT4_KDR remains unresolved:
  the primary papers support separate FLT4 and KDR branches, not a preformed
  composite receptor.
- WNT11-FZD1 and WNT5B-FZD10/FZD8/FZD9 remain explicit no-evidence boundaries.
  WNT5B-FZD1/FZD2/FZD3/FZD7 have exact-pair or receptor-dependent primary
  evidence. WNT5B-FZD5 is retained as receptor-complex/genetic-function
  evidence, while WNT5B-FZD6 is function-only because pooled WNT5A/5B and
  FZD4/FZD6 developmental perturbations did not isolate an exact binary
  WNT5B-FZD6 affinity or proximal relay.
- CCL27a-CCR2 remains unresolved at the exact-pair level; canonical
  CCL27-CCR10 and CCL28 comparator evidence was not transferred to CCR2.
- Activated alpha2M-LRP1 is a direct binding and signaling edge with Src-family
  kinase, Trk transactivation, ERK/Akt, CREB, and cellular outputs. Native
  unactivated A2M and unrelated LRP1 ligands were not silently conflated.
- ADA-DPP4 is retained as binding-only. The ADA/CD26 ecto-complex is directly
  supported, but CD26 costimulation studies do not establish that the ADA
  binding interface is required for an intracellular DPP4 relay.
- ADAM12-SDC4 is a direct cysteine-rich-domain/heparan-sulfate interaction
  with SDC4-to-beta1-integrin adhesion signaling through PKCalpha and RhoA.
  ADAM17-ITGB1 is limited to the alpha5beta1-containing adhesion complex;
  ITGB1 alone is not treated as the receptor.
- ADAM2-CD9 is function-only because CD9 cooperates with the
  ADAM2-alpha6beta1 sperm-egg system but direct ADAM2-CD9 binding was not
  demonstrated. ADAM2-ITGA9 is direct at the alpha9beta1 complex level;
  ADAM2-ITGB7 remains a no-evidence boundary because beta7 evidence belongs
  to ADAM7/ADAM28 comparator systems.
- ADAM9-ITGA3, ADAM9-ITGA6, and ADAM9-ITGAV are direct disintegrin-domain
  adhesion interactions with beta-containing integrin complexes. They are not
  promoted to standalone ITGA-subunit intracellular signaling edges.

## Search boundary and validation

Searches covered exact ligand/receptor names and aliases across PubMed, PMC,
publisher pages, Europe PMC, and the systematic WNT-FZD interaction literature.
Primary biochemical, receptor-reconstitution, co-immunoprecipitation, genetic,
perturbation, adhesion, and cellular-function studies were retained where they
matched the exact pair or an explicitly documented receptor-complex context.
Reviews, expression-only observations, docking predictions, generic receptor
family annotations, and comparator-family results were used only to define
search boundaries and were not promoted to direct molecular edges.

Before any ledger integration, this packet must pass: 25 data rows; unique
review IDs and pair labels; exact alignment to the supplied IDs; exact
13-column schema; populated required fields; confidence vocabulary
`high|medium-high|medium|medium-low|low`; and `terminal_TF` either an explicit
terminal readout (`ATF2` or `CREB`) or literal `null`.
