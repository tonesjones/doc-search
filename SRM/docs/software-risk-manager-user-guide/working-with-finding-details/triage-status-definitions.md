---
title: "Triage Status Definitions"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/triage-status-definitions.html"
content_id: "g6nEcQiIkTNB_9i4A7Q5Tw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:30.782162+00:00"
content_hash: "5ccd0a343249e5b2746d910b5ed6366045003cdd06e7f5d4275309dce1b075c7"
---

# Triage Status Definitions

SRM Triage Status definitions are as follows:

- **Not Triaged.** (Not yet assigned a status.) The finding has not been
  assessed or categorized.
- **Fixed.** The finding has been directly fixed in the current version of the
  software and is awaiting confirmation by a later scan which would set the
  Finding Status to "Gone."
- **Mitigated.** The vulnerability has not been fixed, but steps have been
  taken to reduce its impact or likelihood.
- **Ignored.** The vulnerability has been deemed insignificant and does not
  currently warrant action.
- **False Positive.** The reported finding is not an actual vulnerability.
  After review, it is determined to be incorrect or misleading, and no action is
  needed.
- **To Be Fixed.** The finding has been assessed and flagged as important and
  therefore needs to be fixed.
- **Reopened.** The finding has been reopened per the analysis configuration
  settings. (See Analysis Configuration Options.)
