# mSCIdblit mechanism graph release v1.8.90

Release date: 2026-09-17

This release adds the 85th selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten newly curated
ligand–receptor output annotations as source-linked evidence routes for mSCS
plausibility analysis. Nine routes retain a bounded receptor-to-effector
continuation, while LEAP2–GHSR1A is intentionally retained as an output-only
antagonist route because the ligand inhibits ghrelin-dependent receptor
activation rather than activating the receptor’s downstream branch.

The routes cover LTE4–OXGR1/GPR99, beta-endorphin/endomorphin-1/
Met-enkephalin–OPRM1, acetylcholine–CHRM2/CHRM4, UTP–P2Y2, LEAP2–GHSR1A,
and Urocortin-1–CRHR1/CRHR2. Representative primary support includes
LTE4-dependent OXGR1 reporter and vascular-permeability responses
([PMID:23504326](https://pubmed.ncbi.nlm.nih.gov/23504326/)), beta-endorphin
activity at cloned MOR ([PMID:12513698](https://pubmed.ncbi.nlm.nih.gov/12513698/)),
endomorphin-1 inhibition of adenylate cyclase
([PMID:11404430](https://pubmed.ncbi.nlm.nih.gov/11404430/)), UTP-dependent
P2Y2 calcium signaling ([PMID:10839197](https://pubmed.ncbi.nlm.nih.gov/10839197/)),
LEAP2 antagonism of GHSR1A
([PMID:29233536](https://pubmed.ncbi.nlm.nih.gov/29233536/)), and Urocortin-1
activation of CRH receptors ([PMID:7477349](https://pubmed.ncbi.nlm.nih.gov/7477349/)).
For the M2/M4 records, the queue’s PMID:8382764 entry is retained as review
context; primary Gi/o-coupling support is carried through the receptor-coupling
evidence locators PMID:2172674, PMID:15655507, and PMID:1650470.

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status, and the TF and target
gene fields remain unasserted. mSCS can use the retained output and
intracellular evidence as route-plausibility inputs while applying its own
confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,631
- Cumulative literature-expansion rows: 584
- Unique downstream queue candidates with literature coverage: 567
- Remaining downstream queue candidates: 2,764, including 1,699 P1 candidates
- Literature route tiers: 15 full routes; 22 with ligand–receptor–intracellular–TF and missing target output; 233 with ligand–receptor–intracellular–output and missing TF; 62 with ligand–receptor–TF–output and missing intracellular continuation; and 252 ligand–receptor–output routes missing intracellular and TF layers

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing routes where primary studies can
add an output or a bounded intracellular continuation without overclaiming
terminal transcriptional effects.
