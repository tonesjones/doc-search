---
title: "Taint sources in the code base"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/taint-sources-in-the-code-base.html"
content_id: "UpfNegIGVevAgVWI3eByQQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:23.204586+00:00"
---

# Taint sources in the code base

Command-line options cannot manage the detection of tainted data sources that
originate in the code base you are scanning. To do this, use security directives or
models.

Security directives
:   You can use either the `method_returns_tainted_data` or the
    `tainted_data` directive to designate code that analysis
    should report as a potential tainted-data source.

    C#, Java, or Visual Basic can use
    `method_returns_tainted_data`. JavaScript can use
    `tainted_data`.

    For more information, see the Coverity 2026.6.0 Security Directives Reference.

Models and annotations
:   For compiled languages, you can write function models or add inline code
    annotations to designate code that analysis should report as a potential
    tainted-data source.

    - Models and modeling primitives are available for C/C++, C# and Visual
      Basic (.NET code), Go, and Java.
    - Inline annotations are available for C/C++, C# and Visual Basic (.NET
      code), and Java.

For more information, see Models and primitives.
