---
title: "Tags that influence translation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tags-that-influence-translation.html"
content_id: "l0i1qKDXG7q~MsGVgLvNPA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:04.374772+00:00"
---

# Tags that influence translation

<preprocess_first>
:   Specifies if the build fails because of errors in `cov-emit`'s
    preprocessing. If this is specified, `cov-build` tries to
    preprocess each file with the native compiler before sending it to
    `cov-emit`. This tag does not take a value.

    The command
    to run to preprocess a file is configured by the <preprocess_> options
    given next. It is constructed based on the command line used to actually
    compile the file.

<cygwin>
:   Indicates that the given compiler supports Cygwin file processing.
