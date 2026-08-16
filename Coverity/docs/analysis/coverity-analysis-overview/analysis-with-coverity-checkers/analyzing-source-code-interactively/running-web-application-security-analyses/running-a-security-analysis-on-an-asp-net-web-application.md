---
title: "Running a security analysis on an ASP.NET web application"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-a-security-analysis-on-an-asp.net-web-application.html"
content_id: "klltmOTu_Ny7mU_Ai5EPfg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:04.600265+00:00"
---

# Running a security analysis on an ASP.NET web application

Attention: Support for ASP.NET Web Forms and ASPX page analysis will be removed
in a future release. This includes Web Forms entry point detection, Web Forms-specific
directives, and the CONFIG.ASP_VIEWSTATE_MAC and
CONFIG.DEAD_AUTHORIZATION_RULE checkers. Customers using ASP.NET
Web Forms should plan to migrate to Blazor, Razor Pages, or ASP.NET Core MVC.

The security analysis of ASP.NET web applications is capable of reporting defects in Razor view
templates (such as *.cshtml files) and Web Forms (such as
*.aspx files). In most cases, these files are captured
automatically by `cov-build`. If web application template files are
captured, the following message will be displayed in your console output and in
build-log.txt (see The output of 'cov-build': The 'build-log.txt' log file):

```
140 compiled C# template files captured:
   42 ascx files
   33 aspx files
   65 cshtml files
```

In cases where `cov-build` fails to capture the expected number of
template files, please consult Capturing an ASP.NET (4.0 or earlier) web application
and Capturing an ASP.NET Core (2.0 or later) web application.

Following capture (build capture or `coverity capture`),
Coverity Analysis runs the `cov-security-da` command by
default. The `cov-security-da` command extracts additional dataflow and
sanitization information from bytecode libraries in the emit, to limit the number of
false positive defects reported by the XSS checker. You can disable this step by using
the --no-security-da option.
