---
title: "Coverity Analysis checkers replaced by Sigma checks in 2024.9.0"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-checkers-replaced-by-sigma-checks-in-2024.9.0.html"
content_id: "e4oZ7viIl6d6GgyALcGArg"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:54.753536+00:00"
---

# Coverity Analysis checkers replaced by Sigma checks in 2024.9.0

A number of Coverity Analysis
checkers have been either completely or partially replaced by Sigma (SIGMA.*)
checks.

The following Coverity Analysis checkers have been replaced by
Sigma (SIGMA.*) checks for equivalent languages.

Table 1. Coverity Analysis checkers replaced by Sigma checks for specific
languages

| Coverity Analysis checker | Languages removed from Coverity Analysis checker | Sigma checks replacing this Coverity checker |
| --- | --- | --- |
| ``` CONFIG.ENABLED_DEBUG_MODE ``` | Python | ``` SIGMA.debug_enabled_core_python_asyncio ``` |
| ``` INSECURE_COMMUNICATION ``` | C#, Visual Basic (XML configuration files only) | ``` SIGMA.missing_tls_dotnet_core_entity_framework SIGMA.missing_tls_dotnet_core_mongodb SIGMA.missing_tls_dotnet_core_mysql SIGMA.missing_tls_dotnet_core_oracle SIGMA.missing_tls_dotnet_core_postgresql SIGMA.missing_tls_dotnet_core_redis SIGMA.missing_tls_dotnet_core_sqlserver ``` |
| ``` INSECURE_COOKIE ``` | C#, Visual Basic | ``` SIGMA.missing_httponly_attribute_dotnet_core SIGMA.missing_secure_attribute_dotnet_core SIGMA.missing_secure_attribute_aspnet_core_config SIGMA.missing_samesite_attribute_aspnet_core_config ``` |
| ``` INSECURE_NETWORK_BIND ``` | Python | ``` SIGMA.insecure_network_bind_core_python_socket ``` |
| ``` RISKY_CRYPTO ``` | Python | ``` SIGMA.weak_hash_core_python_hashlib ``` |
| ``` SECURE_TEMP ``` | Python | ``` SIGMA.insecure_temporary_file_core_python_tempfile ``` |
| ``` UNSAFE_XML_PARSE_CONFIG ``` | Python | ``` SIGMA.xml_external_entity_enabled_core_python_sax ``` |
| ``` XML_EXTERNAL_ENTITY ``` | Python | ``` SIGMA.xml_external_entity_enabled_core_python_pandas SIGMA.xml_external_entity_enabled_core_python_sax SIGMA.xml_external_entity_enabled_core_python_xml ``` |

The following Coverity Analysis checkers have been replaced by Sigma (SIGMA.*) checks for
all languages.

Table 2. Coverity Analysis checkers completely replaced by Sigma checks

| Coverity Analysis checker | Sigma checks replacing this Coverity checker |
| --- | --- |
| ``` CONFIG.COOKIES_MISSING_HTTPONLY ``` | ``` SIGMA.missing_httponly_attribute_aspnet_core_config ``` |
| ``` CONFIG.DJANGO_CSRF_PROTECTION_DISABLED ``` | ``` SIGMA.csrf_protection_disabled_django ``` |
| ``` EXPOSED_PREFERENCES ``` | ``` SIGMA.shared_preferences_data_exposure_android ``` |
| ``` INSECURE_REFERRER_POLICY ``` | ``` SIGMA.insecure_referrer_policy_django SIGMA.insecure_referrer_policy_django_config_settings ``` |
| ``` JINJA2_AUTOESCAPE_DISABLED​ ``` | ``` SIGMA.expression_escaping_disabled_jinja2 ``` |
