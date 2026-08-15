# Module 21A batch 031 review summary

## Scope

Reviewed the exact frozen Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0076` through `M20A-CELLCHAT-REMAINING-0100` (25 rows). The queued labels combine serotonin-related processing/transport components with HTR receptor nodes:

- `TPH2 + SLC18A1): 5 rows (`HTR3_complex`, HTR4, HTR5A, HTR6, HTR7)
- `TPH2 + SLC18A2`: 13 rows (HTR1A/B/D/E/F, HTR2A/B/C, HTR3_complex, HTR4/5A/6/7)
- `TPH2 + SLC6A4`: 7 rows (HTR1A/B/D/E/F, HTR2A/B)

Module20A and all shared Module21A registers/ledgers were not modified.

## Classification

- Exact rows reviewed: 25
- `reviewed_relay_candidate`: 25
- `reviewed_function_only`: 0
- `reviewed_binding_only`: 0
- `reviewed_no_downstream_evidence`: 0
- `reviewed_unresolved`: 0
- Terminal TF assignments: 0

The promoted evidence layer is `receptor_proximal_relay`. The TSV keeps upstream serotonin production/vesicular handling or reuptake conceptually separate from direct serotonin-receptor activation and from the measured receptor relay/function.

## Main findings

- HTR1A, HTR1B, HTR1D, HTR1E, and HTR1F: primary receptor-defined assays support 5-HT-stimulated Gi/o-linked inhibition of adenylyl cyclase/cAMP, with subtype- and cell-context-dependent Ca2+, PLC, ERK, or growth outputs.
- HTR2A, HTR2B, and HTR2C: primary studies support 5-HT-linked Gq/11→PLC/Ca2+ relay; HTR2A and HTR2C include ERK measurements, and HTR2B includes an astrocyte glycogenolytic output.
- HTR3 complex: 5-HT-evoked cation currents are supported in HTR3A homomeric and HTR3A/3B heteromeric preparations. The receptor-complex node remains explicit.
- HTR4: 5-HT stimulation supports Gs→adenylyl cyclase/PKA and T-type Ca2+ relay with cortisol secretion in human adrenocortical models.
- HTR5A: 5-HT stimulation supports Gi/o-linked cAMP inhibition and IP3-sensitive Ca2+ mobilization in human HTR5A-expressing C6 glioma cells.
- HTR6 and HTR7: 5-HT stimulation supports Gs-linked cAMP relay; HTR7 also has PKC-MAPK-dependent synaptic-function evidence in mouse cerebellar slices.

## Limitations and search boundaries

Searches were bounded to exact HTR subtype/complex names and serotonin receptor pharmacology in PubMed, PMC, publisher-indexed primary papers, and pathway/pharmacology context. Representative primary records include direct HTR1A/1B/1D/1E/1F second-messenger assays, HTR2A/B/C PLC/Ca2+ studies, HTR3 channel-current studies, and HTR4/5A/6/7 relay/function studies. Pathway resources were used only for branch terminology and receptor-complex context.

The reviewed receptor experiments generally applied exogenous 5-HT or receptor-selective agonists. They did not manipulate TPH2 flux, SLC18A1/VMAT1 packaging, SLC18A2/VMAT2 packaging, or SLC6A4/SERT-mediated reuptake in the same exact source-to-receptor assay. Therefore these records support receptor activation and receptor-proximal relay, not a demonstrated enzyme-to-receptor transfer, local production event, vesicular-release event, or SERT-clearance-to-receptor coupling. Agonist-only evidence is not used to claim that the agonist is the queued ligand. No primary assay directly measured a terminal TF for these exact source branches; no TF was assigned. HTR3 evidence remains a receptor-complex node rather than being collapsed to a single subunit.

## File

- `module21a_batch031_review.tsv`

