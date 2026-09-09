# Interview Defense Guide — Senior Data Engineer Portfolio

This document is a study and interview-preparation guide for the projects in this repository. It separates **production experience** from **hands-on/reference work** and focuses on the architectural decisions that should be explainable in a technical interview.

## 1. Positioning in one sentence

> My strongest production experience is with AWS, Python and SQL, building and supporting data pipelines in production. This portfolio uses that foundation to demonstrate architecture, incremental processing, data quality, observability and modern Data Engineering patterns across additional stacks.

## 2. Flagship: AWS Incremental Data Pipeline

### Problem to explain

A daily full-load process reprocessed a large historical dataset even when only a small portion changed. That increased runtime, cloud resource consumption, cost and failure risk.

### Core solution

Move to incremental processing so that the pipeline identifies only new or changed records, processes that slice, validates it and safely updates the target.

### Key interview concepts

#### Full load vs incremental
- Full load reprocesses the full dataset.
- Incremental processing selects only new or changed records.
- Incremental is more complex because state, change detection and recovery must be designed explicitly.

#### Watermark
A watermark stores the last successfully processed change position. It may be based on an `updated_at`, ingestion timestamp, CDC sequence or another reliable source indicator.

Important rule: **advance the watermark only after target write and validation succeed**.

#### Idempotency
Running the same logical batch twice must not generate duplicates or inconsistent results.

Typical controls:
- stable business key;
- deterministic transformations;
- deduplication;
- MERGE/upsert for mutable records;
- watermark commit only after success.

#### Partitioning
Partitioning reduces the amount of data scanned when aligned with real access patterns. It is an optimization technique, not the definition of incremental processing.

Trade-off: too many high-cardinality partitions can create many small files and metadata overhead.

#### Reprocessing
A resilient pipeline should allow one failed batch or partition to be reprocessed without rebuilding all historical data.

Explain the sequence:
1. identify failed logical batch;
2. keep or restore the previous valid watermark;
3. re-read affected source data;
4. apply deterministic transformation;
5. merge/upsert into target;
6. validate result;
7. commit new watermark.

#### Observability
Be ready to discuss:
- pipeline status;
- processing duration;
- rows read / selected / written;
- rejected rows;
- last successful watermark;
- freshness;
- retries and failures;
- processed volume;
- cost indicators.

### Production case answer

> One of the most relevant environments I worked on used daily full loads and reprocessed a large historical volume. Jobs could take around four to six hours and the architecture had unnecessary resource consumption and recurring failures. We evolved the processing model to incremental, processing only new or changed records. Comparing processing time, resource consumption and AWS cost before and after the change, we observed a reduction of around 60%.

Do not invent the exact physical table reorganization or internal implementation details that are not documented.

### Difficult questions

**How do you know a row changed?**  
Possible mechanisms include `updated_at`, CDC metadata, source sequence, ingestion timestamp or another reliable change indicator. The correct choice depends on guarantees provided by the source.

**What happens if a job fails after writing data but before updating the watermark?**  
The batch may be replayed. This is why target writes must be idempotent so rerunning the same logical batch does not corrupt the target.

**Why not always use incremental processing?**  
For small datasets, unreliable change tracking or cases where full reload cost and runtime are acceptable, a simpler full load can be the better trade-off.

**How would you handle late-arriving records?**  
Use a controlled lookback window, CDC sequence or another source-specific strategy, then deduplicate/merge based on stable key and version metadata.

## 3. AWS Redshift + DMS Modernization

### Positioning

This is a hands-on/reference project, not claimed production experience with Redshift or DMS.

### Architecture to explain

`Operational DB → DMS Full Load + CDC → S3/Staging → Transformation → Redshift → BI/Analytics`

### Concepts to defend

- full load establishes the historical baseline;
- CDC captures subsequent inserts, updates and deletes;
- DMS reduces custom replication implementation;
- S3 staging decouples ingestion from analytical transformation;
- Redshift is designed for analytical/OLAP workloads rather than transactional access;
- source and target reconciliation is required before cutover.

### Comparisons

**Aurora vs Redshift**  
Aurora is a relational operational database suited to low-latency transactional workloads. Redshift is an analytical warehouse optimized for large scans, aggregations and BI workloads.

**Athena vs Redshift**  
Athena is serverless SQL over files in S3 and is useful for ad hoc or lake-oriented access. Redshift provides a dedicated analytical execution engine and warehouse model for repeated analytical workloads and controlled performance.

**DMS vs custom pipeline**  
DMS is useful when the central problem is database migration/replication and CDC. Custom pipelines are more appropriate when complex transformations, business logic or non-database integration dominate the workload.

## 4. Databricks + PySpark Lakehouse

### Positioning

Hands-on/reference Lakehouse project. Do not present it as extensive Databricks production experience.

### Concepts to defend

**Bronze** — source-aligned/raw data with ingestion metadata.  
**Silver** — cleaned, standardized, validated and deduplicated data.  
**Gold** — business-ready analytical datasets and marts.

**Lazy evaluation**  
Spark builds a logical execution plan for transformations and executes it when an action is triggered.

**Shuffle**  
Redistribution of data across partitions/executors, commonly caused by joins, groupBy, distinct and orderBy. It can be expensive due to network, disk, serialization and memory pressure.

**Broadcast join**  
When one dataset is sufficiently small, Spark can distribute it to executors to avoid shuffling the larger dataset.

**repartition vs coalesce**  
`repartition` can increase or decrease partitions and normally causes shuffle. `coalesce` is mainly used to reduce partitions with less redistribution.

### Transferability answer

> My strongest production experience is AWS, Python and SQL. With Spark and Databricks, my hands-on experience is more recent, but the engineering problems are familiar: incremental processing, partitioning, data quality, joins, performance, reprocessing and observability.

## 5. Snowflake + dbt Analytics Engineering

### Positioning

Hands-on/reference project.

### dbt mental model

`Source / RAW → staging → intermediate → marts → analytics/BI`

### Concepts to defend

- `source()` identifies upstream source relations;
- `ref()` expresses model dependencies and supports lineage;
- staging standardizes source data;
- intermediate models hold reusable transformation logic;
- marts expose business-ready facts/dimensions;
- tests validate assumptions such as uniqueness and non-null keys;
- incremental models avoid rebuilding all transformed data;
- snapshots can track historical changes in mutable source records.

### Important distinction

> dbt is primarily a transformation, modeling, testing and documentation layer. It is not an ingestion platform or a database.

### Snowflake mental model

- storage and compute are separated;
- virtual warehouses provide compute;
- data is organized internally using micro-partitions;
- roles control access;
- Time Travel enables access to historical states within configured retention.

Avoid claiming implementation details that are not present in the repository.

## 6. Azure Data Engineering Platform

### Positioning

Reference architecture showing transferability of Data Engineering principles from AWS to Azure.

### Mapping

| Azure | AWS mental model |
|---|---|
| ADLS Gen2 | S3 |
| Azure Data Factory | Glue workflows / orchestration + connectors |
| Azure Databricks | Spark-based distributed transformation |
| Key Vault | Secrets Manager |
| Entra ID | IAM / identity concepts |
| Azure Monitor | CloudWatch |

Explain that mappings are conceptual and not one-to-one.

## 7. Questions a Senior Data Engineer should be able to answer

1. How do you make a pipeline idempotent?
2. How do you choose between full load and incremental?
3. What is a watermark and when can it safely advance?
4. How do you reprocess one failed batch?
5. How do you handle duplicate delivery?
6. How do you detect late-arriving data?
7. What metrics would you monitor in production?
8. When would you choose Athena instead of Redshift?
9. When would Aurora be a bad analytical target?
10. What causes shuffle in Spark?
11. When is a broadcast join useful?
12. Why use Bronze/Silver/Gold?
13. What does dbt solve and what does it not solve?
14. What is the difference between CDC and incremental processing?
15. How would you validate a database migration before cutover?
16. How do you optimize cloud cost without sacrificing reliability?
17. What happens if the same batch is delivered twice?
18. Where should business rules live in a data architecture?
19. What would make you reject a dataset before publication?
20. How would your architecture change if volume increased 10x?

## 8. English interview version

### Flagship project

> One of the most relevant projects I worked on involved a data platform that was reprocessing a large historical dataset every day using a full-load approach. The jobs could take around four to six hours and this created unnecessary cloud resource consumption and recurring failures. We evolved the architecture to incremental processing, so the pipeline processed only new or changed records. By comparing processing time, AWS resource consumption and cloud cost before and after the change, we observed a reduction of around 60%.

### Technology gap

> My main production experience is with AWS, Python and SQL. I haven't used this technology extensively in production, but I understand the architecture, the engineering problem it solves and the trade-offs involved, and I have been building hands-on projects to deepen that knowledge.

### Architecture explanation

> I usually start by understanding the source guarantees, data volume, latency requirements and consumption pattern. From there, I define the ingestion strategy, incremental state management, transformation layers, data quality controls, observability and reprocessing strategy before choosing the final services.

## 9. Rule for interviews

Never defend a technology by saying only that it is "better" or "faster". Explain:

**problem → requirement → option → trade-off → decision**.

That reasoning is more important for a Senior Data Engineer than memorizing service names.
