---
title: "Exit status"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/exit-status.html"
content_id: "CAQKhSdQSdgVRNC_nl33IQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:33.991302+00:00"
---

# Exit status

Coverity Fortran Syntax Analysis exits with a specified exit status which can be tested
in command files.

- 0 - Success
- 2 - User Error
- 4 - Internal Error

User errors indicate that there was a problem with the command-line syntax, a file was
missing or some other error in configuring and running the tool. An internal error
indicates that `cov-run-fortran` encountered an error in processing and
aborted. Internal errors should be reported to Coverity Support.
