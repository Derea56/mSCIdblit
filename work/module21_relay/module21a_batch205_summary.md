# Module 21A batch 205 summary

## Scope

This batch reviews exactly the 25 queued Module20A external-review pairs
M20A-EXT-1353 through M20A-EXT-1377. Pair labels are preserved verbatim. The
review separates ligand–receptor binding or activation, receptor-proximal
relay, and downstream pathway or cellular-function evidence. Only the two
batch-205 artifacts were written; no Module20A or Module21A ledger, frozen
manifest, saturation register, or SQL file was edited.

## Disposition

- 25 exact pair rows were written.
- 9 rows are `reviewed_relay_candidate`.
- 3 rows are `reviewed_binding_only`.
- 1 row is `reviewed_function_only`.
- 12 rows are `no_evidence_boundary`.
- One provisional Module22A endpoint was recorded: `CREB` for the CRH–CRHR1
  branch because the primary olfactory-bulb study explicitly describes
  CRHR1-dependent CREB transcription. All other `terminal_TF` fields are the
  literal `null`.

## Positive evidence

The batch contains direct or bounded extracellular evidence for MAG binding to
type IX collagen, COLQ binding to MuSK in the perlecan-containing
neuromuscular-junction complex, and COMP/TSP5 interaction with chondrocyte
alpha5beta1 integrin. These are not promoted to intracellular relay edges
when the primary work shows adhesion or anchoring without kinase activation.

Cortistatin was treated as the likely meaning of the Module20A `Cort` token.
Primary recombinant-receptor studies support binding and adenylate-cyclase
inhibition at SSTR1–5. Cortistatin also has primary receptor and functional
evidence for GHSR1a and human MRGPRX2, including G-protein coupling and
mast-cell calcium/SOCE outputs. The `Cort-Mrgprb1` row remains unresolved
because the positive mouse orthologous mast-cell receptor is generally
MrgprB2, not MrgprB1.

Ceruloplasmin–SLC40A1 is recorded as function-only: ceruloplasmin ferroxidase
activity supports ferroportin-mediated iron export and surface stability, but
the primary studies do not establish a physical Cp–ferroportin interaction or
a receptor-proximal kinase relay.

CRH–CRHR1 is supported by receptor-proximal cAMP/PKA, beta-arrestin/MAPK, and
context-dependent cellular outputs. CRH–CRHR2 is supported by cAMP and
CRHR2-antagonist-sensitive neuronal/cardiovascular responses, with the
co-release of glutamate retained as a limitation. No terminal TF was assigned
to CRHR2.

## Search boundary and limitations

Searches covered exact submitted symbols and principal aliases across PubMed,
PMC, publisher records, and primary receptor/pharmacology literature. The
COPA rows remain explicit boundaries because COPA is characterized as a
cytosolic COP-I coatomer subunit, not a secreted ligand. The noncognate
cortistatin rows (ADRA2A, GRM7, Mrgprb1, MTNR1A) and noncognate CRH rows
(ADCYAP1R1, ADRB2, ADRB3, GPR20) retain comparator citations and PubMed search
URLs but were not promoted by family-level or pathway analogy. The exact
ligand identity of `Cort` must be checked against the Module20A naming source;
the positive cortistatin rows are not transferable if the token instead means
corticosterone.

## Validation target

The TSV must contain exactly 25 data rows, the exact 13-column schema,
unique review IDs and pair labels, populated required fields, allowed
confidence values, exact requested pair order, and literal `null` in every
unvalidated terminal-TF field. No materialized ledger edge is created in this
batch.
