#!/usr/bin/env python3
"""Load a validated mechanism bundle into PostgreSQL using the psql client."""

from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ROOT / "data" / "processed" / "mechanism_graph_module20_24_v2026_08_25"
TEMPLATE = ROOT / "scripts" / "load_mechanism_graph_bundle.sql"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--database-url",
        default=os.environ.get("MSCIDBLIT_DATABASE_URL") or os.environ.get("DATABASE_URL"),
        help="PostgreSQL connection string accepted by psql -d.",
    )
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--psql", default="psql", help="psql executable")
    return parser.parse_args()


def sql_literal(path: Path) -> str:
    return "'" + str(path.resolve()).replace("'", "''") + "'"


def main() -> None:
    args = parse_args()
    if not args.database_url:
        raise SystemExit("Provide --database-url or set MSCIDBLIT_DATABASE_URL/DATABASE_URL.")
    bundle_dir = args.bundle_dir.resolve()
    required = {
        "nodes_file": bundle_dir / "mechanism_nodes.tsv",
        "roles_file": bundle_dir / "mechanism_node_roles.tsv",
        "edges_file": bundle_dir / "mechanism_edges.tsv",
        "sources_file": bundle_dir / "mechanism_edge_sources.tsv",
        "pathways_file": bundle_dir / "mechanism_pathways.tsv",
    }
    missing = [str(path) for path in required.values() if not path.exists()]
    if missing:
        raise SystemExit("Bundle is missing required files: " + ", ".join(missing))

    sql = TEMPLATE.read_text()
    for variable, path in required.items():
        sql = sql.replace(f":{variable}", sql_literal(path))

    command = [args.psql, "-X", "-v", "ON_ERROR_STOP=1", "-d", args.database_url, "-f", "-"]
    result = subprocess.run(command, input=sql, text=True, check=False)
    raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
