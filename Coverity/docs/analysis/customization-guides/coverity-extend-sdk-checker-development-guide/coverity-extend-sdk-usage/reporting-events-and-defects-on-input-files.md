---
title: "Reporting events and defects on input files"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/reporting-events-and-defects-on-input-files.html"
content_id: "XeDLdDUwDIBFox_rPY0qPQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:59.135807+00:00"
---

# Reporting events and defects on input files

In addition to analyzing ASTs and reporting defects in source code, Coverity Extend
SDK checkers can also inspect the contents of files captured during the
Coverity build and emit processes and report defects in them. These files
can include source files, files packaged within a WAR file (and emitted with
`cov-emit-java --webapp-archive` or similar), or an Android
AndroidManifest.xml and its associated APK file (emitted with
the `--android-apk` and `--input-file` options to
`cov-emit-java`).
