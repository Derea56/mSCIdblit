-- Explicit NFKB1 component, TNF pathway membership, and a lightweight
-- evidence-backed core regulon.
--
-- Apply after:
--   schema/schema.sql
--   schema/mechanism_roles_layer.sql
--   schema/mechanism_register_layer.sql
--   schema/regulon_layer.sql
-- and after the Module 20-24 graph bundle has been loaded.
--
-- This migration deliberately keeps IKK-NFKB1-RELA as a signaling-cascade
-- node. The NFKB1 and RELA mappings are non-activating component mappings.
-- Pathway membership makes the TF association queryable without inventing a
-- standalone TNFR-to-NFKB1 activation edge.

BEGIN;

DO $$
BEGIN
  IF to_regclass('public.regulon') IS NULL
     OR to_regclass('public.regulonmember') IS NULL
     OR to_regclass('public.regulonmembersource') IS NULL THEN
    RAISE EXCEPTION
      'NFKB1 layer requires schema/regulon_layer.sql to be applied first';
  END IF;
END $$;

CREATE TEMP TABLE nfkb1_core_targets (
  symbol TEXT PRIMARY KEY,
  effect_polarity TEXT NOT NULL,
  pmids TEXT NOT NULL
) ON COMMIT DROP;

INSERT INTO nfkb1_core_targets (symbol, effect_polarity, pmids) VALUES
  ('BCL2A1', 'activating', '11880364;12665576;19343319;10733571;17000776'),
  ('BCL2L1', 'context_dependent', '12226754;14978135;15756023;15856023;15986355;16904634;18223231;20066113;15231833;10733571;10925251;12176906;14739605;16453001;17673602;18222423'),
  ('BIRC2', 'context_dependent', '12010810;15756023;18566231;12687011;15050749;16453001;17673602;20103608'),
  ('BIRC3', 'context_dependent', '10733571;11297551;11880364;12010810;19343319;15231833;15723831;18566231;10823821;15050749;17000776;17673602'),
  ('CCL2', 'activating', '10530453;11512674;12488502;12647268;16206198;16764699;20200316;9388261;10744656;11006087;11949945;12218154;14631383;15950427;16040075;16818736;8617886'),
  ('CCL5', 'activating', '11478739;9120310;11259372;11389171;11413310;12122011;19786024'),
  ('CXCL1', 'activating', '10530453;15958549;11112786;16040075;7479086'),
  ('CXCL2', 'unknown', '17363596'),
  ('CXCL8', 'context_dependent', '10506755;10530453;11297551;11512674;11564889;12058956;15350531;15387324;15688424;15958549;16701870;16764699;17040605;17041011;17917246;18074095;18996370;22340043;7876168;15517885;8413215;10477716;11120852;11342414;11953364;12218154;12485925;12643600;12707271;12716652;14631383;14670967;15289496;15950427;16004996;16105834;16803583;17045242;18281166;19376732;19732956;19786024;19837667;8878392;9698090'),
  ('ICAM1', 'activating', '10092659;10946302;11463837;11877286;16317091;16385502;17121934;19074768;20173029;22001597;22708120;9733827;9916895;10738944;10837365;10926553;11198351;11401521;12490396;12691701;15480988;15800027;15843586;16105834;16453001;18285351;18928584;20103608;9192770'),
  ('IFNB1', 'activating', '10074115;12077266;17496231;15955070;16125763;17079305'),
  ('IL1B', 'activating', '12686724;14960579;8413223;8679226;9878621;10080875;10963848;16433741;17707233;18285351;20336759;9058643'),
  ('IL6', 'context_dependent', '10329846;10903137;11327783;11504280;12058956;12887736;14532843;15756023;16984731;17040605;17196927;18057724;18061164;18243142;18942706;18996370;19124729;19164127;20066113;22547075;7876168;8679226;8725624;10823821;10963848;11120852;11975924;15158360;16112536;17490702;17532054;19469019;19707556;2405250;8752656;15517885'),
  ('NFKBIA', 'context_dependent', '12885753;11744993;10454561;15499023;17876798'),
  ('TNF', 'activating', '10079106;10748079;11749970;12058956;12686724;15013838;16707469;16916598;17407192;18057724;20066113;7876168;8219230;8679226;10551799;10837498;10963848;11297551;14960579;15812247;16040075;16433741;17442180;17707233;18285351;20237317;9916895'),
  ('TNFAIP3', 'activating', '11880364;19343319;10807933'),
  ('VCAM1', 'activating', '10329958;10946302;11359843;16271621;16317091;16385502;19281832;19422386;22708120;10553096;10833420;16453001');

CREATE TEMP TABLE nfkb1_cascade_handoffs (
  source_name TEXT NOT NULL,
  pathway_name TEXT NOT NULL,
  register_edge_id TEXT PRIMARY KEY,
  evidence_ids TEXT NOT NULL
) ON COMMIT DROP;

INSERT INTO nfkb1_cascade_handoffs (source_name, pathway_name, register_edge_id, evidence_ids) VALUES
  ('TNFR1/p55 receptor', 'TNF-NF-kappaB-MAPK-death', 'M21B-NFKB1-CASCADE-TNFR1', 'M21B-EVID-000053;M21B-EVID-000004'),
  ('TNFR2 receptor complex', 'TNFR2-TRAF2-NF-kappaB', 'M21B-NFKB1-CASCADE-TNFR2', 'M21B-EVID-000054;M21B-EVID-000021');

INSERT INTO SignalingEntity (
  canonical_name, entity_type, gene_symbol, organism_scope, aliases, notes
)
VALUES (
  'NFKB1',
  'transcription_factor',
  'NFKB1',
  'human; mouse',
  'NF-kB1; NF-κB p105/p50',
  'Explicit gene-level TF component of the IKK-NFKB1-RELA composite; activation and target membership are separately evidenced.'
)
ON CONFLICT (canonical_name) DO NOTHING;

INSERT INTO SignalingEntityRole (
  entity_id, role, role_status, role_source, role_evidence,
  source_registry, source_version, export_priority
)
SELECT
  entity_id,
  'transcription_factor',
  'curated',
  'TRRUST_v2_and_TNF_branch_normalization',
  'NFKB1 is an explicit TF record in TRRUST v2 and is named in the TNF-pathway composite IKK-NFKB1-RELA; this role does not by itself assert TNF activation.',
  'TRRUST; mSCIdblit_module20_24',
  '2018-04-16;2026-08-25',
  'high'
FROM SignalingEntity
WHERE canonical_name = 'NFKB1'
ON CONFLICT (entity_id, role) DO NOTHING;

INSERT INTO SignalingPathway (
  pathway_name, pathway_class, description, source_registry, notes
)
VALUES (
  'NFKB1-core-regulon',
  'transcriptional_regulon',
  'Lightweight human NFKB1 target summary drawn from the TRRUST v2 literature-curated target table.',
  'TRRUST',
  'Core summary only; it is not an exhaustive NFKB1 regulon and does not imply TNF-specific regulation in every cell type.'
)
ON CONFLICT (pathway_name) DO NOTHING;

DO $$
DECLARE
  nfk_id INTEGER;
  rel_a_id INTEGER;
  composite_id INTEGER;
  target_row RECORD;
  target_id INTEGER;
  selected_pathway_id INTEGER;
  db_edge_id INTEGER;
  member_id INTEGER;
  regulon_pk INTEGER;
  component RECORD;
  cascade_handoff RECORD;
  pathway_name_row RECORD;
  synthetic_edge_id TEXT;
  synthetic_evidence_id TEXT;
  member_effect TEXT;
BEGIN
  SELECT entity_id INTO nfk_id FROM SignalingEntity WHERE canonical_name = 'NFKB1';
  SELECT entity_id INTO rel_a_id FROM SignalingEntity WHERE canonical_name = 'RELA';
  SELECT entity_id INTO composite_id FROM SignalingEntity WHERE canonical_name = 'IKK-NFKB1-RELA';

  -- These memberships make the TF association queryable without asserting
  -- that TNF activates NFKB1 in every receiver cell.
  FOR pathway_name_row IN
    SELECT pathway_name
    FROM (VALUES
      ('TNF-NF-kappaB'),
      ('TNFR2-NF-kappaB-JNK'),
      ('TNF-NF-kappaB-MAPK-death'),
      ('TNFR2-TRAF2-NF-kappaB')
    ) AS pathways(pathway_name)
  LOOP
    SELECT pathway.pathway_id INTO selected_pathway_id
    FROM SignalingPathway AS pathway
    WHERE pathway.pathway_name = pathway_name_row.pathway_name;

    IF selected_pathway_id IS NULL THEN CONTINUE; END IF;

    INSERT INTO SignalingPathwayMember (
      pathway_id, entity_id, member_role, ordinal, membership_status, notes
    ) VALUES (
      selected_pathway_id, nfk_id, 'transcription_factor', 90, 'supported',
      'Pathway-associated NFKB1 component of the IKK-NFKB1-RELA/NF-kappaB branch; not a direct TNFR-to-NFKB1 activation assertion.'
    ) ON CONFLICT (pathway_id, entity_id) DO NOTHING;

    IF rel_a_id IS NOT NULL THEN
      INSERT INTO SignalingPathwayMember (
        pathway_id, entity_id, member_role, ordinal, membership_status, notes
      ) VALUES (
        selected_pathway_id, rel_a_id, 'transcription_factor', 91, 'supported',
        'Pathway-associated RELA component of the IKK-NFKB1-RELA/NF-kappaB branch; not a direct TNFR-to-RELA activation assertion.'
      ) ON CONFLICT (pathway_id, entity_id) DO NOTHING;
    END IF;
  END LOOP;

  -- Preserve the supported TNF-receptor-to-composite cascade continuity in
  -- the exported graph. This is deliberately not an activation edge and does
  -- not assert direct receptor-to-TF contact.
  FOR cascade_handoff IN SELECT * FROM nfkb1_cascade_handoffs LOOP
    SELECT edge.edge_id INTO db_edge_id
    FROM SignalingEdge AS edge
    JOIN SignalingEntity AS source ON source.entity_id = edge.source_entity_id
    JOIN SignalingEntity AS target ON target.entity_id = edge.target_entity_id
    WHERE source.canonical_name = cascade_handoff.source_name
      AND target.canonical_name = 'IKK-NFKB1-RELA'
      AND edge.pathway_id = (
        SELECT pathway.pathway_id
        FROM SignalingPathway AS pathway
        WHERE pathway.pathway_name = cascade_handoff.pathway_name
      )
      AND edge.relation_type = 'supports_cascade'
    LIMIT 1;

    IF db_edge_id IS NULL THEN
      INSERT INTO SignalingEdge (
        source_entity_id, target_entity_id, pathway_id, relation_type,
        effect_polarity, species_context, compartment_context,
        evidence_status, context_scope, export_priority, notes
      )
      SELECT
        source.entity_id,
        composite_id,
        pathway.pathway_id,
        'supports_cascade',
        'unknown',
        'human; mouse',
        'receptor-proximal signaling to nucleus',
        'pathway_handoff_support',
        'Pathway continuity from the TNF receptor record to the existing IKK-NFKB1-RELA cascade node; not direct receptor-to-TF binding.',
        'medium',
        'This edge joins companion pathway labels so the supported TNF cascade is traversable without splitting the composite node into an unsupported activation claim.'
      FROM SignalingEntity AS source
      JOIN SignalingPathway AS pathway
        ON pathway.pathway_name = cascade_handoff.pathway_name
      WHERE source.canonical_name = cascade_handoff.source_name
      RETURNING SignalingEdge.edge_id INTO db_edge_id;
    END IF;

    INSERT INTO SignalingEdgeRegister (
      edge_id, register_edge_id, module, source_label, target_label,
      register_relation_type, graph_relation_type, pathway_name,
      evidence_layer, edge_status, confidence_tier, evidence_ids,
      consolidation_note
    ) VALUES (
      db_edge_id,
      cascade_handoff.register_edge_id,
      '21B',
      cascade_handoff.source_name,
      'IKK-NFKB1-RELA',
      'supports_cascade',
      'supports_cascade',
      cascade_handoff.pathway_name,
      'pathway_handoff',
      'supported',
      'medium',
      cascade_handoff.evidence_ids,
      'Pathway-continuity edge; not a direct receptor-to-TF activation assertion.'
    ) ON CONFLICT (register_edge_id) DO NOTHING;

    INSERT INTO SignalingEdgeRegisterSource (
      edge_id, register_edge_id, register_evidence_id, module,
      support_kind, species_support, source_scope, confidence_tier,
      citation_note, notes, source_kind, source_locator,
      source_locator_status, evidence_summary, limitations,
      evidence_layer, evidence_exportable, consolidation_note
    ) VALUES (
      db_edge_id,
      cascade_handoff.register_edge_id,
      cascade_handoff.register_edge_id || '-SOURCE',
      '21B',
      'primary_experiment',
      'both',
      'pathway_membership',
      'medium',
      'Reuses matched TNF receptor and NF-kappaB branch evidence IDs: ' || cascade_handoff.evidence_ids,
      'Companion-label normalization for the supported cascade path.',
      'mSCIdblit_register_reuse',
      'mSCIdblit://module20_24/register/' || cascade_handoff.evidence_ids,
      'stable_internal_register',
      'TNF receptor engagement is linked to the IKK-NFKB1-RELA NF-kappaB branch at pathway level.',
      'Does not assert direct physical receptor-complex binding to the composite node or independent NFKB1 activation.',
      'pathway_handoff',
      TRUE,
      'Original evidence remains separately available on the Module 21B receptor and branch records.'
    ) ON CONFLICT (edge_id, register_evidence_id) DO NOTHING;
  END LOOP;

  -- Decompose the composite label while keeping the edge non-activating.
  FOR component IN
    SELECT nfk_id AS component_id, 'NFKB1'::TEXT AS component_name
    UNION ALL
    SELECT rel_a_id, 'RELA'
  LOOP
    IF component.component_id IS NULL OR composite_id IS NULL THEN CONTINUE; END IF;

    synthetic_edge_id := 'M21B-NFKB1-COMPONENT-' || lower(component.component_name);
    synthetic_evidence_id := synthetic_edge_id || '-SOURCE';

    SELECT edge.edge_id INTO db_edge_id
    FROM SignalingEdge AS edge
    WHERE edge.source_entity_id = composite_id
      AND edge.target_entity_id = component.component_id
      AND edge.relation_type = 'contains_component'
      AND edge.pathway_id = (
        SELECT pathway_id FROM SignalingPathway WHERE pathway_name = 'TNF-NF-kappaB'
      )
    LIMIT 1;

    IF db_edge_id IS NULL THEN
      INSERT INTO SignalingEdge (
        source_entity_id, target_entity_id, pathway_id, relation_type,
        effect_polarity, species_context, compartment_context,
        evidence_status, context_scope, export_priority, notes
      )
      SELECT
        composite_id, component.component_id, pathway.pathway_id,
        'contains_component', 'unknown', 'human; mouse', 'cytoplasm to nucleus',
        'curated_component_mapping',
        'Composite decomposition only; component membership does not imply TF activation.',
        'medium',
        'The canonical IKK-NFKB1-RELA label explicitly names this component.'
      FROM SignalingPathway AS pathway
      WHERE pathway.pathway_name = 'TNF-NF-kappaB'
      RETURNING SignalingEdge.edge_id INTO db_edge_id;
    END IF;

    INSERT INTO SignalingEdgeRegister (
      edge_id, register_edge_id, module, source_label, target_label,
      register_relation_type, graph_relation_type, pathway_name,
      evidence_layer, edge_status, confidence_tier, evidence_ids,
      consolidation_note
    ) VALUES (
      db_edge_id, synthetic_edge_id, '21B', 'IKK-NFKB1-RELA', component.component_name,
      'contains_component', 'contains_component', 'TNF-NF-kappaB',
      'component_normalization', 'supported', 'medium',
      'M21B-EVID-000004;M21B-EVID-000021',
      'Component mapping is explicit and not an activation edge.'
    ) ON CONFLICT (register_edge_id) DO NOTHING;

    INSERT INTO SignalingEdgeRegisterSource (
      edge_id, register_edge_id, register_evidence_id, module,
      support_kind, species_support, source_scope, confidence_tier,
      citation_note, notes, source_kind, source_locator,
      source_locator_status, evidence_summary, limitations,
      evidence_layer, evidence_exportable, consolidation_note
    ) VALUES (
      db_edge_id, synthetic_edge_id, synthetic_evidence_id, '21B',
      'manual_background', 'both', 'contextual_support', 'medium',
      'Canonical Module 21B composite node label: IKK-NFKB1-RELA.',
      'Explicit component normalization for graph querying.',
      'mSCIdblit_component_review',
      'mSCIdblit://module20_24/component/IKK-NFKB1-RELA',
      'stable_internal_register',
      'The composite label contains an explicit NFKB1 or RELA TF component.',
      'This row does not assert that the component edge is a direct biochemical interaction.',
      'component_normalization', TRUE,
      'Activation evidence remains on the original receptor-proximal cascade edges.'
    ) ON CONFLICT (edge_id, register_evidence_id) DO NOTHING;
  END LOOP;

  SELECT regulon.regulon_id INTO regulon_pk
  FROM Regulon AS regulon
  WHERE regulon.tf_entity_id = nfk_id
    AND regulon.species_context = 'human'
    AND regulon.cell_type_context = 'unspecified'
    AND regulon.compartment_context = 'nucleus'
    AND regulon.source_registry = 'TRRUST'
    AND regulon.source_version = '2018-04-16';

  IF regulon_pk IS NULL THEN
    INSERT INTO Regulon (
      tf_entity_id, regulon_name, species_context, cell_type_context,
      compartment_context, source_registry, source_version,
      definition_status, membership_semantics, notes
    ) VALUES (
      nfk_id, 'NFKB1 core literature regulon', 'human', 'unspecified', 'nucleus',
      'TRRUST', '2018-04-16', 'curated', 'target_gene_membership',
      'Lightweight 17-target summary from the TRRUST v2 NFKB1 target table; not exhaustive and not TNF-specific.'
    ) RETURNING Regulon.regulon_id INTO regulon_pk;
  END IF;

  SELECT pathway.pathway_id INTO selected_pathway_id
  FROM SignalingPathway AS pathway
  WHERE pathway.pathway_name = 'NFKB1-core-regulon';

  FOR target_row IN SELECT * FROM nfkb1_core_targets ORDER BY symbol LOOP
    SELECT entity_id INTO target_id
    FROM SignalingEntity
    WHERE upper(coalesce(gene_symbol, '')) = target_row.symbol
       OR upper(canonical_name) = target_row.symbol
    ORDER BY CASE WHEN upper(coalesce(gene_symbol, '')) = target_row.symbol THEN 0 ELSE 1 END,
             entity_id
    LIMIT 1;

    IF target_id IS NULL THEN
      INSERT INTO SignalingEntity (canonical_name, entity_type, gene_symbol, organism_scope, notes)
      VALUES (
        target_row.symbol, 'target_gene', target_row.symbol, 'human',
        'Added for the lightweight TRRUST v2 NFKB1 target summary.'
      ) RETURNING SignalingEntity.entity_id INTO target_id;
    END IF;

    INSERT INTO SignalingEntityRole (
      entity_id, role, role_status, role_source, role_evidence,
      source_registry, source_version, export_priority
    ) VALUES (
      target_id, 'target_gene', 'curated', 'TRRUST_v2_NFKB1_core_regulon',
      'NFKB1 target relationship in TRRUST v2; PMIDs: ' || target_row.pmids,
      'TRRUST', '2018-04-16', 'medium'
    ) ON CONFLICT (entity_id, role) DO NOTHING;

    SELECT edge.edge_id INTO db_edge_id
    FROM SignalingEdge AS edge
    WHERE edge.source_entity_id = nfk_id
      AND edge.target_entity_id = target_id
      AND edge.pathway_id = selected_pathway_id
      AND edge.relation_type = 'regulates_target_gene'
    LIMIT 1;

    IF db_edge_id IS NULL THEN
      INSERT INTO SignalingEdge (
        source_entity_id, target_entity_id, pathway_id, relation_type,
        effect_polarity, species_context, compartment_context,
        evidence_status, context_scope, export_priority, notes
      ) VALUES (
        nfk_id, target_id, selected_pathway_id, 'regulates_target_gene',
        target_row.effect_polarity, 'human', 'nucleus', 'TRRUST_v2_curated',
        'Literature-curated NFKB1 target relationship; not a TNF-specific target induction claim.',
        'medium', 'Lightweight NFKB1 target summary; use regulon provenance for the target-set interpretation.'
      ) RETURNING SignalingEdge.edge_id INTO db_edge_id;
    END IF;

    synthetic_edge_id := 'TRRUST-NFKB1-' || lower(target_row.symbol);
    synthetic_evidence_id := synthetic_edge_id || '-SOURCE';

    INSERT INTO SignalingEdgeRegister (
      edge_id, register_edge_id, module, source_label, target_label,
      register_relation_type, graph_relation_type, pathway_name,
      evidence_layer, edge_status, confidence_tier, evidence_ids,
      consolidation_note
    ) VALUES (
      db_edge_id, synthetic_edge_id, 'regulon', 'NFKB1', target_row.symbol,
      'regulates_target_gene', 'regulates_target_gene', 'NFKB1-core-regulon',
      'regulon', 'supported', 'medium', target_row.pmids,
      'TRRUST v2 literature-curated NFKB1 target summary.'
    ) ON CONFLICT (register_edge_id) DO NOTHING;

    INSERT INTO SignalingEdgeRegisterSource (
      edge_id, register_edge_id, register_evidence_id, module,
      support_kind, species_support, source_scope, confidence_tier,
      citation_note, notes, source_kind, source_locator,
      source_locator_status, evidence_summary, limitations,
      evidence_layer, evidence_exportable, consolidation_note
    ) VALUES (
      db_edge_id, synthetic_edge_id, synthetic_evidence_id, 'regulon',
      'database_curated', 'human', 'direct_edge', 'medium',
      'TRRUST v2 NFKB1 -> ' || target_row.symbol || '; PMIDs: ' || target_row.pmids,
      'TRRUST reports activation, repression, and/or unknown mode records; the graph effect is retained as context-dependent when modes conflict.',
      'TRRUST_v2',
      'https://www.grnpedia.org/trrust/export_tsv.php?tabletype=TF&gene=NFKB1&species=human',
      'stable_query',
      'Literature-curated TF-target relationship from the TRRUST v2 NFKB1 target table.',
      'Human literature summary; it does not establish TNF-specific regulation in every receiver cell or injury context.',
      'regulon', TRUE,
      'The regulon membership row stores the same target-set relationship separately from signaling activation.'
    ) ON CONFLICT (edge_id, register_evidence_id) DO NOTHING;

    member_effect := CASE target_row.effect_polarity
      WHEN 'activating' THEN 'activating_target'
      WHEN 'inhibitory' THEN 'repressing_target'
      WHEN 'context_dependent' THEN 'context_dependent'
      ELSE 'unknown'
    END;

    INSERT INTO RegulonMember (
      regulon_id, target_entity_id, membership_basis, regulatory_effect,
      membership_status, confidence_tier, export_priority, notes
    ) VALUES (
      regulon_pk, target_id, 'inferred_regulatory', member_effect,
      'supported', 'medium', 'medium',
      'TRRUST v2 NFKB1 core target summary; not TNF-specific activation evidence.'
    ) ON CONFLICT (regulon_id, target_entity_id) DO NOTHING;

    SELECT member.regulon_member_id INTO member_id
    FROM RegulonMember AS member
    WHERE member.regulon_id = regulon_pk
      AND member.target_entity_id = target_id;

    INSERT INTO RegulonMemberSource (
      regulon_member_id, source_registry, source_version,
      external_record_id, source_locator, support_kind, evidence_scope,
      evidence_status, species_support, confidence_tier, citation_note,
      limitations
    ) VALUES (
      member_id, 'TRRUST', '2018-04-16', 'TRRUST:NFKB1:' || target_row.symbol,
      'https://www.grnpedia.org/trrust/export_tsv.php?tabletype=TF&gene=NFKB1&species=human',
      'database_curated', 'inferred_regulatory', 'supporting', 'human', 'medium',
      'TRRUST v2 NFKB1 -> ' || target_row.symbol || '; PMIDs: ' || target_row.pmids,
      'This is a literature-curated human NFKB1 regulon membership, not a TNF-specific target induction claim.'
    ) ON CONFLICT (
      regulon_member_id, source_registry, source_version,
      external_record_id, support_kind
    ) DO NOTHING;
  END LOOP;
END $$;

COMMIT;
