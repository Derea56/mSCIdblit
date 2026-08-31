# Database load audit

Observed on 2026-08-31 against the local PostgreSQL database
`mscidblit_local` through the configured local socket.

The additive migration and generated materialization SQL were each rerun
successfully. The second run produced no duplicate rows.

| Database table | Rows |
|---|---:|
| `EvidenceArtifact` | 2,753 |
| `EvidenceArtifactIdentifier` | 1,625 |
| `EvidenceArtifactRegisterCrosswalk` | 3,175 |

Crosswalk rows by module:

| Module | Crosswalk rows | Artifacts | Register sources |
|---|---:|---:|---:|
| 20B | 418 | 215 | 251 |
| 21B | 113 | 44 | 47 |
| 22B | 807 | 352 | 430 |
| 23B | 1,608 | 603 | 832 |
| 24B | 229 | 147 | 146 |

Integrity checks:

- orphan crosswalk rows: `0`;
- invalid SHA-256 values: `0`;
- duplicate artifact paths: `0`;
- existing canonical graph/evidence counts unchanged: 1,747 Papers, 1,763
  Experiments, 1,763 Observations, 1,763 AuthorClaims, 1,763 EvidenceLinks,
  3,399 SignalingEdges, and 5,087 SignalingEdgeSources;
- existing mechanism-role, database-release, and regulon validators: all
  issue counts `0`;
- isolated database-native graph export: 3,065 nodes, 4,980 node roles,
  3,399 edges, and 10,024 edge sources;
- isolated export TSVs for nodes, node roles, edges, and edge sources were
  byte-identical to the frozen v1.2.0 bundle.

The provenance layer does not alter canonical evidence grades, context levels,
graph edges, or canonical source-unit records.
