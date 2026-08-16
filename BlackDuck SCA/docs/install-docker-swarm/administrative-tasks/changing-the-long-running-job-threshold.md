---
title: "Changing the long running job threshold"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/changing-the-long-running-job-threshold.html"
content_id: "AWcQi3mL85rAMT7_aWjoqQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:10.438881+00:00"
---

# Changing the long running job threshold

You can configure the threshold to determine long running jobs by adding the following
variable to your `blackduck-config.env` file:

- BLACKDUCK_DEFAULT_JOB_RUNTIME_THRESHOLD_HOURS={value in hours}

The default value for this environment variable is 24 hours.
