# Public TF/regulon union v1

Status: additive discovery layer; not a replacement or revision of the
frozen `mSCIdblit-v1.0.0` / `mechanism-graph-v1.0.0` release.

The provenance-preserving candidate-universe expansion is documented in
[`docs/PUBLIC_TF_UNION_EXPANSION_V1.md`](PUBLIC_TF_UNION_EXPANSION_V1.md) and
staged separately under
`data/processed/public_tf_union_expansion_v1/`. It does not alter this v1
integration or promote any additional TF-target assertion.

This integration keeps TRRUST and OmniPath/DoRothEA assertions source- and
species-specific. It is queryable for coverage discovery, but it is not a
truth set and it is not exported as original mSCIdblit mechanism evidence.
The retrieved OmniPath causal snapshots are not imported into v1; upstream
coverage is derived only from existing frozen `SignalingEdge` rows, so no
external causal edge can be mistaken for original register evidence.

## Frozen-release boundary

The loader creates and populates only the `external_tf_*` tables defined in
[`schema/public_tf_union_integration.sql`](../schema/public_tf_union_integration.sql).
It does not insert into or update `SignalingEntity`, `SignalingEntityRole`,
`SignalingEdge`, `Regulon`, `RegulonMember`, `RegulonMemberSource`, or the
frozen mechanism bundle. All external regulons, members, and records have
`export_priority = 'exclude'`.

The v1.0 bundle and release metadata were left unchanged. This integration
must not be committed, tagged, pushed, or released as a new mechanism-graph
version until a later evidence-review decision promotes any selected rows.

## Materialized inventory

| Layer | Count |
|---|---:|
| Source registry rows | 4 |
| Public source records | 45,795 |
| Reference links | 240,805 |
| Identity mapping rows | 16,894 |
| Source-specific candidate regulons | 2,317 |
| Materialized source-regulon members | 44,965 |
| Priority-TF verification rows | 117 |

Simple normalized-pair coverage is complete for the imported snapshots:

| Source | Species | Raw simple pairs | Materialized simple pairs | Raw pairs not materialized |
|---|---|---:|---:|---:|
| TRRUST | human | 8,426 | 8,426 | 0 |
| TRRUST | mouse | 6,490 | 6,490 | 0 |
| OmniPath/DoRothEA | human | 15,116 | 15,116 | 0 |
| OmniPath/DoRothEA | mouse | 13,197 | 13,197 | 0 |

The raw source snapshots, retrieval date, source URLs, and SHA-256 digests
are recorded in
[`integration_manifest.json`](../data/processed/public_tf_union_v1/integration_manifest.json)
and the `external_tf_source_registry` table.
The source normalization table is
[`identity_mapping.tsv`](../data/processed/public_tf_union_v1/identity_mapping.tsv);
the post-load exact-symbol matches and explicit frozen TF/target-role flags
are in [`frozen_entity_mapping.tsv`](../data/processed/public_tf_union_v1/frozen_entity_mapping.tsv).

## Identity and evidence policy

Normalization trims simple symbols and stores a case-folded comparison key. It
does not apply aliases, split composites, convert complexes to component
pairs, or collapse human and mouse records. Composite, empty, and selected
accession-like values remain in
[`unresolved_identity_queue.tsv`](../data/processed/public_tf_union_v1/unresolved_identity_queue.tsv).

Each raw source row retains its source-specific record identifier, raw-row
hash, JSON payload, source locator, effect, DoRothEA level, source/reference
fields, and reference links. TRRUST rows remain `database_curated` with an
unresolved relationship modality. DoRothEA rows remain
`database_curated`/`inferred_regulatory`; a DoRothEA level is not treated as
proof of direct binding.

The bounded priority-TF review covers:

- Primary-reference support was recorded for human `TP53`, `JUN`, `FOS`,
  `MYC`, `STAT1`, `HIF1A`, `SP1`, `ETS1`, `RUNX1`, `GATA3`, `CEBPB`, and
  `NFKB2` records where the selected PMID occurred in the imported public
  row.
- Mouse rows tied to human-only references are marked
  `context_limited_reference`, not silently promoted to mouse primary
  evidence.
- `IRF1`, `ATF2`, `EGR1`, and `KLF4` remain
  `database_curated_unverified` with an explicit unresolved reason.

Selected primary-reference leads:

- [TP53, PMID 19411072](https://pubmed.ncbi.nlm.nih.gov/19411072/) — p53
  reactivation and context-dependent transcriptional responses.
- [JUN/FOS, PMID 9334186](https://pubmed.ncbi.nlm.nih.gov/9334186/) —
  c-Fos/c-Jun/Ets complex and promoter interaction evidence.
- [MYC, PMID 8206526](https://pubmed.ncbi.nlm.nih.gov/8206526/) — c-Myc
  suppression of HLA-B transcription through core promoter elements.
- [STAT1, PMID 16628196](https://pubmed.ncbi.nlm.nih.gov/16628196/) —
  STAT1-dependent response in poly(I:C)-treated human keratinocytes.
- [HIF1A, PMID 8955077](https://pubmed.ncbi.nlm.nih.gov/8955077/) — HIF-1
  binding sites in hypoxia-response promoters.
- [SP1, PMID 9574539](https://pubmed.ncbi.nlm.nih.gov/9574539/) — SP1
  promoter binding and C4 transcription.
- [ETS1, PMID 18381358](https://pubmed.ncbi.nlm.nih.gov/18381358/) — ETS1
  involvement in selected hypoxia-inducible gene responses.
- [RUNX1, PMID 12771199](https://pubmed.ncbi.nlm.nih.gov/12771199/) — RUNX1
  binding and CCL3/MIP-1alpha promoter activation.
- [GATA3, PMID 22120723](https://pubmed.ncbi.nlm.nih.gov/22120723/) — GATA3
  promoter binding and FOXC1 repression in basal-like breast cancer.
- [CEBPB, PMID 10453008](https://pubmed.ncbi.nlm.nih.gov/10453008/) — C/EBP
  binding and cytokine-receptor beta promoter activation.
- [NFKB2, PMID 18504428](https://pubmed.ncbi.nlm.nih.gov/18504428/) —
  NF-kB-dependent CCND2/CDK6 induction in an HTLV-I Tax context.

The complete row-level table is
[`priority_tf_evidence.tsv`](../data/processed/public_tf_union_v1/priority_tf_evidence.tsv).
The selected records retain their public raw effect; the verification table
stores the independently assessed evidence class, direction, context, and
limitations. This keeps disagreements visible. For example, MYC/HLA-family
rows include public-direction assertions that should not be treated as
resolved without target-specific adjudication.

## Upstream and downstream queries

`external_tf_downstream_union` exposes every imported assertion and separate
flags for frozen TF-node presence, frozen target-node presence, explicit TF
role, and explicit target-gene role:

```sql
SELECT source_registry, species_context,
       source_tf_symbol, source_target_symbol,
       raw_relationship_effect, effect_polarity,
       relationship_class, evidence_basis,
       tf_node_present, tf_role_present,
       target_node_present, target_role_present,
       verification_status
FROM external_tf_downstream_union
WHERE tf_normalized_symbol_key = 'tp53'
ORDER BY source_registry, species_context, source_target_symbol;
```

`external_tf_upstream_paths` returns only existing, exportable
`SignalingEdge` rows whose target is an exact frozen entity-symbol match. It
preserves the upstream edge, pathway, source/evidence fields, and target TF
entity; it does not infer ligand-to-TF activation from a regulon.

```sql
SELECT source_registry, species_context,
       tf_normalized_symbol, edge_id,
       upstream_entity_name, tf_entity_name,
       pathway_name, relation_type,
       support_kind, source_scope, confidence_tier
FROM external_tf_upstream_paths
WHERE tf_normalized_symbol_key = 'nfkb1'
ORDER BY edge_id;
```

`external_tf_upstream_gaps` reports `tf_node_unmapped`,
`upstream_path_absent`, or `upstream_path_present`. Human-to-mouse symbol
matches are only exact frozen `gene_symbol` matches; they are not a claim
that the frozen mouse-scoped graph is a human mechanistic graph. Complex TF
labels and unresolved aliases remain gaps.

## Independent audit

The independent audit is generated by
[`scripts/audit_public_tf_union_v1.py`](../scripts/audit_public_tf_union_v1.py)
and writes:

- [`PUBLIC_TF_UNION_GAP_AUDIT_V1.md`](../data/processed/public_tf_union_v1/PUBLIC_TF_UNION_GAP_AUDIT_V1.md)
- [`public_tf_union_gap_report.json`](../data/processed/public_tf_union_v1/public_tf_union_gap_report.json)

The artifact and frozen-boundary validator is
[`scripts/validate_public_tf_union_v1.py`](../scripts/validate_public_tf_union_v1.py);
its current result is `pass` in
[`public_tf_union_validation.json`](../data/processed/public_tf_union_v1/public_tf_union_validation.json).

Current audit results:

- Referential-integrity failures: `0`.
- Simple public pairs not materialized: `0`.
- Non-excluded external records or members: `0`.
- Raw rows with unresolved identity decisions: `830` (repeated source rows;
  the unique mapping queue has 690 rows).
- Source-specific TF-regulon groups with no frozen TF node: `2,180`.
- Mapped TF-regulon groups with no supported frozen upstream path: `76`.
- Mapped TF-regulon groups with a supported upstream path: `61`.
- Direction-conflict groups retained without collapsing: `435`.

The large absence counts are coverage gaps relative to the frozen graph, not
claims that the public TFs or relationships are biologically invalid.
