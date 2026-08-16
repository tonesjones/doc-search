---
title: "Database metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/database-metrics.html"
content_id: "lgcCU546FKM4~vOpMQZ67A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:10.017455+00:00"
---

# Database metrics

The following table describes database metrics.

Table 1. Database metrics

| Metric | Description | Metric type | Examples: PromQL queries |
| --- | --- | --- | --- |
| `active_db_​connections` | Track the number of active database connections. | Gauge | `active_db_connections` |
| `db_size` | **Database size**  This metric is a gauge the shows the current database size in bytes.  This metric presents the same database size value that you can find in the Coverity Connect UI, on the Help > System Diagnostics > Overview page, under System Totals. See Connect UI System Totals list. | Gauge | `db_size` Note: See an example of the `db_size` metrics, presented in Grafana, in Coverity Connect metrics example. |
| **Interpreting the metric**  This is a way to monitor the database size and if it is growing at a higher-than-expected rate. It can also be used to see quickly see the results of database cleanup, auto-vacuuming, tuning and XREF migration. To dig deeper see the Table Sizes metric. | | |
| `max_db_​connections` | Track the maximum number of database connections. | Gauge | `max_db_connections` |
| `table_size` | **Table sizes**  This metric is a gauge that lists the sizes of the 18 (configurable default) largest tables. You can change the number of tables listed using the Connect (cim) property: `connect.metrics.​table.​data.​collection.​limit` property.  Table size metrics are published daily at 1 AM by default. This schedule can be changed using the Connect (cim) property: `connect.metrics.​table.​data.​collection.​schedule` This metric presents the same table size values that you can find in the Coverity Connect UI, on the Help > System Diagnostics > Database page, with Table Sizes selected in the Query dropdown. | Gauge | `sum by (tablename) (table_size)` The `table_size` PromQL is derived from the `table_size` metric with the `tablename` label.  Note: See an example of the Table sizes metrics, presented in Grafana, in Coverity Connect metrics example. |
| **Interpreting the metric**  This is a way to monitor the database size of the largest tables to further pinpoint which databases are growing the most. | | |
