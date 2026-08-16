---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "hgdu3jaZ0b9kSFngG2o5og"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:07.627473+00:00"
---

# Description

The `cov-run-desktop` command performs an expedited local analysis by
considering only the files or translation units specified by the user, subject to
various command line options. When running `cov-run-desktop`, you must
either include the specific file name(s) at the end of the command, pass the --analyze-scm-modified option to
let your Source Code Management system (SCM) specify which files to analyze, or analyze
previously captured source, by using the --analyze-captured-source
option. Translation unit selection
has additional information on this process.

You can create a coverity.conf file to share compiler configurations
and other desktop analysis settings to multiple users of the same code base. This
configuration file can also be used by individual users to maintain these settings
locally (see the Coverity
Desktop Analysis
2026.6.0 User Guide for details).

The analysis performed is the same as when using `cov-analyze`, so
`cov-run-desktop` accepts most of the same options as `cov-analyze`.

Because `cov-run-desktop` normally does not analyze an entire code base,
it relies on summaries stored in Coverity Connect to get information about the code that
is not analyzed locally. This requires that a periodic (perhaps nightly) full analysis
be run in order to populate the summary information. Additionally, after the main
analysis phase is complete, `cov-run-desktop` normally contacts the
Coverity Connect server to determine which defects were newly introduced, and to
retrieve triage data (Classification, Severity, Owner, etc.) for existing issues.
`cov-run-desktop` can also operate in "disconnected" mode, relying
on previously downloaded summary and issue data, if any.

By default, `cov-run-desktop` produces issue output in a text format
that is intended to imitate the typical output syntax of compiler error messages. Most
editors and IDEs will then automatically allow you to navigate to the corresponding
locations in the source code. `cov-run-desktop` can also write the
issues in JSON format so that a user-provided tool can consume and present them in a
user-defined way.

The exit code of `cov-run-desktop` is 0 when the analysis completes
successfully and 2 or greater if there is an error. The
`--exit1-if-defects` option causes `cov-run-desktop`
to exit with code 1 when defects are present.

You can configure this command to use a forward proxy when communicating with the Coverity
Connect server. The setup is the same as with the `cov-commit-defects`
command. For more information on this topic, see "Using a forward proxy" in
the `cov-commit-defects` section.
