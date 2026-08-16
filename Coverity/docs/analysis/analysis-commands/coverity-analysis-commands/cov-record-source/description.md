---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "jzCnWAp4~js4BkbFb0OKEw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:03.762560+00:00"
---

# Description

The `cov-record-source` command records Java Web application files and
outputs them to an intermediate directory (this command does not attempt to parse or
emit the files).

The Java Web applications can be in the following forms:

- Web Archive (`.war` file)
- Enterprise Archive (`.ear` file)
- A directory with the unpacked contents of either
- Any combination of the above

When recording a build that contains a Java Web application that you want to analyze, you
must run the `cov-record-source` command in addition to the cov-build
--record-with-source command to properly record the Java Web application.
