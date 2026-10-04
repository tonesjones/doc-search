---
title: "Component Match Type table (component_match_types)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/component-match-type-table-component_match_types-.html"
content_id: "e_ew_cSmwU8pevGl1hGtmQ"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-10-04T23:32:26.698134+00:00"
content_hash: "db361d3a0f3ae6ef1cf56b460648f49446f2d8a9fc16b11dd83ecc4cb473459d"
---

# Component Match Type table (component_match_types)

| Column | Type | Description |
| --- | --- | --- |
| `component_id` | int8 | `id` field in the Component table. |
| `match_type` | text | One of the following values:   - BINARY - FILE_FILES_ADDED_DELETED_AND_MODIFIED - FILE_DEPENDENCY - FILE_DEPENDENCY_DIRECT - FILE_DEPENDENCY_TRANSITIVE - FILE_EXACT - FILE_EXACT_FILE_MATCH - FILE_SOME_FILES_MODIFIED - MANUAL_BOM_COMPONENT - MANUAL_BOM_FILE - PARTIAL_FILE - SBOM - SNIPPET |
| `project_version_id` | UUID | Project version ID. |
