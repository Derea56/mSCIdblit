# Module 21A Batch 195 review summary

Batch 195 reviews exactly the 25 supplied Module20A CellChat-remaining pairs
and uses the exact 13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

## Disposition

| status | count |
|---|---:|
| `reviewed_relay_candidate` | 22 |
| `reviewed_binding_only` | 3 |
| **total** | **25** |

Confidence counts: high 6; medium-high 14; medium 5. Twelve rows carry
provisional terminal-TF candidates (`STAT1;STAT3;STAT5`, `STAT3`, `STAT5`, or
`SMAD2;SMAD3`); all other rows use the literal `null`.

## Evidence decisions

- Canonical cytokine receptor-complex relays were retained for IL-22,
  IL-24, IL-3, IL-33, IL-34, IL-36alpha/beta/gamma, IL-5, and IL-6. The
  relevant layers remain separated: ligand/receptor binding or activation,
  receptor-proximal JAK/TIR/kinase relay, and downstream pathway or cellular
  function.
- Activin A and activin B rows are receptor-complex claims, not isolated type-I
  receptor binary-binding claims. ACVR2A/ACVR2B binding, type-I recruitment,
  SMAD2/3 or context-dependent SMAD1/5/8 outputs, and receptor/cofactor
  dependence are kept explicit. Inhibin A/B rows remain binding-only because
  the strongest evidence requires the TGFBR3/betaglycan complex and does not
  establish an autonomous ACVR2A/B intracellular relay for the submitted rows.
- `Klk1b4` is retained as the mouse alpha-NGF/Ngfa nomenclature mapping and
  reviewed against primary NGFR/p75NTR and NTRK1/TrkA studies. The alias,
  receptor co-expression, proNGF processing, and neuronal model boundaries
  are recorded rather than silently normalized to a generic NGF edge.
- LGALS9-HAVCR2/TIM-3 is direct binding plus immune function, but no single
  intracellular TIM-3 relay was isolated. NRXN1/2-ADGRL1 is direct,
  splice-sensitive transsynaptic adhesion; it is not promoted to a GPCR
  pathway or TF endpoint.

## Search boundary and validation

Searches covered exact ligand/receptor and receptor-complex names across
PubMed, PMC, and publisher records, with primary structural, biochemical,
reconstitution, perturbation, and cellular-function studies retained where
available. Reviews and pathway-family records were used only to orient the
search or reconcile aliases. Generic cytokine-family, receptor-family,
expression-only, and phenotype-only results were not used to infer an exact
direct molecular edge.

Before handoff, this packet must pass: 25 data rows; unique IDs and pair
labels; exact alignment to the supplied IDs; exact 13-column schema; populated
required fields; valid confidence vocabulary; and `terminal_TF` either a
directly supported candidate or literal `null`. Only this TSV and summary are
written by Batch 195; shared Module20A/21A ledgers and the frozen manifest are
untouched.
