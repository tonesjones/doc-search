---
title: "User group project mapping table (user_group_project_mapping)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/user-group-project-mapping-table-user_group_project_mapping-.html"
content_id: "LYG_mI3~Dtt2ZuwgWv2S3Q"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-10-04T23:32:27.099106+00:00"
content_hash: "e2e1d3bf8e42f24f3c0e5af0c7c534a322cc3be8b787a9fa99d481347bc21bd1"
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
