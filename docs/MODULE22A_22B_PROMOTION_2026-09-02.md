# Module 22A-to-22B high-confidence promotion — 2026-09-02

This promotion pack records the bounded reuse of existing, exportable
high-confidence Module 22B TF-target evidence for exact Module 22A
ligand/receptor handoffs. It is an audit-layer cross-module linkage
artifact, not a new canonical SignalingEdge or evidence-unit write.

## Result

- Promotion records: 113
- Distinct 22A handoffs represented: 104
- Handoffs with an existing terminal-TF assignment: 102
- Evidence-backed terminal-TF assignments added in the linkage layer: 2
- Distinct reused 22B edges: 33
- Module 21A handoff register changed: false
- Module 22B edge/evidence registers changed: false
- PostgreSQL/canonical materialization performed: false

## Gate and boundaries

Each row is carried forward only from the high-confidence linkage audit
after checking the handoff identity, terminal TF, exportable 22B edge,
exportable evidence, and either high register evidence or a reviewed
primary extraction with High confidence. The `high` tier applies to the
tested TF-target evidence in its recorded comparator model; it does not
assert the same receptor-complex activity in an SCI receiver cell.

The source handoff, edge, and evidence limitations are copied into the
promotion ledger. This preserves receptor-complex ambiguity, ligand or
cofactor specificity, model/species limits, program-level edges, and
the distinction between a bounded upstream handoff and the reused 22B
TF-target record.

## Reproduction

- Audit input: `work/module22a_22b_promotion_audit/module22a_22b_high_confidence_links.tsv`
- Promotion ledger: `work/module22a_22b_promotion_audit/module22a_22b_high_confidence_promotions.tsv`
- Generator: `scripts/promote_module22a_22b_high_confidence_links.py`
