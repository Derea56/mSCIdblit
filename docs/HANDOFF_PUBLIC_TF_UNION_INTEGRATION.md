# Handoff: public TF/regulon union integration and evidence verification

## Mission

Integrate the public TF/regulon resources into a separate, provenance-preserving
union layer, then verify the most important new TFs and reconstruct their
upstream and downstream evidence to the same standard used for the original
mSCIdblit TF layer.

Do not rewrite, silently expand, or retag the frozen `mSCIdblit-v1.0.0` or
`mechanism-graph-v1.0.0` release. The integration must be additive and must
remain distinguishable from the curated mechanism graph.

## Starting state

Repository: `/Users/derea/Documents/SCI/mSCIdblit`

Frozen graph:

- Git commit: `eeb9960`
- Tags: `mSCIdblit-v1.0.0`, `mechanism-graph-v1.0.0`
- Release bundle: `data/processed/mechanism_bundle_module20_24_db_v1_0_0/`
- Frozen PostgreSQL socket: `/private/tmp/mscidblit_pg_socket`
- Database: `mscidblit_local`
- Port: `55432`

Public snapshots already retrieved for this workspace:

```text
/private/tmp/cellchat_human_lr.tsv
/private/tmp/cellchat_mouse_lr.tsv
/private/tmp/trrust_human.tsv
/private/tmp/trrust_mouse.tsv
/private/tmp/omnipath_dorothea_human.tsv
/private/tmp/omnipath_dorothea_mouse.tsv
/private/tmp/omnipath_causal_human.tsv
/private/tmp/omnipath_causal_mouse.tsv
/private/tmp/reactome_v97/ReactomePathways.gmt
```

Existing audits:

- `data/processed/public_database_comparison_v1/PUBLIC_DATABASE_COMPARISON_V1.md`
- `data/processed/public_database_comparison_v1/HARMONIZED_LR_COMPARISON_V1.md`
- `scripts/compare_public_databases_v1.py`
- `scripts/harmonize_ligand_receptor_v1.py`

The frozen mSCIdblit TF layer currently contains approximately 30
simple-symbol TF nodes, 44 generic regulons, 88 supported/exportable regulon
rows, and 43 symbol-resolved TF→target pairs across 15 TFs. These are baseline
counts; query the database rather than hard-coding them.

## Agent workstreams

Delegate these workstreams in parallel. The main model owns schema decisions,
merges results, and resolves conflicts.

### Agent A — source ingestion and normalization

1. Parse TRRUST human/mouse and OmniPath/DoRothEA human/mouse.
2. Preserve source version, retrieval date, source URL, raw record ID,
   species, PMID/reference fields, effect, and DoRothEA confidence level.
3. Normalize symbols conservatively and produce a mapping table for every
   imported TF and target gene.
4. Do not collapse human and mouse records into one species-free assertion.
5. Keep composite or unresolved names in a review queue rather than splitting
   them heuristically.

### Agent B — TF literature verification

Prioritize TFs that are present in both public TF resources but absent from the
explicit mSCIdblit TF-role set. Start with:

```text
TP53, JUN, FOS, MYC, STAT1, HIF1A, SP1, ETS1,
RUNX1, GATA3, CEBPB, IRF1, ATF2, EGR1, KLF4, NFKB2
```

For each prioritized TF:

1. Verify that the TF identity is real for the species being imported.
2. Resolve the database-linked PMID/reference records.
3. Inspect primary literature where possible, not only database summaries.
4. Classify each TF-target relationship as direct binding, perturbation
   response, expression association, inferred regulation, or unresolved.
5. Record whether the evidence supports activation, repression, or a
   context-dependent effect.
6. Record cell type, compartment, species, stimulus, and limitations.
7. If a public database contains the relationship but no usable supporting
   reference can be verified, retain it as `database_curated` with an explicit
   `unverified_public_record` status; do not promote it to primary evidence.

TRRUST PMID fields and OmniPath/DoRothEA `sources`, `references`,
`dorothea_level`, and `curation_effort` are evidence leads, not automatic
proof. Database presence alone is insufficient for the highest confidence
tier.

### Agent C — upstream and downstream reconstruction

For every integrated TF:

Downstream:

- Materialize source-specific regulons and members.
- Preserve direction and confidence.
- Keep direct TF-target evidence separate from inferred or perturbational
  regulation.
- Verify that every target has an explicit `target_gene` role or a documented
  role gap.

Upstream:

- Query existing `SignalingEdge` rows that terminate at the TF or a documented
  TF-containing complex.
- Preserve the path as separate edges: ligand/receptor → cascade → TF.
- Do not infer ligand→TF activation merely because a TF-target regulon exists.
- If OmniPath causal edges are added, store them as an external causal source
  layer with their own provenance; never relabel them as original mSCIdblit
  register evidence.
- Report integrated TFs with no supported upstream path as explicit upstream
  gaps.

### Agent D — schema, materialization, and QA

Use the existing evidence-aware schema where possible:

- `SignalingEntity`
- `SignalingEntityRole`
- `Regulon`
- `RegulonMember`
- `RegulonMemberSource`

Use separate source registries and versions for TRRUST and OmniPath/DoRothEA.
Do not overwrite the existing `mSCIdblit_signaling_edges:2026-08-25`
regulons. If the existing tables cannot represent an external mapping or
verification status cleanly, add a small normalized integration table rather
than putting source data into free-text notes.

The external union may be queryable and low-priority, but it must not silently
become part of the frozen mechanism bundle. Keep `export_priority` and source
provenance explicit.

### Agent E — independent gap audit

After materialization, independently recompute:

1. TF-node coverage versus TRRUST and DoRothEA.
2. TF-target pair coverage after exact symbol normalization.
3. Remaining unresolved aliases and composite TFs.
4. Downstream gaps: public target pairs not materialized.
5. Upstream gaps: integrated TFs lacking a supported signaling path.
6. Evidence gaps: imported records without verifiable references.
7. Conflicts where sources disagree on direction or context.

The audit must distinguish:

- absent TF node;
- TF node present but missing explicit TF role;
- TF present but missing downstream regulon;
- target present but unmapped alias;
- downstream present but upstream path absent;
- public record present but reference not independently verified.

## Required integration semantics

The union is a discovery and coverage layer, not a truth set. Every record
must retain:

```text
source_registry
source_version
retrieval_date
species_context
TF symbol and normalized identity
target symbol and normalized identity
relationship/effect
evidence basis
confidence tier
external record ID
PMID/reference/source locator
verification status
limitations
```

Do not merge away disagreement. If TRRUST says activation and another source
says repression, preserve both source-specific assertions and expose the
conflict in the audit.

Do not treat the following as equivalent:

- TF presence versus TF activation;
- TF-target membership versus direct binding;
- pathway membership versus a mechanistic edge;
- a receptor complex such as `Fzd1_Lrp6` versus standalone `FZD1`;
- a human assertion versus a mouse assertion;
- a public database record versus independently verified primary evidence.

## Verification priorities

First verify the high-impact TFs that were entirely absent from the frozen
graph: `TP53`, `JUN`, `FOS`, `MYC`, `STAT1`, `HIF1A`, `SP1`, `ETS1`, `RUNX1`,
and `GATA3`. Then review TFs that are present only under a non-TF role, such as
`CEBPB` as a target gene.

Use the existing mSCIdblit evidence conventions and register concepts. A
database-supported TF-target pair should not receive the same confidence as a
primary experiment showing direct binding or perturbation response.

## Required deliverables

1. Additive integration schema or migration.
2. Deterministic source-normalization/import script.
3. Entity and alias mapping table with unresolved queue.
4. Source-specific TF/regulon materialization with reference provenance.
5. Evidence-verification table for prioritized TFs and targets.
6. Upstream/downstream query views or documented SQL queries.
7. Post-integration gap report with counts and named examples.
8. Validation scripts with zero referential-integrity failures.
9. A release note explicitly stating that the frozen v1.0 graph was not
   modified.

## Acceptance criteria

The work is not complete until:

- Every imported record is traceable to its public source record.
- Every imported TF and target has a deterministic identity decision.
- Public TF-target pairs are queryable without losing source or species.
- The priority TFs have verified-reference status or an explicit unresolved
  reason.
- Upstream and downstream gaps are separately quantified.
- Existing mSCIdblit validation gates still pass.
- The frozen v1.0 bundle hashes and release metadata remain unchanged.
- No new public relationship is presented as original mSCIdblit evidence.

Do not commit, tag, push, or release the integrated layer until the independent
gap audit and evidence verification are complete.
