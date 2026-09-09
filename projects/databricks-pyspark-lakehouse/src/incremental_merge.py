def merge_incremental(spark, source_view: str, target_table: str) -> None:
    """Reference Delta MERGE pattern for idempotent incremental upserts."""
    spark.sql(f"""
        MERGE INTO {target_table} AS target
        USING {source_view} AS source
        ON target.customer_id = source.customer_id
        WHEN MATCHED AND source.updated_at >= target.updated_at THEN
          UPDATE SET *
        WHEN NOT MATCHED THEN
          INSERT *
    """)
