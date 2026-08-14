# Module 21A to Module 20A node reconciliation audit

Date: 2026-08-14

This is a read-only reconciliation against the frozen Module 20A source-union queue in `module20a_external_review_queue.tsv`. Module 20A rows are used only to confirm ligand/receptor vocabulary and pair-context availability. Their confidence calls are not transferred to Module 21A intracellular or functional edges.

## Reconciled contexts

- Q001 CNTF/gp130: `cntf il6st_lifr` (`M20A-EXT-1200`, low), `cntf cntfr_il6st` (`M20A-EXT-1196`, low), and `osm osmr_il6st` (`M20A-CELLCHAT-REMAINING-1489`, low) are present. These rows do not resolve the exact CNTFRα/gp130/LIFR versus CNTFRα/gp130/OSMR branch in SCI astrocytes.
- Q002 IFN-lambda: an `il10 ifnlr1` row is present (`M20A-EXT-2128`, low), but it is not an exact IFN-lambda/IFNLR1–IL10RB complex row; no Module 21A branch promotion is based on it.
- Q003 TNFR2: `tnf tnfrsf1b` is present (`M20A-LIANA-REMAINING-0239`, low).
- Q005 chemokine bias: CCL17/22–CCR4, CCL19/21–CCR7, and CXCL9/10/11–CXCR3 contexts are present, all low in the frozen queue.
- Q006 TGF/BMP: canonical TGFβ1/TGFBR1–TGFBR2 and BMP4/BMPR1A–BMPR2 contexts are present, with low and medium queue calls respectively.
- Q007 RTKs: FGF10–FGFR2 is present at medium (`M20A-EXT-0086`); PDGFB/PDGFD–PDGFRβ and VEGFA–KDR are present at low. These LR calls do not establish the downstream SCI receiver branches separately recorded in Module 21A.
- Q008 WNT: WNT5A–RYK is present at low and WNT5A–PTK7 at medium. The Module 21A RYK edge remains a functional SCI astrocyte record with a noncanonical-branch limitation.
- Q009 Notch: DLL4–NOTCH1 and JAG1–NOTCH1/2/3/4 contexts are present at low. The Module 21A DLL4–NOTCH1 pathway record is supported by separate primary intracellular/functional evidence and is not promoted to NOTCH2/3/4 equivalence.
- Q010 CSF1/CSF1R: `csf1 csf1r` is present in the frozen source-union queue (`M20A-CELLCHAT-REMAINING-0381`) and in the audited CellChat/ConnectomeDB seed contexts. These Module 20A LR records remain separate from the new focal-SCI CSF1/IFN-beta pathway/function edges; no Module 20A confidence call is copied into Module 21A.

## Unresolved or absent exact contexts

- No exact IL1R2 ligand/receptor row was found in the frozen source-union queue during this audit; the IL1R2 decoy remains a separately documented Module 21A boundary.
- The Module 20A queue contains ligand/receptor contexts, not intracellular kinase, transcriptional, or cellular-function evidence. No Module 20A LR confidence was copied into Module 21A.
- Composite receptor labels remain explicit. A component-level match is not treated as proof of the full receptor complex.

## Pre-SQL implication

All Module 21A relay and functional edges can retain their current source and target node labels for staging, but materialization must preserve the distinction between Module 20A ligand/receptor context and Module 21A intracellular/pathway/function evidence. Module 20A ledgers and the frozen manifest were not modified.
