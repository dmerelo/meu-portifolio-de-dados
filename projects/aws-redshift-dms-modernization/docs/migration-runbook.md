# Migration Runbook — Full Load + CDC

## 1. Discovery
- Inventory source schemas, tables, primary keys and data volumes.
- Identify unsupported data types and transformation requirements.
- Establish RPO/RTO and acceptable cutover window.

## 2. Connectivity and security
- Configure source and target endpoints.
- Validate network routes/security groups.
- Store credentials securely and apply least privilege.

## 3. Baseline migration
- Execute initial full load.
- Monitor throughput, task errors and rejected records.
- Reconcile source and target row counts.

## 4. Enable CDC
- Start change capture from the agreed log position.
- Monitor replication latency and backlog.
- Validate inserts, updates and deletes.

## 5. Analytical transformation
- Land replicated data in staging.
- Apply transformations and model analytical tables.
- Execute data quality checks before publishing.

## 6. Cutover
- Confirm CDC lag is within the agreed threshold.
- Pause or control source writes if required.
- Apply final changes.
- Validate critical business totals and freshness.
- Redirect downstream consumers.

## 7. Post-cutover
- Monitor errors, latency and query performance.
- Keep rollback procedures available for the agreed stabilization window.
- Document reconciliation results and operational ownership.
