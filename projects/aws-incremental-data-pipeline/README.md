# AWS Incremental Data Pipeline — Reference Architecture

This is a **sanitized portfolio/reference project** inspired by a real class of production problem: replacing expensive daily full-load processing with an incremental architecture.

It does **not** contain proprietary code, internal datasets or confidential architecture from previous employers.

## Problem

A common legacy pattern is to reload and reprocess the complete historical dataset every day, even when only a small percentage of records changed.

Typical consequences:
- long-running jobs;
- unnecessary reads and compute;
- higher cloud cost;
- increased failure surface;
- difficult reprocessing;
- poor scalability as history grows.

## Target design

```text
Source systems
      |
      v
Raw / Landing (S3)
      |
      | incremental detection
      v
Processing (Glue / Python / SQL)
      |
      | validation + deduplication + transformation
      v
Curated data (S3 / analytical store)
      |
      v
Athena / Aurora / BI / APIs
```

## Incremental strategy

The pipeline should identify only records that are new or changed since the previous successful execution.

Possible mechanisms include:
- `updated_at` timestamp;
- watermark table;
- CDC event position;
- monotonically increasing key;
- ingestion date/partition.

The selected mechanism depends on source-system guarantees and business requirements.

## Idempotency

A production pipeline should be safe to execute more than once for the same logical batch.

Key techniques:
- deterministic batch identifiers;
- deduplication using business/technical keys;
- upsert/merge instead of blind append when updates exist;
- persist the watermark only after successful processing;
- isolate failed batches for controlled reprocessing.

## Partitioning

Partitioning should reduce the amount of data scanned without creating an excessive number of tiny partitions/files.

Typical partition candidates:
- ingestion date;
- event/reference date;
- region or domain when cardinality is appropriate.

Partitioning is an optimization strategy — it is **not** the mechanism that defines incremental processing by itself.

## Data quality

Example checks:
- primary/business key not null;
- duplicate detection;
- schema/type validation;
- expected row-count ranges;
- freshness;
- domain/range validation;
- reconciliation between source and target batches.

## Observability

At minimum, capture:
- pipeline execution status;
- start/end time and duration;
- input/output row counts;
- rejected records;
- last successful watermark;
- data freshness;
- retries/failures;
- processing volume and cloud cost indicators.

In AWS, these signals can be integrated with CloudWatch logs, metrics and alarms.

## Reprocessing

A resilient design should support reprocessing a specific batch or partition without rebuilding the entire historical dataset.

Recommended pattern:
1. identify the failed logical batch;
2. preserve or restore the previous valid watermark;
3. re-read the affected source slice;
4. apply deterministic transformations;
5. merge/upsert into the target;
6. validate row counts and quality;
7. commit the new watermark only after success.

## Trade-offs

### Full load can still be appropriate when
- dataset is small;
- source does not expose a reliable change indicator;
- simplicity is more valuable than optimization;
- reload time and cost remain acceptable.

### Incremental processing becomes attractive when
- historical volume is large;
- daily change rate is small compared with total history;
- jobs have long runtimes;
- compute/scanning cost is material;
- reprocessing and SLA requirements matter.

## Files

- [`architecture.md`](./architecture.md) — design decisions and failure handling
- [`sql/incremental_upsert.sql`](./sql/incremental_upsert.sql) — vendor-neutral upsert/merge example

## What this project demonstrates

This reference architecture is intended to demonstrate Senior Data Engineering reasoning around:

`incremental processing` · `idempotency` · `partitioning` · `data quality` · `observability` · `reprocessing` · `performance` · `cloud cost`
