# Module 21A batch 052 review summary

Batch scope: exact Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0676` through `-0700`, in queue order. No shared Module21A registers, Module20A ledgers, or frozen manifest were modified.

## Classification

- 25/25 exact queue rows reviewed.
- 19 `reviewed_relay_candidate`: primary recombinant GABAA receptor-complex studies measured GABA-evoked currents or subtype-specific receptor pharmacology for the submitted alpha/beta/delta/gamma assemblies.
- 1 `reviewed_binding_only`: GABA binding at the GABAB1 orthosteric component, with productive signaling requiring the GABAB1-GABAB2 heterodimer.
- 5 `reviewed_unresolved`: GABAB2 as a standalone submitted receptor component, and the rare exact alpha3beta3epsilon/alpha3beta3theta combinations where available primary studies test related assemblies rather than the exact submitted complex.
- 0 terminal TF assignments.

## Evidence decisions

The GABAA relay rows are receptor-complex/pathway edges only: GABA activates the assembled ligand-gated anion channel, producing inhibitory membrane current, phasic inhibition, or extrasynaptic tonic inhibition. These rows do not infer intracellular kinase pathways or transcription-factor endpoints from subtype pharmacology.

GABAB1 and GABAB2 were kept distinct. GABAB1 carries the principal orthosteric GABA-binding site, whereas GABAB2 supplies the principal G-protein-coupling role in the obligatory heterodimer. The GABAB2 row therefore remains unresolved as a standalone ligand-receptor edge even though the assembled heterodimer is well supported.

GAD2, SLC6A13, and SLC6A6 were treated as biosynthetic or transport/reuptake context. They were not treated as the ligand, receptor subunits, or part of the receptor-proximal relay.

The exact alpha3beta3epsilon and alpha3beta3theta rows were not promoted from family or review evidence. Primary evidence includes related alpha3beta1epsilon/theta and other epsilon-containing assemblies, while the comparative GABAA review reports the rare alpha3beta3epsilon/theta combinations. The review was retained as a search-boundary citation, not as sole primary proof for the exact submitted pairs.

## Validation

- 25 unique review IDs.
- Queue IDs and canonical pair labels match the requested source rows in order.
- Required TSV fields are populated, including stable citations, species/model, assay, relation type, evidence layer, pathway branch, confidence, limitations, and terminal TF field.
- No TF was assigned because no exact batch record directly measured a terminal TF.
- Frozen Module20A manifest SHA256 remains `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Search boundary

Searches covered exact composite labels, canonical GABA, GABAA/GABAB nomenclature, alpha/beta/gamma/delta/epsilon/theta receptor assemblies, PubMed/PMC records, and primary recombinant electrophysiology/pharmacology. Pathway and receptor-family resources were used only to resolve nomenclature and complex architecture; they were not promoted as exact-pair evidence. Expression-only, transporter/enzyme, family-level, noncognate-subunit, and review-only evidence was retained as limitation context.
