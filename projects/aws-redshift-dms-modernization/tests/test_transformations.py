def normalize_region(value: str) -> str:
    return value.strip().upper()


def test_normalize_region():
    assert normalize_region("  southeast ") == "SOUTHEAST"


def test_incremental_batch_has_business_key():
    batch = [
        {"order_id": "A1", "updated_at": "2026-09-01T10:00:00"},
        {"order_id": "A2", "updated_at": "2026-09-01T10:05:00"},
    ]
    assert all(row.get("order_id") for row in batch)
