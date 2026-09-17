# mSCIdblit Module 20B–24B mechanism graph v1.8.80

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-075`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion075/`

This seventy-fifth selective literature-expansion release adds ten bounded
endocrine and metabolite GPCR evidence routes: FSH–FSHR–GNAS,
LH–LHCGR–GNAS, TSH–TSHR–GNAS, ACTH–MC2R/MRAP1–GNAS,
kisspeptin–KISS1R–GNAQ/GNA11, dopamine–DRD1–GNAS, dopamine–DRD4–GNAI/O/Z,
lactate–HCAR1/GPR81–GNAI/O/Z, succinate–SUCNR1/GPR91–GNAI/O/Z, and bile
acids–GPBAR1/TGR5–GNAS.

Each annotation retains a primary ligand–receptor claim, a graph-linked
receptor-proximal continuation, and a measured second-messenger or cellular
functional output. The TF and terminal target-gene layers remain open for
mSCS. These are evidence-layer routes, not causal graph edges, and no
database confidence score or SCI-specific transfer is asserted. Context
boundaries include recombinant or transfected-cell assays, accessory-protein
requirements, tissue-specific physiology, non-exclusive GPCR coupling, and
metabolite or macrophage functional readouts.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,530 |
| Literature-expansion annotations in this batch | 10 |
| Cumulative literature-expansion annotations | 483 |
| Unique covered queue candidates | 467 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 140 |
| Cumulative L→R→TF→output annotations missing intracellular | 62 |
| Cumulative L→R→output-only annotations | 244 |
| Unused downstream queue candidates remaining | 2,864 |
| Unused P1 queue candidates remaining | 1,799 |

Primary studies represented include FSHR expression and cAMP bioassay
([PMID 8046308](https://pubmed.ncbi.nlm.nih.gov/8046308/)), TSHR cAMP
bioassay ([PMID 8227980](https://pubmed.ncbi.nlm.nih.gov/8227980/)),
MRAP-dependent MC2R binding and cAMP signaling
([PMID 17456795](https://pubmed.ncbi.nlm.nih.gov/17456795/)), D4 receptor
signaling ([PMID 7512953](https://pubmed.ncbi.nlm.nih.gov/7512953/)),
lactate sensing by HCAR1/GPR81
([PMID 18952058](https://pubmed.ncbi.nlm.nih.gov/18952058/)), succinate
sensing by SUCNR1/GPR91 ([PMID 15141213](https://pubmed.ncbi.nlm.nih.gov/15141213/)),
and bile-acid activation of GPBAR1/TGR5
([PMID 12524422](https://pubmed.ncbi.nlm.nih.gov/12524422/)).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors
and preserves all prior `LITEXP` overlay records.
