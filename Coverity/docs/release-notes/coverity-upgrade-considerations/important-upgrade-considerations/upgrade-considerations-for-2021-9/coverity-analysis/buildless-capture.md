---
title: "Buildless capture"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/buildless-capture.html"
content_id: "8F8COizNnDxXprUTKuYz1g"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:21.019373+00:00"
---

# Buildless capture

The `cov-capture` command now bundles an upgraded Gradle distribution
(v7.1). This upgrade might cause issues for some Gradle projects, for example, projects
using deprecated dependency configurations like `compile` and
`testCompile`. When this situation is identified,
`cov-capture` presents the following warning:

> [WARNING] Some Gradle projects couldn't be captured properly, likely because they
> require a different Gradle version. Please provide a Gradle distribution and
> compatible JDK "COVERITY_BLC_GRADLE_ZIP" and "COVERITY_BLC_GRADLE_JDK". For example,
> for a project compatible with Gradle 6.1 use:
> COVERITY_BLC_GRADLE_ZIP=C:/gradle-6.1-bin.zip COVERITY_BLC_GRADLE_JDK=C:/jdk15/
> cov-capture --dir ... Note that only JDKs 8 and above are supported.

To properly capture such projects, you must provide a Gradle distribution compatible with
the captured project using the `COVERITY_BLC_GRADLE_ZIP` environment
variable. If this Gradle distribution requires a compatible JDK, provide one using the
`COVERITY_BLC_GRADLE_JDK` environment variable. Check your Gradle
release notes for information about compatible JDKs. Note that only JDK version 8 or
newer is supported by the `cov-capture` command.
