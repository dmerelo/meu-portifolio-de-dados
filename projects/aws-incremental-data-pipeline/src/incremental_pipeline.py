from __future__ import annotations

import csv
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import TypeAlias

Row: TypeAlias = dict[str, str]
RowLike: TypeAlias = Mapping[str, str]

REQUIRED_COLUMNS = {"customer_id", "updated_at"}


class DataQualityError(ValueError):
    """Raised when input data violates a blocking quality rule."""


@dataclass(frozen=True)
class PipelineMetrics:
    rows_read: int
    rows_selected: int
    rows_upserted: int
    target_rows_after_merge: int
    previous_watermark: str
    candidate_watermark: str


def parse_timestamp(value: str) -> datetime:
    try:
        return datetime.fromisoformat(value)
    except (TypeError, ValueError) as exc:
        raise DataQualityError(f"Invalid ISO-8601 timestamp: {value!r}") from exc


def validate_rows(rows: Iterable[RowLike]) -> list[Row]:
    validated: list[Row] = []

    for index, source_row in enumerate(rows, start=1):
        row = dict(source_row)
        missing = REQUIRED_COLUMNS - row.keys()
        if missing:
            raise DataQualityError(
                f"Row {index} is missing required columns: {sorted(missing)}"
            )

        if not row["customer_id"].strip():
            raise DataQualityError(f"Row {index} has an empty customer_id")

        parse_timestamp(row["updated_at"])
        validated.append(row)

    return validated


def read_rows(path: Path) -> list[Row]:
    with path.open(encoding="utf-8", newline="") as file:
        return validate_rows(csv.DictReader(file))


def select_incremental(rows: Iterable[RowLike], watermark: str) -> list[Row]:
    watermark_dt = parse_timestamp(watermark)
    validated_rows = validate_rows(rows)
    latest_by_key: dict[str, Row] = {}

    for row in validated_rows:
        row_timestamp = parse_timestamp(row["updated_at"])
        if row_timestamp <= watermark_dt:
            continue

        key = row["customer_id"]
        previous = latest_by_key.get(key)
        if previous is None or row_timestamp > parse_timestamp(previous["updated_at"]):
            latest_by_key[key] = row

    return sorted(latest_by_key.values(), key=lambda row: row["customer_id"])


def merge_rows(
    current_rows: Iterable[RowLike], incoming_rows: Iterable[RowLike]
) -> list[Row]:
    current = validate_rows(current_rows)
    incoming = validate_rows(incoming_rows)
    target: dict[str, Row] = {row["customer_id"]: row for row in current}

    for row in incoming:
        key = row["customer_id"]
        existing = target.get(key)
        if existing is None or parse_timestamp(row["updated_at"]) >= parse_timestamp(
            existing["updated_at"]
        ):
            target[key] = row

    return [target[key] for key in sorted(target)]


def execute(
    source_rows: Iterable[RowLike],
    target_rows: Iterable[RowLike],
    previous_watermark: str,
) -> tuple[list[Row], PipelineMetrics]:
    source = validate_rows(source_rows)
    target = validate_rows(target_rows)
    parse_timestamp(previous_watermark)

    incremental_rows = select_incremental(source, previous_watermark)
    merged = merge_rows(target, incremental_rows)

    candidate_watermark = previous_watermark
    if incremental_rows:
        candidate_watermark = max(
            incremental_rows,
            key=lambda row: parse_timestamp(row["updated_at"]),
        )["updated_at"]

    metrics = PipelineMetrics(
        rows_read=len(source),
        rows_selected=len(incremental_rows),
        rows_upserted=len(incremental_rows),
        target_rows_after_merge=len(merged),
        previous_watermark=previous_watermark,
        candidate_watermark=candidate_watermark,
    )
    return merged, metrics


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    source = read_rows(root / "data" / "incremental_batch.csv")
    target = read_rows(root / "data" / "full_snapshot.csv")
    merged, metrics = execute(source, target, "2026-09-06T23:59:59+00:00")
    print(metrics)
    print("Target row count:", len(merged))
