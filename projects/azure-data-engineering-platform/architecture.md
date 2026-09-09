# Architecture Decisions — Azure Data Engineering Platform

## 1. Ingestion and orchestration

Use **Azure Data Factory (ADF)** for source connectivity and pipeline orchestration.

A typical incremental pattern:

1. read the last successful watermark from pipeline metadata;
2. query the source using that watermark;
3. write new or changed records to ADLS Raw;
4. validate ingestion counts;
5. update the watermark only after successful completion.

This prevents advancing the checkpoint when a downstream step fails.

## 2. Storage layout

ADLS Gen2 separates data by processing responsibility:

```text
/raw/<source>/<entity>/ingestion_date=YYYY-MM-DD/
/bronze/<domain>/<entity>/
/silver/<domain>/<entity>/
/gold/<domain>/<dataset>/
```

Partition keys should reflect common filtering patterns and should avoid excessive cardinality.

## 3. Processing

Azure Databricks / PySpark handles transformations that benefit from distributed compute.

Key optimization principles:

- filter as early as possible;
- select only required columns;
- avoid unnecessary shuffles;
- broadcast genuinely small dimension tables when appropriate;
- compact small files where necessary;
- use partitioning based on access patterns rather than arbitrary columns.

## 4. Idempotency

A rerun for the same input window should not duplicate target records.

Typical strategies:

- deterministic business keys;
- deduplication before write;
- MERGE/upsert for mutable datasets;
- immutable partition replacement for append-oriented datasets;
- checkpoint/watermark updates only after successful writes.

## 5. Security

- credentials in Azure Key Vault;
- workload identities instead of hard-coded secrets when possible;
- least privilege access;
- separate permissions for raw, curated and consumption zones;
- avoid exposing PII to layers that do not require it.

## 6. Data quality

Quality checks should be automated and observable:

- primary/business key uniqueness;
- mandatory field completeness;
- accepted value checks;
- source-target row count reconciliation;
- freshness validation;
- duplicate rate monitoring.

## 7. Failure and reprocessing strategy

Store enough metadata to answer:

- which source window was processed?
- which files were produced?
- what watermark was used?
- where did the execution fail?
- can the same window be safely rerun?

A senior-level pipeline design treats reprocessing as part of the architecture, not an emergency procedure.

## 8. AWS comparison

The architectural reasoning maps directly to common AWS patterns:

```text
ADF                     -> Glue/Step Functions orchestration concepts
ADLS Gen2               -> S3
Azure Databricks        -> Databricks on AWS / distributed Spark
Key Vault               -> Secrets Manager
Azure Monitor           -> CloudWatch
Entra ID                -> IAM/federated identity concepts
```

The services differ, but the core decisions remain: incremental processing, idempotency, security, observability, quality and cost-aware design.
