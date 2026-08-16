---
title: "Working with the report generator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/working-with-the-report-generator.html"
content_id: "1bx4BPkUfEazNeoI36Arpg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:00.820700+00:00"
---

# Working with the report generator

The following sections explain how you install the report generator, how you configure it, and
how you generate a report.

The following procedure assumes that someone has already used Coverity Analysis to
analyze your code base and commited the resulting defect data to Coverity Connect. For
guidance with this process, see Coverity Analysis 2026.6.0 User and Administrator Guide.

The workflow is:

1. Install the report generator using the
   Coverity Reports installer.
2. Configure the report generator. The structure of the configuration file is explained
   in Mobile OWASP Top 10 report configuration file.
3. Generate a report.

Note: If the `--output` option isn’t used, then the report is saved in the
directory the user calls the command from.
