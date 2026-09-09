from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def build_silver(df: DataFrame) -> DataFrame:
    """Clean, standardize and deduplicate customer records."""
    window = Window.partitionBy("customer_id").orderBy(F.col("updated_at").desc())

    return (
        df
        .filter(F.col("customer_id").isNotNull())
        .withColumn("email", F.lower(F.trim(F.col("email"))))
        .withColumn("_row_number", F.row_number().over(window))
        .filter(F.col("_row_number") == 1)
        .drop("_row_number")
    )
