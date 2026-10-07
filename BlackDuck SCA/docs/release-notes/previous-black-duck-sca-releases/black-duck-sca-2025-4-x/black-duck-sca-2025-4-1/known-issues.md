---
title: "Known issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/known-issues.html"
content_id: "AnUwy6b8psLy3mRg21jgzA"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:29.223653+00:00"
content_hash: "c14092e2c274953e354ac50efa9aeda74f82b195c0513229d23d69380642888b"
---

# Known issues

The following is a list of new known issues and limitations in Black Duck SCA:

- In some cases, remediation statuses that initially appear correctly may become out of sync after several days. This issue is believed to be related to automated remediation workflows and affects only certain vulnerabilities. The issue is under investigation.
- In rare cases, a vulnerability's ignored status may not align with its remediation state. Specifically, some vulnerabilities may appear as ignored even when their status is shown as New or Remediation Required. This issue primarily affects older vulnerabilities and is currently under investigation.
