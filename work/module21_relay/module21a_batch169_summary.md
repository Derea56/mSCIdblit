# Module 21A batch 169 review summary

Batch 169 reviews exactly the 25 supplied Module 20A queue rows at filtered
queue ordinals 3676–3700. The raw output is
`module21a_batch169_review.tsv` and uses the exact requested 13-column schema:

`review_id`, `pair`, `status`, `stable_citations`, `species`,
`cell_type_model`, `assay_or_perturbation`, `relation_type`, `evidence_layer`,
`pathway_branch`, `confidence`, `limitations`, `terminal_TF`.

## Validation and scope

- 25/25 exact queue IDs and pair labels are preserved in queue order.
- 25 unique review IDs and 25 unique pair labels are present.
- Every row has 13 tab-delimited fields, populated limitations, stable PMID,
  PMCID, DOI, or URL citations, and literal `terminal_TF=null`.
- Binding/activation, receptor-proximal relay, and downstream pathway/function
  are kept as separate evidence layers. Pathway or phenotype results were not
  used to infer direct interaction.
- Only the requested batch TSV and summary were written. Module20A files,
  shared Module21A registers, Module22A handoff files, and integration outputs
  were not modified. No commit was created.

## Disposition

| Status | Rows |
|---|---:|
| `reviewed_relay_candidate` | 2 |
| `reviewed_binding_only` | 3 |
| `reviewed_function_only` | 5 |
| `reviewed_unresolved` | 15 |
| **Total** | **25** |

The relay candidates are WNT3A–APCDD1 and WNT4–NOTCH1. The binding-only rows
are VWF propeptide–ITGA4, VWF propeptide–ITGB1 as part of the alpha4-beta1
complex, and VWF–OPG as a vascular storage/complex interaction without a
TNFRSF11B intracellular relay.
The function-only rows capture VTN-dependent alpha-v-beta-6 adhesion/migration,
WNT1-dependent CD36 regulation, and WNT3A modulation by ATP6AP2, LGR5, or ROR1.

## Layered evidence decisions

| Exact pair | Binding/activation layer | Receptor-proximal relay | Downstream pathway/function | Decision |
|---|---|---|---|---|
| Vwf Itga4 / Vwf Itgb1 | pp-VWF binds the alpha4-beta1/VLA-4 complex in adhesion and affinity assays. | No intracellular adaptor or kinase relay measured. | Adhesion is the measured output. | Binding-only; mature-VWF versus propeptide limitation retained. |
| Vwf Tnfrsf11b | VWF binds OPG/TNFRSF11B in purified and endothelial Weibel-Palade-body assays, with the VWF A1 domain mapped. | No intracellular TNFRSF11B relay was tested. | VWF-OPG complex modulation of platelet-adhesion context is separate from binding. | Binding-only. |
| Vtn Itgb6 | No purified VTN-beta6 binding assay; alpha-v-beta-6 dependence is shown by beta6 deletion and blocking antibody. | No defined kinase/adaptor relay. | Vitronectin-dependent keratinocyte adhesion/migration and PKC-sensitive modulation. | Function-only. |
| Wnt1 Cd36 | No WNT1-CD36 ligand binding; CD36 is an expression target. | No CD36 receptor relay. | WNT1-dependent canonical Wnt/PPAR-gamma/TCF4 regulation of CD36 in macrophage differentiation. | Function-only. |
| Wnt3a Apcdd1 | APCDD1 extracellular domain co-precipitates with WNT3A. | APCDD1 is an extracellular inhibitor, not a demonstrated canonical signaling receptor. | APCDD1 suppresses WNT3A-induced reporter and developmental Wnt outputs. | Relay candidate with inhibitor-context limitation. |
| Wnt3a Atp6ap2 / Lgr5 / Ror1 | No direct WNT3A binding to the queued protein was established. | ATP6AP2, LGR5, and ROR1 modulate Wnt receptor/signaling contexts in distinct models. | WNT3A-induced reporter, LRP6 trafficking, RSPO potentiation, or reporter inhibition is retained as function-only evidence. | Function-only or unresolved according to the exact row. |
| Wnt4 Notch1 | A recent primary report describes WNT4–NOTCH1 protein interaction. | Canonical WNT4 receptor complex and intracellular relay remain unresolved. | Wnt/beta-catenin-dependent c-Jun/VEGFA/CYCD1 and repair outputs are separate functional evidence. | Relay candidate, medium confidence. |

## Explicit unresolved/no-evidence boundaries

- VIP–RAMP3, VIP–SCTR, and VIP–TSHR remain unresolved. The primary studies
  support VIPR1/VPAC1 or VIPR2/VPAC2, secretin–SCTR, and TSH–TSHR branches,
  respectively; receptor-family or shared cAMP signaling was not transferred.
- VTN–CD47, VTN–ITGA3, VTN–ITGA5, and VTN–TNFRSF11B remain unresolved. The
  direct VTN receptor literature is centered on alpha-v-beta-3/alpha-v-beta-5;
  CD47 is an associated component rather than a VTN ligand, and OPG is not
  supported as a VTN ligand.
- VWF–ITGA9 and VWF–SIRPA remain unresolved. Alpha9-beta1 primary studies use
  NGF, VCAM-1, tenascin-C, or osteopontin, while VWF macrophage uptake studies
  implicate LRP1-associated biology rather than SIRPA.
- WFIKKN2–IGDCC3, WFIKKN2–IGDCC4, and WFIKKN2–PRTG remain unresolved. WFIKKN2
  primary biochemical evidence concerns GDF8/myostatin and GDF11, not the
  submitted receptors.
- WIF1–RYK, WNT11–KLRG2, and WNT3A–LRP1 remain unresolved. WIF1/RYK domain
  terminology, WNT11/FZD7 signaling, and WNT3A/LRP5/LRP6 or RYK comparator
  evidence do not establish the exact submitted edges.

No terminal TF was assigned. TCF4/PPAR-gamma, TCF/LEF reporter activity,
beta-catenin, and downstream gene expression are retained in the relevant
pathway/function descriptions but were not promoted to `terminal_TF` without a
pair-specific validated relay and TF endpoint.
