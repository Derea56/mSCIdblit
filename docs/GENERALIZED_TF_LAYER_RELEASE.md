# Generalized TF, pathway, target, and regulon layer

Release date: 2026-08-25

This release generalizes the NFKB1 correction across the complete current
mechanism database. It materializes what is already evidence-backed in the
graph; it does not claim an exhaustive biological regulon for every TF.

## Release contents

- 44 explicit transcription-factor sources with canonical target-gene edges.
- 90 unique TF-to-target pairs from 95 exportable target-gene edges.
- 44 release-scoped regulons in `mSCIdblit_signaling_edges:2026-08-25`.
- 90 regulon memberships: 88 supported/exportable and 2 retained as
  candidate/non-exportable because their current register evidence is only
  negative evidence.
- 145 register-backed regulon-source rows, including 139 supporting and 6
  explicitly negative source rows.
- Every pathway carried by a target-gene edge has an explicit TF pathway
  member where the role was not already present. This is a downstream
  target-gene-layer association, not a shortcut that asserts upstream TF
  activation.
- 175 composite-label component review candidates. The 173 unresolved
  candidates remain excluded; the 2 accepted rows correspond to the existing
  evidence-backed `IKK-NFKB1-RELA -> NFKB1/RELA` component edges.

## Evidence boundary

The generalized migration reads only canonical target-gene edges and their
`SignalingEdgeRegisterSource` provenance. It does not:

- create direct ligand-to-TF or receptor-to-TF activation edges;
- infer component membership from a composite label;
- turn an unsupported target set into an exportable regulon;
- treat a pathway member row as an activation-state assertion.

The two current candidate memberships are deliberately retained for audit but
are not exported. Future expansions can promote them only after an additional
non-negative source is curated.

## Query pattern

The database can now answer a bounded, evidence-aware query for any signal or
TF. The exact downstream chain is:

```text
ligand/receptor/cascade
  -> SignalingEdge
  -> explicit transcription_factor role
  -> Regulon
  -> supported RegulonMember
  -> explicit target_gene role
```

For all evidence-backed target-gene edges, a direct TF/regulon query is:

```sql
SELECT
  pathway.pathway_name AS signaling_pathway,
  tf.canonical_name AS transcription_factor,
  regulon.regulon_name,
  target.canonical_name AS downstream_target,
  member.regulatory_effect,
  member.confidence_tier,
  source.external_record_id,
  source.source_locator
FROM SignalingEdge AS edge
JOIN SignalingPathway AS pathway
  ON pathway.pathway_id = edge.pathway_id
JOIN SignalingEntity AS tf
  ON tf.entity_id = edge.source_entity_id
JOIN SignalingEntityRole AS tf_role
  ON tf_role.entity_id = tf.entity_id
 AND tf_role.role = 'transcription_factor'
 AND tf_role.export_priority <> 'exclude'
JOIN Regulon AS regulon
  ON regulon.tf_entity_id = tf.entity_id
 AND regulon.source_registry = 'mSCIdblit_signaling_edges'
 AND regulon.source_version = '2026-08-25'
 AND regulon.definition_status = 'curated'
JOIN RegulonMember AS member
  ON member.regulon_id = regulon.regulon_id
 AND member.target_entity_id = edge.target_entity_id
 AND member.membership_status = 'supported'
 AND member.export_priority <> 'exclude'
JOIN SignalingEntity AS target
  ON target.entity_id = member.target_entity_id
JOIN SignalingEntityRole AS target_role
  ON target_role.entity_id = target.entity_id
 AND target_role.role = 'target_gene'
 AND target_role.export_priority <> 'exclude'
JOIN RegulonMemberSource AS source
  ON source.regulon_member_id = member.regulon_member_id
 AND source.evidence_status = 'supporting'
 AND source.evidence_scope <> 'negative_evidence'
WHERE edge.relation_type IN (
    'regulates_target_gene',
    'induces_target_gene',
    'represses_target_gene'
  )
  AND coalesce(edge.export_priority, '') <> 'exclude'
  AND tf.canonical_name = 'NFKB1'
ORDER BY signaling_pathway, downstream_target, source.external_record_id;
```

For an upstream signal, join this result to the independently supported
signaling cascade query. For example, the TNF/NFKB1 chain remains:

```text
TNF
  --binds_receptor-->
TNFR1/p55 receptor or TNFR2 receptor complex
  --supports_cascade-->
IKK-NFKB1-RELA
  --contains_component-->
NFKB1 or RELA
  --regulates_target_gene-->
target gene
```

The `supports_cascade` and `contains_component` edges are non-activating
continuity/component relations. Their role is to preserve the supported path
without asserting that the database observed receptor-to-TF binding directly.

## Validation

Run the generalized and existing release gates together:

```bash
psql "$MSCIDBLIT_DATABASE_URL" -v ON_ERROR_STOP=1 \
  -f scripts/validate_generalized_tf_layer.sql \
  -f scripts/validate_mechanism_roles.sql \
  -f scripts/validate_mechanism_database_release.sql \
  -f scripts/validate_regulon_layer.sql \
  -f scripts/validate_nfkb1_core_regulon.sql
```

All checks returned zero issues in the 2026-08-25 local release validation.
