---
title: "Hybrid (Java and Kotlin) Android applications"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/hybrid-java-and-kotlin-android-applications.html"
content_id: "3MTKBMTJ1~0DLF9I_3yuoQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:09.117669+00:00"
---

# Hybrid (Java and Kotlin) Android applications

- Run the `cov-configure --java` command and the
  `cov-configure --kotlin` command to enable the build capture of both Java and Kotlin
  Android source.
- To capture Android configuration files, use `coverity capture`.

  Coverity captures Java and Kotlin Android files that are needed by the
  analysis, including the manifest (AndroidManifest.xml) and the
  layout resource files.
- You need to pass `--android-security` to the `cov-analyze` command.

Note:
Java and Kotlin source code are analyzed separately.
