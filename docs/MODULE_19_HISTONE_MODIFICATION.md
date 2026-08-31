# Module 19: Histone Modification Query Guide

Module 19 uses the shared graph to connect histone marks with writers, erasers, readers, loci, transcriptional programs, pathway intersections, and phenotypes.

## Find Writers, Erasers, or Readers for a Mark

```sql
SELECT
  source_entity.canonical_name AS regulator,
  se.relation_type,
  target_entity.canonical_name AS histone_mark,
  se.cell_type_context,
  se.compartment_context,
  se.evidence_status
FROM SignalingEdge se
JOIN SignalingEntity source_entity ON source_entity.entity_id = se.source_entity_id
JOIN SignalingEntity target_entity ON target_entity.entity_id = se.target_entity_id
WHERE target_entity.canonical_name = 'H3K27ac'
  AND source_entity.entity_type IN ('writer', 'eraser', 'reader');
```

## Find Genes or Enhancers Associated with a Mark

```sql
SELECT
  mark.canonical_name AS histone_mark,
  se.relation_type,
  locus.canonical_name AS locus,
  se.ligand_context,
  se.cell_type_context,
  se.injury_context,
  se.evidence_status
FROM SignalingEdge se
JOIN SignalingEntity mark ON mark.entity_id = se.source_entity_id
JOIN SignalingEntity locus ON locus.entity_id = se.target_entity_id
WHERE mark.entity_type = 'histone_mark'
  AND locus.entity_type IN ('gene', 'enhancer', 'promoter');
```

## Find Histone-Modifying Enzymes Intersecting a Pathway

```sql
SELECT
  regulator.canonical_name,
  se.relation_type,
  target.canonical_name,
  p.pathway_name,
  se.cell_type_context,
  se.injury_context
FROM SignalingEdge se
JOIN SignalingEntity regulator ON regulator.entity_id = se.source_entity_id
JOIN SignalingEntity target ON target.entity_id = se.target_entity_id
JOIN SignalingPathway p ON p.pathway_id = se.pathway_id
WHERE regulator.entity_type IN ('writer', 'eraser', 'reader')
  AND p.pathway_name = 'NLRP3 inflammasome';
```

## Compare Mark Perturbation Phenotypes

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
WHERE entity.canonical_name IN ('HDAC', 'p300', 'H3K9 lactylation', 'CITED2');
```

## Interpretation Rules

- A histone mark is not automatically activating or repressive without locus and cell-state context.
- Global mark abundance, locus occupancy, chromatin accessibility, and target-gene expression are separate evidence layers.
- Writer/eraser pharmacology may be pleiotropic; preserve target specificity and rescue evidence.
- Histone modification evidence can nominate a causal regulatory node without proving that the mark alone produces the phenotype.
