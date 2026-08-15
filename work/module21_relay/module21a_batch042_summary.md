# Module 21A batch 042 review summary

## Scope

Reviewed exactly the 25 requested frozen Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0420` through `M20A-CELLCHAT-REMAINING-0444` inclusive. Queue membership was checked against `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`; no row `0445` or later was included. No Module20A files, the frozen LR manifest, or shared Module21A registers were modified.

## Classification

- Exact rows reviewed: 25
- `reviewed_relay_candidate`: 19
- `reviewed_binding_only`: 5
- `reviewed_unresolved`: 1
- `reviewed_function_only`: 0
- Direct terminal TF row assignments: 3 (`ESR1` on rows 0440 and 0444; `ESR2` on row 0441)

## Findings

The 15 dopamine rows were retained as receptor-proximal relay candidates for mature dopamine activation of DRD1–DRD5. The CellChat ligand tokens combine DOPA with DDC and either SLC18A1, SLC18A2, or SLC6A3. DDC-mediated dopamine production, vesicular monoamine transport, and dopamine reuptake were kept as handling context; they were not treated as receptor subunits or as direct components of a mature dopamine–DRD molecular edge. Primary cloned-receptor assays support canonical DRD1/DRD5 Gs/olf and DRD2/DRD3/DRD4 Gi/o-family branches with subtype-dependent additional coupling, but no terminal TF was directly measured for these exact composite rows.

The five desmosomal rows were classified as binding-only adhesion edges. Primary recombinant ectodomain, SPR, solution-biophysics, and coated-bead aggregation experiments support family-wide heterophilic Dsg:Dsc adhesive dimers with pair-specific affinities. These are intercellular desmosomal adhesion relationships, not intracellular signaling relays; no kinase or TF assignment was made.

Four estrogen rows were promoted to receptor-proximal relay candidates for mature 17β-estradiol activation of ESR1, ESR2, or GPER1. CYP19A1 and HSD17B1 were kept as biosynthesis/availability context rather than receptor-complex components. ESR1/ESR2 assignments reflect direct E2 binding/transactivation evidence; GPER1 evidence supports cAMP/CREB and ERK/p38 branches without a terminal TF assignment. The E2-CYP19A1–NR1I2 row remained unresolved because no qualifying exact E2/NR1I2 activation study was located.

## Search boundaries and limitations

Searches covered exact queue labels, mature dopamine and estradiol aliases, receptor-subtype and complex notation, PubMed, PMC, and publisher pages. Primary sources included the five-receptor dopamine G-protein/cAMP study (PMID 38481695), cloned DRD1 signaling (PMID 7838121), DRD4 receptor pharmacology (PMID 20873719), desmosomal cadherin structural/adhesion work (PMID 27298358), ERα/ERβ coactivator and AP-1 transactivation studies (PMIDs 12554768 and 9278514), direct ERβ/ERα estradiol binding (PMID 9292936), GPER signaling in primary fallopian-tube and spermatocyte models (PMIDs 34069403 and 22306083), and HSD17B1-dependent estrogen-response studies (PMID 25617485).

Pathway and family-level context was used only to define branches and limitations. No direct molecular interaction was inferred from enzyme co-occurrence, biosynthetic context, adhesion output, or generic steroid-receptor promiscuity. The `E2-CYP19A1 Nr1i2` search was bounded by exact E2/estradiol–NR1I2/PXR queries and receptor activation terms; no qualifying primary exact-pair assay was located.

## File

- `work/module21_relay/module21a_batch042_review.tsv`
