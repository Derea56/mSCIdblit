# mSCIdblit release v1.9.310

Release ID: `module20_24_mechanism_graph:2026-09-24-all-ligand-curation-queue-511`

This release applies a conservative semantic repair to the all-ligand route
evidence layer and rebuilds the full-sequence curation queue. Nine existing
route transcription-factor nodes now carry an additional
`transcription_factor` role because they are already used in route TF fields
and have direct evidence-gated transcription-like graph edges. No graph edge,
route row, literature row, causal assertion, or confidence score was created
or rewritten.

The repaired bundle contains 2,613 ligand coverage rows. The derived audit
recognizes 179 ligands with at least one full
ligand→receptor→intracellular→transcription-factor→functional-output route and
59 with at least one full target-gene route. The all-ligand queue contains
15,078 deduplicated route signatures spanning 1,862 ligands and 1,633
receptors, including 9,302 P1 primary-literature curation candidates.

Validation passed with no errors. The remaining warning concerns evidence
sources without stable locators and remains unchanged from the source bundle.
