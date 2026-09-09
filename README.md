# Data Engineering Portfolio — Douglas Merelo

[![CI](https://github.com/dmerelo/meu-portifolio-de-dados/actions/workflows/ci.yml/badge.svg)](https://github.com/dmerelo/meu-portifolio-de-dados/actions/workflows/ci.yml)

Portfolio focused on **Data Engineering, AWS, Python, SQL, ETL/ELT, data pipelines, performance and cloud architecture**.

My strongest production experience is with **AWS, Python and SQL**. Projects involving Spark, Databricks, Snowflake, dbt and Azure are clearly identified as hands-on/reference labs rather than previous production experience.

## Selected professional impact

- Contributed to the evolution of a national-scale telecom data platform from daily **full-load processing to incremental processing**.
- Reduced reprocessing, execution time, AWS resource consumption and cloud cost by approximately **60%**.
- Supported and evolved approximately **20 production data pipelines** in a critical environment processing millions of records.

> Proprietary code, datasets and internal architecture are not exposed. Public examples are sanitized or recreated as reference architectures.

## Project map

| Project | Stack / Concepts | What it demonstrates |
|---|---|---|
| [AWS Incremental Data Pipeline](./projects/aws-incremental-data-pipeline/) | AWS, Python, SQL, incremental, watermark, idempotency | **Flagship** — architecture, reprocessing, data quality, observability, performance and cloud cost |
| [AWS Redshift + DMS Modernization](./projects/aws-redshift-dms-modernization/) | Redshift, DMS, CDC, S3, SQL | Full load + CDC, OLTP → OLAP separation, migration validation and cutover thinking |
| [Databricks + PySpark Lakehouse](./projects/databricks-pyspark-lakehouse/) | PySpark, Delta concepts, Medallion | Bronze/Silver/Gold, deduplication, incremental processing, Spark performance and CI |
| [Snowflake + dbt Analytics Engineering](./projects/snowflake-dbt-analytics-engineering/) | Snowflake, dbt, SQL | Staging/intermediate/marts, tests, snapshots, incremental models and lineage-oriented structure |
| [Azure Data Engineering Platform](./projects/azure-data-engineering-platform/) | ADF, ADLS Gen2, Databricks, Key Vault | Transfer of core Data Engineering principles from AWS to Azure |

## Production-inspired flagship

### AWS Incremental Data Pipeline

The flagship is the closest public representation of the type of problem I have handled in production: evolving an expensive full-load pattern into a more efficient incremental architecture.

It includes:
- synthetic reproducible dataset;
- executable Python incremental pipeline;
- watermark lifecycle;
- idempotent merge/upsert behavior;
- automated tests;
- before-vs-after design analysis;
- operational runbook;
- failure and reprocessing strategy;
- architecture and trade-off documentation.

[Open the flagship project](./projects/aws-incremental-data-pipeline/)

## Core production stack

**AWS:** S3, Glue, Athena, Lambda, Aurora PostgreSQL, DynamoDB, ECS, EC2, API Gateway, EventBridge, CloudWatch, IAM, Secrets Manager  
**Languages:** Python, SQL, Shell Script  
**Databases:** PostgreSQL, Aurora PostgreSQL, Oracle, SQL Server, MySQL, DynamoDB  
**Engineering:** ETL/ELT, Data Pipelines, Data Modeling, REST APIs, Docker, Git, CI/CD, monitoring and troubleshooting

## Engineering principles

- Process only what changed when possible
- Design pipelines to be idempotent
- Separate ingestion, transformation and consumption responsibilities
- Make reprocessing predictable
- Validate data before publication
- Monitor failures, latency, freshness and processing volume
- Optimize data layout before scaling compute
- Treat cost as an architectural metric
- Apply least privilege and avoid hard-coded credentials
- Document trade-offs instead of treating tools as interchangeable

## Interview preparation

I keep a technical defense guide for the portfolio with the concepts, trade-offs and questions I should be able to explain in an interview.

[Open the interview defense guide](./docs/interview-defense-guide.md)

## Hands-on expansion

Current practical study focuses on:

`Advanced SQL` · `Redshift` · `AWS DMS / CDC` · `Spark / PySpark` · `Databricks / Delta Lake` · `Snowflake` · `dbt` · `Azure Data Engineering`

## Supporting / historical work

- [Python CSV Transformation](./src/data_processing/tratar_fonte.py)
- [Jupyter study archive](https://github.com/dmerelo/Project_Jupyter_Notebooks)
- [Portfolio website](https://dmerelo.github.io/)

## About

**Douglas Merelo**  
Senior Data Engineer | AWS | Python | SQL | ETL/ELT | Data Pipelines | Cloud Architecture

- [LinkedIn](https://www.linkedin.com/in/douglas-merelo/)
- [GitHub](https://github.com/dmerelo)
