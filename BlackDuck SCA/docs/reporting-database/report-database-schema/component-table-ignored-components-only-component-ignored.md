---
title: "Component table (Ignored components only) (component_ignored)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/component-table-ignored-components-only-component_ignored-.html"
content_id: "i7VIktBBmtbTkomR3KRnHA"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-08-08T15:34:33.779512+00:00"
---

# Component table (Ignored components only) (component_ignored)

| Column | Type | Description |
| --- | --- | --- |
| `component_id` | UUID | Component ID. |
| `component_type` | text | The type of component.  Possible values [PROJECT, COMPONENT, AI_MODEL] |
| `component_name` | text | Component name. |
| `component_version_id` | UUID | Component version ID. |
| `component_version_name` | text | Component version name. |
| `id` | int8 | ID. |
| `ignored` | boolean | Indicates whether the component is ignored:   - "t" indicates that the component is ignored. - "f" indicates that the component is not ignored. |
| `license_high_count` | numeric | Number of high license risk. |
| `license_medium_count` | numeric | Number of medium license risk. |
| `license_low_count` | numeric | Number of low license risk. |
| `license_ok_count` | numeric | Number of no license risk. |
| `operational_high_count` | numeric | Number of high operational risk. |
| `operational_medium_count` | numeric | Number of medium operation risk. |
| `operational_low_count` | numeric | Number of low operational risk. |
| `operational_ok_count` | numeric | Number of no operational risk. |
| `origin_id` | text | Origin ID.  Note that origin ID is blank if the component does not have a distribution. |
| `origin_name` | text | Name of the distribution (origin). |
| `policy_approval_status` | text | One of the following values:   - IN_VIOLATION - NOT_IN_VIOLATION - IN_VIOLATION_OVERRIDDEN |
| `project_version_id` | UUID | Project version ID. |
| `review_status` | text | Review status of the component. Possible values are:  - UNREVIEWED - IN_REVIEW - REVIEWED - APPROVED - LIMITED_APPROVAL - REJECTED - DEPRECATED |
| `reviewed_by` | UUID | User who reviewed the component. |
| `reviewed_on` | timestamp in UTC | When the component was reviewed. |
| `security_critical_count` | numeric | Number of critical security vulnerabilities. |
| `security_high_count` | numeric | Number of high security vulnerabilities. |
| `security_medium_count` | numeric | Number of medium security vulnerabilities. |
| `security_low_count` | numeric | Number of low security vulnerabilities. |
| `security_ok_count` | numeric | Number of no security vulnerabilities. |
| `version_origin_id` | UUID | Version origin ID. |
