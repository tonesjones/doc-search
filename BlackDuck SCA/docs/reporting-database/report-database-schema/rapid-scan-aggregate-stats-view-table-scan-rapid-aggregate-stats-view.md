---
title: "Rapid Scan aggregate stats view table (scan_rapid_aggregate_stats_view)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/rapid-scan-aggregate-stats-view-table-scan_rapid_aggregate_stats_view-.html"
content_id: "YeFt1behovNUEoK0vaztqA"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-08-08T15:34:42.493869+00:00"
---

# Rapid Scan aggregate stats view table (scan_rapid_aggregate_stats_view)

| Column | Type | Description |
| --- | --- | --- |
| `avg_duration_ms` | numeric | The average duration in milliseconds over the sample time period. |
| `avg_num_components` | numeric | The average number of identified components. |
| `avg_num_components_with_policy_bloc` | numeric | The average number of identified components with blocker severity policy rule violations. |
| `avg_num_components_with_policy_crit` | numeric | The average number of identified components with critical severity policy rule violations. |
| `avg_num_components_with_policy_major` | numeric | The average number of identified components with major severity policy rule violations. |
| `avg_num_components_with_policy_minor` | numeric | The average number of identified components with minor severity policy rule violations. |
| `avg_num_components_with_policy_triv` | numeric | The average number of identified components with trivial severity policy rule violations. |
| `avg_num_components_with_policy_unsp` | numeric | The average number of identified components with unspecified severity policy rule violations. |
| `avg_num_components_with_vuln_crit` | numeric | The average number of identified components with critical severity vulnerabilities. |
| `avg_num_components_with_vuln_high` | numeric | The average number of identified components with high severity vulnerabilities. |
| `avg_num_components_with_vuln_low` | numeric | The average number of identified components with low severity vulnerabilities. |
| `avg_num_components_with_vuln_med` | numeric | The average number of identified components with medium severity vulnerabilities. |
| `avg_num_components_with_vuln_none` | numeric | The average number of identified components with none severity vulnerabilities. |
| `avg_num_licenses_internal_prop` | numeric | The average number of identified licenses with internal proprietary license families. |
| `avg_num_licenses_permissive` | numeric | The average number of identified licenses with permissive license families. |
| `avg_num_licenses_reciprocal` | numeric | The average number of identified licenses with reciprocal license families. |
| `avg_num_licenses_reciprocal_agpl` | numeric | The average number of identified licenses with reciprocal AGPL license families. |
| `avg_num_licenses_restricted_prop` | numeric | The average number of identified licenses with restricted proprietary license families. |
| `avg_num_licenses_unknown` | numeric | The average number of identified licenses with unknown license families. |
| `avg_num_licenses_weak_reciprocal` | numeric | The average number of identified licenses with weak reciprocal license families. |
| `avg_num_policies_by_blocker` | numeric | The average number of blocker severity policy rule violations. |
| `avg_num_policies_by_crit` | numeric | The average number of critical severity policy rule violations. |
| `avg_num_policies_by_major` | numeric | The average number of major severity policy rule violations. |
| `avg_num_policies_by_minor` | numeric | The average number of minor severity policy rule violations. |
| `avg_num_policies_by_trivial` | numeric | The average number of trivial severity policy rule violations. |
| `avg_num_policies_by_unspecified` | numeric | The average number of unspecified severity policy rule violations. |
| `avg_num_scans_per_project` | numeric | The average number of scans per project. |
| `avg_num_scans_per_user` | numeric | The average number of scans per user. |
| `avg_num_scans_per_version` | numeric | The average number of scans per project version. |
| `avg_num_vuln_count_by_critical` | numeric | The average number of critical severity vulnerabilities. |
| `avg_num_vuln_count_by_high` | numeric | The average number of high severity vulnerabilities. |
| `avg_num_vuln_count_by_low` | numeric | The average number of low severity vulnerabilities. |
| `avg_num_vuln_count_by_med` | numeric | The average number of medium severity vulnerabilities. |
| `avg_num_vuln_count_by_none` | numeric | The average number of none severity vulnerabilities. |
| `distinct_projects` | int4 | The count of unique projects. |
| `distinct_users` | int4 | The count of unique users. |
| `distinct_versions` | int4 | The count of unique project versions. |
| `end_time` | timestamp with time zone | The ending timestamp of this sample time period. |
| `iqr_duration_ms` | int4 | The interquartile range of scan times over the sample time period. |
| `max_duration_ms` | int4 | The maximum duration in milliseconds over the sample time period. |
| `max_num_components` | int4 | The maximum number of identified components. |
| `min_duration_ms` | int4 | The minimum duration in milliseconds over the sample time period. |
| `sample_time` | timestamp with time zone | The beginning timestamp of this sample time period. |
| `stddev_duration_ms` | numeric | The standard deviation duration in milliseconds over the sample time period. |
| `total_components` | int4 | The total number of components. |
| `total_components_with_pol_viol` | int4 | The total number of components with policy rule violations. |
| `total_noproject_scans` | int4 | The total number of scans without a project. |
| `total_noversion_scans` | int4 | The total number of scans without a project version. |
| `total_num_scans` | int4 | The total number of scans over the sample time period. |
| `total_q1_scans` | int4 | The total number of scans considered ‘short scans’. |
| `total_q4_scans` | int4 | The total number of scans considered ‘long scans’. |
