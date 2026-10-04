---
title: "Upgrade considerations for 2026.9"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/upgrade-considerations-for-2026.9.html"
content_id: "uPk14mHrRjnYGoEeuYTLpg"
version: "2026.9"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-10-04T23:39:46.315607+00:00"
---

# Upgrade considerations for 2026.9

For information about deprecated and dropped support, other updates, known issues, and
fixed bugs, see the Coverity Release Notes.

## Coverity Checker Policy Enforcement

Coverity 2026.9 introduces Checker Policy Enforcement (CEP), a new opt-in feature.
No policies are configured by default after upgrading. Existing scan workflows are
not affected unless an administrator creates and uploads a policy in Coverity
Connect.

If you plan to use CEP after upgrading, note the following:

- The default non-compliance handling is **Reject**. Scans that do not satisfy
  the effective policy will be rejected at commit time. If your organization
  prefers a warning instead, configure non-compliance handling to **Warn and
  Accept** before uploading a policy. See Configuring non-compliance handling.
- The default precedence is **Top Down**, meaning the global policy takes
  priority over project policies when conflicts exist. Review the precedence
  setting before assigning project-level policies. See Configuring checker policy precedence.
- No migration is required from previous releases. CEP is a new capability with
  no replacement of existing functionality.

For setup instructions, see Coverity Checker Policy Enforcement overview.

## cov-link removed

Note:
As of Coverity 2026.9, the `cov-link` command has been removed. To resolve
duplicate function call linkage for C/C++, use the `--tu-pattern` option to
`cov-analyze` instead. See Getting linkage information.

## **Coverity Analysis checkers replaced by Sigma checks in 2026.9.0**

A number of Coverity Analysis checkers have been either completely or partially
replaced by Sigma (SIGMA.*) checks.

The following Coverity Analysis checkers have been replaced by new Sigma (SIGMA.*)
checks for all languages, and the corresponding Coverity Analysis checker no longer
exists.

Table 1. Coverity Analysis checkers completely replaced by Sigma checks for all
languages

| **Coverity checker name** | **Sigma checker name** |
| --- | --- |
| `HOST_HEADER_VALIDATION_DISABLED` | `host_header_validation_disabled_dotenv` |
| `MOBILE_ID_MISUSE` | `mobile_id_misuse_android` |

The following Coverity Analysis checkers have been replaced by new Sigma (SIGMA.*)
checks for specific languages.

Table 2. Coverity Analysis checkers replaced by Sigma checks for specific
languages

| **Coverity checker name** | **Language** | **Sigma checker name** |
| --- | --- | --- |
| `INSECURE_RANDOM` | Python | `insecure_random_core_python` |
| `BAD_CERT_VERIFICATION` | Python | `certificate_verification_disabled_core_python_requests, certificate_verification_disabled_core_python_requests_adapters, certificate_verification_disabled_core_python_requests_session` |
| `CONFIG.ANDROID_GRADLE_OBFUSCATION_NOT_ENABLED` | Gradle, Kotlin | `obfuscation_not_enabled_gradle_android` |
| `INSECURE_RANDOM` | Kotlin | `insecure_random_core_kotlin` |
| `PREDICTABLE_RANDOM_WITH_SEED` | Kotlin | `insecure_random_seed_core_kotlin` |
| `UNLOGGED_SECURITY_EXCEPTION` | Kotlin | `unlogged_security_exception_core_java` |
| `WEAK_PASSWORD_HASH` | Python | `weak_password_hash_django_config_settings` |
| `INSECURE_COOKIE` | Python | `missing_httponly_attribute_csrf_cookie_django_config_settings, missing_httponly_attribute_session_cookie_django_config_settings, missing_samesite_attribute_csrf_cookie_django_config_settings, missing_samesite_attribute_session_cookie_django_config_settings, missing_secure_attribute_csrf_cookie_django_config_settings, missing_secure_attribute_session_cookie_django_config_settings` |
| `WEAK_URL_SANITIZATION` | Python | `weak_url_sanitization_core_python` |

The following Coverity Analysis checkers have been replaced by Sigma for specific
languages, but have the same names.

Table 3. Coverity Analysis checkers replaced by Sigma checks for specific languages,
with the same names

| **Coverity checker name** | **Language** |
| --- | --- |
| `HARDCODED_CREDENTIALS` | Python |
| `MISSING_PERMISSION_FOR_BROADCAST` | Kotlin |
| `RISKY_CRYPTO` | Kotlin |
| `SOCKET_ACCEPT_ALL_ORIGINS` | Go |
| `SQL_NOT_CONSTANT` | Kotlin |
| `XML_INJECTION` | Kotlin |

For the following Coverity Analysis checkers, additional defects may be reported
because Sigma also reports defects using the same checker names.

Table 4. Coverity Analysis checkers that may report additional defects in
Sigma

| **Coverity checker name** | **Language** |
| --- | --- |
| `HARDCODED_CREDENTIALS` | Go |
| `NOSQL_QUERY_INJECTION` | Go |
| `TEMPLATE_INJECTION` | Go |
| `XSS` | Go |
| `LOCALSTORAGE_MANIPULATION` | JavaScript, TypeScript |
| `SESSIONSTORAGE_MANIPULATION` | JavaScript, TypeScript |

## Changes related to Coverity Kotlin support

- As of Coverity 2026.6, most Kotlin security checkers in Coverity, including
  taint-flow checkers, were replaced by Sigma checkers. With this release, all
  remaining security checkers (except `XML_EXTERNAL_ENTITY`)
  have been replaced by Sigma checkers, as listed in the tables above. The
  `XML_EXTERNAL_ENTITY` checker no longer supports
  Kotlin.
- All Coverity quality checkers have been removed.
- Support for running `cov-make-library` to customize Kotlin
  analysis has been removed.

## Checker and checker option changes

- `HARDCODED_CREDENTIALS` - The
  `report_empty_credentials` checker option has been
  removed for Python.
- `RISKY_CRYPTO` - The following checker options have been
  removed for Kotlin: `assume_fips_mode`,
  `forbid_ciphersuite`, `forbid`,
  `minimum_tls`, `require_asymmetric`,
  `require_hash`, `require_symmetric`, and
  `usage_report`. For Kotlin, the usage report will always
  be generated in the intermediate directory at the location
  <idir>/output/crypto-report.csv.
- `SQL_NOT_CONSTANT` - The `report_nosink_errors` checker
  option has been removed for Kotlin. Additionally, because the Kotlin
  implementation of this checker is provided by Sigma, it is not affected by
  the `enabled-audit-mode` option.

## Sigma merge key fix

- Fixed an issue where some checkers incorrectly set merge keys, causing
  multiple instances of a defect to be merged into one. These checkers now
  report vulnerabilities individually, allowing each instance to be triaged
  and resolved separately. As a result, more defects may be reported for the
  affected checkers. This applies to the following checkers:
  - `missing_global_exception_handler`
  - `missing_httponly_attribute`
  - `container_cpu_share_unlimited`
  - `default_service_account_enabled`
  - `graphiql_enabled`

## `SINGLETON_RACE` checker removed

The `SINGLETON_RACE` checker has been removed from Coverity. This
checker was previously deprecated and superseded by
`UNLOCKED_ACCESS`.
