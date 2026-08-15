# Module 21A batch 049 review summary

Batch scope: exact Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0601` through `-0625`, in queue order. Shared Module21A registers, Module20A ledgers, and the frozen Module20A manifest were not modified.

## Classification

- 25/25 exact queue rows reviewed.
- 22 `reviewed_relay_candidate` rows: recombinant or heterologous primary studies directly measured GABA-evoked activity of the specified GABAA receptor complex.
- 1 `reviewed_binding_only` row: GABA binding to the GABAB1 ligand-binding component (`-0617`); productive signaling requires the GABAB1/GABAB2 heterodimer.
- 2 `reviewed_unresolved` rows: standalone GABAB2 entries (`-0601`, `-0618`); GABAB2 supplies coupling/trafficking in the assembled receptor but is not the principal orthosteric GABA-binding component.
- 0 terminal TF assignments. GABA receptor subtype pharmacology and membrane-current measurements were not promoted to transcription-factor evidence.

## Evidence handling

The GABAA rows use primary receptor-complex pharmacology and electrophysiology, including recombinant expression, whole-cell or single-channel current recordings, two-electrode voltage clamp, stoichiometry/assembly studies, and subtype-selective modulation. The retained branches are receptor-proximal: ligand-gated anion-channel current, phasic inhibition, or extrasynaptic tonic conductance.

The GABAB rows preserve the obligate receptor-complex distinction. GABAB1 carries the principal Venus-flytrap orthosteric site, while GABAB2 contributes trafficking and G-protein coupling in the assembled GABAB1/GABAB2 heterodimer. No standalone GABAB2 activation edge was inferred.

`GAD2` is retained as the GABA-biosynthetic enzyme and `SLC32A1`/`SLC6A1` as transport machinery. None was treated as a GABA receptor component or as evidence of receptor activation. No receptor subtype was assigned a terminal TF without a direct TF assay.

## Search boundary

Primary literature was checked through stable PubMed/PMC/DOI records for the exact receptor complexes and their GABA-evoked currents or GABAB heterodimer mechanisms. Evidence was reused across the two source-label contexts only because the receptor-complex edge was directly tested; source/enzyme and transporter labels were not used to strengthen the receptor claim. Native assembly, cell-type localization, and network effects remain model-dependent limitations.

## Output

The exact TSV is [module21a_batch049_review.tsv](/Users/derea/Documents/SCI/mSCIdblit/work/module21_relay/module21a_batch049_review.tsv).
