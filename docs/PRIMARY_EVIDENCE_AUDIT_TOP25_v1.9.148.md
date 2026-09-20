# Primary-evidence audit of the ranked public-only LR queue

This audit reviews the 25 highest-priority public-only ligand–receptor
candidates emitted by the v1.9.148 public-database comparison. The queue is a
review priority list, not a confidence list. A public-resource match is not
promoted to the mechanism graph unless a primary paper directly supports the
exact ligand–receptor pair in the relevant biological context.

The audit distinguishes:

- `confirmed_primary_functional`: a primary study directly links the exact
  ligand and receptor and reports a receptor-specific functional consequence.
- `confirmed_primary_interaction_noncanonical`: a primary study directly
  demonstrates the molecular interaction and a consequence, but the pair is
  not yet treated as a canonical secreted ligand–receptor signaling route.
- `family_level_primary_not_isoform_exact`: primary evidence supports a family
  or complex, but not the exact component-level pair in the queue.
- `supplied_locator_secondary_or_wrong`: the supplied locator is a review,
  network/database paper, population-genetics paper, or otherwise does not
  establish the exact pair.
- `locator_not_verified`: the supplied locator was not sufficient to verify the
  exact pair during this pass.

No candidate in this audit was added to the graph. The next curation step is
to identify the original primary paper for rows marked secondary, wrong, or
not verified, then re-check species, molecular form, receptor specificity,
and output before promotion.

## Findings

| Candidate | Supplied locator assessment | Primary-evidence result | Supported layer | Decision |
|---|---|---|---|---|
| GRP → NMBR | PMID 25209280 is a primary mouse study; PMID 29133874 is a primary mouse study. | The 2014 study reports that GRP can signal through NMBR, with weaker signaling than through GRPR, and uses receptor genetics, pharmacology, and itch behavior. The 2017 study provides complementary functional neuronal evidence. | L→R→O, with itch transmission as the output; no intracellular/TF route asserted. | Confirmed primary functional lead; still requires context/species normalization before graph promotion. |
| HDC → HRH1 | PMID 10444208 is a review; PMID 35378699 is an axis-focused article, not yet verified here as the original direct HDC–HRH1 study. | The supplied locators do not establish the exact pair as a primary interaction record. | Unknown. | Hold. |
| HDC → HRH2 | PMID 10444208 is a review; PMID 35378699 is not the original direct pair record. | Exact primary HDC–HRH2 evidence was not established from the supplied locators. | Unknown. | Hold. |
| HDC → HRH3 | PMID 10444208 is a review; PMID 35378699 is not the original direct pair record. | Exact primary HDC–HRH3 evidence was not established from the supplied locators. | Unknown. | Hold. |
| HDC → HRH4 | PMID 10444208 is a review; PMID 35378699 is not the original direct pair record. | Exact primary HDC–HRH4 evidence was not established from the supplied locators. | Unknown. | Hold. |
| LRRC4B → PTPRS | PMIDs 23916315 and 29674953 are reviews. | The supplied locators summarize synaptic adhesion biology but do not constitute an exact primary LRRC4B–PTPRS record. | Unknown. | Hold. |
| POMC → OPRD1 | PMID 29934561 is a review; PMID 34724150 is a manually curated opioid signaling network. The mature ligand identity is also ambiguous because POMC is a precursor. | No exact primary POMC-derived peptide–OPRD1 record was verified in this pass. | Unknown. | Hold. |
| POMC → OPRK1 | PMID 29934561 is a review; PMID 34724150 is a signaling-network paper. The mature ligand identity is ambiguous. | No exact primary POMC-derived peptide–OPRK1 record was verified in this pass. | Unknown. | Hold. |
| POMC → OPRM1 | PMID 29934561 is a review; PMID 34724150 is a signaling-network paper. The mature ligand identity is ambiguous. | No exact primary POMC-derived peptide–OPRM1 record was verified in this pass. | Unknown. | Hold. |
| PTN → SDC1 | PMID 25620911 is a review; PMID 28356350 is a review. | The supplied locators do not establish exact primary PTN–SDC1 evidence. | Unknown. | Hold. |
| PTN → SDC2 | PMID 25620911 is a review; PMID 28356350 is a review. | The supplied locators do not establish exact primary PTN–SDC2 evidence. | Unknown. | Hold. |
| PTN → SDC3 | PMID 25620911 is a review; PMID 28356350 is a review. | The supplied locators do not establish exact primary PTN–SDC3 evidence. | Unknown. | Hold. |
| PTN → SDC4 | PMID 25620911 is a review; PMID 28356350 is a review. | The supplied locators do not establish exact primary PTN–SDC4 evidence. | Unknown. | Hold. |
| AGT → AGTR2 | PMID 20606419 is a human genetic-association study, not a direct AGT–AGTR2 interaction study. | The supplied locator is insufficient for the exact LR claim. | Unknown. | Reject supplied evidence; search for the original receptor pharmacology paper. |
| ANGPTL1 → PIRB | PMID 24478758 is a review. A separate primary study (PMID 22660330) directly tests ANGPTL binding to PIRB but the exact ANGPTL1 isoform requires checking in the primary figures/data. | Family-level primary lead only; exact queued pair not verified. | Potential L→R→O through HSC expansion, but not asserted for ANGPTL1. | Hold pending isoform-specific check. |
| ANGPTL2 → TLR4 | PMID 24478758 is a review. | No exact primary ANGPTL2–TLR4 interaction record was verified from the supplied locator. | Unknown. | Hold; do not infer from ANGPTL2–PIRB evidence. |
| ANGPTL4 → SDC1 | PMID 29017031 is a primary study showing ANGPTL4 binds syndecans and forms an ANGPTL4–syndecan–LRP6 complex. The exact SDC1 component was not established here. | Family-level primary support, not exact SDC1 support. | Potential L→R/complex→Wnt output at the syndecan-family level. | Hold exact SDC1 edge. |
| ANGPTL4 → SDC2 | PMID 29017031 is primary family-level evidence; exact SDC2 support was not established here. | Family-level primary support, not exact SDC2 support. | Potential L→R/complex→Wnt output at the syndecan-family level. | Hold exact SDC2 edge. |
| ANGPTL4 → SDC3 | PMID 29017031 is primary family-level evidence; exact SDC3 support was not established here. | Family-level primary support, not exact SDC3 support. | Potential L→R/complex→Wnt output at the syndecan-family level. | Hold exact SDC3 edge. |
| ANGPTL7 → PIRB | PMID 24478758 is a review. A separate primary study (PMID 22660330) is a lead for ANGPTL–PIRB biology, but the exact ANGPTL7 isoform requires checking. | Family-level primary lead only; exact queued pair not verified. | Potential L→R→O through HSC expansion, but not asserted for ANGPTL7. | Hold pending isoform-specific check. |
| APP → CD74 | PMID 19849849 is a primary study showing direct CD74–APP interaction and altered APP trafficking/Aβ production. | Direct primary interaction and output are supported, but this is a cell-associated APP–CD74 interaction rather than a canonical secreted-ligand route. | Interaction→output; not yet classified as canonical L→R signaling. | Retain as a noncanonical evidence lead; role/context review required. |
| BTLA → TNFRSF14 | PMID 21941365 is a lymphoma genetics/prognosis study, not a direct BTLA–TNFRSF14 interaction paper. | Supplied locator is wrong/insufficient. A separate primary-paper lead exists (PMID 19915044), but it was not substituted into the queue in this pass. | Unknown from supplied evidence. | Hold and curate the direct cis/trans interaction paper separately. |
| C3 → CR2 | PMID 16234578 was not verified as the exact primary C3–CR2 paper. | The canonical biology is plausible, but no exact primary locator was established from the supplied citation. | Unknown. | Hold; identify the appropriate C3 fragment/CR2 primary assay. |
| C4B → CR2 | PMID 16234578 was not verified as the exact primary C4B–CR2 paper. | The supplied citation does not establish the exact pair. | Unknown. | Hold; identify the appropriate C4b/CR2 primary assay. |
| CADM3 → CADM1 | PMID 33397712 is a primary genetic/functional study, but its direct conclusion is that CADM3 is the main axonal ligand for CADM4; it does not establish CADM3 as a ligand for CADM1. | Primary study does not support the exact queued pair. | Unknown for CADM3→CADM1. | Hold; do not transpose family-member evidence. |

## Source links checked

- [GRP/NMBR primary study, PMID 25209280](https://pubmed.ncbi.nlm.nih.gov/25209280/)
- [ANGPTL/PIRB primary study, PMID 22660330](https://pubmed.ncbi.nlm.nih.gov/22660330/)
- [ANGPTL4/syndecan/LRP6 primary study, PMID 29017031](https://pubmed.ncbi.nlm.nih.gov/29017031/)
- [APP/CD74 primary study, PMID 19849849](https://pubmed.ncbi.nlm.nih.gov/19849849/)
- [H1-receptor review, PMID 10444208](https://pubmed.ncbi.nlm.nih.gov/10444208/)
- [PTN review, PMID 25620911](https://pubmed.ncbi.nlm.nih.gov/25620911/)
- [Midkine/PTN review, PMID 28356350](https://pubmed.ncbi.nlm.nih.gov/28356350/)
- [SALM/LRFN review, PMID 29674953](https://pubmed.ncbi.nlm.nih.gov/29674953/)
- [Opioid-receptor review, PMID 29934561](https://pubmed.ncbi.nlm.nih.gov/29934561/)
- [Opioid signaling network, PMID 34724150](https://pubmed.ncbi.nlm.nih.gov/34724150/)
- [AGT/AGTR genetics study, PMID 20606419](https://pubmed.ncbi.nlm.nih.gov/20606419/)
- [CADM3/CADM4 primary study, PMID 33397712](https://pubmed.ncbi.nlm.nih.gov/33397712/)

