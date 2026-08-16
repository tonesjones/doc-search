---
title: "Exit codes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/exit-codes.html"
content_id: "Mqmkqmjf5KoY6DRHmxXq3w"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:44.836948+00:00"
---

# Exit codes

Most Coverity Analysis commands can return the following exit codes:

- 0: The command successfully completed the requested task.
- 1: The requested task is complete, but it did not return (or find) any results.
  Note that some Coverity Analysis commands do not return this error code.
- 2: The command was unable to complete the requested task. This error typically
  includes an error message and some remediation advice.
- 4: An unexpected error occurred. This error should not occur when the product is
  used in a supported way. Very likely, the requested task was not completed. This
  error typically provides some diagnostic and/or debugging output, such as a
  stack trace.

For exceptions, see cov-commit-defects, cov-analyze, and cov-build.
