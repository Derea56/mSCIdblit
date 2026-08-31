# Module 18: Non-TLR DAMP Query Guide

Module 18 uses the shared signaling graph to connect damage-associated molecular patterns to non-TLR sensors, downstream programs, pathway intersections, and phenotypes.

## Find Sensors for a DAMP

```sql
SELECT
  source_entity.canonical_name AS damp,
  se.relation_type,
  target_entity.canonical_name AS sensor,
  se.cell_type_context,
  se.compartment_context,
  se.evidence_status
FROM SignalingEdge se
JOIN SignalingEntity source_entity ON source_entity.entity_id = se.source_entity_id
JOIN SignalingEntity target_entity ON target_entity.entity_id = se.target_entity_id
WHERE source_entity.canonical_name = 'HMGB1'
  AND target_entity.entity_type IN ('receptor', 'channel', 'inflammasome sensor', 'nucleic acid sensor');
```

## Find DAMPs That Converge on a Node

```sql
SELECT
  source_entity.canonical_name AS upstream_danger_signal,
  se.relation_type,
  target_entity.canonical_name AS convergence_node,
  se.pathway_id,
  se.evidence_status
FROM SignalingEdge se
JOIN SignalingEntity source_entity ON source_entity.entity_id = se.source_entity_id
JOIN SignalingEntity target_entity ON target_entity.entity_id = se.target_entity_id
WHERE target_entity.canonical_name = 'NLRP3'
ORDER BY upstream_danger_signal;
```

## Compare DAMP Knockout or Inhibition Phenotypes

```sql
SELECT
  p.title,
  entity.canonical_name AS perturbed_node,
  esp.perturbation_type,
  phenotype.canonical_name,
  esph.effect_direction,
  o.observation_value,
  o.extraction_confidence
FROM Experiment_SignalingPerturbation esp
JOIN SignalingEntity entity ON entity.entity_id = esp.entity_id
JOIN Experiment e ON e.experiment_id = esp.experiment_id
JOIN Paper p ON p.paper_id = e.paper_id
JOIN Experiment_SignalingPhenotype esph ON esph.experiment_id = e.experiment_id
JOIN SignalingPhenotype phenotype ON phenotype.phenotype_id = esph.phenotype_id
LEFT JOIN Observation o ON o.observation_id = esph.observation_id
WHERE esp.perturbation_type IN ('knockout', 'knockdown', 'inhibitor', 'neutralization')
  AND entity.canonical_name = 'RAGE';
```

## Find Non-TLR Intersections with TLRs

```sql
SELECT
  source_entity.canonical_name AS source_node,
  se.relation_type,
  target_entity.canonical_name AS target_node,
  se.cell_type_context,
  se.ligand_context,
  se.injury_context,
  se.evidence_status
FROM SignalingEdge se
JOIN SignalingEntity source_entity ON source_entity.entity_id = se.source_entity_id
JOIN SignalingEntity target_entity ON target_entity.entity_id = se.target_entity_id
WHERE (source_entity.entity_type IN ('DAMP', 'receptor', 'inflammasome sensor')
       AND target_entity.canonical_name LIKE 'TLR%')
   OR (target_entity.entity_type IN ('DAMP', 'receptor', 'inflammasome sensor')
       AND source_entity.canonical_name LIKE 'TLR%');
```

## Interpretation Rules

- Elevated DAMP concentration is not equivalent to receptor engagement.
- Sensor activation is not equivalent to a specific downstream death program without perturbation evidence.
- A shared target such as NLRP3 indicates convergence, not identical upstream biology.
- Comparator evidence should remain marked as comparator evidence rather than being promoted to direct SCI evidence.
