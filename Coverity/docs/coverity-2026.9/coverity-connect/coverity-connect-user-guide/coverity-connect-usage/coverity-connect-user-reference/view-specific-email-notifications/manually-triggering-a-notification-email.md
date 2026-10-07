---
title: "Manually triggering a notification Email"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/manually-triggering-a-notification-email.html"
content_id: "UUnsKtE1h88f1XjjJn3Mkw"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:00.914766+00:00"
---

# Manually triggering a notification Email

It is possible to manually trigger a notification using the
`cov-manage-im` command in `notification` mode. To
trigger the notification, enter the following command, where `viewName`
is the name of the Coverity Connect view for which you want to send a notification:

```
cov-manage-im --mode notification --execute --view viewName
```

For more information on `cov-manage-im`, see the Coverity Command Reference.
