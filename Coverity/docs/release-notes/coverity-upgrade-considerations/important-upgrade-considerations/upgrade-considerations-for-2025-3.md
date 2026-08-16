---
title: "Upgrade considerations for 2025.3"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrade-considerations-for-2025.3.html"
content_id: "CTFZ8kMvFavrpZvRR~VCqg"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:48.916304+00:00"
---

# Upgrade considerations for 2025.3

For information about deprecated and dropped support, other updates, known issues, and
fixed bugs, see "Coverity 2025.3.0 Release Notes" (and the sections for associated hot
fixes) in the Coverity 2026.6.0 Release Notes Archive.

For the list of Sigma checkers disabled by default when running Coverity Analysis 2025.3,
see ["Checkers disabled in Sigma when running Coverity
Analysis"](https://documentation.blackduck.com/bundle/coverity-docs-2025.3/page/checker-ref/checkers/S/sigma._checkers.html#d100634e144) in the [*Coverity 2025.3.0 Checker
Reference*](https://documentation.blackduck.com/bundle/coverity-docs-2025.3/page/webhelp-files/checkerref_start.html).

CAUTION:

When you upgrade Coverity Analysis, all previous settings are
overwritten. All checkers listed in the [" Sigma checks disabled by default in Coverity
2025.3"](https://documentation.blackduck.com/bundle/coverity-docs-2025.3/page/checker-ref/checkers/S/sigma._checkers.html#SIGMA_checkers__section_disabled_sigma_checkers) table in the [*Coverity 2025.3.0 Checker Reference*](https://documentation.blackduck.com/bundle/coverity-docs-2025.3/page/webhelp-files/checkerref_start.html)
will be disabled by default in Coverity Analysis 2025.3, regardless of their enablement
status in previous installations.

## Analysis

- `cov-analyze` no longer supports the
  `--misra-config` option. Use the
  `--coding-standard-config` option instead.
- The Coverity integration with Incredibuild is no longer supported.
- The NULL_FIELD checker is now enabled by default. (It was formerly disabled
  by default.)

## Integrations

The following plug-ins are no longer supported.

- Synopsys Coverity for Jenkins (aka Coverity Jenkins) plug-in.
- Synopsys Coverity for Azure DevOps plug in

Instead, use the Black Duck Security Scan plug-in, available on the Jenkins
and Azure marketplaces.

See also the following documentation.

**For Jenkins**

- [Using the Black Duck Security Scan Jenkins Plug-In with Coverity](https://documentation.blackduck.com/bundle/bridge/page/documentation/security_scan_for_coverity.html)
- [Jenkins - Black Duck Security Scan Plugin for Jenkins](https://documentation.blackduck.com/bundle/bridge/page/documentation/c_using-jenkins-plugin.html)
- [Jenkins Prerequisites](https://documentation.blackduck.com/bundle/bridge/page/documentation/c_jenkins-prerequisites.html)

**For Azure**

- [Using the Black Duck Security Scan Extension with
  Coverity](https://documentation.blackduck.com/bundle/bridge/page/documentation/c_azure-with-coverity.html)
- [Azure DevOps prerequisites](https://documentation.blackduck.com/bundle/bridge/page/documentation/c_azure-prerequisites.html)
- [Azure DevOps – Black Duck Security Scan Extension for Azure DevOps](https://documentation.blackduck.com/bundle/bridge/page/documentation/c_security-scan-for-azure-devops.html)

## Coverity CLI

- The Coverity CLI will no longer validate Java web applications by default. The
  default setting for `validate-webapp` has been changed to
  `false`.
- The default arguments passed to “cov-analyze” have been modified. **Instead of**`--android-security`, `--webapp-security`,
  and `--webapp-security-aggressiveness-level`
  **the Coverity CLI will now pass**
  `--recommended-security-checkers`.
