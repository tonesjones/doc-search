---
title: "Configuring KB license update and security update jobs"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-kb-license-update-and-security-update-jobs.html"
content_id: "ZQF5Y9bm6y30PfEMFJA5bg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:25.306046+00:00"
content_hash: "547788c597d51c4c3184865093c88238fc1c6db6d919b6afb2fb79886180b3db"
---

# Configuring KB license update and security update jobs

To disable the KB license update and security update jobs, add the following property in your `blackduck-config.env` file:

`KB_UPDATE_JOB_ENABLED=FALSE`

To change the frequency of the KB license update job, add the following property in your `blackduck-config.env` file:

`KB_LICENSE_UPDATER_PERIOD_MINUTES=`<time in minutes>
