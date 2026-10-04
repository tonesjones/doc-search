---
title: "Environment variables for analysis configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/environment-variables-for-analysis-configuration.html"
content_id: "ru2X2TQwRMwBaDo_ly4Wcw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:25.044939+00:00"
---

# Environment variables for analysis configuration

When you incorporate Coverity into a CI/CD pipeline, you can set values
for the following environment variables. This lets you avoid hard-coding user names and
passwords into the script.

`COVERITY_PASSPHRASE`
:   Sets the Coverity Connect password if the --password (-pa) option does not do so.

`COV_USER`
:   Sets the Coverity Connect user name if the --url or --user option does not do so.

See the Coverity Analysis User and Administrator Guide for more detailed information.
