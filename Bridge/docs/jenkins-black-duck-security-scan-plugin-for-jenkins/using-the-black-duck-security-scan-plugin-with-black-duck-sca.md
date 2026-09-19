---
title: "Using the Black Duck Security Scan Plugin with Black Duck SCA"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-plugin-with-black-duck-sca.html"
content_id: "Q05y_NWq64XNbDVYDabodA"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:40.591401+00:00"
---

# Using the Black Duck Security Scan Plugin with Black Duck SCA

The Black Duck Security Scan Plugin can be used with Jenkins Multibranch, Pipeline and Freeestyle projects.

## Choose pipeline for use with Black Duck SCA

Use the decision table below to choose a suitable type of Jenkins pipeline and view examples for Black Duck® SCA.

| Pipeline type | Use When... | Example |
| --- | --- | --- |
| **Multibranch Pipeline** | - Declarative or Scripted Jenkinsfile pipelines preferred. - Enterprise applications requiring full feature set. - PR Comments and Fix PRs are required. | Multibranch Pipeline |
| **Pipeline** | - Declarative or Scripted Jenkinsfile pipelines preferred. - Push/merge scans only needed for protected branches. - PR Comments and Fix PRs not required. | Pipeline |
| **Freestyle** | Simplest method:   - UI based scan configuration. - Push/merge scans only needed for protected branches. - PR Comments and Fix PRs not required. | Freestyle |

Note: By default, Black Duck® SCA server URL and access token parameters configured in the Black Duck Security Scan Plugin are used by all Multibranch Pipeline, Pipeline and Freestyle projects. For Multibranch Pipeline and Pipeline projects, these parameters can be overridden in the Jenkinsfile using the `blackducksca_url` and `blackducksca_token` parameters. For Jenkins freestyle projects these parameters **cannot** be overridden.

## Black Duck SCA parameters

| Input parameter | Description | Mandatory / optional |
| --- | --- | --- |
| `bitbucket_token` | Applies to Bitbucket users. The token can be configured in Jenkins global configurations or can be passed as environment variable. This is required if `prcomment` is set to true. Example: `bitbucket_token: "${env.BITBUCKET_TOKEN}"` | Optional |
| `github_token` | Applies to GitHub users. The token can be configured in Jenkins global configurations or can be passed as environment variable. Example, `github_token: "${env.GITHUB_TOKEN}"`. | Optional |
| `gitlab_token` | Applies to GitLab users. The token can be configured in Jenkins global configurations or can be passed as environment variable. Example, `gitlab_token: "${env.GITLAB_TOKEN}"`. | Optional |
| `blackducksca_prComment_enabled` | Flag to enable an automatic pull request comment based on the Black Duck® SCA scan result. Supported values are `true` and `false` (default). For example, `blackducksca_prComment_enabled: true`. Note:  - For pull request comment feature, SCM specific token is required. - Black Duck® SCA Prcomment is supported for multibranch pipeline job. It is not supported for freestyle and pipeline job | Optional |
| `detect_download_url` | When a Detect Download URL is provided by the user, Bridge will download detect from the provided URL. | Optional |
| `detect_install_directory` | The directory path used to install Black Duck® SCA. | Optional |
| `blackducksca_scan_failure_severities` | Scan failure severities of Black Duck® SCA. Supported values are as follows:  - `ALL` - `NONE` - `BLOCKER` - `CRITICAL` - `MAJOR` - `MINOR` - `OK` - `TRIVIAL` - `UNSPECIFIED`  For example, `blackducksca_scan_failure_severities: "BLOCKER, TRIVIAL"`. | Optional |
| `blackducksca_scan_full` | Specifies whether full scan is required or not. By default, pushes will initiate a full "intelligent" scan, and pull requests will initiate a rapid scan. Supported values: `true` or `false` (default) | Optional |
| `blackducksca_token` | The API token for Black Duck® SCA. The token can also be configured in Jenkins **Global Configuration** or passed as an **Environment Variable**. For example, `blackducksca_token: "${env.BLACKDUCKSCA_TOKEN}"` | Mandatory (unless configured in Jenkins Global Configuration) |
| `blackducksca_url` | The URL for the Black Duck® SCA server. The URL can also be configured in Jenkins **Global Configuration** or passed as an **Environment Variable**. For example, `blackducksca_url: "${env.BLACKDUCKSCA_URL}"`. | Mandatory (unless configured in Jenkins Global Configuration) |
| `product` | Name of the Black Duck® SCA security product. Example: `product: "BLACKDUCKSCA"` | Mandatory |
| `blackducksca_reports_sarif_create` | Set this to `true` to generate SARIF report.  **Default**: `false`  Note: SARIF reports can be generated for any configured branch; however, report generation is not supported in a PR/MR context. | Optional |
| `blackducksca_reports_sarif_file_path` | File path (including file name) where SARIF report is created.  **Default**: `.blackduck/integrations/blackducksca/sarif/report.sarif.json` | Optional |
| `blackducksca_reports_sarif_severities` | Comma-separated list of SAST/SCA issue severities to include in SARIF file report. Valid severities are `Critical`, `High`, `Medium`, `Low`, and `Informational`.  **Default**: All severities are included. | Optional |
| `blackducksca_reports_sarif_groupSCAIssues` | When set to true, SCA issues are grouped by component. Set this to false to list SCA issues by vulnerability.  **Default**: `true` | Optional |
| `project_directory` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `detect_search_depth` | Number indicating the search depth in the source directory. | Optional |
| `detect_config_path` | Black Duck config file path location. | Optional |
| `detect_args` | Additional arguments for Black Duck. | Optional |
| `blackducksca_waitForScan` | Specifies if the workflow should wait for the analysis to complete.  **Default** : `true`  If set to false, post scan workflows like PR comment, Fix PR, SARIF etc will not be applicable. | Optional |
| `blackducksca_fixpr_enabled` | Enables or disables Fix PR creation for Black Duck SCA. When set to true, a fix PR is created for each vulnerable direct dependency. **Accepted values:** `true`, `false`  **Default:** `false` | Optional |
| `blackducksca_fixpr_filter_severities` | Creates Fix PRs only for issues with the severity level specified. The value is a comma-separated list. Supported severities: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW` | Optional |
| `blackducksca_fixpr_maxCount` | Sets the maximum number of fix pull requests that can be created on a branch. Accepts integer values. | Optional |
| `blackducksca_fixpr_useUpgradeGuidance` | Allows the user to specify short-term or long-term upgrade guidance, or both. If both values are provided, the first takes priority, and the second value is used only if the first returns no results. If upgrade guidance is not available, the fix PR is not created. **Accepted values:**  - `SHORT_TERM` - `LONG_TERM` - `SHORT_TERM, LONG_TERM` - `LONG_TERM, SHORT_TERM`  **Default:** `SHORT_TERM, LONG_TERM` | Optional |

### Networking parameters

The table below describes optional networking parameters for Black Duck® SCA.

| **Input parameter** | Description |
| --- | --- |
| `network_ssl_trustAll` | Disables SSL certificate verification. Use with caution.  Example: `network_ssl_trustAll: true` |
