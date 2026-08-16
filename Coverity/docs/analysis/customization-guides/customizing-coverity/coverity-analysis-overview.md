---
title: "Coverity Analysis Overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-overview.html"
content_id: "xm2SSer7bC7ws7Ft4CqJEw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:07.397025+00:00"
---

# Coverity Analysis Overview

Coverity® Analysis aims to provide a successful out-of-the-box
experience across a wide range of use cases.

The following features and processes contribute to this success:

- We provide a large number of built-in checkers that test for a broad range of
  issues.
- We support many widely used frameworks whose components can include language
  support, libraries, build technologies, and more.
- We minimize the rate at which checkers detect and report false positives.
- We constantly evaluate and tune the default behavior of Coverity Analysis, testing it against real code.

Despite this development work, some software projects do require additional tuning, or
customization, to meet a customer's needs.

Black Duck Software, Inc. provides a rich set of ways to customize Coverity behavior.
There are simple, global ways to adjust the results of an analysis; more specific ways
to tune analysis results; and for advanced users, ways to extend the capabilities of the
analysis itself.

*Customizing Coverity* begins by describing how to fine-tune deployment and analysis configuration in order
to improve performance and manage findings. You can further customize analysis to
support atypical applications or deployment environments, to address project-specific
concerns, and to improve analysis results by eliminating false positives and false
negatives.

The topics that follow introduce the customization options, show some usage examples, and
indicate resources where you can learn more. Within each section, alternative techniques
are ordered from simpler to more advanced—though of course, ease of use can
depend on various factors, including the user's previous experience.

In this section:

- Global customization choices
- Choices that depend on the checker, the language, or other contexts
- Creating new checkers
