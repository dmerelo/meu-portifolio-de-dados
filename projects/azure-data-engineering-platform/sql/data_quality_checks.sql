-- Reference data quality checks for a curated orders dataset.

-- 1. Null business keys
SELECT COUNT(*) AS null_order_ids
FROM gold.orders
WHERE order_id IS NULL;

-- 2. Duplicate business keys
SELECT order_id, COUNT(*) AS duplicate_count
FROM gold.orders
GROUP BY order_id
HAVING COUNT(*) > 1;

-- 3. Invalid amounts
SELECT COUNT(*) AS invalid_amounts
FROM gold.orders
WHERE amount < 0;

-- 4. Unexpected status values
SELECT status, COUNT(*) AS rows_per_status
FROM gold.orders
GROUP BY status
HAVING status NOT IN ('pending', 'paid', 'cancelled', 'shipped', 'delivered');

-- 5. Freshness check
SELECT MAX(updated_at) AS latest_record_timestamp
FROM gold.orders;
