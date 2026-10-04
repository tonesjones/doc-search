---
title: "Including ignored components in reports"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/including-ignored-components-in-reports.html"
content_id: "4lIqQBbhi08XBMM_50QAqg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:24.529206+00:00"
content_hash: "a7e6f594dd7bf43751565452788b5c27b8ef693527037f2ed94b9d113e34f05e"
---

# Including ignored components in reports

By default, ignored components and vulnerabilities associated with those ignored components are excluded from the Vulnerability Status report, Vulnerability Update report, Vulnerability Remediation report and the Project Version report. To include ignored components, set the value of the BLACKDUCK_REPORT_IGNORED_COMPONENTS environment variable in the `blackduck-config.env` file in the `docker-swarm` directory to "true".

Resetting the value of the BLACKDUCK_REPORT_IGNORED_COMPONENTS to "false" excludes ignored components.
