---
title: "Local analysis with Gradle"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/local-analysis-with-gradle.html"
content_id: "vmycwsZykbf71LadcCMr6A"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:00.783231+00:00"
---

# Local analysis with Gradle

Coverity Desktop works out of the box to analyze Gradle builds for IntelliJ and Android
Studio 3.6 and newer versions.

Note: Users **must** remove the Coverity Desktop Gradle plugin and the Coverity Connect maven repository (if applicable) from all the
build.gradle files. Failure to do so will result in errors
fetching the Coverity Desktop Gradle plugin from Coverity Connect.
