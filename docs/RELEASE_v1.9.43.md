# mSCIdblit v1.9.43

## Mechanism graph release

This release adds ten selectively curated primary-literature expansions to the Module 21B mechanism graph. The batch covers LepRb–SHP2, SIRPβ1–DAP12, NKp44–DAP12, NKG2C–DAP12, KIR2DL4–FcRγ, CLEC9A–SYK, VSTM1/SIRL1–SHP1, VSTM1/SIRL1–SHP2, and two CD36 multicomponent-complex branches to FcRγ and SYK.

The routes preserve receptor-adaptor, hemITAM/ITIM, ligand-context, species, cell-type, and assay limitations from the underlying studies. The CD36 entries explicitly retain integrin/tetraspanin/FcRγ assembly and indirect ITAM/SYK coupling rather than asserting binary CD36–adaptor or CD36–SYK binding. All routes remain evidence-only; no causal graph edge, confidence score, transcription factor, or target-gene endpoint is created.

The release contains 10 new literature-expansion rows and increases the materialized route-evidence table from 17,151 to 17,161 rows. The underlying mechanism graph topology is unchanged at 11,952 nodes and 14,722 edges. The evidence layer now contains 1,114 selective literature-expansion routes and remains available to mSCS for route plausibility evaluation.

Primary locators represented in this batch include PMID:10449753, PMID:10604985, PMID:10049942, PMID:9625766, PMID:9655483, PMID:15778339, PMID:19219027, PMID:20375307, and PMCID:PMC3586299.
