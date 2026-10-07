---
title: "Why is no build log generated?"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/why-is-no-build-log-generated-.html"
content_id: "wJFwBxTFcJTL7TjwbOddlw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:31.187795+00:00"
---

# Why is no build log generated?

Check the permissions of the directory that is being written to. Even though the final
message may indicate that a file is available, you will not see any error message when
the file is not written out.

If you cannot write to the expected directory, then give the –dir option either an
absolute path to a directory in your home directory, or a relative path to a better
location.
