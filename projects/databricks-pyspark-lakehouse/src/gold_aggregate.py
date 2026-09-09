from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def build_gold_orders(df: DataFrame) -> DataFrame:
    """Create a simple business-facing aggregate."""
    return (
        df
        .groupBy("order_date", "region")
        .agg(
            F.countDistinct("order_id").alias("orders"),
            F.sum("order_amount").alias("revenue")
        )
    )
