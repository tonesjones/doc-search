---
title: "Project Version table (project_version)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/project-version-table-project_version-.html"
content_id: "akDO_SLetEUIHG60Z8R1Bw"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-08-08T15:34:40.696768+00:00"
---

# Project Version table (project_version)

| Column | Type | Description |
| --- | --- | --- |
| `created_on` | timestamp with time zone | Project version creation date. |
| `distribution` | text | Project Distribution:   - EXTERNAL - SAAS - INTERNAL - OPENSOURCE |
| `license_high_component_count` | integer | Number of component origins in this project version that have at least one high license risk. |
| `license_medium_component_count` | integer | Number of component origins in this project version that have at least one medium license risk. |
| `license_low_component_count` | integer | Number of component origins in this project version that have at least one low license risk. |
| `license_ok_component_count` | integer | Number of component origins in this project version that have no license risk. |
| `nickname` | text | Nickname for the project version. |
| `notes` | text | Notes about this version of the project. |
| `operational_high_component_count` | integer | Number of component origins in this project version that have at least one high operational risk. |
| `operational_medium_component_count` | integer | Number of component origins in this project version that have at least one medium operational risk. |
| `operational_low_component_count` | integer | Number of components in this project version that have at least one low operational risk. |
| `operational_ok_component_count` | integer | Number of components in this project version that have no operational risk. |
| `phase` | text | Project phase:   - PLANNING - DEVELOPMENT - PRERELEASE - RELEASED - DEPRECATED - ARCHIVED |
| `project_id` | UUID | Project ID. |
| `released_on` | timestamp with time zone | Project release date. |
| `security_critical_component_count` | integer | Number of component origins in this project version that have at least one critical security risk. |
| `security_high_component_count` | integer | Number of component origins in this project version that have at least one high security risk. |
| `security_medium_component_count` | integer | Number of component origins in this project version that have at least one medium security risk. |
| `security_low_component_count` | integer | Number of component origins in this project version that have at least one low security risk. |
| `security_ok_component_count` | integer | Number of component origins in this project version that have no security risk. |
| `updated_at` | timestamp with time zone | When the project version was last updated. |
| `version_id` | UUID | Project version ID. |
| `version_name` | text | Project version name. |
