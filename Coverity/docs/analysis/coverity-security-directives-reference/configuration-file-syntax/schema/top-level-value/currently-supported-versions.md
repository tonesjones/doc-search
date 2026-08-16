---
title: "Currently supported versions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/currently-supported-versions.html"
content_id: "xMk_Lv_6rdobiCc8dzazjA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:32.444736+00:00"
---

# Currently supported versions

In addition to the current `format_version`, version 12, a security
directives file can use one of the legacy versions that are listed in the following
table:

Table 1. Supported format_version field values in release 2026.6.0

| Valid value | Changes in this version |
| --- | --- |
| `12` | For Visual Basic, introduced support for `DC.CUSTOM_CHECKER` custom directives. |
| `11` | - For Visual Basic, introduced support for   `DF.CUSTOM_CHECKER` directives. - Introduced `".NET"` as a language value that can match C#, Visual Basic, and .NET   bytecode. |
| `8` | - Added the `TEXT.CUSTOM_CHECKER` directive. - Changed how to specify custom don’t-call   (`DC.*`) and custom dataflow   (`DF.*`) checkers. - Updated `CSRF` directives. - Updated `MISSING_AUTHZ` directives. - Added the `sink_kind` field. - Added the `read_from_HANA_library_import` directive. |
| `6` | - Added JavaScript support. - Added the Java and C# directive   `sanitizer_for_checker`. |
| `5` | - For Java and C#, introduced the `with_annotation`   `MethodSet` and `ClassSet`   through the new `AnnotationSet` object. - For Java and C#, introduced support for   DF.*CUSTOM_CHECKER* custom checker   directives. - Introduced support for these new directives:    - For Java and C#:     `sink_for_checker`   - For Java Android:     `android_safe_categories`   - For Java Android:     `android_protected_intent_actions` |
| `4` | Required the top-level `language` field and added C# support for many former Java-only directives. |
| `3` | Introduced support for these Java directives:   - `method_returns_tainted_data` - `sensitive_operation` (see WEAK_GUARD checker   annotations) - `xss_sanitizer_method` |
| `2` or greater | Introduced support for a Java directive: `simple_entry_point` |
| `1` or greater | Support for all other directives (pre-version 2 directives). See User directives. |
