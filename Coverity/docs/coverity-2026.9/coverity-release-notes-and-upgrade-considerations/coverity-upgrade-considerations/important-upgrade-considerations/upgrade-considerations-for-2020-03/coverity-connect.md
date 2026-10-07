---
title: "Coverity Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/coverity-connect.html"
content_id: "vY8pTzi33hLTmF1HzWjviw"
version: "2026.9"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-10-04T23:39:49.362860+00:00"
---

# Coverity Connect

The default value for the `cim.cleanup.stream.delay.min` property
(specified in the `cim.properties` file) has changed from
`30` to `2`. If you have explicitly set this property
to a significantly higher value than `2`, and you delete large numbers of
streams, we recommend that you set it to `2`. For more information about
this property, refer to the Coverity Platform User and Administrator Guide.
