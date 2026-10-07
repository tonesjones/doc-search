---
title: "Project table (project)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/project-table-project-.html"
content_id: "JdAzZ7X6CG6TdWwUjm825Q"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-10-04T23:32:26.830551+00:00"
content_hash: "244c802a177edcfa38f399b9683c3b92050a44e303229167abdefd7077d601a2"
---

# Project table (project)

| Column | Type | Description |
| --- | --- | --- |
| `created_at` | timestamp with time zone | Project creation date. |
| `description` | text | Project description. |
| `owner` | UUID | User ID in Black Duck. |
| `project_id` | UUID | Project ID |
| `project_name` | text | Project name. |
| `tier` | smallint | Project tier. A value between 0 - 5. |
