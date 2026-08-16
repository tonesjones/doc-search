---
title: "Checker-specific directives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/checker-specific-directives.html"
content_id: "Z8gsPgo~OrnoCBHOg3Hx4A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:27.211879+00:00"
---

# Checker-specific directives

A few of the security directives are for use with a specific checker. These are
shown in the following table:

Table 1.

| Checker | Directive |
| --- | --- |
| CSRF | `csrf_check_needed` |
| `csrf_validator` |
| MISSING_AUTHZ | `sensitive_action` |
| WEAK_GUARD | `sensitive_operation` |
| XSS | `method_with_servlet_sinks_on_input` |
| `method_with_servlet_sinks_on_output` |
| `move_xss_outside_method` |
| `xss_sanitizer_method` |

**Use case for the WEAK_GUARD checker:**

- Specify particular methods for WEAK_GUARD to detect.

  See sensitive_operation.

**Use case for the XSS (cross-site scripting)
checker:**

- Specify methods that send data to HTTP output. These should be reported if
  tainted data is passed to them.

  See method_with_servlet_sinks_on_output.
