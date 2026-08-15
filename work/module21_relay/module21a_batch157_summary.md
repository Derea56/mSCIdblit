# Module 21A batch 157 review summary

Batch 157 reviewed exactly the 25 supplied queue rows corresponding to filtered queue ordinals 3376–3400. The review is recorded in `work/module21_relay/module21a_batch157_review.tsv` using the existing raw 13-column Module 21A batch schema.

## Validation summary

- Rows written: **25/25**
- Unique review IDs: **25/25**
- Unique canonical pair labels: **25/25**
- TSV columns: **13/13**, in the requested order
- Evidence fields: **13/13 populated in every row**
- Invented or out-of-scope rows: **none**
- Terminal TF assignments: **none**; no terminal TF was directly supported for these bounded records
- Module 20A files, shared registers, frozen manifests, and integration outputs: **not modified**
- Commit: **not created**

## Disposition counts

| Status | Count |
|---|---:|
| reviewed_relay_candidate | 6 |
| reviewed_binding_only | 6 |
| reviewed_function_only | 2 |
| reviewed_unresolved | 11 |

| Evidence layer | Count |
|---|---:|
| ligand_receptor_binding_or_activation | 23 |
| receptor_proximal_relay | 6 |
| downstream_pathway_function | 8 |

Layer counts are row-level presence counts; multi-layer rows are counted once in each applicable layer. Binding/activation, receptor-proximal relay, and downstream function were kept distinct in the TSV. Downstream pathway or adhesion phenotypes were not used to infer direct molecular interaction.

## Main evidence retained

- **Saa2–Cd36 and Saa2–Scarb1:** SAA-family/A-SAA primary studies support CD36 or SR-BI/SCARB1 binding and receptor-dependent inflammatory, uptake, or lipid-handling outputs. Exact purified murine Saa2 attribution remains limited by preparation, isoform, lipidation, and species context (PMID 20075072; PMID 20304957; DOI 10.1074/jbc.M411555200; PMID 17034364).
- **Scgb3a2–Marco:** primary expression-cloning and lung studies support SCGB3A2–MARCO binding, while also showing a distinct SCGB3A2 receptor-like activity in fetal lung. This evidence was not transferred to the queued SCGB3A1–MARCO row (PMID 12847263; PMID 18535256).
- **Sdc2–Ptprj:** SDC2 ectodomain/core-protein binding to CD148/PTPRJ and associated phosphatase, PI3K/Src, beta1-integrin and adhesion outputs support a bounded relay candidate, without assigning a terminal TF or SCI-specific weight (PMID 21813734; PMID 33784491).
- **Selectin ligand rows:** primary work supports glycoform-dependent E-selectin binding and leukocyte function for CD44/HCELL and GLG1/ESL-1. PSGL-1-to-Mac-1/beta2-integrin effects were retained as downstream functional coupling only; no direct Selplg–Itgam or Selplg–Itgb2 binding was inferred (PMID 11402070; PMID 17442598; PMID 9099943; PMID 15187162; PMID 1709677).
- **Sema3B complexes:** Sema3B–NRP1 binding was retained as binding-only evidence, whereas the NRP2/PLXNA1 neural-development branch was retained as a relay candidate. Plexin-A2/A3/A4 assignments were not expanded from expression, family, Sema3A, or pathway similarity (PMID 10725340; PMID 20159958; PMID 26680304).

## Explicit unresolved boundaries

No qualifying exact-pair evidence was located for Saa2–Fpr1, Saa2–Grm7, Saa2–Mtnr1a, Scel–Eng, Scgb1a1–Lmbr1l, Scgb1a1–Lrp2, Scgb3a1–Marco, Scgb3a1–Notch3, Sele–Ceacam2, Selplg–Esam, or Sema3b–NRP2_PLXNA2. Sele–Ceacam1 and the three NRP1–Plexin-A2/A3/A4 rows retain only bounded subunit-level or comparator evidence, not exact complex-level relay assignments. The review records these limitations explicitly and does not promote any of them to a direct interaction or terminal-TF claim.
