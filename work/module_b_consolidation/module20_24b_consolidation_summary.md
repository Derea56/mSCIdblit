# Module 20B–24B consolidation batch 001 — reviewed

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
