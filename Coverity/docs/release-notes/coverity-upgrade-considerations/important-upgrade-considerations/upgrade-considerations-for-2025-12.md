---
title: "Upgrade considerations for 2025.12"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrade-considerations-for-2025.12.html"
content_id: "MHcHDJkdAp0YiMddGdneNA"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:46.961505+00:00"
---

# Upgrade considerations for 2025.12

For information about deprecated and dropped support, other updates, known issues, and
fixed bugs, see "Coverity 2025.12.0 Release Notes" (and the sections for associated hot
fixes) in the Coverity 2026.6.0 Release Notes Archive.

For the list of Sigma checkers disabled by default when running Coverity Analysis
2025.12, see ["Checkers disabled in Sigma when running Coverity
Analysis"](https://documentation.blackduck.com/bundle/coverity-docs-2025.12/page/checker-ref/checkers/S/sigma._checkers.html#d100634e144) in the [*Coverity 2025.12.0 Checker
Reference*](https://documentation.blackduck.com/bundle/coverity-docs-2025.12/page/webhelp-files/checkerref_start.html).

CAUTION:

When you upgrade Coverity Analysis, all previous settings are
overwritten. All checkers listed in the [" Sigma checks disabled by default in Coverity
2025.12"](https://documentation.blackduck.com/bundle/coverity-docs-2025.12/page/checker-ref/checkers/S/sigma._checkers.html#SIGMA_checkers__section_disabled_sigma_checkers) table in the [*Coverity 2025.12.0 Checker Reference*](https://documentation.blackduck.com/bundle/coverity-docs-2025.12/page/webhelp-files/checkerref_start.html)
will be disabled by default in Coverity Analysis 2025.12, regardless of their enablement
status in previous installations.

## Coverity Analysis checkers replaced by Sigma checks for specific languages

|  |  |  |
| --- | --- | --- |
| **Coverity checker name** | **Languages removed from Coverity Analysis checker** | **Sigma checks replacing this Coverity checker** |
| `CORS_MISCONFIGURATION_AUDIT` | Go | `cors_expose_sensitive_data_beego`  `cors_expose_sensitive_data_core_go_net_http`  `cors_expose_sensitive_data_gin`  `cors_expose_sensitive_data_go_aws_sdk`  `cors_expose_sensitive_data_gorilla_handlers`  `cors_expose_sensitive_data_rs`  `cors_no_credentials_permissive_origin_beego`  `cors_no_credentials_permissive_origin_core_go_net_http`  `cors_no_credentials_permissive_origin_gin`  `cors_no_credentials_permissive_origin_go_aws_sdk`  `cors_no_credentials_permissive_origin_gorilla_handlers`  `cors_no_credentials_permissive_origin_rs`  `cors_permissive_methods_beego`  `cors_permissive_methods_core_go_net_http`  `cors_permissive_methods_gin`  `cors_permissive_methods_go_aws_sdk`  `cors_permissive_methods_gorilla_handlers`  `cors_permissive_methods_rs` |
| `INSECURE_COMMUNICATION` | Go | `missing_tls_beego`  `missing_tls_core_go_database_sql`  `missing_tls_core_go_net`  `missing_tls_core_go_net_http`  `missing_tls_gin` |

## Coverity 2025.12.0 checkers completely replaced by Sigma checks

|  |  |
| --- | --- |
| **Coverity checker name** | **Sigma checks replacing this Coverity checker** |
| `ANONYMOUS_DB_CONNECTION` | `anonymous_access_enabled_go_database` |
| `EXPOSED_DIRECTORY_LISTING` | `exposed_directory_listing_beego`  `exposed_directory_listing_beego_config`  `exposed_directory_listing_gin` |

## Checkers

- Support for Python quality checkers has been deprecated.
- Support for Go quality checkers has been deprecated.
- Support for JavaScript/TypeScript has been deprecated.
- Support for Detekt has been deprecated.
- Support for SpotBugs has been deprecated.
