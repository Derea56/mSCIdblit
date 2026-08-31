# Module 22A: TF → Target Gene Databases — Phase 1 Discovery Summary

**Date:** 2026-08-05  
**Scope:** Mouse + Human only  
**Goal:** Curated TF → target gene regulation databases (not motifs)

---

## PRIMARY DATABASE FOUND AND DOWNLOADED

### DoRothEA v1.0 — **CONFIRMED WORKING ✅**

**URL:** https://github.com/saezlab/dorothea  
**Bioconductor:** Dorothea (Release 3.19)  

**What it provides:** Curated TF→target gene regulation network with confidence levels A-E (A=highest evidence from multiple orthogonal sources like ChIP-seq, ATAC-seq, RNA-seq; E=lowest/single-source predictions)

**Downloaded files:**
| File | Species | Interactions | Size |
|------|---------|-------------|------|
| `dorothea_mm.rda` | Mouse | 386,758 | 714 KB |
| `dorothea_hs.rda` | Human | 454,504 | 895 KB |
| `tf_annotation.rds` | — | TF symbol metadata | 5.9 KB |

**Data structure (TSV):**
```
tf              confidence    target          mor
4932411N23Rik   E             Smad4           1
ADNP            D             ATF7IP          1
PAX6            A             SOX2            1
```

- `tf`: TF gene symbol (mouse or human)
- `confidence`: A/B/C/D/E evidence grade
- `target`: Target gene symbol
- `mor`: Binary flag (-1 or 1) — likely regulation direction or evidence consistency

**Confidence distribution (human):**
- **A**: 5,434 interactions (strongest: multi-source ChIP/ATAC/RNA-seq)
- **B**: 974
- **C**: 6,815
- **D**: 15,863
- **E**: 425,418 (lowest: predicted/computational)

**Top TFs by target count:** PRRX2 (1,437), MTF1 (1,431), TCF7L1 (1,431), NFATC3 (1,401), FOXJ3 (1,398)

---

## SECONDARY DATABASE — WORKING ✅

### JASPAR API (`jaspar.elixir.no/api/v1/`)
- **Provides:** TF binding motifs (PWMs), NOT direct TF→gene relationships
- **Use case:** When you need motif sequences to predict which promoters a TF can bind
- 4,572 CORE matrices for vertebrates; 5,935 total including unvalidated
- API endpoint: `GET /api/v1/matrix/?ncbi_tax_id=9606&page=1` (human), `ncbi_tax_id=10090` (mouse)

### REMap (`remap.univ-amu.fr`)
- **Provides:** ChIP-seq derived TF peak locations in BED format (not pre-mapped to genes)
- **Human hg38:** 182.4M all-sites, 68.2M non-redundant
- **Mouse mm10:** 123.2M all-sites, 43.9M non-redundant
- **Use case:** Map peaks to nearest genes for TF→target inference

---

## DNS-BLOCKED FROM THIS HOST (cannot reach)

| Database | What it provides | Why needed |
|----------|-----------------|------------|
| **TRRUST v3** (`www.trrust.kr`) | Curated TF→target interactions with activation/repression directionality for human & mouse | Priority #2 — provides the same data as DoRothEA but with different evidence curation |
| **DoOR 3** (`dor2.cpfs.nrc-cnrc.gc.ca`) | Gene regulatory relationships from ChIP-seq + literature | Independent source for cross-validation |
| **ChIP-Atlas** (`www.chip-atlas.org`) | Cross-species ChIP-seq → target gene mapping | Provides tissue-specific TF binding evidence |

---

## RECOMMENDED NEXT STEPS FOR MODULE 22A

### Phase 1b: Download & Process DoRothEA
1. Move `/tmp/dorothea_mm_tfgene.tsv` and `/tmp/dorothea_hs_tfgene.tsv` into the repo
2. Filter to confidence A-C for high-confidence interactions (only ~23K human, ~23K mouse)
3. Cross-validate against JASPAR motifs (which TFs actually have binding motifs vs just predicted targets)
4. Map TF→target pairs into Module 22A tracker format

### Phase 1c: Alternative sources
- Try TRRUST v3 from another machine/network (DNS blocks this host)
- Extract TF-gene relationships from WikiPathways pathways relevant to SCI/immune/signaling
- Check if Reactome has TF→gene cascade edges accessible via alternative endpoints

### Phase 2: Validation with primary resources
- Map DoRothEA interactions to ChIP-seq data (REMap) for independent confirmation
- Cross-check against TRRUST when accessible
- Filter by SCI-relevant cell types/tissues using MGI and ENCODE data
