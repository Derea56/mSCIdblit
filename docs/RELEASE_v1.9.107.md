# mSCIdblit v1.9.107

## Gap-driven primary-literature expansion

This release adds six bounded route annotations selected from signaling gaps
where primary studies provide intracellular, transcriptional, functional or
inhibitory downstream support:

- Activin A > CRIPTO/ACVR2B > inhibited ALK4 reporter signaling
- FGF22 > FGFR1b > FRS2/PI3K-associated excitatory synapse formation
- FGF22 > FGFR2b > FRS2/PI3K-associated excitatory synapse formation
- PVR/CD155 > TIGIT > inhibitory NK-cell functional output
- CD80/B7-1 > CD28 > PI3K-associated T-cell costimulation
- VISTA/VSIR > PSGL-1 > checkpoint-associated T-cell inhibition

The routes use primary studies including PMID:12682303, PMID:18089557,
PMID:25926357, PMID:25766255, PMID:22421438, PMID:23154388,
PMID:7577804, PMID:9915850, PMID:7527824 and PMID:31645726. Complex or
comparator boundaries, model-specific outputs, inhibitory direction and
unresolved TF or target-gene layers remain explicit. These are evidence-layer
annotations only: no graph edges, causal traversals or confidence scores are
asserted.

## Release counts

- Route evidence records: 19,573 -> 19,579
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 6

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion202`.
