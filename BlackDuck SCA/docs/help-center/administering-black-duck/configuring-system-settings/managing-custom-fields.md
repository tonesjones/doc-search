---
title: "Managing custom fields"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-custom-fields.html"
content_id: "yKNFCR44ZVsNUP8MW4PK1Q"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:01.021643+00:00"
---

# Managing custom fields

A custom field is a system-wide property that will apply to all BOM components, components,
component versions, projects, or project versions which provides a way to include
additional information to help you manage open source software in your company or
organize large projects. For example, to help you organize your development teams, you
may want your projects to include the responsible business unit.

Users with the Custom Fields Administrator role
can:

- Create,
  edit, or delete custom
  fields.
- Activate or deactivate a custom
  field. By default, a custom field is inactive and not shown to users.
- Determine the
  order of the custom fields as shown in the UI.

## Recommended vs required custom fields

You can determine the enforcement of required custom fields as they can be mandatory or not
mandatory. By default, if you select that a custom field is recommended, it is not
mandatory: users can still view and save non-custom field information and
information for non-required custom fields on the page if data is not entered for
the required custom field.

When **Force Entry of Required Custom Fields** is enabled, users *must* enter
values when editing objects which have required custom fields.

To enable **Force Entry of Required Custom Fields**:

1. Log into Black Duck as a system administrator user.
2. Click [image: Admin button] → **System Settings**.
3. Click the **Custom Fields** tab.
4. Switch the **Force Entry of Required Custom Fields** toggle to
   **Enabled**.

When enabled, a red asterisk (*) will appear next to the custom field label on the related
page's **Settings** tab, indicating it is a required custom field.

Note the following:

- Use the "Missing Custom Field Data" filter in the BOM to view those components in the
  project version BOM which are missing information.
- A custom field option is available for the Project
  Version report. Selecting this option lists the project version
  custom field labels and values.
- You can create a policy rule for project or BOM component custom fields for any
  field type.
