---
title: "Restart the database"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/restart-the-database.html"
content_id: "osIC_6a7Uh5olhpoD1gs2Q"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:27.130261+00:00"
---

# Restart the database

After you have either received notification that a tuning-write has completed
successfully, or you have modified the PostgreSQL settings in response to a
tuning-suggest, you must restart the database for the tuning parameters to take
effect.

Coverity Connect contains a notifier that runs every morning at 9 AM and notifies you if
you did not restart the database after tuning.

1. Bring down Coverity Connect by changing the CIM deployment replica count to
   '0'.
2. Restart the database.
3. After the database restarts, change the CIM deployment replica count to '1' to
   bring up Coverity Connect.
