---
title: "Example: Finding MISRA standard deviations and customizing a checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/example-finding-misra-standard-deviations-and-customizing-a-checker.html"
content_id: "FchZUkwGIqyTHg4GNhfy3A"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:58.105793+00:00"
---

# Example: Finding MISRA standard deviations and customizing a checker

The following configuration shows an embedded C configuration: The analysis will check the code
for deviations from the MISRA C 2012 coding standard (`misrac2012`)
for required and advisory rules only (`pre-canned: required-advisory`).

The configuration also enables the analysis of calls to function pointers to find defects (`c-cpp-fnptr: true`),
requests that parse warnings be reported, and enables the security checkers (`aggressiveness-level: high`).

Finally, the configuration enables the INFINITE_LOOP checker and turns on
its `report_no_escape` option.

```
capture:
  build:
    clean-command: make clean
    build-command: make

analyze:
  aggressiveness-level: high
  c-cpp-fnptr: true
  parse-warnings:
    enabled: true
  coding-standards:
    misrac2012:
      pre-canned: required-advisory
  checkers:
    checker-config:
      INFINITE_LOOP:
        enabled: true
        options:
          report_no_escape: true

commit:
  connect:
    stream: flux-capacitor
    url: https://connect.example.com
```
