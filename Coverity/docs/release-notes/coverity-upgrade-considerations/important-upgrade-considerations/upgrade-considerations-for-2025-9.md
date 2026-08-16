---
title: "Upgrade considerations for 2025.9"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrade-considerations-for-2025.9.html"
content_id: "3udnMIJdPpdbRwqU3f~N8Q"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:47.608257+00:00"
---

# Upgrade considerations for 2025.9

For information about deprecated and dropped support, other updates, known issues, and
fixed bugs, see "Coverity 2025.9.0 Release Notes" (and the sections for associated hot
fixes) in the Coverity 2026.6.0 Release Notes Archive.

For the list of Sigma checkers disabled by default when running Coverity Analysis 2025.9,
see "Checkers disabled in Sigma when running Coverity Analysis" in the Coverity 2026.6.0 Checker Reference.

CAUTION:

When you upgrade Coverity Analysis, all previous settings are
overwritten. All checkers listed in the "Sigma checks
disabled by default in Coverity 2025.9" table in the Coverity 2026.6.0 Checker Reference will be disabled by default in Coverity Analysis
2025.9, regardless of their enablement status in previous installations.

## Coverity Analysis checkers replaced by Sigma checks for specific languages

Table 1.

| **Coverity Analysis checker** | **Languages removed from Coverity Analysis checker** | **Sigma checks replacing this Coverity checker** |
| --- | --- | --- |
| `INSECURE_COOKIE` | Go, Go Application Config | `missing_httponly_attribute_session_cookie_gorilla_sessions`  `missing_samesite_attribute_revel_config`  `missing_samesite_attribute_session_cookie_gorilla_sessions`  `missing_secure_attribute_revel_config`  `missing_secure_attribute_session_cookie_gorilla_sessions` |

## Coverity Analysis checkers completely replaced by Sigma checks

Table 2.

| **Coverity checker name** | **Sigma checks replacing this Coverity checker** |
| --- | --- |
| `CORS_MISCONFIGURATION` | `cors_with_credentials_all_origin_beego` `cors_with_credentials_all_origin_core_go_net_http`  `cors_with_credentials_all_origin_gin`  `cors_with_credentials_all_origin_gorilla_handlers`  `cors_with_credentials_all_origin_rs`  `cors_with_credentials_http_origin_beego`  `cors_with_credentials_http_origin_core_go_net_http`  `cors_with_credentials_http_origin_gin`  `cors_with_credentials_http_origin_gorilla_handlers`  `cors_with_credentials_http_origin_rs` |
| `INSECURE_NETWORK_BIND` | `insecure_network_bind_beego`  `insecure_network_bind_core_go_net`  `insecure_network_bind_go_gin` |
| `OAUTH2_MISCONFIGURATION` | `misconfigured_oauth2_go_core_oauth2` |
| `STATIC_API_KEY` | `static_non_expiring_token_core_go_oauth2` |
| `CONFIG.COOKIE_SIGNING_DISABLED` | `unsafe_session_storage_revel` |

## Custom Domains

For Coverity cloud deployments, this release introduces a new Coverity Connect
property (`extraProperty`) that you must provide when using custom
domains for storage service configurations. For further information, refer to the
*Coverity Cloud Deployment Administrator and User Guide.*

## Checkers

- The INCOMPLETE_DEALLOCATOR checker is now enabled by default.
- The INCOMPLETE_DEALLOCATOR checker option `escape_is_release`
  has been changed to default `true`, and
  `false` at aggressiveness level high. Formerly, the
  default was `false` and unaffected by aggressiveness.
- A new checker option
  `report_unsigned_underflow_cast_to_signed` has been added
  to the INTEGER_OVERFLOW checker. This option is enabled by default, but it
  can be disabled with the appropriate switch.

## Coverity CLI

How the Coverity CLI interprets the files configuration has changed. Instead of the
files configuration only applying to the capture of files via buildless capture,
this has changed so that the files configuration applies to the capture of files via
build and buildless capture. An implication of this is that a set of default
exclusions will also be applied.
