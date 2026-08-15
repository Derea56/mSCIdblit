# Module 21A Batch 199 review summary

Batch 199 reviews exactly the 25 supplied currently queued Module20A pairs
using the established 13-column schema in
`module21a_batch199_review.tsv`. Only this TSV and this summary are written by
the batch; shared Module20A/21A ledgers and the frozen LR manifest are
untouched.

## Disposition

| status | count |
|---|---:|
| `reviewed_relay_candidate` | 18 |
| `reviewed_scavenging_only` | 4 |
| `reviewed_binding_only` | 1 |
| `no_evidence_boundary` | 2 |
| **total** | **25** |

Confidence counts: high 1; medium-high 16; medium 6; low 2. One row carries
an explicit provisional terminal-TF endpoint (`SMAD1;SMAD5;SMAD8` for the
AMH–AMHR2/ACVR1 receptor-complex branch), and one carries a beta-catenin
coactivator endpoint (`CTNNB1` for the cANGPTL4–CDH11 cadherin-catenin
complex). All other rows use literal `null`.

## Evidence decisions

- Albumin–LRP2 and amelogenin–CD63/LAMP1/LAMP2 were kept as
  `reviewed_scavenging_only`: the primary evidence supports binding,
  receptor-associated uptake, vesicle trafficking, or matrix-protein
  clearance rather than a canonical kinase relay.
- ALCAM–CD6, AMBN–CD63, AMH–AMHR2/ACVR1, ANG–EGFR, ANG–PLXNB2,
  ANGPT–integrin/TIE, and ANGPTL integrin/PIRB records were promoted only
  where primary binding, receptor-proximal perturbation, or receptor-dependent
  pathway/function evidence was available. Receptor-complex and
  receptor-family context is stated explicitly in the limitations.
- ANGPT2–TIE1 remains an explicit `no_evidence_boundary`: primary studies
  support Ang1- or Ang4-associated Tie1 phosphorylation and Ang2–Tie2
  context, but did not establish the submitted exact Ang2–Tie1 branch.
- ALCAM–CHL1 remains an explicit `no_evidence_boundary`; ALCAM–CD6 and
  generic neural/Ig-superfamily adhesion evidence were not transferred to
  CHL1.
- ANGPTL4–CDH11 and ANGPTL4–CDH5 retain their distinct cadherin-complex
  semantics. CDH11 has direct binding plus a beta-catenin/ID3 functional
  branch; CDH5 is recorded as binding-only because Rac1/PAK activation was
  assigned to the parallel alpha5beta1 branch rather than to CDH5 itself.
- The related ANGPTL1 HCC paper with PMID 28904065 was excluded because the
  PubMed record documents a retraction; the independent lung-cancer primary
  study (PMID 23434592; PMCID PMC3582121) was retained for ANGPTL1–alpha1beta1.

## Search boundary and validation

Searches covered exact ligand/receptor names and aliases across PubMed, PMC,
publisher pages, Europe PMC/Reactome records, and primary receptor-signaling,
adhesion, uptake, and perturbation literature. Reviews, expression-only
observations, generic receptor-family annotations, and comparator-family
results were used only to define boundaries and were not promoted to direct
exact-pair edges. Recent primary evidence was retained only with its model and
receptor-composition limitations stated.

Before any ledger integration, this packet must pass: 25 data rows; exact
alignment to the supplied IDs and labels; unique review IDs and pair labels;
exact 13-column schema; populated required fields; confidence vocabulary
`high|medium-high|medium|medium-low|low`; and `terminal_TF` either an explicit
endpoint or literal `null`. No Module20A or shared Module21A ledger files were
modified.
