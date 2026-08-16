---
title: "Reasons for results differences"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/reasons-for-results-differences.html"
content_id: "~o2GEC6gewquk41UWAKBTA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:02.283377+00:00"
---

# Reasons for results differences

When running Desktop Analysis, you may encounter analysis results that differ somewhat
from those found by your central analysis server. This section is intended to highlight
several of the most common causes for result disparities, and suggest ways to lessen or
eliminate those differences. Note that this is not an exhaustive list of all scenarios
in which results differences may be observed.

Missing summary data for adjacent functions
:   Desktop Analysis relies on summary data from the Coverity Connect server. This is used to
    provide information on functions and files within your project that are
    outside of the analysis scope. If `cov-run-desktop` does
    not have access to the most current summary data, your local analysis
    results may differ significantly from those found by central analysis.

    The main causes for missing summary data are as follows:

    - The central analysis did not capture and/or commit analysis summary data (controlled by
      the `cov-analyze --export-summaries` option).
    - `cov-run-desktop` failed to properly download analysis summaries from
      the Coverity Connect server - possibly because the connection
      timed out.
    - If `cov-run-desktop` is run in disconnected mode (specified with the
      `--disconnected` option), it won't attempt
      any connection with the server.

Target configuration differences
:   It is possible that the downloaded summaries were created while analyzing the code when it
    was configured for a different target (e.g. "debug" versus "release" builds,
    separate operating systems, etc). To prevent this issue, make sure that you
    associate your Desktop Analysis run with a reference stream that matches, or
    is sufficiently close to, your local target configuration.

Code version skew
:   Results differences may be present if the downloaded summary data is for a different
    version of the source code than what you have checked out. This can happen
    if you are not using the most recent reference snapshot for retrieving
    analysis summaries.

    To prevent this issue, it is recommended that you set
    the `cov-run-desktop --reference-snapshot` option to
    `scm`, so that the selected reference snapshot is as
    close as possible to your current code version. See
    `--reference-snapshot` option for
    `cov-run-desktop` in the Coverity 2026.6.0 Command Reference for more information.

Dependencies outside the analysis scope
:   In some configurations, changes made locally in one file can affect other code outside the
    analysis scope. When these dependencies flow out of, and then back into, the
    analysis scope, Desktop Analysis accuracy may suffer.

    For example, suppose
    a project contains three functions, A, B, and C, where A calls B, and B
    calls C. If A and C are analyzed locally but B is not, the analysis will
    have to rely on summary data for function B. As such, any local changes
    to C will not be reflected in that summary data, and the analysis
    results may be inaccurate or incomplete.

Problem reporting on anonymous types
:   Certain checkers, including CHECKED_RETURN, occasionally fail to report defects on
    functions that involve anonymous types when called by
    `cov-run-desktop`. Consequently, if your project
    contains any defects in such functions, they may only be found during the
    full central analysis.

Insufficient information for dynamic language call graph
:   In dynamic languages supporting interprocedural analysis (currently JavaScript), in order
    to properly apply downloaded function summaries, the analysis call graph
    computation must process some "extra files" in addition to those selected in
    the analysis scope. This is handled automatically by
    `cov-run-desktop` based on information in the
    downloaded summary batch about the relationships between source files in the
    Central analysis. If a source file that you are analyzing is new, or is
    newly calling into another source file or library, that information might
    not be found by `cov-run-desktop`, and you can improve the
    accuracy of the analysis by manually including those files that are called
    into in the analysis scope.

Whole program checkers
:   For performance reasons, Desktop Analysis does not enable security checkers or other "whole
    program" checkers by default. This may cause discrepancies in your Central
    and Desktop Analysis results. See Running security checkers with cov-run-desktop for more
    information.
