---
title: "Configuring KB license update and security update jobs"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-kb-license-update-and-security-update-jobs.html"
content_id: "q0myj~Lq39mB1UVN71iVGQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:04.272070+00:00"
---

# Configuring KB license update and security update jobs

To disable the KB license update and security update jobs, add the following property in
your `blackduck-config.env` file:

`KB_UPDATE_JOB_ENABLED=FALSE`

To change the frequency of the KB license update job, add the following property in your
`blackduck-config.env` file:

`KB_LICENSE_UPDATER_PERIOD_MINUTES=`<time in minutes>
