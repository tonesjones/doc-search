---
title: "Securing web applications"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/securing-web-applications.html"
content_id: "uIiTfFrk1exF1FXAbyVjkA"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:24.534352+00:00"
---

# Securing web applications

Coverity Static Analysis can keep your Web applications secure by helping you find security
issues before the malicious actors do.

The analysis detects when unsafe data enters your Web application from the HTTP requests,
network transactions, untrusted databases, console input, or the filesystem. It tracks
this unsafe data, and if the data is used incorrectly within a context, Coverity reports
this usage as an issue. Coverity provides you with actionable remediation advice for the
technologies in use. It can flag the following vulnerabilities:

- SQL injection
- Cross-site scripting
- OS command injection

You can enable specific groups of checkers for securing Web applications when you
configure analysis.

In addition to identifying problematic areas, Coverity offers open-source libraries of
sanitizers that can protect vulnerable code for Java and C#.
