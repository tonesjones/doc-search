---
title: "Using the Black Duck Security Scan Plugin with Polaris"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-plugin-with-polaris.html"
content_id: "xbq1NjuyLXf2Xv9EM1M0yw"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:37.563272+00:00"
---

# Using the Black Duck Security Scan Plugin with Polaris

The Black Duck Security Scan Plugin can be used with Jenkins Multibranch, Pipeline and Freeestyle projects.

The Jenkins dashboard link and issue count for Polaris scans is applicable for push events only. The dashboard link is not shown for Pull Requests.

## Choose pipeline for use with Polaris

Use the decision table below to choose a suitable type of Jenkins pipeline and view examples for Polaris.

| Pipeline type | Use when... | Example |
| --- | --- | --- |
| **Multibranch Pipeline** | - Declarative or Scripted Jenkinsfile pipelines preferred. - Enterprise applications requiring full feature set. - PR Comments and Fix PRs are required. | Multibranch Pipeline |
| **Pipeline** | - Declarative or Scripted Jenkinsfile pipelines preferred. - Push/merge scans only needed for protected branches. - PR Comments and Fix PRs not required. | Pipeline |
| **Freestyle** | Simplest method:   - UI based scan configuration. - Push/merge scans only needed for protected branches. - PR Comments and Fix PRs not required. | Freestyle |

Note: By default, Polaris server URL and access token parameters configured in the Black Duck Security Scan Plugin are used by all Multibranch Pipeline, Pipeline and Freestyle projects. For Multibranch Pipeline and Pipeline projects, these parameters can be overridden in the Jenkinsfile using the `polaris_server_url` and `polaris_access_token` parameters. For Jenkins freestyle projects these parameters **cannot** be overridden.

## Polaris parameters

| Input parameter | Description | Mandatory / optional |
| --- | --- | --- |
| `bitbucket_token` | Applies to Bitbucket users. The token can be configured in Jenkins global configurations or can be passed as environment variable. This is required if `prcomment` is set to `true`. Example: `bitbucket_token: "${env.BITBUCKET_TOKEN}"` | Optional |
| `github_token` | Applies to GitHub users. The token can be configured in Jenkins global configurations or can be passed as environment variable. This is required if `prcomment` is set to `true`.  Example, `github_token: "${env.GITHUB_TOKEN}"`. | Optional |
| `gitlab_token` | Applies to GitLab users. The token can be configured in Jenkins global configurations or can be passed as environment variable. This is required if `prcomment` is set to `true`.  Example, `gitlab_token: "${env.GITLAB_TOKEN}"`. | Optional |
| `polaris_access_token` | Access token for the Polaris server. The token can also be provided in Jenkins **Global Configuration** or passed as an **Environment Variable**. For example, `polaris_access_token: "${env.BRIDGE_POLARIS_ACCESSTOKEN}"`. | Mandatory (unless configured in Jenkins Global Configuration) |
| `polaris_application_name` | The application name that was created on the Polaris server.  The default value is the name of the repository. | Optional for multibranch pipeline (Mandatory for freestyle and pipeline jobs) |
| `polaris_assessment_types` | Specifies the type of scan to run  Accepted values:   - `DAST` - `SAST` - `SCA` - `SAST,SCA`   For DAST configuration requirements, see Using Bridge CLI With Polaris. | Mandatory |
| `polaris_branch_name` | The branch name in the Polaris Server.  The default value is the name of the branch. | Optional for multibranch pipeline (Mandatory for freestyle and pipeline jobs) |
| `polaris_project_name` | The project name that was created in Polaris.  The default value is the name of the repository. | Optional for multibranch pipeline (Mandatory for freestyle and pipeline jobs) |
| `polaris_server_url` | URL for the Polaris server. The URL can also be configured in Jenkins **Global Configuration** or can be passed as an **Environment Variable**. For example, `polaris_server_url: "${env.BRIDGE_POLARIS_SERVERURL}"` | Mandatory (unless configured in Jenkins Global Configuration) |
| `product` | Name of the Black Duck security product. Example: `product: "POLARIS"` | Mandatory |
| `polaris_reports_sarif_create` | Set this to true to generate SARIF report.  **Default**: `false`  Note: SARIF reports can be generated for any configured branch; however, report generation is not supported in a PR/MR context. | Optional |
| `polaris_reports_sarif_file_path` | File path (including file name) where SARIF report is created.  **Default**: `.blackduck/integrations/polaris/sarif/report.sarif.json` | Optional |
| `polaris_reports_sarif_severities` | Comma-separated list of SAST/SCA issue severities to include in SARIF file report. Valid severities are `Critical`, `High`, `Medium`, `Low`, and `Informational`.  **Default**: All severities are included. | Optional |
| `polaris_reports_sarif_groupSCAIssues` | When set to true, SCA issues are grouped by component. Set this to false to list SCA issues by vulnerability.  **Default**: `true` | Optional |
| `polaris_prComment_enabled` | Set this to `true` to enable Polaris PR comment feature. Comments are added to the pull request for new issues found. For example, `polaris_prComment_enabled: true`  **Default**: `false`  **Note:**   1. For pull request comment feature, SCM specific token is required. 2. Polaris Prcomment is supported for multibranch pipeline job. It is not supported for freestyle and pipeline job. | Optional |
| `polaris_prComment_severities` | The value should be a comma-separated list of severities. Comments are created for issues where the issue severity matches one of the values specified using this option.  Valid severities are: `Critical`, `High`, `Medium`, `Low`, and `Informational`.  **Default**: `High,Critical` | Optional |
| `polaris_fixpr_enabled` | Enables or disables the Polaris Fix PR workflow.  **Accepted values:** `true`, `false`  **Default:** `false` | Optional |
| `polaris_fixpr_filter_severities` | Creates Fix PRs only for issues with a severity matching a filter. The value is a comma-separated list.  **Values**: One or more of the following, separated by commas:   - `CRITICAL` - `HIGH` - `MEDIUM` - `LOW`   **Default**: `CRITICAL,HIGH` | Optional |
| `polaris_fixpr_maxCount` | Sets the maximum number of fix Pull Requests that can be created on a branch. Accepts integer values.  **Default:** `5` | Optional |
| `polaris_fixpr_useUpgradeGuidance` | Specifies whether to use only short term guidance, only long term guidance, or an ordered preference that allows both. Bridge tries the guidance values in the order provided.  **Values**:   - `SHORT_TERM` - `LONG_TERM` - `SHORT_TERM,LONG_TERM` - `LONG_TERM,SHORT_TERM`   **Default**:`SHORT_TERM,LONG_TERM` | Optional |
| `polaris_branch_parent_name` | Parent Branch name in the Polaris Server. Parent branch name is used by the PR comments feature. | Optional |
| `bitbucket_username` | Applies to Bitbucket cloud users. The username can be configured in Jenkins global configurations or can be passed as environment variable. Example: `"bitbucket_username: ${env.BITBUCKET_USERNAME}"` | Optional |
| `polaris_assessment_mode` (deprecated) | The test mode type of the Polaris scan. Supported values: `SOURCE_UPLOAD`, `CI`   **Default:** `CI`  Note: `polaris_assessment_mode` is deprecated. Use `polaris_test_sast_location`='remote' and/or `polaris_test_sca_location`='remote' for source upload scans instead. **BREAKING CHANGE**: If using an existing freestyle pipeline with `Assessment Mode (Optional)=SOURCE_UPLOAD` then please edit the pipeline to set the value in `SAST Test Location = remote` / `SCA Test Location = remote`. Ensure that values are also re-entered for dependent parameters, such as: `Upload Archive Instead Of Directory (Optional)`, `Project Source Excludes (Optional)` and `Project Source Preserve SymLinks (Optional)`. | Optional |
| `project_source_preserveSymLinks` | Bridge will save the copy of the target file to the zip archive. If the symlink is a directory, Bridge will copy the files in the target directory recursively to the zip archive.  When `project_source_preserveSymLinks` is set as true, Bridge will preserve the links to the zip file.  **Note:** If `project_source_preserveSymLinks` is set as true and there are symlinks to locations outside of the project (or absolute path links) this will cause issues when uploading to Polaris since the analysis environment won’t have those files or directories needed to satisfy the symlink.  **Default:** false. | Optional |
| `polaris_test_sast_location` | Configure location of source code capture and SAST analysis. Supported values are `hybrid`, `local` and `remote`.    **Default:** `hybrid`    In `hybrid` mode Bridge downloads tools for local capture and uploads artifacts (idir) for analysis on Polaris.    In `local` mode Bridge downloads tools for local capture and performs a full analysis in the local CI/CD environment, with results uploaded to Polaris.    In `remote` mode Bridge zips source code and uploads to Polaris for full capture and analysis. | Optional |
| `polaris_test_sca_location` | Configure location of source code capture and SCA analysis. Supported values are `hybrid` and `remote`.    **Default:** `hybrid`    In `hybrid` mode Bridge downloads tools for local capture and uploads artifacts (BDIO) for analysis on Polaris.    In `remote` mode Bridge zips source code and uploads to Polaris for full capture and analysis. | Optional |
| `project_directory` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `project_source_archive` | The zipped source file path. It overrides the project directory. | Optional |
| `project_source_excludes` | A list of git ignore pattern strings that indicate the files need to be excluded from the zip file. | Optional |
| `polaris_test_sast_type` | Polaris test type to trigger sigma rapid scan or full scan. Supported values: `SAST_RAPID` or `SAST_FULL`.  **Default value**: `SAST_FULL`.  Note: Sigma rapid scan is not supported in source upload test mode. | Optional |
| `polaris_test_sca_type` | Polaris test type to trigger signature scan, package manager scan or binary scan. **Default**: `SCA-PACKAGE` **Supported values**:  - SCA-BINARY - `SCA-PACKAGE` - `SCA-SIGNATURE` - SCA-PACKAGE, SCA-SIGNATURE   Note: `SCA-BINARY` can only be used stand-alone. It cannot be combined with `SCA-PACKAGE` or `SCA-SIGNATURE`. | Optional |
| `polaris_artifactToUpload` | Path to a binary or archive file to analyze. This is required when using `SCA-BINARY` as the SCA Test Type. | Optional. Required when `SCA-BINARY` set in `polaris_test_sca_type`. |
| `polaris_waitForScan` | Specifies if the workflow should wait for the analysis to complete.  **Default** : `true`  If set to false, post scan workflows like PR comment, Fix PR, SARIF etc will not be applicable. | Optional |

## Coverity client scan tool parameters

| **Scan Tool** | **Input Parameter** | **Description** |
| --- | --- | --- |
| Coverity | `coverity_build_command` | Build command to be passed to Coverity. |
| `coverity_clean_command` | Clean command to be passed to Coverity. |
| `coverity_config_path` | Path to Coverity.yml file to be passed to Coverity. |
| `coverity_args` | Pass generic arguments to Coverity CLI. |
| `coverity_version` | Select the Coverity version to use for SAST local and SAST hybrid scans (full and rapid) Important: SAST remote scans use default version from Polaris Web UI.  **Default**: Bridge uses the version configured on Polaris Web UI for the application, project or branch being scanned. **Acceptable Values**: Versions of Coverity that are supported on Polaris (including deprecated versions). **Example**: `2025.6.2` |
| Detect | `detect_search_depth` | Search Depth to be passed to Black Duck-Detect. |
| `detect_args` | Pass any argument to Detect. |
| `detect_config_path` | Path to configuration file - to be passed to Detect. |
