# Module 21A batch 039 review summary

## Scope

Reviewed exactly the 25 frozen Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0330` through `-0354`. Queue membership and canonical labels were checked against `module20a_external_review_queue.tsv`. This batch covers cholesterol composite labels, Cldn1/Cldn11/Cldn2/Cldn3 homophilic rows, and the requested CLEC2/KLRB1 family rows.

Module20A files, the frozen LR manifest, and shared Module21A registers were not modified.

## Classification

- Exact rows reviewed: 25
- `reviewed_relay_candidate`: 5
- `reviewed_function_only`: 1
- `reviewed_binding_only`: 3
- `reviewed_unresolved`: 16
- Direct terminal TF assignments: 1 (`STAT3`, for the CLCF1/CNTFR receptor-complex relay)

Promoted receptor-complex/pathway evidence is limited to CLCF1/CNTFR-LIFR, human CLEC2D–KLRB1/CD161, murine Clec2d–Klrb1b/NKR-P1B, murine Clec2f–Klrb1f/NKR-P1F, and murine Clec2g–Klrb1/NKR-P1G. CLCF1 evidence is retained as a composite cytokine/receptor-complex edge because the primary studies require CLC/CLCF1 with CRLF1/CLF-1 or soluble CNTFRα for efficient secretion and receptor assembly. The CLEC2/KLRB1 rows preserve species and nomenclature boundaries rather than transferring human KLRB1 evidence to murine Klrb1 family members.

The claudin rows are adhesion/tight-junction edges, not intracellular signaling receptors. Cldn1, Cldn3, and Cldn11 have direct homophilic trans-interaction evidence in reconstituted cell systems; Cldn2 has functional homophilic adhesion evidence from primary hepatocyte/tumor-cell interaction and perturbation studies. No terminal TF was assigned to any claudin row.

The cholesterol rows remain unresolved as exact CellChat composites. Primary studies support cholesterol or hydroxycholesterol interaction with isolated RORα/RORγ ligand-binding domains, but no direct DHCR7–RORC or LIPA–RORA/RORC receptor-complex assay was located. DHCR7 and LIPA were therefore kept as sterol-processing enzyme labels, and the ROR proteins were not promoted as terminal TFs for those composite rows.

## Search boundaries and limitations

Searches covered exact gene symbols, historical aliases, species-resolved orthologs, receptor-complex notation, PubMed, PMC, publisher pages, and primary receptor/functional studies. Primary sources included CLC/CLCF1–CNTFR complex studies (PMID 11285233; PMCID PMC145510), ROR sterol structural/functional studies (PMID 12467577; PMID 20203100), claudin reconstitution and adhesion studies (PMID 18095722; PMID 21533891; PMID 30734065; PMCID PMC3434516), and NKR-P1:Clr binding/reporter studies (PMID 14990792; PMID 16339512; PMID 21409442; PMID 19535641).

For the mouse NKR-P1 system, `Klrb1` is a historically ambiguous/official symbol associated with NKR-P1G, while `Klrb1a`, `Klrb1b`, `Klrb1c`, and `Klrb1f` resolve to NKR-P1A, B/D, C, and F. This nomenclature was recorded as a limitation. Family-level ligand recognition, co-expression, pathway membership, and human CLEC2D–KLRB1 evidence were not transferred to unsupported exact murine pairs. No TF was inferred from a CellChat label or from a pathway database.

## File

- `module21a_batch039_review.tsv`
