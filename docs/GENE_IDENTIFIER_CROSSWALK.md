# Species-aware gene identifier crosswalk

The `mscs_release_bundle_v1_8_0_nichenet_tf_prior_gene_identifiers_v1` release adds a source-bound gene identifier layer to the existing mouse NicheNet and TF-target prior release. It is additive: the mechanism graph, NicheNet prior, and TF-target prior are copied from the pinned parent release without biological edge or confidence changes.

The crosswalk is built by `scripts/build_gene_identifier_crosswalk.py` from checksum-pinned NCBI GeneInfo snapshots for *Mus musculus* and *Homo sapiens*, plus the NCBI `gene_orthologs.gz` snapshot. The raw downloads remain external inputs; their exact URLs, local snapshot paths, byte sizes, and SHA-256 checksums are recorded in `gene_identifier_crosswalk/gene_identifier_crosswalk_manifest.json`.

Lookup is Unicode-preserving `casefold()` only. Canonical symbols and source-reported aliases are retained, while punctuation changes, substring matches, symbol similarity, and capitalization-based species conversion are not inferred. Ambiguous aliases remain multiple rows with `ambiguous_source_alias`; unresolved symbols remain rows with `unresolved_source_symbol` and no selected GeneID.

Species is explicit in every catalog and crosswalk row. For example, a mouse query `Tnf` resolves to mouse NCBI GeneID `21926` and Ensembl `ENSMUSG00000024401`; an unscoped `TNF` query retains separate mouse and human rows. Mouse-to-human rows are added only when an explicit NCBI `gene_orthologs.gz` record exists, and one-to-many orthology is retained without selecting an ortholog arbitrarily.

The generated standalone artifact contains:

- `gene_catalog.tsv`: source records for all mouse and human NCBI GeneInfo entries used by the crosswalk.
- `gene_crosswalk.tsv`: exact query-to-source mappings and explicit orthology projections, including source checksums and query provenance.
- `gene_orthology.tsv`: source-backed mouse-human orthology records with mapping cardinality.
- `gene_identifier_crosswalk_manifest.json`: schema, source, checksum, count, and limitation metadata.

Rebuild and validate with:

```bash
python3 scripts/build_gene_identifier_crosswalk.py
python3 scripts/build_mscs_gene_identifier_release.py
python3 scripts/validate_mscs_gene_identifier_release.py \
  --nichenet-artifact-root /path/to/pinned/nichenet/companion/root
```

The release does not convert identifiers in place, add graph edges, assign route confidence, or infer orthology. Downstream consumers must apply their own policy to ambiguous and unresolved mappings.
