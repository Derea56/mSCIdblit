# Primary-evidence harvest from the public LR top-25 queue

This audit resolves the 25 highest-priority public-only ligand-receptor rows against the current mSCIdblit graph and the primary literature reviewed for this queue. It is a harvest/disposition record, not an mSCS confidence score and not a claim that every public database row is a valid direct ligand-receptor interaction.

The harvest adds three graph edges to the Module 21B source registers:

- GRP → NMBR, supported by primary mouse itch-circuit studies (PMID:25209280; PMID:29133874). The edge is functional and output-linked, but the branch is weaker than GRP → GRPR and has no asserted intracellular, TF, or target-gene layer.
- PTN → SDC1, supported at the biochemical glycosaminoglycan-binding layer by PMID:15226297.
- PTN → SDC4, supported at the biochemical glycosaminoglycan-binding layer by PMID:15226297.

The remaining rows were not converted into duplicate or over-specified edges. They resolve to existing entries under mature ligand/product names, processed complement fragments, aliases, species-corrected receptors, noncanonical interaction roles, or reverse adhesion orientation. PTN → SDC2 remains conditional because the primary evidence is Y-P30-enhanced binding rather than native PTN-alone binding. C4b → CR2 remains an unresolved boundary because the located evidence concerns complexed/opsonized antigen or does not isolate free C4b binding to endogenous CR2.

The complete row-level disposition is in [primary_evidence_harvest_resolution.tsv](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_database_comparison_v2/primary_evidence_harvest_resolution.tsv).
