---
title: "Java Android applications"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/java-android-applications.html"
content_id: "IES3_NWHmwZVRLupabbUKA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:24.507355+00:00"
---

# Java Android applications

- Run the `cov-configure --java` command to enable the build capture of Java
  Android source.
- To capture Android configuration files, use `coverity capture`.

  Coverity captures Java Android files that are needed by the analysis,
  including the manifest (AndroidManifest.xml) and the layout
  resource files.
- You need to pass `--android-security` to the `cov-analyze` command.
