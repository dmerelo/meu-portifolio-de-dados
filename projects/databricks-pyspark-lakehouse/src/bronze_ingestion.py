from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def ingest_bronze(df: DataFrame, source_name: str) -> DataFrame:
    """Add ingestion metadata while preserving source data."""
    return (
        df
        .withColumn("_ingestion_ts", F.current_timestamp())
        .withColumn("_source", F.lit(source_name))
    )
