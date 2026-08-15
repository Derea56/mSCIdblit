# Module 21A Batch 160 review summary

Batch 160 covers exactly filtered queue ordinals 3451-3475 and the 25 requested Module 20A extension rows. The review IDs are the canonical Module 21A IDs `M21A-PAIR-004891` through `M21A-PAIR-004928` listed in the TSV. No Module 20A files, shared registers, or other batches were modified.

## Outcome

- `reviewed_relay_candidate`: 12
- `reviewed_binding_only`: 7
- `reviewed_unresolved`: 2
- `no_evidence_boundary`: 4
- terminal TF assignments: 0; every `terminal_TF` value is `null`

The relay-candidate calls are evidence-bearing but deliberately bounded. They include Serpine2-Lrp1, Sertad1-Ar, Sftpd-Lair1, Shank2-Cftr, Shbg-Gprc6a, the Shh-Gpc5/Lrp2/PTCH-SMO composite branches, Sirpa-Cd47, Slit1-Flrt3, and Slit2-App. Binding-only calls preserve a molecular association without upgrading it to receptor activation or downstream function. Unresolved and no-evidence calls explicitly prevent family-level, expression-level, or pathway-level annotations from becoming direct pair claims.

## Evidence-layer boundaries

1. Binding/activation is recorded only where the cited primary work supports a physical association, receptor engagement, or defined ligand-dependent activity.
2. Receptor-proximal relay is recorded separately for uptake, scaffold, ITIM, composite receptor-transducer, or receptor-crosstalk mechanisms.
3. Downstream pathway/function is recorded only for measured outputs such as ERK/beta-catenin, CFTR transport, secretion, phagocytosis, reporter activity, or axon guidance. Those outputs were not used to infer a direct interaction.

Specific composite boundaries retained in the TSV:

- `Shh PTCH1_SMO` and `Shh PTCH2_SMO` are composite receptor/transducer annotations. SHH binding is assigned to PTCH1/PTCH2; no direct SHH-SMO interaction is claimed.
- `Slit1 Flrt3` is a Robo1-FLRT3 cis-relay annotation. The cited primary study explicitly did not find direct Slit1-FLRT3 binding.
- `Slit2 Dcc` remains unresolved for the exact binary edge. The cited work supports Slit/Robo and DCC/Netrin crosstalk, not direct Slit2-DCC binding.
- `Sftpd Ly96` is limited to SP-D binding MD-2/LY96; TLR4 effects are treated as complex-level context.

## Main limitations

Most positive evidence comes from biochemical, heterologous, developmental, epithelial, immune, cancer, or axon-guidance systems rather than spinal-cord injury. Several edges require co-receptors or multiprotein complexes, and several functional results are cell-context dependent. No terminal TF was assigned because the reviewed sources did not provide a validated pair-specific terminal-TF relay suitable for Module 22A handoff. PubMed search URLs in the four no-evidence rows document the bounded search boundary; they are not positive evidence.

## Primary-source anchors

The TSV carries stable PMID, PMCID, DOI, or PubMed URLs for each evidence-bearing row. Representative anchors include SerpinE2-LRP1 (`PMID:36439874`), C1-INH-LRP1 (`PMID:9388254`), SFTPD-LAIR1 (`PMID:24585933`), Shank2-CFTR (`PMID:14679199`, `PMID:24445315`), SHBG-GPRC6A (`PMID:27673554`, `PMID:31857654`), SHH-GPC5 (`PMID:21339334`), SHH-LRP2 (`PMID:22340494`), SHH/PTCH-SMO (`PMID:30139912`, `PMID:29229834`), SIRPA-CD47 (`PMID:10572074`, `PMID:22451913`), Slit1-FLRT3 (`PMID:24560577`), Slit2-APP (`PMID:28785723`), and Slit2-GPC1 (`PMID:11375980`).
