# Data Engineering Portfolio — Douglas Merelo

Portfolio focused on **Data Engineering, AWS, Python, SQL, ETL/ELT, data pipelines, performance and cloud architecture**.

This repository is organized to demonstrate how I approach real Data Engineering problems: ingestion, transformation, incremental processing, data quality, observability, modeling, performance, security and cost optimization.

> My strongest production experience is with **AWS, Python and SQL**. Projects involving technologies such as Spark, Databricks, Snowflake, dbt and Azure are identified as hands-on/reference labs when applicable.

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

## Production-inspired flagship project

### AWS Incremental Data Pipeline

This is the main project in the portfolio because it is the closest to the type of problem I have handled in production: evolving a costly full-load pattern into a more efficient incremental architecture.

It focuses on the engineering decisions behind:
- watermark strategy
- idempotency
- partitioning
- upsert / merge logic
- data quality
- observability
- predictable reprocessing
- performance and cost optimization

[View flagship project](./projects/aws-incremental-data-pipeline/)

## AWS-focused hands-on project

### AWS Redshift + DMS Modernization

Hands-on/reference project focused on analytical migration and replication patterns that extend naturally from my AWS background.

Covers:
- DMS full load + CDC
- OLTP to OLAP separation
- Redshift-oriented analytical modeling
- migration validation
- data quality
- cutover and rollback thinking

[View project](./projects/aws-redshift-dms-modernization/)

## Hands-on labs

The projects below are designed to deepen practical knowledge in modern Data Engineering stacks. They are portfolio labs and are not presented as prior production experience.

### Databricks + PySpark Lakehouse

Hands-on Lakehouse lab using Spark and Medallion architecture concepts.

Covers:
- Bronze / Silver / Gold
- PySpark transformations
- deduplication
- incremental processing
- MERGE / upsert
- Spark performance
- data quality
- automated tests and CI

[View lab](./projects/databricks-pyspark-lakehouse/)

### Snowflake + dbt Analytics Engineering

Hands-on lab for modern analytical transformation and modeling.

Covers:
- Snowflake data layers
- dbt sources and models
- staging / intermediate / marts
- tests
- snapshots
- incremental models
- lineage-oriented project structure

[View lab](./projects/snowflake-dbt-analytics-engineering/)

### Azure Data Engineering Platform

Hands-on architecture lab mapping core Data Engineering principles to Azure.

Covers:
- Azure Data Factory
- ADLS Gen2
- Azure Databricks / PySpark
- incremental ingestion
- Medallion layers
- Key Vault
- Entra ID concepts
- observability and data quality
- Azure ↔ AWS architectural analogies

[View lab](./projects/azure-data-engineering-platform/)

## Supporting code

### Python Data Transformation

Existing Python transformation code for CSV data preparation using pandas and logging.

[View source](./src/data_processing/tratar_fonte.py)

## Engineering principles demonstrated

- Process only what changed when possible
- Design pipelines to be idempotent
- Separate ingestion, transformation and consumption responsibilities
- Make reprocessing predictable
- Optimize data layout before scaling compute
- Monitor failures, latency, data freshness and processing volume
- Treat cost as an architectural metric
- Prefer explicit data contracts and quality checks
- Apply least privilege and avoid hard-coded credentials
- Document trade-offs instead of treating tools as interchangeable

## Current technical roadmap

I am deepening hands-on knowledge in:

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
