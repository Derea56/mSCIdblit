# Module 21A SQL staging summary

Date: 2026-08-14

The audit-layer SQL staging script is prepared at `module21a_signaling_staging.sql`. It creates only Module 21A staging tables and imports the main register plus the preserved Q001 seed packet. It does not write Module 20A tables or simulator-facing core `SignalingEdge` rows.

The script preserves stable edge/evidence/perturbation IDs, source locators, species and cell/model context, confidence, evidence layers, and unresolved cases. Database-side assertions check expected counts, evidence coverage, edge-layer references, and cross-packet edge-key uniqueness.

Static payload validation passed before staging generation:

- 110 combined edges
- 50 combined evidence records
- 54 combined perturbation records
- 45 evidence-layer rows
- 10 unresolved cases
- every edge evidence-backed
- every layer row references an edge and evidence record
- Module 20A manifest SHA-256 unchanged: `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`

Runtime execution against a temporary PostgreSQL cluster was attempted but could not initialize because the sandbox disallows the PostgreSQL shared-memory segment required by `initdb`. The SQL remains ready for execution in a normal PostgreSQL environment.

