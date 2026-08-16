---
title: "Legacy ways of creating checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/legacy-ways-of-creating-checkers.html"
content_id: "Gy~IlvHJBqisB6TKMekgbw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:15.269121+00:00"
---

# Legacy ways of creating checkers

Previous releases of Coverity had other ways of creating custom checkers. These are
still supported to provide backward compatibility, but unless your organization has already
invested in the older techniques, we don't recommend that you use them for new
development.

The legacy techniques are the SECURE_CODING checker and the Extend SDK.

## SECURE_CODING checker

The SECURE_CODING checker (not truly customizable) was superseded by the
DC.*CUSTOM_CHECKER* framework, which has in turn been superseded by CodeXM:
See "Writing your own *Don't Call* checker" in the Coverity
CodeXM Checkers Development Guide.

## Extend SDK

Coverity Extend SDK is a framework for writing checkers in C++ that support analyses
of C/C++, Java, and C# applications. Much of this framework is the same as that used
by the checkers that are built in to Coverity Analysis.

**Limitations and alternatives:**

- The Extend SDK is difficult to learn and to use. If you have not already
  invested in Extend SDK development, we strongly recommend that you use CodeXM
  rather than Extend.
- Extend checkers are compiled by a C++ toolchain into separate binaries. They do
  not run as part of `cov-analyze`. They cannot be run in
  parallel with each other, or with the built-in analysis.

**Learn more:** The development kit is described in the Coverity Extend SDK 2026.6.0 Checker Development Guide.
