---
title: "User group project mapping table (user_group_project_mapping)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/user-group-project-mapping-table-user_group_project_mapping-.html"
content_id: "mk8P~YBaUFDLqKF9VMmXIA"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-08-08T15:34:44.842255+00:00"
---

# User group project mapping table (user_group_project_mapping)

| Column | Type | Description |
| --- | --- | --- |
| `group_id` | UUID | The user group ID. |
| `group_name` | text | The user group name. |
| `project_id` | UUID | The project ID to which this user group is mapped. |
| `project_name` | text | The project name to which this user group is mapped. |
| `user_id` | UUID | The user ID that is a member of this user group. |
| `user_name` | text | The user name of the user ID above. |
