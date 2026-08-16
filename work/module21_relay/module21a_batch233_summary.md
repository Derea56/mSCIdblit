# Module 21A batch 233 review summary

Batch 233 covers exactly the 25 frozen Module20A queue rows supplied by the user, in the supplied order. The frozen Module20A LR release manifest was verified by SHA-256 as `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Disposition

| Status | Count |
|---|---:|
| `reviewed_relay_candidate` | 13 |
| `reviewed_binding_only` | 2 |
| `reviewed_function_only` | 3 |
| `reviewed_scavenging_only` | 3 |
| `reviewed_no_downstream_evidence` | 3 |
| `reviewed_unresolved` | 1 |
| **Total** | **25** |

Confidence calls are 16 high, 7 medium, and 2 low. `terminal_TF` is literal `null` for 24 rows. `RelB` is retained provisionally for Vcan-Tlr2 because the cited primary study explicitly measured a TLR2-MyD88-RelB-to-PCB transcriptional axis.

## Evidence boundaries

- UCN3-CRHR2, UTS2-UTS2R, UTS2B/URP-UTS2R, VIP-ADCYAP1R1, VIP-VIPR1, and VIP-VIPR2 are direct peptide-GPCR activation branches with measured second-messenger outputs. No terminal TF was assigned to these receptor outputs.
- VCAM1-alpha4beta1 and VCAM1-alpha4beta7 retain the mature integrin heterodimers and adhesion function. The alpha4beta7 edge is activation-state dependent and lower-preference than MAdCAM1.
- Versican-CD44 and versican-SELL are extracellular glycosaminoglycan-dependent adhesion/binding layers. Versican-TLR2 retains the TLR2/TLR6/CD14 receptor-complex and MyD88/RelB functional branch, while recording that hyaluronan or matrix presentation may contribute to the molecular contact.
- VEGFA-CD44 is resolved specifically for CD44v6; VEGFA-GPC1 is an HS-chain-dependent extracellular chaperone/presentation layer. VEGFA-NRP2, VEGFB-NRP1, and processed VEGFC-NRP2 retain isoform, proteolytic, and co-receptor context.
- Vimentin-CD44 is a cell-surface vimentin/CD44 uptake branch. Vitronectin-KDR is explicitly unresolved at the direct molecular level: the primary paper supports vitronectin-alphaVbeta3 and VEGF-KDR co-context, not VTN-KDR binding.
- VWF-GPIb-alpha/GPIb-beta preserves the mature GPIb-IX-V complex: VWF contact maps primarily to GP1BA, with GP1BB retained as a complex-integrity/signaling subunit. VWF-LRP1, VWF-SCARA5, and VWF-STAB2 are uptake/clearance layers, not generic signaling edges. VWF-SELP is endothelial VWF-string anchoring.
- Wnt1-ROR2 is retained as a Wnt1-dependent ROR2/TAK1 receptor-proximal branch, with no claim that ROR2 is the sole Wnt1 receptor.

## Validation

- 25 data rows plus the exact 13-column header.
- Review IDs and pairs match the supplied manifest slice in exact order.
- All required fields are populated; confidence values are only `high`, `medium`, or `low`.
- `terminal_TF` is `null` except for the explicitly measured provisional `RelB` endpoint.
- Stable citations use only PMID, PMCID, DOI, or stable publisher identifiers; no search-result URLs or review-only citations are used.
- No tabs occur inside fields, no extra columns are present, and the frozen manifest SHA-256 matches the requested value.
- Only `work/module21_relay/module21a_batch233_review.tsv` and `work/module21_relay/module21a_batch233_summary.md` were written. Shared registers, Module20A files, the manifest, SQL, and existing files were not modified.
