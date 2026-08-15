# Module 21A batch 028 summary

## Scope

Reviewed the 25 exact Module20A priority-8 low/uncertain rows `M20A-CELLCHAT-REMAINING-0001` through `M20A-CELLCHAT-REMAINING-0025`. The frozen queue was read first and all 25 IDs were present with the expected canonical pair labels. This batch was read-only with respect to Module20A and the shared Module21A registers.

Search boundaries included exact pair and alias searches across PubMed, PMC, publisher pages, and pathway/pharmacology resources. Primary research was used for the promotable receptor/pathway evidence. Family-level, database-only, coexpression, and enzyme-processing context was not promoted to a direct molecular edge.

## Classification

| Status | Count | Notes |
|---|---:|---|
| `reviewed_relay_candidate` | 8 | Two 22(R)-hydroxycholesterol→FXR rows; four 2-AG→CB1/CB2 rows; two 2-AG→GPR55 rows retained with pharmacology conflict. |
| `reviewed_function_only` | 2 | 12-oxo-LTB4 produced weak residual leukocyte Ca2+ activity, but LTB4R1/2 subtype assignment was not shown. |
| `reviewed_binding_only` | 0 | No exact pair met a binding-only standard. |
| `reviewed_no_downstream_evidence` | 0 | No row had a validated exact receptor edge with downstream evidence absent as the most appropriate classification. |
| `reviewed_unresolved` | 15 | All 5-HT-DOPA-DDC→DRD/HTR composite rows; the mixed ligand/precursor/enzyme notation cannot be treated as one exact ligand→receptor edge. |

## Promoted or retained relay evidence

- `22HC-CYP11A1-Nr1h4`: CYP11A1 produces 22(R)-hydroxycholesterol as a cholesterol-hydroxylation intermediate, and independent primary work showed 22(R)-hydroxycholesterol activates FXR/NR1H4 through its ligand domain and induces the FXR-responsive ABCB11/BSEP promoter. Terminal TF assignment: `NR1H4 (FXR)`.
- `22HC-CYP3A4-Nr1h4`: recombinant CYP3A4 studies support low 22R-hydroxylation activity, while the independent FXR study supports 22(R)-hydroxycholesterol→FXR→BSEP. This is medium confidence because physiological CYP3A4-to-22HC flux and same-cell coupling were not shown. Terminal TF assignment: `NR1H4 (FXR)`.
- `2AG-DAGLA/DAGLB-Cnr1/Cnr2`: primary pharmacology and knockout/perturbation studies support 2-AG activation of CB1/CB2 and downstream Gi/o-linked Fyn/ERK signaling with AP-1 reporter output. DAGLα and DAGLβ source evidence is model-separated from the receptor relay, so the records remain relay candidates rather than direct enzyme–receptor molecular edges.
- `2AG-DAGLA/DAGLB-Gpr55`: an early primary study reported 2-AG GTPγS activation of GPR55 and Gα13/Rho-family signaling, but later primary ligand-panel work did not reproduce 2-AG activation in a Gα13 BRET assay and favors LPI. These rows are retained as low-medium relay candidates with the conflict explicit.

## Unresolved composite rows

Rows 0011–0025 combine 5-HT with DOPA and DDC. DDC converts DOPA to dopamine; it does not establish serotonin production, and DRD1–5 are dopamine receptors while HTR1/2/3/4 are serotonin receptors. Primary 5-HT receptor studies were retained only as contextual boundaries and were not transferred to the composite rows. No terminal TF was assigned for these rows.

## Files changed

- `work/module21_relay/module21a_batch028_review.tsv`
- `work/module21_relay/module21a_batch028_summary.md`

No Module20A ledger, frozen manifest, or shared Module21A register was modified.
