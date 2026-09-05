# Module 23B exhaustive-search handoff

This handoff is for a future search or evidence-expansion pass. The identity
and acquisition work already completed should be treated as a reusable input,
not repeated from scratch.

## Current identity baseline

The paper-level source of truth is:

`work/module_b_consolidation/module23b/module23_all_paper_extraction_inventory_2026-09-05.tsv`

It contains one row per normalized stable paper anchor and keeps PMID, PMCID,
and DOI identifiers separate unless an authoritative resolver has merged them.
Do not replace this with a title-only or filename-only deduplication list.

| Measure | Current value |
|---|---:|
| Module 23B evidence-register rows | 1,674 |
| Module 23B edge-register rows | 1,230 |
| Distinct stable anchors across 23A/23B | 1,511 |
| Anchors covering 23A and 23B | 1,432 |
| 23B-only anchors | 69 |
| 23B register rows without a stable anchor | 41 |
| Anchors with a local artifact | 1,500 |
| Anchors without a local artifact / identifier correction required | 11 |

Current paper-level status is 1,023 abstract/metadata artifacts, 477
full-text artifacts, and 11 identifier-correction cases. All 1,511 rows remain
`human_validation_status=required` and `promotion_status=not_promoted` in the
inventory. The inventory is identification/extraction staging, not proof of a
new canonical edge.

## Read these artifacts first

1. Inventory and summary:
   - `work/module_b_consolidation/module23b/module23_all_paper_extraction_inventory_2026-09-05.tsv`
   - `work/module_b_consolidation/module23b/module23_all_paper_extraction_inventory_2026-09-05.md`
2. Identifier exceptions:
   - `work/module_b_consolidation/module23b/module23_unresolved_doi_resolution_audit_2026-09-05.tsv`
3. Evidence grade/context pass:
   - `work/module_b_consolidation/module23b/module23b_evidence_grade_context_pass_2026-09-05.tsv`
   - `work/module_b_consolidation/module23b/module23b_evidence_grade_context_pass_2026-09-05.md`
4. Current evidence and edge registers:
   - `work/module_b_consolidation/module23b/module23b_evidence_register.tsv`
   - `work/module_b_consolidation/module23b/module23b_edge_register.tsv`
5. Existing paper-extraction batch:
   - `work/module_b_consolidation/module23b/module23b_paper_extraction_batch_2026-09-05.tsv`

The acquisition roots already present in the repository are:

- `data/raw/evidence/module23_pubmed_abstracts_20260905/`
- `data/raw/evidence/module23_pmc_fulltext_20260905/`
- `data/raw/evidence/module23_doi_metadata_20260905/`

Each root has an acquisition manifest where applicable. Preserve those
manifests and their retrieval failures; a failed request is part of the search
history, not evidence that the paper is absent.

## Non-duplicative exhaustive-search procedure

### 1. Establish identity before biological review

Load the inventory and make a lookup set keyed by the normalized pair
`(anchor_type, paper_anchor)`. For every search hit:

- If the normalized anchor is already present, attach the new result to the
  existing `paper_anchor`, `associated_evidence_ids`, and `associated_edge_ids`.
  Do not create a second paper record.
- If a PMID, PMCID, and DOI appear together, retain each identifier as its own
  anchor until an authoritative resolver confirms that they are the same
  publication.
- If a DOI resolves to a different title or PMID than the register’s
  co-identified records, record the discrepancy in the unresolved-DOI audit;
  do not merge it from a title resemblance or local filename.
- If no stable PMID, PMCID, or DOI is available, keep the result in a search
  queue with an explicit unresolved identity. Do not invent an identifier.

The 11 current correction cases are already listed in
`module23_unresolved_doi_resolution_audit_2026-09-05.tsv`; inspect those rows
before starting another DOI-resolution attempt.

### 2. Reuse artifacts before acquiring anything

For an existing anchor, check these inventory fields before requesting a new
source: `local_source_paths`, `selected_artifact_path`,
`source_artifact_status`, `artifact_resolution_method`,
`paper_extraction_status`, and `promotion_status`. A local artifact found by a
filename-token crosswalk is a candidate link, not content-level validation;
retain that distinction.

If acquisition is needed, use the existing scripts, which read the inventory
and preserve manifests:

```text
python3 scripts/acquire_module23_pubmed_abstracts.py
python3 scripts/acquire_module23_pmc_fulltext.py
python3 scripts/acquire_module23_doi_metadata.py
```

These routes are respectively NCBI PubMed XML, NCBI PMC BioC/XML fallback, and
Crossref Works API with an exact PubMed DOI-search fallback. Do not reacquire a
cached artifact merely to repeat identification. After adding or correcting
register anchors, rebuild the inventory with the existing extraction script and
the three acquisition roots as additional roots:

```text
python3 scripts/extract_module23_all_papers.py \
  --additional-root data/raw/evidence/module23_pubmed_abstracts_20260905 \
  --additional-root data/raw/evidence/module23_pmc_fulltext_20260905 \
  --additional-root data/raw/evidence/module23_doi_metadata_20260905
```

The extraction output is deterministic candidate text. It does not by itself
validate a claim or promote an edge.

### 3. Search only the unresolved or genuinely new space

Partition the next search into:

- existing anchors with no local artifact or only abstract/metadata support;
- the 41 23B register rows without a stable anchor;
- the 11 identifier-correction cases;
- new literature published after this inventory date or new query concepts
  not represented in the current registers.

For an existing paper, the deliverable is a new source artifact, exact source
locus, observation, or limitation attached to the existing IDs—not a new paper
identity. For a genuinely new publication, add the stable anchor only after the
identity check above, then record the associated 23B evidence/edge IDs and
source path in the next dated extraction batch.

### 4. Keep evidence grading separate from identity

Run the 23B pass after new evidence is attached:

```text
python3 scripts/run_module23b_evidence_pass.py
```

The pass preserves independent A–E/U and L0–L5 axes. Its L5 definition is
audit-only: explicit injury-model context plus an explicitly named SCI receiver
cell or lesion compartment. Do not convert a stronger paper identity into a
higher evidence grade without reviewing the paper’s observation, claim, locus,
assay, perturbation, species, and scope.

### 5. Preserve negative and failed-search history

Do not delete or overwrite a failed acquisition, unresolved DOI, boundary row,
or previous extraction batch. Add a dated follow-up artifact or update the
corresponding audit row with the new query/source and outcome. A future search
should be able to answer both “what was found?” and “what was already tried?”
from the repository alone.

## Stop conditions and handoff requirements

Before closing a future search round, report:

- the number of new stable anchors, existing anchors receiving new evidence,
  unresolved identities, and duplicate candidates rejected;
- the exact files/manifests added or updated and their checksums where the
  acquisition script provides them;
- the evidence IDs and edge IDs touched;
- which rows remain abstract-only, metadata-only, full-text-unvalidated,
  identifier-correction, boundary/E-grade, or U-grade;
- whether any edge was promoted. Promotion requires a separate explicit review;
  paper identification and candidate extraction do not authorize it.

This handoff intentionally points future work to the existing inventory rather
than copying 1,511 paper rows into another document. The TSV is the detailed
crosswalk; this file defines how to use it without repeating the completed
identity and acquisition work.
