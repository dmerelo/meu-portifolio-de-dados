from pyspark.sql import DataFrame, Window
from pyspark.sql import functions as F


def build_silver_orders(bronze_df: DataFrame) -> DataFrame:
    """Create a cleaned, deduplicated Silver dataset from Bronze orders."""

    normalized = (
        bronze_df
        .select(
            F.col("order_id").cast("long").alias("order_id"),
            F.col("customer_id").cast("long").alias("customer_id"),
            F.to_timestamp("updated_at").alias("updated_at"),
            F.col("status").cast("string").alias("status"),
            F.col("amount").cast("decimal(18,2)").alias("amount")
        )
        .filter(F.col("order_id").isNotNull())
    )

    window = Window.partitionBy("order_id").orderBy(F.col("updated_at").desc())

    deduplicated = (
        normalized
        .withColumn("row_number", F.row_number().over(window))
        .filter(F.col("row_number") == 1)
        .drop("row_number")
    )

    return deduplicated
