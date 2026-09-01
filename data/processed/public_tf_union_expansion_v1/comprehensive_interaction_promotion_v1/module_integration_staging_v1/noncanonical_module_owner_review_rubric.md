# Noncanonical gene-expression regulator module-owner review

Each row is a reviewed A/B evidence-backed relationship that has an explicit module route but is not a canonical sequence-specific TF edge. The evidence tier and provenance columns are source-controlled; module owners should only fill `module_owner_decision` and `module_owner_notes`.

Allowed decisions:

- `promote_to_noncanonical_module_layer`: exact regulator-target-species relationship, mechanism fits the module, and the relationship should be represented in the auxiliary noncanonical layer.
- `retain_context_only`: evidence is useful context but is not sufficiently module-specific or mechanistically actionable.
- `screen_out`: identity, species, target, direction, or mechanism does not support inclusion in the module context layer.
- `needs_more_context`: plausible relationship, but module or SCI target-cell relevance requires additional evidence.

Regardless of decision, do not change the original evidence tier. The fields `regulator_role_class` and `canonical_role_status` describe biological role, while `sci_context_status` records SCI relevance independently. These rows remain noncanonical and an approved row would be placed only in the separate noncanonical module-context layer.
