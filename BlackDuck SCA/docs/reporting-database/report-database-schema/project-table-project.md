---
title: "Project table (project)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/project-table-project-.html"
content_id: "R6JsPeiMBuyJ44QQmq4FtQ"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-08-08T15:34:38.937018+00:00"
---

# Project table (project)

| Column | Type | Description |
| --- | --- | --- |
| `created_at` | timestamp with time zone | Project creation date. |
| `description` | text | Project description. |
| `owner` | UUID | User ID in Black Duck. |
| `project_id` | UUID | Project ID |
| `project_name` | text | Project name. |
| `tier` | smallint | Project tier. A value between 0 - 5. |
