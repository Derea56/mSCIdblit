# Module 21A batch 204 summary

## Scope

This batch reviews exactly the 25 requested queued Module 20A pairs:

`M20A-EXT-1264`, `M20A-EXT-1276`–`M20A-EXT-1279`, `M20A-EXT-1296`,
`M20A-EXT-1300`–`M20A-EXT-1305`, `M20A-EXT-1340`–`M20A-EXT-1352`.

The review preserves the submitted ligand and receptor labels exactly. It
does not modify Module 20A ledgers, Module 21A ledgers, the Module 22A
handoff, or the frozen Module 20A release manifest.

## Disposition

- 4 `reviewed_relay_candidate`: COL1A1–DDR2, COL2A1–DDR1, COL3A1–DDR1,
  and COL3A1–DDR2.
- 10 `reviewed_binding_only`: COL22A1–ITGA10/11/1/2-ITGB1,
  COL3A1–ITGA10/11/1/2-ITGB1, COL7A1–ITGA2-ITGB1, and
  COL8A2–SLC4A11.
- 11 `no_evidence_boundary`: COL7A1–ITGA1-ITGB1, COL8A1–
  ITGA10/11/1/2-ITGB1, COL8A2–ITGA10/11/1/2-ITGB1, and
  COL9A1/COL9A2–MAG.

Evidence layers are kept separate in the TSV. DDR rows carry
ligand/receptor binding or activation and receptor-proximal
autophosphorylation where directly measured. The COL22A1, COL3A1 integrin,
COL7A1, and COL8A2–SLC4A11 rows remain binding/adhesion-only; no intracellular
relay was inferred from adhesion, co-localization, or pathway annotation.

## Primary evidence anchors

- COL1A1–DDR2: PMID 12611880 and PMID 21335558/PMCID PMC3075638. The latter
  directly tests collagen-I stimulation in human lung fibroblasts and reports
  DDR2/JAK2/ERK1/2-dependent downstream responses, including MMP10 and PEA3
  recruitment to the DDR1 promoter. PEA3 is recorded as a provisional,
  context-specific endpoint rather than a universal terminal TF.
- COL2A1/COL3A1–DDR1/DDR2: PMID 21044884 and PMCID PMC3034869, which map
  collagen-II/III binding sites and test receptor autophosphorylation for
  GVMGFO-containing triple-helical peptides.
- COL22A1 integrins: PMID 24428702, DOI 10.1042/BJ20130642, with motif-level
  binding, SPR/solid-phase assays, and limited tissue co-localization.
- COL3A1 integrins: PMCID PMC5380659, PMID 16043429/PMCID PMC3406685, and
  PMID 36517525/PMCID PMC9751114; peptide/domain and adhesion evidence is
  retained without promoting a downstream relay.
- COL7A1–ITGA2/ITGB1: PMID 10366422, an NC1-fragment dermal fibroblast
  attachment study; retained as binding-only with the fragment limitation.
- COL8A2–SLC4A11: PMID 31691803, human corneal endothelial/Descemet's-
  membrane extracellular-loop interaction and adhesion assays; no canonical
  receptor-proximal signaling was demonstrated.

## Search boundaries and unresolved cases

Exact-pair searches used PubMed and Europe PMC with gene/protein aliases,
collagen-chain and heterotrimer terms, mature/processed or fragment forms,
integrin subunits and heterodimers, binding/activation/structure/function
terms, citation trails, and pathway/structure cross-checks. Generic
collagen-family evidence, co-expression, cell-level association, and
integrin-family analogies were not transferred to untested exact pairs.

The negative rows therefore record an explicit search boundary, not a claim
that the proteins can never interact. In particular, the MAG/collagen primary
study located in the search boundary tested collagen types I, II, III, and V,
not collagen IX; it was not transferred to COL9A1 or COL9A2.

## Validation

- 25 data rows plus the required header.
- Exact 13-column schema:
  `review_id,pair,status,stable_citations,species,cell_type_model,assay_or_perturbation,relation_type,evidence_layer,pathway_branch,confidence,limitations,terminal_TF`.
- Review IDs and pair labels are unique and exact to the requested list.
- All fields are populated; confidence values are from the established
  Module 21A vocabulary.
- `terminal_TF` is literal `null` for 24 rows; PEA3 is present only for the
  explicit promoter-recruitment observation in the COL1A1–DDR2 context.
- No SQL materialization or ledger update was performed.
