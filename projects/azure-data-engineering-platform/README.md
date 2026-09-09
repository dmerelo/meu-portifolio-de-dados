# Azure Data Engineering Platform — Reference Architecture

Hands-on portfolio project focused on a modern **Azure Data Engineering** stack. The goal is to demonstrate transferable engineering decisions from AWS-based production experience into Azure services without overstating production experience.

## Scenario

A company needs to ingest operational data from APIs and relational systems, store raw data reliably, transform it into analytics-ready datasets, and expose curated data for reporting and downstream consumption.

The solution must support:

- batch and incremental ingestion
- secure secret management
- scalable storage
- distributed transformations
- data quality checks
- observability
- governed consumption

## Reference architecture

```text
Operational Sources / APIs
        |
        v
Azure Data Factory
        |
        v
ADLS Gen2 — Raw
        |
        v
Azure Databricks / PySpark
        |
        +--> Bronze
        +--> Silver
        +--> Gold
        |
        v
Analytics / BI / Data Consumers

Cross-cutting:
- Azure Key Vault
- Microsoft Entra ID
- Monitoring / logging
```

## Azure ↔ AWS mental model

| Azure | Closest AWS analogy | Purpose |
|---|---|---|
| Azure Data Factory | Glue Workflows / Step Functions + connectors | ingestion and orchestration |
| ADLS Gen2 | Amazon S3 | scalable object storage |
| Azure Databricks | Databricks on AWS / EMR-style distributed processing | Spark-based transformations |
| Azure Key Vault | AWS Secrets Manager | secrets and credentials |
| Microsoft Entra ID | IAM / identity federation concepts | identity and access control |
| Azure Monitor / Log Analytics | CloudWatch | observability |

The mapping is conceptual rather than one-to-one; each cloud has different operational patterns and service boundaries.

## Engineering principles

### Incremental ingestion

Pipelines should avoid reprocessing full historical datasets when source systems expose reliable change indicators such as:

- `updated_at`
- sequential IDs
- CDC metadata
- source watermarks

The ingestion pipeline stores its last successful watermark and requests only data newer than that point.

### Medallion layers

**Bronze**
- source-aligned data
- ingestion metadata
- minimal transformation

**Silver**
- standardized schema
- type normalization
- deduplication
- quality validation

**Gold**
- business-ready datasets
- aggregates
- dimensions / facts
- reporting models

### Security

Secrets should not be embedded in notebooks or pipeline configuration files. Credentials and connection strings should be resolved through Key Vault with identity-based access where possible.

### Observability

Monitor at least:

- pipeline success/failure
- records ingested
- processing duration
- freshness / SLA
- rejected records
- source-to-target reconciliation

## Repository contents

```text
azure-data-engineering-platform/
├── README.md
├── architecture.md
├── adf/
│   └── incremental_pipeline.json
├── databricks/
│   └── silver_transform.py
└── sql/
    └── data_quality_checks.sql
```

## Portfolio note

This is a **reference / hands-on portfolio architecture**. My strongest production experience is with AWS, Python and SQL; this project demonstrates how the same Data Engineering principles map to Azure services.
