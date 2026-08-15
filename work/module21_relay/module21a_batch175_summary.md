# Module 21A batch 175 review summary

Batch 175 reviews exactly the 25 supplied filtered-queue rows, ordinals
3826–3850. The raw artifact is
`work/module21_relay/module21a_batch175_review.tsv` and uses the exact 13-column
TSV schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

Every row has a unique supplied `review_id`, the exact supplied pair label, a
populated `limitations` field, stable PMID/PMCID/DOI/URL citations, and the
literal `terminal_TF=null`. No Module20A file, shared Module21A register,
queue, handoff, or integration output was modified, and no commit was made.

## Disposition

| Status | Count |
|---|---:|
| `reviewed_relay_candidate` | 10 |
| `reviewed_binding_only` | 6 |
| `reviewed_function_only` | 2 |
| `reviewed_unresolved` | 1 |
| `no_evidence_boundary` | 6 |
| **Total** | **25** |

## Exact queue order

| Review ID | Pair | Status | Confidence |
|---|---|---|---|
| M20A-LIANA-REMAINING-0097 | Efnb1 Ephb2 | reviewed_relay_candidate | medium-high |
| M20A-LIANA-REMAINING-0098 | Efnb1 Ephb3 | reviewed_relay_candidate | medium |
| M20A-LIANA-REMAINING-0099 | Efnb1 Ephb4 | no_evidence_boundary | low |
| M20A-LIANA-REMAINING-0100 | Efnb1 Ephb6 | reviewed_function_only | medium |
| M20A-LIANA-REMAINING-0101 | Efnb2 Epha4 | reviewed_binding_only | medium-high |
| M20A-LIANA-REMAINING-0102 | Efnb2 Ephb2 | reviewed_binding_only | medium |
| M20A-LIANA-REMAINING-0103 | Efnb2 Ephb3 | reviewed_unresolved | low-medium |
| M20A-LIANA-REMAINING-0104 | Efnb2 Ephb4 | reviewed_relay_candidate | medium-high |
| M20A-LIANA-REMAINING-0105 | Efnb2 Ephb6 | reviewed_binding_only | medium-high |
| M20A-LIANA-REMAINING-0106 | Efnb3 Epha4 | reviewed_relay_candidate | medium-high |
| M20A-LIANA-REMAINING-0107 | Efnb3 Ephb1 | no_evidence_boundary | low |
| M20A-LIANA-REMAINING-0108 | Efnb3 Ephb2 | no_evidence_boundary | low |
| M20A-LIANA-REMAINING-0109 | Efnb3 Ephb3 | reviewed_binding_only | medium-high |
| M20A-LIANA-REMAINING-0110 | Efnb3 Ephb4 | no_evidence_boundary | low |
| M20A-LIANA-REMAINING-0111 | Fasl Fas | reviewed_relay_candidate | medium-high |
| M20A-LIANA-REMAINING-0112 | Fbln2 Itgb3 | reviewed_function_only | low-medium |
| M20A-LIANA-REMAINING-0113 | Fga Itga2b | reviewed_binding_only | medium |
| M20A-LIANA-REMAINING-0114 | Fga Itgb3 | reviewed_binding_only | medium |
| M20A-LIANA-REMAINING-0115 | Fgb Itga2b | no_evidence_boundary | low |
| M20A-LIANA-REMAINING-0116 | Fgb Itgb3 | no_evidence_boundary | low |
| M20A-LIANA-REMAINING-0117 | Fgf1 Fgfr1 | reviewed_relay_candidate | medium-high |
| M20A-LIANA-REMAINING-0118 | Fgf1 Fgfr4 | reviewed_relay_candidate | medium-high |
| M20A-LIANA-REMAINING-0119 | Fgf17 Fgfr1 | reviewed_relay_candidate | medium |
| M20A-LIANA-REMAINING-0120 | Fgf17 Fgfr2 | reviewed_relay_candidate | medium |
| M20A-LIANA-REMAINING-0121 | Fgf18 Fgfr3 | reviewed_relay_candidate | medium |

## Evidence-layer decisions

- Binding/activation, receptor-proximal relay, and downstream pathway/function
  are recorded independently in the raw `evidence_layer` field. A pathway or
  phenotype readout was never used as proof of a direct molecular interaction.
- EFNB1–EPHB2, EFNB1–EPHB3, EFNB2–EPHB4, EFNB3–EPHA4, FASLG–FAS, and the FGF
  rows retain receptor-proximal or receptor-dependent function only to the
  extent supported by the cited perturbation, receptor-binding, or activation
  assays. Ephrin signaling remains contact-dependent and often bidirectional.
- EFNB2–EPHA4, EFNB2–EPHB2, EFNB2–EPHB6, and EFNB3–EPHB3 are retained as
  binding-only records where the primary evidence establishes recognition but
  not a pair-specific intracellular relay.
- EFNB1–EPHB6 is retained as trans co-clustering/adhesion function. EPHB6 is a
  kinase-impaired receptor, so co-clustering is not flattened into a canonical
  kinase cascade.
- EFNB2–EPHB3 is unresolved because vascular studies involve EPHB2/EPHB3
  receptor combinations and do not isolate the exact row as a single relay.
  EFNB1–EPHB4, EFNB3–EPHB1, EFNB3–EPHB2, and EFNB3–EPHB4 are explicit
  no-evidence boundaries; family membership, co-expression, and related
  receptor evidence were not transferred.
- FBLN2–ITGB3 is function-only because the primary adhesion result is
  beta3-integrin-associated and species-crossed, without purified binary
  affinity or a downstream relay.
- FGA/FGB and ITGA2B/ITGB3 are composite ligand/receptor components. The
  positive FGA rows retain intact fibrinogen–alphaIIb-beta3 complex evidence,
  while FGB rows remain no-evidence boundaries for an isolated B-beta-chain
  versus receptor-subunit edge. Intact-complex platelet signaling was not
  reassigned to an individual chain pair.
- FGF1–FGFR1/4, FGF17–FGFR1/2, and FGF18–FGFR3 retain heparan-sulfate,
  perlecan, receptor-domain, and splice-isoform limitations. ERK, AKT, Rho,
  caspases, and other pathway nodes are not assigned as terminal TFs.

## Primary-source boundary

The review prioritized primary biochemical, structural, receptor-reconstitution,
cellular perturbation, and mouse genetic studies. Stable citations in the TSV
include the Ephrin/Eph receptor studies (PMIDs 8755474, 9484836, 9990854,
10518221, 11182083, 11466320, 11585923, 12383247, 15536074, 18055806,
18300229, 19552627, 19875447, 26687980, and 38627519), Fas/FasL binding and
DISC studies (PMIDs 9126929, 9228058, 11739735, 12556501, and 19641134),
FBLN2/integrin adhesion (PMID 10848816), fibrinogen/alphaIIb-beta3 studies
(PMIDs 6230229, 12008962, 16051597, 16363805, 19778727, and 2722830), and
FGF/FGFR binding and signaling studies (PMIDs 7520751, 7680645, 8663044,
10381577, 11937493, 16384934, 20507176, 20547770, 28813681, and 32801905).

The cited models are mostly developmental, vascular, neuronal, platelet,
hematopoietic, cancer, skeletal, or engineered receptor systems. They support
bounded relay logic and evidence boundaries, not direct transfer of branch
weights to injured spinal-cord receiver states.

## Files written

- `work/module21_relay/module21a_batch175_review.tsv`
- `work/module21_relay/module21a_batch175_summary.md`

