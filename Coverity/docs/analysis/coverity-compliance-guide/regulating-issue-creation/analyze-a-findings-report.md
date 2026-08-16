---
title: "Analyze a findings report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/analyze-a-findings-report.html"
content_id: "3_RcsB2sJMdmyGtOlpJ9_Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:44.262073+00:00"
---

# Analyze a findings report

After generating your initial findings report, you should analyze it and decide on the
filtering policies you want to put in place. The findings report is distributed across
the tabs of the spreadsheet as follows:

- Filtering Report tab – Each row represents a filtering
  policy. These are the columns:

  - Path – The policy's Path Pattern.
  - Compliance – The policy's Compliance Pattern.
  - Score – The score assigned to findings that match
    the policy. This column pertains only to scoring policies.
  - Matched Findings – Number of findings that match
    the filtering policy's patterns. Both the Path Pattern and Compliance
    Pattern must match for the policy to match. An unspecified pattern
    matches all findings.

- Directory Distribution Report tab – Each row correlates
  several categories of findings to a path. These are the columns:

  - Path – Indicates either a file or a directory
    within the source code file system and, if a directory, all files and
    directories (recursively) below it. The Path is relative to the root of
    the stream on which the report was run.
  - Total Findings – Number of findings in the
    indicated Path. This count includes all categories of findings and is
    not restricted to findings related to a coding-standard.
  - Included findings – Number of findings in the
    indicated Path that will be persisted as issues. This count is the sum
    of scored findings that meet the threshold and unmatched findings.
  - Excluded findings – Number of findings in the
    indicated Path that will *not* be persisted as issues. This count
    is the sum of blocked and scored sub-threshold findings.

- Standards Distribution Report tab – Each row correlates
  several categories of findings to a coding-standard rule or directive. These are
  the columns:

  - Compliance – Indicates a coding-standard rule (or
    directive).
  - Total Findings – Number of findings that violate
    the indicated rule.
  - Included findings – Number of findings violating
    the indicated rule that will be persisted as issues.
  - Excluded findings – Number of findings that
    violate the indicated rule that will *not* be persisted as issues.
