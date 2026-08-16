---
title: "Polaris release notes"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/polaris-release-notes.html"
content_id: "JqRc8bkNtPpqwwe5LFqzfA"
product_key: "polaris-platform-latest"
section: "Reference"
scraped_at: "2026-08-12T19:57:53.193267+00:00"
content_hash: "d5e9e54cc98b7826acff8d8c716284934bacb8c63058a5ee756ab0db1b7cc3b3"
---

# Polaris release notes

Everything that's new in Polaris

## August 2026

- **Important**: The sunset date for deprecated endpoints in Polaris APIs was extended to **November 24, 2026, at 05:00:00 GMT**. Deprecated endpoints in Polaris APIs, versions of the Bridge CLI older than 3.6.0, and versions of Code Sight older than 2025.4.0 will stop functioning on November 24, 2026. To avoid failures:
  - Update your API scripts before November 24, 2026
  - Upgrade to Bridge CLI 3.6.0 (or newer) before November 24, 2026
  - Upgrade to Code Sight 2025.4.0 (or newer) before November 24, 2026

  See [EXTENDED DEADLINE to November 24, 2026 for Deprecated Polaris API Endpoints](https://community.blackduck.com/s/question/0D5Ul00000nOAnAKAW/announcement-extended-deadline-to-november-24-2026-for-deprecated-polaris-api-endpoints) in Black Duck Community, the [API reference guide](https://polaris.blackduck.com/developer/default/documentation), [Download Bridge CLI](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/5cc6965a2886bd9786bae37cd8607e8e.topic), and [Installing Code Sight](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/cda9d356f5606c3d361c83423b60679d.topic) for more information.
- The fAST Dynamic checkers list has been updated to reflect new and recent changes:
  - Added entries for `AUTHLEAK`, `NOFIELD`, `CAPTCHA`, and `NEXTJSBYPASS`. These checkers were already available, and vulnerabilities they find appear in DAST test results and the Developer Detail Dynamic report.
  - Updated several existing entries with up-to-date information including CWE™ codes.
  - Updated the class names of the following checkers: `AUTHBYPASS`, `EXPR`, `INSOBJ`, `TOMJSPDISC`.
  - Changed the Checker Code for **API Broken Object Level Authorization** from `APIBA` to `BOLA`.
- Enhancements have been made to Polaris service accounts. You can now:
  - Edit a service account by changing its role type (global or application-level), role, or assigned applications.
  - Regenerate a service account to renew its access token.
  - Search for service accounts by name.

  The Service Accounts page displays a warning if a service account expires in seven days or less, with a link to regenerate. See [Edit or regenerate a Polaris service account](../how-to/service-accounts-for-polaris/edit-or-regenerate-a-polaris-service-account.md) for more information.
- The issue tracking integration for Jira Cloud now includes enhanced options for customizing how Polaris issue data is exported to Jira tickets. You can now:
  - Customize ticket titles using Polaris variable placeholders (application name, project name, severity, and issue type).
  - Map Polaris fields to Jira fields (including custom Jira fields) for one-way export or bi-directional synchronization.
  - Toggle and reorder the Polaris issue details included in the Jira ticket description.

  See Create integration options for Jira for more information.

## July 2026

- Polaris now supports SAST Fix Pull Requests, enabling teams to automatically generate AI-assisted code fixes and submit them directly to their source code repositories. Fix PRs can be created on demand from an issue or automatically through a new issue policy action whenever an eligible SAST finding with an AI-generated recommendation violates a policy rule. Each pull request includes vulnerability details, links back to the Polaris issue for additional context, and the proposed code changes with line-level recommendations. Developers can review, test, and merge fixes directly within their existing SCM workflow, accelerating remediation while reducing manual effort. Detailed documentation will be available in a future update.

  Important: Black Duck® Bridge 4.5.0 or later is required to use this feature.
- Polaris now supports container image analysis for Docker and OCI images, enabling software composition analysis (SCA) of deployed container artifacts in addition to source code and package manifests. Detailed documentation will be available in a future update.

  Important: Black Duck® Bridge 4.5.0 or later is required to use this feature.
- Polaris now allows Organization Admins to search and update existing accounts, manage role and application assignments, monitor token expiration, and quickly regenerate credentials. Detailed documentation will be available in a future update.
- Polaris supports Black Duck® Bridge CLI 4.5.0.
- Polaris supports Rapid Scan Static (Sigma) 2026.6.1. This version has the following changes:
  - **General enhancements and changes:**
    - Validated support for Kotlin 2.4.0.
  - **New checks and hardcoded secrets patterns:**
    - New check `cors_expose_sensitive_data_micronaut` added for Java, Kotlin.
    - New check `cors_no_credentials_permissive_origin_micronaut` added for Java, Kotlin.
    - New check `cors_preflight_age_too_long_micronaut` added for Java, Kotlin.
    - New check `cors_with_credentials_all_origin_micronaut` added for Java, Kotlin.
    - New check `cors_with_credentials_http_origin_micronaut` added for Java, Kotlin.
    - New check `cors_with_credentials_null_origin_micronaut` added for Java, Kotlin.
    - New check `cors_with_credentials_subdomain_origin_micronaut` added for Java, Kotlin.
    - New check `host_header_validation_disabled_dotenv` added for Dotenv.
    - New check `metadata_verification_disabled_gradle` added for XML.
    - New check `null_cipher_used_bouncy_castle` added for Java, Kotlin, Scala.
    - New check `outdated_version_used_gradle` added for Properties.
    - New check `socket_accepts_all_origins_gorilla` added for Go.
    - New check `sql_not_constant_core_kotlin` added for Kotlin.
    - New check `xml_injection_core_kotlin` added for Kotlin.
    - New hardcoded secrets pattern `Laravel Cashier Stripe API key` added.
    - New hardcoded secrets pattern `PHP env() hardcoded value` added.
    - New hardcoded secrets pattern `Swift Crypto Key` added.
- Polaris issue tracking integrations now support two-way triage status synchronization for Jira Cloud. When configured, triage status changes in Polaris automatically update the status of linked Jira tickets, and status changes in Jira automatically update the triage status of linked Polaris issues. Optionally, Polaris fix-by dates and Jira due dates can be kept in sync. Sync events appear in each issue's triage history, attributed to the sync rather than to a specific user.

  See Automatically close tickets and synchronize triage statuses and Create integration options for Jira for more information.
- You can now share copies of your saved dashboard filters and report configurations with other users and groups in your organization. These shared copies have the following characteristics:
  - Most users can only share with people and groups that have the same set of applications as themselves. Org admins can share with any user or group, but doing this will allow the recipient to see all configuration and filter values in the shared resource, even if they don't have access to what's mentioned. The admin will be warned of this before the resource is shared.
  - Distinct from the original, so making changes to a saved filter or configuration won't affect anyone else who has a copy of it.
  - The name of the copy includes the name of the person who shared it. Also, if the shared copy has the same name as one of your existing resources, the end of its name will have a distinguishing instance number. For example, a shared filter might be named `DAST data for July - shared by Bob Slydell - 2`.
  - **Filters only:** Initially appear at the end of the recipient's Saved Filters list, but can be reordered like any other saved filters.
  - **Report configurations only:** Exclude any schedules associated with the original configuration.
- Polaris supports Black Duck® Detect 11.4.2. It includes the following changes:
  - Added support for Apache Ivy projects in code upload and SCM integration workflows using the Ivy Build Parse detector.
  - Added support for the Ivy CLI detector for Apache Ivy projects in Bridge CLI, providing high-accuracy dependency detection. Requires Apache Ant 1.6.0+ and Ivy 2.4.0+.
  - Added support for Go Modules projects in code upload and SCM integration workflows using the Go Mod File detector.
  - Added support for OPAM (OCaml).
  - Added support for Rush (Node.js).
  - Added support for Setuptools (Python).
  - Added support for UV (Python).
  - Extends Cargo support to 1.85.1.
  - Extends Conan support to 2.20.1.
  - Extends Go Modules support to 1.25.0.
  - Extends Gradle support to 9.0.0.
  - Extends Maven support to 3.9.11.
  - Extends npm support to 11.5.2 (Node.js 24.7.0).
  - Extends NuGet support to 6.8.1.
  - Extends pip support to 25.2.0 (with Pipenv 2024.0.1).
  - Extends pnpm support to 10.32.1.
  - Extends RubyGems support to 3.7.1.
  - Extends SBT support to 1.11.3.
  - Extends Yarn support to 4.9.4.

  For a verbose summary of changes from Detect 10.4.0 to 11.4.2, see the [Detect release notes](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/0d19240b926f87f81ef55633a391116a.topic&Version=latest).
- Polaris now supports Coverity 2026.6.0. It includes the following changes:
  - Added support for Java 26.
  - Added support for Go 1.26.
  - Added support for Visual Studio 2026 capture.
  - Added support for Clang 20.1, 21.1, 22.1.
  - Added support for Oracle/Open JDK 26.
  - Updated Linux runtime requirements to glibc 2.28 or newer for Linux x86\_64 and Linux ARM64 environments.
  - Support for Go 1.25 is deprecated and will be removed in a future release.
  - Support for Oracle/Open JDK 17 is deprecated and will be removed in a future release.
  - Support for macOS 14 is deprecated and will be removed in a future release.
  - Support for Go 1.24 was removed.
  - Support for FreeBSD 13 was removed.
  - **Checker Information:**
    - Added a new AI-augmented `IDOR` checker (beta) via the Rapid Scan Static (Sigma) engine.
    - Improved source file mapping for `.cshtml` files to correctly link issues to source locations.
    - Updated Spring Framework models (Phase 4) to improve analysis of modern Java applications, including improved models for the `SCRIPT_CODE_INJECTION` checker.
    - Removed the interdependence between the `SQLI` and `SQL_NOT_CONSTANT` checkers to reduce false negatives and improve SQL injection detection reliability.
    - Enhanced documentation and CWE mapping for the `URL_MANIPULATION` checker. Issues are now mapped to CWE-284.
  - The following Coverity Analysis checkers have had all support for the specified language(s) completely replaced by Sigma checks. Any references to these checkers in `coverity.yml` configuration files should be updated.

    | Coverity Analysis checker | Language | Sigma checks that replace this Coverity checker |
    | --- | --- | --- |
    | `ANDROID_CAPABILITY_LEAK` | Kotlin | `missing_permission_check_android` |
    | `BAD_CERT_VERIFICATION` | Go, Java, Kotlin | `certificate_verification_disabled_crypto_ssh`  `certificate_verification_disabled_crypto_tls`  `certificate_verification_disabled_webview_android` |
    | `CONFIG.BEEGO_CSRF_PROTECTION_DISABLED` | Go | `csrf_protection_disabled_beego`  `csrf_protection_disabled_beego_config` |
    | `CONFIG.UNSAFE_SESSION_TIMEOUT` | Go | `excessive_session_lifetime_beego`  `excessive_session_lifetime_gin`  `excessive_session_lifetime_gorilla` |
    | `HARDCODED_CREDENTIALS` | Kotlin | `hardcoded_credentials_core_kotlin` |
    | `IMPLICIT_INTENT` | Kotlin | `implicit_intent_core_kotlin` |
    | `INSECURE_COMMUNICATION` | Kotlin | `missing_tls_apache_commons_io`  `missing_tls_apache_datasource`  `missing_tls_apache_http`  `missing_tls_spring_boot_elasticsearch`  `missing_tls_core_java_sql`  `missing_tls_datastax_driver`  `missing_tls_dom4j_io`  `missing_tls_dom4j_jaxb`  `missing_tls_guava_resources`  `missing_tls_jackson_core`  `missing_tls_jackson_objectmapper`  `missing_tls_jackson_objectreader`  `missing_tls_mongodb`  `missing_tls_okhttp`  `missing_tls_slick_play_database`  `missing_tls_spring_boot_couchbase`  `missing_tls_spring_boot_datasource`  `missing_tls_spring_boot_flyway`  `missing_tls_spring_boot_influx`  `missing_tls_spring_boot_neo4j`  `missing_tls_spring_boot_r2dbc`  `missing_tls_spring_data_mongodb`  `missing_tls_spring_data_r2dbc`  `missing_tls_spring_datasource`  `missing_tls_spring_http`  `missing_tls_spring_http_client`  `missing_tls_spring_http_client_reactive`  `missing_tls_spring_r2dbc_connection`  `missing_tls_spring_reactive_websocket`  `missing_tls_spring_resttemplate`  `missing_tls_spring_security_oauth`  `missing_tls_vertx` |
    | `INSECURE_CSP` | Go | `csp_unsafe_eval_net_http`  `csp_unsafe_inline_net_http` |
    | `INSECURE_FILE_PERMISSIONS` | Go | `insecure_file_permission_core_go_os` |
    | `JSONWEBTOKEN_UNTRUSTED_DECODE` | Go | `jwt_no_claims_validation_core_go` |
    | `UNRESTRICTED_ACCESS_TO_FILE` | Kotlin | `unrestricted_access_to_file_core_kotlin`  `unrestricted_database_access_android`  `insecure_file_permission_android` |
    | `UNSAFE_BASIC_AUTH` | Go | `basic_auth_enabled_core_go_net_http`  `basic_auth_enabled_gin` |
    | `UNSAFE_FUNCTIONALITY` | Go | `unsafe_functionality_unsafe` |
    | `WEAK_PASSWORD_HASH` | Kotlin | `empty_salt_core_java`  `hardcoded_value_crypto_salt_core_java`  `weak_password_hash_core_java` |

    Note: All of these Coverity checkers have had all support for the specified language(s) completely replaced by the corresponding Sigma checkers. Of these, `CONFIG.BEEGO_CSRF_PROTECTION_DISABLED`, `INSECURE_CSP`, `INSECURE_FILE_PERMISSIONS`, `JSONWEBTOKEN_UNTRUSTED_DECODE`, and `UNSAFE_FUNCTIONALITY` have been completely removed from Coverity for all languages supported by the specific checker.
- Polaris supports Rapid Scan Static (Sigma) 2026.6.0. This version has the following changes:
  - **General enhancements and changes:**
    - Added support for parsing Python code in Jupyter Notebook (.ipynb) files, enabling detection of hardcoded LLM API keys and other sensitive values within notebook cells.
    - Sigma will no longer analyze Kotlin code that is part of JUnit or `kotlin.test` tests. As a result, issues from hardcoded secrets, API checks, or dataflow checks will not be reported.
    - Validated support for Dart 3.12.
  - **New checks and hardcoded secrets patterns:**
    - New check `basic_auth_enabled_micronaut` added for Java, Kotlin.
    - New check `cors_expose_sensitive_data_micronaut_properties` added for Properties, YAML.
    - New check `cors_expose_sensitive_data_micronaut_yaml` added for Properties, YAML.
    - New check `cors_no_credentials_permissive_origin_micronaut_properties` added for Properties, YAML.
    - New check `cors_no_credentials_permissive_origin_micronaut_yaml` added for Properties, YAML.
    - New check `cors_preflight_age_too_long_micronaut_properties` added for Properties, YAML.
    - New check `cors_preflight_age_too_long_micronaut_yaml` added for Properties, YAML.
    - New check `cors_with_credentials_all_origin_micronaut_properties` added for Properties, YAML.
    - New check `cors_with_credentials_all_origin_micronaut_yaml` added for Properties, YAML.
    - New check `cors_with_credentials_http_origin_micronaut_properties` added for Properties, YAML.
    - New check `cors_with_credentials_http_origin_micronaut_yaml` added for Properties, YAML.
    - New check `cors_with_credentials_null_origin_micronaut_properties` added for Properties, YAML.
    - New check `cors_with_credentials_null_origin_micronaut_yaml` added for Properties, YAML.
    - New check `cors_with_credentials_subdomain_origin_micronaut_properties` added for Properties, YAML.
    - New check `cors_with_credentials_subdomain_origin_micronaut_yaml` added for Properties, YAML.
    - New check `empty_key_derivation_password_swift` added for Swift.
    - New check `missing_tls_micronaut_http` added for Java, Kotlin.
    - New check `mobile_id_misuse_android` added for Java, Kotlin.
    - New check `weak_password_hash_django_config_settings` added for Python.
    - New hardcoded secrets pattern `AlamoFire Authorization Value` added.
    - New hardcoded secrets pattern `FMDB Key` added.
    - New hardcoded secrets pattern `FirebaseAuth Confirm Password Reset` added.
    - New hardcoded secrets pattern `Foundation URL Components Password` added.
    - New hardcoded secrets pattern `Network Extension Password` added.
    - New hardcoded secrets pattern `Steel Crypt hardcoded salt` added.
    - New hardcoded secrets pattern `flutter_inappwebview AJAX request secret` added.
    - New hardcoded secrets pattern `flutter_inappwebview HTTP auth secret` added.
    - New hardcoded secrets pattern `flutter_inappwebview URL credential secret` added.
    - New hardcoded secrets pattern `flutter_inappwebview fetch request credential secret` added.
    - New hardcoded secrets pattern `httplib2 Proxy Password` added.
- Organization Admins, Organization Application Managers, and Application Admins can now move SAST & SCA projects between applications. You can move a single project, a selection of projects, or all the projects in an application at once. Test results, triage data, issues, scans, policies, and branches are all preserved after the move. When moving, you choose whether projects should inherit settings from the destination application or retain their existing settings.

  Note: You can only move projects between applications with active team member (concurrent) subscriptions. DAST projects cannot be moved.

  See [Move projects between applications](../how-to/move-projects-between-applications.md) for more information.
- Organization administrators can now define default issue, component, pull/merge request, and test scheduling policies under My Organization > Policies. New applications, projects, and branches inherit default policies automatically. Users with appropriate permissions can override default policies in application, project, or branch settings (and can restore default policy assignments later on). Updates to default policies propagate automatically to all applications, projects, and branches that have not been customized.

  See [Manage your default policies](../how-to/create-and-manage-policies/manage-your-default-policies.md) and Create and manage Policies for more information.

  Important notes on this feature:

  - Policy assignments configured before this feature is enabled are preserved.
  - When this feature is enabled, Polaris automatically applies policies to new branches based on branch type.
    - Default branches receive all inherited policy types.
    - Non-default branches receive only pull/merge request policies by default.

    See [Control how default policies are applied to branches](../how-to/create-and-manage-policies/manage-your-default-policies/control-how-default-policies-are-applied-to-branches.md) for more details on how to change this behavior.
  - When creating or editing a branch, issue, component, and pull/merge request policies are all disabled by default. For each policy type, users can select Use Project Policies to inherit the policies assigned at the project level. This is change from the previous behavior where only pull/merge request policies were automatically enabled by default for new branches.

    See [Create and manage branches in a project](../how-to/create-and-manage-branches-in-a-project.md) for more information.
  - When bulk-onboarding SCM repositories, Polaris no longer includes a manual policy assignment step. Now, projects created during bulk onboarding automatically inherit your organization's default policies.

    See [Connect Polaris to Multiple SCM Repositories](../how-to/connect-polaris-to-multiple-scm-repositories.md) for more information.
- You can now enable AI-driven BOLA (Broken Object Level Authorization) annotation in DAST API projects. When creating or configuring such a project, you can select the new Auto-annotate object visibility in API spec checkbox to turn on auto-annotation. The project must be assigned at least two sets of valid authentication credentials to run this type of test.

  After running a test for the enabled project, you will find a file named `postprocessed_spec.json` in the downloaded .zip volume. This file differs from the `original_spec.json` file by also including the auto-generated BOLA annotations.

  Within the UI, you'll be able to identify BOLA issues by their type: **API Broken Object Level Authorization**.
- Polaris supports Black Duck® Bridge CLI 4.4.0.
- Polaris now supports issue risk scoring for SCA issues. Issue risk scoring uses configurable risk factors — CISA KEV (whether a vulnerability appears on the CISA Known Exploited Vulnerabilities list) and Reachability (whether vulnerable code is actually reachable in your application) — to adjust an issue's base risk score up or down. You can view a breakdown of how each factor affected an issue's score in the new Risk Score Breakdown panel in the Issue Details tab. Issue risk factors are enabled and configured in My Organization > Risk Scoring, alongside existing application risk factors.

  See [Risk scoring in Polaris](../how-to/risk-scoring-in-polaris.md) and Enable risk scoring for more information.

## June 2026

- You can now set up a connection to sync vulnerabilities from your Black Duck SCA instance to Polaris, either daily or on demand. Synced vulnerabilities appear as third-party issues in Polaris, where you can use them with standard features like reports and dashboards, issue policies, application risk scoring, and Black Duck Assist.

  When you sync a connection, projects and versions in Black Duck SCA are mapped to applications, projects, and branches in Polaris automatically. Data sync is one-way only and can be started for the whole organization or for individual mapped projects.

  To configure a Black Duck SCA connection, select My Organization > Integrations. In the Black Duck SCA section, select New Connection and enter the requested details.

  See [Import issues from Black Duck SCA](../how-to/import-issues-from-black-duck-sca.md) for more information.
- Organization Administrators can now control which dashboard sets are available to users in their tenant. In My Organization > Dashboards, two options are available:
  - Polaris (default) - Allows access to all dashboards.
  - Black Duck SCA - Allows access to the Table - Component Search and Table - License Search dashboards only.

  To populate the Black Duck SCA dashboards with issue data, sync vulnerabilities from Black Duck SCA to Polaris using the new Black Duck SCA connection feature.
- Polaris supports Fail PR, which enables pull request policies to automatically warn or block merges when a PR scan detects policy violations. When a PR matches the criteria of an assigned pull/merge request policy that includes the Fail Pull/Merge Request action, Polaris posts a warning in the SCM. If the Block setting is also enabled at the organization or application level under Analysis > SCM Event-based Test Automation, the merge is blocked until the violations are resolved or the setting is changed. Fail PR is supported for Azure DevOps (Premium), Bitbucket Cloud (Premium), GitHub (public repositories only), GitHub Enterprise, and GitLab SaaS (Premium). GitLab and Bitbucket require additional repository-level settings before blocking is active.

  See [Fail Pull Requests (Fail PR)](../how-to/fail-pull-requests-fail-pr.md) for more information.
- Polaris supports secure tunnel connectivity when integrating self-hosted GitHub and GitHub Enterprise Server repositories hosted in a private network. During the repository integration workflow, select Entry Point URL is in a private network and choose a tunnel from the dropdown to route the connection through your secure tunnel. See GitHub Enterprise Server (single Polaris project) and GitHub Enterprise Server (bulk onboarding) for more information.
- Polaris supports tenant-wide secure tunnels — named, reusable TLS connections you create once in My Organization > Secure Tunnels and associate with multiple internal DAST projects. This replaces the need to create a separate project-specific tunnel for each DAST target from the Bridge CLI.

  To use a tenant-wide tunnel, run Bridge CLI 4.3.0 or later from a machine inside your private network, passing your Polaris access token and tunnel name. Once the connection is established, you can start DAST tests on any internal project linked to that tunnel from the Polaris UI, API, or a separate Bridge CLI instance. The tunnel stays active until you stop it, and can be shared across concurrent scans. See [Add and manage secure tunnels in the Polaris UI](../how-to/add-and-manage-secure-tunnels-in-the-polaris-ui.md) for more information.
- Polaris supports Black Duck® Bridge CLI 4.3.0. Now, issues captured in signature analysis tests are included in SARIF output (along with issues captured in package manager tests).
- Polaris supports Rapid Scan Static (Sigma) 2026.5.0. This version has the following changes:
  - **General enhancements and changes:**
    - Validated support for Swift 6.3.
    - Added the `analyze/checkers/cra` configuration setting to allow enablement of the EU Cyber Resilience Act (EU-CRA) checker set in Sigma via `coverity.yml`.
    - Added a new checker set for "CWE Top 25 2025".
  - **New checks and hardcoded secrets patterns:**
    - New check `data_mask_obfuscation_disabled_android_xml` added for XML.
    - New check `idor_core_javascript` added for JavaScript. This is a beta version of the check. Refer to [Configuring the AI-augmented SAST checker plug-in](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/configuring-the-ai-augmented-sast-checker-plug-in.html) for information on how to enable and configure the check.
    - New check `insecure_temporary_file_core_java` added for Java.
    - New check `insufficient_ui_overlay_protection_android` added for Java, Kotlin, XML.
    - New check `unlogged_security_exception_core_java` added for Kotlin.
    - New check `xss_core_go` added for Go.
    - New hardcoded secrets pattern `Hashicorp Vault Unseal Key` added.
  - **Bug fixes:**
    - Fixed a `jwt_non_expiring_token_io_jsonwebtoken` false positive by recognizing newer API methods for setting the expiration time of the token.
    - Fixed a `hardcoded_secrets` false positive that incorrectly reported an issue with a secret used from an environment variable.
- Fix Pull Requests can now be created automatically or manually in the Polaris UI for components with direct dependency vulnerabilities detected by the SCA scan of SCM-integrated projects. For more information, see [Fix Pull Requests (Fix PR)](../how-to/fix-pull-requests-fix-pr.md).
- Reachability Analysis has been incorporated into Polaris SCA testing to determine whether identified component vulnerabilities are actively reachable from source code. This will make SCA results more actionable and relevant, significantly reducing false positives and directing upgrade efforts towards actively exploitable vulnerabilities.

  To enable reachability analysis, contact polaris\_reachability@blackduck.com. Once activated, it is disabled by default. An Organization Admin must enable it at the organization level before it can be enabled for applications, projects, and/or branches. See [Using Reachability Analysis](../how-to/using-reachability-analysis.md) for more information.
- Polaris now supports advanced artificial intelligence based prioritization capabilities.

## May 2026

- Now, SCA issues on the (CISA KEV) catalog are flagged in the Polaris user interface. The CISA KEV catalog — maintained by the U.S. Cybersecurity and Infrastructure Security Agency — lists CVEs with confirmed active exploitation in the wild. When an issue appears on the CISA KEV list, a red CISA KEV label appears next to issues found in the catalog, and detailed information can be viewed in the Issue Details panel. CISA KEV status is refreshed automatically and does not require a new scan.

  You can add rules to issue, component, and pull/merge request policies to automate actions when issues in the CISA KEV catalog are captured in tests. See [Issue policies](../how-to/create-and-manage-policies/issue-policies.md), Component policies, and Pull/merge request policies for more information.
- The Polaris status page (<https://status.polaris.blackduck.com>) is deprecated. The status of Polaris (and its services) is now tracked on the new Black Duck status page (<https://status.blackduck.com>), which covers Polaris and other Black Duck cloud products. The existing Polaris status page remains available during the transition.

  Important: Going forward, scheduled maintenance announcements will only be posted on the Black Duck status page.
- Polaris now has binary analysis which enables users to identify open source risk in compiled software and containers where source code is not available. This delivers a more complete Software Bill of Materials (SBOM) and improves visibility for managing risk across the full software lifecycle.
- Polaris supports Rapid Scan Static (Sigma) 2026.4.1. This version has the following changes:
  - **General enhancements and changes:**
    - Enhanced "hardcoded\_secrets" password detection within URLs and connection strings.
    - Added the `cra` check set, which will enable the EU Cyber Resilience Act (EU-CRA) checks.
    - Added detection for hardcoded keystore and truststore passwords in Spring Integration. Sigma's existing generic secret detection continues to identify hardcoded passwords, bearer tokens, and API keys across Spring Security, Spring Boot Actuator, and various platforms including Twitch, Coinbase, OpenSea, Huawei, Hunter, and IBM.
  - **47 new checks: 15 Scala checks, 16 Kotlin checks, 10 Go checks, 5 C# checks, 1 S/TS check:**
    - New check `broad_domain_attribute_cookie_core_scala_http4s_response_cookie` added for Scala.
    - New check `broad_domain_attribute_cookie_dotnet_core_net` added for CSharp.
    - New check `broad_domain_attribute_cookie_play_config` added for Scala.
    - New check `broad_domain_attribute_cookie_play_mvc` added for Scala.
    - New check `certificate_verification_disabled_crypto_ssh` added for Go.
    - New check `certificate_verification_disabled_crypto_tls` added for Go.
    - New check `cors_with_credentials_null_origin_result_play` added for Scala.
    - New check `csrf_protection_disabled_beego` added for Go.
    - New check `csrf_protection_disabled_beego_config` added for Go.
    - New check `excessive_session_lifetime_beego` added for Go.
    - New check `excessive_session_lifetime_beego_config` added for Go.
    - New check `excessive_session_lifetime_gin` added for Go.
    - New check `excessive_session_lifetime_gorilla` added for Go.
    - New check `hardcoded_credentials_core_kotlin` added for Kotlin.
    - New check `header_injection_core_kotlin` added for Kotlin.
    - New check `implicit_intent_core_kotlin` added for Kotlin.
    - New check `insecure_file_permission_core_go_os` added for Go.
    - New check `missing_httponly_attribute_core_scala_http4s_response_cookie` added for Scala.
    - New check `missing_httponly_attribute_dotnet_core_net` added for CSharp.
    - New check `missing_httponly_attribute_play_config` added for Scala.
    - New check `missing_httponly_attribute_play_mvc` added for Scala.
    - New check `missing_permission_check_android` added for Kotlin.
    - New check `missing_samesite_attribute_core_scala_http4s_response_cookie` added for Scala.
    - New check `missing_secure_attribute_core_scala_http4s_response_cookie` added for Scala.
    - New check `missing_secure_attribute_dotnet_core_net` added for CSharp.
    - New check `missing_secure_attribute_play_config` added for Scala.
    - New check `missing_secure_attribute_play_mvc` added for Scala.
    - New check `missing_tls_moleculer_transporter` added for JavaScript, TypeScript.
    - New check `missing_tls_slick_play_database_config` added for Scala.
    - New check `os_cmd_injection_core_kotlin` added for Kotlin.
    - New check `path_manipulation_core_kotlin` added for Kotlin.
    - New check `persistent_cookie_dotnet_core_net` added for CSharp.
    - New check `regex_injection_core_kotlin` added for Kotlin.
    - New check `root_path_attribute_cookie_core_scala_http4s_response_cookie` added for Scala.
    - New check `root_path_attribute_cookie_dotnet_core_net` added for CSharp.
    - New check `root_path_attribute_cookie_play_config` added for Scala.
    - New check `root_path_attribute_cookie_play_mvc` added for Scala.
    - New check `script_code_injection_core_kotlin` added for Kotlin.
    - New check `sensitive_data_leak_core_kotlin` added for Kotlin.
    - New check `sqli_core_kotlin` added for Kotlin.
    - New check `unencrypted_sensitive_data_core_kotlin` added for Kotlin.
    - New check `unrestricted_access_to_file_core_kotlin` added for Kotlin.
    - New check `unsafe_deserialization_core_kotlin` added for Kotlin.
    - New check `unsafe_functionality_unsafe` added for Go.
    - New check `unsafe_jni_core_kotlin` added for Kotlin.
    - New check `url_manipulation_core_kotlin` added for Kotlin.
    - New check `xpath_injection_core_kotlin` added for Kotlin.
  - **10 new hardcoded secrets patterns: 1 Java/Kotlin pattern, 9 patterns for all languages**
    - New hardcoded secrets pattern `Consumer Key (generic)` added.
    - New hardcoded secrets pattern `GitGuardian personal access token` added.
    - New hardcoded secrets pattern `GitGuardian service account token` added.
    - New hardcoded secrets pattern `GitHub Key` added.
    - New hardcoded secrets pattern `Github Personal Access Token` added.
    - New hardcoded secrets pattern `GoCardless API Key` added.
    - New hardcoded secrets pattern `Google API Key` added.
    - New hardcoded secrets pattern `Heroku OAuth Access Token` added.
    - New hardcoded secrets pattern `HubSpot Private App Token` added.
    - New hardcoded secrets pattern `Token in key` added.
  - **Bug Fixes:**
    - Fixed a `hardcoded_secrets` false negative with certain `key=value` associations in `.yml` files.
    - Fixed a `anonymous_access_enabled_terraform_azurerm_web_app` false positive where `auth_setting_v2` wasn't being recognized as an authentication setting.
  - **Deprecations:**
    - Sigma support for MacOS 14.x on x86\_64 and arm64 has been deprecated.
- The validation that runs before package manager SCA tests was enhanced. When required files for a package manager test aren't detected, the test does not run. Find required files for package manager tests here: SCA Language and Package Manager Support.

  Note: This change affects the North American instances of Polaris.
- Polaris now supports Coverity 2026.3.0. It includes the following changes:
  - Added support for Windows Server 2025.
  - Added support for C# 14.
  - Added support for Bazel 9.
  - Added support for .NET 10.0.
  - Support for .NET 9.0 is deprecated and will be removed in a future release.
  - Support for Bazel 6 was removed.
  - Support for SpotBugs was removed.
  - Support for Detext was removed.

    Important: KOTLIN CHECKER UPDATES:
    - Upcoming support of Coverity 2026.6.0, will have the following Kotlin dataflow checker updates:
      - Kotlin dataflow checkers will migrate to the Rapid Scan (Sigma) engine.
      - Some Coverity Kotlin defects that are replaced by Rapid Scan defects with different issue ids will be reconciled (and therefore won’t need to be retriaged).
      - Most existing Coverity dataflow defects will disappear, and triage history will be lost.
      - These defects will be reported as new defects, and will need to be re-triaged.

    Important: JavaScript, TypeScript, Go, and Python and Kotlin quality checkers have been disabled by default and will be removed in a future release.
  - **Checker Information:**
    - Added a new checker, `SESSION_MANIPULATION`, for Java.
    - The C/C++ checker, `INCONSISTENT_UNION_ACCESS`, is now enabled by default.
    - Support for checker options for trust and distrust settings has been deprecated and will be removed in a future version.
    - Kotlin quality checkers are disabled by default in 2026.3.0 and will be removed in a future version.
    - Improved the `RESOURCE_LEAK` checker to report cases where an allocated object with allocated fields is returned from a function, then freed without freeing some of the fields.
    - Enhanced the `PRECEDENCE_ERROR` checker to handle unexpected binding of expressions outside of macro expansions to expressions within the macro expansions.
    - Updated the `DIVIDE_BY_ZERO` checker to deduce bounds for variables in loop conditions involving "not equals to (!=)" operator.
    - The Linux `scandir()` and `scandirat()` built-in models have been enhanced to no longer require the "namelist" parameter to be initialized, better matching these functions' behavior.
    - Checker `READONLY_BUFFER` is now documented.
    - Improved the event messages in `INCOMPLETE_DEALLOCATOR` when allocations happened in called functions.
    - The `SESSION_MANIPULATION` checker now supports Java.
    - The `MASS_ASSIGNMENT` checker options now supports regular expressions.
    - The `MASS_ASSIGNMENT` checker options now supports class-qualified field names for Java and C#.
    - The `MASS_ASSIGNMENT` checker now respects allow-listing and will no longer report defects on protected types and parameters.
    - Fixed a `RETURN_LOCAL` FP involving `weak_ptr.lock()`.
    - Fixed some One Definition Rule false negatives resulting from conflicts involving compiler-generated functions.
    - Fixed an issue in `INCOMPLETE_DEALLOCATOR` which could cause it not to recognize when a single allocation was assigned to multiple fields within the same structure.
    - Models are added to Linux/Android functions to eliminate certain `RESOURCE_LEAK FPs`.
    - Fixed a recoverable analysis error with message "No ODR diff found" in some cases when analyzing C++ code compiled in both 32 bit and 64 bit mode.
    - Fixed an issue in the way the control buffer in the `recvmsg()` function is handled.
    - Fixed a false positive for the `CSRF` checker. [Java]
    - Addressed `REGEX_INJECTION` false positives by adding a sanitizer for the .NET `Regex.Escape` method.
    - Fixed a false negative for the `SQLI` checker. [C#]
    - Fixed a false positive pattern for the `XML_EXTERNAL_ENTITY` checker. [C#]
- Polaris supports Rapid Scan Static (Sigma) 2026.4.0. This version has the following changes:
  - **2 new Go checks, 1 new Java check, 1 new Java/Kotlin check, 13 new Java/Kotlin/Scala checks, 1 new Properties check, 3 new Scala checks, and 16 checks modified to support additional languages:**
    - Modified existing Java check `missing_tls_spring_boot_couchbase` to support Kotlin, Scala.
    - Modified existing Java check `missing_tls_spring_boot_datasource` to support Kotlin, Scala.
    - Modified existing Java check `missing_tls_spring_boot_flyway` to support Kotlin, Scala.
    - Modified existing Java check `missing_tls_spring_boot_influx` to support Kotlin, Scala.
    - Modified existing Java check `missing_tls_spring_boot_neo4j` to support Kotlin, Scala.
    - Modified existing Java check `missing_tls_spring_boot_r2dbc` to support Kotlin, Scala.
    - Modified existing Java check `missing_tls_spring_data_mongodb` to support Kotlin, Scala.
    - Modified existing Java check `missing_tls_spring_data_r2dbc` to support Kotlin, Scala.
    - Modified existing Java check `missing_tls_spring_datasource` to support Kotlin, Scala.
    - Modified existing Java check `missing_tls_spring_http` to support Kotlin, Scala.
    - Modified existing Java check `missing_tls_spring_http_client` to support Kotlin, Scala.
    - Modified existing Java check `missing_tls_spring_http_client_reactive` to support Kotlin, Scala.
    - Modified existing Java check `missing_tls_spring_r2dbc_connection` to support Kotlin, Scala.
    - Modified existing Java check `missing_tls_spring_reactive_websocket` to support Kotlin, Scala.
    - New check `missing_tls_spring_boot_elasticsearch` added for Java, Kotlin, Scala.
    - New check `missing_tls_spring_security_oauth` added for Java, Kotlin, Scala.
    - New check `basic_auth_enabled_gin` added for Go.
    - New check `broad_domain_attribute_play_config` added for Scala.
    - New check `cors_no_credentials_permissive_origin_result_play_config` added for Scala.
    - New check `cors_with_credentials_http_origin_result_play_config` added for Scala.
    - New check `jwt_no_claims_validation_core_go` added for Go.
    - New check `missing_tls_apache_commons_io` added for Java, Kotlin, Scala.
    - New check `missing_tls_apache_datasource` added for Java, Kotlin, Scala.
    - Modified existing Java, Scala check `missing_tls_apache_http` to support Kotlin.
    - New check `missing_tls_core_java_sql` added for Java, Kotlin.
    - New check `missing_tls_jackson_core` added for Java, Kotlin, Scala.
    - New check `missing_tls_jackson_objectmapper` added for Java, Kotlin, Scala.
    - New check `missing_tls_jackson_objectreader` added for Java, Kotlin, Scala.
    - Modified existing Java check `missing_tls_spring_resttemplate` to support Kotlin.
    - New check `missing_tls_datastax_driver` added for Java, Kotlin, Scala.
    - New check `missing_tls_dom4j_io` added for Java, Kotlin, Scala.
    - New check `missing_tls_dom4j_jaxb` added for Java, Kotlin, Scala.
    - New check `missing_tls_guava_resources` added for Java, Kotlin, Scala.
    - New check `missing_tls_mongodb` added for Java, Kotlin, Scala.
    - New check `missing_tls_vertx` added for Java, Kotlin, Scala.
    - New check `sensitive_data_leak_java_grpc` added for Java.
    - New check `signature_verification_disabled_maven_wrapper` added for Properties.
  - **Support for detecting hardcoded API keys from major LLM providers**
    - Added `Perplexity API key` and updated `Secret key` hardcoded secret patterns enabling Sigma to detect hardcoded API keys from major LLM providers including OpenAI, Anthropic, Perplexity AI, and Gemini. This enhancement significantly improves Sigma's ability to identify exposed credentials for AI services, helping teams prevent unauthorized access to their LLM accounts.
  - **5 other new hardcoded secret patterns**
    - New hardcoded secrets pattern `Generic Application Key` added.
    - New hardcoded secrets pattern `Spring OAuth2 Password Grant Request` added.
    - New hardcoded secrets pattern `Spring OAuth2 Token Introspector` added.
    - New hardcoded secrets pattern `Spring Security Refresh Token` added.
    - New hardcoded secrets pattern `Spring Security Token` added.
  - **Known Issues**
    - Sigma’s SQL injection (SQLI) heuristics may result in occasional false positives (FPs) due to misfiring by the SQL recognizer. Creating stricter heuristics would result in false negatives (FNs)
- **Known issue**: Issue severity and fix-by date changes that are pending approval do not appear on the Triage Approval Overview dashboard. These changes only appear in the dashboard after they're approved.
- When you choose to use a specific Coverity version (including the recommended version), the corresponding version of Rapid Scan Static (Sigma) is locked, and won't change when newer Sigma versions are available.

  Important: Black Duck® Bridge 4.2.1 or later is required to use this feature in CI/CD pipelines.

  See [Manage SAST tool versions](../how-to/manage-sast-tool-versions.md) for more information.
- Polaris supports Black Duck® Bridge CLI 4.2.1.
- The validation that runs before package manager SCA tests was enhanced. When required files for a package manager test aren't detected, the test does not run. Find required files for package manager tests here: SCA Language and Package Manager Support.

  Note: This change affects the European Union and Saudi Arabian instances of Polaris. North American instances will be updated at a later date.
- Now, you can download test artifacts and retrieve test UIDs for troubleshooting from the Polaris user interface. See [Download test artifacts](../how-to/download-test-artifacts.md) and Find a test UID for more information.
- Polaris now detects the programming languages in your source code and displays them in the user interface. Hover over a project name on the Application page, or over a SAST test ID on the Tests page or the project's Tests tab, to see the detected languages as approximate percentages (for example, JavaScript 74.33%, HTML 24.2%, Makefile 1.47%).

  Note: When Polaris detects a language that cannot be analyzed in the current test mode, and that language accounts for more than 90% of the code, a warning [image: icon test metrics error] icon appears next to the project name and test ID, indicating that an alternative testing method is required to fully analyze the source. Typically, this occurs when a language in your source files can only be tested from your CI system using Black Duck® Bridge.
- Polaris now includes a License Manager that provides a global view of all licenses and allows you to:
  - Edit License Family and Text
  - Assign status (Approved, etc.) and expiration date
  - Add notes
  - View terms, usage, and history.

  The project's License tab now shows the same information but does not include editing features.

  Status has been added to component policies and the license table dashboard.

  See [Edit and review licenses](../how-to/edit-and-review-licenses.md) for more information.

## April 2026

- You can now customize the modules included in out-of-the-box reports. When creating a report, use the Report Modules section to include or exclude modules using checkboxes. All modules are enabled by default, with the exception of Tool checker information. For select modules, an Edit button lets you further customize the module's content — either by editing text or selecting which data to include, such as specific charts and table columns. Module selections and content customizations are saved as part of a report configuration. See [Create a report](../how-to/create-a-report.md) for more information.
- Component policies now include an option to set rules for deep license data (if enabled) monitoring.
- Tools in the Issue Management MCP server were renamed, and redundant tools were removed. Users who interact with the server through natural language are not affected. If you invoke tools directly using the MCP protocol, update your tool calls to use the new names.
  - The following tools were renamed:
    - `list_issues_with_filtering` is now `list_issues`.
    - `get_issue_by_id` is now `get_issue`. The updated tool also returns remediation guidance, occurrence properties, and triage status.
    - `get_branches_in_org` is now `get_branches`.
  - The following tools were removed: `get_issue_details_with_remediation`, `get_issue_remediation`, `get_remediation_suggestions`, and `get_ai_powered_remediation`. Use `get_issue` to retrieve remediation information for a specific issue.

  See [Issue Management MCP server](../how-to/issue-management-mcp-server.md) for the updated list of available tools.
- Polaris supports Black Duck® Bridge CLI 4.1.2.
  - Bridge can create Fix Pull Requests from Polaris SCA scan results in CI workflows. Fix Pull Requests update dependency versions in a repository based on upgrade guidance from Polaris SCA scans on branches (direct dependencies only).

    See [Using Fix PRs With Bridge](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/3e23f5f2a9b6a8f2a090f6ec144f46d7.topic) for more information.
  - Programming language metadata (that is, the different programming languages scanned in a test) appears in CI logs for SAST tests. This metadata will be integrated into the Polaris user interface in a future release.
- Polaris now provides deep license information (also called sub-licenses or embedded licenses) found in your open source components. Managing this data reduces license infringement risk and simplifies understanding and reporting on deep licenses. Disabled by default, deep license data can be enabled for the entire organization, specific applications, or projects. See [Managing deep licenses](../how-to/managing-deep-licenses.md) for more information.
- Polaris now supports triaging issue severity. Once enabled, you can change the severity level assigned to DAST, SAST, and SCA issues when triaging (for example, from Medium to High).

  Triaging issue severity can be enabled at the organization level, in applications, or in projects. Organization Administrators can enable this feature for all applications and projects. To do so, go to My Organization > Triage. Then, select Edit, enable Allow triaging issue severity, and select Save. Lock or unlock the setting (using the padlock icon) to determine whether triaging issue severity can be further controlled at the application and project levels.

  - If unlocked, Organization Application Managers, Application Administrators, and users with application management permissions can configure triaging issue severity in application or project settings.
  - If locked, only Organization Administrators can configure triaging issue severity in application or project settings.

  For additional control, you can edit your triage approval workflow to include changes to an issue's severity.

  A new Severity Modified filter has been added to relevant reports and dashboards, and the Issues page.

  See [Triaging issue severity](../how-to/triaging-issue-severity.md) for more information.
- Polaris now supports Rapid Scan Static (Sigma) 2026.3.0. This version has the following changes:
  - **Language/Framework updates:**
    - Added support for Hocon format configuration file types.
    - Validated support for Scala 3.8.
  - **1 new Java checker, 3 new Scala checkers, and 4 checkers modified to support Kotlin or Scala:**
    - New check `missing_tls_java_grpc_insecure` added for Java.
    - New check `broad_filesystem_access_dropwizard_setup` added for Scala.
    - New check `missing_tls_play_ws` added for Scala.
    - New check `missing_tls_result_play` added for Scala.
    - Modified existing Java check `certificate_verification_disabled_core_java` to support Kotlin.
    - Modified existing Java check `debug_logging_enabled_reactor_netty` to support Scala.
    - Modified existing Java check `file_upload_misconfiguration_of_fields_servlet` to support Scala.
    - Modified existing Java check `file_upload_misconfiguration_of_filesize_servlet` to support Scala.
    - Removed the `certificate_verification_disabled_android` check, which is duplicated by the existing `certificate_verification_disabled_core_java` check.
  - **10 new hardcoded secrets patterns:**
    - New hardcoded secrets pattern `AWS IAM Password` added.
    - New hardcoded secrets pattern `Basic Auth Credentials Springframework` added.
    - New hardcoded secrets pattern `Hardcoded IP Address` added.
    - New hardcoded secrets pattern `Java Security PKCS8/X509 Encoded Key` added.
    - New hardcoded secrets pattern `Javax Context Properties` added.
    - New hardcoded secrets pattern `Javax Crypto DES Key` added.
    - New hardcoded secrets pattern `Spring RSA Crypto Salt` added.
    - New hardcoded secrets pattern `Spring Security Crypto Password` added.
    - New hardcoded secrets pattern `Spring Security RSocket Metadata Password` added.
    - New hardcoded secrets pattern `Spring Security Remember me Key` added.
  - **General Enhancements and Changes:**
    - Sigma support on Linux x86\_64 and Linux arm64 now require glibc 2.28 or newer (an increase from the previous requirement of glibc 2.23).
  - **Bug Fixes:**
    - Fixed false positives caused by parse errors on comments in JSON files by ensuring the comments are parsed correctly.

## March 2026

- Now, you can create multiple DAST projects within a single application; for example, one project for a web app and one for a REST API. The maximum quantity of DAST projects allowed across your applications is displayed on the Projects tab, in the info panel.

  See [Test web applications and APIs with Polaris fAST Dynamic](../how-to/test-web-applications-and-apis-with-polaris-fast-dynamic.md) for more information.
- Issue tracking integrations with Azure DevOps and Jira now support automatic ticket closure. You can configure Polaris to automatically close tickets when linked issues become absent or are dismissed. Configure integration options at the organization level, then enable auto-close for specific projects and branches.

  Note: If a ticket is linked to multiple issues, all linked issues must be absent or dismissed before Polaris closes the ticket. Polaris does not re-open tickets once they are closed.

  See Automatically close tickets and synchronize triage statuses for more information.
- **Important**: The sunset date for deprecated endpoints in Polaris APIs was extended to **August 25, 2026, at 12:00 AM EST**. Deprecated endpoints in Polaris APIs, versions of the Bridge CLI older than 3.6.0, and versions of Code Sight older than 2025.4.0 will stop functioning on August 25, 2026. To avoid failures:
  - Update your API scripts before August 25, 2026
  - Upgrade to Bridge CLI 3.6.0 (or newer) before August 25, 2026
  - Upgrade to Code Sight 2025.4.0 (or newer) before August 25, 2026

  See [EXTENDED DEADLINE to August 25, 2026 for Deprecated Polaris API Endpoints](https://community.blackduck.com/s/question/0D5Ul00000g69A7KAI/announcement-extended-deadline-to-august-25-2026-for-deprecated-polaris-api-endpoints) in Black Duck Community, the [API reference guide](https://polaris.blackduck.com/developer/default/documentation), [Download Bridge CLI](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/5cc6965a2886bd9786bae37cd8607e8e.topic), and [Installing Code Sight](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/cda9d356f5606c3d361c83423b60679d.topic) for more information.
- Polaris now provides the Issue Management MCP server that lets you query your security findings using natural language through AI assistants like Claude Code. The MCP server connects AI assistants to Polaris APIs, and translates queries into API calls that retrieve data from Polaris. You can ask questions like "What's the most vulnerable project in my portfolio?" or "Show me all critical SQL injection issues." The MCP server is hosted in Polaris and uses a Polaris access token for authentication—no installation or deployment is required.

  See [Issue Management MCP server](../how-to/issue-management-mcp-server.md) for more information.
- Additional enhancements have been added to help you manage open-source and third-party licenses and their copyrights:
  - A new Notices File report is now available. This report provides a customizable list of open source components, license text, and copyright statements. The report supports PDF, HTML, or text file formats and can include data from up to five branches.

    See Create a Notices File report for more information.
  - Now, you can control how copyright information is displayed throughout Polaris, reports, and dashboards. By default, Polaris normalizes copyright entries (merges date ranges, removes undated entries, and truncates long text). Organization Admins can disable this normalization via My Organization > General.

    See [Manage copyright format](../how-to/manage-copyright-format.md) for more information.
  - Copyright text for individual components can be viewed on the Copyrights tab (Portfolio > select an application > select a project > Components > select a component > Copyrights).
- The issue tracking integrations with Azure DevOps and Jira were improved. Now, you can:
  - Export multiple issues to Azure DevOps or Jira at once. When you export more than one issue, you can link all of the issues to a single ticket, or create a ticket for each issue.
  - Edit or remove links to tickets in Azure DevOps or Jira (via issue triage).
  - Link issues to preexisting tickets in Azure DevOps or Jira (via issue triage).

  Note: Like other triage actions, ticket links are shared across branches in a project. All ticket link operations are tracked as triage events and appear in the issue's triage history.

  See [Issue tracking integrations](../how-to/issue-tracking-integrations.md), Export an issue to Azure DevOps or Jira, and Ways to triage issues in Polaris for more information.
- Polaris supports Black Duck® Bridge CLI 4.0.0. Bridge CLI now supports creating and managing GitHub issues from Polaris scan results as part of CI workflows. This feature automatically opens, updates and closes GitHub issues based on the latest security findings, enabling development teams to track remediation work directly in the source code repository.

  See [Create External Issues From Polaris Scans](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/5f7739bee1d044f67b810469f8ea645c.topic) for more information.

  Note: Resources that were deprecated in March, 2025 have been sunset, and are no longer available in Bridge CLI 4.0.0. See [Deprecated Resources](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/f98a6e9992e47ba6cf40c454d85bd70f.topic) for more information.
- Polaris now supports Rapid Scan Static (Sigma) 2026.2.1. This version has the following changes:
  - **Language/Framework updates:**
    - Validated support for Go 1.26.
    - Validated support for Dart 3.11.
  - **6 new Scala checkers and 7 checkers modified to support Scala:**
    - Modified existing Java check `jwt_algorithm_none_auth0_jwt` to support Scala.
    - Modified existing Java check `jwt_non_expiring_token_auth0_jwt` to support Scala.
    - Modified existing Java check `jwt_non_expiring_token_jose4j` to support Scala.
    - Modified existing Java check `jwt_ignored_expiration_time_jose4j` to support Scala.
    - Modified existing Java check `jwt_ignored_start_time_jose4j` to support Scala.
    - Modified existing Java check `jwt_no_claims_validation_jose4j` to support Scala.
    - Modified existing Java check `jwt_untrusted_decode_jose4j` to support Scala.
    - New check `cors_no_credentials_permissive_origin_core_scala_http4s` added for Scala.
    - New check `cors_preflight_age_too_long_result_play_config` added for Scala.
    - New check `cors_with_credentials_all_origin_result_play_config` added for Scala.
    - New check `cors_with_credentials_null_origin_result_play_config` added for Scala.
    - New check `missing_tls_core_scala_scalaoauth2` added for Scala.
    - New check `security_headers_disabled_play_config` added for Scala.
  - **1 new hardcoded secrets patterns:**
    - New hardcoded secrets pattern `Crypto Bits Private Key` added.
  - **General Enhancements and Changes:** 
    - File path checks will no longer report issues on empty files.
    - `unrestricted_database_access_android` and i`nsecure_file_permission_android` checks modified to improve accuracy.
    - Updated remediation advice for the `unsafe_min_os_version` check to use the correct version information.
  - **Bug Fixes:** 
    - Fixed a `hardcoded_secrets` false positive to not report on the existence of a `settings.py` file, but only actual secrets found within the file.

## February 2026

- Now, you can view the terms of different open-source and third-party licenses used in your projects. Find terms on the Licenses tab (Portfolio > select an application > select a project > Components > select a component > Licenses). The terms of each license are categorized by Forbidden, Permitted, and Required.

  See [Find component license information (including terms)](../how-to/find-component-license-information-including-terms.md) for more information.
- Additional changes to component origins in the Black Duck KnowledgeBase™ are automatically synchronized with projects in your portfolio (without requiring a test). These changes include:
  - A component, component version, or component origin's metadata changes in the KnowledgeBase.
  - A component, component version, or component origin is deleted in the KnowledgeBase.
  - A component or component version is migrated in the KnowledgeBase.

  See [Automatic component updates from the Black Duck KnowledgeBase](../how-to/automatic-component-updates-from-the-black-duck-knowledgebase.md) for more information.
- Polaris now supports Rapid Scan Static (Sigma) 2026.2.0. This version has the following changes:
  - **Language/Framework updates**
    - None
  - **9 new Go checkers:**
    - New check `basic_auth_enabled_beego_httplib` added for Go.
    - New check `broad_domain_attribute_cookie_go_gin` added for Go.
    - New check `insecure_samesite_attribute_cookie_core_go_net_http` added for Go.
    - New check `jwt_algorithm_none_core_go_jwt` added for Go.
    - New check `jwt_non_expiring_token_core_go_jwt` added for Go.
    - New check `missing_httponly_attribute_go_gin` added for Go.
    - New check `missing_samesite_attribute_go_gin` added for Go.
    - New check `missing_secure_attribute_go_gin` added for Go.
    - New check `root_path_attribute_cookie_go_gin` added for Go.
  - **22 new Scala checkers and 1 checker modified to support Scala:**
    - Modified existing Java check `ldap_anonymous_authentication_core_java` to support Scala.
    - New check `broad_domain_attribute_cookie_core_scala_http4s` added for Scala.
    - New check `broad_domain_attribute_cookie_core_scala_play_silhouette` added for Scala.
    - New check `broad_domain_attribute_cookie_core_scala_sttp` added for Scala.
    - New check `certificate_verification_disabled_akka_config_ssl` added for Scala.
    - New check `csrf_protection_disabled_play_config` added for Scala.
    - New check `debug_enabled_akka_config` added for Scala.
    - New check `debug_logging_enabled_akka_config` added for Scala.
    - New check `debug_logging_enabled_akka_config_deployment` added for Scala.
    - New check `excessive_session_lifetime_akka_http_session` added for Scala.
    - New check `excessive_session_lifetime_play_config` added for Scala.
    - New check `excessive_token_lifetime_scala_oauth2_provider` added for Scala.
    - New check `experimental_features_enabled_akka_config_serialize_creators` added for Scala.
    - New check `experimental_features_enabled_akka_config_serialize_messages` added for Scala.
    - New check `hsts_http_header_subdomains_disabled_core_scala_http4s` added for Scala.
    - New check `insecure_network_bind_akka_config_artery` added for Scala.
    - New check `insecure_tls_version_akka_config` added for Scala.
    - New check `missing_httponly_attribute_csrf_cookie_core_scala_http4s` added for Scala.
    - New check `missing_samesite_attribute_play_mvc` added for Scala.
    - New check `missing_secure_attribute_csrf_cookie_core_scala_http4s` added for Scala.
    - New check `remote_execution_enabled_akka_config_remote` added for Scala.
    - New check `root_path_attribute_cookie_core_scala_http4s` added for Scala.
    - New check `unsafe_deserialization_akka_config` added for Scala.
  - **4 new hardcoded secrets patterns**
    - New hardcoded secrets pattern `Pac4j OAuth Key` added.
    - New hardcoded secrets pattern `Pac4j OAuth Profile Access Secret` added.
    - New hardcoded secrets pattern `Pac4j OAuth Profile Access Token` added.
    - New hardcoded secrets pattern `Sqlite3 salt` added.
  - **General Enhancements and Changes:** 
    - Sigma now supports Windows Server 2025.
    - Sigma now scans Kotlin script files (.kts).
    - Go test files (`*_test.go`) are now excluded from analysis by default.
- Bitbucket Cloud (Premium) now has enhanced SCM repository integration capabilities:
  - Bulk onboarding: you can connect multiple Bitbucket Cloud workspaces, projects and repositories to Polaris applications and projects. See [Connect Polaris to Multiple SCM Repositories](../how-to/connect-polaris-to-multiple-scm-repositories.md).
  - You can synchronize Polaris with your Bitbucket Cloud provider to automatically track changes to your repositories and branches. When enabled, Polaris monitors your Bitbucket Cloud for updates, renames, or deletions and automatically applies these changes to the corresponding projects and branches in Polaris. See [Synchronizing Polaris with your SCM Provider](../how-to/synchronizing-polaris-with-your-scm-provider.md) for more information.
  - Event-based test automation allows you to automatically run tests when pull requests are created, updated, or merged in Bitbucket Cloud. You can configure these settings at the organization, application, project, or branch level. See [Event-Based Test Automation in Polaris for SCM Integrations](../how-to/event-based-test-automation-in-polaris-for-scm-integrations.md) for more information. If enabled, you can set Pull/merge request policies to create PR comments.
  - To access these capabilities, the access token used for SCM integration has different requirements (see [Bitbucket Tokens for SCM Bulk Integration and/or Monitoring](../how-to/bitbucket-tokens-for-scm-bulk-integration-and-or-monitoring.md)).
- Azure Repos now has enhanced SCM repository integration capabilities:
  - Bulk onboarding: you can connect multiple Azure Repos organizations, projects and repositories to Polaris applications and projects. See [Connect Polaris to Multiple SCM Repositories](../how-to/connect-polaris-to-multiple-scm-repositories.md).
  - You can synchronize Polaris with your Azure Repos provider to automatically track changes to your repositories and branches. When enabled, Polaris monitors your Azure Repos for updates, renames, or deletions and automatically applies these changes to the corresponding projects and branches in Polaris. See [Synchronizing Polaris with your SCM Provider](../how-to/synchronizing-polaris-with-your-scm-provider.md) for more information.
  - Event-based test automation allows you to automatically run tests when pull requests are created, updated, or merged in Azure Repos. You can configure these settings at the organization, application, project, or branch level. See [Event-Based Test Automation in Polaris for SCM Integrations](../how-to/event-based-test-automation-in-polaris-for-scm-integrations.md) for more information. If enabled, you can set Pull/merge request policies to create PR comments.
  - To access these capabilities, the access token used for SCM integration has different requirements (see [Azure Tokens for SCM Bulk Integration and/or Monitoring](../how-to/azure-tokens-for-scm-bulk-integration-and-or-monitoring.md)).
- Additional changes to component origins in the Black Duck KnowledgeBase™ are automatically synchronized with projects in your portfolio (without requiring a test). These changes include:
  - An issue's vulnerability score changes.
  - An issue's severity changes.
  - An issue's upgrade guidance changes.
  - A component's license definition changes.
  - A component's license metadata changes.
  - The issues linked to a component without a specified origin change.
  - The version upgrade guidance for a component without a specified origin changes.

  Note: Now, synchronization occurs every 3 hours. The issue that affected the EU instance of Polaris (announced in December) is resolved. This integration will be further refined in future releases.

  See [Automatic component updates from the Black Duck KnowledgeBase](../how-to/automatic-component-updates-from-the-black-duck-knowledgebase.md) for more information.
- On February 18, 2026, Polaris will no longer accept legacy TLS cipher suites as part of ongoing efforts to safeguard customer data. Polaris will continue to support TLS 1.3, but only allow a restricted set of strong TLS 1.2 cipher suites.

  See [Upcoming Changes to Polaris Support for Legacy TLS Cipher Suites](https://community.blackduck.com/s/question/0D5Ul00000e7KPrKAM/operational-announcement-upcoming-changes-to-polaris-support-for-legacy-tls-cipher-suites) in Black Duck Community for more information.

## January 2026

- Polaris supports Black Duck® Bridge CLI 3.12.0.
- GitLab SaaS (Premium and Ultimate) now has enhanced SCM repository integration capabilities:
  - Bulk onboarding: you can connect multiple GitLab groups, subgroups and repositories to Polaris applications and projects. See [Connect Polaris to Multiple SCM Repositories](../how-to/connect-polaris-to-multiple-scm-repositories.md).
  - You can synchronize Polaris with your GitLab provider to automatically track changes to your repositories and branches. When enabled, Polaris monitors your GitLab repositories for updates or deletions and automatically applies these changes to the corresponding projects and branches in Polaris. See [Synchronizing Polaris with your SCM Provider](../how-to/synchronizing-polaris-with-your-scm-provider.md) for more information.
  - Event-based test automation allows you to automatically run tests when pull requests are created, updated, or merged in GitLab. You can configure these settings at the organization, application, project, or branch level. See [Event-Based Test Automation in Polaris for SCM Integrations](../how-to/event-based-test-automation-in-polaris-for-scm-integrations.md) for more information. If enabled, you can set Pull/merge request policies to create PR comments.
  - To access these capabilities, the access token used for SCM integration has different requirements (see [GitLab Tokens for SCM Bulk Integration and/or Monitoring](../how-to/gitlab-tokens-for-scm-bulk-integration-and-or-monitoring.md)).
- Polaris now supports Coverity 2025.12.0. It includes the following changes:
  - Added support for macOS 26.
  - Added support for Go 1.25.
  - Added support for Java 25.
  - Added support for Kotlin 2.2.
  - Added support for Scala 3.
  - Added support for GNU GCC 15.2.
  - Added support for Xcode 26.
  - Added support for Oracle JDK 25 and Open JDK 25.
  - Support for macOS on Intel (`macosx`) is deprecated and will be removed in the 2026.12.0 release.
  - Support for Go 1.24 is deprecated and will be removed in a future release.
  - Support for JavaScript/TypeScript quality checkers are deprecated and will be removed in a future release.
  - Support for Go quality checkers are deprecated and will be removed in a future release.
  - Support for Python quality checkers are deprecated and will be removed in a future release.
  - Support for Kotlin quality checkers are deprecated and will be removed in a future release.
  - Support for Bazel 6 is deprecated and will be removed in a future release.
  - Support for Xcode 12.x-14.x is deprecated and will be removed in a future release.
  - Support for SpotBugs is deprecated and will be removed in a future release.
  - Support for Detekt is deprecated and will be removed in a future release.
  - Support for macOS 13 was removed.
  - Support for Windows 10 was removed.
  - Support for Go 1.23 was removed.
  - Support for Open JDK 24 and Oracle JDK 24 was removed.
  - Support for Swift is now autocapture only via Rapid Scan Static (Sigma) engine.
  - **Checker Information:**
    - Added support for xtensa 2023.11 on Linux.
    - Added support for xtensa 2024.4 on Linux.
    - Added support for xtensa 2025.5 on Linux.
    - The `TAINTED_SCALAR` checker now offers the `propagate_taint_on_rshift` option.
    - Added a new C/C++ checker, `HARDCODED_SECRETS`, which finds cases where a secret, such as a password, cryptographic key, or token is stored in plaintext directly in the source code. This checker is disabled by default.
    - Improved the `WRAPPER_ESCAPE` checker to avoid reporting false positives when a pointer cannot be stored in a global variable in a call to a function because parameters prevents it.
    - The `SSRF` checker now supports C# and VB.
    - The integrated version of PMD has been updated from 7.4.0 to 7.17.0 [Apex].
    - Brakeman Pro for Ruby on Rails security analysis has been upgraded to version 7.1.0
    - Fixed a false positive for the `UNLOGGED_SECURITY_EXCEPTION` checker. [C#]
    - Fixed a false positive for the `RISKY_CRYPTO` checker. [C#]
    - The `HARDCODED_SECRET` checker now finds instances where a password string is compared against hard-coded passwords.
  - The following Coverity Analysis checkers have been replaced by Sigma (SIGMA.\*) checks. Any references to these checkers in `coverity.yml` configuration files should be updated.

    | Coverity Analysis checker | Language | Sigma checks that replace this Coverity checker |
    | --- | --- | --- |
    | `ANONYMOUS_DB_CONNECTION` | Go | `anonymous_access_enabled_go_database` |
    | `CORS_MISCONFIGURATION_AUDIT` | Go | `cors_expose_sensitive_data_beego`  `cors_expose_sensitive_data_core_go_net_http`  `cors_expose_sensitive_data_gin`  `cors_expose_sensitive_data_go_aws_sdk`  `cors_expose_sensitive_data_gorilla_handlers`  `cors_expose_sensitive_data_rs`  `cors_no_credentials_permissive_origin_beego`  `cors_no_credentials_permissive_origin_core_go_net_http`  `cors_no_credentials_permissive_origin_gin`  `cors_no_credentials_permissive_origin_go_aws_sdk`  `cors_no_credentials_permissive_origin_gorilla_handlers`  `cors_no_credentials_permissive_origin_rs`  `cors_permissive_methods_beego`  `cors_permissive_methods_core_go_net_http`  `cors_permissive_methods_gin`  `cors_permissive_methods_go_aws_sdk`  `cors_permissive_methods_gorilla_handlers`  `cors_permissive_methods_rs` |
    | `EXPOSED_DIRECTORY_LISTING` | Go, Go Application Config | `exposed_directory_listing_beego`  `exposed_directory_listing_beego_config`  `exposed_directory_listing_gin` |
    | `INSECURE_COMMUNICATION` | Go | `missing_tls_beego`  `missing_tls_core_go_database_sql`  `missing_tls_core_go_net`  `missing_tls_core_go_net_http`  `missing_tls_gin` |

    Note: All of these Coverity checkers have had all Go support completely replaced by the corresponding Sigma checkers. Of these, `ANONYMOUS_DB_CONNECTION` and `EXPOSED_DIRECTORY_LISTING` are only for Go, so they have been completely removed from Coverity.
- Polaris now supports Rapid Scan Static (Sigma) 2026.1.0. This version has the following changes:
  - **Language/Framework updates:**
    - None.
  - **1 new Go checker:**
    - New check `excessive_connection_timeout_beego_httplib` added for Go.
  - **1 new Scala checker:**
    - New check `insecure_network_bind_core_scala_http4s` added for Scala.
  - **General Enhancements and Changes:**
    - Documentation of hardcoded secrets now shows the severity.
    - Improved support for `.conf` files.
    - Updated Sigma issue results category to be more descriptive.
    - Updated metadata documentation to more accurately filter OWASP Top 10 and CWE Top 25 taxonomies checker categories.
- The Component Management Dashboard is available. The new dashboard provides an overview of component and license usage in your portfolio, including charts that show components grouped by security risk and licenses grouped by type. Use the Component and Component Version filters to assess the prevalence of specific components in your portfolio.
- Atlassian has deprecated app passwords for Bitbucket Cloud. Existing projects integrated with Polaris using app passwords will continue to work until the password expires or Atlassian ends support. Once app passwords stop working or for new integrations, use API tokens (see Bitbucket Cloud for details).
- Polaris supports Black Duck® Bridge CLI 3.11.0.
- Polaris now supports Rapid Scan Static (Sigma) 2025.12.0. This version has the following changes:
  - **Language/Framework updates:**
    - Validated Sigma's support of PHP 8.5.
    - Validated support for Dart 3.10.
  - **21 new Go checkers including adding dataflow support (will increase analysis time for Go applications):**
    - New check `broad_domain_attribute_cookie_gorilla_csrf` added for Go.
    - New check `cors_configured_globally_gorilla_csrf` added for Go.
    - New check `cors_preflight_age_too_long_beego` added for Go.
    - New check `excessive_session_lifetime_gorilla_csrf` added for Go.
    - New check `exec_environment_injection_core_go` added for Go.
    - New check `header_injection_core_go` added for Go.
    - New check `insecure_samesite_attribute_cookie_gorilla_csrf` added for Go.
    - New check `insufficient_password_hash_iterations_golang_crypto_scrypt` added for Go.
    - New check `missing_httponly_attribute_session_cookie_beego` added for Go.
    - New check `missing_httponly_attribute_session_cookie_gorilla_csrf` added for Go.
    - New check `missing_secure_attribute_session_cookie_gorilla_csrf` added for Go.
    - New check `open_redirect_core_go` added for Go.
    - New check `os_cmd_injection_core_go` added for Go.
    - New check `path_manipulation_core_go` added for Go.
    - New check `regex_injection_core_go` added for Go.
    - New check `script_code_injection_core_go` added for Go.
    - New check `sensitive_data_leak_core_go` added for Go.
    - New check `sqli_core_go` added for Go.
    - New check `url_manipulation_core_go` added for Go.
    - New check `weak_hash_golang_crypto_ocsp` added for Go.
    - New check `xpath_injection_core_go` added for Go.
  - **3 New Java/Scala checkers:**
    - New check `ldap_anonymous_authentication_apache` added for Java, Scala.
    - New check `ldap_anonymous_authentication_novell` added for Java, Scala.
    - New check `ldap_anonymous_authentication_unboundid_ldap` added for Java, Scala.
  - **14 New Scala checkers:**
    - New check `broad_domain_attribute_cookie_akka_http` added for Scala.
    - New check `cors_expose_sensitive_data_akka_http` added for Scala.
    - New check `cors_no_credentials_permissive_origin_akka_http` added for Scala.
    - New check `cors_preflight_age_too_long_akka_http` added for Scala.
    - New check `cors_with_credentials_all_origin_akka_http` added for Scala.
    - New check `cors_with_credentials_http_origin_akka_http` added for Scala.
    - New check `cors_with_credentials_null_origin_akka_http` added for Scala.
    - New check `cors_with_credentials_subdomain_origin_akka_http` added for Scala.
    - New check `excessive_token_lifetime_play_oauth2` added for Scala.
    - New check `missing_samesite_attribute_core_scala_play_silhouette` added for Scala.
    - New check `missing_tls_core_scala_play_silhouette_oauth2` added for Scala.
    - New check `missing_tls_slick_play_database` added for Scala.
    - New check `persistent_cookie_play_mvc` added for Scala.
    - New check `root_path_attribute_cookie_akka_http` added for Scala.
  - **12 New Hardcoded secrets checkers:**
    - New hardcoded secrets pattern `Beego Authentication` added.
    - New hardcoded secrets pattern `Credentials Uri Gorm` added.
    - New hardcoded secrets pattern `Go Crypto TLS Certificate` added.
    - New hardcoded secrets pattern `NaCL key` added.
    - New hardcoded secrets pattern `SSH key` added.
    - New hardcoded secrets pattern `ScribeJava DeviceAuthorization Secret` added.
    - New hardcoded secrets pattern `ScribeJava OAuth1 Access Token` added.
    - New hardcoded secrets pattern `ScribeJava OAuth2 Access Token` added.
    - New hardcoded secrets pattern `ScribeJava OAuth2 Service Token Revocation Secret` added.
    - New hardcoded secrets pattern `Scribejava OAuth10aService Secret` added.
    - New hardcoded secrets pattern `Slick Database Password` added.
    - New hardcoded secrets pattern `Uri In Go Mysql` added.
- The Triage Approval Overview Dashboard is available. The new dashboard provides a centralized view of triage approval requests across applications and projects, including metrics for pending, approved, and rejected requests along with detailed information about each triage approval request.
- Now, you can download copies of OpenAPI specifications for Polaris APIs from the Black Duck Developer Portal. After you open an API reference, select the Download YAML File [image: Download YAML File] icon at the top-right (next to the Authorize button) to download the OAS file.
- Polaris now supports Rapid Scan Static (Sigma) 2025.11.1. This version has the following changes:
  - Removed redundant Hardcoded Secret pattern `Shared Preferences Android`.
  - Modified existing Java check `plaintext_storage_sensitive_data_shared_preferences_android` to support Scala.
  - New check `basic_auth_enabled_core_go_net_http` added for Go.
  - New check `basic_auth_enabled_go_dghubble_sling` added for Go.
  - New check `certificate_verification_disabled_core_go_grpc` added for Go.
  - New check `cors_no_credentials_permissive_origin_chi` added for Go.
  - New check `cors_preflight_age_too_long_gin_contrib` added for Go.
  - New check `cors_with_credentials_all_origin_chi` added for Go.
  - New check `csp_unsafe_eval_net_http` added for Go.
  - New check `csp_unsafe_inline_net_http` added for Go.
  - New check `database_evolutions_enabled_play_config` added for Scala.
  - New check `insecure_network_bind_core_scala_fs2_io_net` added for Scala.
  - New check `insecure_network_bind_core_scala_fs2_protocols` added for Scala.
  - New check `insufficient_symmetric_key_size_golang_crypto_rsa` added for Go.
  - New check `middleware_applied_globally_gorm` added for Go.
  - New check `missing_samesite_attribute_csrf_cookie_core_scala_play_silhouette` added for Scala.
  - New check `missing_tls_core_go_grpc` added for Go.
  - New check `missing_tls_scribejava_oauth10aservice` added for Java, Kotlin, Scala.
  - New check `sensitive_data_leak_core_go_crypto_tls` added for Go.
  - New hardcoded secrets pattern `Azure storage account key` added.
  - New hardcoded secrets pattern `Play Silhouette OAuth1 Secret` added.
  - New hardcoded secrets pattern `Play Silhouette OAuth2 access token` added.
  - New hardcoded secrets pattern `salsa20 encryption key` added.
  - Fixed a `hardcoded_secrets` false negative by adding a new `Azure storage account key` pattern.

## December 2025

- **Status Update** (EU Only): We have identified issues related to a recent update to our asynchronous CVE update feature.

  Important: To prevent further impact, the update has been rolled back while our team investigates and works on a resolution.

  We will provide another update as soon as more information is available and the issue is fully resolved. Thank you for your patience.
- The option to list checkers during testing (new scans only) has been added to select reports.
- Polaris now supports pull request comments for SCM integrations using test automation (currently for GitHub, SAST, and SCA tests only). Enable pull request comments via policies (see [Pull/merge request policies](../how-to/create-and-manage-policies/pull-merge-request-policies.md) for details). Comments apply only to new issues.
- Triage information — consisting of triage status changes or comments — is now included when you import results from third-party tools (SAST and SCA issues only). To view triage information for imported issues, open the Issue History panel and select Triage.
  - Imported triage events indicate the name of the third-party tool and the external user (if available).
  - Triage status values are mapped from the third-party tool to Polaris, if an equivalent status exists in the third-party tool.

  Note: The ability to import results from third-party tools is available on a limited basis, and is not generally available.

  See [Import results from third-party tools (limited availability)](../how-to/import-results-from-third-party-tools-limited-availability.md) and View issue history for more information.
- Now, you can start DAST tests from the DAST Profiles page.
- Now, you can customize the version of Coverity used for SAST tests at the organization, application, project, and branch level. This feature is generally available, but must be enabled for your organization by Black Duck Support before you can use it.

  Note: Currently, only the latest version of Coverity (2025.9.1) is supported, with additional versions to be added in future releases.

  See [Manage SAST tool versions](../how-to/manage-sast-tool-versions.md) for more information.
- Now, Organization Administrators can create and manage service accounts in the Polaris user interface.

  See [Service accounts for Polaris](../how-to/service-accounts-for-polaris.md) for more information.
- Now, you can configure DAST scan settings and authentication profiles directly in the web UI for Polaris fAST Dynamic. Previously, these settings could only be managed via a JSON configuration file. To access the new settings, select the Scan settings tab when creating a DAST project. The Simple subtab provides settings across six categories, including:
  - Authentication profile configuration
  - Active and passive checker selection
  - Customization of page readiness rules for Single Page Applications (SPAs)
  - URL inclusion and exclusion rules
  - Crawler parser behavior settings
  - Smart Settings configuration (auto-configuration of DAST scans)

  The previously available settings are now positioned on the Configuration options tab, which is selected by default.

  Note: Additional scan settings are available on the Advanced subtab. The JSON file upload method remains available for users who prefer to configure settings programmatically.

  See [Create DAST projects for web applications and APIs](../how-to/test-web-applications-and-apis-with-polaris-fast-dynamic/create-dast-projects-for-web-applications-and-apis.md) and DAST scan settings for more information.
- Polaris fAST Dynamic now supports the configuration of time-based one-time password (TOTP) MFA through the web UI. This provides easier configuration of DAST scans for sites that implement TOTP MFA—where users enter one-time tokens generated in a mobile app to sign in.

  When selecting either the Simple or SAML Login Types, you will see a new Value Type field in the Steps > Inputs forms. Select the `totp` value type and enter your MFA Secret Key in the Value field.

  See [Create DAST projects for web applications and APIs](../how-to/test-web-applications-and-apis-with-polaris-fast-dynamic/create-dast-projects-for-web-applications-and-apis.md) for more information.
- Now, when you create groups in Polaris, group names can be 3-255 characters long.
- Now, certain changes to component origins in the Black Duck KnowledgeBase™ are automatically synchronized with projects in your portfolio (without requiring a test). These changes include:
  - Issues are added to or removed from component origins in the KnowledgeBase
  - A component's security risk changes in the KnowledgeBase

  Note: For now, these are the only changes that are synchronized with Polaris. This integration will be further refined in future releases.

  See [Automatic component updates from the Black Duck KnowledgeBase](../how-to/automatic-component-updates-from-the-black-duck-knowledgebase.md) for more information.
- Polaris now supports Rapid Scan Static (Sigma) 2025.11.0. This version has the following changes:
  - Added support for MacOS 26.
  - **New Kotlin checkers**: added 17 new Java checkers for Kotlin including unsafe CORS configuration checkers and weak cookie security attribute checkers.
  - **New Go checkers:** added 39 new checkers for Go, mainly focused on insecure cryptography, e.g. `weak_hash_golang_crypto`.
  - **New Go hard-coded secrets detection patterns**: added 7 new detection patterns for hardcoded secrets in Go code including PBKDF2, Scrypt and Argon2 salts.
  - **New Scala checkers**: added 26 new checkers for Scala, including `unsafe_language_feature` and `debug_enabled_play_config`.
  - **New Scala hard-coded secrets detection patterns**: added 5 new detection patterns for hardcoded secrets in Scala code including Akka BasicHttpCredentials and multiple Play Framework patterns.
  - Fixed a bug in the Sigma Trojan source checker which may cause Rapid Scan to fail.
  - Fixed a `hardcoded_secrets` false positive that reported issues on environment variables holding passwords.
- Polaris now supports Coverity 2025.9.1. It includes the following key features:
  - Coverity will output a list of enabled checkers in full scans which will can be accessed in reports and APIs.
  - Improvements to Kotlin Hybrid checkers.
  - Coverity will capture code compiled by the Kotlin 2.2 compiler provided no Kotlin 2.2 specific language features are used. Using Kotlin 2.2 specific language features will likely result in capture failure. In this scenario users can specify to failover to an experimental in-development capture engine that may prove more tolerant of Kotlin 2.2 language features. The failover is enabled by setting the `COVERITY_ENABLE_KOTLIN_SIGMA_FALLBACK` environment variable, but will likely result in significant analysis results degradation.
  - **Bug fix**: In the Coverity 2025.9.0 release, a bug was introduced into the Coverity CLI such that the current working directory was being set incorrectly when running user supplied clean and build commands. In the 2025.9.1 release, this was fixed so that the current working directory for user supplied clean and build commands will be set to the project directory as was done in previous releases.
  - A number of Coverity Analysis checkers have been partially replaced by Sigma (SIGMA.\*) checks.

    | Coverity Analysis checker | Language | Sigma checks that replace this Coverity checker |
    | --- | --- | --- |
    | `CONFIG.COOKIE_SIGNING_DISABLED` | Go Application Config | `unsafe_session_storage_revel` |
    | `CORS_MISCONFIGURATION` | Go | `cors_with_credentials_all_origin_beego`  `cors_with_credentials_all_origin_core_go_net_http`  `cors_with_credentials_all_origin_gin`  `cors_with_credentials_all_origin_gorilla_handlers`  `cors_with_credentials_all_origin_rs`  `cors_with_credentials_http_origin_beego`  `cors_with_credentials_http_origin_core_go_net_http`  `cors_with_credentials_http_origin_gin`  `cors_with_credentials_http_origin_gorilla_handlers`  `cors_with_credentials_http_origin_rs` |
    | `INSECURE_NETWORK_BIND` | Go | `insecure_network_bind_beego`  `insecure_network_bind_core_go_net`  `insecure_network_bind_go_gin` |
    | `INSECURE_COOKIE` | Go | `missing_httponly_attribute_session_cookie_gorilla_sessions`  `missing_samesite_attribute_session_cookie_gorilla_sessions`  `missing_secure_attribute_session_cookie_gorilla_sessions` |
    | `INSECURE_COOKIE` | Go Application Config | `missing_samesite_attribute_revel_config`  `missing_secure_attribute_revel_config` |
    | `OAUTH2_MISCONFIGURATION` | Go | `misconfigured_oauth2_go_core_oauth2` |
    | `STATIC_API_KEY` | Go | `static_non_expiring_token_core_go_oauth2` |

    Note: All six of these Coverity checkers have had all Go support completely replaced by the corresponding Sigma checkers. Of these Coverity checkers, `CONFIG.COOKIE_SIGNING_DISABLED`, `STATIC_API_KEY`, `OAUTH2_MISCONFIGURATION`, `INSECURE_NETWORK_BIND`, and `CORS_MISCONFIGURATION` do not support any language other than Go. The `INSECURE_COOKIE` checker does support languages other than Go.
- Polaris supports Black Duck® Bridge CLI 3.10.1.

## November 2025

- An issue where SCM event-based test automation saved changes reset unexpectedly was resolved by having an Organization Owner in GitHub create the personal access token, as GitHub requires this for managing organization webhooks. The UI and documentation have been updated.

## October 2025

- SCM integration test automation (currently only available for GitHub) now provides the option to run Rapid Scan Static (Sigma) tests.
- Polaris supports Black Duck® Bridge CLI 3.9.2.
- **Important**: The sunset date for deprecated endpoints in Polaris APIs was extended to **March 24, 2026, at 12:00 AM EST**. Deprecated endpoints in Polaris APIs, versions of the Bridge CLI older than 3.6.0, and versions of Code Sight older than 2025.4.0 will stop functioning on March 24, 2026. To avoid failures:
  - Update your API scripts before March 24, 2026
  - Upgrade to Bridge CLI 3.6.0 (or newer) before March 24, 2026
  - Upgrade to Code Sight 2025.4.0 (or newer) before March 24, 2026

  See [EXTENDED DEADLINE to March 24, 2026 for Deprecated Polaris API Endpoints](https://community.blackduck.com/s/question/0D5Ul00000XKWOzKAP/announcement-extended-deadline-to-march-24-2026-for-deprecated-polaris-api-endpoints) in Black Duck Community, the [API reference guide](https://polaris.blackduck.com/developer/default/documentation), [Download Bridge CLI](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/5cc6965a2886bd9786bae37cd8607e8e.topic), and [Installing Code Sight](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/cda9d356f5606c3d361c83423b60679d.topic&Version=latest) for more information.
- Three additional scores were added to the SCA **Issue Details** tab:
  - Base score
  - Exploitability score
  - Impact score

  To view, run a new scan and click the blue icon next to the vulnerability score (which displays the new scores and the temporal score).

  Note: The risk scores assigned to applications in your portfolio may change when this feature is enabled.
- Personal, Project, and Group tokens are supported for GitLab SCM Integrations. If using a Project or Group token, select a role above Guest.
- Polaris now supports Rapid Scan Static (Sigma) 2025.10.0. This version has the following changes:
  - **New checkers:** Added 28 new checkers for Scala, 12 new checkers for Kotlin, 7 new checkers for Go, and 3 new checkers for Java.
  - Added 11 new hardcoded secrets detection patterns.
  - Support for Python 3.14.
  - Support for Java 25.
  - Sigma now ships a native ARM64 binary for MacOS. Additionally, MacOS x86 support is deprecated.
  - Fixed an issue where the `hardcoded_secret_pattern` check was reporting false positives in scans run on Windows.
  - Fixed a bug where very deeply nested member function calls in C# caused Sigma to overflow its stack when run on Windows.
- Now, you can get a list of the service accounts (including service account IDs) in your organization using the `GET /api/auth/service-account-tokens endpoint`.

  See [Get a list of service accounts and their IDs](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/d9540d417e952b4580e8f0dd120ba6de.topic) for more information.
- Now, you can save dashboard filter configurations so they can be reapplied later.

  Note: The saved filters you create are not shared with other users in your organization, and only work with one dashboard.

  See Create and manage saved filters for more information.
- Dashboards now include issue data from all the branches in your projects, not just default branches. Add issue data from non-default branches to a dashboard using the Branch Type and Branch filters.
- The Project Label and Branch Label filters were added to Dashboards. Now, in addition to filtering using labels assigned to applications, you can filter using labels assigned to projects and branches.
- Polaris supports Black Duck® Bridge CLI 3.9.0. Now, you can run SAST tests within your CI/CD environment, without sending complete source code to Polaris. When you run SAST tests locally:
  - Essential tools to run tests are downloaded automatically (including Sigma, the Polaris Snippet Generator, and Coverity Analysis tools).
  - Code capture and analysis are performed within your CI/CD environment.

    Note: This differs from the default (`hybrid`) and source upload (`remote`) test modes. In `hybrid` mode, code capture is performed locally, but analysis is performed by Polaris; in `remote` mode, code capture and analysis are both performed by Polaris.
  - Test results (limited to issues and applicable code snippets, and metadata) are sent to Polaris.

  To use local analysis, set `polaris.test.sast.location=local` in your Bridge CLI configuration, or use `BRIDGE_POLARIS_TEST_SAST_LOCATION: 'local'` in CI pipeline configurations. See [Local Analysis Scan](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0c68b6621951399783959d99c58930be.topic) for more information.

  Important: The `polaris.assessment.mode` resource is deprecated. Use `polaris.test.<assessmentType>.location` instead.
- With Bridge 3.5.1 (or newer) and the latest versions of Black Duck Security Scan, you can run SAST tests using the Bridge CLI on Linux ARM.
- Polaris now supports Rapid Scan Static (Sigma) 2025.9.1. This version has the following changes:
  - Support for Scala. Rapid Scan can now parse and analyze the Scala language (version 3). The initial checker set focuses on API safety and secrets detection with 29 checkers.
  - New Checkers Added: 7 new checkers for Kotlin, 9 new checkers for Java, and 1 new checker for Go. Highlights include support for the scribejava OAuth 2.0 library for Java and Scala, and improper resource release detection for the Gorilla library's web sockets implementation for Go.
  - Support for Dart version 3.9.
  - Support for Swift version 6.2.
  - Fixed a bug in the Sigma Trojan source checker which sometimes caused Rapid Scan to fail.
- Polaris now supports Coverity 2025.9.0. It includes the following changes:
  - Added support for Python 3.13.
  - Added support for Kotlin 2.1.10.
  - Added support for LLVM Clang 19.1.0.
  - Support for Java 24 is deprecated and will be removed in a future release.
  - Support for Oracle JDK 24 is deprecated and will be removed in a future release.
  - Support for OpenJDK 24 is deprecated and will be removed in a future release.
  - Support for Android NDK revision r21e (Clang 9.0) has been removed.
  - Added a REST API to enable users to retrieve information about their usage of the Coverity scan service. This API lets users check the status of a scan job, cancel a scan job, and see a list of scans in the queue.
  - Added the option to limit output files to Logs Only in order to simplify troubleshooting in the event that large intermediate directories (idirs) fail to upload.
  - **Checker Information:**
    - Multiple Go checkers are deprecated and will be replaced with Sigma checkers in a future release.
    - A new checker, `UNNECESSARY_STRING_COPY`, detects inefficiencies in the use of C++ std::string objects. It locates inefficient patterns and suggests changes to improve efficiency. The defects reported by this checker do not address program correctness, only inefficient use of resources.
    - Now enables the C++ checker `INCOMPLETE_DEALLOCATOR` by default. This checker reports resource leaks in pairs of allocation and deallocation functions linked to structures.
    - Support for Scala in Coverity Quality checkers has been deprecated, and will be removed in a future release of Coverity Analysis.
    - A new option was added for the `REVERSE_INULL` checker: `report_asserts_regex`. It can be used to check inside macros. The user can use `report_asserts_regex:fatal_if|fatal` to check inside their macros and find these cases. See documentation for a more detailed explanation.
    - The `UNLOCKED_ACCESS` now always considers static initializers to be thread-safe.
    - Added a checker option to `INTEGER_OVERFLOW` to allow the customer to suppress defect reports involving unsigned values being cast to signed values of the same size when the value itself does not fit in the signed type. This invokes implementation-defined behavior.
    - Improved the `OVERRUN` checker to avoid false positives when using the linux `for_each_cpu` macro.
    - Added support for erase through iterator's value such as map::erase(it->second) in the `INVALIDATE_ITERATOR` checker.
    - Added a new property to CodeXM tokens that allows finding matches for a particular regex in the token's text.
    - The `XML_INJECTION` checker now supports Go and Kotlin.
    - The `SQL_NOT_CONSTANT` checker now supports Kotlin.
    - The SSRF checker is now enabled with `--webapp-security`. [Java]
    - Fixed a source of `RESOURCE_LEAK` false positives when using the `WRDE_REUSE` flag to glibc `wordexp`.
    - Fixed an assertion failure involving the constraint FPP.
    - General improvements to `INTEGER_OVERFLOW`.
    - An issue with `RESOURCE_LEAK` related to TEE library function `TEE_AllocatePropertyEnumerator` is fixed
    - Created a built-in model for `socketpair(2)`.
    - Improved the built-in model for `recvmsg(2)`.
    - `BUFFER_SIZE` reports a defect when using the source buffer's length as a parameter in size buffer functions and interprocedural defects generally.
    - Fixed an issue that could cause `RESOURCE_LEAK` false positives when using pointer arithmetic and the `?:` operator.
    - Fixed an issue where range-based 'for' loop would incorrectly add a level of nesting to `HIS_LEVEL`.
    - A `NULL_RETURNS` FN issue with the Java Collection classes is fixed.
    - Improved `BUFFER_SIZE`'s ability to understand array and pointer offsets.
    - Fixed an issue in `INCOMPLETE_DEALLOCATOR` when a linked list is built through multiple layers of nested structs.
    - Fixed an issue related to locating allocators for the `INCOMPLETE_DEALLOCATOR` checker.
    - Fixed a source of `NO_EFFECT` false positives when accessing a static object through an instance, when using a clang-based compiler.
    - Fixed an issue where the `DIVIDE_BY_ZERO` checker could cause significant performance degradation in the presence of `nan` values in the code.
    - Fixed a bug with the `XSS` checker leading to a recoverable error.

## September 2025

- Polaris now supports Rapid Scan Static (Sigma) 2025.9.0. This version has the following changes:
  - Validated support for Go 1.25.
  - C# taint-flow checkers now report cross-file defects.
  - A small number of C# `PATH_MANIPULATION` defects may now be reported as `URL_MANIPULATION` defects.
  - Sigma will no longer scan files inside Coverity intermediate directories.
  - Sigma supports the `base-check-set` option in the `coverity.yml` configuration file.
  - The `include_file_path` option now excludes files that don't match the given glob patterns. Previously this option would only override files that were excluded via other means.
- API endpoints to create and manage service accounts are available. Full support for service accounts (including updates to the Polaris user interface and API enhancements) will be available in a future update.

  See [Service accounts for Polaris](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/d9540d417e952b4580e8f0dd120ba6de.topic) for more information.
- Now, it's easier to monitor issue policy violations in the Polaris user interface:
  - The Policy Violations filter was added to the Issues tab. Use this filter to view issues that violate specific issue policies.
  - A policy status icon was added to the Issues tab, and appears next to issues that violate issue policies. Hover over the icon to see the names of issue policies an issue violates.
  - The names of issue policies a project violates appear when you select the info icon (in the Total Active Policy Violations column) on the Application page.

  Important: In order for policy names to appear when you open the Policy Violations filter, or select the info icon, you must retest your projects or triage an issue in your project.

  See [Monitor policies in Polaris](../how-to/create-and-manage-policies/monitor-policies-in-polaris.md) for more information.
- **Important**: The sunset date for deprecated endpoints in Polaris APIs was extended to **November 18, 2025, at 12:00 AM EST**. Deprecated endpoints in Polaris APIs, versions of the Bridge CLI older than 3.6.0, and versions of Code Sight older than 2025.4.0 will stop functioning on November 18, 2025. To avoid failures:
  - Update your API scripts before November 18, 2025
  - Upgrade to Bridge CLI 3.6.0 (or newer) before November 18, 2025
  - Upgrade to Code Sight 2025.4.0 (or newer) before November 18, 2025

  See [DELAYED DEADLINE to November 18, 2025 12:00am EST for Deprecated Polaris API Endpoints](https://community.blackduck.com/s/question/0D5Uh00000lyakJKAQ/announcement-delayed-deadline-to-november-18-2025-1200am-est-for-deprecated-polaris-api-endpoints-customer-action-required) in Black Duck Community, the [API reference guide](https://polaris.blackduck.com/developer/default/documentation), [Download Bridge CLI](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/5cc6965a2886bd9786bae37cd8607e8e.topic), and [Installing Code Sight](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/cda9d356f5606c3d361c83423b60679d.topic&Version=latest) for more information.
- Now, you can have up to 1000 saved reports at a time (previously, 500).
- Polaris now supports Rapid Scan Static (Sigma) 2025.8.0. This version:
  - Adds Python taint flow checkers.
  - Deprecates support for MacOS 12.x, MacOS 13.x, Windows Server 2016 and Windows Server 2019.
  - Fixed an issue where Sigma would incorrectly return an error for valid uses of `analyze.checkers.webapp-security` in the configuration file.
- **Reminder**: Deprecated endpoints in Polaris APIs, versions of the Bridge CLI older than 3.6.0, and versions of Code Sight older than 2025.4.0 will stop functioning on September 15, 2025. To avoid failures:
  - Update your API scripts before September 15, 2025
  - Upgrade to Bridge CLI 3.6.0 (or newer) before September 15, 2025
  - Upgrade to Code Sight 2025.4.0 (or newer) before September 15, 2025

  See [Reminder: September 15, 2025 DEADLINE](https://community.blackduck.com/s/question/0D5Uh00000lkuqrKAA/announcement-reminder-september-15-2025-deadline-polaris-api-deprecations-and-important-due-dates-for-api-and-bridge-upgrade-requirements) in Black Duck Community, the [API reference guide](https://polaris.blackduck.com/developer/default/documentation), [Download Bridge CLI](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/5cc6965a2886bd9786bae37cd8607e8e.topic), and [Installing Code Sight](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/cda9d356f5606c3d361c83423b60679d.topic&Version=latest) for more information.
- Application Members can now add, update, and delete manually-added components. Previously, these actions were restricted to Organization Administrators, Organization Application Managers, Application Admins, and Application Contributors.
- **Reminder**: Deprecated endpoints in Polaris APIs, versions of the Bridge CLI older than 3.6.0, and versions of Code Sight older than 2025.4.0 will stop functioning on September 15, 2025. To avoid failures:
  - Update your API scripts before September 15, 2025
  - Upgrade to Bridge CLI 3.6.0 (or newer) before September 15, 2025
  - Upgrade to Code Sight 2025.4.0 (or newer) before September 15, 2025

  See [Reminder: September 15, 2025 DEADLINE](https://community.blackduck.com/s/question/0D5Uh00000lGI9WKAW/announcement-reminder-september-15-2025-deadline-polaris-api-deprecations-and-important-due-dates-for-api-and-bridge-upgrade-requirements) in Black Duck Community, the [API reference guide](https://polaris.blackduck.com/developer/default/documentation), [Download Bridge CLI](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/5cc6965a2886bd9786bae37cd8607e8e.topic), and [Installing Code Sight](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/cda9d356f5606c3d361c83423b60679d.topic&Version=latest) for more information.
- The OWASP® Top 10 API Security Risks 2023 standard is now supported in Polaris. You can filter by this standard wherever standard filters are available.

## August 2025

- Now, you can set up triage approval workflows to ensure proper governance of issue and component triage activities. With this feature, you can require designated approvers to review and approve triage actions (like dismissing issues or excluding components from your SBOM) before they take effect. You can create custom roles that grant users permissions to approve issue and component triage requests. Configure approval workflows at the organization, application, or project level.

  See [Set up triage approval workflows](../how-to/set-up-triage-approval-workflows.md) for more information.
- Black Duck Assist (Beta) now leverages Polaris documentation when generating responses. This enhancement allows Black Duck Assist to provide product guidance and best practices in responses.
- **Reminder**: Deprecated endpoints in Polaris APIs, versions of the Bridge CLI older than 3.6.0, and versions of Code Sight older than 2025.4.0 will stop functioning on September 15, 2025. To avoid failures:
  - Update your API scripts before September 15, 2025
  - Upgrade to Bridge CLI 3.6.0 (or newer) before September 15, 2025
  - Upgrade to Code Sight 2025.4.0 (or newer) before September 15, 2025

  See [Reminder: September 15, 2025 DEADLINE](https://community.blackduck.com/s/question/0D5Uh00000kXu7OKAS/announcement-reminder-september-15-2025-deadline-polaris-api-deprecations-and-important-due-dates-for-api-and-bridge-upgrade-requirements) in Black Duck Community, the [API reference guide](https://polaris.blackduck.com/developer/default/documentation), [Download Bridge CLI](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/5cc6965a2886bd9786bae37cd8607e8e.topic), and [Installing Code Sight](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/cda9d356f5606c3d361c83423b60679d.topic&Version=latest) for more information.
- Now, you can use AI-assisted Authentication for fAST Dynamic (early access) to automate the login process for DAST tests on web application targets. You only need to provide a login URL, site credentials, and optional MFA details. Using a Black Duck hosted LLM, AI-assisted Authentication analyzes screenshots and UI elements, auto-detects the site's login sequence, and configures authentication settings. It then logs in automatically to allow DAST testing to start.

  Note: This feature is currently in Early Access. Configuration is supported via updates to the scan settings JSON configuration file. The Polaris Web UI will be updated in a future release.

  See [Use AI-Assisted Authentication](../how-to/test-web-applications-and-apis-with-polaris-fast-dynamic/use-ai-assisted-authentication.md) for more information.
- Multi-factor authentication (MFA) support is now available for DAST tests, including:
  - Time-based One-Time Password (TOTP) MFA: Authenticate to web applications that use standard TOTP multi-factor authentication by providing the secret key in your scan settings. The implementation supports standard TOTP parameters with SHA-1 hash algorithm, 6-digit codes, and 30-second time steps.
  - Email MFA: Authenticate to web applications that send one-time codes via email during the login process. Each DAST project is assigned a unique email address that can receive authentication codes from your application.

  See Authentication profiles for MFA for more information.
- Chrome Recording authentication is now available for DAST tests. This feature allows you to capture complex authentication workflows using the Chrome DevTools Recorder and use the exported recording to authenticate to your web application during DAST scans. Chrome recordings can handle complex multi-step authentication flows and applications with dynamic elements.

  See Chrome Recording for more information.
- Polaris now supports Coverity 2025.6.2. It includes the following changes:
  - Added support for C# 13.
  - Added support for Go 1.24.
  - Added support for Java 24.
  - Added support for Clang 19.
  - Added support for Oracle JDK 24.
  - Added support for OpenJDK 24.
  - Support for macOS 13 is deprecated and will be removed in a future release.
  - Support for Windows 10 is deprecated and will be removed in a future release.
  - Support for Go 1.23 is deprecated and will be removed in a future release.
  - Support for Android NDK revision r21e (Clang 9.0) is deprecated and will be removed in a future release.
  - Support for Go 1.22 has been removed.
  - Support for LLVM Clang 9.0 has been removed.
  - Support for Oracle JDK 23 has been removed.
  - Support for OpenJDK 23 has been removed.
  - **Checker Information:**
    - The `INCOMPLETE_DEALLOCATOR` checker locates C-language equivalent functions to the C++ concepts of constructors and destructors.
    - The `RESOURCE_LEAK` checker now reports cases where an allocation happens inside a switch case, controlled by the new checker option track\_allocations\_in\_switches. This option is enabled by default.
    - Fixed a pattern of `NO_EFFECT` false positive in JavaScript involving "strict mode" directives and import statements.
    - When set to `true`, the `USE_AFTER_FREE:report_out_parameter_free` checker option will report a defect whenever a function's pointer argument is written to and later freed.
    - Improved the handling of small negative numbers in INTEGER\_OVERFLOW, to better handle functions that can return a negative error code, but which otherwise only return positive values.
    - Added new checker `SSRF` for Java. CWE 918 is now supported.
    - Improved remediation guidance for the `URL_MANIPULATION` checker. [Java/C#]
    - Improved remediation guidance for the `PATH_MANIPULATION` checker. [C#]
    - Fixed a false positive for the `PATH_MANIPULATION` checker. [C#]
    - A new quality checker, `REVERSE_INVALID_ITERATOR`, finds defects where iterator is first dereferenced and then checked for validity.
- Now, it's easier to monitor component policy violations in the Polaris user interface:
  - The Policy Violations filter was added to the Components tab. Use this filter to view components that violate specific component policies.
  - A policy status icon was added to the Components tab, and appears next to components that violate component policies. Hover over the icon to see the names of component policies a component violates.
  - An info icon was added to the Total Active Policy Violations column on the Application page. Select the icon to view the names of component policies a project violates.

  See [Monitor policies in Polaris](../how-to/create-and-manage-policies/monitor-policies-in-polaris.md) for more information.
- Enhanced SCM repository integration capabilities (currently limited to GitHub and GitHub Enterprise repositories only):
  - Now, you can synchronize Polaris with your GitHub provider to automatically track changes to your repositories and branches. When enabled, Polaris monitors your GitHub repositories for updates, deletions, or renames and automatically applies these changes to the corresponding projects and branches in Polaris. See [Synchronizing Polaris with your SCM Provider](../how-to/synchronizing-polaris-with-your-scm-provider.md) for more information.
  - Event-based test automation allows you to automatically run tests when pull requests are created, updated, or merged in GitHub. You can configure these settings at the organization, application, project, or branch level. See [Event-Based Test Automation in Polaris for SCM Integrations](../how-to/event-based-test-automation-in-polaris-for-scm-integrations.md) for more information.
  - The personal access token used for SCM integration with GitHub requires additional scopes (`read:org` and `admin:org_hook`, in additon to `repo`).
- The behavior of report configurations has changed. If an application, project, branch, or label that is included in the scope of a report configuration is deleted, the report fails to run, and you get an “invalid report scope” error message on the Latest Reports tab. Previously, the report would be generated, but the data from the deleted object was removed from the report scope.
- Polaris supports Rapid Scan Static (Sigma) 2025.7.1. This version:
  - Adds support for the Go programming language.
  - Validated support for Kotlin 2.2, Dart 3.8, and recent infrastructure as code languages (Dockerfile and Terraform HCL).
  - Added the `path_manipulation`, `sensitive_data_leak`, and `trust_boundary_violation` taint-flow checkers for Java.
  - Fixed a `harcoded_secrets` false positive where a full sentence is being detected as a password.
  - Fixed a `hardcoded_secrets` false positive that reported issues in `.npmrc` files.
  - Fixed a `hardcoded_secrets` false positive that reported on variables holding password titles or fields.
- **Important**: Deprecated endpoints in Polaris APIs, versions of the Bridge CLI older than 3.6.0, and versions of Code Sight older than 2025.4.0 will stop functioning on September 15, 2025. To avoid failures:
  - Update your API scripts before September 15, 2025
  - Upgrade to Bridge CLI 3.6.0 (or newer) before September 15, 2025
  - Upgrade to Code Sight 2025.4.0 (or newer) before September 15, 2025

  See [Reminder - Polaris API Deprecations and Important Due Dates for API and Bridge Upgrade Requirements](https://community.blackduck.com/s/question/0D5Uh00000ix5u5KAA/announcement-reminder-polaris-api-deprecations-and-important-due-dates-for-api-and-bridge-upgrade-requirements) in Black Duck Community, the [API reference guide](https://polaris.blackduck.com/developer/default/documentation), [Download Bridge CLI](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/5cc6965a2886bd9786bae37cd8607e8e.topic), and [Installing Code Sight](https://docs.blackduck.com/access?ft:originId=e5be419b9a362d8c0118eeab3a8ee157/cda9d356f5606c3d361c83423b60679d.topic&Version=latest) for more information.
- The availability of Synopsys domains was extended to September 30, 2025. For more information, see [Migrate Polaris to the Black Duck domain](../how-to/migrate-polaris-to-the-black-duck-domain.md).
- The [Black Duck Security App for GitHub](https://github.com/marketplace/black-duck-security) is available. This app provides a streamlined user interface for configuring security scans across your GitHub repositories. With this app, you can generate and deploy workflows to multiple repositories at once, configure scan options through a user-friendly interface, and review workflows before deployment. See [GitHub App – Black Duck Security](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/6177ea380f30fe0aaaa52d2ecd6901e2.topic) for more information.
- AI-assisted Authentication for fAST Dynamic (Early Access) is now available. This feature uses machine learning, computer vision techniques, and a large language model to automate the login process for DAST tests on web application targets. The feature can handle:
  - Simple form-based authentication with username and password (single and multi-page login sequences)
  - Multi-factor authentication including time-based one-time passwords (TOTP) and email MFA

  See [Use AI-Assisted Authentication](../how-to/test-web-applications-and-apis-with-polaris-fast-dynamic/use-ai-assisted-authentication.md) for more information.
- Polaris supports Black Duck Bridge CLI 3.7.1. Now, if you attempt to run a Rapid Scan Static test before a full SAST test (using the latest version of Coverity that Polaris supports) is completed, Bridge starts a full SAST scan automatically.

  Important: Now, when using older versions of the Bridge CLI, if you request a Rapid Scan Static test before a full SAST test is completed, the test will not run.

## July 2025

- Polaris supports Black Duck® Bridge CLI 3.7.0. Now, you can start DAST tests from pipelines using the Bridge CLI. When you test internal targets from the Bridge CLI, the Bridge CLI runs Secure Tunnel automatically (provided your system meets the [System requirements](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/ae8dc35e863863d358eb74906b7d6359.topic) for Secure Tunnel). See [DAST configuration requirements](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0c68b6621951399783959d99c58930be.topic) for more information.
- Polaris Assist has been rebranded as Black Duck Assist. Today, two Black Duck Assist features are available in Polaris:
  - Generating SAST remediation guidance

    Note: Generating SAST remediation guidance is now generally available, having completed its Beta phase.
  - Using natural language queries to gain insight into your organization's data (beta)
- Organization Administrators can create Labels on the My Organization page.

  Users can apply labels to applications, projects, and branches to categorize them in ways that make sense to your organization, such as by business unit, development team, or environment. This enables filtering, navigation, and reporting enhancements, including the ability to:

  - Filter applications by label
  - Filter projects by label
  - Adjust the scope of a report to applications, projects, or branches matching a specific label

  See [Create and manage labels](../how-to/create-and-manage-labels.md) for more information.

  Note: Labels have replaced Application Tags in the Polaris UI. Tags you previously assigned to your applications will be converted to labels automatically. Support for searching your Portfolio by label will be added in a future release.
- Endpoints used to manage tags (found in the [Portfolio](https://polaris.blackduck.com/developer/default/documentation/portfolio) API) are deprecated, and will be sunset on September 15, 2025. Update your scripts before September 15, 2025 to avoid failures.

  Important: New tags you create using the deprecated endpoints will not be converted to labels, or appear in the Polaris user interface. New labels you create will not be converted to tags.

  Deprecated tag endpoints are listed below:

  - `GET /api/portfolios/tags`
  - `POST /api/portfolios/applications/{id}/tags`
  - `PUT /api/portfolios/applications/{id}/tags`
  - `GET /api/portfolios/applications/{id}/tags`
- New options to manage the scope of a report have been added to the Create Report page. These allow you to filter which applications, projects, and branches you want to include in reports. You can select from the following options:
  - All applications and projects (default branches/profiles only)
  - Applications, projects and branches/profiles matching specific filters (non-IDE branches only): Create a filter to select applications, projects, and branches to include in the report. Optionally, refine your selection using branch-specific labels.
  - Specific project branches/profiles: Create a filter to select specific branches to include in the report. Optionally, refine your selection using branch-specific labels. This option also allows you to include or exclude IDE branches from the filter.

  Once you have adjusted the report scope, you can create a report configuration to save your selected filters. See [Create a report](../how-to/create-a-report.md) for more information.
- First detected dates, triage statuses, and owners were added to the Issue List tab (found in the Issue Summary Dashboard).
- Now, you can manually manage components in your projects' software bill of materials (SBOM). This includes:
  - Adding components that aren't captured in tests to assess their risk before you use them.
  - Modifying components captured in tests (including selecting a specific component origin for components with multiple origins).
  - Deleting components that you've added manually.

  See [Add or modify components](../how-to/add-or-modify-components.md) for more information.
- A new instance of Polaris is available in the Kingdom of Saudi Arabia (KSA) region. Now, users in the Middle East have access to a regionally-optimized instance, reducing latency and improving performance.
  - KSA instance URL: <https://ksa.polaris.blackduck.com>
  - To ensure Polaris functions correctly in the KSA region, add the IPs listed on Polaris IP ranges to your allow list.
- **Reminder**: Deprecated endpoints in Polaris APIs will stop functioning on September 15, 2025. Update your scripts before September 15, 2025 to avoid failures.

  See [Reminder - Polaris API Deprecations and Important Due Dates](https://community.blackduck.com/s/question/0D5Uh00000gdoMpKAI/announcement-reminder-polaris-api-deprecations-and-important-due-dates) in Black Duck Community and the [API reference guide](https://polaris.blackduck.com/developer/default/documentation) for more information.
- Polaris supports Black Duck® Bridge CLI 3.6.0.
- Polaris now supports Rapid Scan Static as a standalone SAST analysis engine through the Bridge CLI (for instructions, see [Using Rapid Scan Static with Bridge](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/cea065ce813ed8815a6bc8909bd20795.topic)). Rapid Scan Static tests provide quick actionable results, whereas full SAST tests can provide more in-depth but time-consuming analysis. With this feature, you can run a full SAST scan for the first time or at build for the in-depth analysis followed by a rapid scan for quick results as part of subsequent pull request workflows. New filters are available in the tests, issues, and report configuration views to identify issues specifically found by Rapid Scan Static.

  Important: Ensure that a full SAST scan of the project is completed before using Rapid Scan Static to test a project. The full SAST scan **must** be run with the latest version of Coverity, before performing a Rapid Scan Static test. If you perform a Rapid Scan Static test before a full SAST scan has been completed, duplicate issues will be created when you run a full SAST test.
- Polaris now supports Rapid Scan Static (Sigma) as a stand-alone engine starting with version 2025.6.0. Rapid Scan Static scans are supported using the Black Duck Bridge CLI integration and are no longer automatically bundled with the Coverity version.
- Polaris supports the beta version of Insights NLQ (natural language queries). To enable Insights NLQ, go to My Organization > Black Duck Assist.
- The **Remediation Dashboard** is available. The new dashboard shows the average time required to remediate issues in your portfolio.
- Polaris supports Black Duck® Detect 10.4.0. It includes the following changes:
  - Updated the Conan 2 detector to provide log entries in case of error.
  - Extends Conda support to 25.1.1.
  - Added support for the Cargo CLI detector. The Cargo CLI detector uses `cargo tree` to extract direct and transitive dependencies, offering improving accuracy over the previous flat lockfile detection. This build-based detector is triggered for Cargo projects with a `Cargo.toml` file and requires Cargo version **1.44.0+**. For further information, see [Cargo package manager support](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/9b5e5b2ce6ee3bbd18c13256c6a2dec8.topic&Version=latest).
  - Added the [detect.cargo.path](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/3ec7ee2c7fa1f21d7930de92c4a90170.topic&Version=latest) property, which allows you to specify a custom Cargo executable path.
  - Added support for `ArtifactsPath` and `BaseIntermediateOutputPath` properties in Black Duck Detect NuGet Inspector. See [detect.nuget.artifacts.path](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/4c32600833bb2d93b8d644f81e7cfa55.topic&Version=latest) for more details.
  - New `detect.pnpm.included.packages` and `detect.pnpm.excluded.packages` properties for pnpm provide increased control over what directories Detect scans under a pnpm project. See the [pnpm](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/132e1bdca1a225f026bd643f0a819952.topic&Version=latest) property page for more information.
  - Use of the `--detect.yarn.ignore.all.workspaces` flag is not required for Yarn 4 projects, thus configuration parameters such as `--detect.yarn.dependency.types.excluded=NON_PRODUCTION` can be employed.
  - ID strings of detected Yarn project dependencies are now correctly formed. Related warning messages have been improved to identify entries in the yarn.lock file that have not been resolved through package.json files and could not be resolved with any standard NPM packages.
  - Improved the Yarn detector to handle non-standard version entries for component dependencies.
  - The PIP Native Inspector now supports Python 3.12+.
  - Detect will now return a unique error code (`code 16 - FAILURE_OUT_OF_MEMORY`) when sub processes experience "Out of memory" issues.
  - Improved handling of pnpm packages that contain detailed version information in the `pnpm-lock.yaml`. Resolving Detect missing some packages through failure to link direct and transitive dependencies.
  - Resolved a Go dependency scan issue that resulted in transitive dependencies assigned to incorrect parent. (For further details on how the Go Mod CLI detector determines parents, see [GoLang support](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/a386ee865aae7c017fc2b96a3f11cf8d.topic&Version=latest).)
  - Resolved an issue with Detect Gradle Native Inspector causing scans to hang indefinitely when submodule has the same name as the parent module.
  - Resolved Detect failing to handle duplicate keys in `package.json` files across npm, pnpm, Lerna, and Yarn projects.
  - Resolved an issue where Detect would exit with a 0 (zero) success code despite dependency requirements not being met for the PIP Native Inspector. The PIP Native Inspector will yield to other detectors when it cannot resolve an expected dependency from the PIP cache.
- Now you can use application risk scoring to qualify the significance of applications in your portfolio with risk factors you define. After you enable application risk scoring, Polaris assigns a composite score (ranging between 0–100) to each application in your Portfolio. Higher risk scores indicate an application's vulnerabilities pose a larger threat to your organization.

  See [Risk scoring in Polaris](../how-to/risk-scoring-in-polaris.md) for more information.

## June 2025

- Issues captured using fAST Dynamic include evidence, such as the API endpoint, payload, and target. Now, this information is included when you export DAST issues to Azure DevOps or Jira. You'll find DAST-specific evidence in the Evidence section of the ticket description.

  See [Issue tracking integrations](../how-to/issue-tracking-integrations.md) for more information.
- Now you can set up file and folder exclusion rules to ignore SAST issues (including SAST issues imported from third-party tools) associated with files in your projects. Excluded files are hidden in the Polaris user interface, do not count as policy violations, and won't be tagged with pull request comments.

  See [Exclude files and folders from tests](../how-to/exclude-files-and-folders-from-tests.md) for more information.
- **Reminder**: Deprecated endpoints in Polaris APIs will stop functioning on September 15, 2025. Update your scripts before September 15, 2025 to avoid failures.

  See [Reminder - Polaris API Deprecations and Important Due Dates](https://community.blackduck.com/s/question/0D5Uh00000e8ShfKAE/announcement-reminder-polaris-api-deprecations-and-important-due-dates) in Black Duck Community and the [API reference guide](https://polaris.blackduck.com/developer/default/documentation) for more information.
- A mandatory maintenance update was applied to the Teleport Agent bundled with Polaris Secure Tunnel (used to run DAST tests on targets inside a private network). Please restart any active Secure Tunnel sessions to use the latest version (no configuration changes required).

  See [Connect to an internal DAST target from the Bridge CLI](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/13132819f3ced5c3e7fdea47460c8d65.topic) for more information.

## May 2025

- Polaris supports Black Duck® Bridge CLI 3.5.1.
- Polaris now supports Coverity 2025.3.0. It includes the following changes:
  - Added support for Kotlin 2.1.0.
  - Added support for GNU GCC 14.1.
  - Added support for .NET 9.0.
  - Added support for Bazel 8.
  - Support for Go 1.22 is deprecated and will be removed in a future release.
  - Support for Kotlin 2.0.x is deprecated and will be removed in a future release.
  - Support for Oracle JDK 23 is deprecated and will be removed in a future release.
  - Support for OpenJDK 23 is deprecated and will be removed in a future release.
  - Support for Kotlin 1.9 has been removed.
  - Support for JSHint has been removed.
  - **Checker Information:**
    - Detekt and Spotbugs are now disabled by default for the default workflow. They can be enabled with `--enable-spotbugs` or `--enable-detekt`.
    - Added a new primitive and annotation to allow suppression of `CHECKED_RETURN` defects.
    - Fixed a source of `FORWARD_NULL` false positives when taking the address of element 0 of a null array.
    - A new checker option `REPORT_UNPROTECTED_INDEXING` reports any indexing where there is no local checking of the index range.
    - Improved the event text associated with an `INTEGER_OVERFLOW` defect pattern to better explain the defect.
    - The `DEADCODE` checker now leverages more information about set and unset bits.
    - The `NULL_FIELD` checker is now enabled by default for C, C++, and CUDA.
    - In `INTEGER_OVERFLOW`, do not immediately report a defect on the overflow of an unsigned value. Instead, wait until that value is used in a sensitive context. The former behavior can be recovered with a new checker option: `report_unsigned_overflow_immediately`.
    - The `URL_MANIPULATION` checker now supports C# and Visual Basic.
    - The `OS_CMD_INJECTION` checker was enhanced to address some false negatives for Java, C# and Visual Basic.
    - Fixed a false negative for the `XSS` checker. [Go]
    - Fixed a false negative for the `OS_CMD_INJECTION` checker. [Python]
  - Included in this update are changes from Coverity 2024.12.1:
    - Fixes bug in Coverity 2024.12.0 where Kotlin-only projects on Polaris did not show any issues.
- **Reminder**: Deprecated endpoints in Polaris APIs will stop functioning on September 15, 2025. Update your scripts before September 15, 2025 to avoid failures.

  See [Reminder - Polaris API Deprecations and Important Due Dates](https://community.blackduck.com/s/question/0D5Uh00000b67RJKAY/announcement-reminder-polaris-api-deprecations-and-important-due-dates) in Black Duck Community and the [API reference guide](https://polaris.blackduck.com/developer/default/documentation) for more information.
- The `POST /configurations/{id}/issues-export` endpoint (found in the [Bug Tracking Integration](https://polaris.blackduck.com/developer/default/documentation/bug-tracking-integration) API) was enhanced. Now (in addition to creating tickets in Jira and Azure DevOps), you can use this endpoint to link issues in Polaris to preexisting tickets in Jira or Azure DevOps.
- The [Black Duck Polaris YouTube channel](https://www.youtube.com/@BlackDuckPolaris) is available. Here, you'll find helpful overviews of Polaris' major features, and new videos will be posted when major features are released. Subscribe and enable post notifications to be notified whenever new videos are posted.
- The sunset date for deprecated endpoints in Polaris APIs was extended to September 15, 2025. Scripts that call deprecated endpoints must be updated before September 15 to avoid failures.

  See the [API reference guide](https://polaris.blackduck.com/developer/default/documentation) for more information.

## April 2025

- Bitbucket users can now use the Black Duck Security Scan Pipe to automate Polaris tests in Bitbucket Pipes.

  See [Bitbucket – Black Duck Security Scan Pipe](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/211ac3b53bbc29ae8d23708b9d6840ba.topic) for more information.
- Now, Organization Administrators can create custom application-level roles.

  See [Manage permissions with custom roles](../how-to/manage-permissions-with-custom-roles.md) for more information.
- The software bill of materials (SBOM) report now supports CycloneDX v1.6 (in addition to v1.4). You can now select from multiple versions of CycloneDX when generating the SBOM report.

  See Create a software bill of materials report for more information.

## March 2025

- With Bridge CLI 3.4.0, you can run both types of SCA tests (package manager and signature scans) in the same pipeline. To run both, set `polaris.tests.sca.type` to `SCA-PACKAGE, SCA-SIGNATURE`.

  See [Using Bridge CLI with Polaris](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0c68b6621951399783959d99c58930be.topic) and [Complete List of Bridge Arguments](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/104e9b8ad79809821c6b1e50bb52508d.topic) for more information.
- Polaris supports Black Duck Bridge CLI Bundle 3.4.0.
- The SCAN\_CLI (a utility the Bridge CLI downloads when running signature scans) was upgraded to version 2025.1.1.
- The status page for Polaris migrated to a new domain. Find it here: <https://status.polaris.blackduck.com>.
- Now, you can create a Developer Detail Dynamic Report that provides an overview of the issues in the selected application(s) including details that will help developers select what to focus on.
- The Dashboards page has a new look and feel.
  - Now, when you open the Dashboards page, you won't be redirected to a third-party service. You can remove the following domains and IPs from your allow list:
    - https://polaris.sisense.com (formerly, https://synopsys.sisense.com), 54.188.167.106
    - https://poc-polaris.sisense.com (formerly, https://synopsys-se.sisense.com), 35.81.206.33
    - https://eu-polaris.sisense.com (formerly, https://synopsys-ie.sisense.com), 52.30.201.44
  - Please note:
    - Custom filters set in the old Dashboards page will need to be reapplied after the upgrade.
    - Image exports don't work in Firefox.

  See [Work with dashboards](../how-to/work-with-dashboards.md) for more information.

## February 2025

- Polaris supports Black Duck Bridge CLI Bundle 3.3.0 and Bridge CLI Thin Client 3.0.18.
- Black Duck will update server certificates for the polaris.synopsys.com domain on March 5, 2025. If you haven't migrated your Polaris tenant to the new Black Duck domain, you will need to update trusted certificates for Polaris to avoid potential SSL/TLS errors.

  Find instructions to update trusted certificates in Black Duck Community: [Scheduled Certificate Updates for Coverity on Polaris and Polaris on March 5, 2025](https://community.blackduck.com/s/question/0D5Uh00000UlyuKKAR/operational-announcement-scheduled-certificate-updates-for-coverity-on-polaris-and-polaris-on-march-5-2025).
- The [Tests](https://polaris.blackduck.com/developer/default/documentation/tests) API was restructured to improve usability. This includes:
  - Changing each endpoint's base path from `/api/test-manager` to `/api/tests`.
  - Updating terminology used in endpoint paths to improve clarity and consistency.
  - Deprecating endpoints that reference the old base path. Deprecated endpoints have `deprecation` and `sunset` headers. They will not be available after "Mon, 15 Sept 2025 23:59:59 GMT" (sunset date).
- The [Repos Integration](https://polaris.blackduck.com/developer/default/documentation/repos-integration) API was restructured to improve usability. This includes:
  - Changing each endpoint's base path from `/api/scm` to `/api/integrations/repos`.
  - Updating terminology used in endpoint paths to improve clarity and consistency.
  - Deprecating endpoints that reference the old base path. Deprecated endpoints have `deprecation` and `sunset` headers. They will not be available after "Mon, 15 Sept 2025 23:59:59 GMT" (sunset date).
- We're extending the availability of <https://sig-repo.synopsys.com> to March 31, 2025. To ensure Polaris and the Bridge CLI continue to function as expected, keep <https://sig-repo.synopsys.com> (34.110.245.127) on your allow list until March 31, 2025.
- Now, you can use the Attempt Build Break action with component policies. This allows you to break builds in your CI system (using Bridge CLI Bundle 3.2.0 or later, or Bridge CLI Thin Client 3.0.16 or later) when components with specific properties are detected in an SCA test.

  Note: See [Component policies](../how-to/create-and-manage-policies/component-policies.md) for more information.
- Polaris supports Black Duck Bridge CLI Bundle 3.2.0 and Bridge CLI Thin Client 3.0.16.
- Now, you can search through the Polaris documentation from the Polaris user interface. After you sign in to Polaris, select the Help [image: help icon] icon (in the banner) to reveal the search panel. Links in the search panel direct you to documentation in the Black Duck documentation portal, the common documentation platform for Black Duck products. Documentation for Polaris is divided into two sets:
  - [Polaris user documentation](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/dce6ee4226e0067782f65e5feb6313df.topic)
  - [Polaris continuous integration documentation](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/cd6ad452381a0099cb4d143a5cad6fba.topic)

  Note: After you open the search panel, you can select the Need additional help or support? button (near the bottom of the panel) to find links to API references, Black Duck Community, and support.
- After you set up an issue tracking integration, DAST issues can be exported to Azure DevOps or Jira (in addition to SAST and SCA issues).

  Note: See [Export an issue to Azure DevOps or Jira](../how-to/issue-tracking-integrations/export-an-issue-to-azure-devops-or-jira.md) for more information.
- Polaris support Black Duck Detect 10.1.0. It includes the following changes:

  - Extends BitBake support to 2.8.0 (Yocto 5.0.3).
  - Extends Dart support to 3.5.0 (Flutter 3.22.2).
  - Extends Go Modules support to 1.22.7.
  - Extends Gradle support to 8.10.1.
  - Extends Lerna support to 8.1.8.
  - Extends Maven support to 3.9.9.
  - Extends npm support to 10.8.2 (Node.js 22.7.0).
  - Extends pip support to 24.2 (with Pipenv 2024.0.1).
  - Extends pnpm support to 9.0.0.
  - The npm package.json detector now performs additional parsing when attempting to find dependency versions. This can result in additional matches since versions like `^1.2.0` will now be extracted as `1.2.0` instead of as the raw `^1.2.0` string. In the case where multiple versions for a dependency are discovered, the earliest version will be used.
  - The `.blackduck` temporary folder has been added to the default exclusion list.
  - npm lockfile and shrinkwrap detectors now ignore packages flagged as extraneous in the package-lock.json and npm-shrinkwrap.json files.
  - The new [detect.gradle.root.only](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/585be62266ac8f9b8c042e2dd4daa7e7.topic&Version=latest) option (for the Gradle Native Inspector) allows you to only process the root.
  - Changed Black Duck Detect's JAR signing authority from Synopsys, Inc. to Black Duck Software, Inc.
  - Detect eliminates null (`\u0000`) and replacement (`\uFFFD`) characters during the processing of Python requirements.txt files to ensure successful extraction of dependency information.
  - Upgraded Project Inspector to v2024.12.1.

## January 2025

- The issue tracking integration for Azure DevOps is available. Once configured, the issue tracking integration allows Polaris to create tickets in Azure DevOps for issues captured in Polaris.

  Note: See [Issue tracking integrations](../how-to/issue-tracking-integrations.md) and Issue tracking integration for Azure DevOps for more information.
- Soon, the status page for Polaris (https://systemstatus.polaris.synopsys.com) will migrate to <https://status.polaris.blackduck.com>. The IPs for the status page will not change.
- Now, SAST and SCA issues you import from third-party tools appear in reports and dashboards (along with information about external analysis tests run in your organization).
  - At this time, SCA issues you import from third-party tools are not associated with components or licenses.
  - The ability to import issue data from third-party tools is available on a limited basis, and is not generally available. Please contact your account teams for more information.
- Polaris now supports Coverity 2024.12.0. It includes the following changes:
  - Added support for macOS 15.
  - Added support for Go 1.23.
  - Added support for Java 23.
  - Added support for Xcode 16.0.
  - Added support for Open/Oracle JDK 23.
  - Support for Go 1.22 is deprecated and will be removed in a future release.
  - Support for JSHint is deprecated in Coverity 2024.12.0 and will be removed in Coverity 2025.3.0.
  - Support for macOS 12 has been removed.
  - Support for Go 1.21 has been removed.
  - Support for Java 22 has been removed.
  - Support for Open/Oracle JDK 22 has been removed.
  - Support for .NET 6 has been removed.
  - The following information is only relevant to customers who use the following checkers:
    - The `OVERRUN` checker has been updated so that it handles cases where a condition that controls the increment of an offset is unchanged within a loop. (C/C++)
    - Coverity CLI will now enable the Android security and Web application security checkers by default instead of enabling all security checkers by default. In terms of the arguments passed to `cov-analyze`, instead of passing`-\-all-security` by default, the Coverity CLI will now pass `-\-android-security -\-webapp-security -\-webapp-security-aggressiveness-level low` by default.
    - Added a new early access C/C++ and Java checker, `NULL_FIELD`.
    - The `NULL_RETURNS` and `FORWARD_NULL` checkers no longer report defects on variables asserted as non-null with AssertJ. (Java)
    - The `RESOURCE_LEAK` checker can now track buffers allocated by the `scanf()` family of functions when using the `%m` dynamic allocation conversion specifier.
    - Improved the results of the `POINTER_NONDETERMINISM` checker. It now reports fewer false positives, and defects involving templates are reported in better locations.
    - Fixed a source of false negatives for the `UNSAFE_DESERIALIZATION` checker. (C#)
    - The `MASS_ASSIGNMENT` checker now supports JavaScript and TypeScript.
    - The `CSRF` checker now reports defects in jsp files. This behavior can be disabled using the `disable_jsp_analysis` option. (JavaScript)
    - The `SESSION_FIXATION` checker is now enabled by default for the Go language.
    - Data flow improvements for JavaSpring-related apps.
    - New malicious URL Sigma checker has been added.
    - `UNRESTRICTED_MESSAGE_TARGET` checker (JavaScript, Typescript) has been replaced by SIGMA checker `unrestricted_postmessage_target_javascript_window`.
    - `CONFIG.ENABLED_TRACE_MODE` checker (C#/.net config) has been replaced by SIGMA checker `trace_mode_enabled_aspnet_core_config`.
- Now, you automatically generate reports on a daily, weekly, or monthly basis. To do so, add a schedule to a report configuration.

  Note: See Add or modify a report configuration schedule for more information.
- A bug that caused CloudFlare IPs to appear in Audit Logs instead of user IP addresses is resolved.
- The [Portfolio](https://polaris.blackduck.com/developer/default/documentation/portfolio) API was restructured to improve usability. This includes:
  - Changing each endpoint's base path from `/api/portfolios` to `/api/portfolio`.
  - Updating terminology used in endpoint paths to improve clarity and consistency. This includes renaming "portfolio-items" to "applications," and "portfolio subitems" to "projects".
  - Deprecating endpoints that reference the old base path. Deprecated endpoints have `deprecation` and `sunset` headers. They will not be available after "Mon, 15 Sept 2025 23:59:59 GMT" (sunset date).

## December 2024

- **Correction:** To ensure Polaris and the Bridge CLI continue to function as expected, keep <https://sig-repo.synopsys.com> (34.110.245.127) on your allow list until February 14th, 2025. (POLDOCS-1025)
- Polaris now supports the **Secure Tunnel** solution for Polaris fAST Dynamic, a simple and secure way to scan internal web applications and APIs. This capability enables you to connect to applications within your private network, without the need to manage physical or virtual appliances or perform complex networking. Secure Tunnel opens a secure TLS connection between Polaris and the internal application, with all traffic securely tunneled through port 443. Secure Tunnel is integrated with Bridge CLI 3.1.0 and uses technology provided by Teleport, Inc.

  Note: See [Test internal DAST projects with Polaris Secure Tunnel](../how-to/test-web-applications-and-apis-with-polaris-fast-dynamic/test-internal-dast-projects-with-polaris-secure-tunnel.md) and Create a secure tunnel to a specific internal DAST project for more information.
- Polaris supports Black Duck Bridge CLI 3.1.0.
  - Now, you can use the Bridge CLI to run Polaris Secure Tunnel. Polaris Secure Tunnel establishes a secure connection between Polaris and your private network, allowing you to run DAST tests on applications and APIs on your internal network.
- Polaris supports Black Duck Detect 9.10.1.
- Polaris supports Black Duck Bridge CLI 3.0.0 (which replaces Synopsys Bridge). Now, the Bridge is served in two formats:
  - Bundle: The existing Bridge package, renamed. The bundle includes a root directory that contains all of the essential files.
  - Thin Client: The Thin Client downloads the necessary features at runtime, as it executes a workflow.

  Note: See [Polaris: Migrating to the new Bridge CLI](https://community.blackduck.com/s/article/integrations-black-duck-migration-instructions#Polaris) in Black Duck Community for more information.
- Now, you can save report settings as report configurations. Once saved, you can quickly generate the same report without having to configure the report's settings each time.

  See [Create and manage report configurations](../how-to/create-a-report/create-and-manage-report-configurations.md) for more information.
- The [Bug Tracking Integration](https://polaris.blackduck.com/developer/default/documentation/bug-tracking-integration) API was restructured to improve usability. This includes:
  - Changing each endpoint's base path from `/api/issue-export-service/jira` to `/api/integrations/bugtracking`.
  - Deprecating endpoints that reference the old base path. Deprecated endpoints have `deprecation` and `sunset` headers. They will not be available after "Mon, 15 Sep 2025 23:59:59 GMT" (sunset date).
  - Updating terminology used in endpoint paths to improve clarity and consistency.
- The domains used for reports and dashboards changed:
  - https://synopsys.sisense.com is now https://polaris.sisense.com
  - https://synopsys-se.sisense.com is now https://poc-polaris.sisense.com
  - https://synopsys-ie.sisense.com is now https://eu-polaris.sisense.com

  See [Polaris IP ranges](polaris-ip-ranges.md) for more information.
- The latest Code Sight releases added support for additional IDEs. With Code Sight 2024.11.0, you can:
  - View Polaris issues in your IDE with Android Studio and additional JetBrains IDEs (in addition to IntelliJ, Visual Studio, and VS Code).
  - Run tests on Polaris from you IDE with Android Studio, IntelliJ, and other JetBrains IDEs (in addition to VS Code).
- Many of the endpoints in the [Findings](https://polaris.blackduck.com/developer/default/documentation/findings) API were updated. This includes:
  - Adding the new base path (`/api/findings`) to remaining endpoints in the API (previously, only used in taxon query endpoints). The `/api/specialization-layer-service` base path will continue to function until September 30, 2025 (sunset date).
  - Component and license endpoints in the API were restructured to improve usability. This includes:
    - Replacing the `/api/specialization-layer-service/component-versions` endpoint with `/api/findings/component-versions/_actions/triage` to better-indicate the endpoint's purpose.
    - Updating terminology used in endpoint paths and properties to improve clarity and consistency.
  - Deprecating endpoints that were replaced. Deprecated endpoints have `deprecation` and `sunset` headers. They will not be available after "Mon, 30 Sep 2025 23:59:59 GMT" (sunset date).
- The [Reports](https://polaris.blackduck.com/developer/default/documentation/reports) API was restructured to improve usability. This includes:
  - Now you can create all reports with one endpoint: `/reports/{reportType}/_actions/run` (which replaces the /`reports/{reportType}/generate` and `/reports/{reportType}/export` endpoints).
  - Replacing the `/reports/{reportId}/download` endpoint with `/reports/{reportId}/_actions/download` for consistency.
  - Deprecating endpoints that were replaced. Deprecated endpoints have `deprecation` and `sunset` headers. They will not be available after "Mon, 1 Sep 2025 23:59:59 GMT" (sunset date).
- With a subscription that permits external analysis tests, you can import SAST and SCA issue data from many third-party tools into SAST & SCA projects in Polaris. This is a limited availability release and not generally available. Please contact your account teams for more information.

  Note: See [Import results from third-party tools (limited availability)](../how-to/import-results-from-third-party-tools-limited-availability.md) and Supported third-party tools for more information.

## November 2024

- The Insights API was renamed and is now [Reports](https://polaris.blackduck.com/developer/default/documentation/reports).
- Polaris now supports Coverity 2024.9.1. It includes the following changes:
  - Added support for Kotlin 2.0.
  - Added support for Python 3.12.
  - Added support for Android NDK r27 (Android NDK Clang up to 18.0.1).
  - Added new API safety and hardcoded secret checks for Kotlin and Python.

    Note: These new checkers could result in new issues found compared to previous scans.
  - The new `report_bitand` option of the `OVERRUN` checker reports a defect if the index expression used in an array access is the result of a bitwise AND operation and the value of the mask used in the bitwise AND operation indicates the index may be out of bounds.
  - Added new or updated checker support for C/C++:
    - `OVERRUN` checker now reports cases when a receiving buffer of a `scanf-`type function could be overrun.
    - `OVERRUN` checker now reports fewer false positives related to `strlen` function calls.
    - Added support for `std::rend` in the `INVALIDATE_ITERATOR` checker.
    - Updated the `OVERRUN` checker to report when a call to `scanf` contains a width specifier that might cause an overrun of the destination buffer.
    - Token patterns via CodeXM allowing ability to match preprocessor directives.
    - `USE_AFTER_MOVE` checker improvements to report cases where a function returns after moving a reference parameter.
  - Added new or updated checker support for C# :
    - Added support for the `SESSION_FIXATION` checker.
    - Added ability to detect 'password' keywords for C# through the Sigma engine. The recognition of the keyword happens with or without its usage.
  - Added new or updated checker support for Go :
    - Support for the `SESSION_FIXATION` checker.
  - Added new or updated checker support for Visual Basic:
    - Added support for the `SESSION_FIXATION` checker.
  - Support for Kotlin 1.9.x is deprecated and will be removed in a future release.
  - Support for Kotlin 1.8 has been removed.
  - Support for Open/Oracle JDK 22 is deprecated and will be removed in a future release.
  - Support for .NET 6 is deprecated and will be removed in a future release.
  - Fixes issues found in Coverity 2024.9.0.
- **Correction:** <https://sig-repo.synopsys.com> will continue to function until February 14, 2025.

  Note: See [Transition to repo.blackduck.com in Black Duck Community](https://community.blackduck.com/s/question/0D5Uh00000GrJzXKAV/announcement-transition-to-repoblackduckcom) for more information.
- **Correction:** The Attempt Build Break action only affects tests run using Bridge.

  Note: See [Issue policies](../how-to/create-and-manage-policies/issue-policies.md) for more information.
- As an Organization Administrator, you can migrate your tenant on the Black Duck Polaris® Platform to the Black Duck domain. When the migration is complete, users in your organization can access Polaris via <https://polaris.blackduck.com>, <https://poc.polaris.blackduck.com>, or <https://eu.polaris.blackduck.com> — and old URLs will redirect users automatically. We strongly recommend you complete this migration by February 14, 2025.

  Note: Find migration instructions here: Migrate Polaris to the Black Duck domain.
- Additional API references were renamed (without changes to functionality):
  - The SCM Integrations Service is now [Repos Integration](https://polaris.blackduck.com/developer/default/documentation/repos-integration).
  - The Test Manager API is now [Tests](https://polaris.blackduck.com/developer/default/documentation/tests).
  - The Tool Service is now [Tools](https://polaris.blackduck.com/developer/default/documentation/tools).
- Media type names used in Polaris APIs were renamed and no longer include "synopsys." Although media types that include "synopsys" were removed from the API specifications, existing endpoints will continue to support them until September 1, 2025. Please update your scripts to use the new media types.

## October 2024

- Additional API references were renamed (without changes to functionality):
  - The Audit API is now [Audit](https://polaris.blackduck.com/developer/default/documentation/audit).
  - The Report Service is now [Insights](https://polaris.blackduck.com/developer/default/documentation/reports).
  - The Notification API is now [Notification](https://polaris.blackduck.com/developer/default/documentation/notification).
  - The Customer Identity and Access Management (CIAM) API is now [Identity and Access Management](https://polaris.blackduck.com/developer/default/documentation/identity-and-access-management).
- The Executive Overview Dashboard is available. The new dashboard provides an overview of application security and policy compliance in your organization.
- Several API references were renamed (without changes to functionality):
  - The Issue Export Service is now [Bug Tracking Integration](https://polaris.blackduck.com/developer/default/documentation/bug-tracking-integration).
  - Polaris Issue Workflow Engine API is now [Findings](https://polaris.blackduck.com/developer/default/documentation/findings).
  - Policy Management API is now [Policies](https://polaris.blackduck.com/developer/default/documentation/policies).
  - Portfolio Service is now [Portfolio](https://polaris.blackduck.com/developer/default/documentation/portfolio).
- The [Polaris Issue Workflow Engine Service API](https://polaris.blackduck.com/developer/default/documentation/findings) was restructured to improve usability. This includes:
  - Adding the new base path. `/api/specialization-layer-service` is changing to `/api/findings` (currently, only used in taxon query endpoints). The `/api/specialization-layer-service` base path will continue to function until September 30, 2025 (sunset date).
  - Adding new taxon query endpoints. These return better-structured responses.
  - Deprecating old taxon query endpoints. Deprecated endpoints have `deprecation` and `sunset` headers. They will not be available after September 30, 2025 (sunset date).
  - Updating terminology used in endpoint paths and properties to improve clarity and consistency.
- **Correction:** Two Sisense domains included in the release notes at the start of October were corrected:
  - https://poc-polaris.sisense.com (previously published as https://poc.polaris.sisense.com)
  - https://eu-polaris.sisense.com (previously published as https://eu.polaris.sisense.com)
- The Policy Overview Dashboard is available. View the quantity of issues in your portfolio that violate your organization's policies.

  Tip: Apply the Policy Name filter to limit results to applications with projects specific policies are assigned to.
- The Portfolio ROI Dashboard is available. View the impact of Polaris on your portfolio's security profile over time.
- The Synopsys Software Integrity Group (SIG) is now [Black Duck](https://www.blackduck.com/). Soon, the name of the platform will become Black Duck Polaris® Platform.
  - To ensure Polaris continues to function as expected, update your allow list.
    - <https://sig-repo.synopsys.com> is now <https://repo.blackduck.com/>.
    - https://community.synopsys.com/s/ is now <https://community.blackduck.com/>.
    - See [Polaris IP ranges](polaris-ip-ranges.md) for more information.
  - Learning and support resources have moved:
    - Black Duck Community: <https://community.blackduck.com/>.
    - Black Duck Academy: <http://blackduck.skilljar.com/>.
    - Black Duck on YouTube: <https://www.youtube.com/@BlackDuckSoftware>.
    - Find documentation for other Black Duck products (including [Bridge documentation](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/eeb29c3010d96721ec9540ed4378aa41.topic)) here: <https://docs.blackduck.com/>.
  - Soon, Polaris will send emails via noreply@blackduck.com. Please update your spam filters to avoid interruptions.
  - Additional domain changes are coming soon (https://polaris.blackduck.com, https://poc.polaris.blackduck.com/, https://eu.polaris.blackduck.com/, https://store.polaris.blackduck.com/, https://store-eu.polaris.blackduck.com, https://store-poc.polaris.blackduck.com, https://tool-download.polaris.blackduck.com, https://polaris.sisense.com, https://poc-polaris.sisense.com, https://eu-polaris.sisense.com).
  - See [Black Duck Domain Change FAQ](https://community.blackduck.com/s/article/Black-Duck-Domain-Change-FAQ) for more information.
- Events in the audit log that capture actions performed by internal (Black Duck) users are now associated with the Internal System User (in the User column).

  Note: Events that are visible on the Audit Logs page before this update won't change.

## September 2024

- The quality of upgrade guidance for vulnerable components (detected in SCA tests) was improved.
  - Now (in addition to upgrade guidance for an individual component) upgrade guidance for components that bring in transitive dependencies appears in the user interface, when available.
  - See [Find component upgrade guidance](../how-to/find-component-upgrade-guidance.md) for more information.
- You can run tests on Polaris from your IDE with Code Sight 2024.9.0.
  - When you run a test from your IDE (using Code Sight), Code Sight creates a branch in Polaris. The names of branches created by Code Sight include `CodeSight_` and the email address of the user the branch was created for (for example, `CodeSight_user@domain.com`).

    Important: The branches Code Sight creates are not compatible with SCM integrations.
  - By default, tests run with Code Sight are hidden on the Tests page. Select IDE with the Test Mode filter to show tests run with Code Sight.
  - See [Connect Code Sight to Polaris](../how-to/connect-code-sight-to-polaris.md) for more information.
- To avoid exporting stale or resolved issues to Jira, exporting an issue to Jira was disabled on the Detected Issues and Absent Issues tabs (Tests > See Results > Detected Issues/Absent Issues). Use the Issues tab (Portfolio > select an application > select a project) to export issues to Jira.
- Polaris supports Synopsys® Bridge 2.9.0.
  - To minimize cloud agent runtimes, set `polaris.waitForScan` to `false` in your pipelines. When set, Bridge exits as soon as a test is queued, and does not perform post-analysis operations (break the build, fix PR, PR comments, SARIF, … etc.).
- Date pickers on the Onboarding and Test Summary dashboards were improved.

  Note: This update resets the default date filters. If necessary, use the new date pickers to change the default values for your organization.
- The License and Component dashboards were renamed to Table - Component Search and Table - License Search, respectively.
- The Application Tag filter was added to the Issues Summary Dashboard, Table - Component Search, Table - License Search, and Test Summary dashboards.
- The Vulnerability ID filter was added to the Issues Summary Dashboard.
- The Tool Name filter (found in Dashboards) now includes separate options for different SCA test types: Polaris Package Manager and Polaris Signature Analysis.

## August 2024

- Now, you can run signature analysis tests using Synopsys Bridge on ARM-based Mac.
- Polaris supports Synopsys Bridge 2.8.0.
- Polaris supports Synopsys Detect 9.9.0.
  - If you override properties of parent modules in your Maven project's pom.xml, Polaris uses the overrides to generate more precise results in code upload and SCM workflows.
- Now, you can include DAST test results in eligible reports (excluding the Developer Detail Static, Developer Detail SCA, and SBOM reports).
- Polaris fAST Dynamic now supports dynamic application security testing (DAST) of native APIs. To run a self-service DAST test against an API, you provide the base URL, API specification file, and any authorization headers. You can view issues found alongside HTTP evidence—including endpoints, request and response bodies, and attack payloads—and triage them by severity. REST and GraphQL APIs are both supported.

  Note: To get started, create a new DAST project and specify an API target. See [Test web applications and APIs with Polaris fAST Dynamic](../how-to/test-web-applications-and-apis-with-polaris-fast-dynamic.md) for more information.
- Now, DAST test and issue data is included in Dashboards.

  Note: To include DAST tests in the Test Summary dashboard, the Display Default Branch filter must include true. If only false is selected, DAST test results are hidden.
- Polaris supports Synopsys Bridge 2.7.0.
  - Now, if the application specified when triggering a test (`polaris.application.name`) doesn't already exist in Polaris, Bridge attempts to create the application before running the test.

    Note: A valid concurrent (team member) subscription is required to create applications in Polaris using Synopsys Bridge.
  - If you run a SAST and SCA test in the same job, Bridge ensures the SAST test runs first.
- Now, you can create component policies that notify Organization Administrators when components with specific properties are detected in SCA tests. Policy violation quantities that appear throughout the user interface now include violations from issue and component policies.

  Note: See [Component policies](../how-to/create-and-manage-policies/component-policies.md) for more information.

## July 2024

- As an extension to Polaris SCM onboarding, Polaris will now support single project onboarding of self-hosted versions of GitHub.
- The Onboarding Dashboard is available. View the quantity of applications and projects created in a time period, and how many of the applications and projects were tested. Includes trend charts for applications and projects created, and a table with the total number of tests run per project. Apply the Application Tag filter to limit data to applications with particular tags.

  Note: Any application with a SAST and/or SCA subscription is counted on the Onboarding Dashboard, but DAST projects and tests are ignored. SAST and SCA tests are used to evaluate the percentage of applications and projects scanned.
- For added security, a relay service was implemented that proxies requests from Polaris to LaunchDarkly.

  Note: You don't need to allow list the IP ranges for LaunchDarkly (104.156.80.0/20, 151.101.0.0/16, and 52.21.152.96/32) anymore.
- Polaris now supports Coverity 2024.6.0. It includes the following changes:
  - Support for Go 1.20 has been removed.
  - Support for Java 11 has been removed.
  - Support for LLVM Clang 8.x has been removed.
  - Support for .NET 7.0 has been removed.
  - Support for Open/Oracle JDK 11 has been removed.
  - Support for macOS 12 is deprecated and will be removed in a future release.
  - Support for Go 1.21 deprecated and will be removed in a future release.
  - Support for LLVM Clang 9.0 is deprecated and will be removed in a future release.
  - Added support for Go 1.22.
  - Added support for Java 22.
  - Added support for LLVM Clang 18.1.0 and Xcode 15.3.
  - Added support for Open / Oracle JDK 22.
  - Support for PHP has been improved.

    Note: Improved support could lead to an increase in the number of new PHP defects .
  - Improvements to SQL injection checkers in Python Code.
  - New or updated checkers for C#, Java, JavaScript/TypeScript, and Visual Basic.
  - New secret patterns and checks for JavaScript and Java.
  - Support for Bazel requires current users to make a one-time adjustment to their scans. For more information, see [Changes to Bazel integration method](https://docs.blackduck.com/access?ft:originId=f720d35c853c162f322ebf99909fe7c9/01b1546cf9e9f7a6b4666cde6db8b1f4.topic&Version=latest).
- Now, you can add rules to issue policies that automate actions when issues with different fix-by statuses (Overdue, Due Soon, On Track, or Not Set) are detected in a test.

  Note: We recommend you don't use Fix-By Status in conjunction with other properties. Instead, create a separate rule (or a separate issue policy) to automate actions with fix-by statuses. See [Issue policies](../how-to/create-and-manage-policies/issue-policies.md) for more information.
- While viewing issues in a project, you can filter issues based on their the Fix-By Status.
- Issue exports (to CSV or JSON) include fix-by dates.
- As an extension to Polaris SCM onboarding, Polaris will now support single project onboarding of self-hosted versions of GitLab.
- Using Synopsys Bridge, you can run Black Duck® signature scans (a type of SCA test) and upload results to Polaris. These tests build a project during analysis and can identify components in your project that aren't referenced in your package manager's manifest file. Files and folders in each component captured in a signature analysis test are compared with a copy of the component in the Black Duck knowledge base to generate additional match types (beyond direct and transitive dependencies), and a (percentage) match score. A higher match score indicate a closer match, and a lower match score indicates a component was modified.

  Please note that duplicate SCA issues appear when a component is detected in both package manager and signature analysis tests. While viewing issues in a branch or test, use the Tool Type filter to show SCA issues captured in Package Manager or Signature Analysis tests.

  Note: To run a signature analysis test, include the `SCA-SIGNATURE` SCA test type in your input.json file. See [Running Polaris scans with a JSON file](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0c68b6621951399783959d99c58930be.topic) in the Synopsys Bridge documentation for more information.
- Organization Administrators can update the subscriptions assigned to multiple applications at the same time.

  Note: See Update the subscriptions assigned to multiple applications for more information.
- Polaris supports Synopsys Bridge 2.6.8. Now, short test IDs appear in logs.

## June 2024

- As an extension to Polaris SCM onboarding, Polaris will now support single project onboarding of self-hosted versions of Bitbucket.
- The Audit, CIAM, and Notification APIs were restructured to improve usability. This includes:
  - Changing each API's base path:
    - Audit: From `api/audit-service` to `api/audit`.
    - CIAM: From `api/ciam` to `api/auth`.
    - Notification: From `api/notification-service` to `api/notification`.
  - Deprecating endpoints that reference the old base paths. Deprecated endpoints have `deprecation` and `sunset` headers. They will not be available after "Mon, 31 Mar 2025 23:59:59 GMT" (sunset date).
  - Updating terminology used in endpoint paths to improve clarity and consistency.

  Note: See [Audit API](https://polaris.blackduck.com/developer/default/documentation/audit), [CIAM Service API](https://polaris.blackduck.com/developer/default/documentation/identity-and-access-management), and [Notification API](https://polaris.blackduck.com/developer/default/documentation/notification) for more information.
- You can now triage components. This allows you to exclude specific components from your Software Bill of Materials (SBOM) and removes vulnerabilities related to that component in the issue view. This includes:
  - When you exclude a component, any non-dismissed issues derived from the component are automatically dismissed.
  - When you exclude a components, it reduces the violation counts (if policy is configured to filter only "non-dismissed" issues).
  - Excluded components will not be in SBOM reports.
  - If needed, you can switch a component from excluded back to the default (included).
- Polaris supports Synopsys Bridge 2.6.0. Now, in addition to passing arguments for Coverity and Detect in a configuration file, you can include tool-specific arguments in commands and environment variables.

  Note: See [Passing Arguments using the CLI](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/73a0987ffd7b7f8a51a76a386aabf67a.topic) in the Synopsys Bridge documentation for more information.
- The [Notification API](https://polaris.blackduck.com/developer/default/documentation/notification) reference is available. Use this API to manage your organization's notification settings (including notification settings for users).
- The `PATCH /api/ciam/resources/applications/{applicationId}/roles/{roleId}/users` endpoint was added to the [CIAM Service API](https://polaris.blackduck.com/developer/default/documentation/identity-and-access-management). Use this endpoint to assign application-level roles to users.

  Note: The new `PATCH` endpoint replicates the `POST /api/ciam/resources/applications/{applicationId}/roles/{roleId}/users` endpoint — but returns more informative responses.
- API reference documentation for the [CIAM](https://polaris.blackduck.com/developer/default/documentation/identity-and-access-management) and [Audit](https://polaris.blackduck.com/developer/default/documentation/audit) services was improved. This includes:
  - Adding missing 405 and 500 error responses.
  - Adding missing example values.
  - Adding media types to error responses.
- The Policy Management (formerly, Risk Manager) API was restructured to improve usability. This includes:
  - Changing the service's base path from `api/risk` to `api/policies`.
  - Adding V2 policy assignment endpoints. The V2 endpoints don't use path parameters, and make assigning policies to projects and branches easier.
  - Adding new policy evaluation endpoints that retrieve the count of issues that violate policies and their rules.
  - Deprecating endpoints that reference the old base path, and V1 policy assignment endpoints. Deprecated endpoints have `deprecation` and `sunset` headers. They will not be available after "Sun, 1 Dec 2024 23:59:59 GMT" (sunset date).

  Note: See the [Policy Management API](https://polaris.blackduck.com/developer/default/documentation/policies) reference for more information.
- Organization Administrators and Organization Application Managers can add subscriptions to preexisting applications, and replace application subscriptions with concurrent subscriptions.

  Note: See [Assign subscriptions to applications](../how-to/assign-subscriptions-to-applications.md) for more information.
- Polaris supports Synopsys Bridge 2.5.0. Now, you can use Bridge to upload source code to Polaris, and then scan it with Polaris (mimicking the process a user would follow in the Polaris UI).

  Note: See [Source Code Upload Scan](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0c68b6621951399783959d99c58930be.topic) in the Bridge documentation for more information.

## May 2024

- Polaris supports Synopsys Detect version 9.6.0.
  - This includes support for Gradle's rich model for declaring versions, which allows you to define dependency conflict resolution rules for direct and transitive dependencies. Support for Gradle's rich model for declaring versions is only available when you test with Synopsys Bridge (CI/CLI).

    Note: See [Rich version declaration support](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/2a20929644f28e3401bed8f6d0f21f09.topic&Version=latest) in the Detect documentation for more information.
- Now, you can create an Executive Summary Report that provides an overview of your portfolio and modules that detail the overall risk posture including issue summaries, detected and absent issue charts, issue trend charts, top issue types and top issues with policy violations.
- Find the IPs you may need to allow list to work with Polaris here: Polaris IP ranges, Polaris IP ranges for Bridge CLI.
- Polaris supports Synopsys Bridge 2.4.45. Now, Bridge output includes links to Polaris where you can view:
  - Each completed test's results.
  - The branch that was tested.
- Polaris supports Coverity version 2024.3.1 which fixes a bug introduced in Coverity 2024.3.0 with cov-emit. This bug consumed excess time and memory which impacted Polaris scans completing.
- Now, you can create a Developer Detail Static Report that provides an overview of the issues in the selected application(s) including details that will help developers select what to focus on.
- Now, you can create a Standard Compliance Detail Report that provides an overview of the issues in the selected standard. It also provides an issue count for each project, and issue details organized by test type and standard.
- Now, you can use Polaris Assist to generate SAST remediation guidance with a large language model (LLM). Remediation guidance includes:
  - A short summary of the issue
  - An analysis of the code where the issue is found
  - A revision (in code) that may remediate the issue

  Note: See [Generate SAST remediation guidance with Black Duck Assist](../how-to/generate-sast-remediation-guidance-with-black-duck-assist.md) for more information.

## April 2024

**New Features and Changes**

- Now, you can create a Developer Detail SCA Report that provides an overview of the issues in the selected application(s) including details that will help developers select what to focus on.
- Polaris supports Synopsys Bridge 2.4.12.
- Now, you can create an Issue Overview Report that provides a high level overview of your applications and projects to show your risk posture across the entire portfolio.
- Now, you can create a Test Summary Report that allows you to see tests of your applications and/or projects (depending on selected scope). The report lists the first and last test, number of tests in a time period, test trends, assessment types scanned, and a list of applications and/or projects not tested in the time period.
- Polaris supports Synopsys Detect version 9.5.0.
  - Use the `--detect.maven.include.shaded.dependencies` property to include a Maven project's embedded or shaded dependencies in its bill of materials (BOM).

    Note: See [Include Shaded Dependencies](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/9132fa4c63d9c533dd05778fd7f994a9.topic&Version=latest) in the Detect documentation for more information.
  - The Maven Project Inspector excludes Maven dependencies with `<exclude>` tags in the pom.xml file.
  - Improves the accuracy of SCA tests run on Maven and Gradle projects in Code Upload and SCM workflows.
  - The Maven Project Inspector and Gradle Project Inspector detectors eliminate optional dependencies to reduce false positives.
- Polaris now supports Coverity 2024.3.0. It includes the following changes:
  - Support for Windows Server 2019 has been removed.
  - Support for .NET 6.0 has been removed.
  - Support for Oracle/Open JDK 20 has been removed.
  - Support for Oracle JDK 11 is deprecated and support for it will be removed in a future release.
  - Added support for C# 12.
  - Added support for .NET 8.
- Two new dashboards are available:
  - Component Dashboard: View all the components used in your organization's applications and projects, along with the license each component is subject to.
  - License Dashboard: View all the licenses your organization's applications and projects are subject to, along with a description of each license, and each license's family.

  Note: See [Work with dashboards](../how-to/work-with-dashboards.md) for more information.
- Polaris supports fAST Dynamic. Optimized for advanced JavaScript frameworks and single page applications (SPA), fAST Dynamic enables you to run rapid, self-service security scans of pre-production web applications from within the Polaris platform.

  Dynamic application security testing (DAST) is a method of AppSec testing that examines an application while it's running, without knowledge of the application's internal interactions or designs at the system level, and without access or visibility into the source program. This "black box" testing looks at an application from the outside in, examines its running state, and observes its responses to simulated attacks made by a testing tool. An application's responses to these simulations help determine whether the application is vulnerable and could be susceptible to a real malicious attack.

  Note: See [Test web applications and APIs with Polaris fAST Dynamic](../how-to/test-web-applications-and-apis-with-polaris-fast-dynamic.md) for more information.
- A new application-level role is available in Polaris: Member. Members can do everything Contributors can do, except create, edit, and delete projects.

  Note: See [Roles and permissions](roles-and-permissions.md) for more information.
- Polaris supports Synopsys Detect version 9.4.0, which:
  - Extends Conan support to Conan 2.0.14.
  - Extends NuGet support to NuGet 6.2, and allows Polaris to capture dependencies in projects that use NuGet's Central Package Management.
  - Extends Dart support to Dart 3.1.2 and Flutter 3.13.4.
  - Extends BitBake support to BitBake 2.6.0 (Yocto 4.3.2).
  - Extends pnpm support to pnpm 8.9.2 (using the v6 pnpm-lock.yaml file).

    Important: pnpm 6, and pnpm 7 (using the default v5 pnpm-lock.yaml file) are being deprecated. Support will be removed in future Synopsys Detect release.
  - Extends Yarn support to Yarn 4.1.0.
  - When testing Maven projects with the Maven CLI, arguments that control the number of threads used (included with `detect.maven.build.command` property) are ignored.
  - Includes several bug fixes and improvements.
  - Includes a new detector for Python projects, PIP Requirements File Parse.

    Note: PIP Requirements File Parse is a buildless detector that acts as a LOW accuracy fallback for the PIP Native Inspector. This detector is triggered for Python projects that contain one or more requirements.txt files if Synopsys Detect does not have access to a PIP executable in the environment where the scan is run.

## March 2024

**New Features and Changes**

- Polaris supports Synopsys Bridge 2.4.0.
- Now, you can create a Security Audit report that identifies vulnerable areas in your application including identifying different components that may be exploited, estimating protection from common attacks, and assessing the overall security risk across all threat areas.
- Now, you can use groups to manage access to applications. You can create groups manually in Polaris, or (after you set up single sign-on) you can synchronize groups in your identity provider (like Azure, or Okta) with Polaris.

  Note: See [Manage access with groups](../how-to/manage-access-with-groups.md) and Manage Polaris groups through your identity provider for more information.
- The General tab was added to the My Organization page (and replaces the Data Access and Notifications tabs, which were removed). Here, you can:
  - Find your organization (tenant) name and ID.
  - Enable/disable assessment center access to published issues (enabled by default).
  - Enable or disable email notifications for all users (enabled by default).
- Now, you can create Standard Compliance reports that provide issue counts for each application as it relates to a selected standard, as well as a view of the total issues found per standard.
- Exporting a software bill of materials report to Cyclone DX v. 1.4 is now available.
- Now, you can apply fix-by dates to issues in your portfolio to help your developers prioritize issues for remediation, and enforce your organization's security standards across projects and applications. Fix by dates can be set:
  - Automatically with issue policies, where you can specify severity-specific fix-by dates.

    Note: See Fix-by dates for more information.
  - Manually when you triage issues.

    Note: See [Ways to triage issues in Polaris](../how-to/ways-to-triage-issues-in-polaris.md) for more information.
- Polaris supports Synopsys Bridge 2.3.0. Now, using the Bridge CLI you can:
  - Export issues to a SARIF file.

    Note: See [Exporting a SARIF File](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0c68b6621951399783959d99c58930be.topic) in the Bridge CLI documentation for more information.
  - Use the `--out <outFile>` command to save final state data to a file.
- Reports can now be downloaded from the UI. New features include being able to:
  - View details, search and download reports from the past 30 days.
  - Filter by type of report, date(s) or status.
- Improvements were made to the Test Summary dashboard, along with minor bug fixes. Improvements include revised test state labels and enhanced widget filtering.

## February 2024

**New Features and Changes**

- Now, you can integrate Polaris with Secure Code Warrior. Once the Secure Code Warrior integration is enabled, links to free, interactive training resources appear in the Issue Details pane, when available. Links are context-sensitive, and direct you to training tailored to a specific issue.

  Note: See [Integrate Secure Code Warrior with Polaris](../how-to/integrate-secure-code-warrior-with-polaris.md) for more information.

  Synopsys is a Secure Code Warrior connect partner. Contact your Synopsys sales rep to take full advantage of the Secure Code Warrior platform, which includes additional activities, courses, tournaments, APIs, integrations, and reporting.
- Polaris now supports Coverity 2023.12.1. This fixes known scan error issues with JavaScript and Clang in Coverity 2023.12.0.
- Now, you can configure Polaris to automatically delete non-default branches that aren't tested for a period between 1 and 90 days. You can adjust this in each application, project, and branch's settings. By default, Polaris retains non-default branches indefinitely.

  Note: See Configure automatic branch deletion for more information.
- Each issue's First Detected date (the date and time when an issue was first captured in a test) appears in issue grids and issue details.
- You can view an issue's detection history in the triage panel.

  Note: See [View issue history](../how-to/view-issue-history.md) for more information.
- The new Summary tab is available when you open a project. Here, you'll find the Issues Over Time and Average Age of Outstanding Issues charts. Use these charts to monitor the quantity of issues in a project over time, and see the average age of issues in the project, grouped by severity.

  Note: See Summary tab for more information.

## January 2024

**New Features and Changes**

- Code Sight users can view Polaris issues in Visual Studio.
- Links in emails used to reset passwords, reset two-factor authentication, and join Polaris expire after 24 hours. Until now, these links expired after 12 hours.
- Polaris supports Synopsys Bridge 2.2.1.

  **Correction:** Polaris supports Synopsys Bridge 2.2.1.
- Now, you can download a version of Synopsys Bridge that runs on Apple® silicon (ARM-based Mac) from the Polaris user interface.
  - To download an ARM-compatible version of Synopsys Bridge, go to Account > Downloads.
- Polaris supports Coverity 2023.12.0. It includes the following changes:
  - Support for macOS 11 has been removed.
  - Support for Go 1.19 has been removed.
  - Support for Windows Server 2019 is deprecated will be removed in a future release. Support for Go 1.20 deprecated as of 2023.12 and will be removed in a future release.
  - Added support for Dart/Flutter.
  - Added support for macOS 14.
  - Added support for C++23.
  - Added support for Go 1.21.
  - Added support for Java 21. Preview features are not supported at this time. To avoid issues, ensure error recovery is enabled when using preview features.
  - Added support for Ruby 3.x (via Breakman pro bundled into analysis kit).
  - Added support for ECMAScript 2023.
  - Added support for TypeScript 5.0, 5.1, and 5.2.
  - Updated SQLI checkers optimize the number of false positives/negatives which could result in changes in the number of issues found in Polaris.

  Important: Customers who test projects with JavaScript may experience errors after the Coverity 2023.12.0 upgrade. This is a known issue and a fix is scheduled in the upcoming weeks.
- The Test Summary Dashboard was added to the Dashboards page. Use this dashboard to visualize the quantity of tests run against applications and projects in your organization. Switch between different dashboards using the new Dashboards pane.
- Customers with concurrent subscriptions can now integrate multiple repositories from GitHub and GitHub Enterprise as applications or projects in Polaris. This includes:
  - Using your SCM repository to create new application(s) and project(s) or add multiple repositories to existing applications in Polaris. During this process the user can assign policies and, for applications, roles.
  - Ability to update the connection credentials for all the projects under an application.

## December 2023

**New Features and Changes**

- Polaris supports Synopsys Bridge 2.1.0.
- The retention period for events captured in audit logs was extended from 7 to 30 days.

  Note: Events that are visible on the Audit Logs page when the retention period changes are preserved for 30 days.
- Polaris supports additional package managers for SCA tests run via code upload or SCM integrations, including:
  - Cargo
  - Carthage
  - CocoaPods
  - Conan
  - CRAN
  - Dart
  - Go Dep
  - Go Vendor
  - Gogradle
  - Packagist
  - RubyGems
  - Swift
  - Xcode

## November 2023

**New Features and Changes**

- The Notes field was removed from the New Test page.
- Polaris supports Synopsys Bridge 2.0.0.

  Important: When used with Polaris, this version requires the `polaris.branch.name` variable. Please update your pipelines to avoid errors.
- Polaris supports Coverity 2023.9.2. It includes the following changes:
  - Support for Visual Basic is limited to CLI mode.
  - Support for PHP quality checkers has been removed.
  - Support for Kotlin 1.7.0-1.7.20 has been removed.
  - Support for Open/Oracle JDK 19 compilers has been removed.
  - Support for Kotlin 1.8.x is deprecated and will be removed in a future release.
  - Added support for Kotlin 1.9.0.
  - Added support for Python 3.11.
  - Added support for Java 20.
  - Added support for PHP 8.0. PHP 8 support is now available through Rapid Scan Static (Sigma), bundled with Coverity.
  - Support for Ruby in Coverity quality checkers is being deprecated as of Coverity 2023.9.0 and will be removed in a future release.
- The Synopsys Security Scan Plugin for Jenkins is available in the Jenkins Marketplace. Use the Synopsys Security Scan Plugin (with Bitbucket) to run Polaris scans in your Jenkins pipeline.
- Three new filters were added to the Dashboards page. Now, you can filter issue data by CWE (Common Weakness Enumeration, CWE™), Location, and/or Issue Category.
- Polaris supports Synopsys Bridge 1.2.38. In this version, when Bridge creates a new project (when you test a project that doesn't already exist in Polaris), it uses the branch name you provide (in the command or JSON file) to create the project's default branch.
- Now, Common Vulnerabilities and Exposures (CVE®) and Black Duck® Security Advisory (BDSA) codes appear in the issues table for SCA issues, in the Vulnerability ID column. When a CVE and BDSA code apply to a single issue, the BDSA code is hidden. Hover over (+1) to see the BDSA code.

  Note: CVE and BDSA codes are not added to your existing test results. Retest your projects to reveal these values.
- Now, you can update quantities in the Total Active Policy Violations columns (found on the Portfolio and Portfolio Application pages) by triaging issues. To do so, add triage statuses to your issue policies' rules. To exclude dismissed issues from Total Active Policy Violations columns (and mimic the behavior of other columns on these pages), make sure your policy's rules capture issues with the To Be Fixed and Not Triaged statuses.

  Note: The default issue policy for new Polaris tenants now excludes dismissed issues; however, this change is not applied to preexisting policies.
- The default branch name for new projects has been changed back to "main" and is no longer "polaris\_main".
- Branching with an integrated SCM repository has been made easier including:
  - Polaris automatically imports the default branch from the repository when you integrate.
  - If you have a branch with the same name in your repository and in your Polaris project, Polaris will link the Polaris branch to the SCM branch and you will not lose scan data from the original branch.
- The Refresh buttons near the top of the Portfolio and Application pages were removed.
- Polaris supports Synopsys Detect version 9.0.0, which:
  - Extends Gradle support to Gradle 8.2.
  - Extends npm support to npm 9.8.1.

    Note: Polaris no longer supports scanning Node.js projects that use npm 6.
  - Adds support for npm workspaces.
  - Adds support for NuGet package reference properties from Directory.Build.props and Project.csproj.nuget.g.props files.
- A revised SCA Language and Package Manager Support table is available here: Polaris Support Information. The new table includes:
  - Entry points
  - Detectors and their requirements
  - The relative accuracy of different detectors
  - Additional supported package managers (Cocoapods, CPAN, CRAN, Packagist, PEAR, RubyGems)
- Added the SCA Package Manager Versions (latest) table to the Polaris Support Information page.
- The known issue with dates in the Latest Completed Test column is fixed.

**Correction**

- Git and Bazel were removed from the SCA Language and Package Manager Support table. Neither of these tools is a package manager.

## October 2023

**New Features and Changes**

- Export of software bill of materials (SBOM) via JSON file (SPDX v. 2.3) is now available.
- Polaris supports Synopsys Bridge 1.2.12.
- Policy violations appear on the Portfolio, and Tests pages. See [Monitor policies in Polaris](../how-to/create-and-manage-policies/monitor-policies-in-polaris.md) for more information.
- Now, you can find the latest test of a default branch in any of an application's projects on the Portfolio page.

  Note: When you open the Portfolio page after this feature is released, the Latest Completed Test columns may be empty. Values appear after a project's default branch is scanned.
- An option to select one standard (OWASP®, CWE™ or PCI DSS) when you create a report has been added.
- The default branch name for new projects changed. Previously "main" was used. Now "polaris\_main" is used.
- Polaris supports Synopsys Bridge 1.2.0.
- The default filters on the Dashboards page changed. Now, dismissed issues are hidden by default.

**Known Issue (Fixed)**

- Dates in the Latest Completed Test column (on the Portfolio page) may not be accurate. Our team is actively working on a fix to resolve this issue.

## September 2023

**Other Features and Changes**

- The quantity of projects in each application appears on the Portfolio page (in the Projects column).
- The new Standards filter was added to the Dashboards page. When you apply the Standards filter, a new chart appears.
- We improved the usability of the Policy page, including renaming "test frequency policies" to "test scheduling policies."
- Polaris now supports Synopsys Bridge 1.1.0 and pull request commenting. See [Using Bridge CLI with Polaris](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/0c68b6621951399783959d99c58930be.topic) in the Synopsys Bridge CLI Guide.
- Application Observers can view triage history.
- Now, you can filter issues by triage status on the Dashboards page.
- Limitations for fields (application name, etc.) has been added to the documentation.

**Enhanced Branch Support**

Now, you can add branches to projects in Polaris. What you need to know:

- You can add up to 10 branches to each project by default (although this quantity varies from subscription to subscription). Each branch you add to a project can be connected to a branch in a repository (after you set up an SCM integration), but they don't have to be.
- If the same issue is detected in multiple branches of a project, you only need to triage it once. Triage actions are automatically applied across branches in a project.
- When a component with multiple licensing options is found in different branches of a project, you only need to set the component's license once. License selections are automatically applied across branches in a project.
- When branching features are enabled in Polaris, your projects are upgraded automatically.
  - Projects that aren't connected to an SCM repository:
    - Polaris creates the project's default branch (polaris\_main).
    - All preexisting test data is mapped to the polaris\_main branch.
    - The project's policies are applied to the polaris\_main branch.
  - Projects connected to an SCM repository:
    - Polaris retrieves the default branch name from the repository.

      Note: If the project's SCM access token is invalid, Polaris creates a default branch called `scm_token_invalid`. If this occurs, you need to create a new SCM access token, and reestablish the project's SCM integration. See [Enhanced branch support and invalid SCM access tokens](../how-to/connect-a-polaris-project-to-a-repository-in-your-scm/enhanced-branch-support-and-invalid-scm-access-tokens.md) for more information.
    - Polaris creates the project's default branch (using the name retrieved from the repository).
    - All preexisting test data is mapped to the default branch.
    - The project's policies are applied to the default branch.
- Each test runs on a branch. You can use filters to compare issues between a project's default and non-default branches.
- Default branches are used when you generate reports, or view dashboards.
- Branching actions are tracked in audit logs.

To get started with branching, familiarize yourself with the following:

- The data model: applications and projects in Polaris
- Create and manage branches in a project
- Assign policies to branches
- How to test from the web UI
- Compare default and non-default branches in a project

**Correction**

- Previous revisions of the SCA support matrix for Polaris included C/C++ (Clang) support. In fact, Polaris does not support C/C++ (Clang) for SCA scans, but support is being considered for a future release.

## August 2023

**New Features and Changes**

- Polaris now supports Coverity 2023.6.1 which contains a Coverity CLI fix to handle Analysis OOM errors.
- Polaris now includes enhanced logging for policy changes.
- Polaris now supports npm, pip, pnpm, Poetry and Yarn package managers for SCA scans run on manually uploaded files, or SCM repositories integrated with Polaris.
- If multiple licensing options are available for a component, you can select the appropriate licenses for your use case.

## July 2023

**New Features and Changes**

- Polaris now supports Coverity 2023.6.0. It includes the following changes:
  - Support for Go 1.18 has been removed.
  - Support for macOS 11 is deprecated and will be removed in a future release.
  - Support for Go 1.19 has been deprecated and will be removed in a future release.
  - Added support for Go 1.20.
  - Added partial support for Java 20. Methods using Java 20 features will be tolerated but not emitted.
  - Improved performance of JavaScript webapp security analysis.
- Now, you can connect Code Sight to Polaris to view issue data in your IDE (VS Code or IntelliJ).
- Polaris supports Synopsys Detect version 8.10.0.
- Issue quantities for each application (organized by severity) appear on the Portfolio page.
- Issue quantities for each project (organized by severity) appear on the Application page.

## June 2023

**New Features and Changes**

- BitBucket projects can now be integrated with Polaris.
- The Notifications event type was added to audit logs. The new event type captures the following events:
  - An Organization Admin enables or disables email notifications for all users (via My Organization > Notifications).
  - A user modifies their personal email notification settings (via Account > Notifications).
- Now, you can see a list of applications linked to a subscription on the Subscriptions page.
- Synopsys Bridge CLI tool has been updated to use `--input` instead of the deprecated `--state` argument.
- Language support table has been updated.

## May 2023

**New Features and Changes**

- Polaris now supports Coverity 2023.3.3 which includes:
  - Added support for C#11.
  - Added support for Java 19.
  - Added support for Kotlin 1.8.0.
  - Added support for TypeScript 4.9.
  - Support for Go 1.18 is deprecated and will be removed in a future release.
  - Support for Kotlin 1.7 is deprecated and will be removed in a future release.
  - Support for Go 1.17 has been removed.
  - Support for Kotlin 1.6.x has been removed.
- Documentation was updated with how to import third-party repos to Azure Repos so it can integrate with Polaris.
- A link to the System Status page has been added to the Need more help topic.
- Software Bill of Materials (BOM) details for SCA analysis have been added to help triage a project's open source component versions and licenses.
- A topic covering Synopsys GitLab Template has been added to Integrations.
- You can now set an issue policy action to create and bundle issues to a single Jira ticket.
- A new **Reporting** page allows the creation of customized downloadable reports of your test results.
- The previous reports page has been moved to the **Dashboards** page. It now contains high-level snapshots and issue details with filters to customize your view of test results.
- Synopsys Bridge now automatically creates a project if one is not present.
- A Synopsys Bridge security fix for CVE-2023-2453 has been implemented. Previously `cov-build` and `cov-configurewould` dump all environment variables to log files, which can present a security concern. This fix sets `COVERITY_NO_LOG_ENVIRONMENT_VARIABLES=1` as the default to close the vulnerability.
- A topic covering Synopsys GitHub Actions has been added to Integrations.

## April 2023

**New Features and Changes**

- Org Admin can delete users via **MyOrganization > Users.**
- Visual Basic is supported via Synopsys Bridge.
- Azure DevOps projects can now be integrated with Polaris.
- Polaris now support SAML SSO 2.0 integration with an identity provider such as Okta, Azure, etc. This allows users to log into Polaris with the same email and passwords with which they log into your organization.

## March 2023

**New Features and Changes**

- The Bridge CLI tool is now called Synopsys Bridge.
- New `--diagnostics` command line option allows access to additional Synopsys Bridge diagnostic information.

## February 2023

**New Features and Changes**

- Projects and applications can now be deleted by Org Admin or Application Managers.
- (Now allowed by default.) The assessment center can view published issues to answer questions and provide feedback. Organizational administrators can disable access via **My Organization > Data Access.**
- The Polaris UI shows metrics for completed tests, including the numbers of files captured and analyzed, and the duration of the test. For comparison, the previous successful test is also shown.
- Added GCC compiler configuration support for `coverity.yaml`. See [Configuring Coverity Thin Client for use with Synopsys Bridge and Polaris](https://docs.blackduck.com/access?ft:originId=cba15d77e1e0a5989f94dbbae8f7dd44/b111ebf4ee3429ab6eea7cab4f88cbd5.topic).
- **Known Issue:** Scan metrics are not available for tests initiated by the Bridge CLI on a Windows machine.

## December 2022

**New Features and Changes**

The following are new features and changes from the GA release.

- Users are now automatically logged out after 15 minutes of inactivity.

Several logging improvements have been made to the Synopsys Bridge CLI tool:

- Synopsys Bridge now outputs colored `ERROR` and `WARN` log messages in the terminal, making troubleshooting easier.
- Synopsys Bridge now offers a `—json-log` option for the user to output JSON format logs.
- Synopsys Bridge now offers a `—json-log-file` option, which formats the `synopsys-bridge.log` file as JSON.
- Synopsys Bridge now provides more logs in adapters, with five log levels:
  - `DEBUG`
  - `INFO`
  - `WARN`
  - `ERROR`
  - `FATAL`
- Synopsys Bridge now offers improved array passing using comma separated values (CSV). For example, you can pass `polaris.assessment.types=SAST,SCA` rather than `polaris.assessment.types="[\"SAST\"]"`.

## GA release

- **Known Issues**: If you have issues seeing the Dashboard or Reports pages, check the following.
  - Safari: “Prevent cross-site tracking” is not on.
  - Chrome: “Allow 3rd party cookies” is on.
