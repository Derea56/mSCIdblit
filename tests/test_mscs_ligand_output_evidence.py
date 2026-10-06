import importlib.util
import json
import sqlite3
import struct
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "build_mscs_ligand_output_evidence.py"
SPEC = importlib.util.spec_from_file_location("build_mscs_ligand_output_evidence", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_builds_release_owned_indexed_ligand_output_database(tmp_path):
    release = tmp_path / "release"
    neutral = release / "method_resources/method_native/nichenet_neutral_v1"
    _write(release / "release_manifest.json", json.dumps({"release_id": "release:test"}))
    _write(neutral / "ligands.tsv", "ligand_id\nL1\nL2\n")
    _write(neutral / "target_genes.tsv", "target_id\nO1\nO2\nO3\n")
    _write(
        neutral / "neutral_model_manifest.json",
        json.dumps(
            {
                "matrix_shape": [3, 2],
                "matrix_dtype": "float64",
                "matrix_endianness": "little",
                "matrix_layout": "column_major",
                "source_model": "synthetic",
                "species": "mouse",
            }
        ),
    )
    matrix = tmp_path / "matrix.bin"
    matrix.write_bytes(struct.pack("<6d", 0.2, 0.9, 0.1, 0.4, 0.3, 0.8))

    output = release / "mechanism_graph/ligand_output_evidence"
    manifest = MODULE.build_ligand_output_evidence(
        release,
        matrix,
        output,
        register_in_release=True,
    )

    assert manifest["counts"]["relationships"] == 6
    assert manifest["database"]["table"] == "ligand_output_prior"
    with sqlite3.connect(output / "ligand_output_evidence.sqlite") as connection:
        rows = connection.execute(
            """
            SELECT l.ligand_id, t.target_id, p.target_rank_within_ligand,
                   p.regulatory_potential
            FROM ligand_output_prior AS p
            JOIN ligands AS l ON l.ligand_idx = p.ligand_idx
            JOIN targets AS t ON t.target_idx = p.target_idx
            WHERE l.ligand_id = 'L1'
            ORDER BY p.target_rank_within_ligand
            """
        ).fetchall()
    assert rows == [("L1", "O2", 1, 0.9), ("L1", "O1", 2, 0.2), ("L1", "O3", 3, 0.1)]

    release_manifest = json.loads((release / "release_manifest.json").read_text())
    assert release_manifest["ligand_output_evidence_database_path"].endswith(
        "mechanism_graph/ligand_output_evidence/ligand_output_evidence.sqlite"
    )
