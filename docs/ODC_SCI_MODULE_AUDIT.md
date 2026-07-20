# ODC-SCI Module Audit

Access date: 2026-07-17

Source snapshot:

- `data/raw/evidence/odc_sci_audit/odc_sci_public_2026-07-17.html`
- `data/raw/evidence/odc_sci_audit/odc_sci_public_2026-07-17.json`

API note: local configuration contains `ODC_SCI_API_KEY`, but the value currently resolves as a placeholder. Authenticated SciCrunch/ODC API probing was therefore not usable in this pass. This audit uses the public ODC-SCI dataset listing.

## Module Update Calls

| Module | Update Needed? | ODC-SCI Candidates | Rationale |
|---|---|---|---|
| Module 3 | YES | ODC-SCI:1536, 1519, 1413, 1387, 695 | Adds raw-data anchors for LPS/microglia/PNN remodeling, fibroblast/macrophage density, macrophage activation genes, TLR agonist inflammation repair, and microglial interaction maps. |
| Module 5 | YES | ODC-SCI:1612, 1609, 1587, 1410, 1315 | Adds neuromodulation, respiratory motor output, nerve-transfer rehabilitation, and human VNS/perilesional stimulation result anchors. |
| Module 6 | YES | ODC-SCI:1282, 1479, 536, 405, 1096 | Adds TRACK-SCI outcome datasets, surgical blood pressure/motor recovery, acute blood RNA, and ISNCSCI standards anchors. |
| Module 7 | YES | ODC-SCI:1536, 1389, 1387, 688, 578 | Adds host-state/systemic conditioning anchors: LPS, Pam3CSK4/TLR2, TLR2/TLR4, probiotic, and fecal-transplant datasets. |
| Module 8 | YES | ODC-SCI:1597, 595, 1081, 1082, 26 | Adds high-value model-system raw-data anchors for graded contusion, MASCIS-scale severity data, CLIMBER meta-analysis layers, and cervical unilateral multimodal injury. |
| Module 9 | YES | ODC-SCI:1235, 930 | Adds a small but relevant in vitro/ex vivo bridge: pleiotrophin in vitro dose-response and cultured macrophage/spinal-cord-homogenate PI3K inhibition. |
| Module 10 | YES | ODC-SCI:1612, 1410, 1408, 1315, 1282, 1479 | Adds clinical result/cohort links that should be tied back to ClinicalTrials.gov and TRACK-SCI rows. |

## Boundary Notes

- ODC-SCI records are dataset-level evidence, not automatically paper-level evidence.
- Public ODC records can upgrade source confidence because they expose raw or curated datasets, but consensus claims still need model, intervention, timing, endpoint, and population boundaries.
- Module 10 should treat ODC-SCI clinical datasets as results/publication-linkage anchors, not as replacements for registry-status rows.
- Module 8 should treat ODC-SCI model datasets as strong raw-data anchors for model ontology and severity calibration.
