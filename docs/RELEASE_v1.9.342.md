# mSCIdblit release v1.9.342

Release ID: `module20_24_mechanism_graph:2026-09-25-jak-stat-relay-promotion-queue-575`

This release promotes 781 existing primary-evidence route records across 21
ligands where the ligand, receptor, transcription factor, and target gene were
already curated but the intracellular continuation was left unresolved. The
promotion covers compatible JAK/STAT and MyD88/NF-kappaB relay annotations and
keeps all receptor-to-relay and relay-to-TF handoffs explicitly unasserted.
Five records with no defensible relay in the current graph remain partial.

This is an evidence-layer composition. No graph edge, causal assertion, or
database confidence score was created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 593,268 -> 594,049
- Literature-expansion rows: 27,154 -> 27,935
- Full-sequence curation candidates: 15,135 -> 15,139
- Unique ligands in the curation queue: 1,863 (unchanged)
- P1 review candidates: 9,306 (unchanged)
- Full target-gene ligands: 163 (unchanged)
- Full functional-output ligands: 110 (unchanged)
- Partial downstream ligands: 1,533 (unchanged)

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion575/`
- `scripts/build_jak_stat_relay_promotion_routes.py`
- `docs/RELEASE_v1.9.342.md`
