# Module 21A all-pair relay backbone

Generated from the frozen Module 20A external review queue on 2026-08-14.

## Purpose

This backbone expands Module 21A from the bounded family seed to the complete
5,906-pair Module 20A source-backed LR universe. It does not infer signaling
from ligand-receptor evidence. Every pair remains represented individually so
that ligand-specific context, receptor-complex identity, species, cell model,
and terminal TF outcome can be linked without duplicating shared pathway
records.

## Deduplication rule

`module21a_pathway_reuse_registry.tsv` stores each validated relay branch once.
The pair-level coverage table points to one or more reusable pathway keys. A
pathway may be reused only when receptor complex, branch, species, cell/model,
assay, and evidence scope match. Reuse does not merge ligand-specific outcomes.

`module21a_all_pair_relay_coverage.tsv` preserves the individual:

`Module20A ligand-receptor pair -> reusable Module21A relay -> Module22A TF handoff`

relationship.

## Module 22A boundary

`module22a_ligand_tf_handoff.tsv` is the pair-specific handoff inventory. TF
activation evidence and TF-to-target-program/phenotype evidence belong in
Module 22A. A terminal TF must not be assigned from pathway membership alone;
it requires a separately validated signaling or perturbation source.

## Current state

- 5,906 pair-level coverage rows
- 1,893 reusable pathway groups currently indexed: 93 seed, 30 batch001 candidates, 46 batch002-005 candidates, 81 batch006-010 candidates, 17 batch011 candidates, 15 batches012-013 candidates, 1 batches014-015 candidate, 2 batches020-021 candidates, 1 batch022 candidate, 3 batches026-027 candidates, 35 batches028-029 candidates, 50 batches030-031 candidates, 84 batches032-035 candidates, 36 batches036-039 candidates, 14 batches040-041 candidates, 66 batches042-045 candidates, 44 batches046-047 candidates, 44 batches048-049 candidates, 42 batches050-051 candidates, 39 batches052-053 candidates, 41 batches054-055 candidates, 46 batches056-057 candidates, 46 batches058-059 candidates, 46 batches060-061 candidates, 46 batches062-063 candidates, 46 batches064-065 candidates, 46 batches066-067 candidates, 46 batches068-069 candidates, 22 batch070 candidates, 2 batch073 candidates, 25 batch074 candidates, 16 batch075 candidates, 13 batch076 candidates, 20 batch077 candidates, 12 batch078 candidates, 25 batch079 candidates, 12 batch080 candidates, 1 batch081 candidate, 2 batch082 candidates, 18 batch085 candidates, 32 batches086-087 candidates, 16 batch088 candidates, 7 batch089 candidates, 8 batch090 candidates, 13 batch091 candidates, 14 batch092 candidates, 15 batch093 candidates, 4 batch094 candidates, 1 batch096 candidate, 2 batch097 candidates, 7 batch098 candidates, 7 batch099 candidates, 6 batch100 candidates, 6 batch101 candidates, 7 batch102 candidates, 6 batch103 candidates, 6 batch104 candidates, 3 batch105 candidates, 1 batch106 candidate, 6 batch107 candidates, 10 batch108 candidates, 10 batch109 candidates, 5 batch110 candidates, 3 batch111 candidates, 4 batch112 candidates, 2 batch113 candidates, 7 batch114 candidates, 6 batch115 candidates, 17 batches116-117 candidates, 20 batches118-119 candidates, 6 batches120-121 candidates, 13 batches122-123 candidates, 24 batches124-125 candidates, 12 batches126-127 candidates, 24 batches128-129 candidates, 18 batches130-131 candidates, 20 batches132-133 candidates, 14 batches134-135 candidates, 10 batches136-137 candidates, 16 batches138-139 candidates, 17 batches140-141 candidates, 32 batches142-143 candidates, 9 batches144-145 candidates, 46 batches146-151 candidates, 22 batches152-155 candidates, 22 batches156-158 candidates, 31 batches159-161 candidates, and 5 batches162-163 candidates
- 5,906 Module 22A handoff rows
- 4,051 exact pairs reviewed; 1,855 remain queued
- Batch006-010 added 81 reusable relay/function candidates and 44 explicit binding-only or unresolved cases
- Batch011 added 17 reusable relay/function candidates, 3 explicit unresolved cases, and 1 binding-only case; no terminal TF activation candidates were added
- Batches012-013 added 15 reusable relay/function candidates, 6 binding-only or unresolved cases, and 1 no-downstream-evidence case; one directly measured ELK1 activation candidate was handed to Module22A
- Batches014-015 added 1 reusable functional candidate, 9 binding-only cases, and 40 unresolved chain-resolution cases; no terminal TF activation candidates were added
- Batches016-017 added 11 binding-only native collagen-family cases and 39 unresolved exact chain-receptor cases; no relay, functional-output, or terminal TF candidates were added
- Batches018-019 added 6 binding-only collagen-IX material cases and 44 unresolved exact chain-receptor cases; no relay, functional-output, or terminal TF candidates were added
- Batch020 added 1 LAMA2–α3β1 receptor-proximal relay candidate, 1 laminin-1/β8-family binding-only boundary, and 23 unresolved exact chain/complex cases; no terminal TF activation candidates were added
- Batch021 added 1 LAMC3-containing laminin–DAG1 receptor-complex/pathway candidate and 24 unresolved exact chain/complex cases; no terminal TF activation candidates were added
- Batch022 added 1 tenascin-N/W–α9β1 relay candidate with unresolved exact ligand assignment and 11 unresolved tenascin receptor cases; no terminal TF activation candidates were added
- Batch023 retained 11 unresolved TNRC/TNXB exact receptor cases; comparator TNX adhesion/signaling evidence was not transferred and no relay or terminal TF candidates were added
- Batches024-025 reviewed 50 priority-7 collagen/laminin/SV2/DSP rows; batch024 retained 25 unresolved cases and batch025 retained 8 binding-only plus 17 unresolved cases, with no relay or terminal TF candidates added
- Batches026-027 reviewed the final 29 priority-7 rows; batch026 retained 3 function-only, 4 binding-only, and 8 unresolved cases, while batch027 retained 14 unresolved cases; no receptor-proximal relay or terminal TF candidates were added
- Batch028 reviewed 25 priority-8 metabolite/serotonin rows: 8 receptor-relay, 2 functional-output, and 15 unresolved cases; no terminal TF activation candidates were added
- Batch029 reviewed 25 priority-8 serotonin receptor rows; all 25 were receptor-relay candidates covering Gi/o, Gq/11, Gs, or HTR3 cation-channel branches, with no terminal TF activation candidates added
- Batches030-031 reviewed 50 additional priority-8 serotonin receptor rows; all 50 were receptor-proximal relay candidates, with upstream TPH2/VMAT/SERT processing kept separate and no terminal TF activation candidates added
- Batches032-035 reviewed 100 priority-8 acetylcholine, adenosine, adrenergic, activin, steroid, annexin, and apolipoprotein rows; 84 reusable relay/function candidates, 1 binding-only case, and 15 unresolved cases were retained. Three directly supported TF handoffs (NR3C2, SMAD1/5/8, AR) were routed to Module22A; receptor-subtype-unresolved Activin SMAD2 observations were not assigned as exact TF handoffs
- Batches036-039 reviewed 100 priority-8 opioid, calcitonin, immune, adhesion, CEACAM, claudin, CLCF1, and KLRB1-related rows; 36 reusable relay/function candidates, 14 binding-only cases, and 50 unresolved cases were retained. Direct TF handoffs were retained only for matched receptor-complex evidence (ATF2, RORA, RORC, STAT3)
- Batches040-041 reviewed 50 priority-8 CLEC/KLRB1, CNTF/CLCF1, collagen/GPR126, protease/PAR, steroid, and FPR rows; 14 reusable relay/function candidates, 3 binding/disarming cases, and 33 unresolved cases were retained. Direct TF handoffs were retained for matched STAT3, NR3C1, and NR3C2 receptor-complex evidence
- Batches042-045 reviewed 100 priority-8 dopamine, desmosomal, estrogen, FLRT, GABA, and GABA-complex rows; 66 reusable relay/function candidates, 21 binding-only cases, 5 function-only cases, and 8 unresolved cases were retained. Direct TF handoffs were retained for matched ESR1, ESR2, and CREB receptor-relay evidence
- Batches046-047 reviewed 50 additional priority-8 GABA receptor-complex rows; 44 reusable receptor-proximal relay candidates, 3 binding-only cases, and 3 unresolved cases were retained. No terminal TF assignments were made
- Batches048-049 reviewed 50 additional GABA receptor-complex rows; 44 reusable GABA-A relay candidates, 3 GABA-B binding-only cases, and 3 standalone GABA-B unresolved cases were retained. No terminal TF assignments were made
- Batches050-051 reviewed 50 additional GABA receptor-complex rows; 42 reusable GABA-A relay candidates, 2 GABA-B binding-only cases, and 6 unresolved cases were retained. No terminal TF assignments were made
- Batches052-053 reviewed 50 priority-8 GABA, glucagon, and connexin rows; 39 reusable relay/function candidates, 2 binding-only cases, 2 function-only cases, and 9 unresolved cases were retained. No terminal TF assignments were made
- Batches054-055 reviewed 50 priority-8 connexin and glutamate receptor-complex rows; 41 reusable relay/function candidates, 6 function-only cases, and 2 unresolved kainate cases were retained. No terminal TF assignments were made
- Batches056-057 reviewed 50 additional priority-8 glutamate receptor-complex rows; 46 reusable ionotropic/metabotropic relay candidates and 4 unresolved GluK3/GluK4–GluK5 boundaries were retained. No terminal TF assignments were made
- Batches058-059 reviewed 50 priority-8 glutamate receptor-complex rows; 46 reusable ionotropic/metabotropic relay candidates and 4 unresolved kainate boundaries were retained. No terminal TF assignments were made
- Batches060-061 reviewed 50 priority-8 glutamate receptor-complex rows; 46 reusable ionotropic/metabotropic relay candidates and 4 unresolved GluK3/GluK4–GluK5 boundaries were retained. No terminal TF assignments were made
- Batches062-063 reviewed 50 priority-8 glutamate receptor-complex rows; 46 reusable ionotropic/metabotropic relay candidates and 4 unresolved GluK3/GluK4–GluK5 boundaries were retained. No terminal TF assignments were made
- Batches144-145 reviewed 50 exact priority-8 rows spanning Nodal/activin-family, receptor-complex, and unresolved exact-pair boundaries; 8 receptor-proximal relay candidates, 4 binding-only cases, 1 function-only case, and 37 unresolved/no-pair-specific-evidence boundaries were retained. Two directly supported SMAD2/SMAD3 handoffs for matched Nodal receptor-complex rows were routed to Module22A; no TF-target programs were assigned
- Batches146-151 reviewed 150 exact priority-8 rows spanning Ntrk/Omg, PDGF, opioid, plasminogen/urokinase, melanocortin, periostin, protein-C/PAR, presenilin, and Pth/Ptn families; 36 receptor-proximal relay candidates, 28 binding-only cases, 10 function-only cases, and 76 unresolved/no-pair-specific-evidence boundaries were retained. No terminal TF handoffs were assigned; processed-ligand, receptor-complex, enzyme-substrate, and pathway/function boundaries remain explicit
- Batches152-155 reviewed 100 exact priority-8 rows spanning Psen1/Notch, Pspn/Pth/Pth2/Pthlh, Ptn, Ptpn6, Pyy, Rgma/Rgmb, Rims, Rln, Rspo, and Rtn4 families; 16 receptor-proximal relay candidates, 10 binding-only cases, 6 function-only cases, and 68 unresolved/no-pair-specific-evidence boundaries were retained. Four directly supported RBPJ/CSL handoffs for matched Psen1–Notch receptor-complex rows were routed to Module22A; no TF-target programs were assigned
- Batches156-158 reviewed 75 exact priority-8 rows spanning Rtn4, S100, Saa, Scel/Scgb, Sele/Selplg, Sema3/4/5/6, and Serpin families; 16 receptor-proximal relay candidates, 14 binding-only cases, 6 function-only cases, and 39 unresolved/no-pair-specific-evidence boundaries were retained. No terminal TF handoffs or TF-target programs were assigned
- Batches159-161 reviewed 75 exact priority-8 rows spanning Sema4/5/6, Serpin, Shh, Sirpa, Slit, Slurp, Slitrk, Sostdc1, Sparc, Spink3, and Spp1 families; 15 receptor-proximal relay candidates, 16 binding-only cases, 9 function-only cases, 7 scavenging/clearance cases, 4 explicit no-evidence boundaries, and 24 unresolved boundaries were retained. One directly supported TBX21/GATA3/RORC handoff for a matched Sema4a–Plxnd1 context was routed to Module22A; no TF-target programs were assigned
- Batches162-163 reviewed 50 exact priority-8 rows spanning Sst/Tac/Tff, Tdgf1, Tg/Tgfa/Tgfb, Tgm2, Thbs, and related exact receptor-complex boundaries; 13 receptor-proximal relay candidates, 6 binding/processing-only cases, 7 function-only cases, 1 explicit no-evidence boundary, and 23 unresolved boundaries were retained. No terminal TF handoffs or TF-target programs were assigned
- 153 pair-level provisional TF activation candidates are handed off to Module22A; no TF-target programs were assigned
- Detailed evidence fields are recorded in `module21a_pair_relay_evidence_detail.tsv`
- Module 20A ledgers and the frozen manifest were read-only inputs
