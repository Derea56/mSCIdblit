# Module 21A Batch 146 review summary

Reviewed exactly the 25 specified filtered priority-8 queue rows (queue ordinals 3101–3125) and wrote one row per requested Module 20A review ID using the existing 13-column batch-review schema.

## Outcomes

- 3 reviewed receptor-proximal relay candidates: OMgp–LINGO1, OMgp–NGFR/p75, and PCSK1N/proSAAS-derived BigLEN–GPR171.
- 8 reviewed binding-only records: NTRK3–PTPRS, NXPH2–NRXN1, OMgp–RTN4R/NgR1, P4HB–MTP, PCSK9–LRP1, PCSK9–SORT1, PCSK9–VLDLR, and PD-L2–RGMB.
- 1 reviewed function-only record: PDGFB stimulation cooperating with ITGAV-containing alphaVbeta3 adhesions through PDGFRbeta/Src signaling.
- 13 reviewed unresolved/no-evidence boundaries: NTRK3–PTPRF, NTS–NGFR, NUCB2–ERAP1, OIT1–FPR1/2, OLFM2–ROBO2, OMgp–RTN4RL1/NgR2, OMgp–TNFRSF1B, PAM–DPP4/FAP, PDAP1–PDGFRB, PD-L2–PDCD2, and PDGFB–ART1.

## Layer and identity boundaries

Direct binding/activation, receptor-proximal receptor-complex relay, and downstream pathway/function evidence are kept separate in the TSV. OMgp is directly assigned to NgR1/RTN4R; LINGO1 and NGFR/p75 are retained as receptor-complex relay components without inferring direct OMgp binding to either component. OMgp–RTN4RL1/NgR2 remains unresolved because primary receptor-family comparisons report OMgp binding to NgR1 but not NgR2. The queued OMgp–TNFRSF1B row is not the TROY/TNFRSF19 row, so TROY evidence was retained only as a paralog boundary.

NXPH2–NRXN1 is supported by bovine alpha-neurexin evidence but has a rodent expression caveat. PCSK1N–GPR171 evidence is assigned to the processed proSAAS peptide BigLEN, not intact PCSK1N. P4HB–MTP and PCSK9–SORT1 are intracellular complex/trafficking records rather than canonical ligand-triggered signaling. PD-L2–RGMB binding and context-specific functional outputs do not establish a universal intracellular relay. No terminal TF was assigned.

Only the requested raw TSV and this summary were written. Module 20A ledgers, the frozen manifest, shared Module 21A registers, coverage/reuse tables, and integration outputs were not modified. No commit was created.
