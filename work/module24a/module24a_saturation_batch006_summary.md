# Module 24A saturation tranche 006

This reviewable tranche extends the comparator audit for three unresolved
candidate families without changing Module 20A LR classifications or deleting
any no-evidence boundary.

## Additions

- `M24A-E137` / `M24A-B006-EVID-001`: C5a/C5a-desArg binding to human
  C5L2/C5aR2 in receptor and primary-neutrophil comparator systems.
- `M24A-E138` / `M24A-B006-EVID-002`: C5L2/C5aR2-associated intracellular
  internalization, retention, and degradation of C5a/C5a-desArg.
- `M24A-E139` / `M24A-B006-EVID-003`: direct C3d-to-CR2/CD21 structural
  binding, kept distinct from intact C3 and other C3 cleavage products.
- `M24A-E140` / `M24A-B006-EVID-004`: factor Xa/PAR2 activation under
  tissue-factor/cofactor conditions, with comparator ERK and
  inflammatory/profibrotic outputs.

## Promotions and limits

- `M24A-Q0003` now records C5L2/C5aR2 comparator binding and clearance, but
  C5aR2/C5L2 SCI causality remains unresolved.
- `M24A-Q0004` now records factor Xa/PAR2 comparator activation, but the exact
  SCI activating protease remains unresolved.
- `M24A-Q0068` now records C3d/CR2 cleavage-fragment binding, while intact
  C3-to-CR2 activation and an endogenous SCI relay remain unresolved.
- Existing no-evidence records remain explicit; no comparator result was
  promoted to an SCI-specific edge or used to infer a new Module 20A LR pair.

## Validation disposition

- Four new edges and four new evidence records were added.
- The integrated registers now contain 140 edges, 189 evidence records, 31
  explicit no-evidence boundaries, 158 edge/evidence associations, and 189
  saturation-matrix rows.
- Direct binding/activation, receptor-proximal relay, and downstream/function
  layers remain separate.
- SQL staging assertions were updated to 140 edges and 189 evidence records;
  the corrected staging script was materialized successfully in the isolated
  PostgreSQL 16.14 database `mscitdb_module24a` on port `55432`.

## Search boundary

The tranche used stable PubMed/PMC records for C5L2/C5aR2 decoy-receptor
binding and clearance, CR2-C3d structural binding, and factor Xa/PAR2
cofactor-dependent activation. The evidence is comparator-only for 24A SCI
purposes; no direct SCI C5aR2, intact-C3/CR2, or factor-Xa/PAR2 causal record
was validated.
