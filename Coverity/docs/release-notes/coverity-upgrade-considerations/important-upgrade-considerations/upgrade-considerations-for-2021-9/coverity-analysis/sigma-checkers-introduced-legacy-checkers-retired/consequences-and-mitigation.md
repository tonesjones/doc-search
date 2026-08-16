---
title: "Consequences and mitigation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/consequences-and-mitigation.html"
content_id: "KJuIHxeHcjgsXWt4AntCPg"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:22.980871+00:00"
---

# Consequences and mitigation

The following list discusses possible consequences of the Sigma checker-related changes
and possible mitigation strategies:

- Running a 2021.9 analysis using an existing 2021.6 Coverity Connect stream creates and adds
  Sigma-checker issues to a new snapshot in the stream. The new issues will have
  different CIDs than any of the existing issues. Coverity will attempt to match the
  new issues with equivalent existing issues and migrate the triage data. In some
  cases, however, this triage-data migration might not be successful. In such cases,
  you must manually triage the Sigma-checker issues.

  As an aid in identifying
  equivalent issues when you have concerns that triage data was not successfully
  migrated, you can perform a Snapshot Comparison in Coverity Connect between your
  first 2021.9 analysis run and the preceding snapshot. For information on this
  topic, see the "Snapshot
  comparison" section in the Coverity Platform 2026.6.0 User and Administrator Guide.
- For Swift-related information on consequences and mitigation, see Changes to Swift code analysis.
