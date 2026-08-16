# Module 21A batch 223 review summary

## Scope

Reviewed exactly 25 currently queued Module 20A pairs, preserving the supplied
pair labels and the Module 21A review schema. This batch covers neuroligin and
neurexin adhesion, neuromedin, Nodal/TDGF1 receptor complexes, NPB/NPW,
NPFF/NPVF, natriuretic peptides, NPS, neuronal pentraxins, NPY, and NRG2/ErbB
branches.

## Disposition

- 21 `reviewed_relay_candidate`
- 4 `reviewed_function_only`
- 0 `reviewed_binding_only`
- 0 `reviewed_unresolved`
- 0 `no_evidence_boundary`
- 25 literal `terminal_TF=null`

The four function-only rows are NLGN2–NRXN1, NLGN3–NRXN1, NPTX1–NPTXR, and
NPTX2–NPTXR, where direct adhesion or neuronal-complex/function evidence is
present but a unique intracellular relay through the receptor label was not
resolved. All other rows have receptor-proximal pathway evidence, with
composite receptor stoichiometry and isoform limitations retained in the row
limitations.

## Evidence-layer handling

Binding/activation, receptor-proximal relay, and downstream pathway/function
were recorded as separate semicolon-delimited layers. Synaptic adhesion and
neuronal pentraxin organization were not promoted to a canonical kinase relay.
For Nodal, the ACVR1B/ACVR2A, ACVR1B/ACVR2B, and ACVR1B/ACVR2B/TDGF1 labels
retain the receptor-complex context; ACVR2A/B redundancy and species-specific
usage are documented rather than collapsed. For NRG2, ERBB3 is treated as the
ligand-binding partner and ERBB2 as the kinase-competent heterodimer partner,
not as an independently ligand-binding receptor.

## Search boundaries and limitations

Searches covered PubMed, PMC, publisher pages, and Reactome cross-checks for
exact ligand/receptor names and aliases (including GPR7/GPR8, FM-3/FM-4,
GPR147/GPR74, GC-A/GC-B, ALK4/ActRIIA/ActRIIB, and NARP/NPR). Negative or
unresolved cases were not filled by family analogy. The main remaining
uncertainties are isoform- and splice-dependent NLGN/NRXN binding, NMS versus
NMU-specific coupling, partial RF-amide receptor cross-reactivity, Nodal
receptor stoichiometry, NPTXR multicomponent synaptic-complex semantics, and
NRG2 isoform-specific ErbB dimer preference.

No Module 20A ledger, Module 21A ledger, frozen manifest, or SQL materialization
was modified.
