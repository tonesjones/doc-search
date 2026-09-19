---
title: "Central Integrations release notes"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/central-integrations-release-notes.html"
content_id: "DGzGhA5zGE2c9VhXWt_lzA"
version: "latest"
section: "Central Integrations release notes"
scraped_at: "2026-08-08T23:46:47.600024+00:00"
---

# Central Integrations release notes

Everything that's new in Bridge CLI and integrations.

## Integrations support for Polaris SAST Fix Pull Requests

Bridge Integrations can create SAST Fix Pull Requests from Polaris SAST scan results in CI workflows. Fix Pull Requests contain AI-generated code fixes for eligible SAST vulnerabilities detected on monitored branches. For further details refer to release notes included in August 2026.

## Integrations support for Polaris SCA Container Analysis

Bridge Integrations can upload a pre-built container image archive to Polaris for SCA analysis, including analysis of container image layers, open source components, vulnerabilities, and license information. For further details refer to the releases notes included in August 2026.

## Support for Polaris SAST Fix PRs

Bridge can create SAST Fix Pull Requests from Polaris SAST scan results in CI workflows. Fix Pull Requests contain AI-generated code fixes for eligible SAST vulnerabilities detected on monitored branches. For further details, refer to Bridge release notes included in July 2026 and Using SAST Fix PRs with Bridge.

## Support for Polaris SCA Container Analysis

Bridge CLI can upload a pre-built container image archive to Polaris for SCA analysis, including analysis of container image layers, open source components, vulnerabilities, and license information. For further details refer to Bridge releases notes include in July 2026 and Using SCA Container Scan with Bridge.

## GitHub Action 2.10.1 released

For further details refer to release notes included in July 2026.

## Bridge 4.5.0 released

For further details refer to Bridge release notes included in July 2026.

## Support for Polaris Binary Analysis

Polaris Binary Analysis is now available enabling SCA scans to analyze binary and archive files. This capability provides visibility into open source components and license risk even when source code is not available.

For further details and supported integrations refer to Bridge release notes included in July 2026.

## Black Duck Security Bulk Onboarding for Azure DevOps released

For further details refer to Bridge release notes included in June 2026

## Support for Polaris enterprise-scale tunnel sharing

For further details refer to Bridge release notes included in May 2026

## Bridge 4.4.0 released

For further details refer to Bridge release notes included in June 2026

## Polaris Fix PR post scan option added to Black Duck Onboarding Solutions

For further details refer to Bridge release notes included in June 2026

## Bridge 4.3.0 released

For further details refer to Bridge release notes included in May 2026

## GitLab Security Onboarding Solution 1.0.1 released

For further details refer to the Bridge release notes included in May 2026.

## Bridge 4.2.1 and 4.2 Released

For further details refer to the Bridge release notes included in April 2026.

## Bridge 4.1.2 Released - Resolves 4.1.0 Bitbucket and GitLab issue

Bridge CLI 4.2.1 is now available and resolves the GitLab template executor failure previously reported in 4.1.0.

If you are using the `latest` Bridge CLI bundle, no action should be required once the updated bundle is available through the normal download path.

If you explicitly pinned to Bridge CLI 4.1.0, you should update that version reference to 4.1.2.

If you removed a version pin as part of the temporary rollback to 4.0.0, you can now move forward with 4.1.2.

We apologize again for the disruption caused by the 4.1.0 release, and thank you for your patience while the issue was investigated and resolved.

## Bridge 4.1.0 issue

We are currently investigating an issue with scans on GitLab Template and Bitbucket Pipe with Bridge-CLI-Bundle-4.1.0. As a result, we have updated the latest tag in artifactory to Bridge-CLI-Bundle-4.0.0 so that all plugins will automatically download Bridge-CLI-Bundle-4.0.0 for now.

Customers running Bridge via CI pipelines should not use Bridge-CLI-Bundle-4.1.0 but instead continue with version 4.0.0.

We are working on an updated Bridge-CLI-Bundle-4.1.1 which, once released, will automatically be downloaded for customers.

## Bridge CLI 4.0: Sunset of March 2025 deprecated resources

Bridge CLI 4.0, scheduled for release at the end of **January 2026**, will sunset all resources deprecated in **March 2025**. These resources will be removed and will no longer function in version 4.0 and later.

Before upgrading, CI/CD pipelines using Bridge CLI directly should be reviewed for deprecated resources and updated to use the replacement resources.

## Important: Polaris domain migration and Bridge CLI compatibility

The availability of Synopsys domains have been extended to **March 24, 2026**. For more information, see [Migrate Polaris to the Black Duck domain](https://docs.blackduck.com/access?ft:originId=4411d74355056751ace3917564d29bc0/ee117187a16710bb1231f1919c97c0ed.topic).

**Important:** Deprecated endpoints in Polaris APIs, and versions of the Bridge CLI older than 3.6.0 will stop functioning on March 24, 2026. To avoid failures:

- Update your API scripts before March 24, 2026
- Upgrade to Bridge CLI 3.6.0 (or newer) before March 24, 2026

See [Reminder - Polaris API Deprecations and Important Due Dates for API and Bridge Upgrade Requirements](https://community.blackduck.com/s/question/0D5Uh00000ix5u5KAA/announcement-reminder-polaris-api-deprecations-and-important-due-dates-for-api-and-bridge-upgrade-requirements) in Black Duck Community, the [API reference guide](https://polaris.blackduck.com/developer/default/documentation), and Download Bridge CLI for more information.

## New Repo available

As part of the transition to Black Duck Software, we will begin transitioning [sig-repo.synopsys.com](https://sig-repo.synopsys.com/) (34.110.245.127) to [repo.blackduck.com](https://repo.blackduck.com/) (34.149.5.115) starting Sept 1st. The [sig-repo.synopsys.com](https://sig-repo.synopsys.com/) site on the old IP (34.110.245.127) will continue to be available through February 2025. All integrations now use the new [repo.blackduck.com](https://repo.blackduck.com/). Please make sure this new IP (34.149.5.115) is whitelisted if necessary.

List of deprecated Bridge CLI resources: Deprecated resources These resources will be backwards compatible until March 2025. For more information, see [migrating to new Black Duck integrations (CI/CD, CLI)](https://community.blackduck.com/s/article/integrations-black-duck-migration-instructions#Polaris)

## August 2026

- Polaris SCA Container Analysis
  - Azure DevOps | Black Duck Security Scan Extension 2.9.0 - Added support for SCA container scans. A new `SCA-CONTAINER` value is available for the `POLARIS_TEST_SCA_TYPE` parameter. Bridge CLI uploads a container image archive to Polaris for analysis. To enable this capability, specify the path to the container image archive using the `POLARIS_ARTIFACTTOUPLOAD` parameter. The `SCA_CONTAINER` test type must be used as a standalone option and cannot be combined with other SCA test types.

    When using `SCA-CONTAINER`, set `POLARIS_ASSESSMENT_TYPES` to `SCA` and provide a container name using `POLARIS_CONTAINER_NAME`.

    In the Azure DevOps Classic editor, a new `SCA-CONTAINER` value is available in the *Polaris Test Type* field. A new *Container Name* field is also available for specifying a unique name to associate with the uploaded container image archive. For more information, refer to Using the Black Duck Security Scan Extension with Polaris.
  - GitHub | Black Duck Security Scan Action 2.11.0 - Added support for SCA container scans. A new `SCA-CONTAINER` value is available for the `polaris_test_sca_type` parameter. Bridge CLI uploads a container image archive to Polaris for analysis. To enable this capability, specify the path to the container image archive using the `polaris_artifactToUpload` parameter. The `SCA_CONTAINER` test type must be used as a standalone option and cannot be combined with other SCA test types.

    When using `SCA-CONTAINER`, set `polaris_assessment_types` to `SCA` and provide a container name using `polaris_container_name`. For more information, refer to Using the Black Duck Security Scan Action with Polaris.
  - GitLab | GitLab Template 2.7.0 - Added support for SCA container scans. A new `SCA-CONTAINER` value is available for the `BRIDGE_POLARIS_TEST_SCA_TYPE` parameter. Bridge CLI uploads a container image archive to Polaris for analysis. To enable this capability, specify the path to the container image archive using the `BRIDGE_POLARIS_ARTIFACTTOUPLOAD` parameter. The `SCA_CONTAINER` test type must be used as a standalone option and cannot be combined with other SCA test types.

    When using `SCA-CONTAINER`, set `BRIDGE_POLARIS_ASSESSMENT_TYPES` to `SCA` and provide a container name using `BRIDGE_POLARIS_CONTAINER_NAME`. For more information, refer to Using the Black Duck Security Scan Template with Polaris.
- Polaris SAST Fix Pull Requests
  - Azure DevOps | Black Duck Security Scan Extension 2.9.0 - Added support for creating SAST Fix Pull Requests from Polaris SAST scan results. When enabled, Bridge CLI can create Fix Pull Requests containing AI-generated code fixes for eligible SAST vulnerabilities detected by full baseline SAST scans on monitored branches. This capability is configured by setting `POLARIS_FIXPRR_ENABLED` to `true` and configuring `POLARIS_ASSESSMENT_TYPES` to include `SAST`. Fix Pull Request creation can be filtered by severity using  `POLARIS_FIXPR_FILTER_SEVERITIES` and limited using `POLARIS_FIX_PR_MAXCOUNT`. SAST Fix Pull Requests are available only for full baseline SAST scans on monitored branches using hybrid or remote scan modes. They are not available for Pull Request scans or scans using local scan mode. Consult Using the Black Duck Security Scan Extension with Polaris for further details.
  - GitHub | Black Duck Security Scan Action 2.11.0 - Added support for for Polaris SAST Fix Pull Requests. When enabled, Bridge CLI can create Fix Pull Requests containing AI-generated code fixes for eligible SAST vulnerabilities detected by full baseline SAST scans on monitored branches. This capability is configured by setting `polaris_fixpr_enabled` to `true` and configuring `polaris_assessment_types` to include `SAST`. Fix Pull Requests creation can be filtered by severity using `polaris_fixpr_filter_severities` and limited using `polaris_fixpr_maxCount`. SAST Fix Pull Requests are available only for full baseline SAST scans on monitored branches using hybrid or remote scan modes. They are not available for Pull Request scans or scans using local scan mode. Consult Using the Black Duck Security Scan Action with Polaris for further details.
  - GitLab | GitLab Template 2.7.0 - When Polaris Fix Pull Requests are enabled, Bridge CLI can create Fix Pull Requests containing AI-generated code fixes for eligible SAST vulnerabilities detected by full baseline SAST scans on monitored branches. This capability is configured by setting `BRIDGE_POLARIS_FIXPR_ENABLED` to true and configuring `BRIDGE_POLARIS_ASSESSMENT_TYPES` to include `SAST`. Fix Pull Request creation can be filtered by severity using `BRIDGE_POLARIS_FIXPR_FILTER_SEVERITIES` and limited using `BRIDGE_POLARIS_FIX_PR_MAXCOUNT`. SAST Fix Pull Requests are available only for full baseline SAST scans on monitored branches using hybrid or remote scan modes. They are not available for Pull Request scans or scans using local scan mode. Consult Using the Black Duck Security Scan Template with Polaris for further details.

## July 2026

- GitHub | Black Duck Security Scan Action 2.10.1 - Bug fixes and technical improvements.
- Bridge 4.5.0:
  - Bug fixes and technical improvements
  - Added support for SCA container scans in the Bridge Polaris workflow. SCA container scans analyze container image archives and detect open source and license risks, even when source code is unavailable. To use this feature, the Polaris tenant must have the required container analysis entitlement.

    A new `SCA_CONTAINER` value is available for the `POLARIS_TEST_SCA_TYPE` parameter. Bridge CLI uploads a container image archive to Polaris for analysis. To enable this capability, specify the path to the container image archive using the `POLARIS_ARTIFACTTOUPLOAD` parameter. The `SCA_CONTAINER` test type must be used as a standalone option and cannot be combined with other SCA test types.

    When using `SCA_CONTAINER`, set `polaris.assessment.types` to `SCA` and provide a container name using `polaris.container.name`. For further details refer to Using SCA Container Scan with Bridge.
  - Added support for creating SAST Fix Pull Requests from Polaris SAST scan results. When enabled, Bridge CLI can create Fix Pull Requests containing AI-generated code fixes for eligible SAST vulnerabilities detected by full baseline SAST scans on monitored branches. This capability is configured by setting `BRIDGE_POLARIS_FIXPRR_ENABLED` to `true` and configuring `BRIDGE_POLARIS_ASSESSMENT_TYPES` to include `SAST`. Fix Pull Request creation can be filtered by severity using  `BRIDGE_POLARIS_FIXPR_FILTER_SEVERITIES` and limited using `BRIDGE_POLARIS_FIX_PR_MAXCOUNT`, which applies across both SAST and SCA Fix Pull Requests. SAST Fix Pull Requests are available only for full baseline SAST scans on monitored branches using hybrid or remote scan modes. They are not available for Pull Request scans or scans using local scan mode. Consult Using SAST Fix PRs with Bridge for further details.
- Polaris SCA Binary Analysis
  - Azure DevOps | Black Duck Security Scan Extension 2.8.0 - Added support for binary analysis for Polaris SCA tests. A new `SCA-BINARY` value is available for the `POLARIS_TEST_SCA_TYPE` parameter, enabling SCA scans to analyze binary or archive files providing detection of Open Source and license risk even when source code is not available. This capability is configured by specifying the file path using the new `POLARIS_ARTIFACTTOUPLOAD` parameter. The `SCA-BINARY` test type must be used as a standalone option and cannot be combined with other SCA test types. Consult Using the Black Duck Security Scan Extension with Polaris for further details.
  - Bitbucket | Bitbucket Security Scan Pipe 1.6.0 - Added support for binary analysis for Polaris SCA tests with Bitbucket Security Scan Pipe. A new `SCA-BINARY` value is available for the `BRIDGE_POLARIS_TEST_SCA_TYPE` parameter, enabling SCA scans to analyze binary or archive files providing detection of Open Source and license risk even when source code is not available. This capability is configured by specifying the file path using the new `BRIDGE_POLARIS_ARTIFACTTOUPLOAD` parameter. The `SCA-BINARY` test type must be used as a standalone option and cannot be combined with other SCA test types. Consult Using the Black Duck Security Scan Pipe with Polaris for further details.
  - GitHub | Black Duck Security Scan Action 2.10.0 - Added support for binary analysis for Polaris SCA tests. A new `SCA-BINARY` value is available for the `polaris_test_sca_type` parameter, enabling SCA scans to analyze binary or archive files providing detection of Open Source and license risk even when source code is not available. This capability is configured by specifying the file path using the new `polaris_artifactToUpload` parameter. The `SCA-BINARY` test type must be used as a standalone option and cannot be combined with other SCA test types. Consult Using the Black Duck Security Scan Action with Polaris for further details.
  - GitLab | GitLab Template 2.7.0 - Added support for binary analysis for Polaris SCA tests. A new `SCA-BINARY` value is available for the `BRIDGE_POLARIS_TEST_SCA_TYPE` parameter, enabling SCA scans to analyze binary or archive files providing detection of Open Source and license risk even when source code is not available. This capability is configured by specifying the file path using the new `BRIDGE_POLARIS_ARTIFACTTOUPLOAD` parameter. The `SCA-BINARY` test type must be used as a standalone option and cannot be combined with other SCA test types. Consult Using the Black Duck Security Scan Template with Polaris for further details.
  - Jenkins | Black Duck Security Scan Plugin 2.9.0 - Added support for binary analysis for Polaris SCA tests. A new `SCA-BINARY` value is available for the `polaris_test_sca_type` parameter, enabling SCA scans to analyze binary or archive files providing detection of Open Source and license risk even when source code is not available. This capability is configured by specifying the file path using the new `polaris_artifactToUpload` parameter. The `SCA-BINARY` test type must be used as a standalone option and cannot be combined with other SCA test types. Consult Using the Black Duck Security Scan Plugin with Polaris for further details.

## June 2026

- Azure DevOps | Azure Security Onboarding Solution 1.0.0 - The Black Duck Security Onboarding Solution is a new integration for Azure DevOps. The app will generate and deploy a workflow file to selected repositories within a workspace for conducting scans for supported Black Duck platforms: Black Duck® SCA, Coverity and Polaris. For more information, see Getting started: Black Duck Security Bulk Onboarding for Azure DevOps.
- Bridge 4.4.0
  - Bug fixes and technical improvements.
- Support added for a Fix PR post scan option for onboarding Polaris SCA workflows:
  - Bitbucket | Black Duck Security Scan App 1.0.2
  - GitHub | Black Duck Security Scan App 1.3.1
  - GitLab | GitLab Security Onboarding Solution 1.0.2

## May 2026

- Bridge 4.3.0
  - Fixed inaccuracies in SARIF reporting of signature scan components, which are now correctly classified with complete details and reflected in GHAS and other SARIF-compatible tools. SARIF output now includes both existing findings and findings from the current run when signature scan is enabled, provided `polaris.assessment.types` includes SCA and `polaris.reports.sarif.create` is set to true. If configured, `polaris.reports.sarif.issue.types` must also include SCA. On the first run after upgrading, existing GHAS SCA alerts are closed and recreated with updated fingerprints.
  - Added `polaris.tunnel.name` resource for use with the `polaris-secure-tunnel` workflow to allow tenant level tunnel support for internal DAST projects and access to on-prem integrations for GitHub Enterprise. For further details refer to Using Polaris secure tunnel.
- GitLab | GitLab Security Onboarding Solution 1.0.1 - Workflow onboarding filenames have been updated: the Black Duck® SCA filename is now `blackducksca-ci.yml`, Coverity filename is now `coverity-ci.yml`, and Polaris filename is now `polaris-ci.yml`.

## April 2026

- Bridge 4.2.1 - Minor bug fixes and technical improvements.
- GitLab | GitLab Security Onboarding Solution 1.0.0 - The Black Duck Security Onboarding Solution is a new integration for GitLab. The app will generate and deploy a workflow file to selected repositories within a workspace for conducting scans for supported Black Duck platforms: Black Duck® SCA, Coverity and Polaris.
- Bitbucket | Black Duck Security Scan Pipe 1.6.0 - Added support for Fix Pull Request creation for Polaris
- Bridge 4.2
  - Support added for Signal Enterprise.
  - Use Bridge to upload a binary or archive for SCA scanning with Polaris, enabling detection of open source and license risk even when source code is not available.
  - Minor bug fixes and technical improvements.
- Azure DevOps | Black Duck Security Scan Extension 2.7.0 - Added support for Fix Pull Request creation for Polaris
- Bitbucket | Black Duck Security Scan App 1.0.1 - Support has been added to specify test locations for SAST (hybrid, local or remote) and SCA (hybrid or remote) assessment types in Black Duck Security Scan App for Polaris.
- GitHub | GitHub Security Scan App 1.3.0 - Adds enhanced Polaris scan configuration, that includes Polaris source code upload and configurable test locations for SAST and SCA assessment types. New post-scan options allow publishing findings to GitHub Issues or GitHub Advanced Security via SARIF for Polaris and Black Duck® SCA
- GitLab | GitLab Template 2.7.0 - Added support for Fix Pull Request creation for Polaris
- GitHub | Black Duck Security Scan Action 2.9.0 - Added support for Fix Pull Request creation for Polaris SCA scans; Fix Pull Requests are automatically raised on specified branch.
- Jenkins | Black Duck Security Scan Plugin 2.8.0 - Added support for Fix Pull Request creation for Polaris SCA scans; Fix Pull Requests are automatically raised on specified branch.
- Bridge 4.1.1 - Bug fix for scan issues encountered with Bitbucket Pipe and GitLab Template.

## March 2026

- Bridge 4.1
  - Added support for Bridge Signal, enabling AI-powered Signal CLI scans of explicit file paths, staged changes or changes relative to a reference branch, with findings written to a SARIF report.
  - Fix Pull Request creation for Polaris SCA scans; Fix Pull Requests are automatically raised on specified branch.
  - Minor bug fixes and technical improvement
- Bitbucket | Black Duck Security Scan App 1.0.0 - The Black Duck Security Scan App is a new integration for Bitbucket. The app will generate and deploy a workflow file to selected repositories within a workspace for conducting scans for supported Black Duck platforms: Black Duck® SCA, Coverity and Polaris.
- GitHub | Black Duck Security Scan Action 2.8.0 - Added `blackducksca_externalIssues_create`,  `polaris_externalIssues_create` and associated configuration parameters to enable GitHub issues to be created from scan findings for Polaris and Black Duck® SCA. Documentation and examples for these parameters are available on the Using the Black Duck Security Scan Action with Polaris and Using the Black Duck Security Scan Action with Black Duck SCA pages.

## February 2026

- Bridge 4.0 - Minor bug fixes and technical improvements. Resources listed in March 2025 deprecations have now been sunset. Bridge CLI now supports creating and managing repository issues from Polaris and Black Duck® SCA scan results as part of CI workflows. This feature automatically opens, updates and closes issues based on the latest security findings, enabling development teams to track remediation work directly in the source code repository.

## January 2026

- GitHub | Black Duck Security Scan App 1.2.0 - Enhanced repository onboarding with search filters for name, language, license, visibility and topic.
- Azure DevOps | Black Duck Security Scan Extension 2.6.0 - Added `COVERITY_VERSION` parameter to select which Coverity version should be used for Polaris local and hybrid SAST scans. The `Coverity Version` field is located in the `Coverity (SAST) Tool Options` group in the Classic Editor UI. For the Black Duck Security Coverity extension, this field was moved from the `Scan Options` group. Documentation for this parameter is found on the Using The Black Duck Security Scan Extension with Polaris page.
- Bitbucket | Black Duck Security Scan Pipe 1.6.0 - Added `BRIDGE_COVERITY_VERSION` variable to select which Coverity version should be used for Polaris local and hybrid SAST scans. Documentation for this parameter is found on the Using Black Duck Security Scan Pipe with Polaris page and in the Complete List Of Bridge Commands page.
- Jenkins | Black Duck Security Scan Plugin 2.7.0 - Added `coverity_version` parameter to select which Coverity version should be used for Polaris local and hybrid SAST scans. Documentation for this parameter is found on the Using The Black Duck Security Scan Action With Polaris page.

## December 2025

- Bridge 3.11 - SARIF reports generated for Black Duck SCA now includes signature scan findings. Additional match types `FILE_EXACT`, `FILE_SOME_FILES_MODIFIED`, `FILE_FILES_ADDED_DELETED_AND_MODIFIED` and `FILE_EXACT_FILE_MATCH` will be included in the SARIF file.
- GitHub | Black Duck Security Action 2.7.0 - Added `coverity_version` parameter to select which Coverity version should be used for local and hybrid SAST scans. Documentation for this parameter is found on the Using The Black Duck Security Scan Action With Polaris page.
- GitLab | Black Duck Security Scan Template 2.6.0 - Added `BRIDGE_COVERITY_VERSION` variable to select which Coverity version should be used for local and hybrid SAST scans. Documentation for this parameter is found on the Using Black Duck Security Scan Template with Polaris page and in the Complete List Of Bridge Commands page.
- Bridge 3.10.1 - Support added for selecting Coverity version for Polaris SAST scans. Documentation for this feature is found on the Polaris multi version SAST tool support with Bridge page.

## November 2025

- Azure DevOps | Black Duck Security Scan Extension 2.5.0 - Added support for using a proxy through GitHub Action's environment. Documentation for this feature is found on the Additional Azure DevOps Configuration page.
- Bitbucket | Black Duck Security Scan Pipe 1.6.0 - Added support for using a proxy through Bitbucket's environment. Documentation for this feature is found on the Additional Bitbucket Parameters page.
- Bridge 3.10.1 - Minor bug fixes and technical improvements.
- Bridge 3.10 - Minor bug fixes and technical improvements.
- GitHub | Black Duck Security Action 2.6.0 - Added support for using a proxy through GitHub Action's environment. Documentation for this feature is found on the Additional Github Parameters page.
- GitHub | Black Duck Security Scan App 1.1.0 - Added flexible commit options for generated workflows: direct to branch or via Pull Request. Users can now choose between Black Duck Security Scan workflow or direct Bridge CLI usage. Generated workflows automatically use secrets.GITHUB_TOKEN with appropriate permissions. Includes UI enhancements.
- GitLab | Black Duck Security Scan Template 2.6.0 - Added support for using a proxy through GitLab Template's environment. Documentation for this feature is found on the Additional GitLab Parameters page.

## October 2025

- Local analysis is now available for the following integrations.

  Note: Versions remain the same for Security Scan, Security Scan Template and Bridge.

  - Azure DevOps | Black Duck Security Scan Extension 2.4.0 - Deprecated parameter `POLARIS_ASSESSMENT_MODE`. For source upload scans, use `POLARIS_TEST_SAST_LOCATION=remote` and/or `POLARIS_TEST_SCA_LOCATION=remote`. Added support for Polaris Local Analysis, enabled by setting `POLARIS_TEST_SAST_LOCATION=local`. Also includes Coverity Fail PRs.
  - Jenkins | Black Duck Security Scan Plugin 2.6.0 - Deprecated parameter `POLARIS_ASSESSMENT_MODE`. For source upload scans, use `POLARIS_TEST_SAST_LOCATION=remote` and/or `POLARIS_TEST_SCA_LOCATION=remote`. Added support for Polaris Local Analysis, enabled by setting `POLARIS_TEST_SAST_LOCATION=local`.
  - Bitbucket | Black Duck Security Scan Pipe 1.4.0 - Deprecated parameter `POLARIS_ASSESSMENT_MODE`. For source upload scans, use `POLARIS_TEST_SAST_LOCATION=remote` and/or `POLARIS_TEST_SCA_LOCATION=remote`. Added support for Polaris Local Analysis, enabled by setting `POLARIS_TEST_SAST_LOCATION=local`.
  - GitHub | Black Duck Security Scan 2.4.0 - Deprecated parameter `polaris_assessment_mode`. For source upload scans, use `polaris_test_sast_location=remote` and/or `polaris_test_sca_location=remote`. Added support for Polaris Local Analysis, enabled by setting `polaris_test_sast_location=local`.
  - GitLab | Black Duck Security Scan Template 2.4.0 - Deprecated parameter `POLARIS_ASSESSMENT_MODE`. For source upload scans, use `POLARIS_TEST_SAST_LOCATION=remote` and/or `POLARIS_TEST_SCA_LOCATION=remote`. Added support for Polaris Local Analysis, enabled by setting `POLARIS_TEST_SAST_LOCATION=local`.
  - Bridge 3.8.1 - Support added for Polaris Local Analysis
- Azure Devops | Black Duck Security Scan Extension 2.4.1 - Minor bug fixes and technical improvements.
- Bridge 3.9.2 - Updated SARIF generation components.
- Bridge 3.9.1 - Minor bug fixes and technical improvements.
- Bitbucket Pipe | Black Duck Security Scan Pipe 1.5.0 - Added Coverity Fail Pull Request feature that automatically fails builds and adds Pull Request comments when security issues matching specified impact levels are detected during Pull Request scans.
- Jenkins | Black Duck Security Scan Plugin 2.5.0 - Added Coverity Fail Pull Request feature that automatically fails builds and adds Pull Request comments when security issues matching specified impact levels are detected during Pull Request scans.
- GitLab | Black Duck Security Scan 2.5.0 - Added Coverity Fail Pull Request feature that automatically fails builds and adds Pull Request comments when security issues matching specified impact levels are detected during Merge Request scans.
- GitHub | Black Duck Security Scan 2.5.0 - Added Coverity Fail Pull Request feature that automatically fails builds and adds Pull Request comments when security issues matching specified impact levels are detected during Pull Request scans.
- GitHub | Black Duck Security Scan App 1.1.0 - Added flexible commit options for generated workflows: direct to branch or via Pull Request. Users can now choose between Black Duck Security Scan workflow or direct Bridge CLI usage. Generated workflows automatically use secrets.GITHUB_TOKEN with appropriate permissions. Includes UI enhancements.

## September 2025

- Bridge 3.9 - Includes minor bug fixes and technical improvements. Sub-directories generated within the `.bridge` directory are no longer named containing spaces. New parameters `coverity.prcomments.enabled` and `coverity.prcomments.impacts` have been added to support Pull Request comments for issues matching specific impact filters. Matched issues will be uploaded to Coverity and will break the build. Please note that `coverity.automation.prcomments` is scheduled for deprecation. More information can be found here: Deprecated resources.
- Bitbucket | Black Duck Security Scan Pipe 1.4.0 - Technical improvements and bug fixes.
- GitHub | Black Duck Security Scan 2.4.0 - Technical improvements and bug fixes.
- GitLab | Black Duck Security Scan Template 2.4.0 - Technical improvements and bug fixes.
- Jenkins | Black Duck Security Scan Plugin 2.4.0 - Technical improvements and bug fixes.
- Azure Devops | Black Duck Security Scan Extension 2.3.1 - Minor bug fixes
- Azure Devops | Black Duck Security Scan Extension 2.3.0 - Added support for On-Premise servers. The following Azure DevOps Servers (On-Prem) are supported: 2019, 2020, 2022. All features available for Cloud are now fully supported in On-Prem environments.
- Bridge 3.8.1 - Includes a critical bug fix relating to PR comment feature for Black Duck SCA.

## August 2025

- Bridge 3.8 - Includes minor bug fixes and tech improvements. Added `polaris.test.sca.location` and `polaris.test.sast.location` parameters to configure source code upload for SAST and SCA assessment types. Please note that `polaris.assessment.mode=SOURCE_UPLOAD` is scheduled for deprecation. More information can be found here: Deprecated resources. Added support for Polaris Local Analysis.
- Azure Devops | Black Duck Security Scan Extension 2.2.0 - Default SARIF file path has changed for Polaris and SCA. Added support for `POLARIS_TEST_SAST_TYPE`: users may specify full or rapid scan for SAST tests.
- Bitbucket Pipe | Black Duck Security Scan Pipe 1.3.0 - Added support for configuring self-signed signed certificates and trust all certificates.
- Bridge 3.7.1 - Update behavior for Rapid Scan Static in Bridge CLI. If an attempt is made to run a rapid scan before a full SAST test is completed, Bridge starts a full SAST scan automatically. More information can be found here: Using Rapid Scan Static with Bridge
- GitLab | Black Duck Security Scan Template 2.3.0 - Default SARIF file path and default GitLab Reports directory path have changed for Polaris and SCA. Added support for configuring SSL certificate verification (Coverity and Black Duck SCA only).
- Jenkins | Black Duck Security Scan Plugin 2.4.0 - Added support for `polaris_test_sast_type`: users may specify full or rapid scan for SAST tests. Added support for configuring SSL certificate verification (Coverity and Black Duck SCA only).

## July 2025

- GitHub | Black Duck Security Scan App 1.0.0 - The Black Duck Security Scan App is a new integration for GitHub. The app alows users to configure pipelines for many repositories at once, and well as single repositories. Polaris, SCA, and Coverity are supported. Documentation can be found here: GitHub App – Black Duck Security
- Bitbucket Pipe | Black Duck Security Scan Pipe 1.2.0 - Default SARIF file path has changed for Polaris and SCA.
- Jenkins | Black Duck Security Scan Plugin 2.3.0 - Changed default SARIF path for Polaris and SCA. Updated documentation on best practices when using with Docker.
- GitHub | Black Duck Security Scan 2.3.0 - Added support for configuring SSL certificate verification, for SCA and Coverity Connect. Changed default SARIF path for Polaris and SCA.
- Bridge 3.7 - Added support for Polaris DAST scans. Configuration requirements can be found here: DAST configuration requirements
- Rapid Scan Static support - Polaris users can now run Rapid Scan Static using the Bridge CLI. More information can be found here: Using Rapid Scan Static with Bridge
- Bridge 3.6 - Added support for self-signed certificates, available for Coverity Connect and SCA workflows. New parameters can be found in Unervesal Bridge CLI Options on the Complete list of Bridge arguments page.

## June 2025

- GitHub | Black Duck Security Scan 2.2.0 - Added support for major version tags (see Additional GitHub configuration for more information). Added support for Linux ARM. (Linux ARM is supported for Coverity scans only.)
- GitLab | Black Duck Security Scan Template 2.2.0 - GitLab Vulnerability Reports are now supported. Added support for Linux ARM. (Linux ARM is supported for Coverity scans only.)
- Azure Devops | Black Duck Security Scan Extension 2.1.0 - Added support for Linux ARM. (Linux ARM is supported for Coverity scans only.)
- Bitbucket Pipe | Black Duck Security Scan Pipe 1.1.0 - Public and private Docker images are now supported. New parameters are avaliable for custom Docker image configuration. (see Setting up Black Duck Security Scan Pipe for more information) Added support for Linux ARM. (Linux ARM is supported for Coverity scans only.)
- Jenkins | Black Duck Security Scan Plugin 2.2.0 - Added support for Linux ARM. (Linux ARM is supported for Coverity scans only.)
- PR Comments concpet article added to documentation: Pull request (PR) comments

## May 2025

- Bridge 3.5.0 / 3.5.1 - Added support for Linux ARM. Minor updates & bug fixes.
- GitHub | Black Duck Security Scan 2.2.0 - Added support for major version tags (see Additional GitHub configuration for more information). Added support for Linux ARM. (Linux ARM is supported for Coverity scans only.)
- GitLab | Black Duck Security Scan Template 2.2.0 - GitLab Vulnerability Reports are now supported. Added support for Linux ARM. (Linux ARM is supported for Coverity scans only.)
- Azure Devops | Black Duck Security Scan Extension 2.1.0 - Added support for Linux ARM. (Linux ARM is supported for Coverity scans only.)

## April 2025

- GitLab | Black Duck Security Scan Template 2.1.0 - Added support for `mark_build_status` Bridge parameter.
- Bitbucket Pipe | Black Duck Security Scan Pipe 1.0.0 - Bitbucket users can now use Black Duck Security Scan Pipe and Bridge CLI to automate scanning with Black Duck tools in Bitbucket Pipes.

## March 2025

- Bridge 3.4.0 - Bridge now supports the ability to run a Package Manager Scan and a Signature Scan in the same pipeline. This feature is avaliable to Polaris users through the `polaris.tests.sca.type` parameter.
- Black Duck Security Scan Action for GitHub 2.1.1 - Added support for SARIF uplaod on GitHub Enterprise server.
- Black Duck Security Scan Action for GitHub 2.1.0 - Added support for `mark_build_status` Bridge parameter.
- Black Duck Security Scan Extension for Azure DevOps 2.0.0 - Added SARIF upload support for Advanced Security dashboard.
- Black Duck Security Scan Plugin for Jenkins 2.1.1, 2.1.2 - Bug fixes.

## February 2025

- Bridge 3.3.0 - minor bug fixes.
- Black Duck Security Scan Plugin for Jenkins 2.1.0 - Dashboard link and issue count for Polaris, Coverity, and SRM now applicable for push events. Additionally, SCA now has automated Fix PR creation support for GitHub, GitLab, and Bitbucket repositories through multibranch pipelines.

## January 2025

- Minor fixes and improvements.

## December 2024

- Now, you can use the Bridge CLI to run Polaris Secure Tunnel. Polaris Secure Tunnel establishes a secure connection between Polaris and your private network, allowing you to run DAST tests on applications and APIs on your internal network.

  See Connect to an internal DAST target from Bridge CLI for more information.
- Black Duck Security Scan Plugin for Jenkins 2.0.0 has been released. It includes:
  - Synopsys Security Scan Plugin has been renamed to Black Duck Security Scan Plugin.
  - Updated deprecated resources for Black Duck SCA.
- Black Duck Security Scan Extension for Azure DevOps 2.0.0 has been released. It includes:
  - Synopsys Security Scan Extension has been renamed to Black Duck Security Scan Extension.
  - Updated deprecated resources for Black Duck SCA.
- Black Duck Security Scan Template 2.0.0 has been released. It includes:
  - Synopsys GitLab Template has been renamed to Black Duck Security Scan Template.
  - Updated deprecated resources for Black Duck SCA.

## November 2024

- Black Duck Security Scan Action 2.0.0 has been released. It includes:
  - Synopsys GitHub Action has been renamed to Black Duck Security Scan Action.
  - Updated deprecated resources for Black Duck SCA.
- Bridge CLI Bundle and Bridge Thin Client are now available. The existing Bridge package has been renamed to Bridge CLI Bundle and includes all the features.
- Updated Bridge CLI resource names. Old names have been deprecated. You can review the list here: Deprecated resources

## September 2024

- GitHub Action 1.13.0 is available. You can now run scans in asynchronous (non-blocking) mode.

- Synopsys Security Scan Extension for Azure DevOps is available. You can now run scans in asynchronous (non-blocking) mode.

- GitLab 1.11.0 is now available. You can now run scans in asynchronous (non-blocking) mode.

- Jenkins 1.8.0 is now available. This release includes the following:
  - Jenkins now supports scanning with Software Risk Manager.
  - You can now run scans in asynchronous (non-blocking) mode.

- Bridge 2.9.0 is now available. You can now run scans in async mode.

## August 2024

- Jenkins 1.7.0 is now available. Polaris SCA users can choose between a "Signature Scan" or a "Package Scan".
- GitHub Action 1.12.0 now supports scanning with Software Risk Manager.
- GitLab Template 1.10.0 now supports scanning with Software Risk Manager.

## July 2024

- Bridge 2.7.0 is now available. This release includes the following:
  - Support for Application onboarding on Polaris.
  - HTML tags in PR comments for Bitbucket Data Center are not supported.
  - In case the user triggers both SAST and SCA scans - Bridge would run SAST first.

- Synopsys Security Scan Extension for Azure DevOps 1.8.0 is available. This release includes the following:
  - Polaris users can run "Signature Scan" as an alternative to the existing "Package Scan".
  - Polaris, Coverity and Black Duck customers can pass tool options through Synopsys Security Scan.
  - Users now have the ability to mark build as "Failed", "SucceededWithIssues" or "Succeeded" when issues are detected. Default is "Failed".

- GitLab Template now supports Signature Scan. Polaris users can run "Signature Scan" as an alternative to the existing "Package Scan".

- Jenkins 1.6.0 is now available. Polaris, Coverity and Black Duck customers can pass tool options through Synopsys Security Scan.

- GitHub Action 1.11.0 is now available. Polaris users can run "Signature Scan" as an alternative to the existing "Package Scan".

- Polaris users can run "Signature Scan" as an alternative to the existing "Package Scan" with Bridge CLI.

- Jenkins 1.5.0 is now available. This release includes the following:
  - Polaris users can use the "Upload files to Polaris" option as an alternative to the existing build capture method.
  - Bitbucket Cloud SCM is now supported with Jenkins.
  - Users now have the ability to mark build as "Unstable" or "Successful" when issues are detected. Default is "Failed".

## June 2024

- GitLab Template 1.9.0 is now available. Coverity and Black Duck users can pass tool options through GitLab Template.

- GitHub Action 1.10.0 is now available. Polaris users can use the "Upload files to Polaris" option as an alternative to the existing build capture method. Coverity and Black Duck users can pass tool options through GitHub workflow.

- Bridge CLI 2.6.0 is available. Users can now pass Coverity and Black Duck options through Bridge command line.

- Synopsys Security Scan Extension for Azure DevOps 1.7.0 is available. This release includes the following:
  - Workflow simplification for Black Duck, Coverity and Polaris.

- New quickstart workflows available for Polaris:
  - Quickstart: Polaris Bridge CLI in a GitHub workflow
  - Quickstart: Polaris Bridge CLI in a GitLab template
  - Quickstart: Polaris Bridge CLI in a Jenkins pipeline
  - Quickstart: Polaris Bridge CLI in an Azure DevOps pipeline
  - Quickstart: Black Duck Security Scan Action with Polaris
  - Quickstart: GitLab Template with Polaris
  - Quickstart: Jenkins Black Duck Security Scan Plugin with Polaris
  - Quickstart: Azure with Polaris

- GitLab template 1.8.0 is now available. This release includes the following:
  - New simplified workflows for Coverity, Polaris and Black Duck.

## May 2024

- Synopsys Security Scan for Jenkins 1.4.0 is available. This release includes the following:
  - Workflow simplification for multi-branch pipeline jobs for Black Duck, Coverity and Polaris.
  - PR comments for Polaris.
- Bridge CLI 2.5.0 is available. Now you can upload source code to scan or use the existing build capture method.

## April 2024

- Minor fixes and improvements.

## March 2024

- Synopsys Security Scan Extension for Azure DevOps 1.6.0. is available. This release includes the following:
  - Ability to export issues to a SARIF file for Polaris.
  - PR comments for Polaris.
- Using Jenkins, you can export issues to a SARIF file with Polaris and Black Duck.
- Using Azure DevOps, you can export issues to a SARIF file and enable PR comments for Polaris.
- Using the GitLab template, you can export issues to a SARIF file and enable PR comments for Polaris.
- You can now export issues from your Polaris projects to a SARIF file using the Bridge CLI via the new `polaris.reports.sarif.create` argument. See Exporting a SARIF file for more information.
- When running the Bridge CLI, use the `--out <outFile>` command to save final state data to a file. Sensitive information is masked, by default. To include sensitive information in the file, use `--include-sensitive-information` with `--out`.

## February 2024

- Bridge CLI 2.3.0 is available. Now you can export SARIF report for Polaris.
- GitHub Action 1.8.0 is available. Now you can create a SARIF report and post issues to GitHub Advanced Security.
- Synopsys Security Scan Extension for Azure DevOps 1.5.0 is available. This release includes the following:
  - Support for Mac M1/M2 machines by making available an ARM binary of the Bridge CLI for installation.
  - Ability to generate a SARIF report for SCA issues for Black Duck.
- Synopsys Security Scan for Jenkins 1.2.0 is available. This release includes the following:
  - Support for Mac M1/M2 machines by making available an ARM binary of the Bridge CLI for installation.
  - Support for GitHub, GitLab environments in multi-branch pipelines.
  - Support for freestyle and scripted jobs.

## January 2024

- GitLab Template 1.6.0 is available. This release includes the following:

  Support for Mac M1/M2 machines by making available an ARM binary of the Bridge CLI for installation.

  Ability to generate a SARIF report for SCA issues for Black Duck.
- GitHub Action 1.7.0 available. Includes support for Mac M1/M2 machines by making available an ARM binary of the Bridge CLI for installation.
- GitLab Synopsys Template version 1.5.0 is now available.
- As part of Template 1.5.0 release, the property BRIDGE_POLARIS_BRANCH_NAME becomes mandatory, when using the template with Polaris.
- For self-managed GitLab environments, PR comments and Fix PRs require GitLab 15.7 or Later.

## December 2023

- When using Bridge CLI client with GitHub, the variable github.api.url is **deprecated** and is no longer a required variable. It will be removed in a future release. GitHub Enterprise users should use github.host.url to provide the URL of their self-hosted GitHub instance.
- For users of **GitLab Enterprise**, PR Comments and Fix PRs require GitLab 15.7 or later.

## November 2023

- Bridge 2.0 command line client is available. With the introduction of branching in Polaris, branch name is now a required field when using Bridge with Polaris.
- Synopsys Security Scan for Jenkins 1.0.0 became available. At this time, it works only with Bitbucket SCM.
- Known issue: If the name of a file contains spaces, and vulnerabilities are found by Coverity, PR comments will not be created. This issue is observed only in PR comments for Coverity scans in Bitbucket SCM with Jenkins. It does not affect the following.
  - Filenames without spaces.
  - Polaris or Black Duck usage.
  - Integrations other than the Jenkins plug-in.
  - SCM other than Bitbucket.

## October 2023

- Released Synopsys Security Scan Extension for Azure DevOps version 1.3.2. Supports Fix PRs in Black Duck Hub.
- Released GitLab Synopsys Template version 1.4.0. Supports Fix PRs in Black Duck Hub.
- Released GitHub Synopsys Action 1.5.0. Supports Fix PRs in Black Duck Hub.
- Synopsys Bridge CLI 1.2.0. Supports Fix PRs in Black Duck Hub.

## September 2023

**New features and changes**

- GitHub pull request comment support added for Polaris users.
- New pull request comment code examples have been added in Using Synopsys Bridge CLI with Polaris.
- For SCA scans: The default value for Detect's search depth that Bridge uses has been changed from `3` to `0`. You can override the default value using the `DETECT_DETECTOR_SEARCH_DEPTH` environment variable.
- For SCA scans: You can now exclude directories from Detect scan by setting the `DETECT_EXCLUDED_DIRECTORIES` environment variable.
- Airgap support has been added for SRM.
- Pull request comment support added for Polaris, including new `polaris.prcomment.enabled` and `polaris.prcomment.severities` arguments.
- `polaris.branch.parent.name` argument has been added to support Polaris pull request comments.
- `polaris.branch.name` argument has been added to support Polaris branching.

## August 2023

**New features and changes**

- Synopsys Security Scan Extension for Azure DevOps codeblock examples have been updated to version 1.1.2.
- In Additional GitHub Configuration, `synopsys_bridge_path` has been replaced with `synopsys_bridge_install_directory`. If you use this configuration, update your GitHub workflow accordingly.
- In Additional GitLab Configuration, `SYNOPSYS_BRIDGE_PATH` has been replaced with `SYNOPSYS_BRIDGE_INSTALL_DIRECTORY`. If you use this configuration, update your GitLab `.gitlab-ci.yml` file accordingly.
- In Additional Azure DevOps Configuration, `SYNOPSYS_BRIDGE_PATH` has been replaced with `SYNOPSYS_BRIDGE_INSTALL_DIRECTORY`. If you use this configuration, update your Azure configuration accordingly.
- Coverity Cloud Deployment 2023.6 support has been added.
- Software Risk Manager (SRM) support has been added.
- Air Gap support has been added.
