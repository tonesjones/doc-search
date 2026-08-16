---
title: "Coverity Connect exit codes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-exit-codes.html"
content_id: "Dg4WLuZFEEBxD~tcdL2YVg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:49.690654+00:00"
---

# Coverity Connect exit codes

Most Coverity Connect commands use a uniform set of exit codes.

The exception is cov-archive, which uses only two exit codes.

The uniform codes are as follows:

0
:   `SUCCESS:` The command completed successfully.

1
:   `ITEM_NOT_FOUND_ERROR:` For example, the command could not find a project/streamtriage store.

2
:   `EXPECTED_ERROR:` For example, the command could not find a file, or was given an unknown option.

4
:   `UNEXPECTED_ERROR:` This error should not occur when the product is used in a supported way.
    Very likely, the requested task was not completed.

    Typically this error provides some diagnostic or debugging output, such as a stack trace.
