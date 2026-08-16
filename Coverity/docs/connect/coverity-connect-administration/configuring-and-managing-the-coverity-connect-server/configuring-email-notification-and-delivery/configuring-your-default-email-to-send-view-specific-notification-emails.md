---
title: "Configuring your default Email to send view-specific notification Emails"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-your-default-email-to-send-view-specific-notification-emails.html"
content_id: "6RJfKs4J_k4~6j0vmfG7~A"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:00.782354+00:00"
---

# Configuring your default Email to send view-specific notification Emails

If you receive an access denied error message while sending a notification
email, you may need to configure your email configuration settings. You also need to
modify your cim.properties file.

To fix this error message, perform the following steps:

1. Navigate to the right-hand menu in Coverity Connect and click Configuration > System > Email Configuration.
2. Update your cim.properties file (via the command line) with
   the following
   setting:

   ```
   notify.using.configured.from.address.only=true
   ```
