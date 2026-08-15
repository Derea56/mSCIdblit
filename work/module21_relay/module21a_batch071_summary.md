# Module 21A batch 071 review summary

## Scope

- Exact queue IDs reviewed: `M20A-CELLCHAT-REMAINING-1168` through `M20A-CELLCHAT-REMAINING-1192`.
- The queue file has an ordinal/index mismatch: ordinal rows 1076–1100 are Glu/SLC1A6 rows, while the requested IDs 1168–1192 are the H2 partition specified by the task. This batch follows the explicit review-ID range and H2-Bl/H2-D/H2-D1/H2-Ea/H2-K1/H2-L/H2-M1/H2-M10.x content.
- Exactly 25 rows were written, one per requested review ID.

## Disposition

- `reviewed_relay_candidate`: 0
- `reviewed_function_only`: 0
- `reviewed_binding_only`: 0
- `reviewed_unresolved`: 25
- Terminal TF assignments: 0

The unresolved disposition is deliberate. Family-level MHC-I/CD8 binding, MHC-I/Ly49 recognition, and MHC-II/CD4 co-receptor biology were not promoted to exact submitted edges where the chain, allele, receptor subtype, or assembled complex was not directly tested.

## Evidence findings

1. MHC-I/CD8: primary SPR and structural studies support CD8 binding to defined mouse MHC-I molecules, including H-2D(d), H-2K(b), and an unusual peptide-deficient H-2L(d) interaction. They do not establish every submitted H2 gene product with the individual CD8A or CD8B1 edge. H2-L was retained as unresolved because the direct H-2L(d) result is peptide-occupancy dependent and is not equivalent to mature pMHC-driven receptor activation.
2. MHC-I/Klra: primary mouse studies resolve Ly49A or Ly49D with defined H-2D(d) contexts. The queue’s `Klra` receptor label and submitted H2-D/H2-K1 entities do not identify an exact receptor subtype/allele pair.
3. H2-D1/Kir3dl1 and H2-K1/Kir3dl1: primary KIR3DL1 evidence is for human HLA-Bw4 and defined human KIR3DL1 allotypes. No mouse H2-D1 or H2-K1 cross-species edge was promoted.
4. H2-Ea/Cd4: H2-Ea is the MHC-II alpha chain. CD4 evidence maps to the assembled MHC-II complex and prominently to beta-chain regions; the alpha-chain-only pair is therefore a receptor-complex boundary, not a direct ligand edge.
5. H2-M1/H2-M10.x/CD8: primary M1/M10 evidence concerns V2R association, escort function, and vomeronasal receptor trafficking. No direct CD8 binding, receptor-proximal relay, downstream pathway, or TF evidence was found for the submitted pairs.

## Search boundaries

Searches covered PubMed, PMC, publisher pages, and primary structural/biophysical and cell-based studies using exact gene names, allele names, receptor-family expansions, and ortholog/cross-species controls. Evidence was retained when it clarified why a candidate could not be promoted, but family-level, transcriptomic, pathway-only, antigen-presentation-only, or functional association evidence was not converted into a direct molecular edge.

## Files changed

- `work/module21_relay/module21a_batch071_review.tsv`
- `work/module21_relay/module21a_batch071_summary.md`

No shared Module 21A registers, Module 20A ledgers, frozen manifest, or integration outputs were modified.

## Stable primary citations used

- PMID 19625641 / PMCID PMC2782705 — CD8αβ–H-2D(d) structure and SPR.
- DOI 10.4049/jimmunol.160.6.2809 — direct peptide-deficient H-2L(d)–CD8 interaction.
- PMID 10809759 — class I/CD8 binding comparison.
- PMID 11148219; PMID 11513135; PMID 11696552 — defined Ly49/MHC-I interactions.
- PMID 12370253; PMID 21471246; PMID 21746965 — KIR3DL1/HLA-Bw4 binding and function.
- PMID 1552288; PMID 8432982 — CD4/MHC-II interaction mapping.
- PMID 12628182; PMID 16089503; PMID 18322080; PMCID PMC3189042 — M1/M10/V2R association, structure, and trafficking.
