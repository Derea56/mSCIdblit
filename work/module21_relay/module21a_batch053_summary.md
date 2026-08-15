# Module 21A batch 053 review summary

Batch scope: exact requested priority-8 queue IDs `M20A-CELLCHAT-REMAINING-0701` through `-0719`, `-0720` through `-0723`, and `-0741` through `-0742`. The output contains 25/25 exact queue rows. No shared Module 21A registers, Module 20A ledgers, or frozen manifest were modified.

## Queue-membership note

The current queue does not contain 19 GABA-GAD2_SLC6A8 GABAA-complex rows. IDs `-0701` through `-0718` are the 18 GABA-GAD2_SLC6A8 rows: two GABAB component rows (`Gabbr1`, `Gabbr2`) and 16 GABAA-complex rows. ID `-0719` is an exact queue row, but its pair is `Gast-Adgrg1`, not a GABA row. It was retained and reviewed as unresolved so the requested 25-row exact queue span is complete.

## Classification

- 16 `reviewed_relay_candidate` GABAA receptor-complex rows (`-0701`, `-0704`–`-0718`): primary recombinant electrophysiology and concentration-response studies directly measured GABA-evoked currents for the specified alpha/beta/gamma, delta, epsilon, or theta assemblies.
- 1 `reviewed_binding_only` GABAB1 row (`-0702`): GABA-site evidence maps to the GABAB1 Venus-flytrap component; productive signaling requires the assembled GABAB1/GABAB2 heterodimer.
- 1 `reviewed_unresolved` standalone GABAB2 row (`-0703`): GABAB2 supplies trafficking and G-protein coupling in the assembled receptor but is not the principal orthosteric GABA-binding component.
- 1 `reviewed_unresolved` `Gast-Adgrg1` row (`-0719`): exact-pair search did not locate qualifying binding, receptor-dependent perturbation, or downstream functional evidence.
- 2 `reviewed_relay_candidate` glucagon receptor rows (`-0720`, `-0722`): glucagon-GCGR signaling and low-affinity glucagon-to-GLP-1R cross-activation were supported by primary cAMP, antagonist, and islet-function studies.
- 2 `reviewed_unresolved` glucagon cross-receptor rows (`-0721`, `-0723`): exact glucagon-GIPR and glucagon-GLP-2R activation was not promoted; receptor-family similarity and related-peptide evidence were retained only as boundaries.
- 2 `reviewed_function_only` connexin rows (`-0741`, `-0742`): Cx43 homotypic and Cx43/Cx40 heterotypic gap-junction channel function was retained as direct intercellular coupling evidence, not ligand-receptor signaling.
- 0 terminal TF assignments. GABAA currents, GABAB complex assembly, class-B GPCR cAMP responses, and gap-junction conductance were not promoted to TF evidence.

## Evidence handling

`GAD2` was treated as the GABA-biosynthetic enzyme and `SLC6A8` as a creatine transporter label. Neither was treated as a GABA receptor subunit or as evidence that the listed receptor complex was activated. For GABAA rows, the receptor-complex/pathway edge is the experimentally measured GABA-evoked channel current; no downstream transcriptional endpoint was inferred.

For glucagon, `Gcg-Gcgr` is a cognate receptor-proximal cAMP/PKA/Gq branch. `Gcg-Glp1r` is retained as a context-dependent, lower-affinity cross-activation relay in rat islets, with GLP-1R antagonist blockade of high-concentration glucagon effects. `Gcg-Gipr` and `Gcg-Glp2r` remain unresolved/negative specificity boundaries because the reviewed primary studies did not establish the exact edge.

For connexins, the relation is direct channel formation and functional intercellular coupling. Cx43/Cx43 homotypic conductance and Cx43/Cx40 heterotypic conductance were kept in the functional layer; no receptor-proximal kinase or TF pathway was inferred.

## Search boundary

Primary PubMed/PMC and publisher records were checked for the exact GABAA/GABAB assemblies, glucagon receptor-family selectivity and signaling, and Cx43/Cx40 channel function. Key primary records include the recombinant GABAA subtype panel (PMID 22319471), alpha4beta3gamma2 kinetics (PMID 17124266), alpha6beta3delta function (PMID 19765192), glucagon/GLP-1R cross-activation in rat islets (PMID 34896391), GLP-2R ligand selectivity (PMID 9990065), and Cx43/Cx40 heterotypic conductance (PMID 25483586). Database/family context was not used to promote an exact pair.

## Output

The exact TSV is `work/module21_relay/module21a_batch053_review.tsv`. This batch is intentionally review-only; no shared-register or SQL materialization changes were made.
