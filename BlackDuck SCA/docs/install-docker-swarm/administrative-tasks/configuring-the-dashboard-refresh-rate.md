---
title: "Configuring the Dashboard refresh rate"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-the-dashboard-refresh-rate.html"
content_id: "9jDfLxmNXnP421A8EBT50Q"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:43.112411+00:00"
---

# Configuring the Dashboard refresh rate

Schedule the Dashboard refresh rate by configuring the
`SEARCH_DASHBOARD_REFRESH_JOB_DUTY_CYCLE` environment variable in the
`blackduck-config.env` file.

The allowed `SEARCH_DASHBOARD_REFRESH_JOB_DUTY_CYCLE` values are as
follows:

- The default value is 20
- The minimum value is 10.
- The maximum value is 50.

Values that do not match the allowed values are reset to the nearest allowable value.

Examples:

`SEARCH_DASHBOARD_REFRESH_JOB_DUTY_CYCLE=100` The configured value is
reset to the nearest allowable value (10, 20, or 50), which is 50.

`SEARCH_DASHBOARD_REFRESH_JOB_DUTY_CYCLE=10` The configured value stays at
this allowable value, which is 10.

`SEARCH_DASHBOARD_REFRESH_JOB_DUTY_CYCLE=5` The configured value is reset
to the nearest allowable value (10, 20, or 50), which is 10.
