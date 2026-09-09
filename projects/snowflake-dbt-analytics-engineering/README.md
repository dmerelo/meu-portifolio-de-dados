# Snowflake + dbt Analytics Engineering

Reference project focused on modern analytics engineering with Snowflake and dbt.

> Portfolio project for hands-on study. It is not presented as production experience.

## Goals

- Model analytical data in Snowflake
- Apply layered transformations with dbt
- Create reusable, testable and documented models
- Demonstrate incremental models, snapshots and data quality checks
- Show clear separation between ingestion, transformation and consumption

## Architecture

```text
Source Data
   |
   v
Snowflake RAW
   |
   v
dbt STAGING
   |
   v
dbt INTERMEDIATE
   |
   v
dbt MARTS
   |
   v
Analytics / BI
```

## dbt layers

### staging
- standardization
- casting
- renaming
- source-level cleanup

### intermediate
- joins
- business transformations
- reusable logic

### marts
- business-ready facts and dimensions
- stable consumption layer

## Engineering concerns covered

- incremental processing
- idempotency
- tests
- lineage
- documentation
- snapshots
- CI
- model organization
- cost awareness

## Repository structure

```text
models/
  staging/
  intermediate/
  marts/
snapshots/
tests/
macros/
dbt_project.yml
packages.yml
```

## Snowflake concepts demonstrated

- databases and schemas
- virtual warehouses
- separation of storage and compute
- micro-partition awareness
- COPY INTO concept
- role-based access concepts
- time travel concepts

## dbt concepts demonstrated

- source()
- ref()
- tests
- incremental materialization
- snapshots
- macros
- documentation
- lineage

## Why this project matters

This project demonstrates the shift from pipeline-centric Data Engineering to analytics engineering, where transformation logic becomes modular, versioned, tested and easier to maintain.

## Portfolio context

This is a hands-on lab for Snowflake and dbt. My main production-inspired portfolio case remains the **[AWS Incremental Data Pipeline flagship](../aws-incremental-data-pipeline/)**, which demonstrates the underlying engineering principles in greater depth: incremental processing, idempotency, watermarking, testing, observability and controlled reprocessing.
