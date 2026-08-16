---
title: "Changed path for emitted files in Bazel-built projects"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/changed-path-for-emitted-files-in-bazel-built-projects.html"
content_id: "ROES_PBLkOmS0uGx~VE50A"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:58.616606+00:00"
---

# Changed path for emitted files in Bazel-built projects

The path of emitted files for Bazel-built projects has changed from being relative to the
Bazel execution path to being relative to the Bazel workspace. If you build your
projects with Bazel, you might need to make some or all of the following changes.

If you previously stripped the execution root path during analysis or commit by passing
`--strip-path $(bazel info execution_root)` to
`cov-analyze` or `cov-commit-defects`, do one of
following:

- Replace your existing `--strip-path` arguments with
  `--strip-path $(bazel info workspace)` to strip off the workspace
  path instead the execution path. Doing so will keep the results in their current
  relative location.
- Remove the `--strip-path` arguments entirely.

If you use `cov-run-desktop` for desktop analysis of Bazel-built projects,
you must change the relative path to the file you want to analyze in the command
argument. For example, to run analysis on a file named `main.c` in the
root of your Bazel workspace, you would have previously run `cov-run-desktop
$(bazel info execution_root)/main.c`. You must now run
`cov-run-desktop main.c`.
