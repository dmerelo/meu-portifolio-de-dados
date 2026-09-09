from pathlib import Path
import csv
import random
from datetime import datetime, timedelta, timezone

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

random.seed(42)


def build_rows(total_rows: int = 1000):
    base_time = datetime(2026, 9, 1, tzinfo=timezone.utc)
    rows = []
    for customer_id in range(1, total_rows + 1):
        updated_at = base_time + timedelta(minutes=random.randint(0, 60 * 24 * 5))
        rows.append(
            {
                "customer_id": customer_id,
                "status": random.choice(["active", "inactive", "pending"]),
                "segment": random.choice(["consumer", "smb", "enterprise"]),
                "amount": round(random.uniform(10, 5000), 2),
                "updated_at": updated_at.isoformat(),
            }
        )
    return rows


def write_csv(path: Path, rows):
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def main():
    full_rows = build_rows()
    write_csv(OUTPUT_DIR / "full_snapshot.csv", full_rows)

    incremental_rows = []
    for row in full_rows[:50]:
        changed = dict(row)
        changed["amount"] = round(float(changed["amount"]) * 1.05, 2)
        changed["updated_at"] = datetime(2026, 9, 7, 12, tzinfo=timezone.utc).isoformat()
        incremental_rows.append(changed)

    write_csv(OUTPUT_DIR / "incremental_batch.csv", incremental_rows)
    print("Synthetic datasets generated in", OUTPUT_DIR)


if __name__ == "__main__":
    main()
