# Module 21A batch 102 review summary

## Scope and exact queue validation

- Reviewed the explicit review-ID range `M20A-EXT-0958` through `M20A-EXT-0983` from `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`.
- The explicit range contains 26 IDs. The user-described filtered ordinal span is 25 rows, so the explicit IDs were followed and the ordinal discrepancy is recorded here.
- Output: `module21a_batch102_review.tsv`, one row per exact review ID with the requested 13-column schema.
- Shared Module 21A registers, Module 20A LR ledgers, frozen manifest, and integration outputs were not modified.

## Disposition

| Status | Count | Main findings |
|---|---:|---|
| `reviewed_relay_candidate` | 6 | BMP6–ACVR2A/BMPR1A receptor-dependence; BMP7–ACVR2A/BMPR1A receptor-use; BMP7–ENG accessory-complex relay; BMP8A–ACVR2A/BMPR1A canonical relay; BMP8A–TGFBR1 and BMP8A–TGFBR2 SMAD2/3 receptor-complex branch. |
| `reviewed_binding_only` | 3 | BMP7–ACVR2A/BMPR1B component binding without an isolated submitted-complex relay; BSG–SLC16A1/MCT1 and BSG–SLC16A7/MCT2 direct transporter-chaperone complexes. |
| `reviewed_function_only` | 0 | No exact pair had function-only evidence that could be separated from an identified receptor-complex or direct binding record. |
| `reviewed_unresolved` | 17 | All BMP5 exact complexes; BMP6 subtype boundaries and BMP6–AMHR2; BMP7–ActR2, ACVR1B, ACVR2B combinations, and PTPRK; BMP8A ACVR2B/BMPR1A/BMPR1B and ACVR2A/BMPR1B; BPI–SLAMF9. |

## Evidence decisions

- **BMP5:** Primary BMP5 stimulation in rat chondrocytes demonstrates phospho-SMAD1/5/8 and weak p38 activation, but no receptor-specific perturbation or exact ACVR2A/BMPR1A/BMPR1B complex was recovered. Those four rows remain unresolved rather than inheriting BMP6/7 receptor usage.
- **BMP6:** In primary human hMSCs, RNAi and osteoblastic differentiation assays support BMP6 dependence on ACVR2A and BMPR1A at receptor-utilization level. BMPR1B and ACVR2B were low/not significant in the matched model, so only ACVR2A/BMPR1A was promoted and the other exact combinations remain unresolved. The record does not assert a purified ternary complex.
- **BMP7:** ACVR2A/BMPR1A was retained as a receptor-use relay with context limitations. ACVR2A/BMPR1B was retained as binding-only because component binding and a BMPR1B-containing chemotropic model do not isolate the submitted binary complex. ACVR2B combinations were not promoted because the primary chemotaxis work identified ActRIIA and BMPRII rather than ActRIIB. ENG was retained as an accessory co-receptor association with BMP7-SMAD1/5 modulation; ENG is not treated as an autonomous kinase receptor. ACVR1B and PTPRK remained unresolved.
- **BMP8A:** The primary spermatogonial study directly supports ALK3/BMPR1A with ACVR2A for SMAD1/5/8 and ALK5/TGFBR1 with ACVR2A, ACVR2B, or TGFBR2 for SMAD2/3. Therefore, BMP8A–ACVR2A/BMPR1A, BMP8A–TGFBR1, and BMP8A–TGFBR2 were promoted. Evidence was not transferred to BMPR1B or to the ACVR2B/BMPR1A/BMPR1B combinations.
- **BPI/SLAMF9:** BPI innate immune activity through LPS/TLR4 and SLAMF9 macrophage modulation were kept as separate branches. No exact BPI–SLAMF9 binding or receptor-proximal relay was located; SLAMF9 also lacks a canonical intracellular signaling motif in the reviewed primary literature.
- **BSG transporters:** BSG/CD147–SLC16A1/MCT1 and BSG/CD147–SLC16A7/MCT2 are direct ancillary transporter complexes supported by co-localization/co-immunoprecipitation and complex-stability evidence. They are recorded as binding-only transporter-chaperone edges, not ligand-activated receptor relays; no terminal TFs were assigned.

## Search boundaries and unresolved cases

- Exact searches covered PubMed, PMC, publisher pages, and pathway/context records for every submitted pair and receptor subtype.
- Family-level receptor tables, CellChat/LIANA predictions, co-expression, and generic BMP5/6/7/8A pathway annotations were not used to promote an exact ternary complex without pair-specific primary evidence.
- BMP8A SMAD2/3 is recorded as a receptor-complex branch, not as a terminal TF assignment. SMAD1/5/8 and SMAD2/3 are pathway nodes in this batch; no direct TF occupancy or ligand-to-terminal-TF endpoint was demonstrated.
- The BPI–SLAMF9 search was bounded by the absence of a published SLAMF9 ligand assignment and by separate BPI/TLR4 and SLAMF9 macrophage studies. The BSG transporter records were bounded to the demonstrated cell contexts and were not generalized to all tissues.

## Integrity checks

- 26 rows; all 13 columns populated.
- Review IDs unique.
- Exact explicit queue IDs match: PASS.
- Status counts: 6 relay, 3 binding-only, 0 function-only, 17 unresolved.
- No shared registers, Module20A LR ledgers, frozen manifest, or integration outputs changed.
