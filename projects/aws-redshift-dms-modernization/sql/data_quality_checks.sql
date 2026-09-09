-- Basic data quality checks for the analytical layer

-- 1. Duplicate business keys in current customer records
SELECT customer_id, COUNT(*) AS qty
FROM dim_customer
WHERE is_current = TRUE
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- 2. Facts without matching dimension records
SELECT COUNT(*) AS orphan_orders
FROM fact_orders f
LEFT JOIN dim_customer c ON f.customer_sk = c.customer_sk
WHERE c.customer_sk IS NULL;

-- 3. Null critical fields
SELECT COUNT(*) AS invalid_orders
FROM fact_orders
WHERE order_id IS NULL
   OR customer_sk IS NULL
   OR date_key IS NULL;

-- 4. Freshness check
SELECT MAX(updated_at) AS latest_record_timestamp
FROM fact_orders;
