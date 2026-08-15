# Module 21A batch 100 review summary

Reviewed the exact filtered priority-8 queue ordinals 1801–1825 from `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`.

## Scope validation

- 25 exact rows were written and validated.
- Queue IDs and pair labels match the requested filtered slice exactly: `M20A-EXT-0903` through `M20A-EXT-0926`, then `M20A-EXT-0928`.
- `M20A-EXT-0927` is not present in this filtered ordinal slice; later BMP10–ENG/FFAR2/GPR152 rows were not added.
- The TSV has the required 13-column header, 25 unique review IDs, no blank required fields, and one row per exact queue ID.

## Disposition

- 4 `reviewed_relay_candidate`: B2M–HFE, BDNF–ERBB2, BGN–TLR2, and BGN–TLR4.
- 3 `reviewed_binding_only`: AZGP1–ITGAV, BMP10–ACVR2A_ACVRL1, and BMP10–ACVR2B_ACVRL1.
- 2 `reviewed_function_only`: B2M–TFRC and BCAN–EGFR.
- 16 `reviewed_unresolved`: AVP–TSHR/VIPR1; B2M–CD247/CD3D/CD3G/KLRC1/KLRD1; BCAN–NRCAM; BDNF–DRD4/GPR152; BGN–LY96/TLR1; BMP1–BMPR1A/B/BMPR2; and BMP10–BMPR1B.
- One terminal TF is recorded: `HIF1A` for the B2M–HFE cancer-cell iron/HIF-1-alpha branch. No TF was transferred to other B2M, BGN, ECM, neurotrophin, or BMP rows.

## Evidence boundaries

- B2M was separated from the MHC-I heavy-chain or MHC-E presenting complex. CD3 and CD94/NKG2A components were not treated as direct B2M receptors. B2M–HFE is supported as a direct complex with HFE-dependent TFRC/iron regulation and HIF-1-alpha/EMT output; B2M–TFRC remains function-only because the TFRC effect is mediated through HFE.
- BCAN–EGFR is retained only at the functional layer for an ADAMTS-cleaved brevican fragment associated with EGFR activation and glioma motility. Direct full-length BCAN–EGFR binding was not inferred, and brevican–NrCAM remained unresolved.
- BGN–TLR2 and BGN–TLR4 retain direct endogenous-ligand and receptor-proximal MAPK/NF-kappaB evidence from primary macrophage and mouse inflammatory studies. BGN–LY96 and BGN–TLR1 were not promoted from TLR4 accessory or TLR-family context.
- BMP1 was treated as an astacin-like extracellular metalloprotease, not as a canonical BMP/TGF-beta ligand. BMP1 ECM and growth-factor processing evidence was not transferred to BMPR1A, BMPR1B, or BMPR2.
- BMP10–ACVR2A_ACVRL1 and BMP10–ACVR2B_ACVRL1 retain exact type-I/type-II receptor-component binding evidence, but no matched exact-complex cellular SMAD assay or TF endpoint was promoted. BMP10–BMPR1B remains unresolved; ALK1/type-II evidence was not transferred to ALK6/BMPR1B.

## Search boundary

Searches covered PubMed, PMC full text, publisher pages, and pathway/structure context for the exact pair names and receptor aliases, with primary studies retained where available. No-evidence cases retain stable PubMed search URLs and comparator citations so that absence is auditable rather than silently omitted.

No shared Module 21A registers, Module 20A ledgers, frozen manifest, or integration outputs were modified.
