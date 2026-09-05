# Module 22 Paper Extraction

Generated 2026-09-05 from explicit paper locators in the Module 22 source lanes below, including all discovered numbered audit batches.

## Result

- Unique explicit identifiers: **15909** (12114 PMID, 1974 PMCID, 1821 DOI).
- Identifiers matched to an existing local title/metadata record: **862**.
- Identifiers whose associated Module 22 text mentions SCI/spinal cord/spinal injury: **12982**; this is a text-presence flag, not paper-level SCI validation.
- Non-paper or unresolved locator components retained separately: **28766**.
- Module 22A handoff coverage: **5906** handoffs inspected; 5875 had evidence references, covering 5836 unique detail packets; missing detail IDs: 0.

The main TSV is identifier-level. A paper with PMID, PMCID, and DOI can therefore occur as three identifiers until a validated cross-identifier mapping is available; this avoids falsely merging multiple papers cited in one source record.

## Source lanes

- `module22b_evidence_register`: 10780 source records
- `module22a_new_primary_extractions`: 49 source records
- `module22a_pending_candidate_dispositions`: 171 source records
- `module22a_22b_high_confidence_promotions`: 114 source records
- `module22a_handoff_source_evidence`: 5836 source records
- `module22b_low_confidence_upgrade_batch001`: 13 source records
- `module22b_low_confidence_upgrade_batch002`: 1 source records
- `module22b_low_confidence_upgrade_batch003`: 6 source records
- `module22b_low_confidence_upgrade_batch004`: 2 source records
- `module22b_low_confidence_upgrade_batch005`: 1 source records
- `module22b_low_confidence_upgrade_batch006`: 1 source records
- `module22b_low_confidence_upgrade_batch007`: 2 source records
- `module22b_low_confidence_upgrade_batch008`: 1 source records
- `module22b_low_confidence_upgrade_batch009`: 1 source records
- `module22b_low_confidence_upgrade_batch010`: 1 source records
- `module22b_low_confidence_upgrade_batch011`: 1 source records
- `module22b_low_confidence_upgrade_batch012`: 3 source records
- `module22b_low_confidence_upgrade_batch013`: 2 source records
- `module22b_low_confidence_upgrade_batch014`: 7 source records
- `module22b_low_confidence_upgrade_batch015`: 8 source records
- `module22b_low_confidence_upgrade_batch016`: 8 source records
- `module22b_low_confidence_upgrade_batch017`: 5 source records
- `module22b_low_confidence_upgrade_batch018`: 4 source records
- `module22b_low_confidence_upgrade_batch019`: 8 source records
- `module22b_low_confidence_upgrade_batch020`: 6 source records
- `module22b_low_confidence_upgrade_batch021`: 5 source records
- `module22b_general_tf_regulon_promotion_batch001`: 37 source records
- `module22b_signed_public_tf_promotion_batch002`: 3589 source records
- `module22b_target_register_repair_batch004`: 5 source records
- `module22b_trrust_signed_promotion_batch003`: 552 source records
- `module22b_individual_hold_search_log`: 5090 source records

## Non-paper locator classes

- `database_or_local_record`: 2178
- `missing_locator`: 9
- `paper_url_without_explicit_id`: 289
- `search_query`: 12568
- `unresolved_source_label`: 13722

## Files

- Identifier manifest: [`work/module22_paper_extraction/module22_paper_identifiers.tsv`](work/module22_paper_extraction/module22_paper_identifiers.tsv)
- Non-paper locator audit: [`work/module22_paper_extraction/module22_nonpaper_source_locators.tsv`](work/module22_paper_extraction/module22_nonpaper_source_locators.tsv)
- Reproducible extractor: [`scripts/extract_module22_papers.py`](../scripts/extract_module22_papers.py)

No titles, authors, years, or journal fields were invented. Blank metadata means that an exact local metadata match was unavailable to this extraction.
