# Spark / PySpark Performance Notes

## Partitioning
Partition data according to common filters and data distribution. Avoid over-partitioning, which can create excessive small files and scheduling overhead.

## Shuffle
Operations such as joins, groupBy, distinct and orderBy may trigger shuffle. Reduce unnecessary movement by filtering early, selecting only required columns and choosing appropriate join strategies.

## Broadcast join
Broadcast a small dimension table when it is safe to fit in executor memory, avoiding a large shuffle on the bigger dataset.

## Repartition vs coalesce
- `repartition()` can increase or decrease partitions and triggers shuffle.
- `coalesce()` is generally used to reduce partitions with less data movement.

## Data skew
Highly uneven keys can overload a small number of partitions. Diagnose skew from task duration and partition sizes; consider salting, repartitioning or alternative join strategies when necessary.

## Cache / persist
Use only for DataFrames reused multiple times and large enough to justify memory/storage cost. Avoid caching by default.

## File format
Prefer columnar formats such as Parquet/Delta for analytical processing, with compression and column pruning.

## Incremental processing
Process only new or changed records whenever the business semantics allow it. Combine watermarks, CDC or ingestion metadata with idempotent MERGE logic.
