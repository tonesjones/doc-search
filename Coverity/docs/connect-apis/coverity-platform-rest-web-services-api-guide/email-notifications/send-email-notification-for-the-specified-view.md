---
title: "Send email notification for the specified view"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/send-email-notification-for-the-specified-view.html"
content_id: "pKwh__iVpCX14szqeUwZgw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:50.548918+00:00"
---

# Send email notification for the specified view

Example POST request to send email notification for the **Outstanding Issues**
view.

**cURL request**

```
curl --location --request POST "http://my_connect_host:8080/api/v2/\
emailNotifications/view/Outstanding%20Issues?locale=zh_cn" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
```
