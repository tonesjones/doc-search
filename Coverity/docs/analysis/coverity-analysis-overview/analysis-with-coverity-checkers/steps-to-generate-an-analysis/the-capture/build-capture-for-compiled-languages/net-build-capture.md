---
title: ".NET build capture"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/.net-build-capture.html"
content_id: "IOgjFRvyMq0XlE8Q9EN3dA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:47.223140+00:00"
---

# .NET build capture

Capture for languages supported by the .NET framework (C# and Visual Basic, on certain platforms) has two requirements:

1. The platform that Coverity Analysis runs on needs to support a
   .NET 10 run time. Coverity Analysis includes the needed .NET 10 run
   time.
2. Build capture requires a working native build. This is true of all build-capture use cases for all platforms and for all languages.

   Coverity Analysis does not itself depend upon having a .NET SDK installed on any platforms.
   Most .NET native builds, however, will depend upon having access to a .NET SDK to build natively, so the native builds for C# capture will likely require a .NET SDK appropriate
   to the specific build to be available.
