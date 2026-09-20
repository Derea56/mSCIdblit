# Public ligand--receptor evidence-review contract

Review one packet at a time. First decide whether the public row is already
represented by the matched mSCIdblit graph edge under an alias, processed form,
species-specific form, receptor complex, or reverse orientation. If it is not
represented, open the cited primary paper or perform a documented discovery
search.

Return one disposition per candidate unit. Allowed dispositions are:

- `already_present_exact_or_alias`
- `new_primary_supported_edge_candidate`
- `hold_contextual_or_complex_boundary`
- `reject_precursor_or_non_edge_form`
- `no_primary_evidence_found`
- `needs_manual_adjudication`

Record exact source locators, species, assay or functional readout, and a short
evidence note. Do not promote graph edges in the packet. Do not assign route
confidence; mSCS evaluates plausibility after evidence is curated.
