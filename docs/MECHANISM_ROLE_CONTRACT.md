# Mechanism role contract

This contract makes mechanism labels queryable by explicit role while keeping
the evidence gate and composite-label policy intact. It is shared by the
mSCIdblit release bundle, the database-native mechanism layer, and mSCS.

## Allowed roles

| Role | Meaning | Required evidence rule |
|---|---|---|
| `ligand` | A signaling input that participates in a ligand-receptor edge. | Add only when the register or curated mapping explicitly supports ligand status. |
| `receptor` | A receptor or receptor complex at a ligand-receptor edge. | Add only when the register or curated mapping explicitly supports receptor status. |
| `transcription_factor` | A TF or explicitly curated TF complex/program used as a regulatory source. | Add only for an evidence-backed TF role; do not infer from a name alone. |
| `target_gene` | A gene-level target of a canonical TF-target edge. | Add only for a target endpoint in an evidence-backed target-gene relation. |
| `signaling_cascade` | Baseline participation in the released mechanism graph. | Every non-retired graph node must have this role; it does not imply activation or a molecular subtype. |

Roles are many-to-many. A node may carry `signaling_cascade` plus one or more
specialized roles. Composite labels remain intact (for example,
`TGFBR1-TGFBR2 receptor complex` or `SMAD2/3;SMAD4`); the role table must not
silently split them into unsupported entities.

## Edge contract

Use canonical relation types when an edge is intended to support role-aware
queries:

- `binds_receptor`: source has `ligand`; target has `receptor`.
- `regulates_target_gene`, `induces_target_gene`, or
  `represses_target_gene`: source has `transcription_factor`; target has
  `target_gene`.

The original register relation is retained as an audit field in the release
bundle. Other edges may still connect signaling-cascade nodes without claiming
one of these specialized endpoint roles.

## Bundle and database representations

The release bundle uses `mechanism_node_roles.tsv` with these required columns:

```text
node_id    role    role_source    role_evidence
```

The database authority is `SignalingEntityRole`, added by
`schema/mechanism_roles_layer.sql`. It stores role status, provenance, source
registry/version, and an export gate. `SignalingEntity.entity_type` remains a
legacy single-valued field and is not the authority for role-aware queries.

For an already materialized database graph, the safe idempotent derivation is
`scripts/materialize_mechanism_roles.sql`. It derives only the baseline and
canonical relation-implied roles, uses `ON CONFLICT DO NOTHING`, and does not
overwrite curated mappings. Run it before
`scripts/validate_mechanism_roles.sql`.

The current Module 20B–24B release is register-backed and intentionally keeps
`canonical_database_materialization=false`. The migration defines the safe
database contract; a database-native export should populate `SignalingEntity`
and `SignalingEntityRole` through an explicit, reviewable entity-mapping step
before running `scripts/validate_mechanism_roles.sql`.

## Query pattern

Once the role layer and canonical edges are materialized, a downstream query can
ask for the complete typed neighborhood of a signaling input without treating
all connected nodes as TFs or genes:

```sql
SELECT
  source.canonical_name AS source_name,
  edge.relation_type,
  target.canonical_name AS target_name,
  source_role.role AS source_role,
  target_role.role AS target_role,
  edge.pathway_id,
  edge.evidence_status
FROM SignalingEdge AS edge
JOIN SignalingEntity AS source ON source.entity_id = edge.source_entity_id
JOIN SignalingEntity AS target ON target.entity_id = edge.target_entity_id
JOIN SignalingEntityRole AS source_role
  ON source_role.entity_id = source.entity_id
 AND source_role.role_status <> 'retired'
JOIN SignalingEntityRole AS target_role
  ON target_role.entity_id = target.entity_id
 AND target_role.role_status <> 'retired'
WHERE source.canonical_name = 'TGFB1'
ORDER BY edge.pathway_id, edge.relation_type, target.canonical_name;
```

For production mSCS exports, keep the role table as the authority and emit
`node_type` only for backward compatibility. Run both the graph validator and
the database validator as release gates.
