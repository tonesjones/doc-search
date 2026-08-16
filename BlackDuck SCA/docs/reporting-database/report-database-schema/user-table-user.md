---
title: "User table (user)"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/user-table-user-.html"
content_id: "NndicSIiIMiG1I2uY1oshA"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-08-08T15:34:44.248944+00:00"
---

# User table (user)

| Column | Type | Description |
| --- | --- | --- |
| `active` | boolean | Defines whether this user is active.   - "true" indicates this user is active. - "false" indicates this user is inactive. |
| `email` | text | User's email address. |
| `first_name` | text | User's first name. |
| `id` | UUID | ID. |
| `last_login` | timestamp with timezone | Time that the user last logged in to Black Duck. |
| `last_name` | text | User's last name. |
| `username` | text | User's username in Black Duck. |
