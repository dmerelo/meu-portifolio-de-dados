-- Reference analytical model for Amazon Redshift

CREATE TABLE dim_customer (
    customer_sk BIGINT IDENTITY(1,1),
    customer_id VARCHAR(64) NOT NULL,
    customer_name VARCHAR(255),
    region VARCHAR(100),
    valid_from TIMESTAMP,
    valid_to TIMESTAMP,
    is_current BOOLEAN DEFAULT TRUE
);

CREATE TABLE dim_date (
    date_key INTEGER NOT NULL,
    full_date DATE NOT NULL,
    year INTEGER,
    month INTEGER,
    day INTEGER
);

CREATE TABLE fact_orders (
    order_id VARCHAR(64) NOT NULL,
    customer_sk BIGINT NOT NULL,
    date_key INTEGER NOT NULL,
    order_amount DECIMAL(18,2),
    updated_at TIMESTAMP
);

-- Example analytical query
SELECT
    d.year,
    d.month,
    c.region,
    SUM(f.order_amount) AS revenue
FROM fact_orders f
JOIN dim_customer c ON f.customer_sk = c.customer_sk
JOIN dim_date d ON f.date_key = d.date_key
WHERE c.is_current = TRUE
GROUP BY d.year, d.month, c.region
ORDER BY d.year, d.month, c.region;
