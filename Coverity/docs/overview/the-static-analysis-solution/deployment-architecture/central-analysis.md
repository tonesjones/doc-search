---
title: "Central analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/central-analysis.html"
content_id: "mbvbtTqmYRoy3BQk7Op5lg"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:14.523630+00:00"
---

# Central analysis

With central analysis, the code is built and analyzed on a shared build server. The
following diagram illustrates a basic Coverity deployment. As shown: Coverity Connect is
installed on a separate host, along with its embedded database. The process would
include the following steps:

1. Coverity Analysis is installed on a build server where the artifacts of the build
   are analyzed.
2. At the conclusion of each build-and-analysis run, code issues that have been
   discovered are committed to Coverity Connect as issues.
3. Developers use their clients to connect to the Connect server and check out the code
   for which they are responsible.
4. Developers examine the issues found, and attempt to resolve them.
5. Developers check their code in again, and another analysis is run at the scheduled
   time.
6. As multiple developers perform steps 3 to 5, Coverity Connect tracks each issue's
   history and evolution to allow managers to look at trends and generate progress
   reports.

Figure 1. Central Analysis
[image: image]
