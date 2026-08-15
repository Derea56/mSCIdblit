# Module 21A batch 076 review summary

## Scope

- Exact filtered priority-8 queue ordinals reviewed: 1201–1225.
- Exact review IDs: `M20A-CELLCHAT-REMAINING-1330` through `...-1357`, with the filtered-slice gap at `...-1356` documented: it is not present in this 25-row ordinal slice.
- Queue source: `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`.
- Review output: `module21a_batch076_review.tsv`.
- No shared Module 21A registers, Module 20A ledgers, frozen manifest, or integration outputs were modified.

## Disposition

- 25/25 exact rows written and validated.
- 12 `reviewed_relay_candidate`:
  - KLK14–F2R and KLK14–F2RL1: direct proteolytic PAR activation/proximal calcium evidence.
  - KLK4–F2R and KLK4–F2RL1: direct PAR calcium-signaling evidence.
  - KLK5–F2RL1: direct PAR2 activation evidence.
  - KLK6–F2R and KLK6–F2RL1: receptor-dependent ERK/calcium evidence in neuronal and glial models.
  - LAMA2–ADGRG6: laminin-211/Laminin-alpha2 binding and context-dependent GPR126 cAMP relay.
  - LCK–CD8: intracellular CD8-coreceptor/LCK association in the TCR-proximal relay.
  - LGALS9–BCR/CD45/CD22: glycan-organized receptor-complex association with proximal inhibitory signaling.
  - LGALS9–CD44: direct lectin/receptor association with LCK-linked T-cell activation context.
  - LGALS9–IGHM: direct Gal9–IgM-BCR binding with BCR-complex organization and proximal inhibition.
- 4 `reviewed_binding_only`:
  - JAM2–JAM3 and JAM3–JAM3: heterophilic/homophilic adhesion, kept separate from intracellular relay.
  - L1CAM–L1CAM: homophilic adhesion and neurite-outgrowth context, without a direct relay assignment.
  - LAIR1–LILRB4A: very weak purified-protein interaction, retained at low confidence and not promoted to a physiological relay.
- 1 `reviewed_function_only`:
  - KLK8–F2R: PAR1-antagonist-sensitive colorectal cancer function; no direct KLK8 cleavage/binding assay was promoted.
- 8 `reviewed_unresolved`:
  - ITGAV_ITGB5–ADGRB1, JAM2–F11R, JAM2–JAM2, JAM3–F11R, JAM3–ITGAM_ITGB2L, KLK1–F2R, KLK7–F2RL1, and LAIR1–PIRA2.

## Accuracy boundaries

- JAM adhesion evidence was kept in the binding layer; canonical JAM3–alphaMbeta2 evidence was not transferred to the noncanonical `ITGB2L` receptor complex.
- KLK7–PAR2 was not promoted: the direct skin-KLK assay reported no KLK7 PAR2 signaling, and later combination experiments do not isolate a mature KLK7→PAR2 edge.
- KLK14–PAR1 includes positive activation in receptor-expressing cells but is explicitly limited by context-dependent PAR1 disarming/processing reports.
- The LAMA2 row refers to the alpha2 chain within laminin-211 and preserves the static-versus-mechanical GPR126 signaling limitation.
- LCK–CD8 is recorded as an intracellular kinase–coreceptor association, not as an extracellular ligand–receptor interaction.
- Galectin-9 rows distinguish direct lectin binding, receptor-complex organization, and downstream BCR/T-cell outputs; no direct Gal9→TF edge was inferred.
- No terminal TF assignments were made in this batch.

## Search boundary

The review used exact-pair searches and expanded-family/comparator audits across PubMed, PMC, publisher pages, and stable source URLs. Primary evidence included JAM-B/JAM-C adhesion (`PMID:16093349`, `PMID:16118203`), KLK–PAR signaling (`PMID:16800746`, `PMID:17625593`, `PMID:21907696`, `DOI:10.1074/jbc.M709493200`, `PMID:23647384`), L1 homophilic binding (`PMID:2627381`), LAIR1/LILRB4 weak binding (`PMID:19283782`), laminin-211/GPR126 (`PMID:25695270`, `PMCID:PMC4335265`), CD8–LCK (`PMID:8814252`, `PMCID:PMC4248239`), and Gal9 BCR/CD44 studies (`PMID:30120235`, `PMID:30120234`, `PMID:34411088`).

All 25 rows have complete 13-column records, unique review IDs, stable citations or bounded stable search URLs, explicit evidence layers, limitations, and `terminal_TF=none`.
