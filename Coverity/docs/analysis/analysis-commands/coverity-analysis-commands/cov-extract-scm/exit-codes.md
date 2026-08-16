---
title: "Exit codes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/exit-codes.html"
content_id: "Io71cZ19fyEofNTG6ul5jA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:45.904920+00:00"
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
- 8: This exit code is specific to `cov-extract-scm`. It signifies
  either that the command attempted to extract a file that does not exist in the
  SCM, or that there may have been an unknown error.

For exceptions, see cov-commit-defects, cov-analyze, and cov-build.
