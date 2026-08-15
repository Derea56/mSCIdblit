# Module 21A Batch 193 review summary

Batch 193 reviews exactly the 25 supplied Module20A external-review pairs. The
raw artifact is `module21a_batch193_review.tsv` and uses the exact 13-column
schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

## Disposition

| status | count |
|---|---:|
| `reviewed_relay_candidate` | 9 |
| `reviewed_binding_only` | 8 |
| `reviewed_unresolved` | 2 |
| `no_evidence_boundary` | 6 |
| **total** | **25** |

Confidence counts: medium-high 8; medium 7; low-medium 1; low 9. Every
`terminal_TF` value is the literal `null`.

## Exact pair scope

The packet preserves the 25 supplied IDs and labels exactly:

`M20A-CELLCHAT-REMAINING-0268`–`0277`, `M20A-CELLCHAT-REMAINING-0370`,
`M20A-CELLCHAT-REMAINING-0381`, `M20A-CELLCHAT-REMAINING-0389`–`0401`, and
`M20A-CELLCHAT-REMAINING-0450`.

The pair labels retain the submitted receptor-complex notation
`CNTN2_CNTNAP2` and the submitted receptor paralog labels `Ccr1l1`.

## Evidence decisions

- **Bounded relay candidates.** CCL8/MCP-2 has direct binding and receptor-dependent chemotaxis or calcium/function evidence for CCR1, CCR2B, and CCR5. CCL9 has CCR1 activation and chemotaxis/recruitment evidence with strong dependence on N-terminal processing. CSF1-CSF1R and EGF-EGFR retain direct ligand binding, receptor-proximal kinase activation, and downstream myeloid or growth outputs. CXCL11-CXCR3 and CXCL9-CXCR3 retain direct receptor activation with Gi/PLC/Ca2+-linked chemotaxis. CD160-TNFRSF14/HVEM retains direct binding and receptor-dependent immune function.

- **Binding or atypical-receptor boundaries.** CCL7-CCR3 is retained as direct binding only. CNTN2-CNTNAP2 is retained as a direct adhesion-complex interaction with axonal-growth function, not as a canonical intracellular receptor relay. CXCL1, CXCL2, CXCL3, CXCL5, and CXCL11 ACKR1 rows retain atypical DARC/ACKR1 binding or scavenging boundaries; none is treated as canonical G-protein signaling. CXCL11-ACKR3 retains binding/scavenging/desensitization evidence without canonical calcium, ERK, or AKT activation.

- **Unresolved exact identities.** CCL8-CCR1L1 and CCL9-CCR1L1 retain related CCR1-family, paralog, species, or broad chemokine evidence only. Those comparator observations were not promoted to the submitted exact receptor identities.

- **Explicit no-evidence boundaries.** CCL8-ACKR1, CCL8-ACKR4, CXCL10-ACKR1, CXCL13-ACKR1, CXCL3-CXCR1, and CXCL9-ACKR1 remain unassigned after exact-pair searches. CXCL10-CXCR3, CXCL13-CXCR5, CXCL1/2/5 ACKR1, and other family-level or review-level observations were not transferred to these exact pairs.

## Layer and terminal-TF boundary

Ligand-receptor binding or activation, receptor-proximal relay, and downstream
pathway or cellular function were recorded separately. Direct molecular
interaction was not inferred from receptor-family analogy, pathway-level
cross-talk, uptake/scavenging, expression, or phenotype alone. MAPK, PI3K-AKT,
Gi/o, PLC, Ca2+, beta-arrestin, and receptor-kinase outputs remain pathway or
functional annotations; no terminal TF met the explicit Module22A boundary.

## Search boundary and validation

Searches used primary PubMed/PMC and publisher records where available, with
targeted Europe PMC and exact-pair query URLs retained for negative or
unresolved cases. Family-level chemokine receptor lists, Reactome/pathway
annotations, expression-only results, and noncognate ligand studies were used
only as search comparators and not as exact-pair evidence.

Validation completed before handoff:

- 25 data rows, all unique review IDs and pair labels.
- Exact 13-column schema on every row.
- Exact alignment to the supplied frozen external-review queue entries.
- All required fields populated; confidence vocabulary valid.
- All terminal TF values are literal `null`.
- Only the batch 193 TSV and summary are written; shared Module20A/21A ledgers and the frozen manifest are untouched.
