# Module 22B low-confidence upgrade batch 002 — 2026-09-02

This single-row batch promotes `M22B-E000782` from low to medium confidence.
The linked primary human pancreatic-cancer study reports that recombinant
WNT5A increases ABCG2 expression and gemcitabine resistance, while FZD7
silencing or inhibition blocks those responses. The result supports a bounded
WNT5A–FZD7 receptor-dependent functional relay, but not purified binding,
context-independent generalization, or a terminal TF-target edge.

The evidence row is upgraded to high source confidence because the primary
study directly tests the perturbation relationship. The edge remains medium
because the receptor assignment is perturbational and model-specific. The
canonical SQL materialization is intentionally unchanged; this batch updates
the Module 22B register and its auditable upgrade packet only.
