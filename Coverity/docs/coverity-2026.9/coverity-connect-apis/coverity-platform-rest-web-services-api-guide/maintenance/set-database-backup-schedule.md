---
title: "Set database backup schedule"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/set-database-backup-schedule.html"
content_id: "oUFDvzx3V4myEbuwgebgAg"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:06.856894+00:00"
---

# Set database backup schedule

Example PUT request to configure the schedule for automated backup of the Coverity
Connect database.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/maintenance/backupConfiguration" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "backupLocation":"C:\\Products\\Coverity\\backups",
  "backupTime":"04:00",
  "fridayEnabled":false,
  "mondayEnabled":false,
  "saturdayEnabled":false,
  "sundayEnabled":true,
  "thursdayEnabled":false,
  "tuesdayEnabled":false,
  "wednesdayEnabled":false
}'
```
