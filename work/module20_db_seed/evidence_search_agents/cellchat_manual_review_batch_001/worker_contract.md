# CellChat manual/uncertain re-review contract

Re-review every submitted pair from scratch, prioritizing exact primary
literature and authoritative receptor-complex sources. Search canonical names,
aliases, processed ligand forms, receptor chains/complexes, and species. Open
the cited sources rather than relying on search-result snippets. Distinguish
direct binding, receptor activation, adhesion, receptor-dependent function,
family/pathway evidence, expression-only evidence, and wrong-pair notation.

Return exactly one row per input in identical order with this header:
`review_id	pair_key	pair_label_canonical	final_class	source_locators	species_support	support_kind	evidence_summary	limitations	review_notes`

Allowed `final_class` values: `promote_medium`, `promote_low`, `retain_manual`,
`no_evidence`, `non_ligand_receptor`. Use `promote_medium` only for direct,
replicated, exact-pair evidence sufficient to move beyond low evidence. Use
`promote_low` for a real but contextual or species/complex-limited pair. Use
`no_evidence` only when the expanded review finds no qualifying support. Use
`non_ligand_receptor` only for a wrong relationship or invalid LR notation.
Every promotion must include stable PMID, PMCID, DOI, or authoritative URL
locators and state the exact assay or functional result. Do not edit canonical
ledgers.
