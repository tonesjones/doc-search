---
title: "Running web application security analyses"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-web-application-security-analyses.html"
content_id: "zHLT_cFpBpoCM05AAticwA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:02.659016+00:00"
---

# Running web application security analyses

Coverity Analysis can find security vulnerabilities such as cross-site scripting (XSS) and SQL
injection in a wide variety of web applications. To enable web application security
analysis, pass the `--webapp-security` option to
`cov-analyze`. See Software issues and impacts by checker in the
Coverity 2026.6.0 Checker Reference for details on which kinds of
vulnerabilities Coverity can find for each programming language. For memory requirements
and other prerequisites to the analysis,
see Prerequisites.

CAUTION:

The "Software issues and impacts by checker" table is published only in HTML format.
It does not appear in the PDF version of the Coverity 2026.6.0 Checker Reference.

This section adds recommendations and troubleshooting information to supplement the basic
analysis steps in The analysis for some kinds
of web applications. Languages or environments that are not mentioned in this section do
not require additional steps.

In this section:

- Running a security analysis on a Java web application
- Running a security analysis on an ASP.NET web application
