# Cross-module path linkage batch 01: gp130-family cytokines

This batch links existing Module 20B ligand–receptor candidates to Module 21B
receptor-proximal relays and Module 22B terminal TF/program records. It is an
audit-layer linkage table, not a canonical SignalingEdge materialization.

## Batch result

- 8 linkage records were added.
- 2 are candidate cross-module paths with a STAT3 terminal program/target.
- 2 are candidate functional-output paths without a terminal TF assignment.
- 1 is a STAT5B relay candidate with no matched terminal target.
- 2 are CNTF receptor-complex candidates where the 20B LR layer remains boundary-only.
- 1 IL6 receptor-complex record remains unresolved at the exact STAT3 relay step.
- No Module 20A LR classification or frozen manifest was changed.

## Supplemental primary-literature search

The focused search added five supplemental evidence records for triage. These
are not yet promoted into the Module 21A or 22A registers:

- IL-6/JAK2/STAT3 signaling was perturbation-linked to glial activation after
  SCI (PMID 37863306), and IL-6R blockade reduced astrogliosis and improved
  recovery after experimental SCI (PMID 15048924).
- OSM-induced Wnt16 expression in primary mouse osteoblasts required OSMR,
  gp130, SHC1 and STAT3, with ERK independence (PMID 34566421).
- CNTF-associated astrocyte differentiation required STAT3 but not STAT1 in
  developmental/progenitor models (PMID 24466267).
- Reconstituted LIFR-gp130 and OSMR-gp130 complexes activated STAT1, STAT3 and
  STAT5B in comparator systems (PMID 9182534).

These records strengthen the candidate paths but do not erase model, species,
or receiver-cell limitations. The external evidence register and path links
are stored separately so they can undergo normal evidence-ID, citation, and
module-register intake review.

## Interpretation rules

The records preserve the three evidence layers:

1. ligand–receptor binding or activation;
2. receptor-proximal relay/pathway;
3. downstream pathway, TF, or cellular function.

The linkage status is deliberately stricter than “all three labels appear.” A
shared gp130-family receptor or STAT3 label does not establish a ligand-specific
path unless the source record supports that step. Boundary-only 20B records
remain visible but cannot support canonical traversal.

## Highest-value follow-up

The next search should target exact, context-matched terminal outputs for:

- IL6→IL6R-gp130→STAT3 in neural or spinal receiver cells;
- OSM→OSMR-gp130→STAT5B terminal targets;
- CNTF→CNTFRa-gp130-LIFR/OSMR→STAT3 terminal targets in injured astrocytes;
- LIF/OSM gp130-family STAT3 target regulation where receptor and ligand are
  experimentally separated.

Full record-level details are in
`module20_24_path_linkage_batch01_gp130_stat3.tsv`.

Supplemental records are in
`module20_24_path_linkage_batch01_external_evidence.tsv`, with path mappings in
`module20_24_path_linkage_batch01_external_evidence_links.tsv`.
