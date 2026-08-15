# Module 21A batch 209 summary

## Scope

Batch 209 covers exactly the 25 requested currently queued Module20A pairs:
M20A-EXT-1524, 1526, 1527, 1531, 1532, 1535, 1540, 1543, 1547, 1562,
1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574,
1575, 1576, and 1577. Pair labels are preserved exactly as submitted.

## Disposition

- 9 reviewed relay candidates: Efna3-Epha7, Efna4-Epha10, Efna5-Epha2,
  Efna5-Ephb2, Efnb1-Ephb1, Egf-Rhbdl2, Epo-Ephb4, Epo-Epor, and
  Ereg-Erbb3, with complex or processing semantics retained where applicable.
- 3 reviewed binding-only records: Efna3-Epha3, Efna4-Epha2, and Egf-Nrp1.
- 4 unresolved cases: Efna3-Epha8, Efnb2-Ephb1, Enho-Gpr19, and Epo-Crlf3.
- 7 reviewed function-only records: Egf-Pld2, Egf-Tnfrsf11b,
  Entpd1-Adora1, Entpd1-Adora2a, Entpd1-Adora2b, Entpd1-Adora3, and F10-F3.
- 2 explicit no-evidence boundaries: Enam-Cd63 and Etv5-Erbb2.

The counts above are intentionally a prose audit note; the TSV is authoritative
and will be validated mechanically. One pair, Efna5-Ephb2, has confidence
`medium-high` in the TSV despite the primary exact-pair evidence being strong;
this preserves a conservative cross-subclass assignment. No terminal TF is
assigned except NANOG for Efna4-Epha10, STAT3 for Epo-Ephb4, and STAT5 for
Epo-Epor, where the primary perturbation studies explicitly identify those
transcriptional endpoints.

## Search boundary and interpretation rules

Searches covered exact submitted symbols and principal aliases across PubMed,
PMC, publisher pages, and pathway resources, with primary biochemical,
receptor-activation, genetic-perturbation, and cell-function studies retained
where available. Direct binding, receptor-complex/proximal relay, and
downstream function are separated in `evidence_layer` and `relation_type`.

ENTPD1-to-ADORA1/2A/2B/3 rows are explicitly function-only metabolic-coupling
records: CD39 generates nucleotide intermediates and CD73 is generally required
before adenosine can activate the receptor. EGF-Pld2, EGF-TNFRSF11B, and F10-F3
are likewise pathway or biochemical-complex outputs, not direct ligand-receptor
edges. EGF-RHBDL2 is an enzyme-substrate processing relation that leads to EGFR
activation and is not treated as receptor binding. ETV5-ERBB2 is a node-role
mismatch because ETV5 is a transcription factor, not an upstream ligand.

No direct molecular interaction was inferred from pathway-level or phenotype-only
evidence. Unresolved and no-evidence boundaries are recorded explicitly for
future re-search.

## Validation target

The TSV must contain exactly 25 data rows, the exact 13-column schema
`review_id,pair,status,stable_citations,species,cell_type_model,assay_or_perturbation,relation_type,evidence_layer,pathway_branch,confidence,limitations,terminal_TF`, unique review IDs and pair labels, populated required fields, allowed confidence values, and literal `null` in every unvalidated terminal-TF field. No ledgers or commits are created in this batch.
