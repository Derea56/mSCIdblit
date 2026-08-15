# Module 21A evidence review — Batch 178

## Scope

This bounded review covers only filtered queue ordinals 3901–3925 from the
Module20A external-review queue: 25 exact LIANA-remaining rows,
`M20A-LIANA-REMAINING-0173` through `M20A-LIANA-REMAINING-0197`, in queue
order. The raw output is
[`module21a_batch178_review.tsv`](./module21a_batch178_review.tsv) and uses
the exact 13-column batch177 schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

Module20A files and shared Module21A/Module22A ledgers were read-only
context. No shared register or Module20A file was modified.

## Disposition

| disposition | count | rows |
|---|---:|---|
| reviewed_relay_candidate | 17 | 0177–0184, 0186–0193, 0196 |
| reviewed_binding_only | 2 | 0194–0195 |
| no_evidence_boundary | 6 | 0173–0176, 0185, 0197 |
| total | 25 | exact requested batch |

Confidence counts: high 4; medium-high 12; medium 3; low 6.

## Explicit boundary cases

- `0173–0176` (INHBE with ACVR1B/ACVR1C plus ACVR2A/ACVR2B): inhibin A/B
  and related TGF-beta-family studies do not establish INHBE specificity for
  any submitted composite receptor.
- `0185` (LTA–TNFRSF14/HVEM): TNFRSF14/HVEM evidence is centered on
  LIGHT-family signaling, while primary LTA evidence supports TNFR1/TNFR2;
  noncognate family evidence was not transferred.
- `0197` (PDGFA/PDGF-AA–PDGFRB): primary receptor-subtype studies distinguish
  PDGF-AA/PDGFRA signaling from PDGFRB activation by PDGF-BB or PDGF-AB.

These are explicit `no_evidence_boundary` calls, not pathway-only positive
assignments.

## Evidence-layer rules applied

- `binding_activation` records ligand binding, receptor engagement, or
  receptor activation only.
- `receptor_proximal_relay` records receptor cleavage, kinase/adaptor relay,
  receptor-complex assembly, or receptor-dependent perturbation only when the
  primary study supports that step.
- `downstream_pathway_function` records measured pathway or functional outputs
  separately from the ligand–receptor claim.
- Pathway or phenotype evidence was never used by itself to infer a direct
  ligand–receptor interaction.
- `terminal_TF` is literal `null` throughout. RBPJ, TCF/LEF, beta-catenin,
  STAT3, SMAD, MAPK, and NF-kappaB outputs were retained as pathway/function
  context rather than promoted to terminal TF assignments.

## Main findings

- Direct or receptor-dependent Notch evidence supports JAG1–NOTCH1/2/3/4 and
  JAG2–NOTCH1/2/3, with receptor-specific differences in binding strength,
  ligand presentation, and signal output. JAG1–NOTCH4 is retained at medium
  confidence because the direct binding assay uses a Notch4 EGF10–14
  peptibody, while vascular genetic/functional evidence supports the pathway
  in endothelial models.
- LEAP2 is retained as a GHSR antagonist/inverse agonist with receptor-binding
  and receptor-dependent physiology. Its effects include GHSR inactive-state
  stabilization and reduced ghrelin-associated outputs, but the evidence does
  not define one native SCI relay.
- LTA–TNFR1 and LTA–TNFR2 are supported by comparative binding and
  receptor-selective functional studies. TNFR2 is recorded conservatively as a
  binding/modulatory branch because the tested LTA response was more strongly
  propagated through TNFR1.
- MIF–ACKR3/CXCR7, MSMP/PSMP–CCR2B, NDP/Norrin–FZD4, NRTN–GFRA2–RET,
  NGF–NGFR, NGF–NTRK1, and PDGFA–PDGFRA have primary binding or
  receptor-dependent relay support. Composite receptor notation is preserved
  as submitted; the NRTN row explicitly retains the biologically required
  tripartite GFRA2–RET complex.
- NTF3–NGFR and NTF5–NGFR are retained as `reviewed_binding_only`: primary
  neurotrophin/p75 studies support direct binding, but an autonomous exact
  NGFR downstream relay was not assigned.

## Limitations and handoff boundary

Most positive evidence comes from recombinant receptor fragments,
engineered-cell systems, neuronal or hematopoietic models, endothelial and
cancer contexts, or comparative TNF/neurotrophin assays rather than spinal
cord injury receiver cells. Ligand processing, receptor isoforms,
heteromeric-complex stoichiometry, membrane presentation, Fringe or other
co-receptor effects, and species/cell-state dependence are recorded in each
TSV row. No Module22A terminal-TF program or SCI-specific functional claim
should be created from these rows without a separate TF-level review.

## Validation target

The TSV contains one header plus exactly 25 data rows, 25 unique review IDs
matching filtered queue ordinals 3901–3925, 13 fields per row, populated
stable citations and limitations, and literal `null` in `terminal_TF` for all
rows. The four confidence values that had a leading space were normalized to
`high` before validation.
