---
title: "Checkers disabled in Sigma when running Coverity Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/checkers-disabled-in-sigma-when-running-coverity-analysis.html"
content_id: "OR25GNVtdCiOwUDPaAOzlg"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:16.468337+00:00"
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
Coverity Analysis 2022.3, regardless of their enablement status in previous
installations.

Table 1. Sigma checkers now disabled by default

| Disabled Sigma checker |
| --- |
| SIGMA.certificate_verification_disabled_core_java |
| SIGMA.certificate_verification_disabled_node_https |
| SIGMA.certificate_verification_disabled_node_request_reject_unauthorized |
| SIGMA.certificate_verification_disabled_node_tls |
| SIGMA.insecure_cipher_node_crypto |
| SIGMA.insecure_tls_cipher_suite_node_tls |
| SIGMA.insecure_tls_version_node_https |
| SIGMA.insecure_tls_version_node_request |
| SIGMA.insecure_tls_version_node_tls |
| SIGMA.insufficient_password_hash_iterations_node_crypto |
| SIGMA.missing_httponly_attribute_session_cookie_express |
| SIGMA.missing_secure_attribute_servlet |
| SIGMA.missing_secure_attribute_session_cookie_express |
| SIGMA.missing_secure_attribute_session_cookie_servlet_xml |
| SIGMA.missing_secure_attribute_session_cookie_spring_boot_properties |
| SIGMA.missing_secure_attribute_session_cookie_spring_boot_yaml |
| SIGMA.root_path_attribute_cookie_express |
| SIGMA.unrestricted_database_access_android |
| SIGMA.unrestricted_file_access_android |
