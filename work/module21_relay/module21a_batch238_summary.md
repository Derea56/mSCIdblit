# Module 21A batch 238 review summary

Batch 238 reviews exactly the 25 supplied queued Module21A rows, in the
supplied order, for `M20A-LIANA-REMAINING-0562` through `-0586`.

## Disposition counts

| status | rows |
|---|---:|
| reviewed_relay_candidate | 1 |
| reviewed_function_only | 0 |
| reviewed_unresolved | 7 |
| reviewed_no_downstream_evidence | 0 |
| no_evidence_boundary | 17 |
| **total** | **25** |

Confidence counts: `low` 17, `medium` 7, `medium-high` 1, `high` 0.

## Evidence posture

The primary WNT-FZD receptor map reports WNT9A activity through FZD4 and
FZD10, and WNT9B activity through FZD4, FZD5, FZD8, and FZD10 (PMID:28733458;
PMCID:PMC5636703; DOI:10.1096/fj.201700144R). These component-level WNT-FZD
results were kept separate from LRP5/6 assignment.

The biochemical WNT9B study directly measured WNT9B binding to LRP6 and weak
binding to FZD8, but its purified ternary reconstitution was
FZD8-WNT3A-LRP6, not WNT9B-FZD8-LRP6 (PMID:20093360; PMCID:PMC2838336).
Accordingly, WNT9B-FZD10-LRP5/6 and the other partial WNT9A/B composite rows
remain unresolved rather than being promoted by family or generic
beta-catenin evidence.

The strongest exact-composite result is WNT9A-FZD9/Fzd9b-LRP6. Primary
zebrafish and human studies show FZD9/Fzd9b-dependent WNT9A canonical
signaling, direct LRP6 requirement, EGFR-dependent FZD9b phosphorylation and
endocytosis, and hematopoietic stem/progenitor-cell function
(PMCID:PMC6559346; DOI:10.1038/s41556-019-0330-5; PMCID:PMC11103623). The
LRP5-specific row remains unresolved because the later loss-of-function test
used LRP5/6 double knockout and did not isolate LRP5.

The mouse nephron-progenitor study supports WNT9B-FZD5 and WNT9B-LRP6 in
related component assays, including TOPFlash and LRP6 knockdown, but it does
not provide a matched purified WNT9B-FZD5-LRP6 ternary assay; this evidence was
not transferred to the queued FZD10 or FZD1/FZD2 composites
(PMCID:PMC6461349; DOI:10.1371/journal.pone.0215139).

All unresolved and no-evidence rows explicitly state that no exact
pair-specific downstream endpoint or terminal TF was established. No
standalone `reviewed_no_downstream_evidence` row was used because the partial
rows either had component reporter/function evidence or were classified as
no-evidence boundaries. `terminal_TF` is the literal `null` in all 25 rows.

## Validation

- TSV has the exact 13-column schema and 25 data rows.
- IDs and pairs match the supplied 25-row order exactly.
- All 25 rows have 13 populated fields; no tabs occur inside fields and no
  extra columns are present.
- Status vocabulary is limited to `reviewed_relay_candidate`,
  `reviewed_unresolved`, and `no_evidence_boundary` in this batch.
- Confidence vocabulary is limited to `low`, `medium`, and `medium-high`.
- All 25 `terminal_TF` values are literal `null`.
- Frozen manifest SHA-256 matches
  `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.
- Only `work/module21_relay/module21a_batch238_review.tsv` and this summary
  were written; shared registers, Module20A files, the manifest, SQL, and
  unrelated existing files were not modified.
