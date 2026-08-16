---
title: "Security configuration file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/security-configuration-file.html"
content_id: "YvGzebmBwkXVhHenebb3iA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:22.891016+00:00"
---

# Security configuration file

A *security configuration file* either alters the default
behavior of a checker that is provided with Coverity Analysis, or it defines a
new, custom checker.

Security analysis directives provide hints and describe patterns that cannot easily be
captured by using a model or an annotation. You can use analysis directives to focus and
fine-tune source-code analysis.

Coverity Analysis provides a set of directives that allow you to define new
checkers and to modify the behavior of existing Web application and Android application
security checkers; for example, to support new frameworks and APIs or to suppress false
positive defect reports.

To use this functionality, you must create a file in JSON syntax and pass it to either the
`--directive-file` option or, for the `DC.CUSTOM`
checker, the `--dc-config` option of `cov-analyze`. See
How to
invoke a custom configuration.

The following sections describe the syntax of these JSON files, including some extensions
to standard JSON that this format supports. The subsections of Configuration file usage describe the individual
directives, along with objects that support their use.
