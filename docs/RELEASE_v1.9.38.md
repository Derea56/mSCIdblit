# mSCIdblit v1.9.38

## Mechanism graph release

This release adds ten selectively curated primary-literature expansions to the Module 21B mechanism graph. The new routes cover GAS6–MERTK–GRB2, GDNF–GFRA1:RET–SHP2, MSP–MST1R/RON–GAB1, MSP–MST1R/RON–GRB2, Mdk–ALK–SHC1, SCF–KIT–SHP1, C1q–TREM2/DAP12–SHIP1, C1q–CD33–SHP1, C1q–CD33–SHP2, and MAG–PIR-B–SHP1.

All ten routes include a source-supported receptor-proximal intracellular continuation. The ALK, TREM2, CD33, and PIR-B routes explicitly retain composite evidence where the ligand–receptor input and downstream receptor/adaptor evidence come from separate bounded primary-literature layers. All ten routes remain evidence-only: no causal graph edge, confidence score, transcription factor, or target-gene endpoint is created.

The release contains 10 new literature-expansion rows and increases the materialized route-evidence table from 17,101 to 17,111 rows. The underlying mechanism graph topology is unchanged at 11,952 nodes and 14,722 edges. Evidence remains available to mSCS as `ligand>receptor>intracellular>????>output` or, for the receptor-only case, `ligand>receptor>????>????>output`.

Primary locators represented in this batch include PMID:18039660, PMID:20682772, PMID:21784853, PMID:17274988, PMID:9528781, PMID:20484116, PMID:10206955, PMID:10887109, PMID:9482905, PMID:18988857, and PMCID:PMC19370.
