# mSCIdblit release v1.9.386

This release adds five primary-literature evidence routes for ligands that had
receptor-linked downstream observations but lacked an addressable route record
for mSCS plausibility analysis.

The additions cover VEGFA→KDR→ERK→EGR1→tissue-factor output, HGF→MET→ERK→AP-1
transcriptional output, two WNT5B→FZD2→JNK→NF-kB target-gene outputs (Il6 and
CXCL8), and CXCL12→CXCR4→ERK dendritic-cell chemotaxis/survival output. The
routes retain primary locators and model-specific limitations from PMID:11149911,
PMID:11387210, PMID:11071904, PMID:15218027, PMID:27036869,
PMID:21878648, and PMID:28325822.

The WNT5B records are target-gene-expression routes. The VEGFA and HGF records
are transcription-factor-to-functional-output routes without a named terminal
target gene. The CXCL12 record is an intracellular-to-functional-output route
without a transcription-factor assertion. Missing handoffs remain explicit in
`missing_layers`; no causal graph edge, traversal permission, SCI transfer, or
database confidence score is created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 597,189 → 597,194
- Route nodes: 2,506,517 → 2,506,538
- Route edges: 2,305,095 → 2,305,111
- Literature-expansion rows: 31,075 → 31,080
- Full-sequence curation candidates: 15,525 (unchanged)
- Unique ligands in the curation queue: 1,872 (unchanged)
- Coverage summary: 182 full functional-output, 176 → 177 full target-gene,
  1,453 → 1,452 partial downstream, and 802 ligand–receptor-only ligand rows
- Route tiers added: two `ligand_receptor_intracellular_tf_target_missing_direct_tf_edges`,
  two `ligand_receptor_intracellular_tf_output_missing_target_gene`, and one
  `ligand_receptor_intracellular_output_missing_tf`

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators; those rows retain their limitations for review.

The literature-expansion table is mSCS-compatible: all 31,080 rows use the
importer-required `curated_primary_route` status. Four inherited PACAP alias
rows retain their alias-specific evidence semantics in `route_linkage_status`;
the release metadata records this compatibility normalization.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion627/`

For GitHub distribution, the literature-expansion table is stored as
`mechanism_literature_expansion.tsv.gz`; downstream mSCS table resolution
accepts this compressed form as the logical literature-expansion table.

## Lineage and consolidation

This bundle is the consolidated child of release
`module20_24_mechanism_graph:2026-09-25-literature-expansion-626`. The parent
bundle remains available as the historical release baseline; the current
bundle contains the complete graph and route tables needed for import, so
intermediate curation queue snapshots are not release inputs. Their cleanup
manifest records the exact temporary filenames and hashes before removal.
