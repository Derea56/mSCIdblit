# Module 21A batch 032 review summary

## Scope

Reviewed exactly the frozen Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0101` through `M20A-CELLCHAT-REMAINING-0125` (25 unique rows). Queue membership and canonical pair labels were checked against `module20a_external_review_queue.tsv` before finalization.

The batch contains:

- 6 `5-HT-TPH2_SLC6A4` rows: HTR2C, HTR3 complex, HTR4, HTR5A, HTR6, and HTR7.
- 1 `5alphaP-DHRS9 Pgr` row.
- 10 `Ach-CHAT_SLC10A4` rows: M1–M5 muscarinic receptors and the five requested nicotinic receptor complexes.
- 8 `Ach-CHAT_SLC18A3` rows: M1–M5, α1β1δε, α1β1γδ, and α3β4. The queue ends at `0125`; `0126` and later rows were excluded.

## Classification

- Exact rows reviewed: 25
- `reviewed_relay_candidate`: 24
- `reviewed_binding_only`: 1 (`5alphaP-DHRS9 Pgr`)
- `reviewed_function_only`: 0
- `reviewed_unresolved`: 0
- Terminal TF assignments: 0

The 5-HT rows are supported at the mature 5-HT receptor level: HTR2C uses Gq/11–PLC–Ca2+–ERK; HTR3 is a ligand-gated cation-channel complex; HTR4, HTR6, and HTR7 use Gs/cAMP branches; HTR5A uses a Gi/o-linked branch. None of these assays coupled TPH2 biosynthesis or SLC6A4 reuptake to receptor activation.

The muscarinic rows retain subtype-specific receptor-proximal evidence: M1/M3/M5 are associated with PTX-insensitive Gq/11/PLC or KCNQ-current branches, while M2/M4 support Gi/o-mediated adenylyl-cyclase inhibition. The nicotinic rows preserve receptor-complex identity and use direct ACh-evoked electrophysiology for α1β1δε, α1β1γδ, α3β4, α4β2, and α7 assemblies. CHAT biosynthesis and SLC10A4 or SLC18A3/VAChT handling were not manipulated in those receptor assays.

The `5alphaP-DHRS9 Pgr` row is deliberately binding-only. Primary studies support species- and sequence-dependent 5α-dihydroprogesterone/PGR binding, but the queued DHRS9 production step was not coupled to PGR activation, and no direct terminal transcription-factor readout was assigned.

## Search boundaries and limitations

Searches covered exact receptor/subunit combinations and mature-ligand pharmacology in PubMed, PMC, publisher-indexed primary papers, and pathway/pharmacology context. Representative primary sources include HTR2C signaling (PMID 10498829), HTR3 channel activation (PMID 11489465; PMID 15831437), muscarinic M2/M4 second-messenger assays (PMCID PMC1576035), muscarinic M1/M3/M5 KCNQ modulation (PMID 12591092), and comprehensive mouse nicotinic receptor electrophysiology (PMID 20100906; PMCID PMC2872959).

Pathway or receptor-family annotations were used only to name branches. No CellChat label was used to infer a terminal TF. No shared Module21A registers, Module20A ledgers, or frozen manifest were modified.

## File

- `module21a_batch032_review.tsv`
