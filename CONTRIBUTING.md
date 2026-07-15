# Scientific Curation Protocol

This repository treats literature curation as scientific work. Preserve the distinction between extracted evidence, author interpretation, and project-level synthesis.

## Curation Order

1. Verify access to full text, figures, legends, methods, and results.
2. Register the paper.
3. Extract research questions.
4. Extract experimental paradigms.
5. Extract experiments as atomic comparisons.
6. Extract observations as immutable empirical findings.
7. Extract author claims.
8. Link claims to observations with `EvidenceLink`.
9. Run validation queries.
10. Only after corpus completion, begin consensus synthesis.

## Evidence Rules

- Do not infer values that are not stated or measured in the source.
- Preserve literal source text when a value is normalized.
- Record figure, panel, table, section, page, or quote provenance whenever available.
- If an observation is wrong, add a corrected observation. Do not update or delete the original.
- If a claim has no supporting observation, leave it unlinked and add a `CuratorNote`.

## Controlled Vocabulary Requests

Use a curator note with `note_type = 'vocabulary_request'` when a term does not fit existing vocabulary.

Include:

- proposed canonical term
- source phrase
- table where it belongs
- reason existing terms do not fit

## Consensus Boundary

Corpus-building modules should not create `Consensus` or `Hypothesis` records unless the module explicitly enters a synthesis phase. Module 1A remains extraction-only until its completion checklist is satisfied.
