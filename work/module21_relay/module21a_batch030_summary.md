# Module 21A batch 030 summary

## Scope

Reviewed the 25 exact frozen Module20A priority-8 queue rows `M20A-CELLCHAT-REMAINING-0051` through `M20A-CELLCHAT-REMAINING-0075`:

- `5-HT-TPH1_SLC18A2`: HTR4, HTR5A, HTR6, HTR7
- `5-HT-TPH1_SLC6A4`: HTR1A, HTR1B, HTR1D, HTR1E, HTR1F, HTR2A, HTR2B, HTR2C, HTR3 complex, HTR4, HTR5A, HTR6, HTR7
- `5-HT-TPH2_SLC18A1`: HTR1A, HTR1B, HTR1D, HTR1E, HTR1F, HTR2A, HTR2B, HTR2C

## Classification

- 25/25 `reviewed_relay_candidate`
- 25/25 `receptor_proximal_relay`
- 0 terminal TF assignments
- 0 shared-register, Module20A-ledger, or frozen-manifest changes

The promoted content is the mature-serotonin receptor relay only. Primary receptor studies support subtype-specific activation and proximal signaling, including Gi/o–adenylyl cyclase inhibition for HTR1-family receptors, Gq/11–PLC/Ca2+/ERK for HTR2-family receptors, HTR3 ligand-gated cation-channel currents, and Gs–cAMP/PKA or Src–ERK branches for HTR4/6/7. Representative primary sources include PMID 8380639 for HTR1F, PMID 10498829 and PMCID PMC3380724 for HTR2 signaling, PMID 15831437/PMCID PMC4548296 for HTR3 assemblies, PMID 17377064 for HTR4–Src–ERK, PMID 12558985 for HTR5A, PMID 16865095/PMCID PMC1752021 for HTR6, and PMID 15339860/PMCID PMC1575348 for HTR7.

## Evidence separation and limitations

TPH1/TPH2 are biosynthetic enzymes; SLC18A1/SLC18A2 are vesicular monoamine transporters; and SLC6A4 is a serotonin reuptake transporter. The cited receptor assays used mature 5-HT, receptor-selective agonists, recombinant receptor systems, or receptor-dependent cellular perturbations. They did not manipulate the submitted enzyme/transporter module, measure its flux or release into the same receptor assay, or establish a direct molecular interaction between the processing component and the receptor. Those upstream processing/storage/reuptake claims therefore remain explicitly unresolved for the exact composite pair.

No study in this batch directly measured a terminal transcription factor. cAMP, Ca2+, ERK, PKC, PKA, ion-channel currents, hormone secretion, glycogenolysis, cell growth, and synaptic function were retained as relay or functional outputs only; none was converted into a TF edge by coexpression or pathway inference.

Search boundaries included exact composite strings, mature-serotonin plus receptor-subtype searches, PubMed, PMC, publisher pages, and GPCR pharmacology/pathway context. Reviews and nomenclature resources were used for orientation only; row-level support is anchored to primary receptor pharmacology or primary signaling studies. Negative conclusions are bounded to the searched exact composite pair and do not reject the underlying mature-5-HT receptor biology.

## Validation

- 25 unique review IDs and 25 exact queue memberships
- Required TSV header and fields present for every row
- All rows contain stable PMID, PMCID, DOI, or stable PubMed/PMC source locators
- No non-empty terminal TF field
- Frozen Module20A LR manifest SHA256 unchanged: `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`

Output: `module21a_batch030_review.tsv`
