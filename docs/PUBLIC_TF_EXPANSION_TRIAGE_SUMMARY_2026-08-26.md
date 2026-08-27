# Public TF expansion first-pass triage summary

**Date:** 2026-08-26  
**Status:** staging only; no canonical TF, Module 22B, or evidence-promotion writes

## Scope

This review covers the 2,051 normalized TF keys absent from the current TF
sets in every species scope. The underlying ledger is
[`tf_expansion_triage.tsv`](</Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/tf_expansion_triage.tsv>), with structural checks in
[`triage_validation.json`](</Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/triage_validation.json>).

This is an evidence-topology triage, not a final biological classification.
In particular, `promote_identity_staging` means that two identity catalogs
agree; it does not mean that the candidate is a canonical sequence-specific
TF or that any Module 22B edge has been promoted.

## First-pass disposition

| Triage bucket | Count | Share | Interpretation | Next route |
|---|---:|---:|---|---|
| Promote identity staging | 869 | 42.4% | Lambert and AnimalTFDB3 identity agreement; pair evidence still unverified | Role audit, then exact pair review |
| Manual identity review | 684 | 33.3% | One catalog/profile lane and no exact pair evidence in this expansion | Verify identity and biological role |
| Prioritize target evidence search | 478 | 23.3% | TFLink target-membership lead; the retained GMT is not pair-level evidence | Acquire detailed TFLink/GTRD records and review exact edges |
| Unresolved identifier | 16 | 0.8% | OmniPath/DoRothEA protein accession without a stable gene-symbol identity | Map accession before biological review |
| Profile-only | 4 | 0.2% | JASPAR profile without target-level evidence | Retain as binding-profile provenance only |
| **Total** | **2,051** | **100%** |  |  |

Thus, 1,182 candidates (57.6%) were not automatically promoted. Of those,
478 (40.4%) have a concrete TFLink target-search lead, 684 (57.9%) need
identity/role review, and 20 (1.7%) are not currently reviewable as ordinary
gene-symbol candidates.

## Provenance structure

The major source combinations are:

| Source combination | Count | Main interpretation |
|---|---:|---|
| AnimalTFDB3 only | 601 | Broad catalog identity; no pair evidence in this expansion |
| TFLink only | 416 | Aggregated target lead; exact assay and PMID still required |
| AnimalTFDB3 + Lambert | 351 | Identity agreement, but still identity-only |
| AnimalTFDB3 + Lambert + TFLink | 204 | Identity agreement plus target-search lead |
| AnimalTFDB3 + JASPAR + Lambert + TFLink | 172 | Identity/profile agreement plus target-search lead |
| AnimalTFDB3 + JASPAR + Lambert | 142 | Identity/profile agreement without target-search lead |
| Lambert only | 65 | Expert-catalog identity requiring role and pair review |
| AnimalTFDB3 + TFLink | 34 | One catalog plus target-search lead |
| Lambert + TFLink | 23 | One catalog plus target-search lead |
| OmniPath/DoRothEA only | 16 | Protein-accession mapping required |

The source versions, raw record keys, and source-specific identity records are
preserved in the parent expansion artifacts; the cross-species collapse is an
inventory operation only.

## Chromatin/nuclear role signal

The TFLink target-lead queue contains many names that should be treated as
possible chromatin regulators, transcriptional cofactors, or nuclear machinery
rather than assumed to be canonical sequence-specific TFs. Examples include
BRD4, KDM1A, KDM2B, KMT2B, RAD21, SMC1A, SMC3, NIPBL, CHD2, MED12, RCOR1,
SSRP1, TET1, and YAP1. These are manual role-review flags, not final
exclusions. They are visible in the local queue, for example in the
[BRD4 record](</Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/tf_expansion_triage.tsv:747>),
[RAD21 record](</Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/tf_expansion_triage.tsv:1036>),
and [TET1 record](</Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/tf_expansion_triage.tsv:1132>).

A conservative manual screen identified at least 24 obvious
chromatin/nuclear-regulator signals, including BRD4, CHD2, HDAC6, KDM1A,
RAD21, SMC1A, SMCHD1, TET1, TET2, TET3, ADNP, BAZ2A, CENPA, and MBD4. This
is a lower-bound review flag, not a complete biological count: the imported
catalog snapshots do not preserve the domain, family, and confidence fields
needed to classify all 2,051 candidates automatically. No likely biological
artifact has been confirmed yet; the current artifact-risk signals are
transcript-like symbols, predicted mouse symbols, and unmapped protein
accessions.

The existing TET2 row demonstrates the boundary clearly: it has independent
AnimalTFDB3/Lambert identity support plus TFLink membership, so it is in
identity staging, but the correct biological category is a noncanonical
chromatin regulator rather than a strict sequence-specific TF. Its local row
is [here](</Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/tf_expansion_triage.tsv:1460>).

The current snapshots do not contain enough functional annotation to assign a
defensible chromatin/nuclear count for all candidates. That classification
requires a second pass against richer source metadata and authoritative
protein/gene annotations. It should be recorded separately from evidence
readiness so that a noncanonical regulator is not mistaken for either a false
entry or a promoted canonical TF.

All 2,051 rows currently have zero `unique_reference_pmids` in this triage
ledger. There are 854 TFLink target-membership leads in total: 478 are in the
dedicated target-search bucket and 376 are attached to identity-staged rows.
This is why the TFLink signal is useful for prioritization but cannot yet be
counted as verified pair-level evidence.

## Review lanes

1. **TFLink/GTRD leads — 478 keys.** Obtain the detailed interaction export,
   retain TF, target, assay, source database, PMID, species, and experiment
   fields, then review exact TF-target pairs. GMT membership alone remains a
   search lead.
2. **Single-catalog identity — 684 keys.** First resolve transcript-like and
   predicted mouse identifiers, then review the remaining candidates against
   richer catalog fields, domain annotations, and literature.
3. **Identity-staged candidates — 869 keys.** Perform the biological role
   audit before any Module 22B promotion. Split canonical TFs from
   chromatin regulators, cofactors, nuclear scaffolds, and other noncanonical
   regulators.
4. **Blocked identifiers/profiles — 20 keys.** Map protein accessions and
   retain JASPAR-only rows as profile provenance; neither group is deleted.

The recommended role vocabulary for the next pass is:

`canonical_sequence_specific_tf`, `noncanonical_chromatin_regulator`,
`transcriptional_cofactor`, `chromatin_remodeler_or_epigenetic_enzyme`,
`nuclear_signaling_or_scaffold`, `target_or_interaction_only`,
`unresolved_identifier`, and `likely_artifact`.

Each role should have an independent `module22b_eligibility` field. This keeps
strong chromatin evidence useful without allowing ChIP occupancy or broad
database labeling to silently promote a protein into the strict TF set.

## Noncanonical regulator staging overlay

A conservative exact-symbol/family screen has now placed **195 candidates** in
a separate noncanonical-regulator staging queue. This is a parallel overlay:
the candidates remain in their original triage bucket, and their source
provenance is not collapsed or deleted.

| Staged role signal | Rows |
|---|---:|
| Chromatin modifier or reader | 72 |
| Chromatin modifier/reader plus chromatin architecture | 4 |
| Chromatin modifier/reader plus transcriptional modifier/elongation factor | 3 |
| Chromatin remodeler or architecture | 38 |
| Transcriptional coregulator or complex | 56 |
| Transcriptional coregulator plus transcriptional modifier/elongation factor | 2 |
| Transcriptional modifier or elongation factor | 20 |

The queue includes TET2, TET1, TET3, BRD/CBX-family readers, KDM/KMT/SET-family
modifiers, cohesin/SMC/STAG/NIPBL architecture proteins, SWI/SNF/CHD/INO80
components, Polycomb components, Integrator/NELF/Mediator/elongation proteins,
and corepressors such as RCOR, BCOR, CTBP2, and TLE5. The role labels are
screening labels for later evidence review, not confirmed functional
annotations.

The staged rows are in
[`noncanonical_regulator_staging.tsv`](</Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/noncanonical_regulator_staging.tsv>),
with counts and validation metadata in
[`noncanonical_regulator_staging_summary.json`](</Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/noncanonical_regulator_staging_summary.json>).
All 195 rows remain `not_strict_tf_pending_role_and_pair_review`; no Module
22B evidence or canonical TF role was created. The initial 2,051-row triage
therefore has 1,856 candidates not yet placed in this noncanonical overlay.

## Full role sorting

The full inventory is now sorted into mutually exclusive primary role-review
categories in
[`public_tf_role_triage.tsv`](</Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/public_tf_role_triage.tsv>),
with the machine-readable counts in
[`public_tf_role_triage_summary.json`](</Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/public_tf_role_triage_summary.json>).

| Primary role-review category | Rows | Interpretation |
|---|---:|---|
| Catalog-concordant TF candidate | 818 | Identity catalogs agree; exact TF role and pair evidence remain pending |
| Noncanonical transcriptional regulator | 195 | Chromatin/co-regulator/elongation candidates held outside strict TF identity |
| Regulon lead, role unclassified | 233 | TFLink target lead requiring role and exact-edge review |
| Identity review, unclassified | 678 | Single-source or otherwise unresolved identity/role cases |
| RNA-binding/post-transcriptional | 26 | RNA processing or RNA-guided regulation; not automatically chromatin TFs |
| Signaling/metabolic/membrane/cell-cycle | 29 | Receptor, enzyme, transporter, kinase, or cell-cycle role signals |
| DNA repair/genome maintenance | 18 | Repair, replication, recombination, or chromosome-maintenance proteins |
| Nuclear structure/transport | 7 | Lamina, pore, or genome-organization candidates |
| Nuclear machinery/structural, not regulatory | 8 | Centromere, telomere, or nuclear-processing proteins without locus-directed evidence |
| Dual-role TF/chromatin candidate | 14 | Retain as TF candidates while flagging chromatin-coregulator functions |
| Provisional nuclear regulator | 3 | Nuclear transcriptional effects, but weaker chromatin classification |
| Alias/ingestion-artifact review | 2 | Placeholder or alias resolution required |
| Unresolved identifier | 16 | Protein accession mapping required |
| Binding profile only | 4 | Motif/profile support without pair evidence |

This sorting is a routing layer, not a confidence claim. It keeps, for example,
RNA-guided silencing, DNA repair, and membrane-receptor biology from being
mistaken for canonical TF activity, while preserving the original database
provenance for later evidence review.

## Candidate regulon attribution

The sorted candidates now have a separate candidate-regulon handoff. The
[`public_tf_candidate_regulon_index.tsv`](</Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/public_tf_candidate_regulon_index.tsv>)
contains one row for each of the 2,051 candidates. **854 candidate keys** have
an imported database-attributed regulon set, **1,181** have no regulon set in
the currently imported sources, and **16** remain blocked on identifier
mapping.

The corresponding
[`public_tf_candidate_regulon_attribution.tsv`](</Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/public_tf_candidate_regulon_attribution.tsv>)
contains 991 source-set records: 714 human TFLink sets and 277 mouse TFLink
sets, reporting 3,442,771 source-reported target memberships in aggregate.
That aggregate is not deduplicated and is not evidence of activation. Each
record retains its TFLink source record ID, raw snapshot path, SHA-256 record
hash, and target count so the underlying set can be reviewed later.

For every candidate-regulon row, target-cell presence, upstream relay status,
and downstream activation are explicitly `not_assessed`. TFLink does not
provide target-level assay, PMID, or effect-direction fields in this snapshot,
so its sets remain candidate attribution and all rows remain export-excluded.
Canonical TF candidates route to the Module 22B evidence queue; chromatin and
cofactor candidates route to a separate regulatory-machinery program queue.
The machine-readable summary is
[`public_tf_candidate_regulon_summary.json`](</Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/public_tf_candidate_regulon_summary.json>).

## Evidence collection batch 001

All 25 TFLink source sets in batch 001 have now been bounded-reviewed as 100
exact regulator-target search pairs. The review register is in
[`public_tf_evidence_review_batch001_pairs.tsv`](</Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_001/public_tf_evidence_review_batch001_pairs.tsv>).
One pair, ZNF580-to-ABCA1, has partial functional support in human THP-1
oxLDL foam cells, but lacks direct binding and independent corroboration and
therefore remains staging-only. The other 99 had no defensible exact
regulator-target-species result in this pass. All 100 remain non-exportable
database-attributed search leads; target-cell presence, downstream activation,
and upstream relay are not promoted.

General regulator-level literature was found for 24 of the 25 reviewed
regulators
and is intentionally separated in
[`public_tf_evidence_review_batch001_regulator_register.tsv`](</Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_001/public_tf_evidence_review_batch001_regulator_register.tsv>).
Those records support regulator identity or regulatory capacity in the cited
models, but do not support the queued target pairs or a Module 22B promotion.
The partial ZNF580-to-ABCA1 functional observation is recorded as a separate
downstream-expression evidence row, not as a direct TF-binding claim.
Near matches are recorded as exclusions so evidence cannot silently migrate
between regulators or targets. The batch summary reports zero exportable
pair rows and zero canonical writes.

## Evidence collection batches 002-016

Batches 002 through 006 extend the same provenance-preserving, staging-only
review to another 500 exact regulator-target-species pairs. Each batch keeps
the source registry, source record ID, raw symbol, species, graph-module
mapping, search URL, cited evidence, and disposition together in its own
register.

Batch 002 found no exact supported pair; one PATZ1-to-ADAM17 co-expression
near-match was excluded. Batch 003 found no exact supported pair; one
ZNF750-to-ADAM10 contextual co-mention was excluded. Batch 004 found no exact
supported pair; one TGIF2-to-ABCA1 hit was correctly rejected as TGIF1
paralog evidence. These three batches together retain 300 non-exportable
search leads and regulator-level records separately.

Batch 005 reviewed 100 pairs and found no functional promotion-ready edge.
Five exact GTRD-derived occupancy leads were retained as binding-only holds
(four ZSCAN4 targets and ZNF768-to-APOE); none establish perturbation,
direction, target-cell presence, or SCI activation.

Batch 006 reviewed 100 pairs and found no functional promotion-ready edge.
Forty-eight exact GTRD-derived occupancy leads were retained as binding-only
holds, while 52 pairs remained bounded-search negatives. Regulator-level
evidence for Hoxc12, Grhl3, FOXN3, ZNF84, ZNF318, HAND1, ZBTB18, ZFP91, FEV,
and others is recorded separately and was not transferred to unrelated
queued edges.

Batch 007 reviewed 100 pairs and found no functional promotion-ready edge.
Seventy-one exact binding/association leads were retained as non-promotable
holds, while 29 pairs remained bounded-search negatives. Regulator-level
evidence for ZNF2, ZNF146, ZNF7, ZNF282, ZBTB12, ZNF22, FEV, and others is
recorded separately and was not transferred to unrelated queued edges.

Batch 008 reviewed 100 pairs and found no functional promotion-ready edge.
Ninety-five exact GTRD-derived occupancy leads were retained as non-promotable
holds, while five pairs remained bounded-search negatives. Regulator-level
evidence for ZNF490, ZNF512, ZNF10, ZNF257, ZNF579, RFX6, BARHL1, and others
is recorded separately and was not transferred to unrelated queued edges.

Batch 009 reviewed 100 pairs and identified one exact promotion candidate:
mouse Ovol2-to-Cdh2, supported by Ovol2 ChIP-seq/ChIP validation plus Cdh2
change after Ovol2 deletion and DNA-binding-dependent rescue. Because those
experiments are in mouse mammary models rather than the SCI target cell, the
edge remains staging-only pending target-cell context. Ninety-four additional
exact GTRD-derived occupancy leads were retained as non-promotable holds; three
exact pairs were bounded negatives, one was a readthrough near-match, and the
ZNF507-to-IGF2R perturbation signal remained non-promotable because directness
was unresolved. No canonical or Module 22B write was made.

Batch 010 reviewed 100 pairs and identified one additional exact promotion
candidate: mouse Msgn1-to-Dll3, supported by upstream binding, loss/gain
perturbation, and reporter transactivation. Because those experiments are in
presomitic mesoderm rather than the SCI target cell, the edge remains
staging-only pending target-cell context. The other 99 pairs remain
database/binding leads without matched target-level functional validation.
No canonical or Module 22B write was made.

Batch 011 reviewed 100 pairs and found no additional promotion candidate.
Eighty-seven exact GTRD/MSigDB promoter-occupancy leads and 13 TFLink-only
database leads were retained separately; all lacked matched target-level
functional validation in this bounded pass. No canonical or Module 22B write
was made.

Batch 012 reviewed 96 exact pairs across 25 additional source sets and found
no promotion candidate. Sixty-eight pairs were retained as species-matched
GTRD/MSigDB occupancy leads and 21 as database-membership-only leads. Five
near matches were kept separate: two ZFP90-derived FIK/FOXP3/KAP1 complex
relationships for IFNG and IL2, one mouse Hoxa13-to-Aldh1a2 relationship for
the human pair, and two regulator-swapped ZNF510 relationships. Two pairs
were bounded-search negatives. None establishes SCI target-cell presence,
downstream activation, or an upstream relay, and no canonical or Module 22B
write was made.

Batch 013 reviewed 87 exact pairs across 25 further source sets and found no
promotion candidate. Fifty-six pairs were retained as occupancy/binding leads
and 26 as database-membership-only leads. Three near matches were kept
separate, including SP6 versus KLF14 evidence and a cross-species HOXB9-NCAM1
reporter; two pairs remained bounded-search negatives. No target-cell presence,
downstream activation, or upstream relay was established, and no canonical or
Module 22B write was made.

Batch 014 reviewed 81 exact pairs across 25 further source sets. It identified
one exact staging promotion candidate, human BHLHA15/MIST1-to-RAB26, supported
by target-site ChIP, induction/loss expression changes, and a RAB26-dependent
secretory-granule phenotype. Because the evidence is from secretory-cell
models rather than the SCI target cell, it remains non-exportable. Four
ZNF513 rows have direct promoter-binding-only evidence; 50 additional rows are
occupancy/binding leads, 22 are database-only leads, and four partial/near
matches remain explicitly separated. No canonical or Module 22B write was
made.

Batch 015 reviewed 38 exact pairs across 25 further source-set ranks. It
identified one exact TF staging candidate, mouse NOBOX-to-Pou5f1, supported by
promoter binding, reporter activation, ChIP, and loss-of-function expression
evidence. It also retained two exact ZNF385A/Hzf RNA 3-prime-UTR regulator
relationships as noncanonical post-transcriptional candidates, not promoter-TF
edges. ESX1-to-KRAS and HOXD10-to-HOXD9 were kept as limited fragment/reporter
cases, while human NKX2-8-to-AKIP1 evidence was not transferred to the mouse
row. No canonical or Module 22B write was made.

Batch 016 reviewed 100 exact pairs across 25 further source-set ranks and found
no direct TF promotion candidate. Eight ZNF711/PRDM12 rows were retained as
aggregate promoter-occupancy leads, not target-specific causal evidence. BRD4
had three indirect target-expression associations (mouse A2m, mouse Abca1, and
human Abca1), KDM1A had two indirect pathway/signature associations (mouse
Abca1 and Ackr3), and one KDM2B-to-ACKR2 row had processed chromatin-occupancy
evidence. The remaining chromatin readers, writers, cohesin components, DNA
repair factors, and transcriptional machinery were retained in the separate
noncanonical regulator category. All 100 rows remain non-exportable; no
canonical or Module 22B write was made.

Batch 017 reviewed 100 exact pairs across 25 noncanonical source-set ranks and
found no strict TF promotion candidate. Two exact module-relevant relationships
were retained in the separate chromatin/coregulator category: mouse KMT2D-to-
Abca1, where LXR/ASC-2/MLL4 chromatin assays supported Abca1 activation, and
mouse GPS2-to-Abca1, where promoter/enhancer co-occupancy with NF-kB p65 and
macrophage loss-of-function supported reduced Abca1 and cholesterol efflux.
Neither is a sequence-specific TF edge, and both remain pending SCI target-cell
context. TET2-to-Abca1 was explicitly tested in a mouse perturbation study but
was non-supportive. The remaining 97 rows were bounded database, chromatin,
cofactor, or network leads; all 100 remain non-exportable and no canonical or
Module 22B write was made.

Batch 018 reviewed 100 exact pairs across 25 additional noncanonical source-set
ranks and found no strict TF promotion candidate. The bounded searches retained
limited evidence separately: a human STAG2-to-ABCA1 chromatin edge for the
queued mouse row, an ambiguous mouse KDM6A lipid-expression panel, contextual
mouse YAP1/ABCA1 complex evidence where direct promoter support belonged to
KLF11, reverse-direction ACKR3/YAP1 and ACVR1/YAP1 associations, and network or
chromatin-resource leads involving SAP130, BRD9, and H2AZ1. These were not
transferred to exact causal TF edges. All 100 rows remain non-exportable and no
canonical or Module 22B write was made.

Batch 019 reviewed 100 exact pairs across 25 additional noncanonical source-set
ranks and found no strict TF promotion candidate. One exact human
TBL1XR1/TBLR1-to-ABCA1 relationship was staged as noncanonical coregulator
evidence because promoter ChIP and siRNA reduced LXR-induced ABCA1 in HepG2
cells. A human PRMT1-to-ABCA1 result was retained only as a nonspecific type-I
PRMT-inhibitor association because PRMT1-specific causality and direct locus
binding were not established. The remaining rows were database, chromatin,
resource, or transcriptional-machinery leads. All 100 remain non-exportable
and no canonical or Module 22B write was made.

Batch 020 reviewed 100 exact pairs across 25 additional noncanonical source-set
ranks and found no strict TF promotion candidate. One exact human STAG2-to-ABCA1
relationship was staged as a provisional noncanonical cohesin/chromatin-
architecture candidate because STAG2 promoter occupancy and knockout-associated
ABCA1 loss/acetylation change were reported in an AACR abstract and same-study
preprint. The evidence lacks independent corroboration and SCI target-cell
validation. Two mouse SETDB1 rows remain binding-profile-only, and NCAPD3-to-
Ackr3 plus two mouse CDK9 rows remain contextual or indirect near-matches. The
remaining rows are bounded database, chromatin, cofactor, or transcriptional-
machinery leads. All 100 remain non-exportable and no canonical or Module 22B
write was made.

Batch 021 reviewed 100 exact pairs across 25 additional noncanonical source-set
ranks and found no strict TF promotion candidate. One exact human YAP1/YAP-TAZ-
to-ACTR2 coactivator relationship was staged as a noncanonical candidate because
enhancer ChIP-qPCR, depletion, and active-YAP rescue supported ACTR2 regulation;
YAP and TAZ were not fully separated. YAP1-to-ACKR2 was retained as expression-
only evidence. KDM3A-to-ABCA1, CDK7-to-Abca1, HDAC6-to-ADAM10, and SIRT6-to-
Adam12 were retained as indirect, complex-level, profile, or cross-species
near-matches. The remaining rows are bounded database, chromatin, cofactor, or
transcriptional-machinery leads. All 100 remain non-exportable and no canonical
or Module 22B write was made.

Batch 022 reviewed 100 exact pairs across 25 additional noncanonical source-set
ranks and found no strict TF or exact noncanonical functional promotion
candidate. The limited findings were retained separately: UBN1 profile-only,
KAT8 genetic co-occurrence, KDM5C perturbation-only, KDM4A cross-species,
SIRT6 profile-only, USP16/CHD2 profile or interaction-only, and no qualifying
exact target edge for the remaining rows. All 100 remain non-exportable and no
canonical or Module 22B write was made.

Batch 023 reviewed 100 exact pairs across 25 additional noncanonical source-set
ranks and staged two exact noncanonical chromatin-regulator candidates: human
NSD2-to-ADAM9, supported by ADAM9 promoter ChIP-qPCR, NSD2 perturbation, and
independent direction corroboration; and mouse ASH2L-to-Adam17, supported by
promoter-associated H3K4me3 and Ash2l loss-of-function evidence. Neither is a
strict TF or validated in the SCI target-cell context. Mouse TET3-to-Agrn was
retained as locus-level epigenetic evidence without direct occupancy. ADNP,
ZNF592, DIDO1, and RCOR1 profile leads, plus KANSL3 contextual evidence, were
not promoted. All 100 remain non-exportable and no canonical or Module 22B write
was made.

Batch 024 reviewed 100 exact pairs across 25 additional noncanonical source-set
ranks and found no strict TF or exact noncanonical functional promotion
candidate. AUTS2-to-CCND1 and TET1-to-IL5 were retained as expression-only
associations; AFF4-to-CDH1 and SETD7-to-CCND1 as species/complex near-matches;
CHAF1B-to-ETV5 as reverse-direction evidence; and the remaining profile,
chromatin, cofactor, and machinery findings as non-causal leads. All 100 remain
non-exportable and no canonical or Module 22B write was made.

Batch 025 reviewed 95 exact pairs across 25 additional noncanonical source-set
ranks. Two exact noncanonical candidates were staged: human CARM1-to-GREB1,
where ERalpha-bound regulatory-region occupancy and CARM1 loss reduced
estrogen-induced GREB1; and mouse Tle5/Grg5-to-Ihh, where Grg5 loss reduced
Ihh and downstream Hedgehog signaling but direct Ihh occupancy was not shown.
Neither is a strict sequence-specific TF edge or validated in the SCI target-cell
context. Exact PRMT5-to-EPHA2 protein-stability regulation was routed to a
separate receptor/protein-regulation category, not treated as transcriptional
evidence. The remaining rows were profile-only, complex/locus-level,
expression-only, direct-binding-only, reverse-direction, or bounded negative
leads. All 95 remain non-exportable and no canonical or Module 22B write was
made.

At the Batch 025 checkpoint, the consolidated registers and reports were in the
`evidence_batches/batch_002` through `evidence_batches/batch_025` directories.
Across those twenty-five batches, 2,397 exact provenance-aware pairs had been
reviewed. Eight exact noncanonical or strict TF candidates remained in staging:
mouse Ovol2-to-Cdh2, mouse Msgn1-to-Dll3, human BHLHA15/MIST1-to-RAB26, mouse
NOBOX-to-Pou5f1, human NSD2-to-ADAM9, mouse ASH2L-to-Adam17, human
CARM1-to-GREB1, and mouse Tle5/Grg5-to-Ihh. None had been materialized because
SCI target-cell context was still unestablished. No canonical or Module 22B
write had been performed. Binding-only leads remained valuable follow-up
candidates for SCI-cell occupancy or perturbation data, but were not functional
signaling evidence by themselves.

Batch 026 reviewed 93 exact pairs across 25 additional noncanonical source-set
ranks. Two exact noncanonical chromatin-regulator candidates were staged:
human WIZ-to-CWH43 and human WIZ-to-DIP2C, both supported by WIZ occupancy and
siRNA-associated target-expression changes in U2OS cells. They are not strict
sequence-specific TF edges and lack SCI target-cell validation. Exact
IVNS1ABP-to-ACTR2 protein-complex evidence was routed to the separate
protein-regulation category; CUL4A-to-ACVR1 was retained only as a complex-level
near-match. The remaining rows were profile-only, unsupported, or other bounded
near-matches. All 93 remain non-exportable and no canonical or Module 22B write
was made.

The consolidated registers and reports now extend through
`evidence_batches/batch_026`. Across all twenty-six batches, 2,490 exact
provenance-aware pairs have been reviewed. Ten exact noncanonical or strict TF
candidates remain in staging: mouse Ovol2-to-Cdh2, mouse Msgn1-to-Dll3, human
BHLHA15/MIST1-to-RAB26, mouse NOBOX-to-Pou5f1, human NSD2-to-ADAM9, mouse
ASH2L-to-Adam17, human CARM1-to-GREB1, mouse Tle5/Grg5-to-Ihh, human
WIZ-to-CWH43, and human WIZ-to-DIP2C. None has been materialized because SCI
target-cell context is still unestablished. No canonical or Module 22B write
has been performed. Binding-only leads remain valuable follow-up candidates for
SCI-cell occupancy or perturbation data, but are not functional signaling
evidence by themselves.

Batch 027 reviewed 100 exact pairs across 25 additional source-set ranks. One
exact noncanonical RNA-regulator candidate was staged: human METTL3-to-ADAM10,
where ADAM10 m6A, transcript stability, mRNA/protein abundance, and downstream
phenotypes changed with METTL3 perturbation and ADAM10 rescue. Exact human
AMH-to-ACVR1 ligand/receptor signaling was routed to the ligand/receptor
category rather than treated as transcriptional evidence. HMGB1-to-ACVR1,
INSR-to-ADAM17, and Tbxt-to-Adam17 were retained as receptor-response,
reverse-direction, or paralog near-matches. The remaining rows were profile-only
or bounded unsupported leads. All 100 remain non-exportable and no canonical or
Module 22B write was made.

The consolidated registers and reports now extend through
`evidence_batches/batch_027`. Across all twenty-seven batches, 2,590 exact
provenance-aware pairs have been reviewed. Eleven exact noncanonical or strict
TF candidates remain in staging, adding human METTL3-to-ADAM10 to the ten
previous candidates. None has been materialized because SCI target-cell context
is still unestablished. No canonical or Module 22B write has been performed.

Batch 028 reviewed 100 exact pairs across 25 additional source-set ranks and
found no new promotion candidate. SUMO1, ZMYND8, MYH11, and SIGMAR1 rows with
apparent support were resolved as cross-species, other-regulator, fusion, or
pharmacologic near-matches; TEX10, MSL1, SUPT16H, PRKDC, ZC3H11A, and OGT
profile rows remain binding leads only. All 100 remain non-exportable and no
canonical or Module 22B write was made.

The consolidated registers and reports now extend through
`evidence_batches/batch_028`. Across all twenty-eight batches, 2,690 exact
provenance-aware pairs have been reviewed. The same eleven exact noncanonical
or strict TF candidates remain in staging; no new candidate was added in Batch
028, and none has been materialized because SCI target-cell context is still
unestablished.

Batch 029 reviewed 100 exact pairs across 25 additional source-set ranks. One
exact ligand/RNA-regulatory candidate was staged: mouse Ccl5-to-Agrp, where
CCL5/CCR5 signaling changed hypothalamic Agrp mRNA in knockout, ex vivo, and
primary-neuron/ligand-antagonist assays. This is routed to ligand/receptor and
downstream RNA evidence, not canonical TF evidence. Exact mouse GSK3B-to-Ccnd1
protein phosphorylation/stability regulation was also retained separately; it
does not establish Ccnd1 transcription. MSL2, NUCKS1, WRNIP1, GREB1, SUMO1, and
ZC3H11A profile rows remain profile-only. HBZ/HBAZ identity and viral-HBZ
near-matches, ZSCAN5DP family evidence, DDX21/FXR1 perturbation-only signals,
and other protein-complex or reverse-direction results were explicitly kept
separate. All 100 rows remain non-exportable and no canonical or Module 22B
write was made.

The consolidated registers and reports now extend through
`evidence_batches/batch_029`. Across all twenty-nine batches, 2,790 exact
provenance-aware pairs have been reviewed. Twelve exact noncanonical or strict
TF/functional candidates are now in staging: the prior eleven plus the
ligand/RNA-regulatory Ccl5-to-Agrp relationship. None has been materialized
because SCI target-cell context is still unestablished.

Batch 030 reviewed the literal 100-pair queue across 25 additional source-set
ranks. One exact noncanonical ligand/protease-to-RNA relay was staged:
human F10/factor-Xa-to-CCN1, where PAR1 blockade prevented factor-Xa-induced
CCN1/CYR61 expression in HeLa cells. This is routed to ligand/protease
signaling and downstream RNA evidence, not Module 22B. Exact human
DYRK1A-to-CCND1 phosphorylation/stability regulation was routed to the
kinase/protein category; SUPT16H-to-CCND1 was retained only as a partial
protein readout. F10-to-CDH2 (engineered substrate), F10-to-COL3A1
(cross-species indirect RNA), DYRK1A-to-COL1A1 (cross-species indirect RNA),
ADA2-to-ANXA2 (expression association), and HSD17B8 rows (annotation-review
hold) remain explicitly nonpromotable. All literal queue provenance was
preserved; alternate reconstructed regulator names from a lane-integrity check
were not ingested. All 100 rows remain non-exportable and no canonical or
Module 22B write was made.

The consolidated registers and reports now extend through
`evidence_batches/batch_030`. Across all thirty batches, 2,890 exact
provenance-aware pairs have been reviewed. Thirteen exact noncanonical or
strict TF/functional candidates are now in staging, including the
F10-to-CCN1 ligand/RNA relay. None has been materialized because SCI
target-cell context is still unestablished.

Batch 031 reviewed the literal 100-pair queue across 25 additional source-set
ranks. Ten exact memberships remained profile-only on documented MSigDB/GTRD
promoter-profile pages: ZNF830-to-JAG1, METTL14-to-JUND, SRPK1-to-COL6A3,
FZD6 and LAMP1, UBE2I-to-BDNF, COL6A1, PLXDC1 and VIM,
TERT-to-PLXDC1, and SYNCRIP-to-ANXA2. (UBE2I-to-VIM,
IGF1R-to-IGF1R and TERT-to-RELB were routed to stronger target-specific
findings below.)
These are reproducible regulon leads only: the profile source does not establish
occupancy in an SCI target cell, effect direction, or perturbation, so none was
promoted. Seven exact noncanonical functional candidates were staged:
METTL14-to-FGFR4 (m6A/RNA stability), SRPK1-to-IGF1R (indirect kinase/protein
response), UBE2I-to-VIM (protein/PTM phenotype), IGF1R-to-APOB (kinase-dependent
lipid transport), IGF1R-to-IGF1R (nuclear receptor autoregulation), mouse
Nfam1-to-Il2 (ITAM/NFAT cytokine relay), and TERT-to-RELB (limited RNA
perturbation). METTL14-to-HMGB1 was retained as a cross-species/partial
RNA-inflammatory near-match; TERT-to-ANG and TERT-to-JUND were retained as
reverse-direction near-matches. Four ZA rows remain identity-review holds because
the raw symbol could not be mapped confidently to an approved human gene. All
100 rows remain non-exportable and no canonical or Module 22B write was made.

The consolidated registers and reports now extend through
`evidence_batches/batch_031`. Across all thirty-one batches, 2,990 exact
provenance-aware pairs have been reviewed. Twenty exact noncanonical or strict
TF/functional candidates are now in staging, including the seven Batch 031
findings above; no strict sequence-specific TF promotion was added.

## Validation and data-safety result

The triage manifest reports 2,051 input keys, 2,051 output rows, zero duplicate
keys, zero missing source registries, zero missing source versions, and zero
unexpected module-evidence promotions. No canonical data, source records, or
provenance rows were modified by this summary pass.
