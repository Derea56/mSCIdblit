# mSCIdblit v1.9.40

## Mechanism graph release

This release adds ten selectively curated primary-literature expansions to the Module 21B mechanism graph. The batch covers phosphatidylserine–CD300A–SHP1, S100A9–LILRB1–SHP1, three FLT3 phosphosite–GRB2/GRB10 branches, three FLT3 phosphosite–LNK branches, and phosphatidylserine–CD300F pY276–p85/PI3K efferocytosis.

All ten routes include source-supported receptor-proximal intracellular continuations. The FLT3 entries preserve site-specific and joint-site limitations from the primary studies, including the distinction between GRB2/GAB2, GRB10, and LNK binding. The CD300A, LILRB1, and CD300F entries preserve surrogate-receptor, tandem-ITIM, orthology, and efferocytosis context. All routes remain evidence-only; no causal graph edge, confidence score, transcription factor, or target-gene endpoint is created.

The release contains 10 new literature-expansion rows and increases the materialized route-evidence table from 17,121 to 17,131 rows. The underlying mechanism graph topology is unchanged at 11,952 nodes and 14,722 edges. The evidence layer now contains 1,084 selective literature-expansion routes and remains available to mSCS for route plausibility evaluation.

Primary locators represented in this batch include PMID:22537350, PMID:22043923, PMID:11907092, PMID:24156302, PMID:19438505, PMCID:PMC5528487, PMCID:PMC3476541, PMID:21865548, PMID:24477292, PMCID:PMC3178745, and PMCID:PMC4151829.
