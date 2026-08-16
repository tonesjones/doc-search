---
title: "Scan view table (scan_view)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/scan-view-table-scan_view-.html"
content_id: "Wxd8DnN9qgfEAanifsE37A"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-08-08T15:34:43.703905+00:00"
---

# Scan view table (scan_view)

| Column | Type | Description |
| --- | --- | --- |
| `application_id` | text | The external application id that is associated to the mapped project. |
| `archive_initiated_by` | UUID | The user that archived the scan. |
| `archived_at` | timestamp | The timestamp at which the scan was archived. |
| `basedir` | text | The base directory path under which the scan occurred (signature scans). |
| `code_location_id` | UUID | The code location ID. |
| `code_location_name` | text | The code location name. |
| `created_by_user_id` | UUID | The user ID of the user that created the scan. |
| `file_system_size` | int8 | The file system size in bytes of inspected uncompressed files in the scan. |
| `host_name` | varchar | The host name under which the scan occurred (signature scans). |
| `match_count` | int4 | The number of identified matches from the scan. |
| `name` | text | The scan name. |
| `num_dirs` | int4 | The number of directories inspected within the scan. |
| `num_non_dir_files` | int4 | The number of non-directory files inspected within the scan. |
| `project_id` | UUID | The project ID to which the scan is associated. |
| `project_name` | text | The project name to which the scan is associated. |
| `scan_end_at` | timestamp with time zone | The timestamp at which the scan ended. |
| `scan_id` | UUID | The scan ID. |
| `scan_source_id` | text | The internal scan source ID. |
| `scan_source_type` | varchar | The internal scan source type. |
| `scan_start_at` | timestamp with time zone | The timestamp at which the scan started. |
| `scantime` | int8 | The timestamp at which the scan occurred (millis since epoch). |
| `server_version` | varchar | The Black Duck server version under which this scan occurred. |
| `status` | varchar | The transition reason for the scan. |
| `status_message` | text | The message associated with the scan's transition reason. |
| `timelastmodified` | int8 | The timestamp at which the scan was last modified (millis since epoch). |
| `type` | text | The scan type. |
| `uploaded_at` | timestamp with time zone | The timestamp at which the scan data was uploaded from the client. |
| `version_id` | UUID | The project version id to which the scan is associated. |
| `version_name` | text | The project version name to which the scan is associated. |
