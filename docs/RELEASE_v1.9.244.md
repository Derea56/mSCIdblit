# mSCIdblit release v1.9.244

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-all-ligand-target-promotions-367`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion367/`

## Target-gene route promotion

This release expands 61 individually addressable full-sequence evidence routes
from target-gene lists already present in the curated full-sequence queue. The
new routes cover IFN-I (30), IFN-γ (20), EPO (3), IL-21 (3), IL-6 (2), IL-15
(2), and IL-12/23 (1). Each retains the source-linked ligand, receptor,
intracellular continuation, TF, target-gene node, and primary locators.

The intracellular-to-TF and TF-to-target handoffs remain explicitly marked when
they are not represented as graph edges. These are evidence routes, not causal
chains: no graph edges, confidence scores, or universal target claims are
created. mSCS can therefore evaluate the route together with cell type,
species, assay, and context metadata.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 339,607 |
| Literature-expansion annotations | 5,939 |
| Full-sequence curation candidates | 7,742 |
| Full target-gene sequence routes | 424 |
| Normalized route nodes | 1,305,018 |
| Normalized route edges | 1,283,072 |

The release validator passed with zero errors. The only warning remains the
pre-existing stable-locator audit warning for some evidence-source rows.
