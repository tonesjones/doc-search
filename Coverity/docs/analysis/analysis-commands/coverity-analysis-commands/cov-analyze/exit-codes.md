---
title: "Exit codes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/exit-codes.html"
content_id: "TULHoCq4dtwmeYp5zZo5QQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:45.404835+00:00"
---

# Exit codes

- 0: The analysis was successful. Results should be considered usable and are ready
  to be committed with `cov-commit-defects`.
- 2: The command was unable to complete the requested task. This error typically
  includes an error message and some remediation advice.
- 4: An unexpected error occurred. This error should not occur when the product is
  used in a supported way. Very likely, the requested task was not completed. This
  error typically provides some diagnostic and/or debugging output, such as a
  stack trace.

Although the console output can provide diagnostics and warnings that might help to
improve the analysis configuration, or suggest reporting "recoverable errors" to
Coverity support, this information is auxiliary to the exit code. Users and scripts
should rely on the exit code when determining whether to proceed in consuming the
analysis results.
