# Module 21A Batch 198 review summary

Batch 198 reviews exactly the 25 supplied currently queued Module20A pairs in
`module21a_batch198_review.tsv`. Only this TSV and this summary are written by
the batch; the shared Module21A ledgers, Module22A handoff, Module20A LR
ledgers, and frozen LR manifest are untouched.

## Disposition

| status | count |
|---|---:|
| `reviewed_relay_candidate` | 16 |
| `reviewed_binding_only` | 6 |
| `reviewed_function_only` | 3 |
| **total** | **25** |

The relay-candidate records cover PAC1/ADCYAP1R1, AdipoR1/AdipoR2,
ADM-CALCRL/RAMP complexes, adenosine A1/A2A/A2B/A3 receptors, agrin-ATP1A3,
agrin-LRP4/MuSK complex signaling, AgRP-MC3R/MC4R inhibitory GPCR branches,
and AHSG-INSR inhibition. Binding-only records cover ADAM9-ITGB1,
AM2/IMD component-level CALCRL/RAMP1/RAMP2/RAMP3 rows, and albumin-FcRn.
Function-only records cover PACAP-VPAC1/VPAC2, where subtype-isolated PACAP
relay evidence was not recovered, and ADM-ACKR3 scavenging.

## Evidence decisions

- ADAM9-ITGB1 is retained as beta1-class integrin binding/adhesion evidence;
  alpha3beta1, alpha6beta1, and alphavbeta1 complex context is explicit, and
  no ITGB1-only intracellular relay is inferred.
- PACAP-PAC1 is supported by cAMP, ERK, receptor internalization/endosome,
  PLC/PKC, Src, neuritogenesis, and neuronal-excitability perturbation studies.
  PACAP-VPAC1 and PACAP-VPAC2 remain function-only because the strongest exact
  studies jointly express or perturb PAC1/VPAC1/VPAC2 and do not isolate a
  purified PACAP-to-VPAC1 or PACAP-to-VPAC2 relay.
- Adiponectin-AdipoR1/2 is supported by APPL1 interaction, AMPK, ERK, eNOS,
  PPARalpha, and metabolic perturbation evidence. Receptor coexpression and
  overlapping branch usage limit receptor-specific weighting.
- ADM-ACKR3 is represented as ligand scavenging/internalization that regulates
  CALCRL-RAMP ligand availability, not as a canonical G-protein relay.
  ADM-CALCRL, ADM-RAMP2, and ADM-RAMP3 retain their receptor-complex identity
  and direct cAMP evidence. AM2/IMD-CALCRL/RAMP component rows are binding-only:
  the primary structural evidence is for purified heteromeric complexes, not
  standalone component binding or an exact cellular terminal relay.
- Adenosine A1/A2A/A2B/A3 records retain subtype-specific G-protein, cAMP,
  PI3K/AKT, ERK/JNK, PLC/PKC, p38, and cellular-output evidence from primary
  receptor and native-cell studies. No universal TF endpoint is assigned.
- Agrin-ATP1A3 is a direct alpha3 Na+/K+-ATPase interaction with pump and
  cardiac-myocyte outputs. Agrin-LRP4 is the direct ligand/co-receptor edge;
  Agrin-MuSK is explicitly a receptor-complex relay and not a direct binary
  Agrn-Musk binding claim.
- AgRP-MC3R/MC4R records distinguish antagonism/inverse agonism from
  beta-arrestin endocytosis and context-dependent Gi/o signaling. AHSG-INSR is
  an inhibitory receptor-proximal interaction that blocks insulin receptor
  autophosphorylation and IRS-1 signaling. Albumin-FcRn is binding and
  pH-dependent recycling/transcytosis, not a kinase relay.

## Search boundary and validation

Searches covered exact ligand/receptor names and aliases across PubMed, PMC,
publisher records, and Europe PMC. Primary receptor-reconstitution,
biophysical, co-immunoprecipitation, pharmacology, genetic, inhibitor,
knockdown, and native-cell perturbation studies were retained when they
matched the exact pair or an explicitly documented receptor-complex context.
Reviews, expression-only observations, generic family annotations, and
pathway analogy were used only to define limitations or search boundaries.

Before any ledger integration, this packet must pass: 25 data rows; unique
review IDs and pair labels; exact 13-column schema; populated required fields;
confidence vocabulary `high|medium-high|medium|medium-low|low`; and literal
`terminal_TF=null` for every row because no direct terminal-TF endpoint was
validated for these exact pair rows.
