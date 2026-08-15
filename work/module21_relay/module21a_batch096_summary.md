# Module 21A batch 096 review summary

## Scope

- Reviewed exact filtered priority-8 queue ordinals 1701–1725 from `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`.
- The requested slice contains 25 exact rows with intentional review-ID gaps: M20A-EXT-0750 through M20A-EXT-0805 as listed by the filtered queue, not a contiguous ID interval.
- Output is isolated in `module21a_batch096_review.tsv`; shared Module 21A registers, Module 20A ledgers, frozen manifest, and integration outputs were not modified.

## Disposition

- 25 exact rows reviewed.
- 5 `reviewed_function_only`: AGT–AGTR1A, AGT–AGTR2, AGT–ENPEP, AGT–MAS1, and AMH–EGFR. These retain mature-peptide processing or functional modulation evidence without converting precursor or cross-talk biology into direct ligand-receptor activation.
- 3 `reviewed_binding_only`: AGT–LRP2/megalin, ANXA1–DYSF, and ANXA1–EGFR. These are direct endocytic or intracellular associations, not canonical secreted-ligand activation edges.
- 1 `reviewed_relay_candidate`: AGRP–SDC3 as a syndecan-3/heparan-sulfate co-receptor facilitation of AgRP action at MC4R; the co-receptor/pathway node remains explicit.
- 16 `reviewed_unresolved`.
- 0 terminal TF assignments.

## Promoted evidence

1. **AGRP–SDC3:** AgRP binds heparan sulfate and syndecan-3 co-expression potentiates AgRP inhibition of MC4R signaling in recombinant systems; the edge is retained as a receptor-complex/co-receptor relay, not as an unsupported standalone SDC3 direct-binding claim. Primary support: PMID 12851299; PMCID PMC5418061.
2. **AGT precursor boundaries:** AGT is processed into active angiotensin peptides. Ang II supports AGTR1A/AGTR2 branches, Ang-(1-7) supports MAS1, ENPEP processes RAS peptides, and LRP2/megalin directly binds and endocytoses AGT in renal proximal-tubule models. Primary support: PMID 17881465; PMID 17990103; PMID 20966072; PMID 28082260; PMID 22461301.
3. **AMH–EGFR:** historical MIS/AMH work measured inhibition of EGFR autophosphorylation and epithelial growth, so the row is function-only. Canonical AMH receptor-complex signaling remains AMHR2/type-I receptor to BMP-SMAD, not direct EGFR ligand binding. Primary support: PMID 3030847; comparator: PMCID PMC9201060.
4. **ANXA1–DYSF and ANXA1–EGFR:** direct intracellular/membrane associations are supported by co-immunoprecipitation, imaging, competition, and trafficking assays. These are recorded as binding-only because they do not establish secreted ANXA1 activation of EGFR or a downstream receptor relay. Primary support: PMID 14506282; PMID 40470752; PMCID PMC4906250.

## Unresolved and no-evidence boundaries

- AGT–ADRA2A, AGT–GRM7, and AGT–MTNR1A had no exact mature-AGT or processed-angiotensin activation assay. Angiotensinogen precursor biology and receptor-family annotations were not transferred.
- AIMP1–NTRK1 remains unresolved because the primary receptor-identification study supports CD23 with ERK1/2 and TNF-alpha outputs, not NTRK1: PMID 22767513.
- AMH–GREM2 remains unresolved; shared TGF-beta/BMP biology or functional antagonism does not demonstrate direct AMH-GREM2 binding: PMCID PMC4043579.
- ANGPTL1–PIRB, ANGPTL1–TEK, ANGPTL2–TIE1, ANGPTL4–TIE1, and ANGPTL7–PIRB were kept unresolved. Canonical ANG1/ANG2–TIE1/TIE2 evidence and ANGPTL-family/PirB annotations were not reassigned across paralogs. ANGPTL1 studies point to integrin alpha1beta1 signaling; ANGPTL7 HSPC work did not establish LILRB2/PirB as its receptor: PMID 8980224; DOI 10.1172/JCI64044; PMCID PMC4420207; PMID 27941161.
- ANGPTL4–SDC1/2/3 remains unresolved because heparan-sulfate association and syndecan expression/neutralization do not resolve the syndecan core protein as the exact direct receptor: PMID 29017031; PMCID PMC7746371.
- ANXA1–ADRA2A, ANXA1–GRM7, and ANXA1–MTNR1A remain unresolved. Established ANXA1-FPR2/ALX signaling and unrelated GPCR subtype pharmacology were not used to infer these exact edges.

## Validation

- Header matches the requested 13-column schema.
- 25 rows; all rows have 13 fields and required fields populated.
- Review IDs are unique and exactly match filtered priority-8 ordinals 1701–1725.
- Pair keys and canonical pair labels exactly match the queue slice.
- Stable citations are present for every row; the one explicit PubMed search URL is retained only for the documented no-evidence ANXA1–MTNR1A boundary.
- No terminal TF was assigned without exact downstream evidence.
- Frozen Module20A LR manifest SHA256 before/after review: `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Search boundary

Searches covered PubMed, PMC, publisher pages, and the existing Module 20A evidence-search packets. Primary studies were prioritized for receptor pharmacology, substrate processing, endocytosis, co-receptor facilitation, intracellular association, and perturbation. Pathway-level or functional-output evidence was not used to infer a direct extracellular molecular interaction. Canonical ANG–TIE, ANXA1–FPR, AMH–AMHR2, and AIMP1–CD23 evidence was retained as a boundary comparator where the exact queued pair lacked support.
