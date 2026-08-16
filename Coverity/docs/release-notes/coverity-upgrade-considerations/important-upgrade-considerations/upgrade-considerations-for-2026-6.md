---
title: "Upgrade considerations for 2026.6"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrade-considerations-for-2026.6.html"
content_id: "gjz75ZA5g4jPB9~wef909Q"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:45.664238+00:00"
---

# Upgrade considerations for 2026.6

For information about deprecated and dropped support, other updates, known issues, and
fixed bugs, see the Coverity 2026.6.0 Release Notes.

For the list of Sigma checkers disabled by default when running Coverity Analysis 2026.6,
see "Checkers disabled in Sigma when running Coverity Analysis" in the Coverity 2026.6.0 Checker Reference.

CAUTION:

When you upgrade Coverity Analysis, all previous settings are
overwritten. All checkers listed in the "Sigma checks
disabled by default in Coverity 2026.6" table in the Coverity 2026.6.0 Checker Reference will be disabled by default in Coverity Analysis
2026.6, regardless of their enablement status in previous installations.

## **Coverity Analysis checkers replaced by Sigma checks in 2026.6.0**

A number of Coverity Analysis checkers have been either completely or partially
replaced by Sigma (SIGMA.*) checks.

The following Coverity Analysis checkers have been replaced by Sigma (SIGMA.*) checks
for equivalent languages.

Table 1. Coverity Analysis checkers replaced by Sigma checks for specific
languages

| **Coverity checker name** | **Language** | **Sigma checker name** |
| --- | --- | --- |
| `ANDROID_CAPABILITY_LEAK` | Kotlin | `missing_permission_check_android` |
| `BAD_CERT_VERIFICATION` | Go, Java, Kotlin | `certificate_verification_disabled_crypto_ssh`  `certificate_verification_disabled_crypto_tls`  `certificate_verification_disabled_webview_android` |
| `CONFIG.UNSAFE_SESSION_TIMEOUT` | Go | `excessive_session_lifetime_beego`  `excessive_session_lifetime_gin`  `excessive_session_lifetime_gorilla` |
| `HARDCODED_CREDENTIALS` | Kotlin | `hardcoded_credentials_core_kotlin` |
| `IMPLICIT_INTENT` | Kotlin | `implicit_intent_core_kotlin` |
| `INSECURE_COMMUNICATION` | Kotlin | `missing_tls_apache_commons_io`  `missing_tls_apache_datasource`  `missing_tls_apache_http`  `missing_tls_spring_boot_elasticsearch`  `missing_tls_core_java_sql`  `missing_tls_datastax_driver`  `missing_tls_dom4j_io`  `missing_tls_dom4j_jaxb`  `missing_tls_guava_resources`  `missing_tls_jackson_core`  `missing_tls_jackson_objectmapper`  `missing_tls_jackson_objectreader`  `missing_tls_mongodb`  `missing_tls_okhttp`  `missing_tls_slick_play_database`  `missing_tls_spring_boot_couchbase`  `missing_tls_spring_boot_datasource`  `missing_tls_spring_boot_flyway`  `missing_tls_spring_boot_influx`  `missing_tls_spring_boot_neo4j`  `missing_tls_spring_boot_r2dbc`  `missing_tls_spring_data_mongodb`  `missing_tls_spring_data_r2dbc`  `missing_tls_spring_datasource`  `missing_tls_spring_http`  `missing_tls_spring_http_client`  `missing_tls_spring_http_client_reactive`  `missing_tls_spring_r2dbc_connection`  `missing_tls_spring_reactive_websocket`  `missing_tls_spring_resttemplate`  `missing_tls_spring_security_oauth`  `missing_tls_vertx` |
| `UNRESTRICTED_ACCESS_TO_FILE` | Kotlin | `unrestricted_access_to_file_core_kotlin`  `unrestricted_database_access_android`  `insecure_file_permission_android` |
| `UNSAFE_BASIC_AUTH` | Go | `basic_auth_enabled_core_go_net_http`  `basic_auth_enabled_gin` |
| `WEAK_PASSWORD_HASH` | Kotlin | `empty_salt_core_java`  `hardcoded_value_crypto_salt_core_java`  `weak_password_hash_core_java` |

The following Coverity Analysis checkers have been replaced by Sigma (SIGMA.*)
checks.

Table 2. Coverity Analysis checkers completely replaced by Sigma checks

| **Coverity checker name** | **Language** | **Sigma checker name** |
| --- | --- | --- |
| `CONFIG.BEEGO_CSRF_PROTECTION_DISABLED` | Go | `csrf_protection_disabled_beego`  `csrf_protection_disabled_beego_config` |
| `INSECURE_CSP` | Go | `csp_unsafe_eval_net_http`  `csp_unsafe_inline_net_http` |
| `INSECURE_FILE_PERMISSIONS` | Go | `insecure_file_permission_core_go_os` |
| `JSONWEBTOKEN_UNTRUSTED_DECODE` | Go | `jwt_no_claims_validation_core_go` |
| `UNSAFE_FUNCTIONALITY` | Go | `unsafe_functionality_unsafe` |

## Coverity Kotlin security checkers replaced with Sigma checkers

Kotlin security checkers in Coverity, including taint-flow checkers, have been been
replaced by Sigma checkers. In some cases, these are replaced by new Sigma checkers
(see the table above “Coverity Analysis checkers replaced by Sigma checks for
specific languages” for details). In other cases, these are replaced by Sigma
checkers with the same names.

Most existing Coverity dataflow defects will disappear and be reported as new Sigma
defects, which will need to be triaged again. New Kotlin security defects may be
reported.

With this change,

- Checker trust options such as `trust_filesystem` for taint
  flow checkers are no longer supported for Kotlin.
- The `ANDROID_CAPABILITY_LEAK` checker options
  `default_targetSdk` and
  `detect_targetSdk` no longer support Kotlin.
- The `BAD_CERT_VERIFICATION` checker option
  `check_ssl_session` has been removed entirely.
- The `HARDCODED_CREDENTIALS` checker option
  `report_empty_credentials` no longer supports Go,
  Kotlin, or Python.
- The `OS_CMD_INJECTION` checker option
  `ignore_command_as_array` no longer supports Kotlin. The
  related functionality is always enabled for Kotlin.
- The `OS_CMD_INJECTION` checker option
  `report_concat_errors` no longer supports Kotlin.
- The `SQLI` checker option `disable_heuristic`
  no longer supports Kotlin.
- The `SQLI` checker option
  `report_nosink_errors` no longer supports Kotlin. Note
  that the behavior is now turned on by default for Kotlin.
- The `UNENCRYPTED_SENSITIVE_DATA` checker options
  `report_from_cookie`,
  `report_from_database`,
  `report_from_filesystem`,
  `report_from_network`, and
  `report_from_url_connection` no longer support
  Kotlin.
- The `UNRESTRICTED_ACCESS_TO_FILE` checker option
  `api_level` no longer supports Kotlin.
- The `WEAK_PASSWORD_HASH` checker options
  `allow_sha2` and
  `report_weka_hashing_on_all_strings` no longer
  support Kotlin or Python.

## Sigma support on Linux x86_64 and ARM64

Sigma support on Linux x86_64 and Linux ARM64 now require glibc 2.28 or newer (an
increase from the previous requirement of glibc 2.23).

## Analysis Commands

- The `cov-analyze` command option
  `--enable-callgraph-metrics` has been deprecated.

## Checker and Checker Option Deprecations

- `CSRF`. Support for Python has been deprecated.
- `DISTRUSTED_DATA_DESERIALIZATION`. Checker-specific trust
  options have been deprecated for Go.
- `HARDCODED_CREDENTIALS`. The
  `report_empty_credentials` checker option has been
  deprecated for Go and Python and will be removed in a future release.
- `INSECURE_RANDOM`. The `report_no_sink_errors`
  checker option has been deprecated for Kotlin and will be removed in a
  future release.
- `MISSING_AUTHZ`. Support for Python has been deprecated.
- `MOBILE_ID_MISUSE`. The
  `report_all_mobile_id_uses` checker option has been
  deprecated for Kotlin.
- `RISKY_CRYPTO`. The following checker options have been
  deprecated for Go and Kotlin and will be removed in a future release:
  `assume_fips_mode`, `forbid_ciphersuite`,
  `forbid`, `minimum_tls`,
  `require_asymmetric`, `require_hash`,
  `require_symmetric`, and
  `usage_report`.
- `SESSION_FIXATION`. Checker-specific trust options have been
  deprecated for Go.
- `SQL_NOT_CONSTANT`. The `report_nosink_errors`
  checker option has been deprecated for Kotlin.
- `SUPPRESSED_ERROR`. This checker has been deprecated.
- `UNLOGGED_SECURITY_EXCEPTION`. The following checker options
  have been deprecated for Kotlin and will be removed in a future release:
  `enable_name_hueristics`,
  `enable_standard_output_logging`, and
  `security_exceptions`.
- `WEAK_PASSWORD_HASH`. The following checker options have been
  deprecated for Python and will be removed in a future release:
  `allow_sha2` and
  `report_weak_hashing_on_all_strings`.
- `XML_EXTERNAL_ENTITY`. Support for Go and Kotlin have been
  deprecated.
- `XML_INJECTION`. Checker-specific trust options have been
  deprecated for Go.
