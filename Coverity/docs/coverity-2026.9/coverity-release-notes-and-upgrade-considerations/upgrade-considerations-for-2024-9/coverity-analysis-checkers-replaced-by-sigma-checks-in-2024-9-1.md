---
title: "Coverity Analysis checkers replaced by Sigma checks in 2024.9.1"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/coverity-analysis-checkers-replaced-by-sigma-checks-in-2024.9.1.html"
content_id: "fH8eJ5yKswyTl~Y~ohFSMA"
version: "2026.9"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-10-04T23:39:46.967090+00:00"
---

# Coverity Analysis checkers replaced by Sigma checks in 2024.9.1

A number of Coverity Analysis
checkers have been either completely or partially replaced by Sigma (SIGMA.*)
checks.

The following Coverity Analysis checkers have been replaced by
Sigma (SIGMA.*) checks for equivalent languages.

Table 1. Coverity Analysis checkers replaced by Sigma checks for specific
languages

| Coverity Analysis checker | Languages removed from Coverity Analysis checker | Sigma checks replacing this Coverity checker |
| --- | --- | --- |
| ``` ANONYMOUS_DB_CONNECTION ``` | Python | ``` SIGMA.anonymous_access_enabled_core_python_couchdb SIGMA.anonymous_access_enabled_core_python_pymongo SIGMA.anonymous_access_enabled_django_dj_database_url SIGMA.anonymous_access_enabled_flask_couchdb SIGMA.anonymous_access_enabled_flask_pymongo SIGMA.anonymous_access_enabled_django_db ``` |
| ``` INSECURE_COMMUNICATION ``` | Python | ``` SIGMA.missing_tls ``` |

The following Coverity Analysis checkers have been replaced by Sigma (SIGMA.*) checks for
all languages.

Table 2. Coverity Analysis checkers completely replaced by Sigma checks

| Coverity Analysis checker | Sigma checks replacing this Coverity checker |
| --- | --- |
| ``` MISSING_PASSWORD_VALIDATOR ``` | ``` SIGMA.weak_password_policy ``` |
