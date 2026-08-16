---
title: "Checkers disabled in Sigma when running Coverity Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/checkers-disabled-in-sigma-when-running-coverity-analysis.html"
content_id: "~o9C7~B8iBre1rPK2xqeDQ"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:11.885591+00:00"
---

# Checkers disabled in Sigma when running Coverity Analysis

A number of Coverity checkers are duplicated in Sigma. Since
Sigma is integrated in Coverity Analysis, the duplicate Sigma checks are automatically
disabled when running Coverity Analysis in order to avoid duplicate error messages. For
this reason, there may be differences between what Sigma reports when run inside
`cov-analyze` and what Sigma reports when running as standalone.

The following Sigma checks are now disabled by default in Coverity
Analysis. A Sigma check can be enabled manually using the following command:

```
% sigma analyze --enable <check_name>
```

CAUTION:

When you upgrade Coverity Analysis, all previous settings are
overwritten. All checkers listed in the following table will be disabled by default in
Coverity Analysis 2022.9, regardless of their enablement status in previous
installations.

Table 1. Sigma checkers now disabled by default

| Disabled Sigma checker |
| --- |
| SIGMA.certificate_verification_disabled_node_restify |
| SIGMA.certificate_verification_disabled_node_ws |
| SIGMA.certificate_verification_disabled_sequelize |
| SIGMA.certificate_verification_disabled_sequelize_mssql |
| SIGMA.certificate_verification_disabled_socket_io |
| SIGMA.hardcoded_secret_pattern |
| SIGMA.insecure_block_cipher_algorithm_core_java |
| SIGMA.insecure_block_cipher_mode_core_java |
| SIGMA.insecure_permission_on_exported_component_android_provider |
| SIGMA.insecure_permission_on_exported_component_android_receiver |
| SIGMA.insecure_permission_on_exported_component_android_service |
| SIGMA.insecure_tls_version_core_java |
| SIGMA.missing_permission_on_exported_component_android_activity |
| SIGMA.missing_permission_on_exported_component_android_provider |
| SIGMA.missing_permission_on_exported_component_android_receiver |
| SIGMA.missing_permission_on_exported_component_android_service |
| SIGMA.missing_secure_attribute_core_java |
| SIGMA.missing_secure_attribute_session_cookie_servlet |
| SIGMA.unrestricted_postmessage_target_javascript_window |
