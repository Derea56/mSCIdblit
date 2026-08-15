# Module 21A batch 051 review summary

Batch scope: exact Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0651` through `-0675`, in queue order. Shared Module21A registers, Module20A ledgers, and the frozen Module20A manifest were not modified.

## Classification

- 25/25 exact queue rows reviewed.
- 21 `reviewed_relay_candidate` rows: primary recombinant GABAA receptor-complex studies directly measured GABA-evoked channel activity for the specified alpha/beta/gamma, delta, epsilon, or theta assemblies.
- 2 `reviewed_binding_only` rows (`-0651`, `-0668`): GABA binding to the GABAB1 orthosteric ligand-binding component; productive GABAB signaling requires the GABAB1/GABAB2 heterodimer.
- 2 `reviewed_unresolved` rows (`-0652`, `-0669`): standalone GABAB2; GABAB2 contributes trafficking and G-protein coupling in the assembled receptor but is not the principal orthosteric GABA-binding component.
- 0 terminal TF assignments. GABA-A channel currents, GABA-B receptor-complex coupling, and subtype pharmacology were not promoted to transcription-factor evidence.

## Evidence handling

The GABAA records use primary receptor-complex pharmacology and electrophysiology, including recombinant expression, whole-cell or single-channel recordings, two-electrode voltage clamp, assembly/stoichiometry studies, and subtype-selective modulation. These are receptor-proximal relay or receptor-complex/pathway edges leading to ligand-gated anion-channel current, phasic inhibition, or extrasynaptic tonic conductance—not downstream TF edges.

The GABAB records preserve the obligate-complex distinction. GABAB1 carries the principal Venus-flytrap orthosteric site, while GABAB2 contributes surface trafficking and G-protein coupling in the assembled GABAB1/GABAB2 heterodimer. No standalone GABAB2 activation edge was inferred.

`GAD2` is retained as the GABA-biosynthetic enzyme. `SLC6A12` and `SLC6A13` are retained as source-label transport components. None was treated as a GABA receptor subunit or as evidence that the receptor complex is activated. No receptor subtype was assigned a terminal TF without a direct TF assay.

## Search boundary

Primary PubMed/PMC/DOI records were checked for the exact GABAB1/GABAB2 receptor mechanism and the specified GABAA complexes. Evidence was reused across the two source-label contexts only where the receptor-complex edge was directly tested; GAD2, SLC6A12, and SLC6A13 were not used to strengthen receptor claims. Native assembly, cell-type localization, tonic versus phasic interpretation, and network effects remain model-dependent limitations.

## Output

The exact TSV is [module21a_batch051_review.tsv](/Users/derea/Documents/SCI/mSCIdblit/work/module21_relay/module21a_batch051_review.tsv).
