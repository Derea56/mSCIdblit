# mSCIdblit release v1.9.334

Release ID: `module20_24_mechanism_graph:2026-09-25-all-ligand-full-sequence-promotion-queue-559`

This release reruns the complete source-linked all-ligand promotion family
against the current route evidence table. The sweep evaluates the full set of
1,862 ligand entries using target-gene, output-template, shared-anchor,
source-linked component, and pairwise source-overlap selectors. It adds 48
deduplicated literature-expansion records for the ADCYAP1/PACAP alias, each
retaining ligand, receptor, intracellular, TF, and target-gene layers with
composed-evidence and missing-handoff fields preserved.

No additional eligible rows were found for the remaining ligand entries under
the current exact source-linkage and primary-locator rules. This is therefore
the end of the automated promotion pass, not evidence that the remaining
ligands lack signaling literature; further expansion requires paper-level
review of the remaining queue.

No graph edges, causal assertions, or database confidence scores were created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 593,206 -> 593,254
- Literature-expansion rows: 27,092 -> 27,140
- Full-sequence curation candidates: 15,125 (unchanged)
- Unique ligands in the curation queue: 1,862 (unchanged)
- P1 review candidates: 9,306 (unchanged)
- Full target-gene ligands: 154 (unchanged)
- Partial downstream ligands: 1,541 (unchanged)

Validation passed with no errors. The inherited warning remains that some
evidence sources lack stable public locators.

Files:

- `data/processed/mechanism_graph_module20_24_v2026_09_24_literature_expansion559/`
- `docs/RELEASE_v1.9.334.md`
