# Module 21A batch 161 review

Date: 2026-08-15

## Scope

Reviewed only the 25 exact filtered-queue rows supplied for batch 161
(queue ordinals 3476–3500). The raw review file preserves the requested
13-column schema and the supplied Module 20A review IDs. The handoff boundary
was applied: a Module 20A ligand–receptor candidate is not treated as proof of
receptor activation or intracellular signaling.

Output: [`module21a_batch161_review.tsv`](./module21a_batch161_review.tsv)

## Disposition

| Status | Rows |
|---|---:|
| `reviewed_unresolved` | 9 |
| `reviewed_binding_only` | 9 |
| `reviewed_function_only` | 5 |
| `reviewed_relay_candidate` | 2 |
| **Total** | **25** |

The nine unresolved rows are M20A-EXT-3154, 3156, 3160, 3161, 3176, 3177,
3186, 3193, and 3204. They retain explicit no-evidence or exact-pair-unresolved
limitations rather than pathway analogies.

The nine binding-only rows are M20A-EXT-3162, 3166, 3167, 3168, 3170, 3171,
3172, 3188, and 3203. These are not downstream relay claims. The SLURP1
results are heteromer-level nAChR electrophysiology for α3β2, α3β4, α4β4,
and α9α10; they were not reassigned to isolated CHRNA/CHRNB subunits. The
SPP1–PTGER4 result is a heterologous GPCR protein-association observation,
not a validated ligand-activation experiment.

The five function-only rows are M20A-EXT-3155, 3163, 3182, 3184, and 3185.
They retain pathway or functional context without upgrading it to an
exact direct interaction. In particular, Slit2–Robo4 signaling was not
claimed because the primary study assigned transduction to Robo1; Slit2–Sdc1
was not promoted from Drosophila Sdc or mammalian SDC4 comparator evidence;
SPARC–FGFR1 was retained as downstream/intracellular antagonism because the
primary study did not show extracellular-domain binding; and Sostdc1–Lrp5
was retained as LRP5/6-dependent Wnt function with direct LRP5 binding
unresolved.

The two relay candidates are:

- M20A-EXT-3174, SNX14–HTR6: direct receptor-proximal regulatory interaction,
  HTR6–Gαs–cAMP control, PKA-dependent switching, and HTR6 trafficking.
- M20A-EXT-3175, SOCS2–EPOR: SOCS2 recognition of phosphorylated EPOR
  peptide and CRL5 negative-feedback substrate handling, with EPO/EPOR/JAK2/
  STAT5 evidence kept separate from the SOCS2 edge.

## Evidence-layer accounting

| Evidence layer | Rows |
|---|---:|
| `ligand_receptor_binding_or_activation` | 10 |
| `receptor_proximal_relay` | 2 |
| `downstream_pathway_function` | 5 |
| `none` | 8 |

No `terminal_TF` was assigned. TF/pathway names appearing in pathway-branch
descriptions are contextual pathway outputs only; they are not asserted as
direct terminal-TF evidence for the exact pair.

## Citation and limitation policy

Stable PMID, PMCID, DOI, and PubMed query URLs are recorded in every TSV row.
Primary studies were used where available. Related-family papers are retained
only to document the boundary and are explicitly identified in the row
limitations. Expression, pathway co-membership, CellPhoneDB/LIANA-style
pairing, and family/paralog evidence were not promoted to direct interaction.
Every row has a populated limitation, including all unresolved/no-evidence
rows.

## Scope protection

No Module20A file, shared Module21A register, Module22A handoff, or canonical
coverage table was modified. No commit was created.
