import importlib.util
from pathlib import Path
import sys

import pytest

MODULE_PATH = Path(__file__).resolve().parents[1] / "src" / "incremental_pipeline.py"
spec = importlib.util.spec_from_file_location("incremental_pipeline", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

DataQualityError = module.DataQualityError
execute = module.execute
merge_rows = module.merge_rows
select_incremental = module.select_incremental


def test_selects_only_rows_newer_than_watermark_and_deduplicates():
    rows = [
        {"customer_id": "1", "updated_at": "2026-09-07T10:00:00+00:00", "amount": "100"},
        {"customer_id": "1", "updated_at": "2026-09-07T11:00:00+00:00", "amount": "120"},
        {"customer_id": "2", "updated_at": "2026-09-05T11:00:00+00:00", "amount": "50"},
    ]

    result = select_incremental(rows, "2026-09-06T00:00:00+00:00")

    assert len(result) == 1
    assert result[0]["customer_id"] == "1"
    assert result[0]["amount"] == "120"


def test_merge_is_idempotent_for_same_batch():
    target = [
        {"customer_id": "1", "updated_at": "2026-09-07T09:00:00+00:00", "amount": "100"}
    ]
    incoming = [
        {"customer_id": "1", "updated_at": "2026-09-07T10:00:00+00:00", "amount": "120"}
    ]

    first = merge_rows(target, incoming)
    second = merge_rows(first, incoming)

    assert first == second
    assert len(second) == 1
    assert second[0]["amount"] == "120"


def test_watermark_advances_only_to_latest_processed_change():
    source = [
        {"customer_id": "1", "updated_at": "2026-09-07T10:00:00+00:00", "amount": "100"},
        {"customer_id": "2", "updated_at": "2026-09-07T12:30:00+00:00", "amount": "200"},
    ]

    merged, metrics = execute(source, [], "2026-09-06T00:00:00+00:00")

    assert len(merged) == 2
    assert metrics.rows_read == 2
    assert metrics.rows_selected == 2
    assert metrics.rows_upserted == 2
    assert metrics.target_rows_after_merge == 2
    assert metrics.candidate_watermark == "2026-09-07T12:30:00+00:00"


def test_watermark_does_not_advance_when_no_new_rows_exist():
    watermark = "2026-09-08T00:00:00+00:00"
    source = [
        {"customer_id": "1", "updated_at": "2026-09-07T10:00:00+00:00", "amount": "100"}
    ]

    _, metrics = execute(source, [], watermark)

    assert metrics.rows_selected == 0
    assert metrics.rows_upserted == 0
    assert metrics.candidate_watermark == watermark


def test_rejects_empty_business_key():
    rows = [
        {"customer_id": "", "updated_at": "2026-09-07T10:00:00+00:00", "amount": "100"}
    ]

    with pytest.raises(DataQualityError, match="empty customer_id"):
        select_incremental(rows, "2026-09-06T00:00:00+00:00")


def test_rejects_invalid_timestamp():
    rows = [{"customer_id": "1", "updated_at": "not-a-date", "amount": "100"}]

    with pytest.raises(DataQualityError, match="Invalid ISO-8601 timestamp"):
        select_incremental(rows, "2026-09-06T00:00:00+00:00")


def test_rejects_missing_required_column():
    rows = [{"customer_id": "1", "amount": "100"}]

    with pytest.raises(DataQualityError, match="missing required columns"):
        select_incremental(rows, "2026-09-06T00:00:00+00:00")
