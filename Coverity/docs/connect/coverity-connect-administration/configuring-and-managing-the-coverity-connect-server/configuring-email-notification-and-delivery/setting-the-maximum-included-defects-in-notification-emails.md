---
title: "Setting the maximum included defects in notification Emails"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-the-maximum-included-defects-in-notification-emails.html"
content_id: "62ce05qIR6zXlD8oaul9Nw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:58.347824+00:00"
---

# Setting the maximum included defects in notification Emails

By default, notification emails triggered by Coverity Connect include a maximum of 100
defects. To update the maximum number of included defects, add the
`notification.maximum.rows` property to the
cim.properties file, with a value equal to the new maximum.

For example, if you wanted to include a maximum of 50 defects in notification emails, you
would add the following line to cim.properties:
`notification.maximum.rows=50`
