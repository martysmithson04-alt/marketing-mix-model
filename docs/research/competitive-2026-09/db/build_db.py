#!/usr/bin/env python3
"""Build competitive.sqlite from JSONL snapshots. Research only."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = ROOT / "competitive.sqlite"

TABLES = {
    "competitors": "competitors.jsonl",
    "listings": "listings.jsonl",
    "problems": "problems.jsonl",
    "review_quotes": "review_quotes.jsonl",
    "sources": "sources.jsonl",
    "opportunities": "opportunities.jsonl",
    "religion": "religion.jsonl",
}


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def main() -> None:
    if DB.exists():
        DB.unlink()
    con = sqlite3.connect(DB)
    cur = con.cursor()
    for table, filename in TABLES.items():
        rows = load_jsonl(ROOT / filename)
        if not rows:
            continue
        cols = list(rows[0].keys())
        col_sql = ", ".join(f"{c} TEXT" for c in cols)
        cur.execute(f"CREATE TABLE {table} ({col_sql})")
        placeholders = ", ".join("?" * len(cols))
        for row in rows:
            # serialize nested lists/dicts
            values = []
            for c in cols:
                v = row.get(c)
                if isinstance(v, (list, dict)):
                    v = json.dumps(v)
                elif v is None:
                    v = None
                else:
                    v = str(v)
                values.append(v)
            cur.execute(f"INSERT INTO {table} ({', '.join(cols)}) VALUES ({placeholders})", values)
        print(f"{table}: {len(rows)} rows")
    con.commit()
    con.close()
    print(f"wrote {DB}")


if __name__ == "__main__":
    main()
