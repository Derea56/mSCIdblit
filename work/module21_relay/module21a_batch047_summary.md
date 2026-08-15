# Module 21A batch 047 review summary

## Scope

Reviewed exactly the 25 requested frozen Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0551` through `-0575`, in queue order. The batch contains 15 `GABA-GAD1_SLC6A13` rows (0551–0565) and 10 `GABA-GAD1_SLC6A6` rows (0566–0575). No Module20A files, frozen LR manifest, or shared Module21A registers were modified.

## Classification

- Exact rows reviewed: 25
- `reviewed_relay_candidate`: 23
- `reviewed_binding_only`: 1 (`GABA-GAD1_SLC6A6`–`Gabbr1`)
- `reviewed_unresolved`: 1 (`GABA-GAD1_SLC6A6`–`Gabbr2`)
- `reviewed_function_only`: 0
- Direct terminal TF assignments: 0

Primary recombinant pharmacology supports GABA-evoked currents and receptor-complex function for the 23 queued GABAA assemblies: alpha1beta2, alpha1beta2delta, alpha1beta2gamma2, alpha1beta3, alpha1beta3gamma2, alpha2beta3gamma2, alpha3beta3epsilon, alpha3beta3gamma2, alpha3beta3theta, alpha4beta2delta, alpha4beta3delta, alpha4beta3gamma2, alpha5beta3gamma2, alpha6beta3delta, and alpha6beta3gamma2. These are receptor-complex/pathway edges in the receptor-proximal relay layer, with ligand-gated anion-channel, inhibitory-current, phasic-inhibition, or tonic-inhibition branches.

GABBR1 and GABBR2 were kept distinct from GABAA receptors. GABBR1 carries the principal orthosteric GABA-binding site but does not by itself form the complete surface signaling receptor, so it remains `reviewed_binding_only`. GABBR2 supplies G-protein coupling in the obligatory GABBR1–GABBR2 heterodimer, but the cited studies do not support a standalone GABA→GABBR2 activation edge, so it remains `reviewed_unresolved`. Assembled GABAB heterodimer evidence (GIRK/PLC coupling) was not assigned to either singleton.

## Composite-label boundaries

GAD1 is the GABA biosynthetic enzyme. SLC6A13 and SLC6A6 are GABA transporters. Their synthesis and transport functions were not merged with GABAA or GABAB receptor activation, and no direct molecular edge from the composite labels to a receptor subtype was inferred. No terminal transcription factor was directly measured in the cited receptor pharmacology or receptor-complex studies.

## Search boundaries and limitations

Searches covered exact alpha/beta/gamma/delta/epsilon/theta GABAA combinations, GABBR1/GABBR2 and historical GB1/GB2 aliases, PubMed/PMC/publisher records, and receptor-pharmacology context. Primary recombinant electrophysiology and receptor-complex studies were prioritized. Receptor-complex evidence was retained separately from ligand-binding and functional inhibition. Native subunit abundance, receptor stoichiometry, synaptic versus extrasynaptic localization, and network effects remain model- and species-dependent. Family-level transport, synthesis, and assembled GABAB heterodimer evidence was used only to document boundaries and limitations.

## Files

- `work/module21_relay/module21a_batch047_review.tsv`
- `work/module21_relay/module21a_batch047_summary.md`
