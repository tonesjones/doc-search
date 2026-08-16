---
title: "Coverity Template Dynamic Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-template-dynamic-analysis.html"
content_id: "BvezrVViSaF4ookC9h_01w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:36.844173+00:00"
---

# Coverity Template Dynamic Analysis

Coverity Template Dynamic Analysis (DA) can be enabled to run as part of the *capture* step in the
Coverity Analysis workflow.
It translates supported web page template languages based on JavaScript (ECMAScript®) and TypeScript into an abstract syntax tree.
It then runs dynamic analysis on the controllable parameters of the web page to determine their effect upon the rendered page.
The intent of Template DA is to provide a more complete dataflow model when a supported web template language is used.
Its effect is to increase the accuracy of security dataflow checkers in projects that use one of the supported template languages.

Since Template DA executes code on the platform used for capture, it presents a security risk.
However, the way in which these local invocations are performed minimizes that risk, as described here:

- As with Security DA, the set of inputs used to test an interface is stereotyped.
  It is unlikely that such input would trigger malicious behavior: Such behavior would need to already exist in the template implementation.
  Further, the scenarios used to determine input-output relations are run within a sandbox. The sandbox prevents template implementations
  (or application code) from invoking a known set of system calls that are considered dangerous. It does so by intercepting calls to `require()`
  and replacing the dangerous calls with calls to mock routines.
- To avoid security risks that have not been addressed by the previous item, you can
  simply avoid using the --run-template-da-on-emit option with
  `cov-build`.
