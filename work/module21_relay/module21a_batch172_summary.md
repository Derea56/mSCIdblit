# Module 21A batch 172 review summary

Batch 172 is a bounded review of exactly the 25 supplied queue rows for
filtered queue ordinals 3751–3775. The raw artifact is
`module21a_batch172_review.tsv` and uses the exact 13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

No Module20A file, shared register, canonical queue, or signaling staging
table was modified. No terminal TF was assigned; every `terminal_TF` value is
the literal `null`.

## Disposition

| Status | Count |
|---|---:|
| `reviewed_relay_candidate` | 14 |
| `reviewed_function_only` | 2 |
| `reviewed_binding_only` | 1 |
| `reviewed_unresolved` | 1 |
| `no_evidence_boundary` | 7 |
| **Total** | **25** |

The direct/receptor-proximal/function layers are retained independently in
the TSV. A downstream function or pathway label was not used to infer direct
ligand–receptor interaction. Processed complement fragments (C3d/C3dg and
C4d), composite BMP receptor complexes, the Ccl21b/Ccl27b paralog boundaries,
and atypical-receptor/scavenger claims are explicitly limited in the row-level
`limitations` field.

## Exact queue order

| Queue row | Pair | Status | Confidence |
|---|---|---|---|
| M20A-LIANA-REMAINING-0018 | Bmp8a Bmpr1a_bmpr2 | reviewed_relay_candidate | medium-high |
| M20A-LIANA-REMAINING-0019 | Bmp8a Bmpr1b_bmpr2 | reviewed_unresolved | low |
| M20A-LIANA-REMAINING-0020 | Btla Tnfrsf14 | reviewed_relay_candidate | medium |
| M20A-LIANA-REMAINING-0021 | C3 C3ar1 | no_evidence_boundary | low |
| M20A-LIANA-REMAINING-0022 | C3 Cr2 | reviewed_relay_candidate | medium-high |
| M20A-LIANA-REMAINING-0023 | C4a C3ar1 | no_evidence_boundary | low |
| M20A-LIANA-REMAINING-0024 | C4b Cr2 | reviewed_binding_only | medium |
| M20A-LIANA-REMAINING-0025 | Calr Lrp1 | reviewed_function_only | medium |
| M20A-LIANA-REMAINING-0026 | Ccl1 Ccr8 | reviewed_relay_candidate | medium-high |
| M20A-LIANA-REMAINING-0027 | Ccl11 Ccr3 | reviewed_relay_candidate | high |
| M20A-LIANA-REMAINING-0028 | Ccl11 Ccr5 | reviewed_function_only | low-medium |
| M20A-LIANA-REMAINING-0029 | Ccl12 Ccr2 | reviewed_relay_candidate | medium-high |
| M20A-LIANA-REMAINING-0030 | Ccl17 Ccr4 | reviewed_relay_candidate | medium |
| M20A-LIANA-REMAINING-0031 | Ccl2 Ccr5 | no_evidence_boundary | low |
| M20A-LIANA-REMAINING-0032 | Ccl20 Ccr6 | reviewed_relay_candidate | medium-high |
| M20A-LIANA-REMAINING-0033 | Ccl21b Ccr7 | no_evidence_boundary | low |
| M20A-LIANA-REMAINING-0034 | Ccl21b Cxcr3 | no_evidence_boundary | low |
| M20A-LIANA-REMAINING-0035 | Ccl22 Ccr4 | reviewed_relay_candidate | medium |
| M20A-LIANA-REMAINING-0036 | Ccl24 Ccr3 | reviewed_relay_candidate | medium |
| M20A-LIANA-REMAINING-0037 | Ccl25 Ccr9 | reviewed_relay_candidate | medium |
| M20A-LIANA-REMAINING-0038 | Ccl27b Ccr3 | no_evidence_boundary | low |
| M20A-LIANA-REMAINING-0039 | Ccl28 Ccr10 | reviewed_relay_candidate | medium-high |
| M20A-LIANA-REMAINING-0040 | Ccl28 Ccr3 | reviewed_relay_candidate | medium |
| M20A-LIANA-REMAINING-0041 | Ccl4 Ccr5 | reviewed_relay_candidate | medium-high |
| M20A-LIANA-REMAINING-0042 | Ccl5 Ackr2 | no_evidence_boundary | low |

## Evidence boundary notes

- BMP8A–BMPR1A/BMPR2 is supported by a primary receptor-complex study in mouse spermatogonia, including SMAD1/5/8 activation and differentiation. BMPR1B/BMPR2 was not transferred from BMPR1A evidence.
- BTLA–TNFRSF14/HVEM is retained as a trans-cellular interaction with receptor-dependent immune inhibition; cis/trans geometry and the absence of an SCI receiver model remain limitations.
- Complement rows distinguish intact precursors from processed fragments: C3d/C3dg–CR2 is a supported B-cell coreceptor branch, C4d/C4b–CR2 is binding-only, and C3/C3AR1 plus C4a/C3AR1 remain exact-pair no-evidence boundaries because the primary C3AR1 work tests C3a.
- CALR–LRP1 is retained as receptor-dependent uptake/function context, not as a standalone purified ligand-receptor activation edge.
- Canonical chemokine axes are retained where primary receptor binding, receptor perturbation, or receptor-dependent chemotaxis was available. CCL11–CCR5 is function-only because CCR5-positive-cell association was not receptor-specific; CCL2–CCR5 and CCL5–ACKR2 remain no-evidence boundaries.
- Ccl21b and Ccl27b are not collapsed into canonical CCL21 or CCL27 evidence. Ccl21b–CCR7, Ccl21b–CXCR3, and Ccl27b–CCR3 remain unresolved/no-evidence exact-symbol rows.
