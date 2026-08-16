---
title: "Working with the report generator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/working-with-the-report-generator.html"
content_id: "PoqAQ4AY0puyDw~zXsuFxQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:48.702510+00:00"
---

# Working with the report generator

The following sections explain how you install the report generator, how you configure
it, and how you generate a report.

The following procedure assumes that someone has already used Coverity Analysis to analyze your
code base and commited the resulting defect data to Coverity Connect. For guidance with
this process, see Coverity Analysis 2026.6.0 User and Administrator Guide.

The workflow is:

1. Install the report generator
   using the Coverity Reports installer
2. Set up a connection to Coverity Connect.

   You need to do this only the first time you run the report generator. See  Connecting to
   Coverity Connect for more information.
3. Generate a report.

After you have configured and generated a report, the report file should appear in the
Coverity report installation directory; for example:

```
C:\Program Files\Coverity\Coverity Reports\bin\
```
