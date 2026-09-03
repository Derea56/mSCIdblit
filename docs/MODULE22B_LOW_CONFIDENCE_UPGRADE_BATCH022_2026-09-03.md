# Module 22B low-confidence upgrade batch 022 — 2026-09-03

This batch recovers four bounded program associations from low confidence to
medium confidence. It does not create direct TF-target edges, assign a
terminal TF to a receptor pathway, or infer SCI-specific activity.

| Edge | Recovered bounded claim | Primary source |
| --- | --- | --- |
| `M22B-E000499` | BMP6/7 uses ACVR1A, ACVR2A, and BMPR2-associated signaling for ID1/DLX5/IBSP osteoblastic output; the BMPR1B-BMPR2 composite is removed. | PMID 18436533; PMCID PMC3258927 |
| `M22B-E000728` | TNF-alpha/Msx2-associated WNT7A/WNT3A paracrine signaling is linked to beta-catenin/TCF osteogenic output; LDLR is model context only. | PMID 17932314; PMID 15841209; PMCID PMC1077175 |
| `M22B-E000789` | WNT7A-FZD9 activates an ERK5-dependent PPARgamma antitumor program; the LRP5 composite is removed. | PMID 16835228 |
| `M22B-E000790` | WNT7A-FZD9 activates an ERK5-dependent PPARgamma antitumor program; the LRP6 composite is removed. | PMID 16835228 |

The exact unsupported receptor-composite interpretation remains excluded in
each row, and limitations are preserved in both the edge and evidence
registers. Canonical SQL materialization is not performed by this batch.

Generator: `scripts/promote_module22b_low_confidence_batch022.py`

Audit ledger: `work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch022.tsv`
