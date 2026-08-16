---
title: "Creating a Connect Web application administator password secret"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-a-connect-web-application-administator-password-secret.html"
content_id: "kF1Mwj5E~fgU0tqPs0OLpQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:04.785184+00:00"
---

# Creating a Connect Web application administator password secret

Note: After you create this secret, you can edit it periodically to
change the password. You should need to *create* this secret only once, when you
develop the Helm chart.

As of the 2024.9.0 release, you can specify an administrator password for Connect Web
application administrators within a secret. This enables you to set the administrator
password for the Connect Web UI, and include it in a deployment install, upgrade, or
update.

To create this secret and manage Connect Web application administator passwords, refer to
Managing the Connect Web application administator password.
