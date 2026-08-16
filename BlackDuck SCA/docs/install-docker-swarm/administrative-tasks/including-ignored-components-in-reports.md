---
title: "Including ignored components in reports"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/including-ignored-components-in-reports.html"
content_id: "RPnuv_Lfuf95QjVuoGjtcw"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:45.933124+00:00"
---

# Including ignored components in reports

By default, ignored components and vulnerabilities associated with those ignored
components are excluded from the Vulnerability Status report, Vulnerability Update
report, Vulnerability Remediation report and the Project Version report. To include
ignored components, set the value of the BLACKDUCK_REPORT_IGNORED_COMPONENTS environment
variable in the `blackduck-config.env` file in the
`docker-swarm` directory to "true".

Resetting the value of the BLACKDUCK_REPORT_IGNORED_COMPONENTS to "false" excludes
ignored components.
