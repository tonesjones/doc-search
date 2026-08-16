---
title: "Checkers disabled in Sigma when running Coverity Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/checkers-disabled-in-sigma-when-running-coverity-analysis.html"
content_id: "kroNLPBaMajlNjKM9QhobQ"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:19.090179+00:00"
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

Table 1. List of disabled Sigma checkers when running Coverity Analysis

| Sigma checker |
| --- |
| SIGMA.certificate_verification_disabled_core_java |
| SIGMA.certificate_verification_disabled_node_https |
| SIGMA.certificate_verification_disabled_node_request_reject_unauthorized |
| SIGMA.certificate_verification_disabled_node_restify |
| SIGMA.certificate_verification_disabled_node_tls |
| SIGMA.certificate_verification_disabled_node_ws |
| SIGMA.certificate_verification_disabled_socket_io |
| SIGMA.excessive_session_lifetime_connect_mongo |
| SIGMA.excessive_session_lifetime_connect_redis |
| SIGMA.excessive_session_lifetime_google_cloud_datastore |
| SIGMA.excessive_session_lifetime_express_client_sessions |
| SIGMA.broad_domain_attribute_cookie_express |
| SIGMA.excessive_session_lifetime_express_cookie_session |
| SIGMA.excessive_session_lifetime_express_session |
| SIGMA.missing_httponly_attribute_session_cookie_express |
| SIGMA.insufficient_password_hash_iterations_node_bcrypt |
| SIGMA.missing_secure_attribute_servlet |
| SIGMA.missing_secure_attribute_session_cookie_express |
| SIGMA.missing_secure_attribute_session_cookie_servlet_xml |
| SIGMA.missing_secure_attribute_session_cookie_spring_boot_properties |
| SIGMA.missing_secure_attribute_session_cookie_spring_boot_yaml |
| SIGMA.root_path_attribute_cookie_express |
| SIGMA.insecure_tls_cipher_suite_node_https |
| SIGMA.insecure_tls_cipher_suite_node_request |
| SIGMA.insecure_tls_cipher_suite_node_tls |
| SIGMA.insecure_tls_renegotiation_node_https |
| SIGMA.insecure_tls_renegotiation_node_request |
| SIGMA.insecure_tls_renegotiation_node_tls |
| SIGMA.insecure_tls_version_ios_protocol_max |
| SIGMA.insecure_tls_version_ios_protocol_min |
| SIGMA.insecure_tls_version_ios_stream_property |
| SIGMA.insecure_tls_version_node_https |
| SIGMA.insecure_tls_version_node_request |
| SIGMA.insecure_tls_version_node_tls |
