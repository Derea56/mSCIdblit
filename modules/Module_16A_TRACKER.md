# Module 16A: PNS Electrical Stimulation Preconditioning for CNS Repair - Corpus Building Tracker

## Overview

This tracker captures peripheral nervous system electrical stimulation as a preconditioning or conditioning-like stimulus for CNS repair. The focus is stimulation of peripheral nerves, DRG-associated sensory pathways, or peripheral afferent systems before, during, or shortly after CNS injury, with emphasis on whether electrical stimulation can induce growth-state, activity-dependent, metabolic, transcriptional, or spinal-circuit responses relevant to spinal cord repair.

This module is intentionally separate from Module 15. Module 15 tracks peripheral nerve lesion and DRG priming. Module 16 tracks electrical stimulation as a less destructive and more clinically plausible conditioning stimulus, while preserving the evidence boundary that stimulation may only partially recapitulate conditioning-lesion effects.

**First-pass curation freeze**: 2026-07-22. Status: SATURATED / FROZEN FIRST PASS.

## Scope Boundaries

| Boundary ID | Include | Exclude / Route Elsewhere | Notes |
|---|---|---|---|
| M16A-B001 | Electrical stimulation of peripheral nerve, intact nerve, transected nerve stump, DRG-linked afferents, or peripheral afferent pathways as preconditioning/conditioning for regeneration or CNS repair | Epidural spinal stimulation, brain stimulation, or rehabilitation stimulation without peripheral nerve conditioning logic | Route epidural/rehabilitation-only rows to Module 5 or Module 10 unless they test PNS conditioning. |
| M16A-B002 | Stimulation parameters: nerve target, intact versus injured nerve, frequency, pulse width, intensity, duration, timing relative to injury, repetition, and delivery site | Stimulation studies lacking parameters or regeneration/repair endpoint | Record parameter fields before comparing studies. |
| M16A-B003 | DRG growth-state, neurite outgrowth, dorsal column regeneration, peripheral nerve regeneration, spinal metabolic activation, and activity-dependent repair markers | Pain modulation or neuromodulation-only outcomes without regeneration/repair relevance | Preserve endpoint family. |
| M16A-B004 | Comparisons between electrical stimulation, conditioning crush/axotomy, cAMP, activity, and enriched conditioning | Claims that stimulation fully replaces conditioning lesion without direct head-to-head evidence | Electrical conditioning is a candidate mimic, not automatically equivalent to lesion priming. |

## Search / Source Log

| Search ID | Source | Query / Source | Retrieved | Included | Status | Notes |
|---|---|---|---|---|---|---|
| M16A-S001 | PubMed/PMC | peripheral nerve electrical stimulation conditioning dorsal root ganglion spinal cord injury regeneration | 30+ source-page hits reviewed | 4 | COMPLETE FIRST PASS | Direct sensory axon growth after SCI and DRG neurite outgrowth rows captured. |
| M16A-S002 | PubMed/PMC | brief electrical stimulation sciatic nerve conditioning lesion axon regeneration | 30+ source-page hits reviewed | 4 | COMPLETE FIRST PASS | Peripheral nerve regeneration and conditioning-ES review rows captured. |
| M16A-S003 | PubMed/PMC | electrical stimulation sciatic nerve dorsal root ganglion metabolic activity spinal cord | 10+ source-page hits reviewed | 1 | COMPLETE FIRST PASS | Early metabolic activation boundary row captured. |
| M16A-S004 | PubMed/PMC | electrical stimulation dorsal column spinal cord injury sensory axon regeneration | 20+ source-page hits reviewed | 3 | COMPLETE FIRST PASS | Direct CNS/dorsal column repair and limitation rows captured. |
| M16A-S005 | PubMed/PMC | functional electrical stimulation axon regeneration program peripheral nerve review | 20+ source-page hits reviewed | 2 | COMPLETE FIRST PASS | Review anchors separating molecular pathways from efficacy boundaries captured. |
| M16A-S006 | Citation mining | Module 15 conditioning lesion references and electrical-stimulation review back-citations | 15+ candidate citations reviewed | 2 | COMPLETE FIRST PASS | Lesion-conditioning comparator rows included for boundary only. |

## Evidence Categories Saturated

| Category ID | Category | Required Boundaries | Status |
|---|---|---|---|
| M16A-CAT001 | Direct PNS electrical stimulation for sensory axon growth after SCI | Nerve/DRG target, stimulation timing, dorsal column or graft endpoint, comparison to lesion conditioning | COMPLETE FIRST PASS |
| M16A-CAT002 | Electrical stimulation of intact peripheral nerve before DRG culture or injury | Intact/injured nerve, frequency, duration, DRG harvest timing, neurite endpoint | COMPLETE FIRST PASS |
| M16A-CAT003 | Brief electrical stimulation after peripheral nerve injury/repair | Repair model, motor/sensory axon endpoint, timing, clinical feasibility | COMPLETE FIRST PASS |
| M16A-CAT004 | Activity/metabolic effects of sciatic nerve stimulation | Spinal cord versus DRG compartment, frequency, metabolic endpoint | COMPLETE FIRST PASS |
| M16A-CAT005 | Comparison with conditioning lesion and cAMP-like mechanisms | Conditioning lesion, electrical conditioning, cAMP, transcriptional/regeneration program boundaries | COMPLETE FIRST PASS |
| M16A-CAT006 | Limitations for central regeneration | Initiation versus elongation, growth into lesion versus beyond lesion, chronic functional status | COMPLETE FIRST PASS |
| M16A-CAT007 | Translation and safety | Non-destructive conditioning, stimulation burden, peripheral nerve damage avoidance, clinical analogs | COMPLETE FIRST PASS |
| M16A-CAT008 | Integration with SCI repair strategy | Whether stimulation targets DRG growth state, host state, graft entry, circuit activity, or peripheral nerve repair | COMPLETE FIRST PASS |

## Paper Inventory

| Paper ID | PMID | First Author | Year | Title | Journal | DOI | Curation Status | Notes |
|---|---|---|---|---|---|---|---|---|
| M16A-P001 | PMC5752127 | Udina | 2008 | Depolarization and electrical stimulation enhance in vitro and in vivo sensory axon growth after spinal cord injury | Experimental Neurology | 10.1016/j.expneurol.2008.08.029 | PASS 3 FULLTEXT-PMC | Direct sensory axon growth after SCI; depolarization/electrical stimulation increased initiation but did not fully replace conditioning lesion. |
| M16A-P002 | PMID:3862113 | Kadekaro | 1985 | Differential effects of electrical stimulation of sciatic nerve on metabolic activity in spinal cord and dorsal root ganglion in the rat | Proceedings of the National Academy of Sciences | 10.1073/pnas.82.17.6010 | PASS 3 FULLTEXT-PMC | Sciatic stump stimulation caused frequency-dependent spinal dorsal horn glucose utilization without DRG cell-body metabolic activation. |
| M16A-P003 | PMC10779324 | Gordon | 2023 | Brief Electrical Stimulation Promotes Recovery after Surgical Repair of Injured Peripheral Nerves | International Journal of Molecular Sciences | 10.3390/ijms242316939 | PASS 3 FULLTEXT-PMC | Review anchor for brief ES and conditioning ES; includes intact sciatic nerve 20 Hz for 1 h enhancing DRG neurite outgrowth. |
| M16A-P004 | PMC7425295 | Gordon | 2020 | Functional Electrical Stimulation and the Modulation of the Axon Regeneration Program | Frontiers in Cell and Developmental Biology | 10.3389/fcell.2020.00736 | PASS 3 FULLTEXT-PMC | Review anchor stating ES activates overlapping pathways with conditioning lesions but does not fully recapitulate their growth-promoting effects. |
| M16A-P005 | PMID:10402195 | Neumann | 1999 | Regeneration of dorsal column fibers into and beyond the lesion site following adult spinal cord injury | Neuron | 10.1016/S0896-6273(00)80755-2 | PASS 3 SOURCE-PAGE | Conditioning lesion comparator; defines benchmark that peripheral axotomy before dorsal column injury enables growth beyond lesion. |
| M16A-P006 | PMID:22227059 | Blesch | 2012 | Conditioning lesions before or after spinal cord injury recruit broad genetic mechanisms that sustain axonal regeneration: superiority to cAMP-mediated effects | Experimental Neurology | 10.1016/j.expneurol.2011.12.037 | PASS 3 FULLTEXT-PMC | Conditioning lesion/cAMP comparator for judging whether ES only partially mimics lesion-induced growth programs. |
| M16A-P007 | PMID:15716400 | Qiu | 2005 | Conditioning Injury-Induced Spinal Axon Regeneration Requires Signal Transducer and Activator of Transcription 3 Activation | Journal of Neuroscience | 10.1523/JNEUROSCI.4427-04.2005 | PASS 3 FULLTEXT-PMC | STAT3 conditioning lesion comparator; useful for testing whether ES engages similar DRG pathways. |
| M16A-P008 | PMID:33349630 | Pita-Thomas | 2021 | Enriched conditioning expands the regenerative ability of sensory neurons after spinal cord injury via neuronal intrinsic redox signaling | Nature Communications | 10.1038/s41467-020-20112-4 | PASS 3 SOURCE-PAGE | Activity/enrichment plus lesion-conditioning comparator; supports activity-state synergy boundary. |
| M16A-P009 | PMID:6204020 | Oblinger | 1984 | A conditioning lesion of the peripheral axons of dorsal root ganglion cells accelerates regeneration of only their peripheral axons | Journal of Neuroscience | 10.1523/JNEUROSCI.04-07-01736.1984 | PASS 3 FULLTEXT-PMC | Branch-specific conditioning boundary; prevents assuming peripheral effects equal central branch repair. |
| M16A-P010 | PMID:9527536 | Smith | 1998 | Mechanisms of enhancement of neurite regeneration in vitro following a conditioning sciatic nerve lesion | Journal of Comparative Neurology |  | PASS 3 SOURCE-PAGE | Lesion-conditioning neurite morphology comparator for ES-induced DRG neurite effects. |
| M16A-P011 | PMID:30778286 | Dubovy | 2019 | A Conditioning Sciatic Nerve Lesion Triggers a Pro-regenerative State in Primary Sensory Neurons Also of Dorsal Root Ganglia Non-associated With the Damaged Nerve | Frontiers in Cellular Neuroscience | 10.3389/fncel.2019.00011 | PASS 3 FULLTEXT-PMC | Remote DRG lesion-conditioning comparator; helps frame whether ES has local versus systemic/remote priming evidence. |
| M16A-P012 | PMID:19515349 | Silver | 2009 | CNS regeneration: only on one condition | Current Biology | 10.1016/j.cub.2009.04.026 | PASS 3 FULLTEXT-PMC | Commentary boundary for conditioning lesion timing and central regeneration claims. |
| M16A-P013 | PMID:3167569 | Jenq | 1988 | Conditioning lesions of peripheral nerves change regenerated axon numbers | Brain Research | 10.1016/0006-8993(88)90057-1 | PASS 3 SOURCE-PAGE | Peripheral conditioning lesion timing benchmark for regenerated axon numbers. |
| M16A-P014 | PMID:32778834 | Kong | 2020 | AMPK controls the axonal regenerative ability of dorsal root ganglia sensory neurons after spinal cord injury | Nature Metabolism | 10.1038/s42255-020-0252-3 | PASS 3 SOURCE-PAGE | DRG metabolic growth-state comparator; candidate readout for ES-induced conditioning. |
| M16A-P015 | PMID:29717546 | Bradke | 2018 | The Dorsal Column Lesion Model of Spinal Cord Injury and Its Use in Deciphering the Neuron-Intrinsic Injury Response | Methods in Molecular Biology | 10.1007/978-1-4939-7649-2_13 | PASS 3 SOURCE-PAGE | Model boundary for central branch repair assays. |
| M16A-P016 | PMC3103885 | Houle | 2007 | Sensory Afferents Regenerated into Dorsal Columns after Spinal Cord Injury Remain in a Chronic Pathophysiological State | Experimental Neurology | 10.1016/j.expneurol.2007.01.026 | PASS 3 FULLTEXT-PMC | Functional/chronic boundary: regenerated sensory afferents after conditioning-plus-repair may remain pathophysiological. |

## Experiment-Level Rows

| Experiment ID | Paper ID | Figure/Table Ref | Species / Population | Model / System | PNS Electrical Stimulation / Comparator | Timing | Comparator | Endpoint | Observation Seed | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| M16A-P001-E001 | M16A-P001 | Full text PMC | Adult rat DRG sensory neurons | Dorsal column SCI and DRG culture | Depolarization/electrical stimulation conditioning | before or after central injury as source-specific | conditioning lesion and unstimulated controls | sensory axon growth initiation and elongation | Electrical stimulation/depolarization enhanced sensory axon growth initiation after SCI but was less robust than conditioning lesion for elongation through the lesion. | high |
| M16A-P002-E001 | M16A-P002 | Full text PMC | Adult rat sciatic afferent pathway | Transected sciatic nerve stump stimulation | Electrical stimulation of proximal sciatic nerve stump | acute stimulation | frequency and unstimulated comparators | glucose utilization in spinal cord and DRG | Sciatic nerve stimulation produced frequency-dependent dorsal horn metabolic activation but did not increase DRG cell-body glucose utilization. | high |
| M16A-P003-E001 | M16A-P003 | Full text PMC | Rat DRG neurons / peripheral nerve repair literature | Intact sciatic stimulation and peripheral nerve repair | Brief ES and conditioning ES, including 20 Hz for 1 h intact sciatic stimulation | 1-7 days before DRG culture or at repair | no ES, conditioning lesion, surgical repair controls | DRG neurite outgrowth and peripheral nerve regeneration | Brief ES can enhance DRG neurite outgrowth and peripheral nerve repair outcomes, but conditioning ES and lesion conditioning are not equivalent across endpoints. | high |
| M16A-P004-E001 | M16A-P004 | Full text PMC | Peripheral and central axon regeneration literature | Review of functional ES and regeneration programs | Functional/electrical stimulation as activity-dependent conditioning | source-specific acute or conditioning windows | lesion conditioning, no stimulation, injury controls | regeneration-program activation and axon growth | Review states ES activates overlapping pathways with peripheral conditioning lesions but does not fully recapitulate conditioning lesion effects. | high |
| M16A-P005-E001 | M16A-P005 | Abstract/source page | Adult rat DRG sensory neurons | Dorsal column SCI lesion | Peripheral axotomy conditioning lesion benchmark | 1-2 weeks before dorsal column lesion | no conditioning / concurrent lesion | central axon growth into and beyond lesion | Peripheral lesion preconditioning is the benchmark for central sensory axon growth beyond dorsal column lesion. | medium |
| M16A-P006-E001 | M16A-P006 | Full text PMC | Adult rat DRG sensory neurons | Cervical SCI with graft/neurotrophin support | Sciatic conditioning lesion versus cAMP comparator | before or shortly after SCI | cAMP, graft/neurotrophin controls | central axon regeneration and gene expression | Lesion conditioning recruited broader and longer-lasting genetic programs than cAMP, setting a benchmark for ES mimicry. | high |
| M16A-P007-E001 | M16A-P007 | Full text PMC | Adult rat DRG neurons | Sciatic transection plus dorsal column crush | Conditioning lesion with JAK2/STAT3 perturbation | 1 week before central lesion | saline versus AG490 | STAT3, GAP-43, neurite outgrowth, dorsal column regeneration | STAT3 activation is a required DRG growth-state benchmark for conditioning-like stimulation approaches. | high |
| M16A-P008-E001 | M16A-P008 | Abstract/source page | Adult sensory neurons after SCI | Enriched conditioning plus SCI | Environmental enrichment plus sciatic conditioning | before SCI | enrichment alone or conditioning alone | redox signaling, axon growth beyond lesion, functional recovery | Enriched conditioning shows activity-state synergy with lesion conditioning through PKC-STAT3-NOX2 signaling. | medium |
| M16A-P009-E001 | M16A-P009 | Full text PMC | Adult rat DRG neurons | Peripheral branch versus dorsal root regeneration | Conditioning crush lesion comparator | 2 weeks before branch test lesion | no conditioning lesion | branch-specific axon growth rate | Peripheral conditioning effects can be branch-specific and cannot be assumed to improve central branch repair in every assay. | high |
| M16A-P010-E001 | M16A-P010 | Abstract/source page | Adult rat DRG neurons | DRG culture after sciatic lesion | Conditioning lesion neurite-morphology comparator | before culture | control DRG neurons | neurite initiation, outgrowth rate, branching | Conditioning lesions alter neurite initiation, growth rate, and branching, defining phenotype dimensions for ES comparison. | medium |
| M16A-P011-E001 | M16A-P011 | Full text PMC | Rat lumbar and cervical DRG neurons | Remote/non-associated DRG priming model | Unilateral sciatic lesion comparator | 7 days before second nerve test or culture | control or local lesion only | GAP-43, SCG10, neurite outgrowth, axon regeneration | Lesion conditioning can produce remote/non-associated DRG priming; ES needs separate evidence before remote effects are inferred. | high |
| M16A-P012-E001 | M16A-P012 | Full text PMC | DRG sensory neuron literature | Conditioning lesion timing review | Conditioning lesion commentary comparator | before or after central lesion as reviewed | timing sequence comparator | central axon regeneration boundary | Conditioning-like claims must preserve sequence and timing because reversed-order effects differ from preconditioning. | high |
| M16A-P013-E001 | M16A-P013 | Abstract/source page | Adult rat peripheral nerves | Peripheral nerve regeneration model | Conditioning crush lesion timing comparator | 2, 7, or 14 days before test crush | single crush control | regenerated myelinated axon number | Conditioning effects on regenerated axon numbers require sufficient interval between lesions; timing is a stimulation-design boundary. | medium |
| M16A-P014-E001 | M16A-P014 | Abstract/source page | DRG sensory neurons after SCI | DRG metabolic growth-state model | AMPK metabolic pathway comparator | post-injury as source-specific | pathway perturbation controls | axonal regenerative ability after SCI | AMPK controls DRG sensory-neuron regenerative ability, supporting metabolic readouts for ES preconditioning. | medium |
| M16A-P015-E001 | M16A-P015 | Abstract/source page | DRG sensory neurons / dorsal column model | Dorsal column lesion model review/protocol | Model-system comparator for central branch repair | source-specific | central versus peripheral branch injury comparison | intrinsic injury response and regeneration assay design | Dorsal column model defines the assay boundary for testing whether ES improves central branch regeneration. | medium |
| M16A-P016-E001 | M16A-P016 | Full text PMC | Adult rat sensory afferents | Chronic dorsal column regeneration after SCI | Conditioning lesion plus inhibitory-matrix neutralization comparator | chronic 6-month post-injury assessment | injury/repair controls | functional sensory axon status | Even regenerated sensory afferents after conditioning-plus-repair can remain chronically pathophysiological, setting functional safety boundaries for ES-enabled repair. | high |

## Saturation Checklist

| Check | Status | Notes |
|---|---|---|
| Direct ES-plus-SCI sensory regeneration evidence searched | MET FOR FIRST PASS | Udina full-text row captured. |
| PNS stimulation parameter evidence searched | MET FOR FIRST PASS | Intact/proximal sciatic stimulation, frequency/duration, and brief ES rows captured. |
| DRG and spinal response compartments separated | MET FOR FIRST PASS | Dorsal horn metabolic activation and DRG neurite outcomes kept separate. |
| Conditioning lesion comparator evidence searched | MET FOR FIRST PASS | Module 15 benchmark rows incorporated as comparator-only evidence. |
| Mechanistic readout candidates captured | MET FOR FIRST PASS | STAT3, cAMP, AMPK, redox/NOX2, neurite morphology, and transcriptional-program boundaries retained. |
| Central regeneration limitations captured | MET FOR FIRST PASS | Initiation versus elongation and chronic pathophysiology boundaries recorded. |
| Translation boundaries retained | MET FOR FIRST PASS | ES is treated as clinically plausible but not equivalent to lesion conditioning. |
| Confidence labels retained | MET FOR FIRST PASS | Rows are full-text PMC or source-page as marked. |

## First-Pass Decision

| Decision ID | Status | Basis | Boundary / Queue |
|---|---|---|---|
| M16A-D001 | SATURATED / FROZEN FIRST PASS | 16-source first-pass corpus covers PNS electrical stimulation, sciatic stimulation metabolic effects, DRG neurite outgrowth, sensory axon growth after SCI, brief ES/peripheral repair, conditioning-lesion benchmarks, cAMP/STAT3/AMPK/redox candidate readouts, remote-priming boundary evidence, and chronic functional safety. | Next step is Module 16B consensus-ready extraction with stimulation parameters, nerve target, timing, DRG/spinal compartment, endpoint, and equivalence-to-lesion-conditioning boundaries preserved. |
