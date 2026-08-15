# Module 21A batch 179 review summary

Batch 179 reviews exactly filtered queue ordinals 3926–3950 from
`work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`,
where `review_priority=8` and `confidence_decision` is `low` or `uncertain`.
The 25 queue-aligned IDs are `M20A-LIANA-REMAINING-0198` through
`M20A-LIANA-REMAINING-0222`, in the supplied order. The raw artifact uses the
exact 13-column schema of `module21a_batch175_review.tsv`:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

## Disposition

| Status | Count |
|---|---:|
| `reviewed_relay_candidate` | 19 |
| `reviewed_binding_only` | 4 |
| `reviewed_function_only` | 1 |
| `no_evidence_boundary` | 1 |
| **Total** | **25** |

## Queue alignment

| Filtered ordinal | Review ID | Pair | Status | Confidence |
|---:|---|---|---|---|
| 3926 | M20A-LIANA-REMAINING-0198 | Pdgfc Pdgfra | reviewed_relay_candidate | medium |
| 3927 | M20A-LIANA-REMAINING-0199 | Pf4 Cxcr3 | no_evidence_boundary | low |
| 3928 | M20A-LIANA-REMAINING-0200 | Pspn Gfra4_ret | reviewed_relay_candidate | medium-high |
| 3929 | M20A-LIANA-REMAINING-0201 | Rarres2 Ccrl2 | reviewed_binding_only | medium-high |
| 3930 | M20A-LIANA-REMAINING-0202 | Reln Lrp8 | reviewed_relay_candidate | medium-high |
| 3931 | M20A-LIANA-REMAINING-0203 | Reln Vldlr | reviewed_relay_candidate | medium-high |
| 3932 | M20A-LIANA-REMAINING-0204 | Retn Tlr4 | reviewed_relay_candidate | medium-high |
| 3933 | M20A-LIANA-REMAINING-0205 | Rspo1 Fzd8 | reviewed_relay_candidate | medium |
| 3934 | M20A-LIANA-REMAINING-0206 | Rspo3 Fzd8 | reviewed_relay_candidate | medium |
| 3935 | M20A-LIANA-REMAINING-0207 | S100a8 Ager | reviewed_function_only | low-medium |
| 3936 | M20A-LIANA-REMAINING-0208 | S100a8 Tlr4 | reviewed_relay_candidate | medium-high |
| 3937 | M20A-LIANA-REMAINING-0209 | S100a9 Ager | reviewed_binding_only | medium |
| 3938 | M20A-LIANA-REMAINING-0210 | S100a9 Tlr4 | reviewed_relay_candidate | medium-high |
| 3939 | M20A-LIANA-REMAINING-0211 | S100b Ager | reviewed_relay_candidate | high |
| 3940 | M20A-LIANA-REMAINING-0212 | Saa1 Tlr2 | reviewed_relay_candidate | medium-high |
| 3941 | M20A-LIANA-REMAINING-0213 | Sema3a Nrp2 | reviewed_binding_only | medium |
| 3942 | M20A-LIANA-REMAINING-0214 | Sema4a Plxnb1 | reviewed_relay_candidate | medium |
| 3943 | M20A-LIANA-REMAINING-0215 | Sema4a Plxnb2 | reviewed_relay_candidate | medium |
| 3944 | M20A-LIANA-REMAINING-0216 | Sema4a Plxnb3 | reviewed_relay_candidate | medium |
| 3945 | M20A-LIANA-REMAINING-0217 | Sema4c Plxnb2 | reviewed_relay_candidate | high |
| 3946 | M20A-LIANA-REMAINING-0218 | Sema4g Plxnb2 | reviewed_relay_candidate | medium-high |
| 3947 | M20A-LIANA-REMAINING-0219 | Sema5a Plxna1 | reviewed_binding_only | medium |
| 3948 | M20A-LIANA-REMAINING-0220 | Sema5a Plxnb3 | reviewed_relay_candidate | medium-high |
| 3949 | M20A-LIANA-REMAINING-0221 | Sema6a Plxna2 | reviewed_relay_candidate | medium-high |
| 3950 | M20A-LIANA-REMAINING-0222 | Sema6a Plxna4 | reviewed_relay_candidate | medium-high |

## Evidence-layer decisions and boundaries

- The TSV keeps ligand-receptor binding, receptor-proximal relay, and
  downstream pathway/function in separate `evidence_layer` components. A
  pathway, phenotype, expression result, or database seed was not used as
  proof of a direct molecular edge.
- PF4/CXCL4–CXCR3 is an explicit no-evidence boundary. Primary work describes
  CXCL4 as lacking an established receptor that explains its activity and
  instead supports glycosaminoglycan/proteoglycan localization. CXCL4L1 is a
  distinct variant with CXCR3 activity, and CXCL4 responses in monocytes were
  reported as CXCR3B-independent. That evidence was not transferred to PF4.
- RARRES2/chemerin–CCRL2 is binding-only because CCRL2 is an atypical,
  non-signaling receptor. S100A8–AGER is function-only because the primary
  assay used RAGE blockade to alter migration but did not demonstrate purified
  binary binding.
- RELN/LRP8 and RELN/VLDLR retain the Dab1/Src/PI3K-Akt developmental neuronal
  relay, but receptor clustering and neuronal context remain explicit. PSPN–
  GFRA4_RET is a composite receptor row; chicken GFRA4/RET survival evidence
  and rat GFRA4 binding are not treated as identical mammalian receptor
  activation results.
- RSPO1/3–FZD8 are recorded as Wnt-potentiation rows with multi-component
  LGR/RNF43/ZNRF3 context. The Cristin/R-spondin family paper supports FZD8/
  LRP6 interaction and TCF-dependent activation, but R-spondins were not
  treated as canonical WNT ligands. RSPO3 remains family-level and medium
  confidence in this packet.
- S100A8/A9 rows retain MD-2/CD14, oligomerization, species, and heterocomplex
  caveats. S100A9–AGER direct binding is strongest in human biochemical work;
  S100A8–AGER remains rat functional evidence only. RELA/p65 is used only
  where the cited primary study directly measured NF-kB/p65 pathway output;
  otherwise `terminal_TF` is the literal value `null`.
- Sema4A–Plexin-B1/B2/B3 is supported by a primary receptor-transfection and
  Rnd1/cell-contraction study, but the engineered-cell and membrane-context
  limitations are retained. Sema4C–Plexin-B2 has the strongest developmental
  binding and genetic/function evidence; Sema4G–Plexin-B2 shares the in vivo
  context but has less isolated intracellular-branch resolution.
- Sema5A–Plexin-A1 is binding-only because the cited study's strongest
  functional/genetic causality was assigned to Plexin-A2. Sema5A–Plexin-B3
  retains direct high-affinity binding and receptor-dependent MET/motility
  function. Sema6A–Plexin-A2/A4 retain guidance and receptor-complex evidence,
  with explicit cis/trans, redundancy, and tissue-context boundaries.

## Source posture

Primary support was checked against PubMed, PMC, publisher full text, and
curated pathway/database locators where useful. Stable citations in the TSV
include primary work for PDGF-C/PDGFRA, persephin/GFRA4-RET, CCRL2/chemerin,
Reelin receptors, resistin/TLR4, R-spondin/FZD8, S100/RAGE/TLR4, SAA1/TLR2,
neuropilin-2, B-type plexins, Sema5A receptors, and Sema6A receptors. Database
presence or CellChat/LIANA consensus was retained only as queue provenance and
was not promoted into a direct edge without primary support.

No Module20A file, queue, shared Module21A register, handoff, or integration
ledger was modified. Only the requested review TSV and summary were written.

## Files written

- `work/module21_relay/module21a_batch179_review.tsv`
- `work/module21_relay/module21a_batch179_summary.md`
