# Module 21A batch 167 review summary

## Scope

This bounded review covers exactly the 25 requested queue rows, in the supplied order, and no other rows. Pair labels are preserved literally, including the submitted receptor-complex label `Crlf2_Il7r_Tslp`.

Exact reviewed IDs and pairs:

```text
M20A-EXT-3387 Tshb Vipr1
M20A-EXT-3389 Tslp Crlf2_Il7r_Tslp
M20A-EXT-3390 Ttr Ngfr
M20A-EXT-3391 Txlna Stx1a
M20A-EXT-3392 Txlna Stx3
M20A-EXT-3393 Txlna Stx4a
M20A-EXT-3396 Ucn2 Crhr1
M20A-EXT-3398 Ucn2 Il10rb
M20A-EXT-3399 Ucn3 Crhr1
M20A-EXT-3401 Ucn3 Il10rb
M20A-EXT-3405 Vasp Cxcr2
M20A-EXT-3408 Vcam1 Itga9_Itgb1
M20A-EXT-3410 Vcan Egfr
M20A-EXT-3411 Vcan Itga4
M20A-EXT-3412 Vcan Itgb1
M20A-EXT-3414 Vcan Selp
M20A-EXT-3415 Vcan Tlr1
M20A-EXT-3417 Vcl Alk
M20A-EXT-3418 Vcl Itgb5
M20A-EXT-3420 Vegfa Egfr
M20A-EXT-3421 Vegfa Ephb2
M20A-EXT-3423 Vegfa Grin2b
M20A-EXT-3424 Vegfa Itga9
M20A-EXT-3425 Vegfa Itgav
M20A-EXT-3426 Vegfa Itgb1
```

## Disposition

- `reviewed_relay_candidate`: 8 rows — TSLP/CRLF2-IL7R, VASP/CXCR2, VCAM1/alpha9beta1, VCAN/beta1-integrin, VEGFA/NR2B relay, and VEGFA with alpha9beta1, alphaVbeta3, or beta1-containing integrin evidence.
- `reviewed_binding_only`: 6 rows — TXLNA/STX1A, TXLNA/STX3, TXLNA/STX4A, weak UCN2/CRHR1 and UCN3/CRHR1 binding, and VCAN/P-selectin binding.
- `reviewed_function_only`: 3 rows — VCAN/EGFR, VCL/ITGB5 organization, and VEGFA/EPHB2-associated function.
- `no_evidence_boundary`: 8 rows — Tshb/Vipr1, Ttr/Ngfr, UCN2/IL10RB, UCN3/IL10RB, VCAN/ITGA4, VCAN/TLR1, VCL/ALK, and VEGFA/EGFR.
- Terminal TF assignments: none; every TSV row uses `terminal_TF=null`.

## Evidence-layer findings

1. **TSLP receptor complex:** primary reconstitution and human leukemia studies support TSLP binding to a CRLF2/TSLPR–IL7Ralpha complex and receptor-proximal kinase/STAT5 signaling. The submitted receptor label is retained, but its redundant/noncanonical naming and exact stoichiometry are explicitly limited.
2. **Intracellular and adhesion binding:** alpha-taxilin binds syntaxin-family proteins; VASP is a CXCR2-interacting intracellular adaptor; alpha9beta1 binds VCAM1; versican binds beta1-integrin and P-selectin in distinct contexts. These are not silently treated as one common extracellular ligand-receptor class.
3. **Versican boundaries:** VCAN can modulate EGFR transactivation, beta1-integrin/FAK adhesion, and TLR2/6/CD14 macrophage activation in separate primary systems. Only the beta1-integrin result supports a direct binding-plus-relay row; VCAN/EGFR remains function-only and VCAN/TLR1 is no-evidence.
4. **VEGFA boundaries:** VEGFA directly engages alpha9beta1 and an alphaVbeta3/VEGFR2 signaling complex in primary endothelial studies. VEGFA/GRIN2B is retained as a VEGFR2-to-NR2B relay, not direct VEGFA-GRIN2B binding. VEGFA/EPHB2 is function-only because the primary studies use perturbation/cell-communication inference without direct binding. VEGFA/EGFR remains an explicit no-evidence boundary.
5. **UCN and receptor specificity:** UCN2 and UCN3 are canonically CRHR2 ligands. Weak/very-low-affinity CRHR1 binding is retained as binding-only, while no qualifying UCN2/IL10RB or UCN3/IL10RB evidence was located.

## Evidence discipline and limitations

Binding/activation, receptor-proximal relay, and downstream pathway/function are separate TSV fields. No direct interaction was inferred from pathway/function, expression, co-downregulation, fusion topology, receptor-family membership, or cell-communication prediction. Complex/subunit rows explicitly state when the direct evidence is for alpha9beta1, alphaVbeta3, or another multimer rather than the submitted subunit alone. Every row has populated limitations, and unresolved/no-evidence boundaries are explicit.

Primary stable citations are recorded in the TSV as PMID, PMCID, DOI, and bounded PubMed URL identifiers. Representative primary sources include TSLP receptor reconstitution (PMID 10974032; PMCID PMC2193276), taxilin/syntaxin binding (PMID 12558796), VASP/CXCR2 interaction (PMID 19435808), VCAM1/alpha9beta1 adhesion (PMID 10209034), versican/beta1-integrin binding (PMID 11805102), VEGFA/alpha9beta1 binding (PMID 17363377), VEGFA/NR2B modulation (PMID 21804034; PMCID PMC3158143), and VEGFA/alphaVbeta3 binding (PMCID PMC11128890).

## Validation and file scope

- The TSV has exactly the requested raw 13-column header and 25 data rows.
- Review IDs, pair labels, and order match the supplied queue exactly; IDs are unique.
- Every row has a stable citation field, populated limitations, and `terminal_TF=null`.
- Module20A files, shared Module21A registers, integration outputs, and database tables were not modified by this review.
- No commit was created.

## Files written

- `work/module21_relay/module21a_batch167_review.tsv`
- `work/module21_relay/module21a_batch167_summary.md`
