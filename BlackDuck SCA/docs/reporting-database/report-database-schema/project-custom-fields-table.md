---
title: "Project Custom Fields table"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/project-custom-fields-table.html"
content_id: "EqqDq_TXBapJpiWSkLE5ug"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-10-04T23:32:26.853421+00:00"
content_hash: "90a10f519966819407eb63cf8b1d6353fff3ce9a1a76e139ae5d920ec81721fa"
---

# Project Custom Fields table

| Column | Type | Description |
| --- | --- | --- |
| `active` | boolean | Defines whether this custom field is active.   - "true" indicates the custom field is active. - "false" indicates the custom field is deactivated. |
| `custom_field_id` | integer | ID of the project custom field. |
| `custom_field_label` | text | Label of this custom field. |
| `custom_field_type` | text | Type of this custom field. For example, MULTISELECT or TEXT. |
| `project_id` | UUID | UUID of the project where this project custom field appears. |
| `values` | text[] | Data stored for this project custom field for this project. |
