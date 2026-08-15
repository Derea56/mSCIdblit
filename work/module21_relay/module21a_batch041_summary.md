# Module 21A batch 041 review summary

## Scope

Reviewed exactly the 25 requested frozen Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0382`, `-0383` through `-0388`, and `-0402` through `-0419`. Queue membership was verified against `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`; all 25 IDs were present, unique, and matched the requested canonical labels. No Module20A files, the frozen LR manifest, or shared Module21A registers were modified.

## Classification

- Exact rows reviewed: 25
- `reviewed_relay_candidate`: 4
- `reviewed_binding_only`: 2
- `reviewed_unresolved`: 19
- `reviewed_function_only`: 0
- Direct terminal TF assignments: 1 (`STAT3`, for Ctf1/LIFR_IL6ST)

The strongest exact receptor-proximal relays are CT-1 through the LIFR–gp130 complex to JAK/STAT3 and ERK; cathepsin G through PAR1/F2R in monocyte chemotaxis; cathepsin G through PAR4/F2RL3 in human platelet/fibroblast contexts; and cathepsin G through FPR1 in phagocyte chemotaxis. Cathepsin G also has primary evidence for PAR1, PAR2, and PAR3 cleavage/disarming, which is retained as receptor processing or binding-layer evidence rather than being promoted to productive activation.

The exact `Ctsg Pard3` row is unresolved because PARD3 is a polarity scaffold, while protease-activated receptor 3 is encoded by `F2RL2`; PAR3 evidence was not transferred across this nomenclature mismatch.

The steroid rows are intentionally conservative. Desmosterol, DHEA/DHEAS, DHT, and DOC each have primary evidence for activity at selected nuclear receptors or downstream transcriptional programs, but the queued labels combine the mature steroid with a biosynthetic, sulfotransferase, or steroid-sulfatase enzyme. Those processing enzymes were not treated as receptor subunits or as direct ligand-receptor edges. Accordingly, the composite rows remain unresolved and no AR, LXR, PPAR, PXR, or MR terminal-TF assignments were made for them.

## Search boundaries and limitations

Searches covered exact gene-symbol pairs, historical PAR/FPR aliases, receptor-complex notation, mature steroid names, enzyme names, PubMed, PMC, publisher pages, and primary receptor/transactivation studies. Primary sources included CT-1/gp130/LIFR signaling (PMID 9253712; PMID 15361284), CTSG–PAR1/PAR3/PAR4 studies (PMIDs 19293192, 9058715, 11307827, 10702240, 17142351, 41370205), CTSG–FPR1 (PMID 15210802), desmosterol–LXR studies (PMIDs 23021221, 34782454, 22891291), DHEA/DHEAS receptor studies (PMIDs 23123738, 9449250, 8700121, 18255343), DHT–AR studies (PMIDs 1334007, 12061774, 20560974), and DOC–MR evidence (DOI 10.1210/en.2004-0128).

Pathway or database context was not promoted as pair-specific evidence. Family-level PAR processing, general PXR/PPAR ligand promiscuity, enzyme regulation of sulfotransferases, and mature steroid–nuclear-receptor activation were used only to define boundaries and limitations. No pathway-level or functional evidence was used to infer a direct molecular interaction for an exact enzyme composite.

## Files

- `work/module21_relay/module21a_batch041_review.tsv`
- `work/module21_relay/module21a_batch041_summary.md`
