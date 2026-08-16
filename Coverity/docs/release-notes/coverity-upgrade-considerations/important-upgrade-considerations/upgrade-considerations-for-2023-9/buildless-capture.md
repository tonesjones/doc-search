---
title: "Buildless capture"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/buildless-capture.html"
content_id: "i1G1FQ7W348rmLNjDCRQyw"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:01.238698+00:00"
---

# Buildless capture

The behavior of the `cov-capture` command has changed. Formerly, this
command provided its own copy of Maven and Gradle for use in capturing a Java project.
As of the current release, these software packages are no longer provided by the
`cov-capture` command. For more information on this topic, including
how to tell whether this change affects your projects and how to remediate this change
if it does affect your projects, refer to the following Knowledge Base article:

<https://community.blackduck.com/s/article/Coverity-2023-9-0-Cov-Capture-Change>
