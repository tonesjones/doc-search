---
title: "Capturing an ASP.NET (4.0 or earlier) web application"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/capturing-an-asp.net-4.0-or-earlier-web-application.html"
content_id: "5lwHgaw_mVPdIMWJVq3pUQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:05.892279+00:00"
---

# Capturing an ASP.NET (4.0 or earlier) web application

Attention: Support for ASP.NET Web Forms and ASPX page analysis will be removed
in a future release. This includes Web Forms entry point detection, Web Forms-specific
directives, and the CONFIG.ASP_VIEWSTATE_MAC and
CONFIG.DEAD_AUTHORIZATION_RULE checkers. Customers using ASP.NET
Web Forms should plan to migrate to Blazor, Razor Pages, or ASP.NET Core MVC.

By default, `cov-build` attempts to find and emit any web application
template file (Razor and WebForms) contained in the same folder or sub-folder of every
project file (*.csproj or *.vbproj file) that
is being compiled. To properly emit template files, cov-build also
relies on web.config files being present in the directory that
contains the project file. If the web application being compiled is not structured this
way, the automatic capture of the template files might not capture all of the web
application’s template files.

To manually include these files in the analysis, you should first disable the automatic capture
of web application template files by passing the
`--disable-aspnetcompiler` option to `cov-build`.
Then, `cov-build` must capture an invocation of
Aspnet_compiler.exe on the published web application.
Publishing the web application and running Aspnet_compiler.exe
might not be part of your source build process. Following is an example command line for
running Aspnet_compiler.exe:

```
Aspnet_compiler.exe -p C:\path\to\MyWebApplicationRoot -v root -d -f -c C:\path\to\TargetDir
```

The physical path, specified with the `-p` option, should point to the web
application root path—that is, the directory the web application was published to.

The virtual path, specified with the `-v` option, is required but does not
affect the analysis.

The final command-line option, `-c`, names the output directory for the compiler
outputs.
