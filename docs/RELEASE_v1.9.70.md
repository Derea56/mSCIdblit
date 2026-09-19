# mSCIdblit v1.9.70

## Gap-driven primary-literature expansion

This release adds four evidence-layer routes from the EPO/EPOR/JAK2/STAT5
signaling module to direct pSTAT5-associated target-gene outputs reported in
primary murine erythroid cells:

- EPO > EPOR > JAK2 > STAT5 > PIM1
- EPO > EPOR > JAK2 > STAT5 > CLINT1
- EPO > EPOR > JAK2 > STAT5 > RBM25
- EPO > EPOR > JAK2 > STAT5 > SUV420H2

All four routes are supported by the primary EPO-induced pSTAT5 ChIP-seq and
nascent-transcription study (PMID:28732065; PMCID:PMC5521770). The routes use
existing graph edges and add no causal edges or database confidence scores.
They preserve the murine erythroid context and do not assert SCI transfer or
universal EPOR behavior.

This expansion also illustrates why an empty automated candidate queue is not
equivalent to an exhausted signaling literature: the target-gene edges were
already present, but the EPO-to-target route annotations had not been joined.

## Release counts

- Route evidence records: 19,441 -> 19,445
- Strict full-route annotations: 42 -> 46
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 4

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion165`.
