# Module 22B low-confidence upgrade batch 004 — 2026-09-02

This batch re-anchors two rows whose submitted handoff contained a mismatch or
downstream-adaptor boundary, while retaining the exact receptor pair already
represented in each target program:

- `M22B-E000518`: CD30L/TNFSF8–CD30/TNFRSF8, promoted to medium.
- `M22B-E000619`: OX40L/TNFSF4–OX40/TNFRSF4, promoted to medium.

The primary TNFSF/TNFRSF survey directly tested ligand-receptor interactions in
human and mouse reagent panels. It supports the exact receptor-pair anchor and
not the complete intracellular TRAF/NF-kB relay or a terminal TF target. The
canonical SQL materialization is unchanged; the register and auditable packet
are updated only.
