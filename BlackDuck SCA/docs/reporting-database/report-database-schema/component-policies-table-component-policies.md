---
title: "Component Policies table (component_policies)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/component-policies-table-component_policies-.html"
content_id: "wF~rQy7Unz0VJ2POlFnzxQ"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-10-04T23:32:26.750200+00:00"
content_hash: "63c492a42f9fc069a7746d4614c5c05d2faa2d73db4e1f4efa7b10aaeedccc10"
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
