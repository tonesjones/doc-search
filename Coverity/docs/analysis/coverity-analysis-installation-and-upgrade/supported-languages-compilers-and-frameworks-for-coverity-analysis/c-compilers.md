---
title: "C# compilers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c-compilers.html"
content_id: "Spq9oiV9wR0Dp2CV1kf2BQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:03.362716+00:00"
---

# C# compilers

Table 1. Supported C# compilers for static analysis

| Compiler | Compiler version | Language version | Host OS | Notes |
| --- | --- | --- | --- | --- |
| Visual Studio | 2019, 2022 | Up to C# 14 | Windows 64-bit | Visual Studio Express editions are not supported.  Coverity supports analysis of Windows RT applications.  **Deprecation notice:** NET 9.0 is deprecated as of 2026.3.0 and support for it will be removed in a future release. |
| .NET | 8.0-10.0 | Windows 64-bit releases supported by Coverity Analysis for C# and Visual Basic (see the table titled "Windows: Coverity Analysis platform support" for details).  Linux 64-bit and Linux ARM64 releases that support .NET 10. Coverity's C# compiler depends on an included .NET 10 runtime. |
| Unity | 2022.3 | Windows 64-bit |
