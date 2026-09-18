# mSCIdblit v1.9.42

## Mechanism graph release

This release adds ten selectively curated primary-literature expansions to the Module 21B mechanism graph. The batch covers FcγRIIB–SHIP1, PD-1–SHP2, two NKG2D–DAP10 branches to PI3K p85 and Grb2/Vav1, two CEACAM1-L branches to SHP1 and SHP2, KIR2DL2–SHP1, KIR2DL4–SHP2, LAIR1–SHP2, and ILT7/LILRA4–FcRγ.

The routes preserve phosphosite, ITIM/ITSM, adaptor-complex, species, receptor-isoform, and assay-context limitations from the underlying studies. The NKG2D-DAP10 entries retain the overlapping p85 and Grb2/Vav1 branches rather than treating them as independent universal steps; the KIR, LAIR1, ILT7, and CEACAM1 entries retain their receptor- and model-specific caveats. All routes remain evidence-only; no causal graph edge, confidence score, transcription factor, or target-gene endpoint is created.

The release contains 10 new literature-expansion rows and increases the materialized route-evidence table from 17,141 to 17,151 rows. The underlying mechanism graph topology is unchanged at 11,952 nodes and 14,722 edges. The evidence layer now contains 1,104 selective literature-expansion routes and remains available to mSCS for route plausibility evaluation.

Primary locators represented in this batch include PMID:9234687, PMID:32184441, PMID:15240681, PMID:10426994, PMID:16582911, PMID:16887996, PMID:18424730, PMID:9916713, PMID:11994457, PMID:15100296, PMID:18048391, and PMID:19948503.
