# Remaining CellChat evidence-search contract

Search each assigned CellChat ligand–receptor pair thoroughly. Expand official
and historical gene/protein aliases, mature or processed ligand forms,
receptor subunits/holoreceptors, co-receptors, heterodimers, species names,
full-text primary papers, structural studies, receptor reconstitution,
binding, activation, adhesion, and receptor-dependent function. Follow
citation trails from relevant primary papers and reviews.

PubMed and Europe PMC are required; CellChat, LIANA, GtoPdb, ConnectomeDB,
UniProt, Reactome, reviews, and structure databases are discovery leads.
Do not transfer family, expression, pathway, or database evidence to the exact
pair. Return exactly one TSV row per input to the matching `.report.tsv`:
`pair_key	pair_label_canonical	verdict	source_locators	species_support	support_kind	evidence_summary	limitations	search_notes`

Allowed verdicts: `promote_candidate`, `needs_manual_review`, `hold_low`,
`no_evidence`, `reject_pair`. Use promote_candidate only for exact submitted
pair primary evidence; no_evidence only after expanded searches; reject_pair
only for wrong/non-ligand-receptor relationships; hold_low for concrete but
unresolved evidence. Do not edit canonical ledgers.
