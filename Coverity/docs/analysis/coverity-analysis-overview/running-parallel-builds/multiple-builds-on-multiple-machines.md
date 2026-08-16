---
title: "Multiple builds on multiple machines"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/multiple-builds-on-multiple-machines.html"
content_id: "zwirr~hDJXOB0MrM~ka0ig"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:15.842627+00:00"
---

# Multiple builds on multiple machines

Because the `cov-build` command relies on capturing calls to
`exec()`, distributed builds that use remote procedure calls or
other network communication to invoke builds are not detected. Distributed builds can be
handled by modifying the build system to add an additional Coverity Analysis target that
uses the `cov-translate` program. For more information, see Alternative build command: 'cov-translate'.

Distributed builds using a common intermediate directory on an NFS partition that is
shared by all contributing servers are supported on Linux and Solaris systems that have
the same Coverity Analysis distribution, version, and compiler configuration.

Note: The `cov-emit` command can either run by itself, or be invoked
indirectly by `cov-build` or `cov-translate`. You
cannot directly or indirectly run `cov-emit` on one platform and
`cov-analyze` on another platform.

Build systems can explicitly call `cov-translate` in the following
ways:

- Multiple build commands run on multiple machines, which each locally run
  `cov-translate`.
- A single `make` or similar command distributes individual
  compilations to multiple configured servers via `ssh` or
  another remote job execution service.
