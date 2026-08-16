---
title: "Checkers disabled in Sigma when running Coverity Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/checkers-disabled-in-sigma-when-running-coverity-analysis.html"
content_id: "_54T~YEQazWhyV_w~_SzZg"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:07.144028+00:00"
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
Coverity Analysis 2023.3, regardless of their enablement status in previous
installations.

Table 1. Sigma checks/checkers now disabled by default

| Disabled Sigma check/checker |
| --- |
| SIGMA.certificate_verification_disabled_core_java |
| SIGMA.certificate_verification_disabled_node_https |
| SIGMA.certificate_verification_disabled_node_request_reject_unauthorized |
| SIGMA.certificate_verification_disabled_node_restify |
| SIGMA.certificate_verification_disabled_node_tls |
| SIGMA.certificate_verification_disabled_node_ws |
| SIGMA.certificate_verification_disabled_sequelize |
| SIGMA.certificate_verification_disabled_sequelize_mssql |
| SIGMA.certificate_verification_disabled_socket_io |
| SIGMA.el_injection_core_java |
| SIGMA.header_injection_core_java |
| SIGMA.insecure_block_cipher_algorithm_core_java |
| SIGMA.insecure_cipher_node_crypto |
| SIGMA.insecure_tls_version_core_java |
| SIGMA.insufficient_password_hash_iterations_node_crypto |
| SIGMA.java_code_injection_core_java |
| SIGMA.jcr_injection_core_java |
| SIGMA.jsp_sql_injection_core_java |
| SIGMA.ldap_injection_core_java |
| SIGMA.missing_secure_attribute_core_java |
| SIGMA.missing_secure_attribute_servlet |
| SIGMA.missing_secure_attribute_session_cookie_servlet |
| SIGMA.missing_secure_attribute_session_cookie_servlet_xml |
| SIGMA.missing_secure_attribute_session_cookie_spring_boot_properties |
| SIGMA.missing_secure_attribute_session_cookie_spring_boot_yaml |
| SIGMA.missing_tls_socket_io_client |
| SIGMA.nosql_query_injection_core_java |
| SIGMA.ognl_injection_core_java |
| SIGMA.open_redirect_core_java |
| SIGMA.os_cmd_injection_core_java |
| SIGMA.path_manipulation_core_java |
| SIGMA.regex_injection_core_java |
| SIGMA.script_code_injection_core_java |
| SIGMA.session_fixation_core_java |
| SIGMA.sqli_core_java |
| SIGMA.tainted_environment_with_execution_core_java |
| SIGMA.trust_boundary_violation_core_java |
| SIGMA.unknown_language_injection_core_java |
| SIGMA.unrestricted_database_access_android |
| SIGMA.unrestricted_dispatch_core_java |
| SIGMA.unrestricted_file_access_android |
| SIGMA.unrestricted_postmessage_target_javascript_window |
| SIGMA.unsafe_deserialization_core_java |
| SIGMA.unsafe_jni_core_java |
| SIGMA.unsafe_named_query_core_java |
| SIGMA.unsafe_reflection_core_java |
| SIGMA.url_manipulation_core_java |
| SIGMA.xpath_injection_core_java |
