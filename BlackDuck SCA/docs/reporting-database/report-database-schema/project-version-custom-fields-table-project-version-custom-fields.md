---
title: "Project Version Custom Fields table (project_version_custom_fields)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/project-version-custom-fields-table-project_version_custom_fields-.html"
content_id: "rYgaT5OqwzNx5y3MauzULQ"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-08-08T15:34:41.836887+00:00"
---

# Project Version Custom Fields table (project_version_custom_fields)

| Column | Type | Description |
| --- | --- | --- |
| `active` | boolean | Defines whether this custom field is active.   - "true" indicates the custom field is active. - "false" indicates the custom field is deactivated. |
| `custom_field_id` | integer | ID of the custom field. |
| `custom_field_label` | text | Label of this custom field. |
| `custom_field_type` | text | Type of custom field. For example, MULTISELECT or TEXT. |
| `project_version_id` | UUID | UUID of the project version where this custom field appears. |
| `values` | text | Data stored for this project version custom field for this project. |
