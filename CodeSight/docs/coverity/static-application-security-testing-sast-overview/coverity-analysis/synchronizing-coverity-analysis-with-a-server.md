---
title: "Synchronizing Coverity Analysis with a server"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/synchronizing-coverity-analysis-with-a-server.html"
content_id: "MIzN80q3oVNvBhomq5owcw"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:53.976982+00:00"
---

# Synchronizing Coverity Analysis with a server

Code Sight can run analyses locally, but it can also be configured to share certain data with an analysis server.

Typically, if Code Sight is synchronized, an administrator will set this up for your particular installation.
Once synchronization is enabled, Code Sight downloads issue information for the most recent full central scan,
either from Coverity Connect or from Coverity on Polaris.

When it has a server connection, there are two kinds of data that Code Sight shares:

- Analysis summaries
- Triage Information

By default, Code Sight does not display issues that are not duplicated locally.
You can control this behavior by using the Filter controls.

## Analysis summaries

Coverity Analysis creates summaries when you run a full SAST scan of the code base.
It uses such summaries to improve the accuracy of single-file scans.

When connected, Code Sight obtains analysis summaries from the server.
This reduces the need to run full scans locally.

If you do not connect to one of the analysis servers, we recommend that you run a full
scan from time to time.
