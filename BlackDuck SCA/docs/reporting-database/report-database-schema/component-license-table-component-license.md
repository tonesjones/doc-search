---
title: "Component License table (component_license)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/component-license-table-component_license-.html"
content_id: "ILhgxoeRUmJT7WJrN83wAA"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-08-08T15:34:35.463615+00:00"
---

# Component License table (component_license)

| Column | Type | Description |
| --- | --- | --- |
| `component_table_id` | int8 | `id` field in the Component table. |
| `id` | int8 | ID. |
| `license_display` | text | License name when it is a single license; license display when it is a complex license. For example, (License A OR license B). |
| `license_family_name` | text | License family this license belongs to for purposes of risk calculations and the definition of open source policy rules. |
| `project_version_id` | UUID | Project version ID. |
