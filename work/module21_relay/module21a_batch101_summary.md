# Module 21A batch 101 review summary

## Scope and exact queue validation

- Reviewed the exact filtered priority-8 queue ordinal rows 1826–1850 from `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`.
- The slice contains 25 rows with intentional review-ID gaps: `M20A-EXT-0929`–`M20A-EXT-0935`, `M20A-EXT-0938`–`M20A-EXT-0942`, `M20A-EXT-0945`–`M20A-EXT-0957`.
- Output: `module21a_batch101_review.tsv` with one row per exact review ID, 13 columns, unique IDs, complete evidence fields, and exact queue-ID matching.
- Shared Module 21A registers, Module 20A LR ledgers, frozen manifest, and integration outputs were not modified.

## Disposition

| Status | Count | Main findings |
|---|---:|---|
| `reviewed_relay_candidate` | 6 | BMP10–ENG; BMP2–ACVR2A/BMPR1A; BMP2–ACVR2B/BMPR1A; BMP2–ENG; BMP4–ACVR2A/BMPR1A; BMP4–RGMB/DRAGON. |
| `reviewed_binding_only` | 1 | BMP4–GREM2 direct antagonist/sequestration binding without receptor activation. |
| `reviewed_function_only` | 0 | No exact pair had function-only evidence that met the promotion threshold. |
| `reviewed_unresolved` | 18 | BMP10–FFAR2/GPR152; BMP15 exact subtype boundaries; BMP2 ACVR2A/B–BMPR1B and SMO; BMP3 exact receptor boundaries; BMP4 ACVR2A/B–BMPR1B, ACVR2B/BMPR1A/B, CFC1, and LRP6. |

## Evidence decisions

- **BMP10–ENG:** direct ENG association and endothelial co-receptor activity were retained, but ENG is recorded as an accessory component rather than an independent kinase receptor. The type-II receptor is not forced to a single universal composition. Primary support includes soluble ENG binding to BMP10/BMP9 and ALK1-dependent endothelial signaling (PMCID:PMC3191044; DOI:10.1182/blood-2006-07-034124).
- **BMP15:** the strongest exact primary receptor study identified preferential BMPR1B and BMPR2 binding with SMAD1/5/8 output in human granulosa models (PMID:22294741). ACVR2A, the unspecified ActR2 node, BMPR1A, and TGFBR1 were not promoted. GDF9:BMP15 heterodimer signaling through an ALK4/5/7 context was not transferred to the BMP15 homodimer rows (PMCID:PMC3581982).
- **BMP2:** ACVR2A–BMPR1A and ACVR2B–BMPR1A were retained as receptor-complex relays with SMAD1/5/8 evidence. ACVR2A/B–BMPR1B combinations were kept unresolved because the reviewed primary records did not isolate those exact ternary compositions. BMP2–ENG was retained as an ENG-associated ALK3/ALK6 complex, not autonomous ENG receptor activation (DOI:10.1074/jbc.274.2.584; PMID:22535663).
- **BMP3:** the primary colorectal study supports an ACVR2B/ActRIIB-dependent SMAD2 and TAK1/JNK branch and reports no BMPR2 association in that model (PMCID:PMC6819484; DOI:10.1186/s13046-019-1435-1). That evidence was not transferred to ACVR2A, BMPR1A, BMPR1B, or BMPR2 exact rows.
- **BMP4:** ACVR2A–BMPR1A was cautiously retained as a receptor-complex relay based on primary receptor-usage/SMAD evidence (PMID:18436533). GREM2 was retained at the direct binding/antagonism layer because it binds and inhibits BMP4 without being a signaling receptor (PMCID:PMC8626944; PMCID:PMC4123739). RGMB/DRAGON was promoted as a co-receptor relay because it directly binds BMP4 and enhances BMP signaling (DOI:10.1074/jbc.M410034200; PMCID:PMC1351303).

## Search boundaries and unresolved cases

- Exact searches covered PubMed, PMC, publisher full text, and stable source records for each submitted BMP/receptor combination.
- Canonical BMP2/BMP4 receptor-family annotations, shared SMAD1/5/8 outputs, co-expression, and pathway-database edges were not used to promote exact ACVR2A/B–BMPR1B combinations without pair-specific primary evidence.
- BMP10–FFAR2/GPR152, BMP2–SMO, BMP4–CFC1/LRP6, and the BMP15 subtype rows remained no-evidence or subtype-boundary cases. FFAR2 and SMO ligand pharmacology, CFC1 Nodal co-receptor biology, LRP6 Wnt co-receptor biology, and BMP-family paralog evidence were kept separate.
- No terminal TF was assigned. SMAD1/5/8 and SMAD2/3 are recorded as receptor-proximal pathway branches; no direct TF occupancy or exact ligand-to-TF endpoint was demonstrated in this batch.

## Integrity checks

- 25 rows; all 13 columns populated.
- Review IDs unique.
- Exact filtered queue IDs match: PASS.
- Status counts: 6 relay, 1 binding-only, 0 function-only, 18 unresolved.
- No shared registers, Module 20A LR ledgers, frozen manifest, or integration outputs changed.
