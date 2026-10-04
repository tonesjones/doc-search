---
title: "Exit codes"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/exit-codes.html"
content_id: "YTyUAHjB5lMlKbPB4BdAqg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:53.605728+00:00"
---

# Exit codes

This command returns the following exit codes:

- 0: The command successfully completed the requested task.
- 2: The command was unable to complete the requested task. This error typically
  includes an error message and some remediation advice.
- 4: An unexpected error occurred. This error should not occur when the product is
  used in a supported way. Very likely, the requested task was not completed. This
  error typically provides some diagnostic and/or debugging output, such as a
  stack trace.
