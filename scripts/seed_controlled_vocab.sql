-- ============================================================================
-- mSCIdblit seed controlled vocabulary
-- Initial terms for Module 1A: chronic SCI lesion architecture
-- ============================================================================

INSERT INTO ControlledVocabulary_Species (species_name, ncbi_taxonomy_id, description) VALUES
  ('Mus musculus', '10090', 'Laboratory mouse'),
  ('Rattus norvegicus', '10116', 'Laboratory rat'),
  ('Cavia porcellus', '10141', 'Guinea pig'),
  ('Canis lupus familiaris', '9615', 'Domestic dog'),
  ('Sus scrofa', '9823', 'Pig'),
  ('Homo sapiens', '9606', 'Human')
ON CONFLICT (species_name) DO NOTHING;

INSERT INTO ControlledVocabulary_InjuryModel (model_name, anatomical_target, description) VALUES
  ('Thoracic contusion', 'T9-T10', 'Moderate to severe thoracic contusive SCI'),
  ('Dorsal hemisection', 'Thoracic', 'Dorsal partial transection injury'),
  ('Lateral hemisection', 'Thoracic', 'Lateral partial transection injury'),
  ('Complete transection', 'Thoracic', 'Complete spinal cord transection'),
  ('Compression', 'T10', 'Sustained or transient compression injury'),
  ('Human traumatic lesion', 'Variable', 'Human traumatic SCI pathology')
ON CONFLICT (model_name) DO NOTHING;

INSERT INTO ControlledVocabulary_LesionCompartment (compartment_name, anatomical_description) VALUES
  ('Lesion core', 'Central zone of tissue destruction'),
  ('Fibrotic core', 'Fibroblast-rich central region'),
  ('Astrocytic border', 'Glial scar boundary'),
  ('Reactive neural tissue', 'Altered but intact tissue surrounding lesion'),
  ('Spared white matter', 'Preserved white matter tracts at lesion periphery'),
  ('Spared gray matter', 'Preserved gray matter at lesion periphery'),
  ('Cystic cavity', 'Fluid-filled void within lesion'),
  ('Pericyte border', 'Mesenchymal cell zone'),
  ('Meningeal fibrosis', 'Dural or meningeal fibrotic involvement'),
  ('Remote spinal cord', 'Tissue rostral or caudal to lesion')
ON CONFLICT (compartment_name) DO NOTHING;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES
  ('Histological measurement', 'Quantitative measurement from tissue sections'),
  ('Immunohistochemistry', 'Labeled cellular or molecular identification'),
  ('Electron microscopy', 'Ultrastructural observation'),
  ('MRI measurement', 'Imaging-based quantification'),
  ('CT imaging', 'Imaging-based quantification'),
  ('Two-photon imaging', 'Live tissue visualization'),
  ('Confocal microscopy', 'High-resolution cellular imaging'),
  ('Serial section reconstruction', 'Three-dimensional computational reconstruction'),
  ('Qualitative histology', 'Descriptive anatomical characterization'),
  ('Human tissue examination', 'Autopsy or surgical specimen evidence')
ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_Assay (assay_name, assay_type, description) VALUES
  ('Lesion area measurement', 'histological', 'Quantification of lesion cross-sectional area'),
  ('Cavity volume quantification', 'histological', 'Quantification of cystic cavity volume'),
  ('GFAP immunostaining', 'immunohistochemical', 'Astrocytic border assessment'),
  ('Collagen staining', 'histological', 'Fibrotic scar assessment, including Masson trichrome'),
  ('White matter sparing quantification', 'histological', 'Measurement of preserved myelinated white matter'),
  ('Gray matter loss quantification', 'histological', 'Measurement of gray matter loss'),
  ('MRI T2-weighted lesion volume', 'MRI', 'Lesion volume assessment by T2-weighted MRI'),
  ('Voxel-based morphometry', 'MRI analysis', 'Imaging-based tissue loss analysis'),
  ('Eriochrome cyanine stain', 'histological', 'Myelinated axon and white matter staining'),
  ('Cellularity assessment', 'immunohistochemical', 'Cell density or cell identity assessment'),
  ('Western blot / immunoblot', 'molecular protein', 'Protein abundance or pathway-node assessment by western blot or immunoblot'),
  ('ELISA / cytokine protein assay', 'molecular protein', 'Cytokine, chemokine, or soluble-protein measurement'),
  ('qPCR / RT-PCR / mRNA assay', 'molecular transcript', 'Targeted transcript abundance measurement'),
  ('Flow cytometry / FACS', 'cellular profiling', 'Cell phenotyping, sorting, or abundance measurement by flow cytometry'),
  ('Single-cell RNA-seq / cell-state atlas', 'single-cell transcriptomic', 'Single-cell or single-nucleus transcriptomic cell-state profiling'),
  ('Spatial transcriptomics / spatial atlas', 'spatial transcriptomic', 'Spatial gene-expression or spatial cell-state mapping'),
  ('Bulk transcriptomics / GEO dataset', 'bulk transcriptomic', 'Bulk transcriptomic or public dataset-derived expression profiling'),
  ('Immunostaining / histology / pathology', 'histological', 'Tissue staining, immunolabeling, or pathology assessment'),
  ('Barrier / permeability / endothelial assay', 'vascular barrier', 'Blood-spinal cord barrier, endothelial, permeability, tight-junction, or MMP-associated readout'),
  ('Pathway activity / phospho-signaling assay', 'molecular signaling', 'Signaling pathway activity, phosphorylation, or regulatory-node readout'),
  ('Genetic perturbation / knockdown assay', 'mechanistic perturbation', 'Knockout, deficiency, siRNA, CRISPR, or related causal perturbation'),
  ('MRI / imaging assay', 'imaging', 'MRI or other imaging-based readout'),
  ('Behavioral / functional recovery assay', 'functional', 'Locomotor, neurologic, behavioral, or recovery endpoint')
ON CONFLICT (assay_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, measurement_unit, description) VALUES
  ('Lesion area', 'mm2', 'Cross-sectional lesion area'),
  ('Lesion length', 'mm', 'Rostrocaudal lesion length'),
  ('Lesion volume', 'mm3', 'Three-dimensional lesion volume'),
  ('Cavity volume', 'mm3 or percent of lesion', 'Cystic cavity volume'),
  ('White matter sparing', 'mm2 or percent', 'Preserved white matter'),
  ('Gray matter loss', 'mm2 or percent', 'Gray matter loss'),
  ('Lesion width', 'mm', 'Transverse lesion width'),
  ('Rostral extension', 'mm', 'Rostral lesion extent'),
  ('Caudal extension', 'mm', 'Caudal lesion extent')
ON CONFLICT (outcome_type_name) DO NOTHING;

INSERT INTO CurationPass (pass_code, pass_name, description, expected_table, sort_order) VALUES
  ('-1', 'Full text verification', 'Confirm full text, figures, legends, methods, and results are accessible.', NULL, -1),
  ('0', 'Paper registration', 'Register bibliographic metadata.', 'Paper', 0),
  ('1', 'Research questions', 'Extract explicit research questions and hypothesis direction.', 'ResearchQuestion', 1),
  ('2', 'Experimental paradigms', 'Extract study paradigms and methods strategies.', 'ExperimentalParadigm', 2),
  ('3', 'Experiments', 'Extract atomic experimental comparisons.', 'Experiment', 3),
  ('4', 'Observations', 'Extract atomic empirical findings with source provenance.', 'Observation', 4),
  ('5', 'Author claims', 'Extract author interpretations and link them to observations.', 'AuthorClaim', 5)
ON CONFLICT (pass_code) DO NOTHING;
