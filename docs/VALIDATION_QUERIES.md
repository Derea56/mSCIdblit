# Validation Queries

Use these checks after each curation batch. Most queries should return zero rows; exceptions are noted.

## Papers Missing Core Curation

```sql
SELECT p.paper_id, p.title
FROM Paper p
LEFT JOIN ResearchQuestion rq ON p.paper_id = rq.paper_id
WHERE rq.question_id IS NULL;
```

## Experiments Missing Required Context

```sql
SELECT e.experiment_id, p.title, e.figure_table_reference
FROM Experiment e
JOIN Paper p ON e.paper_id = p.paper_id
LEFT JOIN Experiment_Species es ON e.experiment_id = es.experiment_id
LEFT JOIN Experiment_InjuryModel eim ON e.experiment_id = eim.experiment_id
WHERE es.species_id IS NULL
   OR eim.injury_model_id IS NULL;
```

## Observations Missing Source Provenance

```sql
SELECT o.observation_id, p.title, e.figure_table_reference, o.observation_value
FROM Observation o
JOIN Experiment e ON o.experiment_id = e.experiment_id
JOIN Paper p ON e.paper_id = p.paper_id
WHERE o.source_section IS NULL
   OR (o.source_quote IS NULL AND o.figure_panel_reference IS NULL);
```

## Claims Missing Evidence Links

```sql
SELECT ac.claim_id, p.title, ac.claim_text
FROM AuthorClaim ac
JOIN Paper p ON ac.paper_id = p.paper_id
LEFT JOIN EvidenceLink el ON ac.claim_id = el.claim_id
WHERE el.link_id IS NULL;
```

## Observations Not Used By Claims

This can return legitimate rows when observations are extracted before claims.

```sql
SELECT o.observation_id, p.title, o.observation_value, o.unit
FROM Observation o
JOIN Experiment e ON o.experiment_id = e.experiment_id
JOIN Paper p ON e.paper_id = p.paper_id
LEFT JOIN EvidenceLink el ON o.observation_id = el.observation_id
WHERE el.link_id IS NULL;
```

## Open Curator Notes

```sql
SELECT note_id, note_type, note_text, created_at
FROM CuratorNote
WHERE resolved = FALSE
ORDER BY created_at;
```

## Module Pass Status

```sql
SELECT
  cp.pass_code,
  cp.pass_name,
  pcs.status,
  COUNT(*) AS paper_count
FROM PaperCurationStatus pcs
JOIN CurationPass cp ON pcs.pass_id = cp.pass_id
GROUP BY cp.pass_code, cp.pass_name, cp.sort_order, pcs.status
ORDER BY cp.sort_order, pcs.status;
```

## Consensus With Thin Evidence

Consensus should not be created from a single source.

```sql
SELECT consensus_id, topic, consensus_statement, num_supporting_papers
FROM Consensus
WHERE COALESCE(num_supporting_papers, 0) < 2;
```
