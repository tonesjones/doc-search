---
title: "Scan stats view table (scan_stats_view)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/scan-stats-view-table-scan_stats_view-.html"
content_id: "hNMnD30Xstr4nlQ8wZv5Og"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-08-08T15:34:43.056627+00:00"
---

# Scan stats view table (scan_stats_view)

| Column | Type | Description |
| --- | --- | --- |
| `application_id` | text | The external application id that is associated to the mapped project. |
| `code_location_id` | UUID | The code location ID. |
| `code_location_name` | text | The code location name. |
| `parent_project_group_id` | UUID | The parent project group ID to which the scan is associated. |
| `project_group_id` | UUID | The project group ID to which the scan is associated. |
| `project_group_name` | text | The project group name to which the scan is associated. |
| `project_id` | UUID | The project ID to which the scan is associated. |
| `project_name` | text | The project name to which the scan is associated. |
| `scan_age` | interval | The age since the scan was created. |
| `scan_archived_at` | timestamp | The timestamp at which the scan was archived. |
| `scan_duration` | interval | The scan duration. |
| `scan_end_at` | timestamp with time zone | The timestamp at which the scan ended. |
| `scan_id` | UUID | The scan ID. |
| `scan_name` | text | The scan name. |
| `scan_size` | int8 | The file system size in bytes of inspected uncompressed files in the scan. |
| `scan_start_at` | timestamp with time zone | The timestamp at which the scan started. |
| `scan_status` | varchar | The transition reason for the scan. |
| `scan_type` | text | The scan type. |
| `uploaded_at` | timestamp with time zone | The timestamp at which the scan data was uploaded from the client. |
| `user_id` | UUID | The user ID. |
| `version_id` | UUID | The project version ID to which the scan is associated. |
| `version_name` | text | The project version name to which to the scan is associated. |
