# mSCIdblit v1.9.44

## Mechanism graph release

This release adds ten selectively curated primary-literature expansions to the Module 21B mechanism graph. Four routes retain receptor-proximal continuation evidence: SCARB1/SR-BI–GULP1, FGFRL1 tandem phosphosite–SHP1, RET pY687–SHP2, and RET pY981–SRC. Six additional routes retain explicit ligand–receptor–output evidence for p-octopamine–TAAR1, T1AM–TAAR1, β-phenylethylamine–TAAR4, tyramine–TAAR4, isoamylamine–TAAR3, and cadaverine–TAAR13c.

The TAAR entries intentionally preserve the receptor/cAMP or reporter readout while marking intracellular continuation and transcription-factor layers as unassayed. The FGFRL1 entry retains the kinase-null, decoy-like and ligand-independent caveats, and the RET entries preserve co-receptor, isoform, and phosphosite boundaries. All routes remain evidence-only; no causal graph edge, confidence score, transcription factor, or target-gene endpoint is created.

The release contains 10 new literature-expansion rows and increases the materialized route-evidence table from 17,161 to 17,171 rows. The underlying mechanism graph topology is unchanged at 11,952 nodes and 14,722 edges. The evidence layer now contains 1,124 selective literature-expansion routes and remains available to mSCS for route plausibility evaluation.

Primary locators represented in this batch include PMID:19122200, PMID:23640895, PMCID:PMC3682584, PMID:20682772, PMCID:PMC2951258, PMID:14766744, PMID:11723224, PMID:15146179, PMID:26601069, PMID:16451074, PMID:11459929, PMID:16878137, and PMID:24218586.
