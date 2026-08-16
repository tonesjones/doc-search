---
title: "Custom dataflow and text checkers (JSON directives)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/custom-dataflow-and-text-checkers-json-directives-.html"
content_id: "jUVazacRjKHD7Nf6pW10ng"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:13.954965+00:00"
---

# Custom dataflow and text checkers (JSON directives)

Coverity provides two "frameworks", DF.*CUSTOM_CHECKER* and
TEXT.*CUSTOM_CHECKER,* that let you create your own dataflow or text checkers.
Sometimes a new checker requires just a few lines of JSON.

DF.*CUSTOM_CHECKER*
:   A *dataflow checker* reports when untrusted strings, streams, and byte
    arrays from a tainted source are propagated through the program and used at an
    unsafe sink. Many security vulnerabilities fit this general pattern: these
    include injection issues, data exposure, insecure object references, and more.
    Custom checkers can specify a trust model that enhances the extensive
    data-source modeling that is built in to Coverity Analysis.

TEXT.*CUSTOM_CHECKER*
:   A *text checker* can match patterns that indicate illegal data,
    misconfiguration, or other issues of concern. The patterns to match can be
    either regular expressions or XPath queries.

As with security analysis directives, you specify the directives for a JSON custom
checker by saving them in a file of their own, then using the
`--directive-file` option to identify that file when you invoke
`cov-analyze`.

**Use case:** A security team wants to determine whether HTTP-request data is ever
passed into any C# function whose name ends in the suffix `Db`.

The following JSON record specifies a checker to locate this situation. Its name is
DF.GOES_TO_DATABASE.

```
{
    "type"           : "Coverity analysis configuration",
    "format_version" : 12,
    "language"       : "C#",
    "directives" : [
        {
            "dataflow_checker_name" : "DF.GOES_TO_DATABASE",
            "taint_kinds" : [ "http", "http_header" ]
        },
        {
            "sink_for_checker" : "DF.GOES_TO_DATABASE",
            "sink" : {
                "to_callsite : {
                    "callsite_with_static_target" : {
                        "matching" : ".*Db\\(System.String\\)void"
                    },
                },
                "input" : "arg1"
            }
        }
    ]
}
```

**Use case:** A security team wants to learn if a configuration properties file ever
indicates version 2.x. The following custom text checker, TEXT.UNSAFE_VERSION,
accomplishes this:

```
// In the "directives" object, include ...
{
    "text_checker_name" : "TEXT.UNSAFE_VERSION",
    "file_pattern"      : { "regex" : "config(-.+)\\.json$",
                            "case_sensitive" : false },      
    "defect_pattern"    : { "regex" : "version.*:.*2\\..*" }
}
```

**Limitations and alternatives:** At present, text checkers cannot match regular
expressions in source code that is emitted as an abstract syntax tree (AST).

**Learn more:**

- See "DF.*CUSTOM_CHECKER"* and
  "TEXT.*CUSTOM_CHECKER"* in the Coverity 2026.6.0 Checker Reference for information about these two custom checker
  frameworks.
- For descriptions of the JSON fields that custom checker definitions can use,
  see "Configuration file syntax" in the
  Coverity 2026.6.0 Security Directives Reference.
