---
title: "Security threats"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/security-threats.html"
content_id: "Wv47SJCB14Zo85UG6s9CKg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:25.914558+00:00"
---

# Security threats

Security checkers search for code constructs that are vulnerable to attack. The areas of
concern that Coverity Analysis inspects include the following kinds of constructs:

- Flow of control, including entry points to an application
- Flow of data, including sensitive or tainted data sources and data sinks
- Web attacks such as forged cross-site requests (CSRF) or cross-site scripting
  (XSS)
- Misuse of tags
- Potentially vulnerable operations on data; for example, bit shifts
- The trustworthiness of Android `Intent` objects

You can use directives that narrow down this search, and that address specific
situations. The following use cases describe a few of the possibilities.

**Use cases:**

- Inspect a Web framework that defines new entry points.

  See simple_entry_point and async_method.
- Extend a tainted dataflow checker (such as SQLI or XSS) to identify further
  untrusted sources of data; for example, from a custom library or a custom
  framework.

  See tainted_data, method_returns_tainted_data, and
  data_has_tag.
- Extend a tainted dataflow checker to identify further untrusted *data
  sinks*.

  See sink_for_checker and data_has_tag.
- Extend a dataflow checker by specifying additional *pass-through* rules for
  data from a custom library or a custom framework.

  See method_returns_param, dataflow_through_callsite, async_method, local_callback, map_read, map_write,
  and data_has_tag.
- Suppress false-positive reports from a checker or a group of checkers.

  See sanitizer_for_checker, android_safe_categories, android_protected_intent_actions, ignore_all_argument_dataflow_to_method, ignore_method_dataflow, and ignore_method_output.
