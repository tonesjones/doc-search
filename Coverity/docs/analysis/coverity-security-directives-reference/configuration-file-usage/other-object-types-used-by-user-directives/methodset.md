---
title: "MethodSet"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/methodset.html"
content_id: "hKPlhXlxJKV9~QFLLbDVjw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:25.841339+00:00"
---

# MethodSet

**Used by these directives:**
`ignore_all_argument_dataflow_to_method`,
`ignore_method_dataflow`, `ignore_method_output`,
`method_returns_constant`, `method_returns_param`,
`method_returns_servlet_output_stream`,
`method_returns_tainted_data`,
`method_set_for_dc_checker`,
`method_with_servlet_sinks_on_input`,
`method_with_servlet_sinks_on_output`,
`move_xss_outside_method`, `sensitive_operation`,
`simple_entry_point`, `xss_sanitizer_method`

**Used by these objects:**
`CallsiteSet`

A `MethodSet` value describes a set of methods from the program. You can
specify a `MethodSet` value by using one of the following field
names:

- named
- matching
- overrides
- implemented_in_class
- and
- with_annotation
