---
title: "Coverity Analysis checkers replaced by Sigma checks"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-checkers-replaced-by-sigma-checks.html"
content_id: "rqUYfJTKOrdwk1m~lEZTZg"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:57.354096+00:00"
---

# Coverity Analysis checkers replaced by Sigma checks

A number of Coverity Analysis
checkers have been either completely or partially replaced by Sigma (SIGMA.*)
checks.

The following Coverity Analysis checkers have been replaced by
Sigma (SIGMA.*) checks for equivalent languages.

Table 1. Coverity Analysis checkers replaced by Sigma checks for specific
languages

| Coverity Analysis checker | Languages removed from Coverity Analysis checker | Sigma checks replacing this Coverity checker |
| --- | --- | --- |
| ``` ASPNET_MVC_VERSION_HEADER ``` | C# | ``` SIGMA.sensitive_data_in_response_aspnet_core ``` |
| ``` UNSAFE_XML_PARSE_CONFIG ``` | C# | ``` SIGMA.xml_external_entity_enabled_dotnet_core ``` |

The following Coverity Analysis checkers have been replaced by Sigma (SIGMA.*) checks for
all languages.

Table 2. Coverity Analysis checkers completely replaced by Sigma checks

| Coverity Analysis checker | Sigma checks replacing this Coverity checker |
| --- | --- |
| ``` CONFIG.ASPNET_VERSION_HEADER ``` | ``` SIGMA.sensitive_data_in_response_aspnet_core_config ``` |
| ``` CONFIG.CONNECTION_STRING_PASSWORD ``` | ``` SIGMA.hardcoded_secret_aspnet_core_config ``` |
| ``` CONFIG.MISSING_CUSTOM_ERROR_PAGE ``` | ``` SIGMA.verbose_error_message_aspnet_core_config ``` |
