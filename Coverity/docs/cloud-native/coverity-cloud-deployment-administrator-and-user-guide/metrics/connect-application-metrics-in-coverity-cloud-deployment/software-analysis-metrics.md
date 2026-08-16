---
title: "Software analysis metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/software-analysis-metrics.html"
content_id: "Olt9cs2_TUJ_Mxi~XFVOXQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:14.070973+00:00"
---

# Software analysis metrics

The following table describes a number of software analysis metrics.

Table 1. Software analysis metrics

| Metric | Description | Metric type | Examples: PromQL queries |
| --- | --- | --- | --- |
| `no_of_​componentmaps` | **Number of component maps**  This metric is a gauge that tracks the number of component maps in Connect.  This metric presents the same component maps value that you can find in the Coverity Connect UI, on the Help > System Diagnostics > Overview page, under System Totals. See Connect UI System Totals list. | Gauge | `no_of_componentmaps` |
| `no_of_custom_​roles` | **Number of custom user roles**  This metric is a gauge that tracks the number of custom user roles in Connect. | Gauge | no_of_custom_roles |
| `no_of_projects` | **Number of projects**  This metric is a gauge that tracks the number of projects in Connect.  This metric presents the same number of projects value that you can find in the Coverity Connect UI, on the Help > System Diagnostics > Overview page, under System Totals. See Connect UI System Totals list. | Gauge | no_of_projects |
| `no_of_streams` | **Number of streams**  This metric is a gauge that tracks the number of streams in Connect.  This metric presents the same number of streams value that you can find in the Coverity Connect UI, on the Help > System Diagnostics > Overview page, under System Totals. See Connect UI System Totals list. | Gauge | `no_of_streams` |
| `no_of_​triagestores` | **Number of triage stores**  `no_of_triagestores​` is a gauge that tracks the number of triage stores in Connect.  This metric presents the same value that you can find in the Coverity Connect UI, on the Help > System Diagnostics > Overview page, under System Totals. See Connect UI System Totals list. | Gauge | `no_of_triagestores` |
| `no_of_​usergroups` | **Number of user groups**  This​ metric is a gauge that tracks the number of user groups in Connect.  This metric presents the same number of user groups value that you can find in the Coverity Connect UI, on the Help > System Diagnostics > Overview page, under System Totals. See Connect UI System Totals list. | Gauge | no_of_usergroup |
| `no_of_users` | **Number of users**  This metric is a gauge that tracks the number of users in Connect.  This metric presents the same number of users value that you can find in the Coverity Connect UI, on the Help > System Diagnostics > Overview page, under System Totals. See Connect UI System Totals list. | Gauge | `no_of_users` |
