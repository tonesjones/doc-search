---
title: "Single build on a single machine"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/single-build-on-a-single-machine.html"
content_id: "55lRyyZnH9tXvIo047Au0Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:14.561773+00:00"
---

# Single build on a single machine

The `cov-build` command can capture parallel builds. Examples of
commonly seen parallel build commands would be `make -j` or
`xcodebuild -jobs`. One problem with parallel builds is that the
build-log.txt log file contains interleaved output, which might
make it difficult to determine if a given source file has been parsed and output to the
intermediate directory. In such case, the intermediate directory is still created
without problems.
