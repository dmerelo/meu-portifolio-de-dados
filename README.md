# Data Engineering Portfolio — Douglas Merelo

Portfolio focused on **Data Engineering, AWS, Python, SQL, ETL/ELT, data pipelines, performance and cloud architecture**.

This repository is organized to demonstrate how I approach real Data Engineering problems: ingestion, transformation, incremental processing, data quality, observability, modeling, performance, security and cost optimization.

> My strongest production experience is with **AWS, Python and SQL**. Projects involving technologies such as Spark, Databricks, Snowflake, dbt and Azure are identified as study/lab/reference projects when applicable.

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

## Featured projects

### 1. AWS Incremental Data Pipeline

Reference architecture focused on moving from daily full-load processing to an incremental model.

Covers:
- watermark strategy
- idempotency
- partitioning
- upsert / merge
- data quality
- observability
- reprocessing
- performance and cost

[View project](./projects/aws-incremental-data-pipeline/)

### 2. AWS Redshift + DMS Modernization

Hands-on/reference project focused on analytical migration and replication patterns.

Covers:
- DMS full load + CDC
- OLTP to OLAP separation
- Redshift-oriented analytical modeling
- migration validation
- data quality
- cutover and rollback thinking

[View project](./projects/aws-redshift-dms-modernization/)

### 3. Databricks + PySpark Lakehouse

Hands-on/reference Lakehouse project using Spark and Medallion architecture concepts.

Covers:
- Bronze / Silver / Gold
- PySpark transformations
- deduplication
- incremental processing
- MERGE / upsert
- Spark performance
- data quality
- automated tests and CI

[View project](./projects/databricks-pyspark-lakehouse/)

### 4. Snowflake + dbt Analytics Engineering

Hands-on/reference project for modern analytical transformation and modeling.

Covers:
- Snowflake data layers
- dbt sources and models
- staging / intermediate / marts
- tests
- snapshots
- incremental models
- lineage-oriented project structure

[View project](./projects/snowflake-dbt-analytics-engineering/)

### 5. Azure Data Engineering Platform

Hands-on/reference architecture mapping core Data Engineering principles to Azure.

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

[View project](./projects/azure-data-engineering-platform/)

### 6. Python Data Transformation

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
