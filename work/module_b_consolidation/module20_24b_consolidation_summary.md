# Module 20B–24B consolidation batch 001 — reviewed

## Module 23B second-pass expansion (2026-09-04)

The B023 second-pass expansion promotes the existing MMRN2-CLEC14A direct and functional edges and adds five source-linked B edges for MMRN2-CD93, MMRN2-CD248, and the direct, localization-relay, and developmental-function layers of SLIT2 C-terminal LG-domain–glycosylated DAG1. The Module 23B audit register now contains 1,080 edges and 1,506 evidence rows; its 289 boundary rows are unchanged. The acquired primary records are retained under `data/raw/evidence/module23a_second_pass_20260904/`. These are audit-layer only and do not modify canonical signaling tables or simulator outputs.

The same-day source-backed promotion gate then promoted 701 additional 23B edges whose existing A evidence records were primary-paper, non-boundary, source-linked, and mapped one-to-one to B. The remaining EFNA3–EPHA2 edge is intentionally held as unresolved directness and remains non-exportable. The audit layer now has 773 edges with status `reviewed_supported`; total edge, evidence, and boundary counts remain 1,080, 1,506, and 289, respectively.

The shared B-layer generation pass is complete and has passed structural and
layer-separation review. It produced edge,
evidence, boundary, and consolidation-matrix registers for Modules 20B–24B
from the frozen A-layer inputs.

| B module | edges | evidence | boundaries | exportable edges |
|---|---:|---:|---:|---:|
| 20B | 5,906 | 5,906 | 4,796 | 1,110 |
| 21B | 111 | 54 | 0 | 111 |
| 22B | 5,733 | 5,906 | 5,047 | 723 |
| 23B | 1,075 | 1,456 | 289 | 1,075 |
| 24B | 151 | 200 | 31 | 151 |

Final edge-layer review counts:

| B module | direct molecular / LR | receptor-proximal / pathway | downstream / functional | contextual or unresolved | boundary |
|---|---:|---:|---:|---:|---:|
| 20B | 1,293 | 0 | 0 | 0 | 4,613 |
| 21B | 6 | 70 | 35 | 0 | 0 |
| 22B | 41 | 0 | 5,658 | 0 | 34 |
| 23B | 405 | 269 | 376 | 25 | 0 |
| 24B | 69 | 38 | 44 | 0 | 0 |

The 20B counts agree with the frozen Module 20A release: 1,293 supported
high/medium/uncertain rows, with 1,110 high/medium rows eligible for the
conservative export gate and 183 uncertain rows retained but excluded.

Validation passed for all five B layers:

- stable B edge IDs are unique;
- every exportable edge has at least one exportable evidence source;
- no edge is exportable solely from boundary/negative evidence;
- source A IDs and evidence references resolve;
- Module 22B boundary rows retain both their `module22a_evidence_id` and the
  associated B edge IDs;
- direct, pathway, functional, program, phenotype, and boundary layers remain
  distinguishable;
- Module 21B edge layers match the dedicated 21A evidence-layer register:
  70 receptor-proximal relay, 35 downstream/function, and 6
  ligand-receptor binding/activation edges;
- downstream/function labels containing the word “pathway” are not promoted to
  receptor-proximal relay;
- the frozen Module 20A LR manifest hash remains
  `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

The outputs are audit-layer only. They were loaded into the isolated
`module20b_*` through `module24b_*` PostgreSQL staging tables for validation;
canonical `SignalingEdge`/`SignalingEdgeSource` tables and the simulator bundle
remain untouched.
