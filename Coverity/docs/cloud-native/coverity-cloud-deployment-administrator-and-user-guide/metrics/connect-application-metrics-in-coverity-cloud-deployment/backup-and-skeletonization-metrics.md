---
title: "Backup and skeletonization metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/backup-and-skeletonization-metrics.html"
content_id: "mj1mV4bWOyGFZOJijNaIhg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:12.012353+00:00"
---

# Backup and skeletonization metrics

The following table describes backup and skeletonization metrics.

Table 1. Backup and skeletonization metrics

| Metric | Description | Metric type | Examples: PromQL queries |
| --- | --- | --- | --- |
| `connect_is_​backup_​in_progress` | **Is backup in progress**  This metric (connect_is_​backup_​in_progress) is a boolean gauge that tracks if there is a backup in progress.  A boolean gauge that indicates if a backup is in progress. | Boolean gauge | `connect_is_backup_​in_progress​{kubernetes_namespace=~"$namespace"}` This metric example presents metrics for a specified namespace in a Kubernetes deployment. You might create a Grafana variable in the Grafana dashboard to select and view the metric for one of multiple `namespace` instances. |
| **Interpreting the metric**  Knowing if there is currently a backup in progress can help provide insight into a possible reason for the system not functioning as expected. If backups are impacting the normal operation of the server, then they should be rescheduled for different times. | | |
| `connect_is_​skeletonization_​in_progress` | **Is skeletonization in progress** This metric is a boolean gauge that tracks if there is a background cleanup and garbage collection in progress. | Boolean gauge | `connect_is_​skeletonization​_in_progress​{kubernetes_namespace=~"$namespace"}` This metric example presents metrics for a specified namespace in a Kubernetes deployment. You might create a Grafana variable in the Grafana dashboard to select and view the metric for one of multiple `namespace` instances. |
| **Interpreting the metric**  Knowing if there is currently a skeletonization/cleanup in progress can help provide insight into a possible reason for the system not functioning as expected. If skeletonization/cleanup is impacting the normal operation of the server, then they should be rescheduled for different times. | | |
