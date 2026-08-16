---
title: "Checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/checkers.html"
content_id: "MJfDWaJelfIhKmBBW1i3PA"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:12.687792+00:00"
---

# Checkers

The analysis of your code is done by a collection of programs called *checkers*, which are the foot soldiers of analysis. Each
checker looks for a specific kind of issue, which can range from the simple to the
complex. A simple checker might flag a missing break statement or find a bad comparison.
A more sophisticated checker might find code that is vulnerable to cross-site scripting
attacks or might flag a method call that is not guarded by an authorization check. There
are many possible categories of issues, among them:

- Memory corruption
- Resource leaks
- NULL object or pointer dereferences
- Thread concurrency
- Web application security flaws
- Lines, files, and functions that are insufficiently tested

Coverity Analysis uses hundreds of checkers, and supports over a dozen programming
languages. Checker behavior and performance is constantly checked and updated to
minimize false positives and to improve performance.

Coverity also includes checkers that analyze your code's adherence to a variety of coding
standards, including MISRA, CERT, and OWASP.

When you install Coverity, a standard set of checkers is enabled by default. If you want to
change that, you can enable or disable different checkers when you configure analysis.
After looking at results, you can further refine the analysis by redefining its scope,
by filtering out certain results, or by customizing the behavior of specific
checkers.
