# Module 21A batch 040 review summary

## Scope

Reviewed exactly the 25 requested priority-8 Module20A queue rows `M20A-CELLCHAT-REMAINING-0355` through `-0380`, excluding the absent numeric `-0370` queue item. Queue membership and canonical pair labels were verified against `module20a_external_review_queue.tsv`.

No Module20A files, the frozen LR manifest, or shared Module21A registers were modified.

## Classification

- Exact rows reviewed: 25
- `reviewed_relay_candidate`: 9
- `reviewed_function_only`: 1
- `reviewed_binding_only`: 1
- `reviewed_unresolved`: 14
- Direct terminal TF assignments: 3 (`STAT3`, `NR3C1`, `NR3C2`)

Promoted receptor-proximal evidence includes the murine Clec2g/Clr-d–Klrb1f/NKR-P1F, Clec2h/Clr-f–Klrb1/Klrb1g/NKR-P1G, Clec2h/Clr-f–Klrb1f/NKR-P1F, Clec2i/Clr-g–Klrb1/Klrb1g/NKR-P1G, and Clec2i/Clr-g–Klrb1f/NKR-P1F pairs. These are kept as C-type lectin-like receptor recognition and receptor-response edges; no terminal TF was inferred from NK-cell reporter, calcium, lysis, or down-modulation assays.

CNTF is retained as a receptor-complex edge: CNTF engages CNTFRα with gp130 and LIFR in defined receptor systems and induces STAT3 phosphorylation. The queued `CNTFR_LIFR` token is treated as a complex shorthand, not as a binary receptor pair; alternative CNTFRα–gp130–OSMR signaling is recorded as a limitation.

CNTN2–CNTN2 is direct homophilic adhesion, while CNTN2–L1CAM is direct heterophilic cis adhesion with neurite-outgrowth/fasciculation output. Neither is treated as a kinase relay or terminal-TF edge.

COL3A1–ADGRG1/GPR56 is promoted as an exact receptor-proximal relay because primary studies identify COL3A1 as the ligand and directly measure GPR56-dependent Gα12/13–RhoA activation and migration effects. In contrast, all six collagen-IV chain rows remain unresolved at chain level: the primary ADGRG6/GPR126 study tested intact type-IV collagen, not isolated COL4A1–COL4A6 chains or defined chain-specific protomers.

Cortisol rows are decomposed explicitly. CYP11B1 is retained as the steroidogenic enzyme context, while direct cortisol activation of NR3C1/GR and NR3C2/MR is recorded as downstream nuclear-receptor transcriptional evidence, with NR3C1 and NR3C2 as the directly activated TF nodes. No direct CYP11B1–nuclear-receptor complex is claimed.

## Search boundaries and limitations

Searches covered exact gene symbols, historical Clr/NKR-P1 aliases, receptor-complex notation, species-resolved orthologs, PubMed, PMC, publisher pages, structural/binding studies, receptor-reporter assays, and adhesion GPCR literature. Primary sources included the mouse/rat NKR-P1F/G–Clr specificity study (PMID 21409442), CNTF receptor-complex signaling studies (PMID 38569939; PMID 20584990), CNTN2/L1 adhesion studies (PMID 1720120; PMID 8978825), COL3A1–GPR56 ligand/signaling studies (PMID 21768377), type-IV collagen–GPR126 studies (PMID 25118328), CYP11B1 steroidogenesis (PMID 25880059), and cortisol–GR/MR receptor studies (PMID 26907965; PMID 38866188; PMID 19541744).

Family-level Clr recognition, human CLEC2D–KLRB1 evidence, intact collagen-IV network evidence, enzyme-to-ligand production relationships, and pathway/database co-membership were not promoted to unsupported exact molecular edges. No terminal TF was inferred from adhesion, reporter, calcium, lysis, or family-level evidence.

## File

- `module21a_batch040_review.tsv`
