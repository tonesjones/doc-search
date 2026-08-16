---
title: "Buildless capture"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/buildless-capture.html"
content_id: "Ni6MfX8ZYn_tZYmPuLdvMA"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:27.534794+00:00"
---

# Buildless capture

The behavior of the `cov-capture` command has changed. Formerly, this
command automatically downloaded JavaScript dependencies using NPM, Bower, and Yarn. The
`cov-capture` command no longer downloads JavaScript dependencies.
For more information on this topic, including how to include JavaScript dependencies in
your emitted code, refer to the following Knowledge Base article:

<https://community.blackduck.com/s/article/Coverity-2021-06-Cov-Capture-Change>
