from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import csv


@dataclass
class PipelineMetrics:
    rows_read: int
    rows_selected: int
    rows_written: int
    previous_watermark: str
    new_watermark: str


def read_rows(path: Path):
    with path.open(encoding="utf-8") as file:
        return list(csv.DictReader(file))


def select_incremental(rows, watermark: str):
    watermark_dt = datetime.fromisoformat(watermark)
    selected = [row for row in rows if datetime.fromisoformat(row["updated_at"]) > watermark_dt]

    latest_by_key = {}
    for row in selected:
        key = row["customer_id"]
        previous = latest_by_key.get(key)
        if previous is None or row["updated_at"] > previous["updated_at"]:
            latest_by_key[key] = row

    return list(latest_by_key.values())


def merge_rows(current_rows, incoming_rows):
    target = {row["customer_id"]: dict(row) for row in current_rows}
    for row in incoming_rows:
        current = target.get(row["customer_id"])
        if current is None or row["updated_at"] >= current["updated_at"]:
            target[row["customer_id"]] = dict(row)
    return list(target.values())


def execute(source_rows, target_rows, previous_watermark: str):
    incremental_rows = select_incremental(source_rows, previous_watermark)
    merged = merge_rows(target_rows, incremental_rows)

    new_watermark = previous_watermark
    if incremental_rows:
        new_watermark = max(row["updated_at"] for row in incremental_rows)

    metrics = PipelineMetrics(
        rows_read=len(source_rows),
        rows_selected=len(incremental_rows),
        rows_written=len(merged),
        previous_watermark=previous_watermark,
        new_watermark=new_watermark,
    )
    return merged, metrics


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    source = read_rows(root / "data" / "incremental_batch.csv")
    target = read_rows(root / "data" / "full_snapshot.csv")
    merged, metrics = execute(source, target, "2026-09-06T23:59:59+00:00")
    print(metrics)
    print("Target row count:", len(merged))
