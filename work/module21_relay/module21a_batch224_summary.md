# Module 21A batch 224 review summary

## Scope

Reviewed exactly 25 currently queued Module20A pairs, preserving the supplied
ligand/receptor labels and the exact 13-column Module21A review schema. The
batch covers NRG2-ErbB, neuroligin-neurexin adhesion, neurotrophin-Trk, netrin
receptors, netrin-G synaptic adhesion, neurotensin receptors, neurexophilin-
neurexin binding, and the OSM IL6ST-LIFR receptor complex.

## Disposition

- 13 `reviewed_relay_candidate`
- 4 `reviewed_function_only`
- 6 `reviewed_binding_only`
- 1 `reviewed_scavenging_only`
- 1 `reviewed_unresolved`
- 25 unique review IDs and 25 unique pair labels
- 24 literal `terminal_TF=null` values
- 1 provisional terminal TF: `STAT3` for OSM–IL6ST/LIFR

## Positive relay and receptor-complex evidence

Direct receptor-proximal relays were retained for NRG2 acting through an
ERBB2-ERBB4 kinase-competent complex; NTF3-NTRK2 and NTF3-NTRK3; NTF5-NTRK2;
NTN1-MCAM/CD146; NTN1-NEO1; NTN1-UNC5D; NTN3-NEO1 within the NEO1-CDON/BOC
complex; NTS-NTSR1; NTS-NTSR2; and OSM within the assembled IL6ST/gp130-LIFR
complex. The OSM row preserves STAT3 phosphorylation as the explicit TF
endpoint candidate while documenting that receptor usage and downstream branch
weighting are species- and context-dependent.

## Binding and functional evidence kept separate

NLGN-NRXN rows were kept as function-only or binding-only when the evidence
supported trans-synaptic adhesion and synapse organization without an isolated
cytosolic kinase/adaptor relay. NXPH1/NXPH3 binding to alpha-NRXN LNS2 domains
was recorded as binding-only, with promoter, isoform, and SS2 splice limitations.
NTNG1-LRRC4C and NTNG2-LRRC4 were retained as receptor-complex/synaptic
adhesion edges with functional outputs, not as generic intracellular kinase
pathways. NTS-SORT1 was classified as scavenging-only because sortilin captures
neurotensin and changes NTSR2 availability, but a direct neurotensin-activated
SORT1 cytosolic relay was not isolated.

## Unresolved case and search boundaries

NTN4-DCC remains `reviewed_unresolved`: an early AP-tagged receptor-transfectant
study reported DCC binding, whereas later structure-guided biophysical work
found no direct interaction with DCC or other canonical NTN1 receptors and
supported a laminin-gamma1 extracellular-matrix mechanism. The conflicting
primary evidence was recorded rather than promoted to a direct relay. Searches
covered exact ligand/receptor names and aliases across PubMed, PMC, publisher
pages, Reactome, and structural/biophysical primary studies; family-level
netrin, neurotrophin, neurexin, or receptor evidence was not transferred to
untested exact pairs.

## Validation and protection checks

- Exact 25-row TSV, 13 columns per row, all required fields populated.
- Review IDs and pair labels are unique.
- Confidence values use the existing Module21A vocabulary.
- Terminal TF values are literal `null` except for the explicit OSM/STAT3 row.
- No Module20A ledger, Module21A ledger, frozen manifest, or SQL file was
  modified; no commit was made.
