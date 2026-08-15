# Module 21A batch 050 review summary

Batch scope: exact Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0626` through `-0650`, in queue order. This batch review is isolated: shared Module21A registers, Module20A ledgers, and the frozen Module20A manifest were not modified.

## Classification

- 25/25 exact queue rows reviewed.
- 21 `reviewed_relay_candidate` rows: primary recombinant GABA-A receptor pharmacology directly measured GABA-evoked activity for the specified alpha/beta/gamma or delta/epsilon complex.
- 1 `reviewed_binding_only` row: GABA binding to the GABAB1 orthosteric component (`-0634`); productive GABA-B signaling requires the GABAB1-GABAB2 heterodimer.
- 3 `reviewed_unresolved` rows: standalone GABAB2 (`-0635`) and the rare alpha3beta3theta entries (`-0627`, `-0644`).
- 0 terminal TF assignments. GABA receptor subtype pharmacology, ion-channel currents, G-protein coupling, and receptor-complex structure were not promoted to transcription-factor evidence.

## Evidence handling

The GABA-A records use primary receptor-complex electrophysiology and pharmacology, including recombinant expression, whole-cell or single-channel recordings, two-electrode voltage clamp, concentration-response analysis, receptor assembly/stoichiometry studies, and subtype-selective modulation. These are retained as receptor-proximal relay branches: ligand-gated inhibitory anion current, phasic inhibition, or extrasynaptic tonic conductance.

The GABA-B records preserve the obligate heterodimer distinction. GABAB1 contains the principal orthosteric GABA-binding site, while GABAB2 supplies essential trafficking, conformational activation, and G-protein coupling in the assembled receptor. No standalone GABA-GABAB2 activation edge was inferred.

`GAD2` is retained as the GABA-biosynthetic enzyme. `SLC6A1` and `SLC6A11` are retained as GABA transport/clearance labels. They are not receptor subunits, and the composite CellChat ligand labels were not substituted for direct ligand evidence. The receptor-complex relay rows therefore describe the cognate transmitter GABA acting on the listed receptor complex, with the composite-label limitation recorded per row.

## Search boundary

Primary PubMed/PMC and stable DOI records were checked for exact receptor complexes and expanded receptor-family pharmacology. Representative primary support included recombinant alpha4beta2delta activation (PMID 14966300), alpha4beta3delta pharmacology (PMIDs 16272218 and 18762200), alpha6-containing receptor pharmacology (PMIDs 15696164, 12367596, and 18021290), alpha3beta3epsilon function (PMID 22319471; PMCID PMC3262152), and GABAB1/GABAB2 coupling and structural studies (PMIDs 16120656, 18165688, 22660477, and 32494023).

The exact alpha3beta3theta branch was searched using GABRA3/GABRB3/GABRQ aliases across PubMed, PMC, Europe PMC, publisher pages, and receptor-family terminology. No qualifying exact recombinant activation or receptor-dependent perturbation study was located, so alpha3beta3gamma2 and alpha3beta3epsilon evidence was not transferred. Search URLs are retained in the two unresolved TSV rows.

## Validation

- 25 rows; exact queue membership and queue order passed.
- 13 required TSV fields populated for every row.
- Review IDs unique.
- Frozen Module20A manifest SHA256 unchanged: `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Output

The exact batch TSV is [module21a_batch050_review.tsv](/Users/derea/Documents/SCI/mSCIdblit/work/module21_relay/module21a_batch050_review.tsv).
