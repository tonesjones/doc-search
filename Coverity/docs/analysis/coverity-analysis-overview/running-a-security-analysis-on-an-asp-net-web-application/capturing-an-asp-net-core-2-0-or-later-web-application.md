---
title: "Capturing an ASP.NET Core (2.0 or later) web application"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/capturing-an-asp.net-core-2.0-or-later-web-application.html"
content_id: "X_U6jwuZHBP1FqUVCInerQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:05.238615+00:00"
---

# Capturing an ASP.NET Core (2.0 or later) web application

Attention: Support for ASP.NET Web Forms and ASPX page analysis will be removed
in a future release. This includes Web Forms entry point detection, Web Forms-specific
directives, and the CONFIG.ASP_VIEWSTATE_MAC and
CONFIG.DEAD_AUTHORIZATION_RULE checkers. Customers using ASP.NET
Web Forms should plan to migrate to Blazor, Razor Pages, or ASP.NET Core MVC.

To include web application template files in the analysis, `cov-build` must
capture a compilation of your web applications that has View Precompilation enabled.
Typically, View Precompilation is enabled by default. However, if
`cov-build` is failing to capture Razor template files, take care
to ensure that View Precompilation has not been disabled. This is most commonly
controlled by the following MSBuild properties:

- `RazorCompileOnBuild`
- `RazorCompileOnPublish`
- `MvcRazorCompileOnBuild`
- `MvcRazorCompileOnPublish`
