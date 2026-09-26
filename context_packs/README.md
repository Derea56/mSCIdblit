# Context evidence packs

Context packs are versioned overlays for the neutral mechanism graph. They
contain disease-, injury-, tissue-, study-, and dataset-specific evidence;
they do not modify generic mechanism nodes, edges, or route topology.

The intended composition for downstream analysis is:

```text
generic mechanism release
        +
context evidence pack
        +
dataset observations
        -> mSCS route evaluation
```

## Separation rules

- A mechanism edge remains generic even when a supporting source uses a spinal
  cord injury model.
- Context is attached to an evidence observation or reviewed mechanism link,
  not copied onto the generic edge.
- `not_measured` is distinct from `negative`; missing omics must not be
  treated as evidence against a route.
- External observations remain source-native and provenance-linked.
- Context packs do not contain route confidence scores or arbitrary modality
  weights. mSCS is responsible for evaluation and calibration.
- A source or experiment must not be counted twice merely because it supports
  multiple stages of one route.

The initial pack is [`spinal_cord_injury/`](spinal_cord_injury/). Additional
disease or injury packs can reuse the same tabular contract and mechanism IDs.
