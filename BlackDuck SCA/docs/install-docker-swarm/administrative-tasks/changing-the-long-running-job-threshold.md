---
title: "Changing the long running job threshold"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/changing-the-long-running-job-threshold.html"
content_id: "uG3yWbhZ~a8xaMVxDQHdug"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:25.564679+00:00"
content_hash: "580569b89db53ed4639cbbf16f49afcc238b3836a5810d0e63cfd61e024d4a6a"
---

# Changing the long running job threshold

You can configure the threshold to determine long running jobs by adding the following variable to your `blackduck-config.env` file:

- BLACKDUCK_DEFAULT_JOB_RUNTIME_THRESHOLD_HOURS={value in hours}

The default value for this environment variable is 24 hours.
