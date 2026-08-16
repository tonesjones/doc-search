---
title: "Multiple builds on a single machine"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/multiple-builds-on-a-single-machine.html"
content_id: "PbJcr5Wp4iRiv8bcWPzD1Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:15.194313+00:00"
---

# Multiple builds on a single machine

A build on a single host can use a single build command to create multiple, concurrent
compilation processes. There are several ways to capture information for build and C/C++
analyses.

To capture information for a build, C/C++ analysis, or both, you can run a single
`cov-build` command with a `make -j` or similar
command.

To capture information for a C/C++ analysis, you can use multiple
`cov-build` commands sequentially:

```
cov-build --capture ... make [-j N] ...
cov-build --capture ... make [-j N] ...
cov-build --capture ... make [-j N] ...
```

To capture information for a C/C++ analysis, you can explicitly call
`cov-translate` from the build system:

```
make [-j N] CC="cov-translate ..." ...
```

If all `cov-translate` processes are concurrently running on the same
machine, Coverity recommends using a single intermediate directory. If
`cov-translate` processes run on different machines, then use
multiple local intermediate directories and merge them using
`cov-manage-emit` after the build is finished. Running
`cov-translate` in parallel on NFS is not recommended.

If you use multiple `cov-build` commands sequentially, the
`--capture` flag is not needed.
