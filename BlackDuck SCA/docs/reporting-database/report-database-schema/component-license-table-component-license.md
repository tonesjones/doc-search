---
title: "Component License table (component_license)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/component-license-table-component_license-.html"
content_id: "nFk4cI3ClnokMw17BHpV9w"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-10-04T23:32:26.674047+00:00"
content_hash: "7ddac111bb3cc9954027dac37875b32b2da11ada6b4b54f4c0bf4642a0693722"
---

# Component License table (component_license)

| Column | Type | Description |
| --- | --- | --- |
| `component_table_id` | int8 | `id` field in the Component table. |
| `id` | int8 | ID. |
| `license_display` | text | License name when it is a single license; license display when it is a complex license. For example, (License A OR license B). |
| `license_family_name` | text | License family this license belongs to for purposes of risk calculations and the definition of open source policy rules. |
| `project_version_id` | UUID | Project version ID. |
