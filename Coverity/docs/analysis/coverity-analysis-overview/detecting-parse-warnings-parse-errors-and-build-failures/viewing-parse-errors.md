---
title: "Viewing parse errors"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/viewing-parse-errors.html"
content_id: "31PF2b_0HKjTzdrbm6muDg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:01.580772+00:00"
---

# Viewing parse errors

You can see parse errors in the build-log.txt log file, and through
Coverity Connect.

The build-log.txt file is the log of the
`cov-build` command. It is in
<intermediate_directory>/build-log.txt. The
build-log.txt file contains other error messages in addition to
parse errors, so finding the parse errors can be difficult.

**To view parse errors in Coverity Connect:**

1. Run the `cov-build` (or `cov-translate`) command.
2. Run the `cov-analyze` command with the `--enable PARSE_ERROR`
   option to include parse errors in the analysis.
3. Commit the defects to the Coverity Connect database with the
   `cov-commit-defects` command.
4. Log in to Coverity Connect and look for defects named PARSE_ERROR.

   You can view these
   errors in the source code that caused the error, and the specific error
   message.

If the compiler is able to recover from a parse error, it is identified as a recovery warning,
not a parse error. Recovery warnings have the prefix RW. For more information, see "PW.*, RW.*, SW.*: Compilation
warnings" in the Coverity 2026.6.0 Checker Reference.
