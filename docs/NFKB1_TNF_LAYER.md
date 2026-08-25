# TNF–NF-κB1 query layer

The database-backed Module 20B–24B release now represents `NFKB1` as an
explicit `transcription_factor`. The composite `IKK-NFKB1-RELA` record remains
a `signaling_cascade` node.

The graph uses two intentionally different edge semantics:

```text
TNF --binds_receptor--> TNFR1/p55 or TNFR2 receptor complex
TNFR --supports_cascade--> IKK-NFKB1-RELA
IKK-NFKB1-RELA --contains_component--> NFKB1 or RELA
NFKB1 --regulates_target_gene--> target gene
```

`supports_cascade` and `contains_component` are non-activating annotations.
They make the supported cascade traversable without inventing a direct
TNFR-to-NFKB1 binding or standalone TNFR-to-NFKB1 activation edge.

## Core target summary

The release contains 17 human NFKB1 target-gene edges and matching
`RegulonMember` rows from the TRRUST v2 NFKB1 target table. The summary is
deliberately lightweight, versioned, and not exhaustive. Conflicting or mixed
literature modes are retained as `context_dependent`; the target set is not a
claim that TNF induces every target in every receiver cell.

Apply the layer after the base graph and regulon schema:

```bash
psql "$MSCIDBLIT_DATABASE_URL" -v ON_ERROR_STOP=1 \
  -f schema/regulon_layer.sql \
  -f schema/nfkb1_core_regulon_layer.sql
psql "$MSCIDBLIT_DATABASE_URL" -v ON_ERROR_STOP=1 \
  -f scripts/materialize_mechanism_roles.sql \
  -f scripts/validate_mechanism_roles.sql \
  -f scripts/validate_mechanism_database_release.sql \
  -f scripts/validate_regulon_layer.sql \
  -f scripts/validate_nfkb1_core_regulon.sql
```

## Query TNF → TF → target genes

This query follows only the explicit released TNF receptor, cascade-continuity,
component, and NFKB1 target edges:

```sql
SELECT
  ligand.canonical_name AS ligand,
  receptor.canonical_name AS receptor,
  cascade.canonical_name AS signaling_cascade,
  tf.canonical_name AS transcription_factor,
  target.canonical_name AS target_gene,
  target_edge.effect_polarity,
  target_edge.evidence_status
FROM SignalingEntity AS ligand
JOIN SignalingEdge AS receptor_edge
  ON receptor_edge.source_entity_id = ligand.entity_id
 AND receptor_edge.relation_type = 'binds_receptor'
JOIN SignalingEntity AS receptor
  ON receptor.entity_id = receptor_edge.target_entity_id
JOIN SignalingEdge AS cascade_edge
  ON cascade_edge.source_entity_id = receptor.entity_id
 AND cascade_edge.relation_type = 'supports_cascade'
JOIN SignalingEntity AS cascade
  ON cascade.entity_id = cascade_edge.target_entity_id
JOIN SignalingEdge AS component_edge
  ON component_edge.source_entity_id = cascade.entity_id
 AND component_edge.relation_type = 'contains_component'
JOIN SignalingEntity AS tf
  ON tf.entity_id = component_edge.target_entity_id
JOIN SignalingEntityRole AS tf_role
  ON tf_role.entity_id = tf.entity_id
 AND tf_role.role = 'transcription_factor'
 AND tf_role.export_priority <> 'exclude'
JOIN SignalingEdge AS target_edge
  ON target_edge.source_entity_id = tf.entity_id
 AND target_edge.relation_type = 'regulates_target_gene'
JOIN SignalingEntity AS target
  ON target.entity_id = target_edge.target_entity_id
JOIN SignalingEntityRole AS target_role
  ON target_role.entity_id = target.entity_id
 AND target_role.role = 'target_gene'
 AND target_role.export_priority <> 'exclude'
WHERE lower(ligand.canonical_name) IN ('tnf', 'tnfa')
  AND tf.canonical_name = 'NFKB1'
ORDER BY receptor.canonical_name, target.canonical_name;
```

The database-specific gate is
[`validate_nfkb1_core_regulon.sql`](../scripts/validate_nfkb1_core_regulon.sql).
It requires the explicit TF role, 17 target edges, target roles, provenance,
and zero standalone TNFR-to-NFKB1 activation edges.
