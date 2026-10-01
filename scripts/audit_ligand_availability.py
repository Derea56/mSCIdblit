#!/usr/bin/env python3
"""Audit source evidence for ligand physical-availability classes.

This produces a reviewable, generic ligand-availability layer keyed to the
pinned Module 20B-24B mechanism release. It does not modify mechanism nodes,
edges, route confidence, or SCI evidence tables. Form classifications are
staged candidates unless the source text places an availability term near the
exact ligand label; assay-format language is kept separate.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RELEASE = ROOT / "data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion627"
DEFAULT_LEDGER = ROOT / "work/cross_module_synthesis/canonical_evidence_review/module20_24_integrated_phase2_extractions.tsv"
DEFAULT_PACK = ROOT / "context_packs/spinal_cord_injury"
DEFAULT_OUTPUT = ROOT / "data/processed/ligand_availability_audit_v1"
DEFAULT_SOURCE_REGISTERS = tuple(
    ROOT / "work/module_b_consolidation" / module / f"{module}_evidence_register.tsv"
    for module in ("module20b", "module21b", "module22b", "module23b", "module24b")
)

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.audit_sci_module_spatial_reconciliation import index_pack_rows, source_identifiers, unique_values
from scripts.build_sci_context_pack import read_tsv

SOURCE_FIELDS = (
    "observation_value_or_blocker",
    "claim_text_or_blocker",
)

CONTEXT_FORM_CLASSES = {
    "soluble": "soluble",
    "soluble cytokine": "soluble",
    "membrane_bound": "membrane_bound",
    "surface receptor": "membrane_bound",
    "surface CD3/CD4 or CD3/CD8α proteins": "membrane_bound",
}
CONTEXT_FORM_PATTERNS = (
    (re.compile(r"\b(?:soluble|secreted)\b", re.IGNORECASE), "soluble"),
    (re.compile(r"\b(?:extracellular[ _-]+matrix|matrix[ _-](?:associated|assembled|bands?)|fibrillar[ _-]+(?:matrix|network))\b", re.IGNORECASE), "ecm_retained"),
)

SOURCE_FORM_OVERRIDES = {
    "M20B-EVID-001936": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("observation_value_or_blocker", "observation_perturbation"),
        "pattern": re.compile(r"\bcollagen[- ]I\b.*\bmatrix\b|\bcollagen[- ]I\s+matrix\b", re.IGNORECASE),
    },
    "M20B-EVID-002127": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("observation_value_or_blocker", "claim_text_or_blocker"),
        "pattern": re.compile(r"\b(?:perlecan|HSPG2)\b.*\bextracellular[- ]matrix\b", re.IGNORECASE),
    },
    "M20B-EVID-002232": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("observation_value_or_blocker",),
        "pattern": re.compile(r"\bsoluble\s+netrin\b", re.IGNORECASE),
    },
    "M23B-EVID-000749": {
        "candidate": "both_or_context_dependent",
        "signals": ["soluble", "ecm_retained"],
        "fields": ("observation_value_or_blocker",),
        "pattern": re.compile(r"\b(?:soluble/cellular\s+FN|FN\s+matrix)\b", re.IGNORECASE),
    },
    "M20B-EVID-002154": {
        "candidate": "both_or_context_dependent",
        "signals": ["soluble", "ecm_retained"],
        "fields": ("observation_value_or_blocker", "observation_perturbation"),
        "pattern": re.compile(r"\b(?:polymerized laminin-332 matrices|matrix versus soluble ligand comparison)\b", re.IGNORECASE),
    },
    "M20B-EVID-002199": {
        "candidate": "both_or_context_dependent",
        "signals": ["soluble", "ecm_retained"],
        "fields": ("observation_value_or_blocker", "observation_perturbation"),
        "pattern": re.compile(r"\b(?:polymerized laminin-332 matrices|matrix versus soluble ligand comparison)\b", re.IGNORECASE),
    },
    "M20B-EVID-003229": {
        "candidate": "both_or_context_dependent",
        "signals": ["soluble", "ecm_retained"],
        "fields": ("observation_perturbation",),
        "pattern": re.compile(r"\bsoluble/immobilized decorin\b", re.IGNORECASE),
    },
    "M20B-EVID-002904": {
        "candidate": "membrane_bound",
        "signals": ["membrane_bound"],
        "fields": ("observation_value_or_blocker",),
        "pattern": re.compile(r"\bCD47 displayed on cell membranes\b", re.IGNORECASE),
    },
    "M20B-EVID-004969": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("observation_value_or_blocker",),
        "pattern": re.compile(r"\bmacrophage-secreted osteopontin\b", re.IGNORECASE),
    },
    "M20B-EVID-002994": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("observation_value_or_blocker", "observation_perturbation"),
        "pattern": re.compile(r"\bcollagen XI(?:-containing matrices| in collagen I matrices)\b", re.IGNORECASE),
    },
    "M20B-EVID-003007": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("claim_text_or_blocker", "observation_value_or_blocker"),
        "pattern": re.compile(r"\bdirect matrix-receptor adhesion edge\b|\bcollagen XIV/undulin\b", re.IGNORECASE),
    },
    "M20B-EVID-004966": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("observation_value_or_blocker",),
        "pattern": re.compile(r"\bMindin/SPON2 matrix\b", re.IGNORECASE),
    },
    "M23B-EVID-000346": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("observation_value_or_blocker", "observation_perturbation", "claim_text_or_blocker"),
        "pattern": re.compile(r"\b(?:matrix-associated ligand context|PTN immobilization|matrix-presentation boundaries)\b", re.IGNORECASE),
    },
    "M20B-EVID-001844": {
        "candidate": "both_or_context_dependent",
        "signals": ["soluble", "immobilized"],
        "fields": ("observation_value_or_blocker",),
        "pattern": re.compile(r"\b(?:soluble and immobilized|soluble versus immobilized) CCL21\b", re.IGNORECASE),
    },
    "M20B-EVID-005357": {
        "candidate": "both_or_context_dependent",
        "signals": ["soluble", "membrane_bound"],
        "fields": ("observation_value_or_blocker", "claim_text_or_blocker"),
        "pattern": re.compile(r"\b(?:soluble-fractalkine chemotaxis and membrane-fractalkine adhesion|membrane-bound versus soluble CX3CL1)\b", re.IGNORECASE),
    },
    "M20B-EVID-002290": {
        "candidate": "both_or_context_dependent",
        "signals": ["soluble", "immobilized"],
        "fields": ("observation_value_or_blocker", "observation_perturbation"),
        "pattern": re.compile(r"\b(?:Immobilized VWF.*soluble VWF|soluble versus immobilized VWF)\b", re.IGNORECASE),
    },
}

SOURCE_FORM_OVERRIDES.update(
    {
        "M20B-EVID-000472": {
            "candidate": "both_or_context_dependent",
            "signals": ["soluble", "membrane_bound"],
            "fields": ("observation_value_or_blocker", "observation_perturbation"),
            "pattern": re.compile(r"(?:cell-surface and soluble ectodomain assays|soluble FLRT2 ECD)", re.IGNORECASE),
        },
        "M20B-EVID-001792": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("observation_value_or_blocker",),
            "pattern": re.compile(r"\bSoluble Slit2\b", re.IGNORECASE),
        },
        "M20B-EVID-002382": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("observation_value_or_blocker",),
            "pattern": re.compile(r"\bTHBS2 secreted by\b", re.IGNORECASE),
        },
        "M20B-EVID-002567": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("observation_value_or_blocker",),
            "pattern": re.compile(r"\bsecreted ANGPTL4\b", re.IGNORECASE),
        },
        "M20B-EVID-002886": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("claim_text_or_blocker",),
            "pattern": re.compile(r"\bCD177 is GPI-anchored\b", re.IGNORECASE),
        },
        "M20B-EVID-002906": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("observation_value_or_blocker",),
            "pattern": re.compile(r"\bpurified soluble CD48\b", re.IGNORECASE),
        },
        "M20B-EVID-002912": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("observation_value_or_blocker",),
            "pattern": re.compile(r"\bB-cell surface protein CD72\b", re.IGNORECASE),
        },
        "M20B-EVID-002929": {
            "candidate": "both_or_context_dependent",
            "signals": ["soluble", "ecm_retained"],
            "fields": ("observation_value_or_blocker", "claim_text_or_blocker"),
            "pattern": re.compile(r"(?:Secreted CEACAM16.*tectorial membrane|secreted extracellular-matrix context)", re.IGNORECASE),
        },
        "M20B-EVID-002958": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("observation_value_or_blocker",),
            "pattern": re.compile(r"\bform a secreted composite cytokine complex\b", re.IGNORECASE),
        },
        "M20B-EVID-002981": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("claim_text_or_blocker",),
            "pattern": re.compile(r"\bGPI-anchored CNTN3\b", re.IGNORECASE),
        },
        "M20B-EVID-002982": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("claim_text_or_blocker",),
            "pattern": re.compile(r"\bGPI-anchored CNTN4\b", re.IGNORECASE),
        },
        "M20B-EVID-002985": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("claim_text_or_blocker",),
            "pattern": re.compile(r"\bGPI-anchored CNTN6\b", re.IGNORECASE),
        },
        "M20B-EVID-003389": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("observation_value_or_blocker",),
            "pattern": re.compile(r"\bSecreted FAM3C/ILEI\b", re.IGNORECASE),
        },
        "M20B-EVID-003739": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("observation_value_or_blocker",),
            "pattern": re.compile(r"\bsecreted GZMA\b", re.IGNORECASE),
        },
        "M20B-EVID-003767": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("observation_value_or_blocker",),
            "pattern": re.compile(r"\bSoluble tetrameric murine Qa-1/H2-T23 complexes\b", re.IGNORECASE),
        },
        "M20B-EVID-003768": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("observation_value_or_blocker",),
            "pattern": re.compile(r"\bSoluble tetrameric murine Qa-1/H2-T23 complexes\b", re.IGNORECASE),
        },
        "M20B-EVID-005366": {
            "candidate": "both_or_context_dependent",
            "signals": ["soluble", "membrane_bound"],
            "fields": ("observation_value_or_blocker", "claim_text_or_blocker"),
            "pattern": re.compile(r"\bSoluble and membrane-anchored CXCL16\b", re.IGNORECASE),
        },
        "M24B-EVID-000043": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("observation_value_or_blocker", "claim_text_or_blocker"),
            "pattern": re.compile(r"\bsecreted (?:astrocyte-derived )?CCN1\b", re.IGNORECASE),
        },
        "M24B-EVID-000152": {
            "candidate": "ecm_retained",
            "signals": ["ecm_retained"],
            "fields": ("observation_value_or_blocker",),
            "pattern": re.compile(r"\bCCL27/CTACK bound extracellular matrix\b", re.IGNORECASE),
        },
        "M24B-EVID-000167": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("observation_value_or_blocker", "claim_text_or_blocker", "observation_perturbation"),
            "pattern": re.compile(r"\bSoluble intact human decorin\b|\bsoluble decorin acts\b|\bSoluble intact decorin;", re.IGNORECASE),
        },
        "M24B-EVID-000195": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("observation_value_or_blocker",),
            "pattern": re.compile(r"\bLTB4 was released from traumatized spinal-cord slices\b", re.IGNORECASE),
        },
        "M20B-EVID-001856": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("context_and_limitations",),
            "pattern": re.compile(r"\bEREG EGF domain rather than full-length membrane-tethered ligand\b", re.IGNORECASE),
        },
        "M20B-EVID-001983": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("context_and_limitations",),
            "pattern": re.compile(r"\bsoluble alpha3NC1 fragment\b", re.IGNORECASE),
        },
        "M20B-EVID-002893": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("claim_text_or_blocker", "context_and_limitations"),
            "pattern": re.compile(r"\bCD22-PTPRC/CD45.*cell-surface association boundary\b|\bcell-surface cross-linking\b", re.IGNORECASE),
        },
        "M20B-EVID-002980": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("context_and_limitations",),
            "pattern": re.compile(r"\bCNTN2/TAG1 is a GPI-anchored adhesion molecule\b", re.IGNORECASE),
        },
        "M20B-EVID-002984": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("context_and_limitations",),
            "pattern": re.compile(r"\bCNTN6/NB-3 is GPI-anchored\b", re.IGNORECASE),
        },
        "M20B-EVID-003707": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("context_and_limitations",),
            "pattern": re.compile(r"\bGPC3 is a GPI-anchored heparan-sulfate proteoglycan\b", re.IGNORECASE),
        },
        "M24B-EVID-000085": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("context_and_limitations",),
            "pattern": re.compile(r"\bFAM3D is a secreted chemokine-like ligand\b", re.IGNORECASE),
        },
        "M24B-EVID-000165": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("context_and_limitations",),
            "pattern": re.compile(r"\bsecreted ANXA2 tetramer\b", re.IGNORECASE),
        },
    }
)

# These are keyed, source-register curation rules.  They are intentionally
# separate from SOURCE_FORM_OVERRIDES: register rows are preserved as a
# distinct provenance layer and are only used when the same b_evidence_id is
# not already materialized in the integrated phase-2 ledger.
SOURCE_REGISTER_FORM_OVERRIDES = {
    "M20B-EVID-002097": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("evidence_summary",),
        "pattern": re.compile(r"\bCOMP is an extracellular matrix protein\b", re.IGNORECASE),
    },
    "M21B-EVID-000095": {
        "candidate": "membrane_bound",
        "signals": ["membrane_bound"],
        "fields": ("evidence_summary",),
        "pattern": re.compile(r"\bmembrane-bound DLL1\b", re.IGNORECASE),
    },
    "M21B-EVID-000137": {
        "candidate": "membrane_bound",
        "signals": ["membrane_bound"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bmembrane-spanning semaphorin dimer\b", re.IGNORECASE),
    },
    "M21B-EVID-000241": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bsecreted mouse GlyCAM1\b", re.IGNORECASE),
    },
    "M21B-EVID-000245": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bsecreted ligand\b", re.IGNORECASE),
    },
    "M21B-EVID-000246": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bsecreted ligand\b", re.IGNORECASE),
    },
    "M21B-EVID-000277": {
        "candidate": "both_or_context_dependent",
        "signals": ["soluble", "membrane_bound"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bmembrane/soluble SEMA6D ectodomain\b", re.IGNORECASE),
    },
    "M21B-EVID-000434": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bsecreted SEMA3C processing\b", re.IGNORECASE),
    },
    "M21B-EVID-000436": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bsecreted SEMA3C processing\b", re.IGNORECASE),
    },
    "M21B-EVID-000438": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("evidence_summary",),
        "pattern": re.compile(r"\btumor-secreted ProS1\b", re.IGNORECASE),
    },
    "M21B-EVID-000439": {
        "candidate": "both_or_context_dependent",
        "signals": ["soluble", "membrane_bound"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bsoluble versus membrane SCF\b", re.IGNORECASE),
    },
    "M21B-EVID-000445": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("evidence_summary",),
        "pattern": re.compile(r"\bsoluble human GAS6\b", re.IGNORECASE),
    },
    "M21B-EVID-000513": {
        "candidate": "membrane_bound",
        "signals": ["membrane_bound"],
        "fields": ("evidence_summary",),
        "pattern": re.compile(r"\bGPI-anchored SEMA7A\b", re.IGNORECASE),
    },
    "M21B-EVID-000589": {
        "candidate": "membrane_bound",
        "signals": ["membrane_bound"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bGPI-anchored/membrane SEMA7A\b", re.IGNORECASE),
    },
    "M21B-EVID-000696": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("evidence_summary",),
        "pattern": re.compile(r"\bproBDNF secreted from COS-7 cells\b", re.IGNORECASE),
    },
    "M21B-EVID-000786": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("evidence_summary",),
        "pattern": re.compile(r"\bGremlin1 as a secreted BMP antagonist\b", re.IGNORECASE),
    },
    "M21B-EVID-000787": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("evidence_summary",),
        "pattern": re.compile(r"\bGremlin1 as a secreted BMP antagonist\b", re.IGNORECASE),
    },
    "M21B-EVID-000793": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bsecreted BMP7 antagonist\b", re.IGNORECASE),
    },
    "M21B-EVID-006703": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("evidence_summary",),
        "pattern": re.compile(r"\bsecreted MADD-4/Punctin\b", re.IGNORECASE),
    },
    "M21B-EVID-006910": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("evidence_summary", "limitations"),
        "pattern": re.compile(r"\bmatrix-bound GDNF\b|\bimmobilized matrix-bound GDNF\b", re.IGNORECASE),
    },
    "M21B-EVID-006973": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bUSAG1/SOSTDC1 as a soluble BMP2 antagonist\b", re.IGNORECASE),
    },
    "M21B-EVID-006974": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bUSAG1/SOSTDC1 as a soluble BMP4 antagonist\b", re.IGNORECASE),
    },
    "M21B-EVID-006975": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bUSAG1/SOSTDC1 as a soluble BMP6 antagonist\b", re.IGNORECASE),
    },
    "M21B-EVID-006976": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bNoggin as a soluble BMP7-sequestering antagonist\b", re.IGNORECASE),
    },
    "M21B-EVID-009994": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("evidence_summary",),
        "pattern": re.compile(r"\breactive astrocyte-secreted TNF-alpha\b", re.IGNORECASE),
    },
    "M21B-EVID-010943": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("evidence_summary",),
        "pattern": re.compile(r"\bsoluble APP fragments\b", re.IGNORECASE),
    },
    "M21B-EVID-010981": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("evidence_summary", "limitations"),
        "pattern": re.compile(r"\bbasement membrane\b|\bLAMC3-DAG1 ECM\b", re.IGNORECASE),
    },
    "M21B-EVID-010984": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bcollagen-II fibrillar form\b", re.IGNORECASE),
    },
    "M21B-EVID-010986": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bnative fibrillar type IV presentation\b", re.IGNORECASE),
    },
    "M21B-EVID-010987": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bnative fibrillar type VI presentation\b", re.IGNORECASE),
    },
    "M23B-EVID-001552": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("evidence_summary",),
        "pattern": re.compile(r"\bsoluble ephrin-A2 conditioned-medium\b", re.IGNORECASE),
    },
    "M23B-EVID-000580": {
        "candidate": "both_or_context_dependent",
        "signals": ["soluble", "membrane_bound"],
        "fields": ("evidence_summary", "limitations"),
        "pattern": re.compile(r"\bCX3CL1 membrane/soluble fractalkine\b|\bMembrane-tethered adhesion and soluble chemotaxis\b", re.IGNORECASE),
    },
    "M23B-EVID-000604": {
        "candidate": "both_or_context_dependent",
        "signals": ["soluble", "membrane_bound"],
        "fields": ("evidence_summary", "limitations"),
        "pattern": re.compile(r"\bCXCL16 membrane/shedded chemokine\b|\bMembrane versus soluble CXCL16\b", re.IGNORECASE),
    },
    "M23B-EVID-001390": {
        "candidate": "membrane_bound",
        "signals": ["membrane_bound"],
        "fields": ("limitations",),
        "pattern": re.compile(r"\bcell-surface CALR\b", re.IGNORECASE),
    },
    "M23B-EVID-001392": {
        "candidate": "membrane_bound",
        "signals": ["membrane_bound"],
        "fields": ("evidence_summary",),
        "pattern": re.compile(r"\bCell-surface CALR/LRP1\b", re.IGNORECASE),
    },
}

# Additional register rows with an explicit ligand-form phrase in the
# limitations field.  Keeping this as a compact curation table makes the
# expansion reviewable without enabling generic form-word matching.
SOURCE_REGISTER_FORM_OVERRIDES.update(
    {
        evidence_id: {
            "candidate": candidate,
            "signals": signals,
            "fields": (field,),
            "pattern": re.compile(pattern, re.IGNORECASE),
        }
        for evidence_id, candidate, signals, field, pattern in (
            ("M21B-EVID-000069", "soluble", ["soluble"], "evidence_summary", r"Tagged soluble IL-11"),
            ("M21B-EVID-000111", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"membrane versus soluble ligand form"),
            ("M21B-EVID-000122", "membrane_bound", ["membrane_bound"], "limitations", r"membrane-bound cell-cell geometry"),
            ("M21B-EVID-000133", "membrane_bound", ["membrane_bound"], "limitations", r"membrane CD200/CD200R1 geometry"),
            ("M21B-EVID-000139", "membrane_bound", ["membrane_bound"], "limitations", r"membrane-bound trans-cell geometry"),
            ("M21B-EVID-000140", "membrane_bound", ["membrane_bound"], "limitations", r"membrane-bound trans interaction"),
            ("M21B-EVID-000198", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"membrane-bound versus soluble CXCL16"),
            ("M21B-EVID-000199", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"membrane-anchored versus soluble fractalkine"),
            ("M21B-EVID-000206", "both_or_context_dependent", ["soluble", "ecm_retained"], "limitations", r"soluble versus immobilized/full-length or processed CCL21"),
            ("M21B-EVID-000210", "membrane_bound", ["membrane_bound"], "limitations", r"membrane-presentation"),
            ("M21B-EVID-000248", "membrane_bound", ["membrane_bound"], "limitations", r"CD24 membrane context"),
            ("M21B-EVID-000250", "membrane_bound", ["membrane_bound"], "limitations", r"cell-surface nucleolin pool"),
            ("M21B-EVID-000254", "membrane_bound", ["membrane_bound"], "limitations", r"cell-surface LAMP-1"),
            ("M21B-EVID-000255", "membrane_bound", ["membrane_bound"], "limitations", r"cell-surface LAMP-2"),
            ("M21B-EVID-000258", "membrane_bound", ["membrane_bound"], "limitations", r"cell-surface 72-kDa Mac-2BP glycoform"),
            ("M21B-EVID-000312", "membrane_bound", ["membrane_bound"], "limitations", r"membrane/clustered ephrin-B1"),
            ("M21B-EVID-000325", "membrane_bound", ["membrane_bound"], "limitations", r"clustered/membrane ligand geometry"),
            ("M21B-EVID-000330", "soluble", ["soluble"], "limitations", r"soluble HB-EGF"),
            ("M21B-EVID-000331", "soluble", ["soluble"], "limitations", r"soluble HB-EGF"),
            ("M21B-EVID-000334", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"membrane-anchored versus soluble ligand forms"),
            ("M21B-EVID-000396", "membrane_bound", ["membrane_bound"], "limitations", r"trimeric/membrane-presented ligand"),
            ("M21B-EVID-000398", "membrane_bound", ["membrane_bound"], "limitations", r"membrane/oligomerized TNFSF ligand"),
            ("M21B-EVID-000403", "membrane_bound", ["membrane_bound"], "limitations", r"membrane/oligomerized LIGHT"),
            ("M21B-EVID-000404", "membrane_bound", ["membrane_bound"], "limitations", r"membrane/oligomerized LIGHT"),
            ("M21B-EVID-000405", "membrane_bound", ["membrane_bound"], "limitations", r"trimeric/membrane-presented ligand"),
            ("M21B-EVID-000406", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"membrane versus soluble TWEAK"),
            ("M21B-EVID-000412", "membrane_bound", ["membrane_bound"], "limitations", r"membrane/cross-linked FasL"),
            ("M21B-EVID-000416", "soluble", ["soluble"], "limitations", r"secreted/processed SEMA3C"),
            ("M21B-EVID-000469", "ecm_retained", ["ecm_retained"], "limitations", r"fibrillar/triple-helical collagen III"),
            ("M21B-EVID-000484", "both_or_context_dependent", ["soluble", "ecm_retained"], "limitations", r"soluble-versus-immobilized OPN presentation"),
            ("M21B-EVID-000530", "membrane_bound", ["membrane_bound"], "limitations", r"membrane-bound or clustered ephrin-B1"),
            ("M21B-EVID-000547", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"trimeric/membrane versus soluble CD40L"),
            ("M21B-EVID-000567", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"soluble/membrane CD40L"),
            ("M21B-EVID-000570", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"membrane-versus-soluble CX3CL1"),
            ("M21B-EVID-000571", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"soluble versus membrane CX3CL1"),
            ("M21B-EVID-000572", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"soluble versus membrane CX3CL1"),
            ("M21B-EVID-000585", "ecm_retained", ["ecm_retained"], "limitations", r"immobilized VEGF165/189 ligand form"),
            ("M21B-EVID-000586", "ecm_retained", ["ecm_retained"], "limitations", r"immobilized VEGF165/189 ligand form"),
            ("M21B-EVID-000587", "soluble", ["soluble"], "limitations", r"recombinant/secreted ANGPTL3"),
            ("M21B-EVID-000591", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"membrane or shed RGD-containing GPNMB"),
            ("M21B-EVID-000608", "membrane_bound", ["membrane_bound"], "limitations", r"membrane PVR context"),
            ("M21B-EVID-000610", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"soluble-versus-cell-surface context"),
            ("M21B-EVID-000612", "membrane_bound", ["membrane_bound"], "limitations", r"membrane adhesion geometry"),
            ("M21B-EVID-000614", "membrane_bound", ["membrane_bound"], "limitations", r"APC membrane presentation"),
            ("M21B-EVID-000618", "membrane_bound", ["membrane_bound"], "limitations", r"membrane immune-synapse geometry"),
            ("M21B-EVID-000621", "membrane_bound", ["membrane_bound"], "limitations", r"membrane CD70"),
            ("M21B-EVID-000622", "membrane_bound", ["membrane_bound"], "limitations", r"trimeric/membrane CD40L"),
            ("M21B-EVID-000623", "membrane_bound", ["membrane_bound"], "limitations", r"membrane/cell-context boundaries"),
            ("M21B-EVID-000627", "soluble", ["soluble"], "limitations", r"soluble liver-secreted FGL1"),
            ("M21B-EVID-000642", "soluble", ["soluble"], "limitations", r"multimeric soluble SP-D"),
            ("M21B-EVID-000646", "soluble", ["soluble"], "limitations", r"soluble collectin/membrane-receptor geometry"),
            ("M21B-EVID-000648", "soluble", ["soluble"], "limitations", r"soluble collectin"),
        )
    }
)

SOURCE_REGISTER_FORM_OVERRIDES.update(
    {
        evidence_id: {
            "candidate": candidate,
            "signals": signals,
            "fields": (field,),
            "pattern": re.compile(pattern, re.IGNORECASE),
        }
        for evidence_id, candidate, signals, field, pattern in (
            ("M21B-EVID-000902", "membrane_bound", ["membrane_bound"], "evidence_summary", r"trans-presented latrophilin ligands"),
            ("M21B-EVID-000903", "membrane_bound", ["membrane_bound"], "evidence_summary", r"trans-presented latrophilin ligands"),
            ("M21B-EVID-000904", "membrane_bound", ["membrane_bound"], "evidence_summary", r"trans-presented latrophilin ligands"),
            ("M21B-EVID-000905", "membrane_bound", ["membrane_bound"], "evidence_summary", r"trans-presented latrophilin ligands"),
            ("M21B-EVID-000906", "membrane_bound", ["membrane_bound"], "evidence_summary", r"trans-presented latrophilin ligands"),
            ("M21B-EVID-001896", "membrane_bound", ["membrane_bound"], "limitations", r"cell-surface ligand"),
            ("M21B-EVID-002115", "membrane_bound", ["membrane_bound"], "evidence_summary", r"full-length CNTN3 surface-binding"),
            ("M21B-EVID-002116", "membrane_bound", ["membrane_bound"], "evidence_summary", r"full-length CNTN4 surface-binding"),
            ("M21B-EVID-002117", "membrane_bound", ["membrane_bound"], "evidence_summary", r"full-length CNTN5 surface-binding"),
            ("M21B-EVID-002118", "membrane_bound", ["membrane_bound"], "evidence_summary", r"full-length CNTN6 surface-binding"),
            ("M21B-EVID-002316", "membrane_bound", ["membrane_bound"], "limitations", r"membrane-bound SEMA5A"),
            ("M21B-EVID-002321", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"SEMA4C membrane/secreted form"),
            ("M21B-EVID-002324", "soluble", ["soluble"], "evidence_summary", r"secreted ligands of alpha-neurexins"),
            ("M21B-EVID-002325", "soluble", ["soluble"], "evidence_summary", r"secreted ligands of alpha-neurexins"),
            ("M21B-EVID-002326", "soluble", ["soluble"], "evidence_summary", r"secreted ligands of alpha-neurexins"),
            ("M21B-EVID-002327", "soluble", ["soluble"], "evidence_summary", r"secreted ligands of alpha-neurexins"),
            ("M21B-EVID-002328", "soluble", ["soluble"], "evidence_summary", r"secreted ligands of alpha-neurexins"),
            ("M21B-EVID-002329", "soluble", ["soluble"], "evidence_summary", r"secreted ligands of alpha-neurexins"),
            ("M21B-EVID-002336", "membrane_bound", ["membrane_bound"], "limitations", r"GPI-anchored IgSF21"),
            ("M21B-EVID-002359", "membrane_bound", ["membrane_bound"], "limitations", r"transmembrane tripartite-complex"),
            ("M21B-EVID-002361", "membrane_bound", ["membrane_bound"], "evidence_summary", r"transmembrane GABA-A"),
            ("M21B-EVID-002362", "membrane_bound", ["membrane_bound"], "evidence_summary", r"transmembrane GABA-A"),
            ("M21B-EVID-002363", "membrane_bound", ["membrane_bound"], "evidence_summary", r"transmembrane GABA-A"),
            ("M21B-EVID-002436", "membrane_bound", ["membrane_bound"], "evidence_summary", r"transmembrane AMPA-receptor auxiliary"),
            ("M21B-EVID-002448", "membrane_bound", ["membrane_bound"], "limitations", r"transmembrane auxiliary beta-subunit"),
            ("M21B-EVID-002480", "membrane_bound", ["membrane_bound"], "limitations", r"transmembrane auxiliary subunit"),
            ("M21B-EVID-002503", "membrane_bound", ["membrane_bound"], "limitations", r"cell-surface S100A10"),
            ("M21B-EVID-002504", "membrane_bound", ["membrane_bound"], "limitations", r"cell-surface S100A10"),
            ("M21B-EVID-002552", "soluble", ["soluble"], "limitations", r"secreted Noelin1"),
            ("M21B-EVID-002555", "soluble", ["soluble"], "limitations", r"secreted extracellular scaffold"),
            ("M21B-EVID-002556", "soluble", ["soluble"], "limitations", r"secreted pentraxin scaffold"),
            ("M21B-EVID-002558", "membrane_bound", ["membrane_bound"], "limitations", r"transmembrane neuroplastin isoform"),
            ("M21B-EVID-002597", "soluble", ["soluble"], "limitations", r"secreted progranulin"),
            ("M21B-EVID-002775", "soluble", ["soluble"], "limitations", r"multimerized/secreted ANGPTL5"),
            ("M21B-EVID-002788", "soluble", ["soluble"], "evidence_summary", r"soluble CD52"),
            ("M21B-EVID-002796", "both_or_context_dependent", ["soluble", "membrane_bound"], "evidence_summary", r"cell-surface and shed MUC16"),
            ("M21B-EVID-002826", "membrane_bound", ["membrane_bound"], "limitations", r"GPI-anchored oligodendrocyte myelin inhibitor"),
            ("M21B-EVID-002830", "membrane_bound", ["membrane_bound"], "limitations", r"transmembrane co-receptor"),
            ("M21B-EVID-002836", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"membrane-associated LOTUS"),
            ("M21B-EVID-002847", "membrane_bound", ["membrane_bound"], "evidence_summary", r"cell-surface nucleolin"),
            ("M21B-EVID-002860", "membrane_bound", ["membrane_bound"], "evidence_summary", r"cell-surface COLEC12"),
            ("M21B-EVID-002881", "soluble", ["soluble"], "limitations", r"soluble FBP"),
            ("M21B-EVID-002895", "soluble", ["soluble"], "limitations", r"soluble oligomeric properdin"),
            ("M21B-EVID-002896", "membrane_bound", ["membrane_bound"], "evidence_summary", r"Cell-surface PCNA"),
            ("M21B-EVID-002897", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"soluble-versus-surface form"),
            ("M21B-EVID-002902", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"membrane-anchor"),
            ("M21B-EVID-003146", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"GPI-anchored/soluble RGMa"),
            ("M21B-EVID-003147", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"GPI-anchored/soluble RGMa"),
            ("M21B-EVID-004660", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"KCP soluble/cell-associated form"),
            ("M21B-EVID-004661", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"KCP soluble/cell-associated form"),
            ("M21B-EVID-004765", "membrane_bound", ["membrane_bound"], "evidence_summary", r"multifunctional plasminogen-binding surface protein"),
            ("M21B-EVID-005114", "soluble", ["soluble"], "limitations", r"secreted cerebellin"),
            ("M21B-EVID-005115", "soluble", ["soluble"], "limitations", r"secreted cerebellin"),
            ("M21B-EVID-006968", "soluble", ["soluble"], "limitations", r"secreted OPN"),
            ("M21B-EVID-006980", "soluble", ["soluble"], "limitations", r"soluble BMP7-binding antagonist"),
            ("M21B-EVID-006984", "soluble", ["soluble"], "evidence_summary", r"secreted BMP antagonist"),
            ("M21B-EVID-006991", "ecm_retained", ["ecm_retained"], "limitations", r"ECM targeting"),
            ("M21B-EVID-006992", "ecm_retained", ["ecm_retained"], "limitations", r"ECM targeting"),
            ("M21B-EVID-006994", "ecm_retained", ["ecm_retained"], "limitations", r"ECM targeting"),
            ("M21B-EVID-006996", "ecm_retained", ["ecm_retained"], "limitations", r"ECM targeting"),
            ("M21B-EVID-006999", "ecm_retained", ["ecm_retained"], "limitations", r"ECM targeting"),
            ("M21B-EVID-007000", "ecm_retained", ["ecm_retained"], "limitations", r"ECM targeting"),
            ("M21B-EVID-007001", "ecm_retained", ["ecm_retained"], "limitations", r"ECM targeting"),
            ("M21B-EVID-007002", "ecm_retained", ["ecm_retained"], "limitations", r"ECM targeting"),
            ("M21B-EVID-007020", "membrane_bound", ["membrane_bound"], "limitations", r"membrane-bound/cytoneme"),
            ("M21B-EVID-007031", "soluble", ["soluble"], "limitations", r"soluble WNT9B"),
            ("M21B-EVID-007074", "membrane_bound", ["membrane_bound"], "limitations", r"membrane-presented/reporter"),
            ("M21B-EVID-007075", "membrane_bound", ["membrane_bound"], "limitations", r"membrane-presented/reporter"),
            ("M21B-EVID-007076", "membrane_bound", ["membrane_bound"], "limitations", r"juxtacrine/reporter"),
            ("M21B-EVID-007153", "soluble", ["soluble"], "evidence_summary", r"secreted Wnt antagonist"),
            ("M21B-EVID-007154", "membrane_bound", ["membrane_bound"], "limitations", r"membrane-tethered protease"),
            ("M21B-EVID-009291", "both_or_context_dependent", ["soluble", "membrane_bound"], "limitations", r"tmTNF versus solTNF"),
            ("M21B-EVID-009997", "soluble", ["soluble"], "evidence_summary", r"secreted TNF-alpha"),
            ("M21B-EVID-010734", "soluble", ["soluble"], "limitations", r"mature secreted clusterin"),
            ("M21B-EVID-010735", "soluble", ["soluble"], "limitations", r"mature secreted protein semantics"),
            ("M21B-EVID-010924", "soluble", ["soluble"], "evidence_summary", r"Soluble NG2/CSPG4"),
            ("M23B-EVID-000258", "ecm_retained", ["ecm_retained"], "evidence_summary", r"Fibrillar collagen I"),
            ("M23B-EVID-001454", "soluble", ["soluble"], "limitations", r"secreted opsonin"),
            ("M23B-EVID-001470", "soluble", ["soluble"], "limitations", r"Soluble intact biglycan"),
            ("M23B-EVID-001549", "membrane_bound", ["membrane_bound"], "evidence_summary", r"cell-associated EFNA2"),
        )
    }
)

SOURCE_REGISTER_FORM_OVERRIDES.update(
    {
        evidence_id: {
            "candidate": candidate,
            "signals": signals,
            "fields": fields,
            "pattern": re.compile(pattern, re.IGNORECASE),
        }
        for evidence_id, candidate, signals, fields, pattern in (
            ("M21B-EVID-000157", "soluble", ["soluble"], ("evidence_summary",), r"Human soluble P-selectin"),
            ("M21B-EVID-000249", "membrane_bound", ["membrane_bound"], ("evidence_summary", "limitations"), r"cell-surface nucleolin|cell-surface-exposed nucleolin"),
            ("M21B-EVID-000638", "both_or_context_dependent", ["soluble", "membrane_bound"], ("evidence_summary", "limitations"), r"CD160-GPI/TM-expressing|CD160 GPI versus transmembrane isoforms"),
            ("M21B-EVID-000774", "membrane_bound", ["membrane_bound"], ("limitations",), r"GPI-anchored RGMb topology"),
            ("M21B-EVID-002824", "soluble", ["soluble"], ("evidence_summary",), r"soluble Nogo-66 binding systems"),
            ("M21B-EVID-004681", "both_or_context_dependent", ["soluble", "membrane_bound"], ("limitations",), r"secreted/surface-bound Pra1"),
            ("M21B-EVID-005527", "both_or_context_dependent", ["soluble", "membrane_bound"], ("limitations",), r"membrane/soluble FLT3LG form"),
            ("M21B-EVID-005548", "both_or_context_dependent", ["soluble", "ecm_retained"], ("evidence_summary", "limitations"), r"Endothelial-cell-secreted EGFL7|matrix-attached EGFL7 context"),
            ("M21B-EVID-006331", "ecm_retained", ["ecm_retained"], ("limitations",), r"extracellular matrix assembly only"),
            ("M21B-EVID-006496", "ecm_retained", ["ecm_retained"], ("limitations",), r"extracellular matrix ligand/regulator"),
            ("M21B-EVID-010922", "soluble", ["soluble"], ("evidence_summary",), r"soluble LTalpha3"),
            ("M21B-EVID-010952", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-tethered ephrin-A ligand"),
            ("M21B-EVID-010953", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-tethered ephrin-A ligand"),
            ("M21B-EVID-010954", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-tethered ephrin-A ligand"),
            ("M21B-EVID-010955", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-tethered ephrin-A ligand"),
            ("M21B-EVID-010956", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-tethered ephrin-A ligand"),
            ("M21B-EVID-010957", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-tethered ephrin-A ligand"),
            ("M21B-EVID-010958", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-tethered ephrin-A ligand"),
            ("M21B-EVID-010988", "ecm_retained", ["ecm_retained"], ("evidence_summary",), r"cell-surface FGF2 presentation"),
            ("M23B-EVID-001602", "ecm_retained", ["ecm_retained"], ("evidence_summary",), r"cell-surface collagen-VI retention"),
        )
    }
)

SOURCE_REGISTER_FORM_OVERRIDES.update(
    {
        evidence_id: {
            "candidate": candidate,
            "signals": signals,
            "fields": fields,
            "pattern": re.compile(pattern, re.IGNORECASE),
        }
        for evidence_id, candidate, signals, fields, pattern in (
            ("M21B-EVID-000391", "soluble", ["soluble"], ("evidence_summary",), r"Soluble human IL-22"),
            ("M21B-EVID-000770", "soluble", ["soluble"], ("evidence_summary",), r"soluble SEMA3B treatment"),
            ("M21B-EVID-000794", "soluble", ["soluble"], ("limitations",), r"secreted BMP4 antagonist"),
            ("M21B-EVID-000898", "soluble", ["soluble"], ("evidence_summary",), r"soluble RECK and WNT7A"),
            ("M21B-EVID-000899", "soluble", ["soluble"], ("evidence_summary",), r"soluble RECK and WNT7B"),
            ("M21B-EVID-001428", "membrane_bound", ["membrane_bound"], ("evidence_summary", "limitations"), r"surface-bound C3b"),
            ("M21B-EVID-001429", "soluble", ["soluble"], ("evidence_summary",), r"Recombinant soluble C4b"),
            ("M21B-EVID-001432", "membrane_bound", ["membrane_bound"], ("limitations",), r"surface-bound iC3b"),
            ("M21B-EVID-001703", "soluble", ["soluble"], ("evidence_summary",), r"Soluble human IL-6"),
            ("M21B-EVID-001707", "both_or_context_dependent", ["soluble", "membrane_bound"], ("limitations",), r"membrane/oligomerized TNF|soluble TNF"),
            ("M21B-EVID-002102", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"secreted LGI1"),
            ("M21B-EVID-002112", "soluble", ["soluble"], ("evidence_summary",), r"secreted LGI2"),
            ("M21B-EVID-002113", "soluble", ["soluble"], ("evidence_summary",), r"secreted LGI3"),
            ("M21B-EVID-002835", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"secreted LGI1"),
            ("M21B-EVID-002914", "soluble", ["soluble"], ("evidence_summary",), r"soluble BAG6/BAT3 C-terminal fragment"),
            ("M21B-EVID-002915", "soluble", ["soluble"], ("evidence_summary",), r"soluble recombinant HLA-Cw3"),
            ("M21B-EVID-003053", "soluble", ["soluble"], ("limitations",), r"secreted HtrA1 protease"),
            ("M21B-EVID-004650", "both_or_context_dependent", ["soluble", "membrane_bound"], ("evidence_summary",), r"soluble and cell-associated SPICE"),
            ("M21B-EVID-004651", "both_or_context_dependent", ["soluble", "membrane_bound"], ("evidence_summary",), r"soluble and cell-associated SPICE"),
            ("M21B-EVID-005373", "both_or_context_dependent", ["soluble", "membrane_bound"], ("evidence_summary", "limitations"), r"membrane-presented DLL4|soluble DLL4 binding"),
            ("M21B-EVID-005378", "membrane_bound", ["membrane_bound"], ("evidence_summary",), r"cell-surface-anchored CTHRC1"),
            ("M21B-EVID-005379", "membrane_bound", ["membrane_bound"], ("evidence_summary",), r"cell-surface-anchored CTHRC1"),
            ("M21B-EVID-005380", "membrane_bound", ["membrane_bound"], ("evidence_summary",), r"cell-surface-anchored CTHRC1"),
            ("M21B-EVID-005396", "soluble", ["soluble"], ("limitations",), r"secreted SFRP2"),
            ("M21B-EVID-005397", "soluble", ["soluble"], ("evidence_summary",), r"secreted SFRP1 application"),
            ("M21B-EVID-005559", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"Secreted FAM3C/ILEI|secreted FAM3C/ILEI"),
            ("M21B-EVID-005781", "soluble", ["soluble"], ("evidence_summary",), r"astrocyte-secreted antagonist"),
            ("M21B-EVID-006123", "soluble", ["soluble"], ("limitations",), r"secreted ALKAL1/FAM150A"),
            ("M21B-EVID-006124", "soluble", ["soluble"], ("limitations",), r"secreted ALKAL2/FAM150B"),
            ("M21B-EVID-006158", "soluble", ["soluble"], ("limitations",), r"secreted Cholesin/C7orf50"),
            ("M21B-EVID-006165", "soluble", ["soluble"], ("limitations",), r"secreted PLAU/pro-uPA"),
            ("M21B-EVID-006208", "both_or_context_dependent", ["soluble", "ecm_retained"], ("evidence_summary", "limitations"), r"cell-surface capture|unconventional FGF2 secretion"),
            ("M21B-EVID-006465", "both_or_context_dependent", ["soluble", "membrane_bound"], ("evidence_summary", "limitations"), r"cell-surface-anchored CTHRC1|secreted/cell-surface-anchored Wnt cofactor"),
            ("M21B-EVID-006514", "soluble", ["soluble"], ("limitations",), r"secreted C1QTNF5/CTRP5"),
            ("M21B-EVID-006586", "soluble", ["soluble"], ("limitations",), r"secreted tectorial-membrane structural protein"),
            ("M21B-EVID-006587", "soluble", ["soluble"], ("limitations",), r"secreted tectorial-membrane structural protein"),
            ("M21B-EVID-006608", "soluble", ["soluble"], ("evidence_summary",), r"secreted ligand"),
            ("M21B-EVID-006609", "soluble", ["soluble"], ("evidence_summary",), r"secreted ligand"),
            ("M21B-EVID-006610", "soluble", ["soluble"], ("evidence_summary",), r"secreted ligand"),
            ("M21B-EVID-006611", "soluble", ["soluble"], ("evidence_summary",), r"secreted ligand"),
            ("M21B-EVID-006615", "soluble", ["soluble"], ("limitations",), r"soluble ECD/SPR assay context"),
            ("M21B-EVID-006642", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"Secreted human/mouse EGFL7|secreted EGFL7"),
            ("M21B-EVID-006643", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"Secreted human/mouse EGFL7|secreted EGFL7"),
            ("M21B-EVID-006644", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"Secreted human/mouse EGFL7|secreted EGFL7"),
            ("M21B-EVID-006911", "ecm_retained", ["ecm_retained"], ("evidence_summary", "limitations"), r"matrix-bound neurturin|immobilized matrix-bound neurturin"),
            ("M21B-EVID-006912", "ecm_retained", ["ecm_retained"], ("evidence_summary", "limitations"), r"matrix-bound artemin|immobilized matrix-bound artemin"),
            ("M21B-EVID-000824", "soluble", ["soluble"], ("evidence_summary",), r"extracellular recombinant S100A4"),
            ("M21B-EVID-008802", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"soluble IL-11/IL-11R/gp130"),
            ("M21B-EVID-001700", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"Soluble tagged IL-11|soluble biochemical"),
            ("M21B-EVID-002817", "membrane_bound", ["membrane_bound"], ("evidence_summary",), r"cell-bound iC3b/C3dg"),
            ("M21B-EVID-002900", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-associated MICB"),
            ("M21B-EVID-002901", "membrane_bound", ["membrane_bound"], ("limitations",), r"GPI-linked ULBP1/RAET1I"),
            ("M21B-EVID-002903", "membrane_bound", ["membrane_bound"], ("limitations",), r"GPI-linked ULBP3/RAET1N"),
            ("M21B-EVID-003194", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-tethered ligand"),
            ("M21B-EVID-005513", "ecm_retained", ["ecm_retained"], ("evidence_summary", "limitations"), r"cell-surface GPC5 binding to Wnt3a|cell-surface WNT3A-GPC5"),
            ("M21B-EVID-006080", "ecm_retained", ["ecm_retained"], ("evidence_summary",), r"cell-surface proteoglycan retains FGF2"),
            ("M21B-EVID-006201", "ecm_retained", ["ecm_retained"], ("limitations",), r"cell-surface HS-dependent FGF2 capture/presentation"),
            ("M21B-EVID-006202", "ecm_retained", ["ecm_retained"], ("limitations",), r"FGF4 presentation"),
            ("M21B-EVID-006203", "ecm_retained", ["ecm_retained"], ("limitations",), r"FGF8 presentation"),
            ("M21B-EVID-006212", "ecm_retained", ["ecm_retained"], ("evidence_summary", "limitations"), r"matrix-bound growth factor|matrix binding/release"),
            ("M21B-EVID-006213", "ecm_retained", ["ecm_retained"], ("evidence_summary", "limitations"), r"perlecan HS|presented/bound by perlecan HS"),
            ("M21B-EVID-006502", "membrane_bound", ["membrane_bound"], ("evidence_summary",), r"cell-surface localization"),
            ("M21B-EVID-006668", "ecm_retained", ["ecm_retained"], ("evidence_summary",), r"syndecan-1 heparan-sulfate chains bind HGF"),
            ("M21B-EVID-003784", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-associated/glycosylated podoplanin"),
            ("M21B-EVID-000779", "both_or_context_dependent", ["soluble", "membrane_bound"], ("limitations",), r"GPI-linked/cleaved HJV isoform"),
            ("M21B-EVID-000780", "membrane_bound", ["membrane_bound"], ("evidence_summary",), r"cell-associated .* HJV"),
            ("M21B-EVID-002453", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-associated prototoxin"),
            ("M21B-EVID-002563", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-associated Piezo1"),
            ("M21B-EVID-002564", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-associated Piezo2"),
            ("M21B-EVID-002783", "membrane_bound", ["membrane_bound"], ("limitations",), r"GPI-linked m157"),
            ("M21B-EVID-002899", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-associated stress-inducible MICA"),
            ("M21B-EVID-003132", "membrane_bound", ["membrane_bound"], ("limitations",), r"GPI-anchored topology"),
            ("M21B-EVID-005174", "membrane_bound", ["membrane_bound"], ("limitations",), r"GPI-anchored IgLON"),
            ("M21B-EVID-005175", "membrane_bound", ["membrane_bound"], ("limitations",), r"GPI-anchored IgLON"),
            ("M21B-EVID-005791", "membrane_bound", ["membrane_bound"], ("limitations",), r"GPI-anchored ephrin-A3"),
            ("M21B-EVID-005798", "membrane_bound", ["membrane_bound"], ("evidence_summary", "limitations"), r"GPI-linked non-canonical Notch ligand|GPI-linked contactin"),
            ("M21B-EVID-006117", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"secreted AGR2"),
            ("M21B-EVID-006121", "membrane_bound", ["membrane_bound"], ("limitations",), r"IZUMO1 sperm membrane"),
            ("M21B-EVID-006137", "membrane_bound", ["membrane_bound"], ("limitations",), r"GPI-anchored ephrin-A4"),
            ("M21B-EVID-006376", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-associated glycoprotein ligand"),
            ("M21B-EVID-006460", "membrane_bound", ["membrane_bound"], ("limitations",), r"necrotic-cell-associated ligand"),
            ("M21B-EVID-006467", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"secreted NP2/NPTX2|NPTX2 as a secreted"),
            ("M21B-EVID-006468", "membrane_bound", ["membrane_bound"], ("evidence_summary", "limitations"), r"membrane-associated .* ANXA2"),
            ("M21B-EVID-006556", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"soluble HLA-G1"),
            ("M21B-EVID-006716", "both_or_context_dependent", ["soluble", "membrane_bound"], ("limitations",), r"shed-versus-cell-associated SDC2"),
            ("M21B-EVID-006941", "both_or_context_dependent", ["soluble", "membrane_bound"], ("evidence_summary", "limitations"), r"soluble and membrane-associated DLK2|DLK2 membrane/soluble form"),
            ("M23B-EVID-001546", "membrane_bound", ["membrane_bound"], ("evidence_summary",), r"GPI-linked ligand"),
            ("M21B-EVID-006667", "membrane_bound", ["membrane_bound"], ("evidence_summary",), r"FLRT2.*cell-surface receptor-ligand pair"),
        )
    }
)

SOURCE_REGISTER_FORM_OVERRIDES.update(
    {
        "M21B-EVID-000294": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bmembrane-associated Nodal\b", re.IGNORECASE),
        },
        "M21B-EVID-000413": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\bsoluble RANKL\b", re.IGNORECASE),
        },
        "M21B-EVID-000414": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\bsoluble IL-22\b", re.IGNORECASE),
        },
        "M21B-EVID-000512": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\bsoluble CD100\b", re.IGNORECASE),
        },
        "M21B-EVID-002936": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\breleased vimentin\b", re.IGNORECASE),
        },
        "M23B-EVID-001488": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\bmicroglia-released Gal3\b", re.IGNORECASE),
        },
    }
)

SOURCE_REGISTER_FORM_OVERRIDES.update(
    {
        "M20B-EVID-003285": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\bEphrin-A1 is membrane-tethered\b", re.IGNORECASE),
        },
        "M20B-EVID-003287": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\bsoluble EFNA1-Fc\b", re.IGNORECASE),
        },
        "M23B-EVID-001429": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\bReleased gp96\b", re.IGNORECASE),
        },
        "M24B-EVID-000110": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted Gal-9\b", re.IGNORECASE),
        },
    }
)

SOURCE_REGISTER_FORM_OVERRIDES.update(
    {
        "M21B-EVID-000337": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\btransmembrane chondroitin-sulfate-proteoglycan\b", re.IGNORECASE),
        },
        "M21B-EVID-000462": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\breleased growth-factor-domain\b", re.IGNORECASE),
        },
        "M21B-EVID-000785": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted antagonist\b", re.IGNORECASE),
        },
        "M21B-EVID-000791": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted antagonist\b", re.IGNORECASE),
        },
        "M21B-EVID-000792": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bdirect soluble antagonist-complex formation\b", re.IGNORECASE),
        },
        "M21B-EVID-000795": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted BMP6 antagonist\b", re.IGNORECASE),
        },
        "M21B-EVID-000796": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted BMP7 antagonist\b", re.IGNORECASE),
        },
        "M21B-EVID-000800": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted BMP2 antagonist\b", re.IGNORECASE),
        },
        "M21B-EVID-000801": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted BMP4 antagonist\b", re.IGNORECASE),
        },
        "M21B-EVID-000803": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted BMP4-associated antagonist\b", re.IGNORECASE),
        },
        "M21B-EVID-000805": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble ECM-DAMP\b", re.IGNORECASE),
        },
        "M21B-EVID-000806": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble ECM-DAMP\b", re.IGNORECASE),
        },
        "M21B-EVID-000810": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble decorin\b", re.IGNORECASE),
        },
        "M21B-EVID-000812": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble ECM-DAMP\b", re.IGNORECASE),
        },
        "M21B-EVID-000813": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble ECM-DAMP\b", re.IGNORECASE),
        },
        "M21B-EVID-000857": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble-CD93 opsonin\b", re.IGNORECASE),
        },
        "M21B-EVID-000927": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted processed heterodimeric clusterin\b", re.IGNORECASE),
        },
        "M21B-EVID-001061": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble/peptide versus membrane-receptor context\b", re.IGNORECASE),
        },
        "M23B-EVID-000350": {
            "candidate": "ecm_retained",
            "signals": ["ecm_retained"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bimmobilized/matrix-associated ligand\b", re.IGNORECASE),
        },
        "M23B-EVID-000475": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bSoluble/trimeric CD40L\b", re.IGNORECASE),
        },
        "M23B-EVID-000476": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bSoluble/trimeric CD40L\b", re.IGNORECASE),
        },
        "M23B-EVID-000477": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bSoluble/trimeric CD40L\b", re.IGNORECASE),
        },
        "M23B-EVID-000581": {
            "candidate": "both_or_context_dependent",
            "signals": ["soluble", "membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bMembrane-tethered adhesion and soluble chemotaxis\b", re.IGNORECASE),
        },
        "M23B-EVID-000582": {
            "candidate": "both_or_context_dependent",
            "signals": ["soluble", "membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bMembrane-tethered adhesion and soluble chemotaxis\b", re.IGNORECASE),
        },
        "M23B-EVID-000606": {
            "candidate": "both_or_context_dependent",
            "signals": ["soluble", "membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bMembrane versus soluble CXCL16\b", re.IGNORECASE),
        },
        "M23B-EVID-000610": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bGPI-anchored ephrin-A2 cell\b", re.IGNORECASE),
        },
        "M23B-EVID-000611": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bGPI-anchored ephrin-A2 cell\b", re.IGNORECASE),
        },
        "M23B-EVID-000612": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bGPI-anchored ephrin-A2 cell\b", re.IGNORECASE),
        },
        "M23B-EVID-000709": {
            "candidate": "ecm_retained",
            "signals": ["ecm_retained"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bfibrin betaN domains after fibrin formation\b", re.IGNORECASE),
        },
        "M23B-EVID-000711": {
            "candidate": "ecm_retained",
            "signals": ["ecm_retained"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bfibrin betaN domains after fibrin formation\b", re.IGNORECASE),
        },
    }
)

SOURCE_REGISTER_FORM_OVERRIDES.update(
    {
        "M21B-EVID-000535": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bJAM-C transmembrane endothelial/platelet presentation\b", re.IGNORECASE),
        },
        "M21B-EVID-000837": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\bextracellular or microglia-secreted galectin-3\b", re.IGNORECASE),
        },
        "M21B-EVID-000928": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\bmature secreted clusterin\b", re.IGNORECASE),
        },
        "M21B-EVID-001104": {
            "candidate": "both_or_context_dependent",
            "signals": ["soluble", "ecm_retained"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted-matrix/bridging topology\b", re.IGNORECASE),
        },
        "M21B-EVID-006592": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bRSPO1 as a secreted Wnt potentiator\b", re.IGNORECASE),
        },
        "M21B-EVID-006603": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted-antagonist topology\b", re.IGNORECASE),
        },
        "M21B-EVID-006605": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\brecombinant secreted FAM19A1\b", re.IGNORECASE),
        },
        "M21B-EVID-006639": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\bSecreted human/mouse EGFL7\b", re.IGNORECASE),
        },
        "M21B-EVID-006915": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\bextracellular purified/secreted UMOD\b", re.IGNORECASE),
        },
        "M21B-EVID-006920": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\bsecreted cyclophilin A\b", re.IGNORECASE),
        },
        "M21B-EVID-006924": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted FAM3B\b", re.IGNORECASE),
        },
        "M21B-EVID-006943": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bmature secreted MSMP/PSMP\b", re.IGNORECASE),
        },
        "M21B-EVID-006948": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\btransmembrane semaphorin\b", re.IGNORECASE),
        },
        "M21B-EVID-007067": {
            "candidate": "both_or_context_dependent",
            "signals": ["soluble", "membrane_bound"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\bfull-length CD23 liposomes and soluble CD23\b", re.IGNORECASE),
        },
        "M21B-EVID-007079": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bFCN2–MASP-2 soluble complex association\b", re.IGNORECASE),
        },
        "M21B-EVID-007080": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bFCN3–MASP-2 soluble complex association\b", re.IGNORECASE),
        },
        "M21B-EVID-007081": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bFCN1–MASP-2 soluble complex association\b", re.IGNORECASE),
        },
        "M21B-EVID-007082": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bcollectin-11–MASP-2 soluble complex association\b", re.IGNORECASE),
        },
        "M21B-EVID-007086": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bcollectin-10–MASP-3 soluble complex association\b", re.IGNORECASE),
        },
        "M21B-EVID-007087": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bcollectin-11–MASP-1 soluble complex association\b", re.IGNORECASE),
        },
        "M21B-EVID-007088": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bcollectin-11–MASP-3 soluble complex association\b", re.IGNORECASE),
        },
        "M21B-EVID-010924": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("evidence_summary",),
            "pattern": re.compile(r"\bSoluble NG2/CSPG4\b", re.IGNORECASE),
        },
        "M21B-EVID-010939": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\btransmembrane-semaphorin\b", re.IGNORECASE),
        },
        "M21B-EVID-010943": {
            "candidate": "both_or_context_dependent",
            "signals": ["soluble", "membrane_bound"],
            "fields": ("evidence_summary", "limitations"),
            "pattern": re.compile(r"\b(?:APP or soluble APP fragments|full-length APP or soluble APP-fragment)\b", re.IGNORECASE),
        },
        "M21B-EVID-010983": {
            "candidate": "ecm_retained",
            "signals": ["ecm_retained"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bcollagen-I trimer/fibril component\b", re.IGNORECASE),
        },
    }
)

SOURCE_REGISTER_FORM_OVERRIDES.update(
    {
        "M21B-EVID-000463": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\breleased growth-factor-domain semantics\b", re.IGNORECASE),
        },
        "M21B-EVID-001862": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bextracellular/secreted CIRP form\b", re.IGNORECASE),
        },
        "M21B-EVID-002084": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted hexameric Cbln1\b", re.IGNORECASE),
        },
        "M21B-EVID-002085": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted hexameric Cbln1\b", re.IGNORECASE),
        },
        "M21B-EVID-002087": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted adaptor\b", re.IGNORECASE),
        },
        "M21B-EVID-002095": {
            "candidate": "both_or_context_dependent",
            "signals": ["soluble", "membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bGPI/secreted-domain context\b", re.IGNORECASE),
        },
        "M21B-EVID-002131": {
            "candidate": "ecm_retained",
            "signals": ["ecm_retained"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bextracellular matrix association/modulation\b", re.IGNORECASE),
        },
        "M21B-EVID-002323": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted angiogenin\b", re.IGNORECASE),
        },
        "M21B-EVID-002331": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted catalytically inactive CA10\b", re.IGNORECASE),
        },
        "M21B-EVID-002417": {
            "candidate": "ecm_retained",
            "signals": ["ecm_retained"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bextracellular-matrix inhibitor\b", re.IGNORECASE),
        },
        "M21B-EVID-002444": {
            "candidate": "both_or_context_dependent",
            "signals": ["soluble", "membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble versus GPI-tethered LYNX1\b", re.IGNORECASE),
        },
        "M21B-EVID-002763": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bTransmembrane semaphorin\b", re.IGNORECASE),
        },
        "M21B-EVID-002797": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bglycosylated secreted-ligand\b", re.IGNORECASE),
        },
        "M21B-EVID-003036": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted pro-cathepsin D\b", re.IGNORECASE),
        },
        "M21B-EVID-003054": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted latent pro-heparanase-1\b", re.IGNORECASE),
        },
        "M21B-EVID-004612": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted proteoglycan\b", re.IGNORECASE),
        },
        "M21B-EVID-004613": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted serglycin\b", re.IGNORECASE),
        },
        "M21B-EVID-004614": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted serglycin\b", re.IGNORECASE),
        },
        "M21B-EVID-005510": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\btransmembrane-collagen\b", re.IGNORECASE),
        },
        "M21B-EVID-005566": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted FGL2\b", re.IGNORECASE),
        },
        "M21B-EVID-005575": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\btransmembrane ULBP4\b", re.IGNORECASE),
        },
        "M21B-EVID-005780": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bastrocyte-secreted CHRDL1\b", re.IGNORECASE),
        },
        "M21B-EVID-005817": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bastrocyte-secreted GPC4\b", re.IGNORECASE),
        },
        "M21B-EVID-005909": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\btransmembrane Sema4B\b", re.IGNORECASE),
        },
        "M21B-EVID-005975": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted microglial LRRC15\b", re.IGNORECASE),
        },
        "M21B-EVID-006091": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted C10orf99/GPR15LG\b", re.IGNORECASE),
        },
        "M21B-EVID-006099": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bextracellular/unconventionally secreted TULP1\b", re.IGNORECASE),
        },
        "M21B-EVID-006113": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bmembrane-bound KACL\b", re.IGNORECASE),
        },
        "M21B-EVID-006119": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bTFF1 secreted-protein context\b", re.IGNORECASE),
        },
        "M21B-EVID-006120": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bTFF2 secreted-protein context\b", re.IGNORECASE),
        },
        "M21B-EVID-006193": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted KPI-containing APPs770\b", re.IGNORECASE),
        },
        "M21B-EVID-006362": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bastrocyte-secreted/neuronal accessory-protein context\b", re.IGNORECASE),
        },
        "M21B-EVID-006457": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bTAFA4/FAM19A4 as a secreted ligand\b", re.IGNORECASE),
        },
        "M21B-EVID-006462": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bSPARC as a secreted counter-ligand\b", re.IGNORECASE),
        },
        "M21B-EVID-006480": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted glypican-1\b", re.IGNORECASE),
        },
        "M21B-EVID-006493": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted SEMA3C\b", re.IGNORECASE),
        },
        "M21B-EVID-006497": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bdirect soluble LTalpha3\b", re.IGNORECASE),
        },
        "M21B-EVID-006507": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted lacritin\b", re.IGNORECASE),
        },
        "M21B-EVID-006538": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bmembrane-bound/clustered ligand\b", re.IGNORECASE),
        },
        "M21B-EVID-006662": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bmembrane-bound ligand/receptor clustering\b", re.IGNORECASE),
        },
        "M21B-EVID-007033": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\breleased C-terminal-fragment\b", re.IGNORECASE),
        },
    }
)

SOURCE_REGISTER_FORM_OVERRIDES.update(
    {
        "M21B-EVID-001861": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bmonomeric soluble PGLYRP1\b", re.IGNORECASE),
        },
        "M21B-EVID-002787": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble-HLA-G signaling\b", re.IGNORECASE),
        },
        "M21B-EVID-004607": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble GPNMB extracellular-domain form\b", re.IGNORECASE),
        },
        "M21B-EVID-004611": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble GPNMB extracellular-domain form\b", re.IGNORECASE),
        },
        "M21B-EVID-004640": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble complement edge\b", re.IGNORECASE),
        },
        "M21B-EVID-004642": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble complement inhibition\b", re.IGNORECASE),
        },
        "M21B-EVID-004643": {
            "candidate": "both_or_context_dependent",
            "signals": ["soluble", "membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble versus cell-surface form\b", re.IGNORECASE),
        },
        "M21B-EVID-004644": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted flavivirus NS1\b", re.IGNORECASE),
        },
        "M21B-EVID-004682": {
            "candidate": "both_or_context_dependent",
            "signals": ["soluble", "membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bPra1 surface/secreted form\b", re.IGNORECASE),
        },
        "M21B-EVID-004684": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted fungal protease/inhibitor\b", re.IGNORECASE),
        },
        "M21B-EVID-004809": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bpathogen-secreted receptor antagonist\b", re.IGNORECASE),
        },
        "M21B-EVID-004876": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted parasite calreticulin\b", re.IGNORECASE),
        },
        "M21B-EVID-004877": {
            "candidate": "both_or_context_dependent",
            "signals": ["soluble", "membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsurface/secreted TsPmy\b", re.IGNORECASE),
        },
        "M21B-EVID-004880": {
            "candidate": "both_or_context_dependent",
            "signals": ["soluble", "membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted/surface-associated EmCRT\b", re.IGNORECASE),
        },
        "M21B-EVID-004881": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted EmCRT S-domain\b", re.IGNORECASE),
        },
        "M21B-EVID-004882": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted H\. contortus GAPDH\b", re.IGNORECASE),
        },
        "M21B-EVID-004883": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsecreted H\. contortus GAPDH\b", re.IGNORECASE),
        },
        "M21B-EVID-004889": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\brecombinant/secreted Sapt1\b", re.IGNORECASE),
        },
        "M21B-EVID-004890": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\brecombinant/secreted Sapt1\b", re.IGNORECASE),
        },
        "M21B-EVID-005409": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble/trimeric ligand\b", re.IGNORECASE),
        },
        "M21B-EVID-005455": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bprocessed soluble FNDC4\b", re.IGNORECASE),
        },
        "M21B-EVID-005528": {
            "candidate": "ecm_retained",
            "signals": ["ecm_retained"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bmatrix-bound ligand\b", re.IGNORECASE),
        },
        "M21B-EVID-006140": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble/cleaved EpEX\b", re.IGNORECASE),
        },
        "M21B-EVID-006220": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble CD23\b", re.IGNORECASE),
        },
        "M21B-EVID-006674": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bsoluble tubby\b", re.IGNORECASE),
        },
        "M21B-EVID-006687": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bshed ectodomain\b", re.IGNORECASE),
        },
        "M21B-EVID-006688": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bshed ectodomain\b", re.IGNORECASE),
        },
        "M21B-EVID-006689": {
            "candidate": "soluble",
            "signals": ["soluble"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bshed ectodomain\b", re.IGNORECASE),
        },
        "M21B-EVID-006946": {
            "candidate": "membrane_bound",
            "signals": ["membrane_bound"],
            "fields": ("limitations",),
            "pattern": re.compile(r"\bmembrane LTalpha1beta2-to-LTBR ligand\b", re.IGNORECASE),
        },
    }
)

SOURCE_REGISTER_FORM_OVERRIDES.update(
    {
        evidence_id: {
            "candidate": candidate,
            "signals": signals,
            "fields": fields,
            "pattern": re.compile(pattern, re.IGNORECASE),
        }
        for evidence_id, candidate, signals, fields, pattern in (
            ("M20B-EVID-003426", "soluble", ["soluble"], ("evidence_summary",), r"FGF11 is an unconventional, noncanonical secreted FHF"),
            ("M21B-EVID-002700", "soluble", ["soluble"], ("evidence_summary",), r"SAP130 released from necrotic cells"),
            ("M21B-EVID-004645", "soluble", ["soluble"], ("limitations",), r"Preserve soluble NS1"),
            ("M21B-EVID-004800", "soluble", ["soluble"], ("evidence_summary",), r"StcE as a secreted metalloprotease"),
            ("M21B-EVID-004807", "soluble", ["soluble"], ("evidence_summary",), r"aureolysin as a secreted C3-cleaving complement inhibitor"),
            ("M21B-EVID-004825", "soluble", ["soluble"], ("evidence_summary",), r"Sat as a secreted autotransporter complement protease"),
            ("M21B-EVID-004826", "soluble", ["soluble"], ("evidence_summary",), r"Sat as a secreted autotransporter complement protease"),
            ("M21B-EVID-004827", "soluble", ["soluble"], ("evidence_summary",), r"Sat as a secreted autotransporter complement protease"),
            ("M21B-EVID-004828", "soluble", ["soluble"], ("evidence_summary",), r"Sat as a secreted autotransporter complement protease"),
            ("M21B-EVID-004829", "soluble", ["soluble"], ("evidence_summary",), r"Sat as a secreted autotransporter complement protease"),
            ("M21B-EVID-004830", "soluble", ["soluble"], ("evidence_summary",), r"Sat as a secreted autotransporter complement protease"),
            ("M21B-EVID-004831", "soluble", ["soluble"], ("evidence_summary",), r"Sat as a secreted autotransporter complement protease"),
            ("M21B-EVID-004832", "soluble", ["soluble"], ("evidence_summary",), r"Sat as a secreted autotransporter complement protease"),
            ("M21B-EVID-004833", "soluble", ["soluble"], ("evidence_summary",), r"Sat as a secreted autotransporter complement protease"),
            ("M21B-EVID-004834", "soluble", ["soluble"], ("evidence_summary",), r"Sat as a secreted autotransporter complement protease"),
            ("M21B-EVID-004905", "soluble", ["soluble"], ("evidence_summary",), r"FhSrp1/FhSrp2 as secreted Fasciola complement-evasion serpins"),
            ("M21B-EVID-004911", "both_or_context_dependent", ["soluble", "membrane_bound"], ("evidence_summary",), r"membrane and soluble forms retaining C3b binding"),
            ("M21B-EVID-004912", "both_or_context_dependent", ["soluble", "membrane_bound"], ("evidence_summary",), r"160-kDa soluble and 185-kDa membrane CRP/Gp160 forms"),
            ("M21B-EVID-004915", "soluble", ["soluble"], ("evidence_summary",), r"Secreted H\. contortus calreticulin"),
            ("M21B-EVID-004916", "soluble", ["soluble"], ("evidence_summary",), r"hookworm calreticulin among secreted products"),
            ("M21B-EVID-004917", "soluble", ["soluble"], ("evidence_summary",), r"hookworm calreticulin among secreted products"),
            ("M21B-EVID-004919", "soluble", ["soluble"], ("evidence_summary",), r"shed 87-93-kDa T-DAF activity"),
            ("M21B-EVID-004920", "soluble", ["soluble"], ("evidence_summary",), r"shed 87-93-kDa T-DAF activity"),
            ("M21B-EVID-004923", "soluble", ["soluble"], ("evidence_summary",), r"Released parasite OvCALR"),
            ("M21B-EVID-005419", "soluble", ["soluble"], ("evidence_summary",), r"secreted S100A8/A9 carrying arachidonic acid"),
            ("M21B-EVID-005457", "soluble", ["soluble"], ("evidence_summary",), r"secreted BAI1 extracellular cleavage products"),
            ("M21B-EVID-005552", "soluble", ["soluble"], ("evidence_summary",), r"Secreted or recombinant human CTRP8"),
            ("M21B-EVID-005740", "both_or_context_dependent", ["soluble", "membrane_bound"], ("limitations",), r"neuron-derived membrane/soluble fractalkine"),
            ("M21B-EVID-005816", "soluble", ["soluble"], ("evidence_summary",), r"soluble GPC4"),
            ("M21B-EVID-006087", "soluble", ["soluble"], ("evidence_summary",), r"soluble LRIG1 ectodomain"),
            ("M21B-EVID-006221", "soluble", ["soluble"], ("evidence_summary",), r"Recombinant human soluble CD23"),
            ("M21B-EVID-006224", "soluble", ["soluble"], ("evidence_summary",), r"secreted PLA2-IIA as a direct integrin ligand"),
            ("M21B-EVID-006225", "soluble", ["soluble"], ("evidence_summary",), r"secreted PLA2-IIA as a direct integrin ligand"),
            ("M21B-EVID-006226", "soluble", ["soluble"], ("evidence_summary",), r"secreted PLA2-IIA as a direct integrin ligand"),
            ("M21B-EVID-006239", "soluble", ["soluble"], ("evidence_summary",), r"soluble/recombinant EhCP5"),
            ("M21B-EVID-006297", "soluble", ["soluble"], ("evidence_summary",), r"secreted UGRP1/SCGB3A2"),
            ("M21B-EVID-007077", "soluble", ["soluble"], ("limitations",), r"MBL–MASP-2 soluble complex association"),
            ("M21B-EVID-007078", "soluble", ["soluble"], ("limitations",), r"MBL–MASP-1 soluble complex association"),
            ("M21B-EVID-005587", "membrane_bound", ["membrane_bound"], ("limitations",), r"membrane-anchored sperm"),
            ("M23B-EVID-001424", "soluble", ["soluble"], ("limitations",), r"extracellular Hsp90alpha"),
            ("M23B-EVID-001425", "soluble", ["soluble"], ("evidence_summary",), r"Extracellular Hsp90alpha"),
            ("M23B-EVID-001426", "soluble", ["soluble"], ("evidence_summary",), r"Extracellular Hsp90alpha"),
            ("M23B-EVID-001427", "soluble", ["soluble"], ("limitations",), r"released gp96/gp96-peptide complexes"),
            ("M23B-EVID-001437", "soluble", ["soluble"], ("evidence_summary",), r"Extracellular ISG15"),
            ("M24B-EVID-000167", "soluble", ["soluble"], ("evidence_summary",), r"Soluble decorin"),
            ("M24B-EVID-000195", "soluble", ["soluble"], ("evidence_summary",), r"LTB4 was detectable and released from traumatized rat spinal cord slices"),
            ("M21B-EVID-001171", "both_or_context_dependent", ["soluble", "membrane_bound"], ("evidence_summary",), r"N-cadherin and FGFR1 cocluster.*soluble N-cadherin-Fc"),
            ("M21B-EVID-003155", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"Soluble human RGMa\.Fc"),
            ("M21B-EVID-004606", "both_or_context_dependent", ["soluble", "membrane_bound"], ("limitations",), r"membrane or shed GPNMB/DC-HIL"),
            ("M21B-EVID-005415", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"soluble CEACAM8"),
            ("M21B-EVID-005478", "soluble", ["soluble"], ("evidence_summary",), r"Human and murine soluble PSGL1"),
            ("M24B-EVID-000008", "soluble", ["soluble"], ("evidence_summary",), r"Sustained extracellular ATP"),
            ("M21B-EVID-002108", "soluble", ["soluble"], ("evidence_summary",), r"Hevin as an astrocyte-secreted bridge"),
            ("M21B-EVID-002109", "soluble", ["soluble"], ("evidence_summary",), r"Hevin as an astrocyte-secreted bridge"),
            ("M21B-EVID-002155", "both_or_context_dependent", ["soluble", "membrane_bound"], ("evidence_summary",), r"JAM-B/JAM-C transfectants.*recombinant soluble Ig-domain proteins"),
            ("M21B-EVID-002557", "membrane_bound", ["membrane_bound"], ("evidence_summary", "limitations"), r"membrane-bound NPTXR/NPR"),
            ("M21B-EVID-000121", "both_or_context_dependent", ["soluble", "ecm_retained"], ("evidence_summary", "limitations"), r"immobilized/polymerized.*fibrinogen|fibrinogen-versus-fibrin form"),
            ("M21B-EVID-000814", "both_or_context_dependent", ["soluble", "ecm_retained"], ("evidence_summary",), r"matrix-associated TGF-beta1 bioactivity depending on decorin form and assay context"),
            ("M21B-EVID-003183", "both_or_context_dependent", ["soluble", "ecm_retained"], ("evidence_summary", "limitations"), r"thrombin-cleaved or polymeric osteopontin|processed/polymeric osteopontin"),
            ("M21B-EVID-003184", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"Thrombin-cleaved human osteopontin N-terminal fragment"),
            ("M21B-EVID-004722", "membrane_bound", ["membrane_bound"], ("evidence_summary",), r"Hsf as an H\. influenzae vitronectin-recruiting surface fibril"),
            ("M21B-EVID-004723", "both_or_context_dependent", ["soluble", "membrane_bound"], ("evidence_summary",), r"surface-expressed and soluble E\. coli-expressed Protein E variants"),
            ("M21B-EVID-007028", "soluble", ["soluble"], ("evidence_summary",), r"Soluble human growth hormone"),
            ("M21B-EVID-000543", "both_or_context_dependent", ["soluble", "membrane_bound"], ("evidence_summary", "limitations"), r"recombinant soluble EPCR|soluble versus endothelial EPCR"),
            ("M21B-EVID-000709", "membrane_bound", ["membrane_bound"], ("evidence_summary",), r"cell-surface human VEGF-C/VEGF-D"),
            ("M21B-EVID-000710", "membrane_bound", ["membrane_bound"], ("evidence_summary",), r"cell-surface human VEGF-C/VEGF-D"),
            ("M21B-EVID-004638", "ecm_retained", ["ecm_retained"], ("evidence_summary",), r"biglycan as an MBL-binding extracellular-matrix proteoglycan"),
            ("M21B-EVID-004639", "soluble", ["soluble"], ("evidence_summary",), r"HNP-1 binding to intact C1q and fluid-phase complex formation"),
            ("M21B-EVID-004647", "soluble", ["soluble"], ("limitations",), r"soluble viral complement evasion"),
            ("M21B-EVID-004658", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"Purified soluble CCPH|CCPH soluble regulator"),
            ("M21B-EVID-004659", "soluble", ["soluble"], ("evidence_summary", "limitations"), r"Purified soluble CCPH|CCPH soluble regulator"),
            ("M21B-EVID-004687", "membrane_bound", ["membrane_bound"], ("evidence_summary", "limitations"), r"Gpd2.*surface protein|surface-exposed moonlighting Gpd2"),
            ("M21B-EVID-004688", "membrane_bound", ["membrane_bound"], ("evidence_summary", "limitations"), r"Gpd2.*surface protein|surface-exposed Gpd2"),
            ("M21B-EVID-004693", "membrane_bound", ["membrane_bound"], ("evidence_summary", "limitations"), r"surface acquisition|surface-exposed moonlighting AfEno1"),
            ("M21B-EVID-004695", "membrane_bound", ["membrane_bound"], ("evidence_summary", "limitations"), r"surface-exposed AfEno1"),
            ("M21B-EVID-004709", "membrane_bound", ["membrane_bound"], ("evidence_summary",), r"surface-exposed.*Lsa23"),
            ("M21B-EVID-004710", "membrane_bound", ["membrane_bound"], ("evidence_summary",), r"surface-exposed.*Lsa23"),
            ("M21B-EVID-004718", "membrane_bound", ["membrane_bound"], ("limitations",), r"surface-exposed Lpd"),
            ("M21B-EVID-006490", "both_or_context_dependent", ["soluble", "membrane_bound"], ("limitations",), r"soluble versus membrane SECTM1 isoforms"),
            ("M21B-EVID-006557", "both_or_context_dependent", ["soluble", "membrane_bound"], ("limitations",), r"soluble versus membrane HLA-G isoforms"),
        )
    }
)

SOURCE_REGISTER_FORM_OVERRIDES.update(
    {
        evidence_id: {
            "candidate": candidate,
            "signals": signals,
            "fields": fields,
            "pattern": re.compile(pattern, re.IGNORECASE),
        }
        for evidence_id, candidate, signals, fields, pattern in (
            (
                "M23B-EVID-000028",
                "ecm_retained",
                ["ecm_retained"],
                ("limitations",),
                r"retained as an ECM mechanistic anchor",
            ),
            (
                "M20B-EVID-003231",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"study addresses a secreted proteoglycan core protein",
            ),
            (
                "M23B-EVID-000190",
                "membrane_bound",
                ["membrane_bound"],
                ("limitations",),
                r"Homophilic receptor adhesion",
            ),
            (
                "M23B-EVID-000204",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary", "limitations"),
                r"Contact-dependent ephrin-A1-EphA2 activation|Ligand presentation/clustering is required",
            ),
            (
                "M23B-EVID-000653",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"trans-adhesion interaction",
            ),
            (
                "M23B-EVID-001433",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"interacted in trans",
            ),
            (
                "M20B-EVID-001461",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"intercellular adhesion complex",
            ),
            (
                "M20B-EVID-001470",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"intercellular adhesion complex",
            ),
            (
                "M20B-EVID-001479",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"intercellular adhesion complex",
            ),
            (
                "M20B-EVID-004190",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"trans-synaptic cell-adhesion interaction rather than a soluble ligand-receptor pair",
            ),
            (
                "M20B-EVID-004312",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"transsynaptic adhesion interaction rather than a conventional secreted-ligand system",
            ),
            (
                "M23B-EVID-001439",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"Extracellular ISG15",
            ),
            (
                "M23B-EVID-001345",
                "ecm_retained",
                ["ecm_retained"],
                ("evidence_summary",),
                r"keratinocytes on TG2 ECM",
            ),
            (
                "M23B-EVID-001346",
                "ecm_retained",
                ["ecm_retained"],
                ("evidence_summary",),
                r"keratinocytes on TG2 ECM",
            ),
            (
                "M23B-EVID-001347",
                "ecm_retained",
                ["ecm_retained"],
                ("evidence_summary",),
                r"keratinocytes on TG2 ECM",
            ),
            (
                "M20B-EVID-004268",
                "ecm_retained",
                ["ecm_retained"],
                ("evidence_summary",),
                r"adhesion/ECM receptor association rather than a classical soluble cytokine pair",
            ),
            (
                "M23B-EVID-000836",
                "ecm_retained",
                ["ecm_retained"],
                ("evidence_summary",),
                r"laminin to cytoskeleton and synaptic basement-membrane organization",
            ),
        )
    }
)

SOURCE_REGISTER_FORM_OVERRIDES.update(
    {
        evidence_id: {
            "candidate": candidate,
            "signals": signals,
            "fields": fields,
            "pattern": re.compile(pattern, re.IGNORECASE),
        }
        for evidence_id, candidate, signals, fields, pattern in (
            (
                "M20B-EVID-001922",
                "ecm_retained",
                ["ecm_retained"],
                ("evidence_summary",),
                r"adhesion/synaptic-matrix role",
            ),
            (
                "M23B-EVID-000672",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"heterophilic cell adhesion",
            ),
            (
                "M23B-EVID-000676",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"heterophilic axon[-–]Schwann adhesion",
            ),
            (
                "M23B-EVID-000189",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"heterophilic binding",
            ),
            (
                "M20B-EVID-000370",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"contact-mediated axonal growth/adhesion phenotypes",
            ),
            (
                "M23B-EVID-000453",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"contact-dependent neural crest repulsion",
            ),
            (
                "M23B-EVID-000304",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"NCAM1 homophilic binding",
            ),
            (
                "M23B-EVID-000305",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"NCAM1 homophilic engagement",
            ),
            (
                "M23B-EVID-000013",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"heterophilic adhesion",
            ),
            (
                "M23B-EVID-001141",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"PTPRS-NTRK3 transsynaptic adhesion",
            ),
            (
                "M23B-EVID-000893",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"trans-synaptic adhesion complex",
            ),
            (
                "M23B-EVID-000896",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"trans-synaptic organization",
            ),
            (
                "M23B-EVID-000884",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"trans-synaptic organizer output",
            ),
            (
                "M23B-EVID-001085",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"paranodal adhesion complex",
            ),
            (
                "M20B-EVID-002928",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"heterophilic ligand/co-receptor and topology is cis/trans context dependent",
            ),
            (
                "M23B-EVID-000193",
                "ecm_retained",
                ["ecm_retained"],
                ("limitations",),
                r"Matrix composition-dependent",
            ),
            (
                "M23B-EVID-000516",
                "ecm_retained",
                ["ecm_retained"],
                ("evidence_summary",),
                r"collagen-XI fibril.*matrix response branch",
            ),
            (
                "M23B-EVID-001359",
                "ecm_retained",
                ["ecm_retained"],
                ("evidence_summary",),
                r"VCAN/versican-associated matrix",
            ),
            (
                "M23B-EVID-001360",
                "ecm_retained",
                ["ecm_retained"],
                ("evidence_summary",),
                r"VCAN/versican-associated matrix",
            ),
            (
                "M23B-EVID-001361",
                "ecm_retained",
                ["ecm_retained"],
                ("evidence_summary",),
                r"VCAN/versican-associated matrix",
            ),
        )
    }
)

SOURCE_FORM_OVERRIDES.update(
    {
        evidence_id: {
            "candidate": candidate,
            "signals": signals,
            "fields": fields,
            "pattern": re.compile(pattern, re.IGNORECASE),
        }
        for evidence_id, candidate, signals, fields, pattern in (
            (
                "M20B-EVID-002539",
                "membrane_bound",
                ["membrane_bound"],
                ("observation_value_or_blocker", "claim_text_or_blocker"),
                r"trans-heterophilic interaction|trans-heterophilic support",
            ),
            (
                "M20B-EVID-001875",
                "ecm_retained",
                ["ecm_retained"],
                ("observation_value_or_blocker",),
                r"Substrate-bound FGF2",
            ),
            (
                "M20B-EVID-001914",
                "membrane_bound",
                ["membrane_bound"],
                ("observation_value_or_blocker", "claim_text_or_blocker"),
                r"trans-synaptic Slitrk1-PTPRD association|not soluble ligand signaling",
            ),
            (
                "M20B-EVID-001915",
                "membrane_bound",
                ["membrane_bound"],
                ("observation_value_or_blocker",),
                r"trans-synaptic binding",
            ),
            (
                "M20B-EVID-001916",
                "membrane_bound",
                ["membrane_bound"],
                ("claim_text_or_blocker",),
                r"trans-synaptic binding",
            ),
            (
                "M20B-EVID-001793",
                "membrane_bound",
                ["membrane_bound"],
                ("observation_value_or_blocker",),
                r"trans-synaptic adhesion",
            ),
            (
                "M20B-EVID-001670",
                "membrane_bound",
                ["membrane_bound"],
                ("observation_value_or_blocker",),
                r"Native PSGL-1/SELPLG glycoforms|initial tethering under flow",
            ),
            (
                "M20B-EVID-002262",
                "ecm_retained",
                ["ecm_retained"],
                ("observation_value_or_blocker",),
                r"matricryptic TNC peptide",
            ),
            (
                "M20B-EVID-002917",
                "membrane_bound",
                ["membrane_bound"],
                ("observation_value_or_blocker", "claim_text_or_blocker"),
                r"heterophilic cadherin adhesion edge|heterophilic interaction through their membrane-distal ectodomains",
            ),
            (
                "M20B-EVID-002921",
                "membrane_bound",
                ["membrane_bound"],
                ("claim_text_or_blocker",),
                r"heterophilic adhesion edge",
            ),
            (
                "M20B-EVID-002930",
                "ecm_retained",
                ["ecm_retained"],
                ("claim_text_or_blocker",),
                r"extracellular tectorial-membrane complex",
            ),
            (
                "M20B-EVID-003254",
                "membrane_bound",
                ["membrane_bound"],
                ("observation_value_or_blocker", "claim_text_or_blocker"),
                r"heterophilic adhesive pair|intercellular receptor-complex output",
            ),
            (
                "M20B-EVID-003255",
                "membrane_bound",
                ["membrane_bound"],
                ("observation_value_or_blocker", "claim_text_or_blocker"),
                r"heterophilic adhesive pair|intercellular adhesion output",
            ),
            (
                "M20B-EVID-003256",
                "membrane_bound",
                ["membrane_bound"],
                ("observation_value_or_blocker", "claim_text_or_blocker"),
                r"heterophilic adhesive pair|intercellular adhesion output",
            ),
            (
                "M20B-EVID-003257",
                "membrane_bound",
                ["membrane_bound"],
                ("observation_value_or_blocker", "claim_text_or_blocker"),
                r"heterophilic adhesive pair|intercellular adhesion output",
            ),
            (
                "M20B-EVID-003259",
                "membrane_bound",
                ["membrane_bound"],
                ("observation_value_or_blocker", "claim_text_or_blocker"),
                r"heterophilic adhesive pair|intercellular adhesion output",
            ),
            (
                "M20B-EVID-003263",
                "membrane_bound",
                ["membrane_bound"],
                ("observation_value_or_blocker", "claim_text_or_blocker"),
                r"heterophilic adhesive pair|intercellular adhesion output",
            ),
            (
                "M20B-EVID-003264",
                "membrane_bound",
                ["membrane_bound"],
                ("observation_value_or_blocker", "claim_text_or_blocker"),
                r"heterophilic adhesive pair|intercellular adhesion output",
            ),
            (
                "M20B-EVID-003396",
                "membrane_bound",
                ["membrane_bound"],
                ("observation_value_or_blocker", "claim_text_or_blocker"),
                r"heterophilic cadherin complex|cell-boundary assays",
            ),
            (
                "M23B-EVID-000673",
                "soluble",
                ["soluble"],
                ("observation_value_or_blocker", "observation_assay"),
                r"soluble extracellular CADM3|soluble CADM3-Fc",
            ),
        )
    }
)

SOURCE_REGISTER_FORM_OVERRIDES.update(
    {
        evidence_id: {
            "candidate": candidate,
            "signals": signals,
            "fields": fields,
            "pattern": re.compile(pattern, re.IGNORECASE),
        }
        for evidence_id, candidate, signals, fields, pattern in (
            (
                "M21B-EVID-002894",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"B7-H6 is a selective cell-surface ligand",
            ),
            (
                "M21B-EVID-006470",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"cell-surface TG2 directly associates",
            ),
            (
                "M21B-EVID-006524",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"recombinant/secreted IL-16 binding inhibition",
            ),
            (
                "M21B-EVID-006660",
                "membrane_bound",
                ["membrane_bound"],
                ("evidence_summary",),
                r"ULBP6/RAET1L.*cell-surface expression",
            ),
            (
                "M21B-EVID-002850",
                "ecm_retained",
                ["ecm_retained"],
                ("evidence_summary",),
                r"laminin.?nidogen extracellular-matrix complex as a ligand",
            ),
            (
                "M21B-EVID-000827",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"human and chlamydial HSP60 activate",
            ),
            (
                "M21B-EVID-000828",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"extracellular HSP60 activates",
            ),
            (
                "M21B-EVID-000840",
                "soluble",
                ["soluble"],
                ("limitations",),
                r"extracellular H4/free-histone preparations",
            ),
            (
                "M21B-EVID-000872",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"extracellular HSP70-induced",
            ),
            (
                "M21B-EVID-002932",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"extracellular HSP70 as a direct ligand",
            ),
            (
                "M21B-EVID-002933",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"extracellular HSP70 as a direct ligand",
            ),
            (
                "M21B-EVID-006678",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"extracellular NAMPT as a DAMP ligand",
            ),
            (
                "M21B-EVID-006679",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"extracellular NAPRT as a DAMP ligand",
            ),
            (
                "M21B-EVID-000877",
                "ecm_retained",
                ["ecm_retained"],
                ("limitations",),
                r"collagen-IV basement-membrane form",
            ),
            (
                "M21B-EVID-006149",
                "ecm_retained",
                ["ecm_retained"],
                ("limitations",),
                r"NID2 as a basement-membrane ligand",
            ),
            (
                "M21B-EVID-006693",
                "ecm_retained",
                ["ecm_retained"],
                ("limitations",),
                r"perlecan-CSPG4/NG2 binding.*basement-membrane context",
            ),
            (
                "M21B-EVID-000732",
                "soluble",
                ["soluble"],
                ("limitations",),
                r"soluble-growth-factor",
            ),
            (
                "M21B-EVID-000844",
                "soluble",
                ["soluble"],
                ("limitations",),
                r"extracellular H4/free-histone preparations",
            ),
            (
                "M21B-EVID-000913",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"Recombinant soluble IL-10",
            ),
            (
                "M21B-EVID-007044",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"extracellular ISG15 receptor",
            ),
            (
                "M21B-EVID-009964",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"direct extracellular NLK-binding receptor candidate",
            ),
            (
                "M21B-EVID-009973",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"direct extracellular vimentin.?.?IGF1R interaction",
            ),
            (
                "M21B-EVID-009974",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"Extracellular vimentin increases",
            ),
            (
                "M21B-EVID-009976",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"Extracellular vimentin treatment",
            ),
            (
                "M21B-EVID-009977",
                "soluble",
                ["soluble"],
                ("evidence_summary",),
                r"Extracellular vimentin treatment",
            ),
            (
                "M21B-EVID-002635",
                "ecm_retained",
                ["ecm_retained"],
                ("limitations",),
                r"laminin-332 isoform-specific basement-membrane context",
            ),
            (
                "M21B-EVID-002636",
                "ecm_retained",
                ["ecm_retained"],
                ("limitations",),
                r"laminin-332 basement-membrane context",
            ),
            (
                "M21B-EVID-002845",
                "ecm_retained",
                ["ecm_retained"],
                ("limitations",),
                r"retinal-basement-membrane context",
            ),
            (
                "M21B-EVID-002846",
                "ecm_retained",
                ["ecm_retained"],
                ("limitations",),
                r"retinal-basement-membrane context",
            ),
            (
                "M20B-EVID-005366",
                "both_or_context_dependent",
                ["soluble", "membrane_bound"],
                ("evidence_summary",),
                r"Soluble and membrane-anchored CXCL16",
            ),
            (
                "M21B-EVID-004630",
                "ecm_retained",
                ["ecm_retained"],
                ("evidence_summary",),
                r"collagen IX NC4 as a direct complement-binding extracellular-matrix domain",
            ),
            (
                "M21B-EVID-004631",
                "ecm_retained",
                ["ecm_retained"],
                ("evidence_summary",),
                r"collagen IX NC4 as a direct complement-binding extracellular-matrix domain",
            ),
            (
                "M21B-EVID-004632",
                "ecm_retained",
                ["ecm_retained"],
                ("evidence_summary",),
                r"collagen IX NC4 as a direct complement-binding extracellular-matrix domain",
            ),
            (
                "M21B-EVID-006402",
                "soluble",
                ["soluble"],
                ("limitations",),
                r"phenol-soluble modulin",
            ),
        )
    }
)

# These records contain availability language for a receptor, assay presentation,
# processed partner, or an explicit negative statement rather than for the exact
# ligand node. Keep them auditable but do not emit a positive ligand-form
# candidate from the generic proximity matcher.
SOURCE_FORM_SUPPRESSIONS = {
    "M20B-EVID-002230": "claim explicitly says NCAM1 is not to be treated as a secreted ligand",
    "M20B-EVID-002242": "cell-surface and immobilized language describes SDC1/thrombospondin presentation, not THBS1 form",
    "M20B-EVID-003425": "membrane-bound and soluble language describes FGFRL1 receptor presentation, not FGF10 form",
    "M20B-EVID-003441": "membrane-bound and soluble language describes FGFRL1 receptor presentation, not FGF2 form",
    "M20B-EVID-003444": "immobilized and soluble language describes NRP1 receptor presentation, not FGF2 form",
    "M20B-EVID-003452": "membrane-bound and soluble language describes FGFRL1 receptor presentation, not FGF22 form",
    "M20B-EVID-003457": "membrane-bound and soluble language describes FGFRL1 receptor presentation, not FGF3 form",
    "M20B-EVID-003458": "membrane-bound and soluble language describes FGFRL1 receptor presentation, not FGF4 form",
    "M20B-EVID-003464": "membrane-bound and soluble language describes FGFRL1 receptor presentation, not FGF8 form",
    "M20B-EVID-003506": "cell-surface language describes DIP2A receptor localization, not FSTL1 form",
    "M20B-EVID-005074": "cell-surface language describes CD63 receptor localization, not TIMP1 form",
    "M21B-EVID-000052": "transmembrane language describes IFNGR2 receptor topology, not IFN-gamma form",
    "M21B-EVID-000053": "membrane and soluble language describes TNF-binding receptor forms, not TNF form",
    "M21B-EVID-000054": "cell-surface aggregation describes the TNF-TNFR2 assay context, not membrane-bound TNF",
    "M23B-EVID-000597": "soluble language describes the alphaIIbbeta3 receptor preparation, not CXCL12 form",
    "M23B-EVID-000738": "cell-surface language describes the alphaVbeta1 receptor record, not FN1 form",
    "M24B-EVID-000171": "cell-surface association describes HMGB1 binding to TLR2/TLR4, not membrane anchoring of HMGB1",
}

FORM_PATTERNS = {
    "soluble": re.compile(
        r"\b(?:soluble|secreted|diffusible|free[- ]form)\b",
        re.IGNORECASE,
    ),
    "membrane_bound": re.compile(
        r"\b(?:membrane[- ]bound|membrane[- ]tethered|cell[- ]surface|surface[- ]bound|"
        r"transmembrane|juxtacrine|cell[- ]associated|GPI[- ]anchored|"
        r"glycosylphosphatidylinositol[- ]anchored)\b",
        re.IGNORECASE,
    ),
    "ecm_retained": re.compile(
        r"\b(?:extracellular matrix|ECM[- ]bound|matrix[- ]bound|matrix[- ]retained|"
        r"proteoglycan[- ]bound|heparan[- ]sulfate[- ]bound|basement membrane)\b",
        re.IGNORECASE,
    ),
}
FORM_EXCLUSION = re.compile(
    r"\b(?:not|rather than|without|does not|did not|no longer)\s+(?:an?\s+)?"
    r"(?:soluble|secreted|membrane[- ]bound|cell[- ]surface|"
    r"transmembrane|ECM[- ]bound|matrix[- ]bound)(?:\s+(?:ligand|protein|receptor|form))?\b",
    re.IGNORECASE,
)

OUTPUT_FIELDS = [
    "assertion_origin",
    "mechanism_node_id",
    "ligand_canonical_name",
    "ligand_source_label",
    "mechanism_edge_id",
    "target_node_id",
    "target_label",
    "relation_type",
    "pathway_name",
    "module",
    "b_evidence_id",
    "extraction_id",
    "dependency_group",
    "context_observation_id",
    "context_evidence_role",
    "context_study_id",
    "context_timepoint_id",
    "context_species",
    "context_injury_model",
    "context_injury_level",
    "context_injury_severity",
    "context_tissue",
    "context_cell_type",
    "context_sample_id",
    "context_timepoint_value",
    "context_timepoint_unit",
    "context_perturbation",
    "context_treatment",
    "context_sample_scope",
    "context_protein_form",
    "context_protein_resolution",
    "context_source_locator",
    "context_source_record_key",
    "canonical_paper_key",
    "module_source_locator",
    "observation_status",
    "evidence_layer",
    "confidence",
    "observation_value_or_blocker",
    "observation_cell_or_model",
    "observation_assay",
    "observation_perturbation",
    "claim_text_or_blocker",
    "availability_class_candidate",
    "availability_evidence_state",
    "availability_signal_terms",
    "availability_evidence_snippet",
    "availability_basis_fields",
    "sci_context_match_status",
    "sci_context_observation_ids",
    "sci_context_ids",
    "sci_context_source_artifact_paths",
    "sci_context_source_artifact_sha256",
    "promotion_state",
    "audit_note",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_tsv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def label_tokens(*labels: str) -> list[str]:
    tokens: set[str] = set()
    for label in labels:
        if not label:
            continue
        tokens.add(label.strip())
        tokens.update(token for token in re.split(r"[^A-Za-z0-9]+", label) if len(token) >= 4)
    return sorted(tokens, key=len, reverse=True)


def exact_label_positions(text: str, labels: list[str]) -> list[tuple[int, int, str]]:
    positions: list[tuple[int, int, str]] = []
    for label in labels:
        pattern = re.compile(rf"(?<![A-Za-z0-9]){re.escape(label)}(?![A-Za-z0-9])", re.IGNORECASE)
        positions.extend((match.start(), match.end(), label) for match in pattern.finditer(text))
    return positions


def compact_snippet(text: str, start: int, end: int) -> str:
    left = max(0, start - 100)
    right = min(len(text), end + 100)
    return " ".join(text[left:right].split())


def directly_attached(text: str, match: re.Match[str], positions: list[tuple[int, int, str]]) -> bool:
    """Require a short form-to-ligand phrase, not merely same-sentence proximity."""

    assay_words = re.compile(r"\b(?:assay|assays|binding|screen|screening|expression|cells?)\b", re.IGNORECASE)
    for start, end, _label in positions:
        if start >= match.end():
            between = text[match.end():start]
        elif end <= match.start():
            between = text[end:match.start()]
        else:
            return True
        words = re.findall(r"[A-Za-z0-9-]+", between)
        if (
            (len(words) <= 4 or (len(words) <= 8 and re.search(r"\bforms?\b", between, re.IGNORECASE)))
            and not assay_words.search(between)
        ):
            return True
    return False


def classify_availability(text: str, labels: list[str]) -> tuple[str, str, list[str], str, list[str]]:
    positions = exact_label_positions(text, labels)
    attached: dict[str, list[str]] = defaultdict(list)
    unattached: dict[str, list[str]] = defaultdict(list)
    basis: dict[str, list[str]] = defaultdict(list)
    snippets: list[str] = []
    for kind, pattern in FORM_PATTERNS.items():
        for match in pattern.finditer(text):
            exclusion_window = text[max(0, match.start() - 80):min(len(text), match.end() + 80)]
            if FORM_EXCLUSION.search(exclusion_window):
                continue
            nearby = [item for item in positions if abs(item[0] - match.end()) <= 48 or abs(item[1] - match.start()) <= 48]
            snippet = compact_snippet(text, match.start(), match.end())
            if nearby and directly_attached(text, match, nearby):
                attached[kind].append(match.group(0))
                snippets.append(snippet)
            else:
                unattached[kind].append(match.group(0))
    for kind in attached:
        basis[kind].append(kind)
    attached_kinds = set(attached)
    if attached_kinds:
        if "ecm_retained" in attached_kinds and attached_kinds == {"ecm_retained"}:
            candidate = "ecm_retained"
        elif attached_kinds == {"soluble"}:
            candidate = "soluble"
        elif attached_kinds == {"membrane_bound"}:
            candidate = "membrane_bound"
        else:
            candidate = "both_or_context_dependent"
        return candidate, "source_reported_candidate", sorted(attached_kinds), "; ".join(sorted(set(snippets))), sorted(basis)
    if unattached:
        return "unknown", "assay_or_form_language_not_attached_to_exact_ligand", sorted(unattached), "", sorted(unattached)
    return "unknown", "not_reported_in_source_record", [], "", []


def normalized_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def context_form_class(protein_form: str) -> str:
    normalized_form = protein_form.lower()
    if (
        "exact molecular form not further specified" in normalized_form
        or "exact processing state not resolved" in normalized_form
    ):
        return ""
    if "secreted" in normalized_form and "total" in normalized_form:
        return ""
    if protein_form in CONTEXT_FORM_CLASSES:
        return CONTEXT_FORM_CLASSES[protein_form]
    for pattern, candidate in CONTEXT_FORM_PATTERNS:
        if pattern.search(protein_form):
            return candidate
    return ""


def context_form_matches(
    observations: list[dict[str, str]],
    ligand_nodes: dict[str, dict[str, str]],
) -> list[tuple[dict[str, str], dict[str, str], dict[str, Any], str, str, list[str], str]]:
    """Return exact node/observation matches with an explicit SCI protein form.

    The match is deliberately limited to exact normalized mechanism labels or
    label variants. It does not infer gene-to-protein aliases, receptor
    families, or form from assay type alone.
    """

    label_index: dict[str, list[dict[str, str]]] = defaultdict(list)
    for node in ligand_nodes.values():
        for field in ("canonical_name", "canonical_label"):
            label = node.get(field, "")
            if label:
                label_index[normalized_key(label)].append(node)
        for label in filter(None, node.get("label_variants", "").split(";")):
            label_index[normalized_key(label)].append(node)

    matches: dict[tuple[str, str], tuple[dict[str, str], dict[str, str], dict[str, Any], str, str, list[str], str]] = {}
    for observation in observations:
        if observation.get("modality") != "protein":
            continue
        try:
            provenance = json.loads(observation.get("provenance_note", "{}"))
        except json.JSONDecodeError:
            continue
        protein_form = str(provenance.get("protein_form", "")).strip()
        form_evidence: tuple[str, list[str], str] | None = None
        direct_class = context_form_class(protein_form)
        if direct_class:
            form_evidence = (direct_class, ["observations.tsv:provenance_note.protein_form"], protein_form)
        else:
            observed_labels = [observation.get("measured_entity_name", ""), observation.get("feature_id", "")]
            label_patterns = [
                re.compile(rf"(?<![A-Za-z0-9]){re.escape(label)}(?![A-Za-z0-9])", re.IGNORECASE)
                for label in observed_labels
                if label
            ]
            for field in ("value_text", "direction_vs_control"):
                text = observation.get(field, "")
                if not text or not any(pattern.search(text) for pattern in label_patterns):
                    continue
                candidate = context_form_class(text)
                if candidate:
                    signal_match = next(
                        match for pattern, _candidate in CONTEXT_FORM_PATTERNS for match in pattern.finditer(text)
                        if _candidate == candidate
                    )
                    form_evidence = (
                        candidate,
                        [f"observations.tsv:{field}"],
                        compact_snippet(text, signal_match.start(), signal_match.end()),
                    )
                    break
        if not form_evidence:
            continue
        candidate_nodes: dict[str, dict[str, str]] = {}
        for field in ("measured_entity_name", "feature_id"):
            key = normalized_key(observation.get(field, ""))
            for node in label_index.get(key, []):
                candidate_nodes[node["node_id"]] = node
        for node in candidate_nodes.values():
            matches[(node["node_id"], observation["observation_id"])] = (
                node,
                observation,
                provenance,
                protein_form,
                form_evidence[0],
                form_evidence[1],
                form_evidence[2],
            )
    return list(matches.values())


def source_form_override(module_row: dict[str, str]) -> tuple[str, str, list[str], str, list[str]] | None:
    """Apply only explicitly keyed, source-text-backed form curation rules."""

    rule = SOURCE_FORM_OVERRIDES.get(module_row.get("b_evidence_id", ""))
    if not rule:
        return None
    for field in rule["fields"]:
        text = module_row.get(field, "")
        match = rule["pattern"].search(text)
        if match:
            return (
                rule["candidate"],
                "source_reported_candidate",
                rule["signals"],
                compact_snippet(text, match.start(), match.end()),
                [field],
            )
    return None


def source_form_suppression(module_row: dict[str, str]) -> str:
    """Return the curation reason for a known non-ligand form phrase."""

    return SOURCE_FORM_SUPPRESSIONS.get(module_row.get("b_evidence_id", ""), "")


def source_register_form_override(register_row: dict[str, str]) -> tuple[str, str, list[str], str, list[str]] | None:
    """Apply an exact, manually reviewed form rule to a module-B register row."""

    rule = SOURCE_REGISTER_FORM_OVERRIDES.get(register_row.get("b_evidence_id", ""))
    if not rule:
        return None
    for field in rule["fields"]:
        text = register_row.get(field, "")
        match = rule["pattern"].search(text)
        if match:
            return (
                rule["candidate"],
                "source_register_explicit_form",
                rule["signals"],
                compact_snippet(text, match.start(), match.end()),
                [field],
            )
    return None


def build(
    release_dir: Path = DEFAULT_RELEASE,
    ledger_path: Path = DEFAULT_LEDGER,
    pack: Path = DEFAULT_PACK,
    output_dir: Path = DEFAULT_OUTPUT,
) -> dict[str, Any]:
    release_dir = release_dir.resolve()
    ledger_path = ledger_path.resolve()
    pack = pack.resolve()
    output_dir = output_dir.resolve()
    nodes = {row["node_id"]: row for row in read_tsv(release_dir / "mechanism_nodes.tsv")}
    ligand_nodes = {node_id: row for node_id, row in nodes.items() if row.get("node_type") == "ligand"}
    edges = read_tsv(release_dir / "mechanism_edges.tsv")
    evidence_to_edges: dict[str, list[dict[str, str]]] = defaultdict(list)
    for edge in edges:
        if edge.get("source_node_id") not in ligand_nodes:
            continue
        for evidence_id in filter(None, edge.get("evidence_ids", "").split(";")):
            evidence_to_edges[evidence_id].append(edge)

    ledger_rows = read_tsv(ledger_path)
    observations = read_tsv(pack / "observations.tsv")
    contexts = {row["context_id"]: row for row in read_tsv(pack / "contexts.tsv")}
    context_index = index_pack_rows(observations, ("source_locator", "source_record_key"))
    output_rows: list[dict[str, Any]] = []
    counts_by: dict[str, Counter[str]] = {
        "module": Counter(),
        "availability_class_candidate": Counter(),
        "availability_evidence_state": Counter(),
        "observation_status": Counter(),
        "evidence_layer": Counter(),
        "sci_context_match_status": Counter(),
        "assertion_origin": Counter(),
        "context_form_class": Counter(),
    }
    matched_ledger_rows = 0
    ligand_associations = 0
    source_register_rows_scanned = 0
    source_register_form_assertions = 0
    source_register_skipped_existing_ledger = 0
    source_register_form_applied_to_ledger_ids: set[str] = set()
    source_register_unresolved_mappings: list[dict[str, str]] = []
    ledger_evidence_ids = {row.get("b_evidence_id", "") for row in ledger_rows}

    source_register_rows: list[tuple[Path, dict[str, str]]] = []
    source_register_rows_by_id: dict[str, list[tuple[Path, dict[str, str]]]] = defaultdict(list)
    for register_path in DEFAULT_SOURCE_REGISTERS:
        for register_row in read_tsv(register_path):
            source_register_rows_scanned += 1
            source_register_rows.append((register_path, register_row))
            source_register_rows_by_id[register_row.get("b_evidence_id", "")].append((register_path, register_row))
    source_register_form_by_id: dict[str, tuple[str, str, list[str], str, list[str]]] = {}
    for evidence_id, register_items in source_register_rows_by_id.items():
        if evidence_id not in SOURCE_REGISTER_FORM_OVERRIDES:
            continue
        for _register_path, register_row in register_items:
            register_override = source_register_form_override(register_row)
            if register_override:
                source_register_form_by_id[evidence_id] = register_override
                break

    for module_row in ledger_rows:
        evidence_id = module_row.get("b_evidence_id", "")
        associated_edges = evidence_to_edges.get(evidence_id, [])
        if not associated_edges:
            continue
        matched_ledger_rows += 1
        source_ids = source_identifiers(module_row.get("canonical_paper_key", ""), module_row.get("source_locator", ""))
        matched_context = [row for source_id in source_ids for row in context_index.get(source_id, [])]
        matched_context = list({row["observation_id"]: row for row in matched_context}.values())
        context_status = "matched_exact_source_identifier" if matched_context else "no_exact_source_identifier_match"
        unique_edges = {edge["edge_id"]: edge for edge in associated_edges}
        for edge in unique_edges.values():
            ligand = ligand_nodes[edge["source_node_id"]]
            labels = label_tokens(ligand.get("canonical_name", ""), ligand.get("canonical_label", ""), edge.get("source_label", ""), ligand.get("label_variants", ""))
            field_results = [
                (field, classify_availability(module_row.get(field, ""), labels))
                for field in SOURCE_FIELDS
                if module_row.get(field, "")
            ]
            attached_results = [result for _field, result in field_results if result[1] == "source_reported_candidate"]
            unattached_results = [result for _field, result in field_results if result[1] == "assay_or_form_language_not_attached_to_exact_ligand"]
            attached_signals = {signal for _candidate, _state, signals, _snippet, _basis in attached_results for signal in signals}
            suppression_reason = source_form_suppression(module_row)
            override = source_form_override(module_row)
            source_register_override = source_register_form_by_id.get(evidence_id)
            if suppression_reason:
                candidate = "unknown"
                state = "assay_or_form_language_not_attached_to_exact_ligand"
                signals = []
                snippet = ""
                basis = []
            elif override:
                candidate, state, signals, snippet, basis = override
            elif source_register_override:
                candidate, state, signals, snippet, basis = source_register_override
                state = "source_register_explicit_form"
                basis = [f"source_register:{field}" for field in basis]
                source_register_form_applied_to_ledger_ids.add(evidence_id)
            elif attached_signals:
                if attached_signals == {"ecm_retained"}:
                    candidate = "ecm_retained"
                elif attached_signals == {"soluble"}:
                    candidate = "soluble"
                elif attached_signals == {"membrane_bound"}:
                    candidate = "membrane_bound"
                else:
                    candidate = "both_or_context_dependent"
                state = "source_reported_candidate"
                signals = sorted(attached_signals)
                snippet = "; ".join(sorted({snippet for _candidate, _state, _signals, snippet, _basis in attached_results if snippet}))
                basis = [field for field, result in field_results if result[1] == "source_reported_candidate"]
            elif unattached_results:
                candidate = "unknown"
                state = "assay_or_form_language_not_attached_to_exact_ligand"
                signals = sorted({signal for _candidate, _state, signals, _snippet, _basis in unattached_results for signal in signals})
                snippet = ""
                basis = [field for field, result in field_results if result[1] == "assay_or_form_language_not_attached_to_exact_ligand"]
            else:
                candidate = "unknown"
                state = "not_reported_in_source_record"
                signals = []
                snippet = ""
                basis = []
            ligand_associations += 1
            row = {
                "assertion_origin": "source_linked_mechanism_evidence",
                "mechanism_node_id": ligand["node_id"],
                "ligand_canonical_name": ligand.get("canonical_name", ""),
                "ligand_source_label": edge.get("source_label", ""),
                "mechanism_edge_id": edge.get("edge_id", ""),
                "target_node_id": edge.get("target_node_id", ""),
                "target_label": edge.get("target_label", ""),
                "relation_type": edge.get("relation_type", ""),
                "pathway_name": edge.get("pathway_name", ""),
                "module": module_row.get("module", ""),
                "b_evidence_id": evidence_id,
                "extraction_id": module_row.get("extraction_id", ""),
                "dependency_group": f"{evidence_id}|{ligand['node_id']}",
                "context_observation_id": "",
                "context_evidence_role": "",
                "context_study_id": "",
                "context_timepoint_id": "",
                "context_species": "",
                "context_injury_model": "",
                "context_injury_level": "",
                "context_injury_severity": "",
                "context_tissue": "",
                "context_cell_type": "",
                "context_sample_id": "",
                "context_timepoint_value": "",
                "context_timepoint_unit": "",
                "context_perturbation": "",
                "context_treatment": "",
                "context_sample_scope": "",
                "context_protein_form": "",
                "context_protein_resolution": "",
                "context_source_locator": "",
                "context_source_record_key": "",
                "canonical_paper_key": module_row.get("canonical_paper_key", ""),
                "module_source_locator": module_row.get("source_locator", ""),
                "observation_status": module_row.get("observation_status", ""),
                "evidence_layer": module_row.get("evidence_layer", ""),
                "confidence": module_row.get("confidence", ""),
                "observation_value_or_blocker": module_row.get("observation_value_or_blocker", ""),
                "observation_cell_or_model": module_row.get("observation_cell_or_model", ""),
                "observation_assay": module_row.get("observation_assay", ""),
                "observation_perturbation": module_row.get("observation_perturbation", ""),
                "claim_text_or_blocker": module_row.get("claim_text_or_blocker", ""),
                "availability_class_candidate": candidate,
                "availability_evidence_state": state,
                "availability_signal_terms": ";".join(signals),
                "availability_evidence_snippet": snippet,
                "availability_basis_fields": ";".join(basis),
                "sci_context_match_status": context_status,
                "sci_context_observation_ids": ";".join(unique_values(matched_context, "observation_id")),
                "sci_context_ids": ";".join(unique_values(matched_context, "context_id")),
                "sci_context_source_artifact_paths": ";".join(unique_values(matched_context, "source_artifact_path")),
                "sci_context_source_artifact_sha256": ";".join(unique_values(matched_context, "source_artifact_sha256")),
                "promotion_state": "audit_only_not_promoted",
                "audit_note": (
                    "Availability class is a staged source-text candidate, not a finalized protein property. "
                    "Assay format is not treated as physical localization; no graph edge, route confidence, or numeric weight was created."
                    + (
                        " Source-register form curation was applied to this existing ledger row; the original dependency group was retained."
                        if state == "source_register_explicit_form"
                        else ""
                    )
                    + (f" Manual adjudication: {suppression_reason}." if suppression_reason else "")
                ),
            }
            output_rows.append(row)
            counts_by["module"][row["module"] or "unknown"] += 1
            counts_by["availability_class_candidate"][candidate] += 1
            counts_by["availability_evidence_state"][state] += 1
            counts_by["observation_status"][row["observation_status"] or "unknown"] += 1
            counts_by["evidence_layer"][row["evidence_layer"] or "unknown"] += 1
            counts_by["sci_context_match_status"][context_status] += 1
            counts_by["assertion_origin"][row["assertion_origin"]] += 1

    # Module-B registers contain curated summaries and limitations that are not
    # all repeated in the integrated phase-2 ledger.  Only explicitly keyed
    # form assertions are emitted, and IDs already represented in the ledger
    # are skipped to preserve one dependency group per source record.
    for register_path, register_row in source_register_rows:
            evidence_id = register_row.get("b_evidence_id", "")
            if evidence_id not in SOURCE_REGISTER_FORM_OVERRIDES:
                continue
            if evidence_id in ledger_evidence_ids:
                source_register_skipped_existing_ledger += 1
                continue
            associated_edges = evidence_to_edges.get(evidence_id, [])
            if not associated_edges:
                source_register_unresolved_mappings.append(
                    {
                        "b_evidence_id": evidence_id,
                        "reason": "curated source-register form rule has no exact ligand-source edge in the pinned release",
                    }
                )
                continue
            override = source_register_form_override(register_row)
            if not override:
                source_register_unresolved_mappings.append(
                    {
                        "b_evidence_id": evidence_id,
                        "reason": "curated source-register rule did not match its declared source field",
                    }
                )
                continue
            candidate, state, signals, snippet, basis = override
            source_ids = source_identifiers("", register_row.get("source_locator", ""))
            matched_context = [row for source_id in source_ids for row in context_index.get(source_id, [])]
            matched_context = list({row["observation_id"]: row for row in matched_context}.values())
            context_status = "matched_exact_source_identifier" if matched_context else "no_exact_source_identifier_match"
            unique_edges = {edge["edge_id"]: edge for edge in associated_edges}
            for edge in unique_edges.values():
                ligand = ligand_nodes[edge["source_node_id"]]
                row = {
                    "assertion_origin": "source_register_form_observation",
                    "mechanism_node_id": ligand["node_id"],
                    "ligand_canonical_name": ligand.get("canonical_name", ""),
                    "ligand_source_label": edge.get("source_label", ""),
                    "mechanism_edge_id": edge.get("edge_id", ""),
                    "target_node_id": edge.get("target_node_id", ""),
                    "target_label": edge.get("target_label", ""),
                    "relation_type": edge.get("relation_type", ""),
                    "pathway_name": edge.get("pathway_name", ""),
                    "module": edge.get("module", "") or ligand.get("modules", ""),
                    "b_evidence_id": evidence_id,
                    "extraction_id": "",
                    "dependency_group": f"{evidence_id}|{ligand['node_id']}",
                    "context_observation_id": "",
                    "context_evidence_role": "",
                    "context_study_id": "",
                    "context_timepoint_id": "",
                    "context_species": "",
                    "context_injury_model": "",
                    "context_injury_level": "",
                    "context_injury_severity": "",
                    "context_tissue": "",
                    "context_cell_type": "",
                    "context_sample_id": "",
                    "context_timepoint_value": "",
                    "context_timepoint_unit": "",
                    "context_perturbation": "",
                    "context_treatment": "",
                    "context_sample_scope": "",
                    "context_protein_form": "",
                    "context_protein_resolution": "",
                    "context_source_locator": "",
                    "context_source_record_key": "",
                    "canonical_paper_key": "",
                    "module_source_locator": register_row.get("source_locator", ""),
                    "observation_status": "source_register_curated",
                    "evidence_layer": register_row.get("evidence_layer", ""),
                    "confidence": register_row.get("confidence_tier", ""),
                    "observation_value_or_blocker": register_row.get("evidence_summary", ""),
                    "observation_cell_or_model": register_row.get("species_support", ""),
                    "observation_assay": register_row.get("support_kind", ""),
                    "observation_perturbation": register_row.get("consolidation_note", ""),
                    "claim_text_or_blocker": register_row.get("limitations", ""),
                    "availability_class_candidate": candidate,
                    "availability_evidence_state": state,
                    "availability_signal_terms": ";".join(signals),
                    "availability_evidence_snippet": snippet,
                    "availability_basis_fields": ";".join(basis),
                    "sci_context_match_status": context_status,
                    "sci_context_observation_ids": ";".join(unique_values(matched_context, "observation_id")),
                    "sci_context_ids": ";".join(unique_values(matched_context, "context_id")),
                    "sci_context_source_artifact_paths": ";".join(unique_values(matched_context, "source_artifact_path")),
                    "sci_context_source_artifact_sha256": ";".join(unique_values(matched_context, "source_artifact_sha256")),
                    "promotion_state": "audit_only_not_promoted",
                    "audit_note": (
                        "Exact form assertion curated from a module-B evidence register. This is source-register "
                        "evidence for the cited form/context, not a universal protein property; no graph edge, "
                        "route confidence, or numeric weight was created. Existing phase-2 ledger IDs were excluded "
                        "to avoid duplicate source/dependency counting."
                    ),
                }
                output_rows.append(row)
                source_register_form_assertions += 1
                counts_by["module"][row["module"] or "unknown"] += 1
                counts_by["availability_class_candidate"][candidate] += 1
                counts_by["availability_evidence_state"][state] += 1
                counts_by["observation_status"][row["observation_status"]] += 1
                counts_by["evidence_layer"][row["evidence_layer"] or "unknown"] += 1
                counts_by["sci_context_match_status"][context_status] += 1
                counts_by["assertion_origin"][row["assertion_origin"]] += 1

    context_matches = context_form_matches(observations, ligand_nodes)
    for ligand, observation, provenance, protein_form, context_class, form_basis, form_snippet in context_matches:
        context_curation = provenance.get("context_curation", {})
        context = contexts.get(observation.get("context_id", ""), {})
        context_source_locator = provenance.get("source_location", "") or observation.get("source_locator", "")
        row = {
            "assertion_origin": "sci_context_observation",
            "mechanism_node_id": ligand["node_id"],
            "ligand_canonical_name": ligand.get("canonical_name", ""),
            "ligand_source_label": "",
            "mechanism_edge_id": "",
            "target_node_id": "",
            "target_label": "",
            "relation_type": "",
            "pathway_name": "",
            "module": ligand.get("modules", ""),
            "b_evidence_id": "",
            "extraction_id": "",
            "dependency_group": f"{observation['dependency_group']}|{ligand['node_id']}",
            "context_observation_id": observation.get("observation_id", ""),
            "context_evidence_role": observation.get("evidence_role", ""),
            "context_study_id": context.get("study_id", "") or provenance.get("study_id", ""),
            "context_timepoint_id": provenance.get("timepoint_id", ""),
            "context_species": context.get("species", ""),
            "context_injury_model": context.get("injury_model", ""),
            "context_injury_level": context.get("injury_level", ""),
            "context_injury_severity": context.get("injury_severity", ""),
            "context_tissue": context.get("tissue", ""),
            "context_cell_type": context.get("cell_type", "") or observation.get("cell_type", ""),
            "context_sample_id": context.get("sample_id", "") or observation.get("sample_id", ""),
            "context_timepoint_value": context.get("timepoint_value", "") or observation.get("timepoint_value", ""),
            "context_timepoint_unit": context.get("timepoint_unit", "") or observation.get("timepoint_unit", ""),
            "context_perturbation": context.get("perturbation", "") or provenance.get("study_perturbation_status", "") or observation.get("perturbation", ""),
            "context_treatment": context.get("treatment", ""),
            "context_sample_scope": context.get("sample_scope", "") or provenance.get("sample_scope", ""),
            "context_protein_form": protein_form,
            "context_protein_resolution": provenance.get("protein_resolution", ""),
            "context_source_locator": context_source_locator,
            "context_source_record_key": observation.get("source_record_key", ""),
            "canonical_paper_key": "",
            "module_source_locator": "",
            "observation_status": observation.get("observation_status", ""),
            "evidence_layer": "context_matched_external_observation",
            "confidence": provenance.get("evidence_grade", ""),
            "observation_value_or_blocker": observation.get("value_text", ""),
            "observation_cell_or_model": observation.get("cell_type", ""),
            "observation_assay": observation.get("assay", ""),
            "observation_perturbation": observation.get("perturbation", ""),
            "claim_text_or_blocker": (
                f"Explicit SCI protein-form annotation: protein_form={protein_form}; "
                f"protein_resolution={provenance.get('protein_resolution', '')}"
            ),
            "availability_class_candidate": context_class,
            "availability_evidence_state": "context_observation_explicit_protein_form",
            "availability_signal_terms": context_class,
            "availability_evidence_snippet": form_snippet,
            "availability_basis_fields": ";".join(form_basis),
            "sci_context_match_status": "matched_exact_ligand_observation",
            "sci_context_observation_ids": observation.get("observation_id", ""),
            "sci_context_ids": observation.get("context_id", ""),
            "sci_context_source_artifact_paths": observation.get("source_artifact_path", ""),
            "sci_context_source_artifact_sha256": observation.get("source_artifact_sha256", ""),
            "promotion_state": "audit_only_not_promoted",
            "audit_note": (
                "SCI observation explicitly annotates the measured protein form. This is context-matched "
                "evidence for the observed SCI sample, not a universal protein property and not causal "
                "evidence for a mechanism edge."
            ),
        }
        output_rows.append(row)
        counts_by["module"][row["module"] or "unknown"] += 1
        counts_by["availability_class_candidate"][context_class] += 1
        counts_by["availability_evidence_state"][row["availability_evidence_state"]] += 1
        counts_by["observation_status"][row["observation_status"] or "unknown"] += 1
        counts_by["evidence_layer"][row["evidence_layer"]] += 1
        counts_by["sci_context_match_status"][row["sci_context_match_status"]] += 1
        counts_by["assertion_origin"][row["assertion_origin"]] += 1
        counts_by["context_form_class"][context_class] += 1

    output_rows.sort(key=lambda row: (row["mechanism_node_id"], row["mechanism_edge_id"], row["b_evidence_id"], row["extraction_id"]))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_tsv = output_dir / "ligand_availability_audit.tsv"
    output_json = output_dir / "ligand_availability_audit.json"
    write_tsv(output_tsv, output_rows)

    metadata = json.loads((release_dir / "bundle_metadata.json").read_text(encoding="utf-8"))
    input_paths = [
        release_dir / "bundle_metadata.json",
        release_dir / "mechanism_nodes.tsv",
        release_dir / "mechanism_edges.tsv",
        ledger_path,
        *DEFAULT_SOURCE_REGISTERS,
        pack / "observations.tsv",
        pack / "contexts.tsv",
    ]
    input_artifacts = [
        {"path": str(path.relative_to(ROOT)), "sha256": sha256(path), "size_bytes": path.stat().st_size, "rows": len(read_tsv(path)) if path.suffix == ".tsv" else None}
        for path in input_paths
    ]
    summary = {
        "audit_version": "ligand_availability_audit_v1",
        "scope": "Source-linked ligand evidence in the pinned Module 20B-24B mechanism release; SCI context is linked by exact source identifiers when present.",
        "mechanism_release_id": metadata.get("release_id", ""),
        "mechanism_release_path": str(release_dir.relative_to(ROOT)),
        "input_artifacts": input_artifacts,
        "release_ligand_node_count": len(ligand_nodes),
        "phase2_ledger_rows_scanned": len(ledger_rows),
        "phase2_rows_with_pinned_ligand_edge": matched_ledger_rows,
        "ligand_evidence_associations": ligand_associations,
        "source_register_rows_scanned": source_register_rows_scanned,
        "source_register_form_assertions": source_register_form_assertions,
        "source_register_form_assertion_ids": len(
            {
                row["b_evidence_id"]
                for row in output_rows
                if row["assertion_origin"] == "source_register_form_observation"
            }
        ),
        "source_register_skipped_existing_ledger": source_register_skipped_existing_ledger,
        "source_register_form_applied_to_ledger": len(source_register_form_applied_to_ledger_ids),
        "source_register_form_applied_to_ledger_ids": sorted(source_register_form_applied_to_ledger_ids),
        "source_register_unresolved_mappings": source_register_unresolved_mappings,
        "ligand_context_form_assertions": len(context_matches),
        "ligand_context_form_assertion_nodes": len({ligand["node_id"] for ligand, _observation, _provenance, _form, _class, _basis, _snippet in context_matches}),
        "unique_dependency_groups": len({row["dependency_group"] for row in output_rows}),
        "counts_by": {key: dict(sorted(counter.items())) for key, counter in sorted(counts_by.items())},
        "interpretation": {
            "availability_classes": "soluble, membrane_bound, both_or_context_dependent, and ecm_retained are staged candidates; unknown is retained when the source does not resolve physical availability.",
            "assay_format_gate": "Soluble ectodomain, recombinant-receptor, cell-surface-binding, SPR, or immobilized-assay language is not sufficient by itself to classify the ligand form.",
            "sci_context_linking": "SCI context is linked only through exact PMID, PMCID, or DOI intersections with observations.tsv; absence of a match is not negative protein evidence.",
            "context_form_assertions": "Exact ligand-label matches to observations.tsv provenance_note protein_form values are emitted as context_matched_external_observation rows; they describe the observed SCI sample and do not establish a universal protein property.",
            "source_register_form_assertions": "Only explicitly keyed source-register summaries or limitations are emitted; generic register language is ignored. When an exact source-register form rule targets an existing phase-2 ledger ID, the form assertion is applied to that existing ledger row so its dependency group is retained without adding a duplicate row.",
            "dependency_policy": "Rows sharing b_evidence_id and ligand node_id share a dependency group and must not be counted as independent experiments.",
            "promotion_policy": "This audit does not modify mechanism_nodes.tsv, mechanism_edges.tsv, observations.tsv, mechanism_links.tsv, or the pinned graph release.",
            "next_step": "Manually review source-reported candidates before exposing them as soft spatial filters; preserve unknown and assay-only states separately.",
        },
        "artifacts": {"tsv": output_tsv.name, "json": output_json.name},
    }
    output_json.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-dir", type=Path, default=DEFAULT_RELEASE)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--pack", type=Path, default=DEFAULT_PACK)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    summary = build(args.release_dir, args.ledger, args.pack, args.output_dir)
    print(json.dumps({"release_id": summary["mechanism_release_id"], "ligand_evidence_associations": summary["ligand_evidence_associations"], "counts_by": summary["counts_by"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
