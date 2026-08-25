# Regulon modeling layer

The regulon layer is an evidence-backed target-set model for transcription
factors. It is intentionally separate from the signaling graph:

```text
TGFB1 --supported SignalingEdge--> SMAD3
SMAD3 --supported RegulonMember--> target gene
```

The second statement does not assert that SMAD3 is active. An “active
downstream regulon” result is only valid when both statements are independently
supported and their species/cell/compartment contexts are compatible.

## What is included

Apply [`schema/regulon_layer.sql`](../schema/regulon_layer.sql) after the base
schema. It adds three tables:

- `Regulon`: a versioned TF target-set definition, with source registry,
  release, and context.
- `RegulonMember`: one TF-to-target membership assertion. Candidate rows are
  non-exportable by default; exportable rows must be explicitly supported.
- `RegulonMemberSource`: provenance for each membership, including a paper,
  observation, author claim, or stable external locator.

This first layer does not add an activation-state table, a pathway-to-regulon
shortcut, or a speculative `TGFB -> TF` edge. A `SignalingEdge` remains the
only place to assert a signaling relationship.

## Release gate

Run the read-only checks after applying the migration:

```bash
psql "$MSCIDBLIT_DATABASE_URL" -v ON_ERROR_STOP=1 \
  -f scripts/validate_regulon_layer.sql
```

The gate requires that every exported membership has a curated parent regulon,
an explicitly curated TF role, and at least one supporting evidence row. The
SQL constraints also force candidate, excluded, and superseded memberships to
remain excluded from export.

## Query pattern: signal → TF → regulon → target

The following PostgreSQL query is a bounded path query. It requires a
provenance row for every signaling edge and only returns curated regulons and
supported, exportable memberships. It does not infer activation from a
regulon membership.

```sql
WITH RECURSIVE signal_path AS (
  SELECT
    edge.target_entity_id AS entity_id,
    ARRAY[edge.source_entity_id, edge.target_entity_id] AS node_path,
    ARRAY[edge.edge_id] AS edge_path,
    ARRAY[coalesce(pathway.pathway_name, '')] AS pathway_names,
    1 AS hops
  FROM SignalingEntity AS ligand
  JOIN SignalingEdge AS edge
    ON edge.source_entity_id = ligand.entity_id
  LEFT JOIN SignalingPathway AS pathway
    ON pathway.pathway_id = edge.pathway_id
  WHERE (
      lower(ligand.canonical_name) IN ('tgfb', 'tgfb1')
      OR lower(coalesce(ligand.gene_symbol, '')) IN ('tgfb', 'tgfb1')
    )
    AND coalesce(edge.export_priority, '') <> 'exclude'
    AND EXISTS (
      SELECT 1
      FROM SignalingEdgeSource AS edge_source
      WHERE edge_source.edge_id = edge.edge_id
        AND (
          edge_source.paper_id IS NOT NULL
          OR edge_source.observation_id IS NOT NULL
          OR edge_source.claim_id IS NOT NULL
        )
    )

  UNION ALL

  SELECT
    edge.target_entity_id,
    path.node_path || edge.target_entity_id,
    path.edge_path || edge.edge_id,
    path.pathway_names || coalesce(pathway.pathway_name, ''),
    path.hops + 1
  FROM signal_path AS path
  JOIN SignalingEdge AS edge
    ON edge.source_entity_id = path.entity_id
  LEFT JOIN SignalingPathway AS pathway
    ON pathway.pathway_id = edge.pathway_id
  WHERE path.hops < 12
    AND NOT edge.target_entity_id = ANY(path.node_path)
    AND coalesce(edge.export_priority, '') <> 'exclude'
    AND EXISTS (
      SELECT 1
      FROM SignalingEdgeSource AS edge_source
      WHERE edge_source.edge_id = edge.edge_id
        AND (
          edge_source.paper_id IS NOT NULL
          OR edge_source.observation_id IS NOT NULL
          OR edge_source.claim_id IS NOT NULL
        )
    )
)
SELECT DISTINCT
  array_to_string(array_remove(path.pathway_names, ''), ' > ') AS signaling_pathway,
  tf.canonical_name AS transcription_factor,
  regulon.regulon_name,
  regulon.source_registry,
  regulon.source_version,
  target.canonical_name AS downstream_target,
  member.regulatory_effect,
  member.confidence_tier
FROM signal_path AS path
JOIN SignalingEntity AS tf
  ON tf.entity_id = path.entity_id
JOIN Regulon AS regulon
  ON regulon.tf_entity_id = tf.entity_id
 AND regulon.definition_status = 'curated'
JOIN RegulonMember AS member
  ON member.regulon_id = regulon.regulon_id
 AND member.membership_status = 'supported'
 AND member.export_priority <> 'exclude'
 AND EXISTS (
       SELECT 1
       FROM RegulonMemberSource AS member_source
       WHERE member_source.regulon_member_id = member.regulon_member_id
         AND member_source.evidence_status = 'supporting'
         AND member_source.evidence_scope <> 'negative_evidence'
     )
JOIN SignalingEntity AS target
  ON target.entity_id = member.target_entity_id
WHERE lower(tf.entity_type) IN ('tf', 'transcription_factor', 'tf_complex')
   OR lower(coalesce(tf.entity_subtype, '')) IN ('tf', 'transcription_factor', 'tf_complex')
ORDER BY signaling_pathway, transcription_factor, regulon.regulon_name,
         downstream_target;
```

The result is intentionally empty until the signaling graph and regulon
memberships have been separately curated. That empty result is safer than
turning a pathway label or a TF-target database membership into an unsupported
activation claim.
