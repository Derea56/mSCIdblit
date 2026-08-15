# Module 21A batch 082 review summary

## Scope

Reviewed the exact filtered priority-8 queue ordinal slice 1351–1375 from `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`. The slice contains 25 rows with review IDs `M20A-CELLCHAT-REMAINING-1488` through `-1513`; ID `-1498` is absent from the filtered queue, so the numeric span contains 25 actual records rather than 26.

The search covered PubMed, PMC, publisher pages, and stable database records. Primary research was prioritized. OSM receptor-complex evidence was evaluated separately from clustered protocadherin adhesion and neuronal self-recognition evidence. Family-level protocadherin homophily, a Pcdha4 result, or a solved representative beta isoform was not transferred to an unresolved exact heterophilic or distinct-isoform pair.

## Disposition

- 25 exact queue rows reviewed.
- 2 `reviewed_relay_candidate`: OSM–LIFR_IL6ST and OSM–OSMR_IL6ST.
- 16 `reviewed_binding_only`: clustered protocadherin alpha, PcdhaC2, and beta self-pairs with direct homophilic adhesion evidence.
- 7 `reviewed_unresolved`: Pcdha4b–Pcdha4, PcdhaC1–PcdhaC1, and five submitted Pcdhb heterophilic pairs.
- 0 `reviewed_function_only`.
- Terminal TF assignments were restricted to STAT3 for the two OSM receptor-complex rows, where receptor-proximal STAT3 phosphorylation was directly measured. No TF was assigned from protocadherin adhesion or neuronal self-recognition evidence.

## Evidence boundaries

- OSM–LIFR_IL6ST and OSM–OSMR_IL6ST are receptor-complex/pathway edges, not binary ligand-to-single-subunit claims. OSM receptor usage differs by species, ligand variant, receptor composition, and cell state. Direct JAK/STAT3 and ancillary MAPK/PI3K outputs were retained with those limitations.
- Alternate clustered Pcdha isoforms require carrier-dependent surface delivery in the main heterologous assays, but the exact alpha self-pairs in this batch are supported by the all-isoform homophilic survey. PcdhaC2 has additional mouse axonal-tiling functional evidence.
- PcdhaC1 is an explicit exception in the primary full-length aggregation assay and remains unresolved; an EC1–EC3 chimera was not treated as a full-length exact edge.
- Pcdha4b is a distinct mouse gene/readthrough annotation and was not conflated with Pcdha4.
- The five Pcdhb heterophilic rows remain unresolved. Primary clustered-Pcdh work supports strict isoform-specific homophilic recognition and mismatch exclusion, but absence from a positive pair-specific assay is not treated as proof of zero binding.
- No intracellular pathway or TF was inferred from protocadherin adhesion/self-recognition alone.

## Files changed

- `work/module21_relay/module21a_batch082_review.tsv`
- `work/module21_relay/module21a_batch082_summary.md`

No shared Module 21A registers, Module 20A ledgers, frozen manifest, or integration outputs were modified.
