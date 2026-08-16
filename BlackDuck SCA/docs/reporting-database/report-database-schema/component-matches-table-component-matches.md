---
title: "Component Matches table (component_matches)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/component-matches-table-component_matches-.html"
content_id: "WD5ujpK2sL2GPtzJFsUskw"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-08-08T15:34:36.585602+00:00"
---

# Component Matches table (component_matches)

| Column | Type | Description |
| --- | --- | --- |
| `component_table_id` | int8 | `id` field in the Component table. |
| `match_archive_context` | text | Local path to the archived file relative to the project’s root directory. |
| `match_confidence` | numeric | Represents the confidence in the match, excluding, snippet, binary, or partial file matches.  For manually added components and components added via package manager scans, the value is always 100%.  Components found via signature scans are the only components that have a confidence value between 0.00 (no confidence) and 100.00 (confident). |
| `match_file_name` | text | File name |
| `match_id` | int8 | Match ID. |
| `match_path` | text | Path. |
| `match_type` | text | One of the following values:   - BINARY - FILE_FILES_ADDED_DELETED_AND_MODIFIED - FILE_DEPENDENCY - FILE_DEPENDENCY_DIRECT - FILE_DEPENDENCY_TRANSITIVE - FILE_EXACT - FILE_EXACT_FILE_MATCH - FILE_SOME_FILES_MODIFIED - MANUAL_BOM_COMPONENT - MANUAL_BOM_FILE - PARTIAL_FILE - SNIPPET |
| `project_version_id` | UUID | Project version ID. |
| `snippet_confirmation_status` | text | Review status of the snippet matches. Possible values are:   - Reviewed - Not Reviewed - Null   Note that snippet matches that have not been reviewed will not appear in the reporting database. |
