---
title: "Sensitive data might persist on a local machine"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sensitive-data-might-persist-on-a-local-machine.html"
content_id: "fmu739TTjeU4_uEwWfkQBw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:56.705074+00:00"
---

# Sensitive data might persist on a local machine

The Coverity intermediate directory (`idir/`) might store sensitive data, either as plaintext or in a structured format.
This recorded data can include, but is not necessarily limited to:

- The state of the environment when capturing a build; for example, the names and values of environment variables,
  the arguments passed on the command line.
- Source code and certain types of build artifacts.
- Host names of the systems involved in build capture and analysis runs.
- Defects identified by `cov-analyze`.
- Logs from captured builds, analysis runs, build replays, and so on.
