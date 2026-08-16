---
title: "Specifying a list file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specifying-a-list-file.html"
content_id: "Xj6xrfytmMiX~qertKgdCg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:00.104784+00:00"
---

# Specifying a list file

On the command line, you can specify a list file by using the `-l` option
with the name of the list file as argument. A single dash denotes
`stdout`. If no argument has been specified with the
`-l` option, the name of the first (source or library) file specified
is used as the name of the list file, where the suffix is replaced by the default list
file suffix (.lst).

When no list option has been specified, all diagnostic and system messages will be sent
to `stdout`. That stream is captured and written to the analysis log
file, which can be found at `output/forchk.log` within the specified
intermediate directory.
