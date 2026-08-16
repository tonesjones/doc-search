---
title: "Coverity Analysis checkers replaced by Sigma checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-checkers-replaced-by-sigma-checkers.html"
content_id: "8UdSnwBhdeCvk2LZvJ9zLA"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:08.447083+00:00"
---

# Coverity Analysis checkers replaced by Sigma checkers

A number of Coverity Analysis
checkers have been either completely or partially replaced by Sigma (SIGMA.*)
checks.

The following Coverity Analysis checkers have been replaced by
Sigma (SIGMA.*) checks for equivalent languages.

Table 1. Coverity Analysis checkers completely replaced by Sigma checkers for specific
languages

| Coverity Analysis checker | Languages removed from Coverity Analysis checker | Sigma checkers replacing this Coverity checker |
| --- | --- | --- |
| MISSING_PERMISSION_ON_​EXPORTED_COMPONENT | Java, Kotlin | insecure_permission_on_exported_component_android_activity insecure_permission_on_exported_component_android_provider insecure_permission_on_exported_component_android_receiver insecure_permission_on_exported_component_android_service missing_permission_on_exported_component_android_activity missing_permission_on_exported_component_android_provider missing_permission_on_exported_component_android_receiver missing_permission_on_exported_component_android_service |
