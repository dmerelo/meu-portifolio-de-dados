-- Vendor-neutral example of an incremental upsert pattern.
-- Adapt syntax to the target engine (for example, Redshift, PostgreSQL-compatible systems,
-- Snowflake, Delta Lake SQL, etc.).

MERGE INTO curated_customer AS target
USING incremental_customer AS source
   ON target.customer_id = source.customer_id

WHEN MATCHED
 AND source.updated_at > target.updated_at
THEN UPDATE SET
    customer_name = source.customer_name,
    status        = source.status,
    updated_at    = source.updated_at

WHEN NOT MATCHED
THEN INSERT (
    customer_id,
    customer_name,
    status,
    updated_at
)
VALUES (
    source.customer_id,
    source.customer_name,
    source.status,
    source.updated_at
);

-- Important design notes:
-- 1. customer_id identifies the logical entity.
-- 2. updated_at (or a CDC sequence/watermark) determines whether the incoming version is newer.
-- 3. The same logical batch can be reprocessed without blindly appending duplicate versions.
-- 4. Production implementations should add data-quality validation and transactional safeguards
--    supported by the chosen engine.
