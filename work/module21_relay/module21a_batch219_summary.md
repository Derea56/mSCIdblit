# Module 21A batch 219 review summary

This batch reviews exactly the 25 user-specified queued Module20A pairs, in
the submitted order, using the exact 13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

The search boundary covered exact-symbol and alias queries across PubMed,
PMC/Europe PMC, publisher and structural pages, and pathway/context
comparators. Primary research was prioritized. Existing Module20A ledgers,
the frozen manifest, shared Module21A registers, and integration outputs were
not edited. Only this TSV and summary were written.

## Disposition

- 25 data rows; exact requested IDs and pair labels; 13 columns per row.
- 16 `reviewed_relay_candidate` rows: Ihh–PTCH1/SMO; IL-11–IL11RA1/gp130;
  IL-12; IL-23; IL-13 type-II receptor; IL-15; IL-17A/F; IL-18 (both exact
  label variants); IL-36alpha/beta/gamma; IL-2 high-affinity and intermediate-
  affinity receptor forms; IL-20 type-II receptor; and IL-21.
- 8 `reviewed_binding_only` rows: IGFL3–IGFLR1; Ihh–BOC, CDON, and HHIP;
  isolated IL13RA1; IL-1alpha/IL1R2-IL1RAP; IL-1beta/IL1R2-IL1RAP; and
  IL-36Ra/IL1RL2-IL1RAP.
- 1 `reviewed_function_only` row: IL-16–CD4.
- No unresolved or no-evidence rows were required for this exact canonical
  cytokine/Hedgehog subset.

## Evidence-layer handling

Direct ligand/receptor binding or activation, receptor-proximal relay, and
downstream pathway or cellular function are represented as separate layers in
each row. The incomplete or inhibitory compositions were not promoted to
canonical signaling:

- IGFL3–IGFLR1 is direct recombinant binding without a demonstrated cellular
  relay.
- Ihh–BOC/CDON/HHIP are direct coreceptor or antagonist interactions; only the
  PTCH1/SMO composite carries a receptor-proximal pathway record.
- IL13RA1 alone is retained as a binding/component record, while STAT6 is
  restricted to the complete IL4RA/IL13RA1 complex.
- IL1R2/IL1RAP rows are decoy complexes lacking a productive cytoplasmic TIR
  signaling domain.
- IL-36Ra binds IL1RL2 and prevents IL1RAP recruitment; it is not treated as
  an activating IL-36 relay.
- IL-16–CD4 retains the demonstrated binding and migration output, but no
  intracellular kinase/adaptor sequence is inferred.

The `terminal_TF` column is literal `null` unless the cited primary evidence
directly supports a receptor-linked STAT endpoint. Provisional endpoints are
recorded for IL-11/STAT3, IL-12/STAT4, IL-23/STAT3-STAT4, IL-13/STAT6,
IL-15/STAT5, IL-2/STAT5, IL-20/STAT3, and IL-21/STAT3; these remain separate
Module22A validation candidates and do not alter Module20A classifications.

## Validation

The review packet was checked for exactly 25 data rows, unique review IDs and
pair labels, exact order and label preservation, populated required fields,
allowed confidence vocabulary, literal `null` values where no endpoint was
assigned, and no embedded tabs or extra columns. No SQL or shared-register
materialization was performed.
