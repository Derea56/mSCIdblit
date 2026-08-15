# Module 21A batch 117 review

Batch 117 covers the 25 exact requested rows `M20A-EXT-1533` through `M20A-EXT-1561`, excluding the explicitly absent queue IDs `M20A-EXT-1535`, `M20A-EXT-1540`, `M20A-EXT-1543`, `M20A-EXT-1547`, and `M20A-EXT-1562+`.

## Disposition

- 6 `reviewed_relay_candidate`: EFNA5–EPHA3, EFNA5–EPHA7, EFNB2–PECAM1/CD31, EFNB3–EPHB6, EFNB3–RHBDL2, and EGF-to-AXL EGFR-dependent transactivation.
- 1 `reviewed_binding_only`: EFNA5–EPHA6.
- 5 `reviewed_function_only`: EFNA5–EPHA10 isoform/EFNA5-associated beta-catenin remodeling, EFNB2–GRM1, EFNB2–GRM5, EGF–CAV1, and EGF–FSHR crosstalk.
- 13 `reviewed_unresolved`: exact-pair searches did not recover sufficiently specific evidence for EFNA5–EPHA1, EFNA5–EPHB1, EFNA5–EPHB6, EFNB1–EPHA6, EFNB1–ERBB2, EFNB2–EPHA3, EFNB2–EPHA6, EFNB2–RHBDL2, EGF–ADRB2, EGF–ERBB3, EGF–ERBB4, EGF–LDLR, or EGF–LRP2.
- No terminal transcription factors were assigned. Eph/ephrin, ErbB, AXL, CAV1, FSHR, glutamate-receptor and proteolytic outputs were retained at their supported molecular, receptor-proximal, or functional layer.

## Evidence notes

- EFNA5–EPHA3 is supported by a human EphA3/ephrin-A5 co-complex structure and independent ephrin-A5 mutational evidence for high-affinity EphA3 signaling-complex assembly.
- EFNA5–EPHA7 has cellular co-immunoprecipitation, ligand-competition and EphA7 phosphorylation evidence. EFNA5–EPHA6 is retained as binding-only because the bounded search recovered receptor-family binding evidence without a validated exact downstream relay.
- EFNB2–GRM1/GRM5 is deliberately functional-only. Co-immunoprecipitation in rat brain was observed, but FRET/coclustering excluded a direct ephrin-B2/mGlu physical interaction in HEK293 cells; the authors interpret the association as adaptor/scaffold mediated.
- EFNB2–PECAM1/CD31 is a receptor-complex/proximal endothelial association: EphB4-Fc activation redistributed ephrin-B2 to junctions where it colocalized and co-immunoprecipitated with CD31. This is not a soluble ligand-binding claim.
- EFNB3–EPHB6 is supported in primary mouse Schwann-cell assays by clustered ephrin-B3 binding, Eph receptor phosphorylation and ephrin-B3 blockade. EFNB3–RHBDL2 is a distinct direct substrate-processing edge established by co-expression cleavage assays; its physiological downstream consequence remains incompletely resolved.
- EGF–AXL is an EGFR-dependent transactivation relay, not direct EGF–AXL binding. EGF–CAV1 and EGF–FSHR are functional crosstalk/response edges, not direct ligand-receptor edges. The EGF–ErbB3/ErbB4 records preserve receptor-combination specificity boundaries and do not transfer ErbB2-containing heterocomplex behavior to isolated receptors.

## Search boundary and controls

Searches covered exact gene/protein pair queries and family-comparator queries across PubMed, PMC, publisher pages, structural resources and pathway/interaction databases, with primary research prioritized. Stable PMIDs, PMCID records, DOIs and search URLs are retained in each row. Family-level Eph/ephrin promiscuity, co-expression, receptor-complex membership, shared RHBDL2 substrate screens, EGF-like repeats in LRP2, and reverse-direction GPCR-to-EGFR transactivation were not converted into direct exact-pair interactions. Direct molecular, receptor-proximal, and functional evidence remain separated.

## Validation

- Exactly 25 data rows and 13 tab-delimited columns.
- Review IDs and pair labels match the requested exact batch.
- Fields contain no embedded tabs or newlines.
- Only `module21a_batch117_review.tsv` and `module21a_batch117_summary.md` were written by this batch; shared Module 21A registers, Module 20A ledgers, frozen manifest, and integration outputs were not modified.
