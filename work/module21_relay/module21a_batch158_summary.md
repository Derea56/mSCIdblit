# Module 21A Batch 158 review summary

Batch 158 reviewed exactly the 25 supplied filtered-queue rows at ordinals 3401–3425. The raw output is `module21a_batch158_review.tsv` and uses the exact 13-column schema:

`review_id`, `pair`, `status`, `stable_citations`, `species`, `cell_type_model`, `assay_or_perturbation`, `relation_type`, `evidence_layer`, `pathway_branch`, `confidence`, `limitations`, `terminal_TF`.

## Validation

- 25/25 exact supplied review IDs written.
- 25/25 exact supplied pair labels preserved.
- 25 unique review IDs and 25 unique pair labels.
- 13 fields present on every data row; every row has populated limitations and explicit `null` terminal TF.
- No Module 20A file, shared Module 21A register, Module 22A handoff, or integration output was modified.
- No commit was created.

## Disposition

| Status | Rows |
|---|---:|
| `reviewed_relay_candidate` | 2 |
| `reviewed_function_only` | 2 |
| `reviewed_binding_only` | 2 |
| `reviewed_unresolved` | 19 |
| **Total** | **25** |

The two relay candidates are Sema3C–NRP2/PLXNA1 and the composite Sema3C–NRP1/NRP2/PLXND1 receptor-complex context. The composite row is deliberately low confidence because primary studies support NRP1/PLXND1 and NRP2/PLXND1 in different contexts, not one isolated complex containing both neuropilins. Sema3C–NRP2/PLXNA1 is supported in lymphatic endothelial cells, but PLXND1 is also required in that model and the exact stoichiometry is unresolved (PMID:25808871; PMID:18625214; PMID:34270956).

The single function-only row is Sema3C–NRP1/PLXNA2. Mouse submandibular-gland experiments showed NRP1-dependent Sema3A/Sema3C morphogenesis sensitive to Plexin-A2 or Plexin-D1 reduction, but the study did not isolate a direct Sema3C–NRP1–Plexin-A2 binding event (PMID:17626059). This is recorded as downstream pathway/function evidence, not direct interaction.

The binding-only rows are Sema3E–NRP1 and Sema3F–NRP1. Older primary SemE pharmacology reported NRP1 binding, while later primary work established Plexin-D1 as the canonical direct Sema3E receptor and showed NRP1/VEGFR2 modulation in some contexts (PMID:10196546; PMID:15914725; PMID:26037503). Sema3E–NRP2 is retained as function-only because the classic study reports NRP2-dependent responsiveness without a clean NRP2-only binding assay. Sema3F–NRP1 is supported by soluble NRP-domain competition/sequestration assays, but the strongest functional branch is Sema3F–NRP2 with Plexin-A1/A3 (PMID:23145112; PMID:18660502; PMID:20010807; PMID:15721238). No terminal TF was assigned.

## Unresolved and no-evidence boundaries

The 19 unresolved rows were not promoted from receptor-family or pathway similarity:

- **Sema3B:** NRP2/PLXNA3 and NRP2/PLXNA4 remain unresolved. Primary commissural-axon studies support NRP2/PLXNA1 for Sema3B; Plexin-A3/A4 results from other semaphorin branches were not transferred (PMID:20159958; PMID:26680304).
- **Sema3C:** NRP1/PLXNA1, NRP1/PLXNA3, NRP1/PLXNA4, NRP2/PLXNA2, NRP2/PLXNA3, and NRP2/PLXNA4 remain unresolved. Primary evidence separates NRP1/PLXND1 from NRP2/PLXNA1 rather than supporting the queued substitutions (PMID:18625214; PMID:25808871).
- **Sema3D:** all eight queued NRP1/2–PLXNA1/2/3/4 rows remain unresolved. Primary studies support Sema3D binding to NRP1 and PLXND1, NRP1-dependent endothelial responses, or an NRP2/PLXND1 functional context; they do not establish the submitted Plexin-A complexes (PMID:26243191; PMCID:PMC4811025; PMID:24825896; PMID:37219490).
- **Sema3F:** NRP2/PLXNA4 remains unresolved. Primary studies support NRP2/PLXNA1 or NRP2/PLXNA3, not the submitted Plexin-A4 pair (PMID:18660502; PMID:20010807; PMID:15721238).
- **Sema3G:** Fcgr3 and Gp6 remain unresolved/no-evidence. Primary studies identify NRP2-containing Plexin-D1 or Plexin-A1 complexes, and a separate newer study reports NRP1 activity in tumor immunity; none supports Fcgr3 or GP6 as a Sema3G receptor (PMID:16098142; PMID:27880905; PMID:36720439).

Across the batch, expression, co-occurrence, knockdown of a related receptor, generic semaphorin-family membership, downstream cytoskeletal/vascular phenotype, and pathway diagrams were not treated as proof of direct ligand–receptor binding. Binding/activation, receptor-proximal relay, and downstream pathway/function remain separate in the TSV. Processing, species, cell-type, receptor-complex, and assay-context limitations are recorded per row.
