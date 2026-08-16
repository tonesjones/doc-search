---
title: "Coverity Analysis checkers replaced by Sigma checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-checkers-replaced-by-sigma-checkers.html"
content_id: "Qjnvh1lrFCecTq0NkaKQOw"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:13.199858+00:00"
---

# Coverity Analysis checkers replaced by Sigma checkers

A number of Coverity Analysis
checkers have been either completely or partially replaced by Sigma (SIGMA.*)
checks.

The following Coverity Analysis checkers have been replaced by
Sigma (SIGMA.*) checks for equivalent languages.

Table 1. Coverity Analysis checkers partially replaced by Sigma checkers for specific
languages

| Coverity Analysis checker | Languages removed from Coverity Analysis checker |
| --- | --- |
| CONFIG.UNSAFE_SESSION_TIMEOUT | JavaScript, TypeScript |
| INSECURE_COOKIE | JavaScript, TypeScript |

For the following Coverity Analysis checkers, part
of the language support was moved to Sigma.
A subset of the defects for the affected languages will now be reported as Sigma defects.

Table 2. Coverity Analysis checkers with partial language support for specific languages

| Coverity Analysis checker | Affected languages |
| --- | --- |
| RISKY_CRYPTO | JavaScript, TypeScript |
