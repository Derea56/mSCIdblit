# CellChat non-LR audit contract

Independently audit every submitted CellChat-full pair. Determine whether the
relationship is truly invalid ligand-receptor notation, or whether it is a
valid ligand-receptor edge obscured by processed ligand biology, receptor
complexes, adhesion/co-receptor notation, isoforms, or a database naming issue.
Search PubMed, Europe PMC, and authoritative receptor/complex resources; open
the source rather than relying on snippets. Search canonical names, aliases,
processed forms, receptor chains, complexes, binding, activation, adhesion,
and receptor-dependent function.

Return exactly one row per input in identical order with header:
`review_id	pair_key	pair_label_canonical	final_class	source_locators	species_support	support_kind	evidence_summary	limitations	review_notes`

Allowed `final_class` values: `retain_non_ligand_receptor`, `restore_low`,
`restore_medium`, `retain_manual`. Use `restore_low` only when the exact
relationship is a real but contextual/complex-limited LR edge. Use
`restore_medium` only for direct, exact-pair primary evidence. Use
`retain_manual` when the relationship may be valid but the exact entity or
complex remains unresolved. Every restoration must include stable PMID,
PMCID, DOI, or authoritative URL locators and explain the exact evidence.
Do not edit canonical ledgers.
