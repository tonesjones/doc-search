---
title: "Security analysis directives (JSON)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/security-analysis-directives-json-.html"
content_id: "~LPdRIMtJPt_BKjMRiGCcw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:12.654865+00:00"
---

# Security analysis directives (JSON)

Security analysis directives are an expressive configuration format for providing hints and describing patterns
that cannot easily be captured by using a model or annotation.

Analysis directives also form the backbone of API description for dynamically typed languages, which require a dataflow-based
approach to identify object types of interest.

You specify analysis directives by saving them in a file that uses JSON format.
Then when you invoke `cov-analyze`, use the `--directive-file` option to identify the file name.

**Use case:**
In a Java project, specify that all methods whose name has the prefix `get`,
in classes that specify the `@Controller` annotation, should be treated as receiving untrustworthy data.

For example, the project supports a custom, in-house Java Web service framework.
A security team wants to indicate that all methods whose name has the prefix `get`, receive untrusted
data from the Web.
Flagging these classes in source code with a `@Controller` analysis annotation is part of the solution,
but directives can provide finer-grained control, as shown by the following sample code:

```
// In the "directives" object, include ...
{
    "simple_entry_point" : {
        "and" : [
                { "implemented_in_class" : {
                    "with_annotation" : { "named" : "annot.Controller" }
                  }
                },
                { "matching" : ".*\\.get.*" }
        ]
    },
    "taint_kinds" : ["http"]
}
```

**Use case:**
The following JavaScript example specifies that any read of the global variable `myLibrary.queryParam`
(whose value is similar to `window.location.query` in JavaScript) is untrusted:

```
// In the "directives" object, include ...
{
    "tainted_data" : {
        "read_path_off_global" : [
            { "property" : "myLibrary" },
            { "property" : "queryParam" }
        ]
    },
    "taint_kind" : "js_client_url_query_or_fragment"
}
```

**Limitations and alternatives:**

- For statically typed languages, API models provide an alternative way to specify sources and sinks.
- Certain function properties affect quality and concurrency checkers; for example, dereferenced arguments,
  thrown exceptions, and so on. Security analysis directives can detect such conditions:
  to check for them, you need to use API models.

**Learn more:**

- Coverity 2026.6.0 Security Directives Reference provides a full description of the
  security analysis directives.
- See the "Options: Web and mobile
  application security" section of `cov-analyze`
  in the Coverity 2026.6.0 Command Reference for details of the
  `--directive-file` option.
- The section "Coverity Web application
  security" of the Coverity 2026.6.0 Checker Reference
  discusses issues that are particular to Web applications, and how to guard against
  exploits.
