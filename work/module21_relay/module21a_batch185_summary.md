# Module 21A Batch 185 Summary

Batch 185 reviewed exactly the 25 filtered priority-8, low-confidence queue rows corresponding to ordinals 4076–4100: `M20A-LIANA-REMAINING-0348` through `M20A-LIANA-REMAINING-0372`, in the requested order.

## Outcomes

- 25 explicit no-evidence boundaries: Wnt16–Fzd9/Lrp5, Wnt16–Fzd9/Lrp6, all 20 Wnt2–Fzd10/Fzd1–Fzd9/Lrp5/6 composites, and Wnt2b–Fzd10/Lrp5, Wnt2b–Fzd10/Lrp6, and Wnt2b–Fzd1/Lrp5.
- No receptor-relay candidate, binding-only promotion, or function-only promotion was assigned.
- No terminal TF was assigned; every `terminal_TF` value is the literal `null`.

## Evidence boundaries

The existing Module20A LIANA adjudication packet classifies every requested row as `no_evidence` after bounded exact-pair and expanded-family searches. The review TSV retains primary comparator papers where informative: WNT-FZD selectivity mapping; WNT1-FZD/LRP5/6 receptor-complex studies; WNT10B-FZD6-LRP6 proximity/function; and the WNT16B-FZD5-LRP6 association study. These sources establish comparator ligand, FZD, or LRP contexts only; they do not establish any submitted Wnt16/Wnt2/Wnt2b–Fzd–Lrp5/6 composite.

The WNT16B primary study is especially restrictive: WNT16B-induced FZD5-LRP6 association was measured in engineered cell systems, but association was not treated as purified direct ternary binding, and the study did not test FZD9 or the submitted Wnt16 composites. For Wnt2 and Wnt2b, different-ligand WNT1/WNT7B/WNT10B evidence, FZD-family annotations, LRP5/6 pathway activity, expression, and generic beta-catenin output were not combined into direct exact-pair claims. LRP5 and LRP6 were kept as exact, non-interchangeable complex limitations.

The TSV uses the established 13-column Module 21A schema, contains one unique row per requested queue ID, has populated citations and limitations, and uses `terminal_TF=null` throughout. Existing Module20A adjudication files, shared ledgers, Module21A coverage/handoff registers, and other files were preserved. Only this batch TSV and summary were written; no commit was created.
