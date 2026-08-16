---
title: "Component Custom Fields table (component_custom_fields)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/component-custom-fields-table-component_custom_fields-.html"
content_id: "aIs7wA18Ezhu5tcQIJouAg"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-08-08T15:34:34.907394+00:00"
---

# Component Custom Fields table (component_custom_fields)

| Column | Type | Description |
| --- | --- | --- |
| `active` | boolean | Defines whether this custom field is active.   - "true" indicates the custom field is active. - "false" indicates the custom field is deactivated. |
| `component_id` | int8 | ID of the BOM component.  Use this column to join with other reporting.component* tables to obtain more information. |
| `custom_field_id` | integer | ID of the BOM component custom field. |
| `custom_field_label` | text | Label of this custom field. |
| `custom_field_type` | text | Type of custom field. For example, MULTISELECT or TEXT. |
| `project_version_id` | UUID | Project version ID of the project version where this BOM component appears in the BOM. |
| `values` | text[] | Data stored for this BOM component custom field for this component. |
