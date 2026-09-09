# Data Engineering Portfolio — Douglas Merelo

Portfolio focused on **Data Engineering, AWS, Python, SQL, ETL/ELT, data pipelines, performance and cloud architecture**.

This repository is being organized to demonstrate how I approach real Data Engineering problems: ingestion, transformation, incremental processing, data quality, observability, modeling, performance and cost optimization.

> My strongest production experience is with **AWS, Python and SQL**. Projects involving technologies such as Spark, Databricks, Snowflake and dbt are identified as study/lab projects when applicable.

## Professional focus

- Data Engineering on AWS
- ETL/ELT and data pipelines
- Incremental processing and reprocessing strategies
- SQL performance and data modeling
- Data integration and APIs
- Production troubleshooting and observability
- Cloud cost and processing optimization

## Core stack

**Cloud:** AWS S3, Glue, Athena, Lambda, Aurora PostgreSQL, DynamoDB, ECS, EC2, API Gateway, EventBridge, CloudWatch, IAM, Secrets Manager  
**Languages:** Python, SQL, Shell Script  
**Databases:** PostgreSQL, Aurora PostgreSQL, Oracle, SQL Server, MySQL, DynamoDB  
**Engineering:** Git, Docker, CI/CD, REST APIs, Data Modeling, ETL/ELT  
**Analytics:** Amazon QuickSight

## Selected professional impact

In a national-scale telecom data environment, I contributed to the evolution of a daily **full-load architecture to incremental processing**.

The previous approach reprocessed a large historical volume every day, resulting in long-running jobs and unnecessary cloud resource usage. The evolution to incremental processing reduced reprocessing, execution time and AWS resource consumption, with an observed reduction of approximately **60%** when comparing processing time, resource consumption and cloud cost before and after the change.

The environment included approximately **20 production data pipelines** and processed millions of records.

> The portfolio does not expose proprietary code, datasets or internal architecture. Public examples are sanitized or recreated as reference architectures.

## Projects

### 1. AWS Incremental Data Pipeline — Reference Architecture

A sanitized portfolio project that demonstrates the engineering principles behind moving from full-load processing to an incremental architecture.

Topics covered:
- Raw / processed / curated layers
- Incremental ingestion
- Watermark strategy
- Idempotent processing
- Partitioning
- Upsert / merge logic
- Data quality checks
- Observability
- Reprocessing strategy
- Cost and performance considerations

[View project](./projects/aws-incremental-data-pipeline/)

### 2. Python Data Transformation

Existing Python transformation code for CSV data preparation using pandas and logging.

[View source](./src/data_processing/tratar_fonte.py)

## Repository structure

```text
.
├── projects/
│   └── aws-incremental-data-pipeline/
│       ├── README.md
│       ├── architecture.md
│       └── sql/
│           └── incremental_upsert.sql
├── src/
│   └── data_processing/
│       └── tratar_fonte.py
├── dashboards/
└── README.md
```

## Engineering principles demonstrated

- Process only what changed when possible
- Design pipelines to be idempotent
- Separate ingestion, transformation and consumption responsibilities
- Make reprocessing predictable
- Optimize data layout before scaling compute
- Monitor failures, latency, data freshness and processing volume
- Treat cost as an architectural metric
- Prefer explicit data contracts and quality checks

## Current technical roadmap

I am currently deepening hands-on knowledge in:

- Advanced SQL and database tuning
- Amazon Redshift
- AWS DMS and CDC
- Spark / PySpark
- Databricks / Delta Lake / Medallion Architecture
- Snowflake
- dbt
- Azure Data Engineering

## About me

**Douglas Merelo**  
Senior Data Engineer | AWS | Python | SQL | ETL/ELT | Data Pipelines | Cloud Architecture

- LinkedIn: https://www.linkedin.com/in/douglas-merelo/
- GitHub: https://github.com/dmerelo
