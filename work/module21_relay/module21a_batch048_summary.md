# Module 21A batch 048 review summary

## Scope

Reviewed exactly the 25 requested frozen Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0576` through `-0600`, in queue order. The batch contains the remaining `GABA-GAD1_SLC6A6` rows, the `GABA-GAD1_SLC6A8` rows, and `GABA-GAD2_SLC32A1 Gabbr1`.

No Module20A files, frozen LR manifest, or shared Module21A registers were modified.

## Classification

- Exact rows reviewed: 25
- `reviewed_relay_candidate`: 22
- `reviewed_binding_only`: 2 (`GABA-GAD1_SLC6A8`–`Gabbr1`; `GABA-GAD2_SLC32A1`–`Gabbr1`)
- `reviewed_unresolved`: 1 (`GABA-GAD1_SLC6A8`–`Gabbr2`)
- `reviewed_function_only`: 0
- Direct terminal TF assignments: 0

Primary recombinant pharmacology and receptor-complex studies support the 22 queued GABAA assemblies: alpha1beta2, alpha1beta2delta, alpha1beta2gamma2, alpha1beta3, alpha1beta3gamma2, alpha2beta3gamma2, alpha3beta3epsilon, alpha3beta3gamma2, alpha3beta3theta, alpha4beta2delta, alpha4beta3delta, alpha4beta3gamma2, alpha5beta3gamma2, alpha6beta3delta, and alpha6beta3gamma2, with repeated exact complexes appearing in the queue. These are receptor-complex/pathway edges in the receptor-proximal relay layer, with ligand-gated anion-channel, inhibitory-current, phasic-inhibition, or tonic-inhibition branches.

GABAB1 and GABAB2 were kept distinct from GABAA receptors. GABAB1 carries the principal orthosteric GABA-binding site but does not by itself form the complete surface signaling receptor, so both GABAB1 rows remain `reviewed_binding_only`. GABAB2 supplies G-protein coupling and trafficking in the obligatory GABAB1–GABAB2 heterodimer, but the cited studies do not support a standalone GABA→GABAB2 activation edge, so the singleton GABAB2 row remains `reviewed_unresolved`. Assembled GABAB heterodimer evidence was not assigned to either singleton.

## Composite-label boundaries

GAD1 and GAD2 are GABA biosynthetic enzymes. SLC6A6 and SLC6A8 are GABA transporters, and SLC32A1 is the vesicular GABA transporter. Their synthesis, uptake, or vesicular-loading functions were not merged with mature GABA receptor activation, and no direct molecular edge from a composite label to a receptor subtype was inferred. The GABAA relay classifications represent the underlying cognate GABA→receptor-complex evidence only.

No terminal transcription factor was directly measured in the cited receptor pharmacology or receptor-complex studies. Receptor subtype, channel current, tonic/phasic inhibition, and membrane-potential output were not used to infer a TF.

## Search boundaries and limitations

Searches covered exact alpha/beta/gamma/delta/epsilon/theta GABAA combinations, GABBR1/GABBR2 and historical GB1/GB2 aliases, PubMed, PMC, publisher records, and receptor-pharmacology context. Primary recombinant electrophysiology and receptor-complex studies were prioritized. Evidence for ligand binding, receptor-complex function, and functional inhibition was kept separate. Native subunit abundance, receptor stoichiometry, synaptic versus extrasynaptic localization, and network effects remain model- and species-dependent.

The central supporting studies include direct recombinant GABA-gated current measurements across synaptic and extrasynaptic GABAA isoforms (PMID 22319471; PMCID PMC3262152), alpha4beta2delta single-channel recordings (PMID 18227274; PMCID PMC2213567), alpha6-containing receptor pharmacology (PMID 18021290), and GABAB1/GABAB2 ligand-binding and coupling studies (PMID 22660477; PMID 11588177; PMID 16120656). Database or family-level context was not promoted as exact pair evidence.

## Files

- `work/module21_relay/module21a_batch048_review.tsv`
- `work/module21_relay/module21a_batch048_summary.md`
