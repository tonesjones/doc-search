---
title: "Security Dynamic Analysis for Java and .NET source"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/security-dynamic-analysis-for-java-and-.net-source.html"
content_id: "fkVe_Jxs0az0NvL0FA5aDA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:03.653708+00:00"
---

# Security Dynamic Analysis for Java and .NET source

Following capture, Security Dynamic Analysis processes the captured bytecode libraries for Java and .NET (C# amd Visual Basic) source to extract
additional dataflow and sanitization information. This information is used to increase the accuracy of the defects reported by the XSS checker.
Dataflow and sanitization behavior is inferred by passing stereotyped inputs to selected methods, and observing the results.
This dynamic analysis provides more detailed information than can be obtained by using static analysis of the bytecode.

In some cases, it is not possible for `cov-build` to run Security DA as part of the capture process.
If so, it will post a warning message to the log. In these rare cases, you can run `cov-security-da`
as a separate command.

Security DA is computationally intensive, and might noticeably increase the time required to capture a project.
If the XSS checker is disabled or the accuracy of its results is unimportant, you can disable Security DA without
affecting the results of other checkers. To do so, use the --no-security-da option.

For information about security risks associated with Security DA, see
Coverity Security Dynamic Analysis" in the
2026.6.0 Safety Manual.
