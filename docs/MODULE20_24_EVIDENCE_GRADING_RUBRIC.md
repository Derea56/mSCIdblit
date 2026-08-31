# Module 20B–24B evidence grading rubric

This rubric makes the two evidence axes explicit for Modules 20B, 21B, 22B,
23B, and 24B. It does not replace the existing register `confidence_tier`,
`evidence_layer`, `exportable`, or graph traversal gates.

## Independent axes

`evidence_grade` describes how directly and reproducibly the asserted source
or edge is supported. `context_level` describes the highest biological context
actually represented by that evidence. A high evidence grade does not imply
spinal-cord or SCI context, and L3/L4 context does not make a weak or
non-promotable mechanism claim strong.

| Grade | Meaning | Minimum basis |
|---|---|---|
| A | Independent literature corroboration | The same asserted relationship is supported by a traceable primary source plus independent corroboration, or by multiple independent primary sources. |
| B | Single-source primary evidence | One traceable primary source supports the asserted relationship at the level claimed; abstract-only or indirect cases retain their limitations. |
| C | Source-table or aggregated regulon evidence | A relationship is present in a source table or aggregated resource, but pair-level primary evidence has not been independently verified. |
| D | Database/profile/membership-only evidence | Database, motif/profile, pathway membership, or catalog evidence without pair-specific literature or experiment support. |
| E | Reviewed but non-promotable evidence | The record was reviewed, but it is a near match, wrong direction/species, contextual association, negative/bounded search result, or otherwise cannot support the asserted mechanism. |
| U | Unreviewed or unresolved | The record has not undergone sufficient source adjudication to assign A–E. |

The grade is assigned to the exact asserted relationship, not to the general
biological existence of either endpoint. A paper about a paralog, a related
complex, or a different direction is not silently upgraded to the requested
relationship.

## Context levels

| Level | Meaning |
|---|---|
| L0 | No qualifying context has been established for the exact asserted relationship. |
| L1 | Non-CNS evidence only. |
| L2 | CNS evidence, but no spinal-cord tissue context. |
| L3 | Spinal-cord tissue context, without a spinal-cord injury experiment. |
| L4 | Spinal-cord injury context for the exact asserted relationship or its explicitly bounded experimental system. |

Context is assigned from the source evidence itself. Expression, pathway
membership, orthology, or a shared module does not transfer L3/L4 context to a
different pair. When regulator and target contexts differ, retain separate
component fields in staging and use `context_level` for the exact asserted
source/edge relationship.

## Canonicalization gates

Before a record can become a canonical Paper/Experiment/Observation/
AuthorClaim/EvidenceLink route, it must have:

1. a stable paper identifier or an explicitly approved non-paper source type;
2. a source locator that identifies the relevant experiment, result, or claim;
3. an evidence grade and context level with a written basis;
4. a separately validated relation, species, direction/effect, model/cell
   context, and limitation statement; and
5. a graph edge whose scope matches the evidence. A paper or abstract alone is
   not a license to create an experiment or TF/program claim.

Rows missing any of these remain in the audit/staging layer. `U` and `E` rows
remain queryable and screenable but are not traversal evidence by grade alone.
