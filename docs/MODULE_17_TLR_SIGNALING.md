# Module 17: TLR Signaling Cascade Query Guide

Module 17 provides the normalized graph layer for receptor-to-pathway questions. Module 12 remains the conditioning/tolerance evidence module; Module 17 cross-indexes those observations when they establish TLR signaling edges.

## Entity and Pathway Membership

```sql
SELECT
  e.canonical_name,
  p.pathway_name,
  pm.member_role,
  pm.membership_status
FROM SignalingEntity e
JOIN SignalingPathwayMember pm ON pm.entity_id = e.entity_id
JOIN SignalingPathway p ON p.pathway_id = pm.pathway_id
WHERE e.canonical_name = 'X protein';
```

## Where Two Nodes Intersect

This returns shared pathway membership first, then direct edges touching either node. Use context columns to avoid treating a shared pathway label as proof of a direct interaction.

```sql
SELECT 'shared_pathway' AS route, p.pathway_name, NULL AS relation_type
FROM SignalingPathway p
JOIN SignalingPathwayMember pm_x ON pm_x.pathway_id = p.pathway_id
JOIN SignalingPathwayMember pm_y ON pm_y.pathway_id = p.pathway_id
JOIN SignalingEntity x ON x.entity_id = pm_x.entity_id
JOIN SignalingEntity y ON y.entity_id = pm_y.entity_id
WHERE x.canonical_name = 'X protein'
  AND y.canonical_name = 'X receptor'
UNION ALL
SELECT 'direct_edge', p.pathway_name, se.relation_type
FROM SignalingEdge se
LEFT JOIN SignalingPathway p ON p.pathway_id = se.pathway_id
JOIN SignalingEntity source_entity ON source_entity.entity_id = se.source_entity_id
JOIN SignalingEntity target_entity ON target_entity.entity_id = se.target_entity_id
WHERE (source_entity.canonical_name, target_entity.canonical_name)
      IN (('X protein', 'X receptor'), ('X receptor', 'X protein'));
```

## Knockout or Inhibition Phenotypes

```sql
SELECT
  p.title,
  sp.canonical_name AS perturbed_entity,
  esp.perturbation_type,
  ph.canonical_name AS phenotype,
  esph.effect_direction,
  o.observation_value,
  o.source_section,
  o.extraction_confidence
FROM Experiment_SignalingPerturbation esp
JOIN SignalingEntity sp ON sp.entity_id = esp.entity_id
JOIN Experiment e ON e.experiment_id = esp.experiment_id
JOIN Paper p ON p.paper_id = e.paper_id
LEFT JOIN Experiment_SignalingPhenotype esph ON esph.experiment_id = e.experiment_id
LEFT JOIN SignalingPhenotype ph ON ph.phenotype_id = esph.phenotype_id
LEFT JOIN Observation o ON o.observation_id = esph.observation_id
WHERE sp.canonical_name = 'X protein'
  AND esp.perturbation_type IN ('knockout', 'knockdown', 'inhibitor');
```

## Which TLRs Signal to a Transcription Factor?

The recursive form finds direct and multi-step routes while preserving the evidence status of each edge.

```sql
WITH RECURSIVE routes AS (
  SELECT
    se.source_entity_id,
    se.target_entity_id,
    se.edge_id,
    se.relation_type,
    1 AS depth,
    ARRAY[se.edge_id] AS edge_path
  FROM SignalingEdge se
  JOIN SignalingEntity source_entity ON source_entity.entity_id = se.source_entity_id
  WHERE source_entity.entity_type = 'receptor'
    AND source_entity.canonical_name LIKE 'TLR%'
  UNION ALL
  SELECT
    r.source_entity_id,
    se.target_entity_id,
    se.edge_id,
    se.relation_type,
    r.depth + 1,
    r.edge_path || se.edge_id
  FROM routes r
  JOIN SignalingEdge se ON se.source_entity_id = r.target_entity_id
  WHERE r.depth < 8
    AND NOT se.edge_id = ANY(r.edge_path)
)
SELECT
  receptor.canonical_name AS tlr,
  target_entity.canonical_name AS transcription_factor,
  routes.depth,
  routes.edge_path
FROM routes
JOIN SignalingEntity receptor ON receptor.entity_id = routes.source_entity_id
JOIN SignalingEntity target_entity ON target_entity.entity_id = routes.target_entity_id
WHERE target_entity.entity_type = 'transcription_factor'
ORDER BY receptor.canonical_name, routes.depth;
```

## Interpretation Rules

- A pathway member is not automatically a direct edge.
- A direct edge without observation provenance is a hypothesis or review context, not primary evidence.
- A knockout phenotype establishes necessity only in the tested species, cell type, ligand, compartment, and injury context.
- TLR4 surface/MyD88/TIRAP and endosomal/TRAM/TRIF routing must remain separate records.
