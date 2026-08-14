# Module 21A broader-search batch 2

Date: 2026-08-14

## Approval-ready summary

This batch expands the bounded Module 21A search beyond the original nine priority families where a primary SCI paper supplied a clearly separated signaling or functional branch. It adds three main-register edges, two grouped evidence records, three perturbation records, three evidence-layer assignments, one new CSF1/CSF1R queue family, and two explicit unresolved cases. The prior checkpoint remains intact in commit `a07d22b`; this batch is a separate follow-on change.

### Additions

- `M21A-E111`: TNFR2-specific agonism to PI3K-gamma-linked neuronal protection after mouse contusive SCI, with rat primary-neuron culture evidence. This is receptor-proximal pathway evidence, not a direct TNFR2-PI3Kgamma binding claim. Source: [PMID 30941924](https://pubmed.ncbi.nlm.nih.gov/30941924/) and [PMCID PMC6630008](https://pmc.ncbi.nlm.nih.gov/articles/PMC6630008/).
- `M21A-E112`: lesion-border astrocyte CSF1 to microglial proliferation, wound closure, and motor recovery after focal mouse SCI. This is a functional pathway edge, not a direct CSF1-CSF1R interaction claim.
- `M21A-E113`: microglial IFN-beta to astrocyte IFNAR1-dependent survival, border formation, wound healing, and motor recovery after focal mouse SCI. This remains downstream functional evidence; JAK1/TYK2/STAT ordering is unresolved.

The CSF1/IFN-beta source paper is the primary 2026 focal-SCI study [PMCID PMC13366903](https://pmc.ncbi.nlm.nih.gov/articles/PMC13366903/), [PMID 42217185](https://pubmed.ncbi.nlm.nih.gov/42217185/), DOI `10.1016/j.celrep.2026.117418`.

### Promotions and boundaries

- Promoted: three candidates from `module21a_broader_search_register.tsv` to E111–E113.
- Routed outside 21A: LPS/TLR-associated PI3K/PKCdelta/ERK/NF-kappaB/CHL1 astrocyte signaling ([PMID 19672967](https://pubmed.ncbi.nlm.nih.gov/19672967/)) because it lacks an in-scope secreted ligand-receptor anchor; and astroglial NF-kappaB inhibition after contusive SCI because it is a downstream transcription-factor intervention without a defined ligand-receptor input.
- No Module 20A LR classification, ledger, or frozen manifest was modified.

## Search boundary

The broadened search used PubMed/PMC queries centered on `TNFR2 PI3Kgamma spinal cord injury`, `CSF1 IFN-beta astrocyte microglia spinal cord injury`, and `astrocyte PI3K PKCdelta ERK NF-kappaB spinal cord injury`. It also checked the existing Module 21A unresolved scopes for IFN-lambda, TNFR2 astrocyte branches, and CSF1R comparator evidence. Findings were retained only when the source supplied a primary perturbation, cell/model context, and a stable citation. Absence of a direct kinase or binding assay is recorded as an unresolved boundary rather than inferred.

## Current batch totals

- Main saturation registers: 105 edges, 48 grouped evidence records, 54 perturbation records.
- Separate Q001 seed packet: 8 edges, 4 evidence records, 3 perturbations.
- Combined packet: 113 unique edges, 52 evidence records, 57 perturbations.
- Evidence-layer register: 48 rows: 22 receptor-proximal relay and 26 downstream pathway/function.
- Unresolved register: 12 explicit cases.
- Queue: ten items, all `completed_bounded`; Q010 is the new bounded CSF1/CSF1R family.

## Limitations

The new CSF1 and IFN-beta findings are powerful SCI functional receiver-state evidence but do not justify direct molecular edges for CSF1-CSF1R or IFNAR-JAK/STAT without additional biochemical or phospho-perturbation studies. E111 supports PI3K-gamma pathway dependence in neurons, not astrocyte-specific TNFR2 signaling. These boundaries remain attached to the edge, evidence, layer, perturbation, and unresolved registers.
