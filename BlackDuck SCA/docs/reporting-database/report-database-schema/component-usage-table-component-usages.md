---
title: "Component Usage table (component_usages)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/component-usage-table-component_usages-.html"
content_id: "jMUUauAtI2cMg91nUKjaEg"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-10-04T23:32:26.772469+00:00"
content_hash: "714ce78cb6a7e3468165bbcb2f4a7bc34269223388905690c013e22773be6526"
---

# Component Usage table (component_usages)

| Column | Type | Description |
| --- | --- | --- |
| `component_id` | int8 | `id` field in the Component table. |
| `project_version_id` | UUID | ID. |
| `usage` | text | One of the following values:   - DYNAMICALLY_LINKED - STATICALLY_LINKED - SOURCE_CODE - DEV_TOOL_EXCLUDED - SEPARATE_WORK - IMPLEMENTATION_OF_STANDARD |
