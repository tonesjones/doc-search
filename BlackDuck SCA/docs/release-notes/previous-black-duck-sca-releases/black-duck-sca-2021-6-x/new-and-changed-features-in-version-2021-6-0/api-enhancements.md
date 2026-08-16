---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "LCLn1FaZiUQMxa2Qy7RpFw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:11.982335+00:00"
---

# API enhancements

- (HUB-28332) With the change
  to the jobs subsystem:

  - The `GET /jobs/{jobID}` This call gets the job details
    for a specific job by ID. This call will now return a 404 Not Found
    status code.
  - The following calls are out-of-service since Black Duck version
    2020.2.0, returning a 404 Not Found status code, and will remain
    non-functional in Black Duck version 2021.6.0:
    - `PUT /jobs/{jobID}` This call reschedules a
      job.
    - `DELETE /jobs/{jobID}` This call terminates a
      job.

    The functionality will be replaced with a new Job Rest API
    implementation which will be available in a future release.

- Added new boolean field to policy view (/api/policy-rules/{policyRuleId})
  expressions ("developerScanExpression") to identify rapid scan types.
