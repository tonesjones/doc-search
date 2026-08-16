---
title: "The Coverity Analysis build system"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-coverity-analysis-build-system.html"
content_id: "RGFzXhrkJrEyAwFK34S3zQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:57.873485+00:00"
---

# The Coverity Analysis build system

Before you attempt a native compiler integration, it is useful to understand the commands
that are run as part of the Coverity Analysis build process, and what type of
information they need to successfully complete. The Coverity Analysis build process has
the following command binaries:

`cov-configure`
:   Probes the native compiler and creates the configuration used by the build system to emulate
    the native compiler. See The 'cov-configure' command.

`cov-build`
:   Monitors the native build and invokes `cov-translate` for every invocation
    of the native compiler. `cov-build` is not relevant to the
    discussion of the compiler configuration customization and is not covered in
    this document. For more information, see `cov-build` in the Coverity 2026.6.0 Command Reference.

`cov-translate`
:   Emulates the native compiler by mapping the native compiler command line to the command line
    used by the Coverity compiler. See The 'cov-translate' command.

`cov-emit` (Coverity compiler)
:   Parses the code and stores it in the Coverity emit database. This command is not covered in
    this document. See `cov-emit` in the Coverity 2026.6.0 Command Reference.

`cov-preprocess`
:   Produces preprocessed source using either the native compiler or the Coverity compiler. This
    is useful for debugging parse errors. See The 'cov-preprocess' command.

`cov-manage-emit`
:   Manipulates the Coverity emit database in many different ways. It can be used to call
    `cov-translate`, `cov-emit`, or
    `cov-preprocess` on a previously captured code base. It can
    be viewed as a wrapper for `cov-translate`,
    `cov-emit`, and `cov-preprocess`. This
    command is not covered in this document. For more information, see
    `cov-manage-emit`
    in the Coverity 2026.6.0 Command Reference.

In this section:

- The 'cov-configure' command
- The 'cov-translate' command
- The 'cov-preprocess' command
- The 'cov-test-configuration' command
