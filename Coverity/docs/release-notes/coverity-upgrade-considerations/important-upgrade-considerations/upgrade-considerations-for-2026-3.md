---
title: "Upgrade considerations for 2026.3"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrade-considerations-for-2026.3.html"
content_id: "ShnDD10CEJlFa1U23v5L7g"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:46.316739+00:00"
---

# Upgrade considerations for 2026.3

For information about deprecated and dropped support, other updates, known issues, and
fixed bugs, see the Coverity 2026.6.0 Release Notes.

For the list of Sigma checkers disabled by default when running Coverity Analysis
2026.3, see "Checkers disabled in Sigma when running Coverity Analysis" in the Coverity 2026.6.0 Checker Reference.

CAUTION:

When you upgrade Coverity Analysis, all previous settings are
overwritten. All checkers listed in the "Sigma checks
disabled by default in Coverity 2026.3" table in the Coverity 2026.6.0 Checker Reference will be disabled by default in Coverity Analysis
2026.3, regardless of their enablement status in previous installations.

## Coverity Analysis memory requirements

Coverity analysis can use hardware CPU parallelism (multiprocessor, multi-core, and
simultaneous multi-threading), assuming adequate additional memory is available.
When sufficient memory is available, Coverity analysis will attempt to make use of
it to improve performance by performing more computation in parallel.

Minimum: 3 GB

- Recommended for C/C++ scanning with default checkers: At least 8 GB. For
  larger code bases, 5GB + 3GB per million lines of code.
- Recommended for all other scans: At least 12 GB. For larger code bases, 9GB
  + 3GB per million lines of code.
- Memory requirements for Go. When running only quality checkers (not
  including JavaScript, TypeScript, PHP, or Python analysis): 1.0 GiB + (0.5
  GiB * number of analysis workers).

## Checkers

- CodeXM for Go, Python, and JavaScript is deprecated and will be removed in a
  future release.
- User written models for Go and Kotlin are deprecated. A future release will
  remove support for running cov-make-library to customize analysis of Go or
  Kotlin code.
- Kotlin quality checkers are disabled by default as of 2026.3.0 and will be
  removed in a future version.

## Analysis commands

- The cov-link binary has been deprecated and will be removed in a future release.

## Integrations

- Spotbugs and Detekt integrations have been removed.
