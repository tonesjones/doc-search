---
title: "Component Comments table (component_comments)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/component-comments-table-component_comments-.html"
content_id: "2tdExf9LQ9L55lDutY0oYQ"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-08-08T15:34:34.355353+00:00"
---

# Component Comments table (component_comments)

| Column | Type | Description |
| --- | --- | --- |
| `comment` | text | Text of the comment. |
| `comment_id` | UUID | ID of the comment. |
| `component_table_id` | int8 | ID of the component in the reporting.component table containing the comment. |
| `created_at` | timestamp in UTC | When the comment was created. |
| `created_by` | UUID | User who created the comment |
| `project_id` | UUID | Project ID of the project containing the comment. |
| `project_version_id` | UUID | Project version ID of the project version where this BOM component appears in the BOM. |
| `updated_at` | timestamp in UTC | When the comment was last updated. |
