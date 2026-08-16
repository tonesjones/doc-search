---
title: "Setting up component subscription notification"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-component-subscription-notification.html"
content_id: "083Aw0J_45SKSlV0I86myw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:57.750143+00:00"
---

# Setting up component subscription notification

In order to allow Coverity Connect to send issue notification based on user component
subscription, you must create an external Coverity Connect Web Services script that runs
periodically (for example, nightly), executes the appropriate query for users and their
component assignments, and then invokes the notification API to send out a message in a
predetermined format, such as HTML.

To ensure that notification will work, you should be aware of the following in your Web
Services implementation:

- The usernames of all users that subscribe to the component are available in
  the subscribers element in the componentDataObj type
  for Configuration Web Services.
- The notify() method in the Administration Web Services
  works.

For more information, see the Coverity Platform 2026.6.0 SOAP Web Services API Reference and the Coverity Platform 2026.6.0 REST Web Services API Guide.
