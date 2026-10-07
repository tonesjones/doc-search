---
title: "Web application pod failure scenario"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/web-application-pod-failure-scenario.html"
content_id: "CpUcsVca7gSPsIUXxDPcQg"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:35.438271+00:00"
---

# Web application pod failure scenario

If a Connect Web application pod fails, any in-process work such as a
`commit` will fail and it will not retry. If the pod fails during the
commit, the commit fails. The end user who initiated the commit, for example a
developer, will receive an error message and must re-submit the
`commit`.
