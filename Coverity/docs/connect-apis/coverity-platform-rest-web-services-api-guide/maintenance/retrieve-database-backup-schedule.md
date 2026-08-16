---
title: "Retrieve database backup schedule"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-database-backup-schedule.html"
content_id: "r4JdBtVSai4Woq487N9Qaw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:19.163272+00:00"
---

# Retrieve database backup schedule

Example GET request to retrieve the schedule for automated backup of the Coverity Connect
database.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/maintenance/backupConfiguration?locale=en_us" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "backupLocation": "C:\\Products\\Coverity\\Platform\\backups",
  "backupTime": "22:00",
  "fridayEnabled": true,
  "mondayEnabled": false,
  "saturdayEnabled": false,
  "sundayEnabled": false,
  "thursdayEnabled": false,
  "tuesdayEnabled": false,
  "wednesdayEnabled": false
}
```
