# Module 20 / 24B manual source-review report

Date: 2026-08-31
Scope: final read-only review of the explicitly profiled 24B manual candidates using the exact phase-2 rows, evidence/artifact crosswalk, and local source artifacts. The optional 18-row extension was not included. No repository or database files were modified.

## Disposition summary

| Metric | Count |
|---|---:|
| Explicitly profiled 24B manual candidates reviewed | 8 |
| Verified source-unit records passing both gates | 3 |
| Overlay rows emitted | 3 |
| Explicit manual candidates excluded | 5 |
| Optional additional high-yield candidates reviewed for final overlay | 0 |

Both gates were applied independently: (1) stable exact paper anchor, local full-text-like artifact, and exact atomic source locus; and (2) support for the exact registered edge at the existing evidence layer. Abstract-only, metadata-only, contextual-only, and non-exact records were excluded. Existing evidence grade and L0-L4/context framing were preserved; no contextual or functional record was converted into a TF-target claim.

The final overlay contains exactly three rows. The protected fields `extraction_id`, `module`, `b_edge_id`, `b_evidence_id`, `evidence_layer`, and `canonical_paper_key` were checked against the integrated phase-2 TSV for each row.

## Candidate dispositions

| Candidate | Disposition and verification |
|---|---|
| M24B-EVID-000006 / PMID32964315 | PASS. Local RvD3 SCI full-text PDF reviewed. Female C57BL/6 T10 20-g compression SCI, intrathecal RvD3 at 1 h, comparator cell assays, Figs. 1-7, cytokine/barrier/glial/functional readouts support the registered RvD3 downstream/function edge. Existing High grade/context preserved; receptor identity unresolved and no TF inference. Emitted `M24B-P2-R-000006`. |
| M24B-EVID-000008 / PMID15258577 | EXCLUDE. Exact local material is PubMed/XML abstract-only for the P2X7/ATP SCI record. PMC2718350 is a distinct EVID-000009 record and was not borrowed. |
| M24B-EVID-000018 / PMID30622226 | EXCLUDE. Exact local material is PubMed/XML abstract-only for the P2X4/DHCB SCI record; no exact figure-level full text was available. |
| M24B-EVID-000019 / PMID12111830 | EXCLUDE. Exact local material is PubMed/XML abstract-only for the CCR2 SCI record; no exact figure-level full text was available. |
| M24B-EVID-000054 | PASS. The exact phase-2/register identity is APC/PAR1, PMCID:PMC5266300 / PMID28122028, despite recovery prose mentioning PMID25921821 elsewhere. Local PMC full text reviewed through Methods, Results, Figs. 2-5, and Discussion. Adult WT/PAR1-null contusive SCI plus recombinant APC treatment supports the registered APC/PAR1 functional edge. No purified binding or TF claim. Emitted `M24B-P2-R-RECOVERY-APC-PAR1-SCI-000001`. |
| M24B-EVID-000078 / SCI NK1 component | PASS, bounded. Local PMCID:PMC2685299 full text (PMID18945947) supports increased SP after rat SCI and NK1-antagonist-sensitive bladder reflexes by Figs. 2, 3, 5-7. PMID25921821 remains abstract-only; its ERK/p38 progenitor result was not transferred. Emitted `M24B-P2-R-000078` with exact protected identity unchanged and claim bounded to the SCI bladder-reflex branch. |
| PTF-MODULE-24B-000001 / ADA2-CECR1 -> ANXA2 | EXCLUDE. Co-occurrence/WGCNA-type evidence only; no exact TF-locus occupancy or perturbation-supported TF-target claim and no local full-text artifact. |
| PTF-MODULE-24B-000011 / F10-factor Xa -> CCN1 | EXCLUDE. Factor Xa/PAR1-associated CCN1 RNA induction is not TF locus occupancy or a TF perturbation; no local full-text artifact for the exact public-TF record. |
| PTF-MODULE-24B-000013 / FLII -> Ccn1 | EXCLUDE. TFLink/TRRUST source-table record only, with no independent local artifact, exact assay/perturbation, or exact source locus supporting the registered claim. |

### Identity correction recorded during review

The recovery-review prose associates EVID-000054 with PMID25921821, but the exact phase-2 row, evidence register, and artifact crosswalk associate EVID-000054 with APC/PAR1, PMCID:PMC5266300, PMID28122028. The overlay follows the exact phase-2/register identity and does not merge the records.

## Output validation

- Schema: exact 25 fields from `module20_24_integrated_phase2_extractions.tsv`.
- Rows: 3 unique extraction IDs; all `module=24B`; all observation and claim actions are exact CREATE pairs.
- Protected identity: all six protected fields match the integrated phase-2 rows exactly.
- Local artifacts: 4 unique local artifact paths named in emitted rows; all exist at review time.
- Artifact crosswalk: 4 emitted artifact paths matched the local artifact manifest; 0 were not keyed by the manifest.
- Repository/DB: read-only; no repository or database files modified.
