---
title: "AI triage checker support and confidence levels"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/ai-triage-checker-support-and-confidence-levels.html"
content_id: "R2Gwj9siD7g3on_00iRPEw"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:12.020919+00:00"
---

# AI triage checker support and confidence levels

This reference lists the AI triage support level and expected confidence value for
each supported combination of static analysis checker and programming
language.

## Overview

AI triage exhibits varying levels of support depending on the specific static
analysis checker and programming language combination. The level of support is
reflected in the `Confidence` value returned with each AI triage
result, which corresponds to the extent of benchmarking and validation completed
for the given checker and language pair.

## Checker and language confidence matrix

The following table specifies the expected confidence values for supported static
analysis checker and language combinations when using AI triage
functionality:

Table 1. AI triage confidence levels by checker and language

| Checker | Language | Confidence |
| --- | --- | --- |
| `DEADCODE` | C/C++ | `High` |
| `FORWARD_NULL` | C/C++ | `High` |
| `HARDCODED_CREDENTIALS` | All | `High` |
| `HARDCODED_SECRET` | All | `High` |
| `MISSING_LOCK` | C/C++ | `High` |
| `NULL_FIELD` | C/C++ | `High` |
| `NULL_RETURNS` | C/C++ | `High` |
| `OVERRUN` | C/C++ | `High` |
| `RESOURCE_LEAK` | C/C++ | `High` |
| `SIGMA.hardcoded_secret` | All | `High` |
| `UNCAUGHT_EXCEPT` | C/C++ | `High` |
| `UNINIT` | C/C++ | `High` |
| `UNINIT_CTOR` | C/C++ | `High` |
| Any checker not listed above | C/C++ | `Medium` |
| Any checker not listed above | All other languages | `Low` |
