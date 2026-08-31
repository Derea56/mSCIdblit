#!/usr/bin/env python3
"""Build reusable Module 20A family evidence packet registries."""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


FAMILY_PACKET_HEADERS = [
    "family_packet_id",
    "packet_label",
    "packet_kind",
    "pair_match_rule",
    "reusable_orientation_locators",
    "reusable_primary_locators",
    "reuse_constraints",
    "supporting_pair_count",
    "supporting_pairs",
    "supporting_evidence_item_ids",
    "evidence_origin_files",
    "notes",
]

REUSE_REGISTRY_HEADERS = [
    "pair_label",
    "family_packet_id",
    "reuse_status",
    "reuse_priority",
    "reusable_orientation_locators",
    "reusable_primary_locators",
    "supporting_evidence_item_ids",
    "evidence_origin_files",
    "reuse_constraints",
    "notes",
]


@dataclass(frozen=True)
class FamilyPacketRule:
    family_packet_id: str
    packet_label: str
    packet_kind: str
    pair_regex: str
    orientation_locators: tuple[str, ...]
    primary_locators: tuple[str, ...]
    reuse_constraints: str
    notes: str

    def matches_pair(self, pair_label: str) -> bool:
        return re.search(self.pair_regex, pair_label, flags=re.IGNORECASE) is not None


FAMILY_PACKET_RULES = [
    FamilyPacketRule(
        family_packet_id="M20A-REUSE-001",
        packet_label="VEGF-family canonical FLT packet",
        packet_kind="family_orientation_plus_primary_reuse",
        pair_regex=r"^(Vegfa|Vegfb|Vegfc|Vegfd|Pgf) (Flt1|Flt4)$",
        orientation_locators=("PMID:16633338",),
        primary_locators=(),
        reuse_constraints=(
            "Reusable for VEGF/PlGF to FLT1/FLT4 orientation only; keep species "
            "confidence pair-specific and do not infer KDR/VEGFR2 support."
        ),
        notes=(
            "This packet captures the repeated VEGFR-family orientation review "
            "used across the fast-path batches."
        ),
    ),
    FamilyPacketRule(
        family_packet_id="M20A-REUSE-002",
        packet_label="EGFR and ERBB-family ligand packet",
        packet_kind="family_orientation_plus_primary_reuse",
        pair_regex=r"^(Areg|Btc|Egf) (Egfr|Erbb4)$",
        orientation_locators=("PMID:24691965",),
        primary_locators=("PMID:8570211",),
        reuse_constraints=(
            "Reuse for EGFR/ERBB ligand-family orientation and BTC-directed "
            "ERBB4 support only; AREG and EGF still require their own pair-level "
            "primary anchors."
        ),
        notes=(
            "This packet surfaces the repeated ERBB-family orientation review and "
            "the shared BTC activation paper already used in multiple audits."
        ),
    ),
    FamilyPacketRule(
        family_packet_id="M20A-REUSE-003",
        packet_label="Slit-Robo canonical packet",
        packet_kind="family_orientation_plus_primary_reuse",
        pair_regex=r"^Slit2 Robo[12]$",
        orientation_locators=("https://pmc.ncbi.nlm.nih.gov/articles/PMC5501134/",),
        primary_locators=("PMID:10102268",),
        reuse_constraints=(
            "Reusable for canonical Slit2-Robo orientation; confidence still "
            "depends on whether the retained pair is isolated cleanly in the "
            "primary packet."
        ),
        notes=(
            "This packet captures the shared Slit-Robo primary and review pair "
            "used for both audited Slit2 rows."
        ),
    ),
    FamilyPacketRule(
        family_packet_id="M20A-REUSE-004",
        packet_label="Slitrk and type-IIa RPTP packet",
        packet_kind="family_orientation_plus_primary_reuse",
        pair_regex=r"^Slitrk[12] Ptpr[ds]$",
        orientation_locators=("PMID:30648269", "PMID:30822649"),
        primary_locators=("PMID:23345436",),
        reuse_constraints=(
            "Reusable for family-level Slitrk to type-IIa receptor protein "
            "tyrosine phosphatase support only; do not overpromote to pair-isolated "
            "mouse confidence without stronger pair-specific evidence."
        ),
        notes=(
            "This packet captures the repeated synaptic-adhesion family packet "
            "already reused across four audited rows."
        ),
    ),
    FamilyPacketRule(
        family_packet_id="M20A-REUSE-005",
        packet_label="Complement anaphylatoxin fragment receptor packet",
        packet_kind="family_orientation_plus_primary_reuse",
        pair_regex=r"^(C3a C3ar1|C3 C3ar1|C5a C5ar1|C3 Cr2)$",
        orientation_locators=(
            "https://www.guidetoimmunopharmacology.org/GRAC/ObjectDisplayForward?objectId=64",
            "https://www.guidetoimmunopharmacology.org/GRAC/ObjectDisplayForward?objectId=32",
            "https://www.guidetopharmacology.org/GRAC/LigandDisplayForward?ligandId=3640&tab=refs",
            "PMID:26916158",
        ),
        primary_locators=("PMID:9382922", "PMID:8702752", "PMID:8898085", "PMID:9596584"),
        reuse_constraints=(
            "Reusable only when fragment specificity stays explicit. Do not "
            "treat undifferentiated C3 or C5 as direct receptor ligands without "
            "stating the fragment-level caveat."
        ),
        notes=(
            "This packet consolidates the repeated complement-fragment caution "
            "pattern across C3aR1, C5aR1, and CR2 rows."
        ),
    ),
    FamilyPacketRule(
        family_packet_id="M20A-REUSE-006",
        packet_label="CXCR3 chemokine canonical packet",
        packet_kind="family_orientation_plus_primary_reuse",
        pair_regex=r"^(Cxcl9|Cxcl10|Cxcl11|CXCL9|CXCL10|CXCL11) Cxcr3$",
        orientation_locators=("PMID:14515277",),
        primary_locators=("PMID:11500837", "PMID:12571234", "PMID:15273303"),
        reuse_constraints=(
            "Reusable for canonical CXCL9/CXCL10/CXCL11 to CXCR3 support; do "
            "not transfer this packet to CCR3 side-pairs or other chemokine "
            "receptors."
        ),
        notes=(
            "This packet captures the repeated canonical CXCR3 chemokine packet "
            "already logged for the high-confidence audited CXCR3 rows."
        ),
    ),
    FamilyPacketRule(
        family_packet_id="M20A-REUSE-007",
        packet_label="CCR7 cognate chemokine packet",
        packet_kind="family_orientation_plus_primary_reuse",
        pair_regex=r"^(Ccl19|CCL19|Ccl21|Ccl21a|Ccl21b|Ccl21d|Ccl21e|Ccl21f) Ccr7$",
        orientation_locators=("PMID:34586443",),
        primary_locators=("PMID:9153236", "PMID:15054093", "PMID:11342595"),
        reuse_constraints=(
            "Reusable for canonical CCR7 cognate-chemokine orientation. Keep "
            "paralog-specific mouse caution explicit for Ccl21 variants and do "
            "not collapse CCL19 and CCL21 behavior into one undifferentiated "
            "packet."
        ),
        notes=(
            "This packet captures the repeated CCR7 cognate-chemokine logic "
            "already logged for CCL19 and the earlier Ccl21a/Ccl21b starter rows."
        ),
    ),
    FamilyPacketRule(
        family_packet_id="M20A-REUSE-008",
        packet_label="CXCL12-CXCR4 canonical packet",
        packet_kind="family_orientation_plus_primary_reuse",
        pair_regex=r"^(Cxcl12|CXCL12) Cxcr4$",
        orientation_locators=("PMID:24722947",),
        primary_locators=("PMID:10074122",),
        reuse_constraints=(
            "Reusable for canonical CXCL12-CXCR4 orientation and direct support "
            "only; do not extend to atypical ACKR/CXCR comparator rows."
        ),
        notes=(
            "This packet captures the canonical CXCL12-CXCR4 direct packet "
            "already logged in the starter evidence lane."
        ),
    ),
    FamilyPacketRule(
        family_packet_id="M20A-REUSE-009",
        packet_label="CCR3 nonprincipal-ligand caution packet",
        packet_kind="family_caution_reuse",
        pair_regex=r"^(CCL5|CCL7|CCL8|CXCL9|CXCL10|CXCL11|CXCL16|Ccl5|Ccl6|Ccl7|Ccl8|Ccl9|Ccl24|Ccl26|Ccl27a|Ccl27b|Ccl28) Ccr3$",
        orientation_locators=(
            "work/module20_db_seed/gtopdb_module20_priority_seeds/gtopdb_endogenous_module20_priority.tsv",
            "PMID:8642344",
        ),
        primary_locators=(),
        reuse_constraints=(
            "Reusable only as a caution packet. These rows frequently appear as "
            "secondary or nonprincipal endogenous CCR3 ligands in the local "
            "GtoPdb mirror and should not be auto-promoted to high confidence."
        ),
        notes=(
            "This packet captures the repeated low-confidence CCR3 side-pair "
            "pattern observed in the GtoPdb and CellChat fast-path stress batches."
        ),
    ),
    FamilyPacketRule(
        family_packet_id="M20A-REUSE-010",
        packet_label="CCR5 promiscuous comparator packet",
        packet_kind="family_caution_reuse",
        pair_regex=r"^(CCL2|CCL3|CCL4|CCL5|CCL7|CCL8|CCL11|Ccl3|Ccl4|Ccl5|Ccl8) Ccr5$",
        orientation_locators=(
            "work/module20_db_seed/gtopdb_module20_priority_seeds/gtopdb_endogenous_module20_priority.tsv",
            "PMID:16298345",
            "PMID:9790730",
            "PMID:10318947",
            "PMID:11170631",
            "PMID:10477718",
        ),
        primary_locators=(),
        reuse_constraints=(
            "Reusable only as a promiscuous-comparator packet. These rows may be "
            "retained as database-backed comparator pairs, but local mouse-primary "
            "support is often absent and species confidence should stay conservative."
        ),
        notes=(
            "This packet consolidates the repeated CCR5 side-pair comparator "
            "pattern from the GtoPdb and CellChat fast-path stress batches."
        ),
    ),
    FamilyPacketRule(
        family_packet_id="M20A-REUSE-011",
        packet_label="CCR1 and CCR2 secondary-ligand caution packet",
        packet_kind="family_caution_reuse",
        pair_regex=r"^(CCL7|CCL8|Ccl5|Ccl6|Ccl8|Ccl9) Ccr[12]$",
        orientation_locators=(
            "work/module20_db_seed/gtopdb_module20_priority_seeds/gtopdb_endogenous_module20_priority.tsv",
            "PMID:12381680",
            "PMID:11994538",
            "PMID:9276730",
            "PMID:9346309",
            "PMID:12554737",
        ),
        primary_locators=(),
        reuse_constraints=(
            "Reusable only as a caution packet. These rows often appear with local "
            "GtoPdb comments indicating different principal endogenous agonists, so "
            "they should stay below high confidence without stronger pair-specific evidence."
        ),
        notes=(
            "This packet captures the repeated CCR1 and CCR2 secondary-ligand "
            "pattern from the sparse-citation fast-lane batches."
        ),
    ),
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, headers: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def normalize_list(values: set[str]) -> str:
    return ";".join(sorted(value for value in values if value))


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    starter_dir = root / "work" / "module20_db_seed" / "evidence_escalation_starter"
    evidence_files = sorted(starter_dir.glob("*evidence_register.tsv"))

    evidence_by_pair: dict[str, list[dict[str, str]]] = defaultdict(list)
    for evidence_file in evidence_files:
        for row in read_tsv(evidence_file):
            row = dict(row)
            row["_origin_file"] = evidence_file.name
            evidence_by_pair[row["pair_label"]].append(row)

    family_rows: list[dict[str, str]] = []
    reuse_rows: list[dict[str, str]] = []

    for rule in FAMILY_PACKET_RULES:
        matched_pairs = sorted(pair for pair in evidence_by_pair if rule.matches_pair(pair))
        matched_evidence = [
            row
            for pair in matched_pairs
            for row in evidence_by_pair[pair]
            if row["source_locator"] in set(rule.orientation_locators + rule.primary_locators)
        ]

        evidence_item_ids = {row["evidence_item_id"] for row in matched_evidence}
        evidence_origin_files = {row["_origin_file"] for row in matched_evidence}

        family_rows.append(
            {
                "family_packet_id": rule.family_packet_id,
                "packet_label": rule.packet_label,
                "packet_kind": rule.packet_kind,
                "pair_match_rule": rule.pair_regex,
                "reusable_orientation_locators": ";".join(rule.orientation_locators),
                "reusable_primary_locators": ";".join(rule.primary_locators),
                "reuse_constraints": rule.reuse_constraints,
                "supporting_pair_count": str(len(matched_pairs)),
                "supporting_pairs": ";".join(matched_pairs),
                "supporting_evidence_item_ids": normalize_list(evidence_item_ids),
                "evidence_origin_files": normalize_list(evidence_origin_files),
                "notes": rule.notes,
            }
        )

        for pair in matched_pairs:
            pair_evidence = [row for row in evidence_by_pair[pair] if row["source_locator"] in set(rule.orientation_locators + rule.primary_locators)]
            pair_note = (
                "Start from this family packet before any broader search; retain "
                "pair-specific species caveats from the existing evidence rows."
            )
            reuse_rows.append(
                {
                    "pair_label": pair,
                    "family_packet_id": rule.family_packet_id,
                    "reuse_status": "family_packet_available",
                    "reuse_priority": "1",
                    "reusable_orientation_locators": ";".join(rule.orientation_locators),
                    "reusable_primary_locators": ";".join(rule.primary_locators),
                    "supporting_evidence_item_ids": normalize_list({row["evidence_item_id"] for row in pair_evidence}),
                    "evidence_origin_files": normalize_list({row["_origin_file"] for row in pair_evidence}),
                    "reuse_constraints": rule.reuse_constraints,
                    "notes": pair_note,
                }
            )

    write_tsv(
        starter_dir / "module20a_family_evidence_packets.tsv",
        FAMILY_PACKET_HEADERS,
        family_rows,
    )
    write_tsv(
        starter_dir / "module20a_citation_reuse_registry.tsv",
        REUSE_REGISTRY_HEADERS,
        sorted(reuse_rows, key=lambda row: (row["pair_label"], row["family_packet_id"])),
    )


if __name__ == "__main__":
    main()
