---
title: "Coverity Analysis checkers replaced by Sigma checks in 2024.12.0"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-checkers-replaced-by-sigma-checks-in-2024.12.0.html"
content_id: "Cqdk0I4mBsTQXSJPDwrIGQ"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:51.533908+00:00"
---

# Coverity Analysis checkers replaced by Sigma checks in 2024.12.0

A number of Coverity Analysis
checkers have been either completely or partially replaced by Sigma (SIGMA.*)
checks.

The following Coverity Analysis checkers have been replaced by
Sigma (SIGMA.*) checks for equivalent languages.

Table 1. Coverity Analysis checkers replaced by Sigma checks for specific
languages

| Coverity Analysis checker | Languages removed from Coverity Analysis checker | Sigma checks replacing this Coverity checker |
| --- | --- | --- |
| ``` BAD_CERT_VERIFICATION ``` | Python | ``` SIGMA.certificate_verification_disabled_core_python_paramiko_client ``` |
| ``` CONFIG.ENABLED_DEBUG_MODE ``` | C#, Visual Basic (.config files only) | ``` SIGMA.debug_enabled_aspnet_core_config ``` |
| ``` CONFIG.ENABLED_TRACE_MODE ``` | C#, Visual Basic (.config files only) | ``` SIGMA.trace_mode_enabled_aspnet_core_config ``` |
| ``` RISKY_CRYPTO ``` | JavaScript, TypeScript | ``` SIGMA.insecure_cipher_node_crypto SIGMA.insecure_cipher_node_forge SIGMA.insufficient_password_hash_iterations_node_bcrypt SIGMA.insufficient_password_hash_iterations_node_crypto SIGMA.insufficient_password_hash_iterations_node_argon2 SIGMA.weak_hash_node_crypto ``` |

The following Coverity Analysis checkers have been replaced by Sigma (SIGMA.*) checks for
all languages.

Table 2. Coverity Analysis checkers completely replaced by Sigma checks

| Coverity Analysis checker | Sigma checks replacing this Coverity checker |
| --- | --- |
| ``` UNRESTRICTED_MESSAGE_TARGET ``` | ``` SIGMA.unrestricted_postmessage_target_javascript_window ``` |
