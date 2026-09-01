# Module 20–24 promotion queue review — 2026-08-31

## Purpose

This packet records the adjudication state of the 18 supporting-valid rows
that remain outside the Phase-2 source-defined layer. It is a promotion
preparation record, not a canonical database write. Every row is retained
with its submitted identifiers, source locator, evidence description, and a
specific next action. No identifier, Paper relationship, register edge, or
mechanistic direction was inferred in this pass.

## Current disposition

| Queue group | Exact rows | Current evidence state | Promotion disposition | Required next action |
|---|---|---|---|---|
| 20B register gap: LRRC4B/NGL-3–PTPRS | `M20B-P2-R-004191-R162A`, `M20B-P2-R-004191-R162C` | Exact Paper PMID:20139422 is present; the submitted register evidence IDs are not present in `SignalingEdgeRegisterSource`. The source supports a direct trans-synaptic NGL-3/LRRC4B–PTPRS/PTPsigma adhesion interaction and a related functional record. | Hold as promotion candidates. The evidence is usable, but the canonical register/source layer is incomplete. | Adjudicate and create the two exact register-source records, preserving the existing edge `M20B-E004191` and the direct/function distinction. |
| 20B register gap: MIA–alpha4beta1 | `M20B-P2-R-004244-R184A`, `M20B-P2-R-004244-R184B`, `M20B-P2-R-004244-R184C`, `M20B-P2-R-004245-R184A`, `M20B-P2-R-004245-R184B`, `M20B-P2-R-004245-R184C` | Exact Paper PMID:16517605 is present. The source supports MIA engagement of the alpha4beta1 heterodimer and its bounded relay/function records; submitted register evidence IDs are absent from `SignalingEdgeRegisterSource`. | Hold as promotion candidates. Do not collapse alpha4beta1 into isolated ITGA4 or ITGB1 binding. | Adjudicate and create the six exact register-source records, preserving the separate `M20B-E004244` and `M20B-E004245` edges and the direct/relay/function distinctions. |
| 22B abstract-bounded record | `M22B-P2-R-000266` | Exact Paper/register metadata now resolve to PMID:30826495 / DOI:10.1016/j.lfs.2019.01.060 / `M22B-EVID-000304`. The record is explicitly `validated_primary_abstract`; it supports the bounded Sema6A–Plexin-A2–RANKL–PLCγ–NFATC1 osteoclastogenesis pathway, not direct NFATC1 target occupancy. | Keep as paper provenance and an abstract-level candidate. Do not admit as a Phase-2 full source unit under the current gate. | If full text becomes available, re-review figure-level evidence. Otherwise retain the abstract-bounded status and lower-context interpretation. |
| 22B source-identity conflict | `M22B-P2-R-000396` | The queue declares PMID:31940275 with PMCID:PMC10409762. The local PMC artifact embeds a different PMID (37553521) and its title/content do not agree with the declared PubMed identity. The authoritative PubMed record for PMID:31940275 is a BMP8A granulosa-cell paper, not the local adipogenesis artifact. | Hold. Do not attach the local artifact to PMID:31940275 or promote the queued receptor/TF claim from this unresolved identity. | Resolve the exact source identity from an authoritative record. If the local artifact is the intended source, replace the queued PMID only after direct evidence establishes its correct PMID/DOI/PMCID relationship; otherwise preserve the row unresolved. |
| 23B source-identity conflict | `M23B-P2-R-000018` | The queue declares PMID:24932026 with PMCID:PMC4116228 and DOI:10.1371/journal.pone.0103839. The authoritative PMC/PubMed record identifies PMC4116228 as PMID:25075518, the LRP-1/TIMP-1 study; the declared PMID does not match that source. | Hold as a strong identity-correction candidate. The direct LRP1–TIMP1 evidence itself is reviewable, but the canonical Paper relationship is not safe to write from the conflicting row. | Adjudicate the source identity, then update the Paper relationship only with the exact authoritative crosswalk. Preserve LRP1 domains II/IV and the direct binding/endocytic boundary. |
| 23B source-identity conflict: Fzd7 | `M23B-P2-R-000345`, `M23B-P2-R-000346`, `M23B-P2-R-000347` | The queue declares PMID:31907106 with PMCID:PMC7487719 and DOI:10.1186/s12964-020-00646-2. The authoritative record identifies that PMCID/DOI as PMID:32894152, the Fzd7/Wnt5b/Col6a1 study; PMID:31907106 is a distinct Fzd2 paper. | Hold as identity-correction candidates. The local evidence supports a contextual Fzd7-associated Wnt5a/b claim, not a purified WNT5B–FZD7 affinity edge. | Adjudicate the PMID correction as a group, then preserve the contextual/unresolved ligand attribution and do not promote direct binary binding without a qualifying assay. |
| 23B no register edge key | `M23B-P2-R-000642` | Exact Paper PMID:31011859 / PMCID:PMC6689289 / DOI:10.1007/s00401-019-02011-1 is present. The source supports an EphrinB3-dependent Eph receptor complex response involving EphA4 and EphB1/B2, with EphB6 as a bounded kinase-defective complex component. The Phase-2 row has blank `b_edge_id` and no canonical register edge. | Hold as a source-defined promotion candidate, not a canonical edge. Do not invent an EphB6-specific edge key. | Adjudicate whether an existing canonical edge represents the measured multi-receptor complex. If not, create a new explicitly named register edge only after defining the complex-level scope. |
| 23B mixed-anchor identity conflict | `M23B-P2-R-C23B274-000001`, `M23B-P2-R-C23B274-000002`, `M23B-P2-R-C23B274-000003` | The queue declares PMID:11518717 while citing PMCID:PMC3315466 and PMCID:PMC6821389. The local artifacts embed PMIDs 22479204 and 29941485, respectively, and represent two distinct E-cadherin/IGF1R comparator studies. PMID:11518717 is a different IGF-I receptor cell-adhesion paper. | Hold the group. The two cited studies can be biologically interpreted separately, but they cannot be merged under the current mixed PMID anchor. | Split/adjudicate the source records using exact PMCID/DOI metadata. Preserve the distinct developmental and breast-cancer contexts, the opposing context-specific E-cadherin effects, and the absence of SCI transfer or terminal-TF evidence. |

## Evidence available for later promotion

The following records are sufficiently described for efficient follow-up once
their structural blocker is resolved:

1. The eight 20B rows have exact local Paper support and full observation and
   claim descriptions. Their blocker is register materialization, not a lack
   of mechanistic content. Any future register write must preserve the
   submitted direct/relay/function separation.
2. `M23B-P2-R-000642` has an exact Paper and a bounded receptor-proximal
   observation. Its blocker is the absent edge key, not an absent source.
3. `M23B-P2-R-000018`, the Fzd7 group, and the C23B274 group have usable
   local source content but require paper-identity adjudication before their
   provenance can be canonicalized.
4. `M22B-P2-R-000266` is usable as abstract-level provenance but remains
   outside the full-text Phase-2 layer by design.

The evidence grades and context levels already present in the integrated TSV
remain unchanged. In particular, these rows should not be upgraded to a
stronger context level merely because their source identity or register
relationship is repaired. Mechanistic evidence grade and CNS/spinal-cord/SCI
context are separate dimensions.

## Authoritative identity checks

- PMID:31907106 is the distinct Fzd2 record; the Fzd7 DOI/PMCID pair resolves
  to PMID:32894152 in the official PubMed record:
  <https://pubmed.ncbi.nlm.nih.gov/31907106/>
  <https://pubmed.ncbi.nlm.nih.gov/32894152/>
- PMCID:PMC4116228 resolves to PMID:25075518, the LRP-1/TIMP-1 record:
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC4116228/>
- PMID:31940275 is the BMP8A granulosa-cell record and does not by itself
  validate the local PMC10409762 identity:
  <https://pubmed.ncbi.nlm.nih.gov/31940275/>
- PMID:11518717 is the IGF-I receptor/ZO-1 cell-adhesion record and should
  not be used as the shared anchor for the two cited PMC studies:
  <https://pubmed.ncbi.nlm.nih.gov/11518717/>

## Result of this pass

No canonical Paper, SignalingEdge, SignalingEdgeSource, or
SignalingEdgeRegisterSource rows were changed by this review. The queue is
now partitioned into eight register-gap candidates, one abstract-only
provenance record, eight source-identity correction candidates, and one
paper-anchored row lacking a register edge key. This is the maximum safe
promotion preparation available from the currently reconciled records without
inventing identifiers or canonical mappings.
