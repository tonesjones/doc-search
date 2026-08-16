---
title: "Kotlin Android applications"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/kotlin-android-applications.html"
content_id: "Pr7Z~m75DA734xArtXfziw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:08.476258+00:00"
---

# Kotlin Android applications

- Run the `cov-configure --kotlin` command to enable the build capture of
  Kotlin Android source.
- To capture Kotlin configuration files, use `coverity capture`.

  Coverity captures Kotlin Android files that are needed by the analysis,
  including the manifest (AndroidManifest.xml) and the layout resource files.
- No special flags are needed for the `cov-analyze` command, because Kotlin
  checkers are enabled by default.
