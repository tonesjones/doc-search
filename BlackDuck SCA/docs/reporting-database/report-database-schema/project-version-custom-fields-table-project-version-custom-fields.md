---
title: "Project Version Custom Fields table (project_version_custom_fields)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/project-version-custom-fields-table-project_version_custom_fields-.html"
content_id: "K_P19lyDoRZRDbw5RW1NQw"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-10-04T23:32:26.952971+00:00"
content_hash: "0f610d964075aac6b0a33167fe682983a3ec256e514d1f73f609515710ab4f53"
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
