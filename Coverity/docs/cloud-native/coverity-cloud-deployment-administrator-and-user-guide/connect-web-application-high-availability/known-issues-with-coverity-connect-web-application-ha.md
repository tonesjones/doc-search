---
title: "Known issues with Coverity Connect Web application HA"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/known-issues-with-coverity-connect-web-application-ha.html"
content_id: "3UsXF7BIngP2FFRGAmwTHQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:29.679185+00:00"
---

# Known issues with Coverity Connect Web application HA

Coverity Connect Web application HA currently has the following known issues:

- Initial Commits are slower with 2 or more replicas because there is greater cache
  overhead which causes initial commits to be slower.
- Some Commits, especially for large projects, run more slowly if the second run
  hits an alternate Web application instance because the cache needs to be
  repopulated.
