# Module 21A batch 216 review summary

Batch 216 reviews exactly the 25 user-specified queued Module20A pairs from
`M20A-EXT-1783` through `M20A-EXT-1938`, preserving the submitted ligand and
receptor-complex labels. The review TSV is the authoritative row-level
artifact. No Module20A ledger, Module21A ledger, frozen manifest, SQL table,
or commit was modified.

## Disposition

- 13 `reviewed_relay_candidate`
- 8 `reviewed_unresolved`
- 1 `reviewed_binding_only`
- 1 `reviewed_function_only`
- 1 `reviewed_scavenging_only`
- 1 `no_evidence_boundary`

The relay candidates include GDF5 BMPR1A/BMPR1B complexes with ACVR2A or
ACVR2B, the GDF6-BMPR1A/ACVR2A branch, GDF9-BMPR2/TGFBR1, GDNF-GFRalpha2-RET,
GH-GHR, GH-PRLR, GHRH-GHRHR, ghrelin-GHSR, GIP-GIPR, and GnRH-GNRHR. The
GDF6/GDF7 receptor-complex rows that lack exact receptor-subunit or ternary
assays remain unresolved rather than being promoted from family-level BMP/GDF
evidence.

GPC3-CD81 is retained as a binding-plus-functional growth-regulation record,
not a kinase relay. GPC3-LRP1 is retained as receptor-mediated endocytosis of
the GPC3-Hedgehog complex, not intracellular LRP1 signaling. GPC3-UNC5C is
retained as extracellular Unc5-family recognition/binding evidence because the
published structural and functional work is centered on Unc5-family context
and does not isolate a unique UNC5C intracellular branch. GNB3-TGFBR1 is an
explicit no-evidence boundary because GNB3 is an intracellular G-protein
subunit and no exact ligand/receptor relationship was recovered.

## Terminal-TF handling

`STAT5` is retained for GH-GHR because the primary receptor-triggering study
directly measured JAK2 and STAT5 activation. `CREB` is retained for GIP-GIPR
because GIP-dependent CREB phosphorylation, CREB/TORC2 promoter occupancy, and
CREB knockdown effects were directly measured. `HHEX` is retained for
GPC3-CD81 because the primary liver study directly linked GPC3-CD81 binding to
HHEX availability and nuclear localization. All other rows use literal
`null`; generic SMAD, ERK, calcium, growth, migration, secretion, or pathway
outputs were not converted into terminal-TF assignments.

## Search boundaries and limitations

Searches covered exact ligand/receptor-complex names and aliases across
PubMed, PMC, publisher pages, Europe PMC, and pathway-resource leads. Primary
anchors were retained for the GDF/BMP receptor-complex rows, GDF9 BMPR2/ALK5,
GDNF GFRalpha2/RET, lactogenic receptor cross-reactivity, GHRH/GHSR/GIP/GnRH
GPCR signaling, and GPC3-CD81/LRP1/Unc5-family mechanisms. Family-level BMP/GDF
receptor compatibility, canonical GDNF-GFRalpha1 biology, and Unc5D-centered
structure/function evidence were not silently reassigned to untested exact
composites. Binding, receptor-proximal relay, downstream pathway, endocytic,
and functional-output evidence remain separated in the TSV.

## Validation

- 25 data rows in the requested order and with the requested exact labels
- 25 unique review IDs and 25 unique pair labels
- Exact 13-column schema:
  `review_id,pair,status,stable_citations,species,cell_type_model,assay_or_perturbation,relation_type,evidence_layer,pathway_branch,confidence,limitations,terminal_TF`
- All required fields populated
- Confidence values restricted to the established vocabulary
- `terminal_TF` is literal `null` except for the three explicit endpoint records
- No evidence was used to alter Module20A LR classifications
