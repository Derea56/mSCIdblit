# Module 22 Paper Extraction

Generated 2026-09-05 from explicit source locators in the four Module 22 source lanes below.

## Result

- Unique explicit identifiers: **15038** (11627 PMID, 1777 PMCID, 1634 DOI).
- Identifiers matched to an existing local title/metadata record: **854**.
- Identifiers whose associated Module 22 text mentions SCI/spinal cord/spinal injury: **9129**; this is a text-presence flag, not paper-level SCI validation.
- Non-paper or unresolved locator components retained separately: **12356**.

The main TSV is identifier-level. A paper with PMID, PMCID, and DOI can therefore occur as three identifiers until a validated cross-identifier mapping is available; this avoids falsely merging multiple papers cited in one source record.

## Source lanes

- `module22b_evidence_register`: 10780 source records
- `module22a_new_primary_extractions`: 49 source records
- `module22a_pending_candidate_dispositions`: 171 source records
- `module22a_22b_high_confidence_promotions`: 114 source records

## Non-paper locator classes

- `database_or_local_record`: 1431
- `paper_url_without_explicit_id`: 142
- `search_query`: 7391
- `unresolved_source_label`: 3392

## Files

- Identifier manifest: [`work/module22_paper_extraction/module22_paper_identifiers.tsv`](work/module22_paper_extraction/module22_paper_identifiers.tsv)
- Non-paper locator audit: [`work/module22_paper_extraction/module22_nonpaper_source_locators.tsv`](work/module22_paper_extraction/module22_nonpaper_source_locators.tsv)
- Reproducible extractor: [`scripts/extract_module22_papers.py`](../scripts/extract_module22_papers.py)

No titles, authors, years, or journal fields were invented. Blank metadata means that an exact local metadata match was unavailable to this extraction.
