# mSCIdblit v1.9.37

## Mechanism graph release

This release adds ten selectively curated primary-literature expansions to the Module 21B mechanism graph. The new routes cover receptor-proximal intracellular continuations for ANGPT1–Tie2–Dok-R, GDNF–GFRA1:RET–Src/FRS2A/IRS1/DOK4/DOK5, FLT3L–FLT3–Src-family kinases/SHP2, and GAS6–AXL–PIK3R1/p85.

All ten routes are retained as traversable evidence routes with bounded cellular or activation outputs. None is promoted to a causal edge or assigned a transcription factor or target-gene endpoint. The evidence contract therefore represents these routes as `ligand>receptor>intracellular>????>output`, preserving the receptor-proximal support for downstream route plausibility while keeping unresolved layers explicit for mSCS confidence evaluation.

The release contains 10 new literature-expansion rows and increases the materialized route-evidence table from 17,091 to 17,101 rows. The underlying mechanism graph topology is unchanged: 11,952 nodes and 14,722 edges. This release does not add confidence scores.

Primary locators represented in this batch include PMID:12665569, PMID:14766744, PMID:16684964, PMID:11390647, PMID:11313948, PMID:11470823, and PMID:18346204, with PMCID support retained where present in the curated source records.

