---
title: "Coverity Analysis checkers replaced by Sigma checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-checkers-replaced-by-sigma-checkers.html"
content_id: "~7hdoPRA4By_qbeNzibCQw"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:06.469129+00:00"
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
| ANDROID_DEBUG_MODE | Android | SIGMA.debug_enabled_android |
| CONFIG.HTTP_VERB_​TAMPERING | Java | SIGMA.http_verb_tampering_method_​inclusion_​servlet  SIGMA.http_verb_tampering_method_​omission_​servlet |
| EXPRESS_X_POWERED_​BY_​ENABLED | JavaScript, TypeScript | SIGMA.verbose_server_banner_express |
