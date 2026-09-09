# AWS Redshift + DMS Modernization Reference Architecture

Reference project focused on migration, replication and analytical modernization on AWS.

> This is a portfolio reference architecture based on common Data Engineering patterns. It does not claim direct production use of Redshift or AWS DMS in previous employment.

## Scenario

A legacy relational database supports operational workloads, while analytics teams need fresher data and a scalable analytical layer without overloading the source system.

## Target architecture

```text
Operational Database
      |
      | Full Load + CDC
      v
   AWS DMS
      |
      v
Amazon S3 / Staging
      |
      v
Transformation Layer
  Glue / SQL / Python
      |
      v
Amazon Redshift
      |
      +--> BI / Analytics
      +--> Data Marts
```

## Goals

- Minimize downtime during migration
- Use CDC to capture ongoing changes
- Separate operational and analytical workloads
- Improve analytical query performance
- Preserve traceability and reprocessing capability
- Add data quality and observability checks

## Key design decisions

### Full load + CDC
The initial historical dataset is migrated once. After the baseline load, CDC continuously captures inserts, updates and deletes from the source until cutover.

### Staging layer
S3 is used as a durable intermediate layer for raw or staged data, enabling replay, auditability and decoupling between source ingestion and analytical transformation.

### Redshift analytical layer
Redshift is used for OLAP workloads, large scans, aggregations and BI-oriented access. Tables should be modeled according to access patterns rather than simply copying the OLTP schema.

### Performance
Key considerations include:

- columnar storage
- sort strategy
- distribution strategy
- predicate filtering
- compression
- workload management
- avoiding unnecessary full-table scans

## Reliability and observability

Track at least:

- DMS task status
- replication lag
- rejected/failed records
- row-count reconciliation
- data freshness
- load duration
- Redshift query performance

## Security

- IAM least privilege
- encryption at rest and in transit
- Secrets Manager for credentials
- restricted network access
- audit logging

## Repository contents

- `sql/redshift_star_schema.sql` — simple analytical model
- `sql/data_quality_checks.sql` — validation examples
- `docs/migration-runbook.md` — migration and cutover steps
- `tests/test_transformations.py` — lightweight transformation tests

## What this project demonstrates

- Understanding of DMS migration/replication patterns
- CDC and incremental data movement
- Separation of OLTP and OLAP workloads
- Redshift-oriented analytical modeling
- Data quality, observability and operational thinking

## Portfolio context

This lab extends the AWS concepts used in my main portfolio case. For the strongest production-inspired example — including executable incremental logic, idempotency, watermark handling, tests, observability and reprocessing — see the **[AWS Incremental Data Pipeline flagship](../aws-incremental-data-pipeline/)**.
