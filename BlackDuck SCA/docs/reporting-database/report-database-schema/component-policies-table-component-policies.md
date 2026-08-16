---
title: "Component Policies table (component_policies)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/component-policies-table-component_policies-.html"
content_id: "yi50UVt0eljsobpM0A~3dg"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-08-08T15:34:37.141387+00:00"
---

# Component Policies table (component_policies)

| Column | Type | Description |
| --- | --- | --- |
| `category` | text | Policy Category information. Current values are:   - COMPONENT - LICENSE - OPERATIONAL - SECURITY - UNCATEGORIZED |
| `component_table_id` | int8 | `ID` field in the Component table. |
| `description` | text | Policy description. |
| `overridden_at` | timestamp with time zone | When the policy was overridden. |
| `overridden_by` | UUID | User who overrode the policy. |
| `override_comment` | text[] | Notes about this version of the project. |
| `policy_id` | UUID | Policy ID. |
| `policy_name` | text | Name of the policy. |
| `policy_status` | text | Status of the policy. |
| `project_version_id` | UUID | Project version ID. |
| `severity` | text | Severity level of the policy. Possible values are:   - BLOCKER - CRITICAL - MAJOR - MINOR - TRIVIAL |
