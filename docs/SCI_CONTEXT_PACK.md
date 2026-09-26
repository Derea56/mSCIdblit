# SCI context evidence overlay

The Module 20B–24B mechanism graph is intentionally disease-neutral. It
describes reusable signaling relationships and route evidence. Spinal cord
injury (SCI) evidence is therefore maintained as a context overlay rather
than being written into generic mechanism edges.

## Data composition

```text
mSCIdblit mechanism release
        +
spinal_cord_injury context pack
        +
dataset observations
        -> mSCS route evaluation
```

The overlay is located at
[`context_packs/spinal_cord_injury/`](../context_packs/spinal_cord_injury/).
Its manifest pins `mSCIdblit-v1.9.386` and the corresponding mechanism release
so that context links can be interpreted against a known route/node/edge
namespace.

## What belongs in the SCI pack

The pack may contain observations from spinal cord injury studies, including:

- protein and phosphoprotein measurements;
- transcriptomic measurements and target responses;
- spatial or anatomical co-localization;
- epigenetic and chromatin observations;
- imaging and histology;
- interventions, knockouts, inhibitors, rescue experiments, and stimulation;
- functional, behavioral, or tissue-level outputs.

Every observation should preserve the reported study context when available:
species, injury model, injury level, tissue, cell type, timepoint,
perturbation, treatment, sample, assay, and source locator.

## What does not belong in the SCI pack

- Generic mechanism edges copied from the base graph.
- A new SCI-specific version of a generic ligand–receptor edge.
- A route confidence score or hand-assigned modality weight.
- A claim that an unmeasured intracellular protein was observed.
- A negative conclusion from a modality that was not measured.

## Evidence roles

The overlay distinguishes four roles:

| Role | Meaning |
|---|---|
| `dataset_observation` | Measured in the dataset or study being evaluated |
| `context_matched_external_observation` | Measured in an external study with an explicitly recorded context match |
| `inferred_bridge` | A mechanistic or modality-based inference used to connect observations, not a direct measurement |
| `contextual_annotation` | Tissue, injury, spatial, regulatory, or study context that does not by itself assert route activity |

`ContextEvidenceObservation.dependency_group` identifies observations that are
not independent, such as multiple readouts from one experiment or multiple
claims derived from one source artifact. mSCS can use this field to prevent
double counting.

## Mechanism links

`ContextMechanismLink` points to an identifier in the pinned mechanism release
using text keys because the release is a file-based external bundle. A link
records the route stage it bears on—ligand, receptor, intracellular, TF,
output, or context—and whether the relationship is exact, related, generic,
or unknown.

A context link does not create a `SignalingEdge`, grant traversal permission,
or promote a partial route to a complete route. It is evidence for mSCS to
consider during route evaluation.

## Population sequence

1. Register the exact source record and artifact checksum.
2. Define the study or sample context.
3. Import the observation without filling unmeasured fields.
4. Assign a dependency group for double-counting control.
5. Link the observation to stable mechanism identifiers.
6. Review source scope and context match.
7. Export the context pack with counts, hashes, and validation results.

The scaffold currently contains one scope-level context profile and zero
study-level observations or mechanism links. That is deliberate: it provides
the contract for adding data without asserting unverified SCI evidence.
