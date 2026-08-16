---
title: "Defining custom checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/defining-custom-checkers.html"
content_id: "eDPjixH_9BaAexDIuX4NYw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:26.570430+00:00"
---

# Defining custom checkers

The following directives are for defining custom checkers.

Table 1. Directives that define custom checkers

| Checker type | Directive |
| --- | --- |
| DF.*CUSTOM_CHECKER* | `dataflow_checker_name` |
| TEXT.*CUSTOM_CHECKER* | `text_checker_name` |
| DC.*CUSTOM_CHECKER* | `dc_checker_name` |
| `method_set_for_dc_checker` |

Note: Use of the DC (DON'T CALL) custom checker is discouraged, in favor of using
CodeXM.

**Use cases for a TEXT custom checker:**

- Report an XML file that contains an XPath query.
- Report a text file that contains a match for a particular regular
  expression.

**Use case for a DF (data flow) custom checker:**

- Report code that passes an HTTP request to a database function.
