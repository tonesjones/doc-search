---
title: "Determining when to deploy PostgreSQL database read replicas"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/determining-when-to-deploy-postgresql-database-read-replicas.html"
content_id: "Kavd1s4OOKDX4CkTWM1wmQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:10.082456+00:00"
---

# Determining when to deploy PostgreSQL database read replicas

This section provides commit throughput test results for environments with and without
database read replicas and at varying loads of database read requests.

The following table compares commit throughput for initial commits in deployments with
and without database read replicas, and with a number of view loading (database reads)
request rates. The commit throughput is in commits/hour. This table provides rough
guidance; actual results will vary. These tests were performed using view loads that
range from 'No view loads' to '320 view loads.' The following table shows the difference
in commit throughput in a deployment with no database replicas vs a deployment with two
database replicas. It indicates that commit performance is significantly better with two
database replicas and view loads >= 40. This table shows the benefits afforded by
database read replcas in environments with significant view loads.

Table 1. Load balancing initial commit throughput (commits/hour)

| Instance | No view loads | 40 view loads | 80 view loads | 120 view loads | 160 view loads | 240 view loads | 320 view loads |
| --- | --- | --- | --- | --- | --- | --- | --- |
| no DB replica | 547 | 372 | 292 | 230 | 203 | 150 | 106 |
| 2 DB replicas | 535 | 503 | 512 | 532 | 504 | 413 | 345 |

The following chart provides similar data, however it provides tested commit throughput
results in commits/hour for subsequent commits.

Table 2. Load balancing subsequent commit throughput (commits/hour)

| Instance | No view loads | 40 view loads | 80 view loads |
| --- | --- | --- | --- |
| no DB replica | 715 | 486 | 385 |
| 2 DB replicas | 755 | 586 | 556 |

As read load rises, using database read replicas improves performance of both reads from
the replica databases and writes to the primary database. Especially when commit traffic
is high, reads are distributed to database replicas, leaving the primary database free
to handle the commits. If you are experiencing high read and write loads and slowness
during peak times, using read replicas can significantly improve performance. If high
primary database load is purely from commits, database read replicas will not help.

The following section provides a formula to help you determine when you might deploy
database read replicas.

## Using metrics to plan database read replicas

This section provides some guidance to help you determine when it is appropriate to
deploy database read replicas.

You can use the following formula to help determine whether or not to configure
database read replicas. Consider enabling database read replicas if:

```
total_db_cpu_usage
```

is greater than the estimated maximum read load that can be handled:

```
1 - (connect_commit_executor_size * num_webapp_ha_replicas) / total_db_cpu_usage
```

If the database CPU usage from read loads is greater than the estimated maximum read
load that can be handled, then use database read replicas.

For example, if the total database CPU usage is 75% (.75), and the maximum read load
that can be handled is .71 as calculated in the following example, then you should
consider enabling database read replicas:

```
1 - (.5 * 1) / .7 = .71
```

The following table identifies the metrics and values used in the formula.

Table 3. CPU metrics to determine when to deploy database read replicas

| Platform | Formula element | Metric or Value | See |
| --- | --- | --- | --- |
| AWS | `total_db_cpu_usage` | Amazon RDS metric: `CPUUtilization` | [Amazon CloudWatch instance-level metrics for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-metrics.html) |
| GCP | Google Cloud SQL metric: `database/cpu/utilization` | [Cloud SQL metrics](https://cloud.google.com/sql/docs/mysql/admin-api/metrics) |
| Azure | Microsoft Azure SQL metric: `cpu_percent` | [Monitor Azure SQL Database with metrics and alerts](https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-metrics-alerts?view=azuresql) |
| CNC | `connect_commit_executor_size` | `connect_commit_executor_size` | Commit metrics |
| `num_webapp_ha_replicas` | Value: The number of Web application high availability (HA) replicas. | Connect Web application high availability |
