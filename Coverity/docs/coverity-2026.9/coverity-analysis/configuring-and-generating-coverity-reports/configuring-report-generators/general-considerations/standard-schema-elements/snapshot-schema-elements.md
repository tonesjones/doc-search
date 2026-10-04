---
title: "Snapshot schema elements"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/snapshot-schema-elements.html"
content_id: "uxhd7jXYSvOwf2yWxPRCfg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:40.118924+00:00"
---

# Snapshot schema elements

Elements for snapshot-id and snapshot-date are described below. If both keys are defined,
`snapshot-id` will get the highest priority.

| Key | Class Type | Description | Default | Required? |
| --- | --- | --- | --- | --- |
| `snapshot-id` | Long | Retrieves the defects of a specific snapshot id, instead of using the latest snapshot id of all the streams associated with the project. | N/A | No |
| `snapshot-date` | String using the format MM/DD/YYY | Retrieves the most recent snapshot of each stream in the project whose date is less than or equal to the given date. | N/A | No |
