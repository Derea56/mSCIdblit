# Module 21A batch 045 review summary

## Scope

Reviewed exactly the 25 requested frozen Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0501` through `-0525`, in queue order. Queue membership and canonical pair labels were checked against `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`. No Module20A files, the frozen LR manifest, or shared Module21A registers were modified.

## Classification

- Exact rows reviewed: 25
- `reviewed_relay_candidate`: 23
- `reviewed_binding_only`: 1 (`GABA-GAD1_SLC6A11`–`Gabbr1`)
- `reviewed_unresolved`: 1 (`GABA-GAD1_SLC6A11`–`Gabbr2`)
- `reviewed_function_only`: 0
- Direct terminal TF assignments: 0

The 23 relay candidates are receptor-complex/pathway edges, not direct GAD1/SLC6A1/SLC6A11-to-receptor molecular interactions. Primary recombinant pharmacology supports GABA-evoked currents for the requested GABAA assemblies: alpha1beta2delta, alpha1beta2gamma2, alpha1beta3, alpha1beta3gamma2, alpha2beta3gamma2, alpha3beta3epsilon, alpha3beta3gamma2, alpha3beta3theta, alpha4beta2delta, alpha4beta3delta, alpha4beta3gamma2, alpha5beta3gamma2, alpha6beta3delta, and alpha6beta3gamma2. These were routed to the receptor-proximal relay layer with chloride/anion-channel and inhibitory-current branches.

GABBR1 and GABBR2 were kept distinct. GABBR1 is the principal orthosteric ligand-binding component, but does not by itself provide the complete surface signaling receptor; it was retained as `reviewed_binding_only`. GABBR2 is the principal G-protein-coupling component of the obligatory GABBR1–GABBR2 heterodimer, but standalone GABA→GABBR2 activation was not supported; it was retained as `reviewed_unresolved`. The assembled GABAB heterodimer is supported by GABA/Baclofen-dependent GIRK/PLC signaling studies, but that evidence was not misassigned to either singleton.

## Composite-label boundaries

GAD1 is the GABA biosynthetic enzyme. SLC6A1 and SLC6A11 are GABA transporters. Their synthesis and transport functions were not merged with receptor activation, and no direct molecular edge was inferred from the composite queue labels. GABAA receptor-family activation was not extended to any terminal transcription factor. No TF was directly measured in the cited receptor pharmacology studies.

## Search boundaries and limitations

Searches covered exact alpha/beta/gamma/delta/epsilon/theta receptor combinations, GABBR1/GABBR2 heterodimer notation, historical GB1/GB2 aliases, PubMed, PMC, publisher pages, and pathway/pharmacology resources. Primary sources were prioritized. Receptor-complex evidence was retained separately from ligand-binding and functional inhibition. Receptor isoform abundance, synaptic versus extrasynaptic localization, and neuronal network effects remain model- and species-dependent. Related alpha3beta1epsilon/theta evidence was used only as context for the exact alpha3beta3epsilon/theta rows and was not used as a substitute for exact-pair evidence.

## Files

- `work/module21_relay/module21a_batch045_review.tsv`
- `work/module21_relay/module21a_batch045_summary.md`
