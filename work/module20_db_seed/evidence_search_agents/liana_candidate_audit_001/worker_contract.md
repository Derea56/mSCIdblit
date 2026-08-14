# Remaining LIANA candidate citation-audit contract

Audit every proposed candidate by opening the cited primary paper(s) or exact
source. Confirm that the submitted ligand and receptor pair—not merely a
family, pathway, subunit, processed fragment, or related receptor—is actually
tested. Confirm assay type, species, receptor complex/chain notation, and
whether the result is direct binding, adhesion, receptor activation, or
receptor-dependent function.

Return exactly one row per input to the matching `.report.tsv` with header:
`pair_key	pair_label_canonical	final_verdict	source_locators	species_support	support_kind	evidence_summary	limitations	audit_notes`

Allowed final verdicts: `approve_candidate`, `retain_low`, `no_evidence`,
`reject_pair`, `needs_manual_review`. Approve only exact-pair primary evidence
with a usable citation. Retain low for real but contextual or unresolved
evidence. Use no_evidence when the cited source does not support the pair. Use
reject_pair only when the submitted relationship is wrong or not ligand–receptor.
Do not edit canonical ledgers.
