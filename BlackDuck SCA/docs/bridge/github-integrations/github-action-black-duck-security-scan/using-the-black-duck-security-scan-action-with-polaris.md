---
title: "Using the Black Duck Security Scan Action with Polaris"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-action-with-polaris.html"
content_id: "d3p4Yewl9PEUoAJn9oR~Sw"
version: "latest"
section: "GitHub Integrations"
scraped_at: "2026-08-08T23:47:43.958136+00:00"
---

# Using the Black Duck Security Scan Action with Polaris

As a GitHub Actions with Polaris customer, you can use the Black Duck Security Scan Action to automate scanning in your CI pipeline. Visit our [Academy Micro-Course](https://blackduck.skilljar.com/polaris-using-the-black-duck-security-scan-action-for-github?utm_source=docsportal&utm_medium=banner&utm_campaign=pol_academypromo) to quickly get started.

You can use Black Duck Security Scan Action with Polaris in the following ways:

- Adding Pull Request comments to GitHub
- Raise Fix Pull Requests for SAST and SCA vulnerabilities
- Exporting a SARIF file
- Uploading Polaris issues to GitHub Advanced Security
- Upload a binary file or archive to Polaris for analysis
- Upload a container image archive to Polaris for analysis

The Black Duck Security Scan Action provides parameters to configure client scan tools.

Before running a pipeline using the Black Duck Security Scan Action with Polaris, you must set the appropriate applications and entitlements in your Polaris environment. Project is created as necessary. If you don't want the project to be created, set `polaris.onboarding` to `false`.

Using GitHub Action, you can perform scans on push events to main branches. Client scan tools can be configured using the parameters provided by the GitHub Action.

When adding pull request comments, you must have a baseline scan on your main branch. When another branch is merged with your main, a scan will be triggered. While pull request comments are turned on, they will be triggered by the scan if the branch introduces a new vulnerability.

For an overview about using PR Comments, please see the following documentation page: Pull request (PR) comments.

For an overview about using Fix PRs, please see the following documentation page: Fix pull requests (Fix PRs).

Add the following code block to your existing `workflow.yml` file in your `.github/workflows` directory. (If you need to create a workflow, go to the repository you're integrating with Polaris on the GitHub UI, click the **Actions** tab at the top, then click **New Workflow**.)

Below is a simplified example of a `workflow.yml` file configured for Polaris.

```
name: CI-Polaris-Basic
on:
  push:
    branches: [main, master, develop, stage, release]
  pull_request:
    branches: [main, master, develop, stage, release]
  workflow_dispatch:

jobs:
  build:
    runs-on: [ubuntu-latest]
    steps:
    - name: Checkout Source
      uses: actions/checkout@v5
    - name: Polaris Scan
      id: polaris-scan
      uses: blackduck-inc/black-duck-security-scan@v2
      with:
        ### SCANNING: Required fields
        polaris_server_url: ${{ vars.POLARIS_SERVER_URL }}
        polaris_access_token: ${{ secrets.POLARIS_ACCESS_TOKEN }}
        polaris_assessment_types: "SCA,SAST"

        ### Binary scan: requires polaris_assessment_types set to SCA only
        # polaris_test_sca_type: "SCA-BINARY"
        # polaris_artifactToUpload: "/path/to/binary-file"

        ### SCA container scan: requires polaris_assessment_types set to SCA only
        # polaris_test_sca_type: 'SCA-CONTAINER'
        # polaris_artifactToUpload: '/path/to/container.tar.gz'
        # polaris_container_name: 'unique-container-name' # use for filtering

        ### SCANNING: Optional fields
        # polaris_application_name: ${{ github.event.repository.name }}
        # polaris_project_name: ${{ github.event.repository.name }}

        ### PULL REQUEST COMMENTS: Uncomment below to enable
        # polaris_prComment_enabled: true 
        # github_token: ${{ secrets.GITHUB_TOKEN }} # Mandatory when PR comments is enabled

        ### FIX PR: Uncomment below to enable
        # polaris_fixpr_enabled: true
        # github_token: ${{ secrets.GITHUB_TOKEN }} # Mandatory when polaris_fixpr_enabled is set to 'true'

        ### Github Issues
        # polaris_externalIssues_create: true
        # github_token: ${{ secrets.GITHUB_TOKEN }} # Mandatory when polaris_externalIssues_create is set to 'true'

        ### SARIF report parameters
        # polaris_reports_sarif_create: true
        # polaris_upload_sarif_report: true

        ### Signature scan
        # polaris_test_sca_type: "SCA-SIGNATURE"

        ### Mark build status if policy violating issues are found
        # mark_build_status: 'success'

        ### Uncomment below configuration to add custom logic based on return status
        # - name: cmdLine
        #   id: cmdLine
        #   run: |
        #     EXIT_CODE=${{ steps.polaris-scan.outputs.status }}
        #     echo "Polaris Scan exit status - $EXIT_CODE"
```

What follows is a more detailed example of a `workflow.yml` file configured for Polaris for more advanced users.

```
name: CI-Polaris
on:
  push:
    branches: [main, master, develop, stage, release]
  pull_request:
    branches: [main, master, develop, stage, release]
jobs:
  polaris-scan:
    runs-on: [ubuntu-latest]
    steps:
    - name: Checkout Source
      uses: actions/checkout@v5
    - name: Polaris Full Scan
      id: polaris-full-scan
      if: ${{ github.event_name != 'pull_request' }}
      uses: blackduck-inc/black-duck-security-scan@v2
      with:
        polaris_server_url: ${{ vars.POLARIS_SERVER_URL }}
        polaris_access_token: ${{ secrets.POLARIS_ACCESS_TOKEN }}
        polaris_application_name: ${{ github.event.repository.name }}
        polaris_project_name: ${{ github.event.repository.name }}
        polaris_assessment_types: "SCA,SAST"
        # polaris_waitForScan: false  # Used to support the async mode
        # project_directory: ${{ vars.PROJECT_DIRECTORY }}

        ### Github Issues
        # polaris_externalIssues_create: true
        # polaris_externalIssues_types: "SCA,SAST"
        # polaris_externalIssues_severities: "critical,high,medium"
        # polaris_externalIssues_groupSCAIssues: true
        # polaris_externalIssues_maxCount: 10
        # github_token: ${{ secrets.GITHUB_TOKEN }} # Mandatory when polaris_externalIssues_create is set to 'true'

        ### FIX PR
        # Creates Fix PRs for the assessment types configured in polaris_assessment_types (SAST, SCA, or both).
        # polaris_fixpr_enabled: true
        # Shared limit across SAST and SCA Fix PRs.
        # polaris_fixpr_maxCount: 10
        # Applies to SCA Fix PRs only.
        # polaris_fixpr_useUpgradeGuidance: "SHORT_TERM,LONG_TERM"
        # SAST and/or SCA Fix PR severity filter.
        # polaris_fixpr_filter_severities: "critical,high,medium"
        # GitHub token is mandatory when polaris_fixpr_enabled is 'true'.
        # github_token: ${{ secrets.GITHUB_TOKEN }}

        ### Uncomment below configuration if Bridge diagnostic files needs to be uploaded
        # include_diagnostics: true

        ### SARIF report generation and upload to GitHub Adavanced Security Tab: Uncomment below to enable
        # polaris_reports_sarif_create: true  
        # polaris_reports_sarif_file_path: '/Users/tmp/report.sarif.json' # File path (including file name) where SARIF report is created.
        # polaris_reports_sarif_severities: 'CRITICAL,HIGH'
        # polaris_reports_sarif_groupSCAIssues: true 
        # polaris_reports_sarif_issue_types: 'SCA, SAST' 
        # polaris_upload_sarif_report: true 
        # github_token: ${{ secrets.GITHUB_TOKEN }} # Required when polaris_upload_sarif_report is set as true

        ### Mark build status if policy violating issues are found
        # mark_build_status: 'success'

        ### Signature scan
        # polaris_test_sca_type: 'SCA-SIGNATURE'

        ### Binary scan: requires polaris_assessment_types set to SCA only
        # polaris_test_sca_type: "SCA-BINARY"
        # polaris_artifactToUpload: "/path/to/binary-file"

        ### SCA container scan: requires polaris_assessment_types set to SCA only 
        # polaris_test_sca_type: 'SCA-CONTAINER'
        # polaris_artifactToUpload: '/path/to/container.tar.gz'
        # polaris_container_name: 'unique-container-name' # use for filtering

        ### Uncomment this to use Source Upload method. Default value is hybrid (build based)
        # polaris_test_sast_location: 'remote'
        # polaris_test_sca_location: 'remote'
        # project_source_archive: ${{ vars.PROJECT_SOURCE_ARCHIVE }}
        # project_source_excludes: ${{ vars.PROJECT_SOURCE_EXCLUDES }} # Accepts Multiple Values
        # project_source_preserveSymLinks: true

        #### Uncomment this to use Local Analysis feature
        # Please use Local Analysis or Source Upload exclusively
        # polaris_test_sast_location: 'local'

        ### Uncomment below to add arbitrary CL parameters
        # detect_search_depth: 2
        # detect_args: '--detect.diagnostic=true'
        # detect_config_path: '/Users/Config/application.properties'
        # coverity_build_command: mvn clean install
        # coverity_clean_command: mvn clean
        # coverity_config_path: /Users/Config/coverity.yml
        # coverity_args: --config-override capture.build.build-command=mvn install
        # coverity_version: '2025.6.2'

    - name: Polaris PR Scan
      id: polaris-pr-scan
      if: ${{ github.event_name == 'pull_request' }}
      uses: blackduck-inc/black-duck-security-scan@v2
      with:
        polaris_server_url: ${{ vars.POLARIS_SERVER_URL }}
        polaris_access_token: ${{ secrets.POLARIS_ACCESS_TOKEN }}
        polaris_application_name: ${{ github.event.repository.name }}
        polaris_project_name: ${{ github.event.repository.name }}
        polaris_assessment_types: "SCA,SAST"
        # project_directory: ${{ vars.PROJECT_DIRECTORY }}

        ### Uncomment this to use Source Upload method. Default value is hybrid (build based)
        # polaris_test_sast_location: 'remote'
        # polaris_test_sca_location: 'remote'
        # project_source_archive: ${{ vars.PROJECT_SOURCE_ARCHIVE }}
        # project_source_excludes: ${{ vars.PROJECT_SOURCE_EXCLUDES }} # Accepts Multiple Values
        # project_source_preserveSymLinks: true

        #### Uncomment this to use Local Analysis feature
        # Please use Local Analysis or Source Upload exclusively
        # polaris_test_sast_location: 'local'

        ### Below configuration is used to enable feedback from Polaris security testing as pull request comment
        polaris_prComment_enabled: true
        github_token: ${{ secrets.GITHUB_TOKEN }}
        # Mandatory when polaris_prComment_enabled is set to 'true'

        ### Mark build status if policy violating issues are found
        # mark_build_status: 'success'

        ### Uncomment below configuration if Bridge diagnostic files needs to be uploaded
        # include_diagnostics: true

        ### Uncomment below configuration to add custom logic based on return status
        # - name: cmdLine
        #   id: cmdLine
        #   run: |
        #     EXIT_CODE=${{ steps.polaris-full-scan.outputs.status }}
        #     echo "Polarity Full Scan exit status - $EXIT_CODE"
```

Note: SARIF report creation is only supported for non MR/PR scans.

Table 1. List of mandatory and optional parameters for Polaris

| **Input Parameter** | Description | **Mandatory / Optional** |
| --- | --- | --- |
| `github_token` | GitHub Access Token.  **Example**: `github_token: ${ secrets.GITHUB_TOKEN }` | Mandatory when `polaris_prComment_enabled,` `polaris_fixpr_enabled`, or `polaris_externalIssues_create` is set to `true`. |
| `polaris_access_token` | Polaris Access token. You can use either an access token created in the Polaris UI or a service account token. | Mandatory |
| `polaris_application_name` | Polaris Application name. Default value is GitHub repository name. | Optional |
| `polaris_assessment_types` | Polaris assessment types  Accepted values:   - `DAST` - `SAST` - `SCA` - `SAST,SCA`   For DAST configuration requirements, see Using Bridge CLI With Polaris. | Mandatory |
| `polaris_branch_name` | Branch name in the Polaris Server. Branch is created if it doesn't exist in Polaris.  Note: GitHub users: If this option is not specified, `github.branch.name` is used for branch name. | Optional |
| `polaris_branch_parent_name` | Parent Branch name in the Polaris Server. Parent branch name is used by the PR comments feature.  Note: GitHub users: If this option is not specified `github.branch.parent.name` is used for parent branch name. | Optional |
| `polaris_externalIssues_create` | Enable creation of Polaris external GitHub issues.  Flag to enable/disable external GitHub issues creation from scan findings. When `false`, no external issues are created.  **Default:**`false` | Optional |
| `polaris_externalIssues_types` | List of Polaris issue types for which GitHub issues should be created. Accepted values: `SAST`, `SCA` (case‑insensitive). | Optional |
| `polaris_externalIssues_severities` | List of Polaris severities for which GitHub issues should be created. List of severities `["Critical", "High" "Medium", "Low"]`.  **Default:**`["Critical", "High"]` | Optional |
| `polaris_externalIssues_groupSCAIssues` | Flag to denote whether to group SCA issues by vulnerabilities of a component‑version pair while creating external issues.  **Default:**`true` | Optional |
| `polaris_externalIssues_maxCount` | Maximum number of external issues to create at any given time per assessment/workflow. Default limits SAST/SCA issues to 10 when not specified.  **Default:**`10` | Optional |
| `polaris_project_name` | Polaris Project name. Default value is the name of the repository, which includes repository name. | Optional |
| `polaris_server_url` | Polaris URL. | Mandatory |
| `polaris_prComment_enabled` | Set this to `true` to enable Polaris PR comment feature. Comments are added to the pull request for new issues found.  **Default**: `false` | Optional |
| `polaris_prComment_severities` | The value should be a comma-separated list of severities. Comments are created for issues where the issue severity matches one of the values specified using this option.  Valid severities are: `Critical`, `High`, `Medium`, `Low`, and `Informational`.  **Default**: `high,critical` | Optional |
| `polaris_fixpr_enabled` | Enable automatic Fix Pull Request creation for eligible SAST and/or SCA issues. Creates Pull Requests containing dependency upgrades for SCA issues and/or AI-generated code fixes for SAST vulnerabilities, based on the configured assessment types.  **Default**: `false` | Optional |
| `polaris_fixpr_maxCount` | Maximum number of Fix Pull Requests to create per scan/workflow run. This limits the number of Pull Requests generated to avoid overwhelming the repository with too many automated Pull Requests at once. By default, a maximum count of five Fix PRs can be raised across both SAST and SCA scans, with SAST evaluated first. Dismissed issues are excluded, then the `polaris_fixpr_filter_severities` allow list is applied. Only the first `polaris_fixpr_maxCount` results are selected.  **Default**: `5` | Optional |
| `polaris_fixpr_useUpgradeGuidance` | For SCA Fix PRs, allows the user to specify short-term or long-term upgrade guidance, or both.  If both values are provided, the first takes priority and the second value is used only if the first returns no results.  If upgrade guidance is not available, the Fix Pull Request is not created.  **Accepted values:**   - `SHORT_TERM` - `LONG_TERM` - `SHORT_TERM, LONG_TERM` - `LONG_TERM, SHORT_TERM`   **Default**: `SHORT_TERM,LONG_TERM` | Optional |
| `polaris_fixpr_filter_severities` | Creates Fix PRs only for issues with a severity matching a filter. The value is a comma-separated list. If both SAST and SCA assessments types are enabled, the specified severities are applied to issues from both assessment types.  **Accepted values**: One or more of the following (comma-separated, case-insensitive):   - `CRITICAL` - `HIGH` - `MEDIUM` - `LOW`   **Default**: `CRITICAL,HIGH` | Optional |
| `polaris_reports_sarif_create` | Set this to `true` to generate SARIF report.  **Default**: `false`  Note: SARIF reports can be generated for any configured branch; however, report generation is not supported in a PR/MR context. | Optional |
| `polaris_reports_sarif_file_path` | File path (including file name) where SARIF report is created.  When the Bridge version is lower than 3.5.0, the default SARIF file path will be:  `.bridge/Polaris SARIF Generator/report.sarif.json`  If the Bridge version is greater than 3.5.0, the default SARIF file path will be: `.blackduck/integrations/polaris/sarif/report.sarif.json` | Optional |
| `polaris_reports_sarif_severities` | Comma-separated list of SAST/SCA issue severities to include in SARIF file report. Valid severities are `Critical`, `High`, `Medium`, `Low`, and `Informational`.  **Default**: All severities are included. | Optional |
| `polaris_reports_sarif_groupSCAIssues` | When set to true, SCA issues are grouped by component. Set this to false to list SCA issues by vulnerability.  **Default**: `true` | Optional |
| `polaris_reports_sarif_issue_types` | Lists which assessment issues types to include in SARIF file report | Optional |
| `polaris_upload_sarif_report` | Set this to `true` to upload Polaris SARIF issues to GitHub Advanced Security | Optional |
| `polaris_assessment_mode` | The test mode type of the Polaris scan. Supported values: `SOURCE_UPLOAD`, `CI`. Warning: This parameter is deprecated. Use `polaris_test_sast_location=remote` and/or `polaris_test_sca_location=remote` for source upload scans instead.  **Default:**`CI` | Optional |
| `polaris_test_sast_location` | Configure the location of source code capture and SAST analysis. Supported values are `hybrid`, `local` and `remote`.  **Default**:`hybrid`  In `hybrid` mode Bridge downloads tools for local capture and uploads artifacts (idir) for analysis on Polaris.  In `local` mode Bridge downloads tools for local capture and performs a full analysis in the local CI/CD environment, with results uploaded to Polaris.  In `remote` mode Bridge zips source code and uploads to Polaris for full capture and analysis. Note: When Fix PRs are enabled and `polaris_assessment_types` includes SAST then valid values are `hybrid` or `remote`. If `local` is specified, Fix PRs will be skipped and a warning will be logged. | Optional. Required for Source Code Upload for SAST assessment type. |
| `polaris_test_sca_location` | Configure location of source code capture and SCA analysis. Supported values are `hybrid` and `remote`.  **Default**:`hybrid`  In `hybrid` mode Bridge downloads tools for local capture and uploads artifacts (BDIO) for analysis on Polaris.  In `remote` mode Bridge zips source code and uploads to Polaris for full capture and analysis. | Optional. Required for Source Code Upload for SAST assessment type. |
| `project_directory` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `project_source_archive` | The zipped source file path. It overrides the project directory. | Optional |
| `project_source_excludes` | A list of git ignores pattern strings that indicate the files need to be excluded from the zip file. | Optional |
| `project_source_preservesymlinks` | Flag indicating whether to preserve symlinks in the source zip. **Default:**`false` | Optional |
| `polaris_test_sca_type` | Polaris test type to trigger signature scan, package manager scan, container scan or binary scan. **Default value**: `SCA-PACKAGE` **Supported values**:  - `SCA-BINARY` - `SCA-CONTAINER` - `SCA-PACKAGE` - `SCA-SIGNATURE` - SCA-PACKAGE, SCA-SIGNATURE   Note: `SCA-BINARY` and `SCA-CONTAINER` can only be used stand-alone. Those parameter values cannot be combined with `SCA-PACKAGE` or `SCA-SIGNATURE` in the same run. Attempting to mix scan types results in a validation error. | Optional |
| `polaris_artifactToUpload` | Path to an artifact file to be uploaded for analysis. Use this parameter when `polaris_test_sca_type` is set to `SCA-BINARY` or `SCA-CONTAINER`.  - For `SCA-BINARY`, specify the path to the binary or archive file to analyze. - For `SCA-CONTAINER`, specify the path to a valid container image archive (`tar`, `zip`, `gz`, or `tgz`). The archive must contain a container image, such as one created using `docker save`.   Note: The file must be accessible from the execution environment. If the parameter is not specified, the scan fails validation.  **Default:**None | Optional. Required when `polaris_test_sca_type` is set to `SCA-BINARY` or `SCA-CONTAINER`. |
| `polaris_container_name` | A name to associate with the container image. The container name will be listed in the containers section of the project in the Polaris web UI and can also be used as a filter. | Optional. Required when `polaris_test_sca_type` is set to `SCA-CONTAINER`. |
| `polaris_test_sast_type` | Polaris test type to trigger sigma rapid scan or full scan. Supported values: `SAST_FULL` or `SAST_RAPID`.  **Default:**`SAST_FULL` | Optional |
| `polaris_waitForScan` | Specifies whether the workflow should wait for the analysis to complete or not. Supported values: `true` or `false`  **Default**: `true`  If set to false, post scan workflows like PR comment, Fix PR, SARIF etc will not be applicable. | Optional |

Table 2. List of optional parameters for Polaris client scan tools

| **Scan Tool** | **Input Parameter** | **Description** |
| --- | --- | --- |
| Coverity | `coverity_build_command` | Build command for the project to be passed to Coverity. |
| `coverity_clean_command` | Clean command for the project to be passed to Coverity. |
| `coverity_config_path` | Path to Coverity.yml file to be passed to Coverity. |
| `coverity_args` | Pass generic arguments to Coverity CLI. |
| `coverity_version` | Select the Coverity version to use for SAST local and SAST hybrid scans (full and rapid) Important: SAST remote scans use default version from Polaris Web UI.  **Default**: Bridge uses the latest version configured on Polaris Web UI for the application, project or branch being scanned. **Acceptable Values**: Versions of Coverity that are supported on Polaris (including deprecated versions). **Example**: `2025.6.2` |
| Detect | `detect_search_depth` | Search Depth to be passed to Black Duck-Detect. |
| `detect_args` | Pass any argument to Detect. |
| `detect_config_path` | Path to configuration file - to be passed to Detect. |

## Uploading security scan issues to GitHub Advanced Security

To upload the security scan results in GitHub Advanced Security tab, you need to have the following options enabled as shown in the examples above:

1. Create SARIF file (Option: `polaris_reports_sarif_create`)
2. Upload SARIF file (Option: `polaris_upload_sarif_report`)

GitHub Enterprise (GHE) server users can upload SARIF reports as well. This feature has been verified on Enterprise Server version 3.15. Prior to uploading SARIFs to the GitHub Advanced Security dashboard on your GHE server, ensure that these prerequisites are met:

- **GitHub Advanced Security** must be enabled for the repository.
- **Code Scanning** should be activated.
- The **GitHub Actions workflow** must have `security-events: write` permission.

Important: People with admin permissions to a repository, or the security manager role for the repository, can configure code scanning for that repository. People with write permissions to a repository can also configure code scanning, but only by creating a workflow file or manually uploading a SARIF file.

Code scanning is available for all public repositories on [GitHub](http://github.com/). Code scanning is also available for private repositories owned by organizations that use GitHub Enterprise Cloud or GitHub Enterprise Server. This feature requires a license for GitHub Advanced Security. For more information, see "[About GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)."
