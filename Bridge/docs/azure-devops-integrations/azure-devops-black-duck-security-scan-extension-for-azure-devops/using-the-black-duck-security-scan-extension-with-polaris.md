---
title: "Using the Black Duck Security Scan Extension with Polaris"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-extension-with-polaris.html"
content_id: "vHXxGhhAyXCi9TyA84do~w"
version: "latest"
section: "Azure DevOps Integrations"
scraped_at: "2026-08-08T23:48:22.730543+00:00"
---

# Using the Black Duck Security Scan Extension with Polaris

Before running a pipeline using the Black Duck Security Scan Extension with Polaris, you must set the appropriate applications and entitlements in your Polaris environment. Project is created as necessary. If you don't want the project to be created, set `polaris.onboarding` to `false`.

Using Black Duck Security Scan Extension, you can perform scans on push events to main branches.

The Black Duck Security Scan Extension provides parameters to configure client scan tools.

For an overview about using PR Comments, please see the following documentation page: Pull request (PR) comments.

For an overview about using Fix Pull Requests, please see the following documentation page: Fix pull requests (Fix PRs).

To use Black Duck Security Scan Extension:

1. Configure sensitive data such as user names, passwords and URLs using pipeline variables.
2. Add `azure-pipelines.yml` to your project.
3. Push the changes and an agent will pick up the job and initiate the pipeline.

Here is a simplified example for `azure-pipelines.yml` that you can use with Polaris:

```
trigger:
  - main

pool:
  vmImage: ubuntu-latest

variables:
  - group: Polaris

steps:
- task: BlackDuckSecurityScan@2
  displayName: 'Polaris Scan'
  inputs:
    POLARIS_SERVER_URL: $(POLARIS_SERVER_URL)
    POLARIS_ACCESS_TOKEN: $(POLARIS_ACCESS_TOKEN)
    POLARIS_ASSESSMENT_TYPES: 'SCA,SAST'

    ### Uncomment for binary analysis of binary file or archive file
    ### Requires that POLARIS_ASSESSMENT_TYPES is set to SCA only
    # POLARIS_TEST_SCA_TYPE: 'SCA-BINARY'
    # POLARIS_ARTIFACTTOUPLOAD: '/path/to/source.zip'

    ### Uncomment for container analysis of container image archive file
    ### Requires that POLARIS_ASSESSMENT_TYPES is set to SCA only
    # POLARIS_TEST_SCA_TYPE: 'SCA-CONTAINER'
    # POLARIS_ARTIFACTTOUPLOAD: '/path/to/container.tar.gz'
    # POLARIS_CONTAINER_NAME: 'unique-container-name' # use for filtering

    ### Pull Request Comments
    # POLARIS_PRCOMMENT_ENABLED: true
    # AZURE_TOKEN: $(System.AccessToken)

    ### Polaris Fix Pull Requests 
    # POLARIS_FIXPR_ENABLED: 'true'
    # AZURE_TOKEN: $(System.AccessToken)

    ### SARIF report generation 
    # POLARIS_REPORTS_SARIF_CREATE: true

    ### Uncomment below configuration for signature scan
    # POLARIS_TEST_SCA_TYPE: 'SCA-SIGNATURE'

    ### Uncomment below configuration for sigma rapid scan
    # POLARIS_TEST_SAST_TYPE: 'SAST_RAPID'

    ### Uncomment below configuration to mark build status if policy violating issues are found
    # MARK_BUILD_STATUS: 'SucceededWithIssues'

    ### Uncomment below to use returned status in subsequent tasks if MARK_BUILD_STATUS is not set or set to FAILED
    # continueOnError: true

    ### Uncomment below configuration to add custom logic based on return status    
    # - task: CmdLine@2
    #   displayName: 'Command Line'
    #   condition: not(eq(variables['BlackDuckSecurityScan.status'], '0'))
    #   inputs:
    #     script: |
    #       echo Black Duck Security Scan exit status - $(BlackDuckSecurityScan.status)

    ### Uncomment below to upload to Advanced Security  
    # - task: AdvancedSecurity-Publish@1
    #   inputs:
    #     SarifsInputDirectory: '.bridge/Polaris SARIF Generator' # When the bridge version is lower than 3.5.0
    #     SarifsInputDirectory: '$(Build.SourcesDirectory)/.blackduck/integrations/polaris/sarif' # When the bridge version is greater than 3.5.0
```

Note: `continueOnError` is required to use returned status from Black Duck Security Scan in subsequent tasks if `MARK_BUILD_STATUS` is not set or set to FAILED.

Here is a detailed example for `azure-pipelines.yml` that you can use with Polaris:

```
trigger:
  - main

pool:
  vmImage: ubuntu-latest

variables:
  - group: polaris

steps:
- task: BlackDuckSecurityScan@2
  displayName: 'Polaris Scan'
  condition: not(eq(variables['Build.Reason'], 'PullRequest'))
  inputs:
    POLARIS_SERVER_URL: $(POLARIS_SERVER_URL)
    POLARIS_ACCESS_TOKEN: $(POLARIS_ACCESS_TOKEN)
    POLARIS_APPLICATION_NAME: $(Build.Repository.Name)
    POLARIS_PROJECT_NAME: $(Build.Repository.Name)
    POLARIS_ASSESSMENT_TYPES: 'SCA,SAST' # Accepts Multiple Values
    # POLARIS_WAITFORSCAN: false   # Used to support the async mode 
    # PROJECT_DIRECTORY: "$(PROJECT_DIRECTORY)"

    ### Uncomment below configuration to specify branch name in the Polaris Server
    # POLARIS_BRANCH_NAME: $(POLARIS_BRANCH)

    ### Automatically create Fix PRs
    # Creates Fix PRs for the assessment types configured in
    # POLARIS_ASSESSMENT_TYPES (SAST or SCA or SAST,SCA).
    # POLARIS_FIXPR_ENABLED: 'true'
    # Maximum number of Fix PRs across SAST and SCA combined.
    # POLARIS_FIXPR_MAXCOUNT: '5'
    # Upgrade guidance applies to SCA Fix PRs only.
    # POLARIS_FIXPR_USEUPGRADEGUIDANCE: 'SHORT_TERM,LONG_TERM'
    # Matching severities generate SAST and/or SCA Fix PRs,
    # depending on BRIDGE_POLARIS_ASSESSMENT_TYPES configuration.
    # POLARIS_FIXPR_FILTER_SEVERITIES: 'CRITICAL,HIGH'
    # AZURE_TOKEN: $(System.AccessToken) # Mandatory when POLARIS_FIXPR_ENABLED is set to 'true'

    ### Uncomment below configuration for signature scan
    # POLARIS_TEST_SCA_TYPE: 'SCA-SIGNATURE'

    ### Uncomment for binary analysis of binary file or archive file
    ### Requires that POLARIS_ASSESSMENT_TYPES is set to SCA only
    # POLARIS_TEST_SCA_TYPE: 'SCA-BINARY'
    # POLARIS_ARTIFACTTOUPLOAD: '/path/to/source.zip'

    ### Uncomment for container analysis of container image archive file
    ### Requires that POLARIS_ASSESSMENT_TYPES is set to SCA only
    # POLARIS_TEST_SCA_TYPE: 'SCA-CONTAINER'
    # POLARIS_ARTIFACTTOUPLOAD: '/path/to/container.tar.gz'
    # POLARIS_CONTAINER_NAME: 'unique-container-name' # use for filtering

    ### Uncomment this to use Source Upload method. Default value is hybrid (build based)
    # POLARIS_TEST_SAST_LOCATION: "remote"
    # POLARIS_TEST_SCA_LOCATION: "remote"
    # PROJECT_SOURCE_ARCHIVE: "$(PROJECT_SOURCE_ARCHIVE)"
    # PROJECT_SOURCE_EXCLUDES: "$(PROJECT_SOURCE_EXCLUDES)" # Accepts Multiple Values

    #### Uncomment this to use Local Analysis feature
    # Please use Local Analysis or Source Upload exclusively
    # POLARIS_TEST_SAST_LOCATION: 'local'

    ### Uncomment below configuration for sigma full scan
    # POLARIS_TEST_SAST_TYPE: 'SAST_FULL'

    ### Uncomment below configuration if Bridge diagnostic files needs to be uploaded
    # INCLUDE_DIAGNOSTICS: 'true'

    POLARIS_REPORTS_SARIF_CREATE: true # Create SARIF report and upload it as artifact
    POLARIS_REPORTS_SARIF_GROUPSCAISSUES: true # By default true
    POLARIS_REPORTS_SARIF_FILE_PATH: '$(Build.SourcesDirectory)/sarif/report.sarif.json' # Custom file path including file name where SARIF report should be created
    POLARIS_REPORTS_SARIF_SEVERITIES: 'CRITICAL,HIGH' # Accepts Multiple Values
    POLARIS_REPORTS_SARIF_ISSUE_TYPES: 'SAST,SCA' # Accepts Multiple Values

    ### Uncomment below configuration to mark build status if policy violating issues are found
    # MARK_BUILD_STATUS: 'SucceededWithIssues'

    ### Coverity (SAST) Tool Settings
    # COVERITY_CLEAN_COMMAND: 'mvn clean'
    # COVERITY_BUILD_COMMAND: 'mvn clean install'
    # COVERITY_ARGS: '--config-override capture.build.build-command=mvn install'
    # COVERITY_CONFIG_PATH: /Users/tmp/coverity.yml
    # COVERITY_VERSION: '2025.9.0'

    ### Detect Tool Settings
    # DETECT_SEARCH_DEPTH: 2
    # DETECT_ARGS: '--detect.diagnostic=true'
    # DETECT_CONFIG_PATH: '/Users/tmp/application.properties'

    ### Uncomment below to use returned status in subsequent tasks if MARK_BUILD_STATUS is not set or set to FAILED
    # continueOnError: true

- task: BlackDuckSecurityScan@2
  displayName: 'Polaris PR Scan'
  condition: eq(variables['Build.Reason'], 'PullRequest')
  inputs:
    POLARIS_SERVER_URL: $(POLARIS_SERVER_URL)
    POLARIS_ACCESS_TOKEN: $(POLARIS_ACCESS_TOKEN)
    POLARIS_APPLICATION_NAME: $(Build.Repository.Name)
    POLARIS_PROJECT_NAME: $(Build.Repository.Name)
    POLARIS_ASSESSMENT_TYPES: 'SCA,SAST'
    # PROJECT_DIRECTORY: "$(PROJECT_DIRECTORY)"

    ### Uncomment below configuration to specify branch name in the Polaris Server
    #POLARIS_BRANCH_NAME: $(POLARIS_BRANCH) # Branch name in the Polaris Server

    ### Below configuration is used to enable automatic pull request comment based on Polaris scan result
    POLARIS_PRCOMMENT_ENABLED: true
    AZURE_TOKEN: $(System.AccessToken) # Mandatory when POLARIS_PRCOMMENT_ENABLED is set to 'true'

    ### Uncomment below configuration for signature scan
    # POLARIS_TEST_SCA_TYPE: 'SCA-SIGNATURE'

    ### Uncomment this to use Source Upload method. Default value is hybrid (build based)
    # POLARIS_TEST_SAST_LOCATION: "remote"
    # POLARIS_TEST_SCA_LOCATION: "remote"
    # PROJECT_SOURCE_ARCHIVE: "$(PROJECT_SOURCE_ARCHIVE)"
    # PROJECT_SOURCE_EXCLUDES: "$(PROJECT_SOURCE_EXCLUDES)" # Accepts Multiple Values

    #### Uncomment this to use Local Analysis feature
    # Please use Local Analysis or Source Upload exclusively
    # POLARIS_TEST_SAST_LOCATION: 'local'

    ### Uncomment below configuration for sigma rapid scan
    # POLARIS_TEST_SAST_TYPE: 'SAST_RAPID'

    ### Uncomment below configuration if Bridge diagnostic files needs to be uploaded
    # INCLUDE_DIAGNOSTICS: 'true

    ### Uncomment below configuration to mark build status if policy violating issues are found
    # MARK_BUILD_STATUS: 'SucceededWithIssues'

    ### Coverity (SAST) Tool Settings
    # COVERITY_CLEAN_COMMAND: 'mvn clean'
    # COVERITY_BUILD_COMMAND: 'mvn clean install'
    # COVERITY_ARGS: '--config-override capture.build.build-command=mvn install'
    # COVERITY_CONFIG_PATH: /Users/tmp/coverity.yml
    # COVERITY_VERSION: '2025.9.0'

    ### DETECT Tool Settings
    # DETECT_SEARCH_DEPTH: 2
    # DETECT_ARGS: '--detect.diagnostic=true'
    # DETECT_CONFIG_PATH: '/Users/tmp/application.properties'

    ### Uncomment below to use returned status in subsequent tasks if MARK_BUILD_STATUS is not set or set to FAILED
    # continueOnError: true

    ### Uncomment below configuration to add custom logic based on return status    
    # - task: CmdLine@2
    #   displayName: 'Command Line'
    #   condition: not(eq(variables['BlackDuckSecurityScan.status'], '0'))
    #   inputs:
    #     script: |
    #       echo Black Duck Security Scan exit status - $(BlackDuckSecurityScan.status)

    ### Uncomment below to upload to Advanced Security  
    # - task: AdvancedSecurity-Publish@1
    #   inputs:
    #     SarifsInputDirectory: '$(Build.SourcesDirectory)/sarif'
```

Note: SARIF report creation is only supported for non MR/PR scans.

Note: `continueOnError` is required to use returned status from Black Duck Security Scan Extension in subsequent tasks if `MARK_BUILD_STATUS` is not set or set to FAILED.

**Here is an example using SARIF reports for Polaris:**

To upload SARIF files to Advanced Security using Black Duck Security Scan, you must configure the `AdvancedSecurity-Publish@1` task with the following input:

- `SarifsInputDirectory`: Use this field to specify the path to the directory containing the SARIF file to be published to Advanced Security. This is a mandatory field.
  - If `POLARIS_REPORTS_SARIF_CREATE` is set to `true`, and `POLARIS_REPORTS_SARIF_FILE_PATH` is not provided, `SarifsInputDirectory` will be the default directory for SARIF creation. You must input the directory path **excluding the file name**.

    For example: `.bridge/Polaris SARIF Generator/report.sarif.json` is the default file path for SARIF creation (when Bridge version is lower than 3.5.0), therefore you must input `.bridge/Polaris SARIF Generator` to `SarifsInputDirectory`.

    (When Bridge version is greater than 3.5.0, the default file path for SARIF creation is `.blackduck/integrations/polaris/sarif/report.sarif.json`.)
  - If `POLARIS_REPORTS_SARIF_CREATE` is set to `true`, and a custom path is provided to `POLARIS_REPORTS_SARIF_FILE_PATH`, then you must provide the same path **excluding the file name** to `SarifsInputDirectory`.

    For example: if `$(Build.SourcesDirectory)/sarif/report.sarif.json` is provided to `POLARIS_REPORTS_SARIF_FILE_PATH`, then you must provide `$(Build.SourcesDirectory)/sarif` to `SarifsInputDirectory`.
  - When using a custom path, if there are multiple SARIF files under the path used in `SarifsInputDirectory`, the Azure task `AdvancedSecurity-Publish@1` will combine all SARIF files and upload them to Advanced Security. Therefore, make sure to keep the relevant SARIF file under this path.
- `Category`: This is an optional field and should be left blank.

Note: For the `AdvancedSecurity-Publish@1` task, only `SarifsInputDirectory` is required. The other input fields are not required or may not be relevant.

Here is a complete example:

```
trigger:
  - main

pool:
  vmImage: ubuntu-latest

variables:
  - group: Polaris

steps:
  - task: BlackDuckSecurityScan@2
    displayName: 'Polaris Scan'
    inputs:
      POLARIS_SERVER_URL: $(POLARIS_SERVER_URL)
      POLARIS_ACCESS_TOKEN: $(POLARIS_ACCESS_TOKEN)
      POLARIS_ASSESSMENT_TYPES: 'SCA,SAST'

      # SARIF report generation
      POLARIS_REPORTS_SARIF_CREATE: true
      POLARIS_REPORTS_SARIF_GROUPSCAISSUES: true
      POLARIS_REPORTS_SARIF_FILE_PATH: '$(Build.SourcesDirectory)/sarif/report.sarif.json'
      POLARIS_REPORTS_SARIF_SEVERITIES: 'CRITICAL,HIGH'
      POLARIS_REPORTS_SARIF_ISSUE_TYPES: 'SAST,SCA'

  - task: AdvancedSecurity-Publish@1
    inputs:
      SarifsInputDirectory: '$(Build.SourcesDirectory)/sarif'
```

Table 1. List of mandatory and optional parameters for Polaris

| **Input parameter** | **Description** | **Mandatory / optional** |
| --- | --- | --- |
| `POLARIS_ACCESS_TOKEN` | Polaris access token. You can use either an access token created in the Polaris UI or a service account token. | Mandatory |
| `POLARIS_APPLICATION_NAME` | Polaris Application name. Default value is the name of the repository, which includes repository name. | Optional |
| `POLARIS_ASSESSMENT_TYPES` | Polaris assessment types  Accepted values:   - `DAST` - `SAST` - `SCA` - `SAST,SCA`   For DAST configuration requirements, see Using Bridge CLI With Polaris. | Mandatory |
| `POLARIS_PROJECT_NAME` | Polaris Project name. Default value is the name of the repository, which includes repository name. | Optional |
| `POLARIS_SERVER_URL` | Polaris URL. | Mandatory |
| `POLARIS_BRANCH_NAME` | Branch name on the Polaris Server. The branch will be created if it doesn't exist in Polaris. | Optional |
| `POLARIS_BRANCH_PARENT_NAME` | Parent Branch name in the Polaris Server. Parent branch name is used by the PR comments feature. | Optional |
| `POLARIS_PRCOMMENT_ENABLED` | Option to enable automatic creation of pull request comments for new issues found in the pull request.  Note: The merge request from the feature branch to the main branch must exist for this feature to work.  **Default**: `false` | Optional |
| `POLARIS_PRCOMMENT_SEVERITIES` | Adds PR Comments only for issues with the severity level specified. If the value is "HIGH", only issues with that severity will have PR comment. The value is a comma-separated string.  **Default**: `"Critical, High"` | Optional |
| `POLARIS_FIXPR_ENABLED` | Enable automatic Fix Pull Request creation for eligible SAST and/or SCA issues. Creates Pull Requests containing dependency upgrades for SCA issues and/or AI-generated code fixes for SAST vulnerabilities, based on the configured assessment types. Only runs on push and workflow_dispatch events.  **Default**: `false`  **Classic Editor UI**: When `Scan Type = "Polaris"`, the Classic editor shows a new `"Fix Pull Request Options"` group. Users enable it using the `"Create Fix Pull Request"` checkbox; when selected, three fields appear to set the `max PR count`, `upgrade guidance (SHORT_TERM/LONG_TERM)`, and `severity filter (CRITICAL/HIGH/MEDIUM/LOW)`. | Optional |
| `POLARIS_FIXPR_MAXCOUNT` | Maximum number of Fix Pull Requests to create per scan/workflow run. This limits the number of Pull Requests generated to avoid overwhelming the repository with too many automated Pull Requests at once. By default, a maximum count of five Fix PRs can be raised across both SAST and SCA scans, with SAST evaluated first. Dismissed issues are excluded, then the `polaris.fixPR.filter.severities` allow list is applied. Only the first `maxCount` results are selected.  **Default**: `5` | Optional |
| `POLARIS_FIXPR_USEUPGRADEGUIDANCE` | For SCA Fix PRs, this allows the user to specify short-term or long-term upgrade guidance, or both. If both values are provided, the first takes priority, and the second value is used only if the first returns no results. If upgrade guidance is not available, the Fix Pull Request is not created.  **Accepted Values**:  - `SHORT_TERM` - `LONG_TERM` - `SHORT_TERM,LONG_TERM` - `LONG_TERM,SHORT_TERM`  **Default**: `SHORT_TERM,LONG_TERM` | Optional |
| `POLARIS_FIXPR_FILTER_SEVERITIES` | Creates Fix PRs only for issues with a severity matching a filter. The value is a comma-separated list. If both SAST and SCA assessments types are enabled, the specified severities are applied to issues from both assessment types.  **Accepted values**: One or more of the following (comma-separated, case-insensitive):   - CRITICAL - HIGH - MEDIUM - LOW   **Default**: CRITICAL,HIGH | Optional |
| `AZURE_TOKEN` | Azure Access Token.  **Example**: `AZURE_TOKEN: $(System.AccessToken)` or `AZURE_TOKEN: $(PAT_TOKEN)` | Mandatory if `polaris_prcomment_enabled` or `polaris_fixpr_enabled` is set as `true`. |
| `POLARIS_REPORTS_SARIF_CREATE` | Set this to `true` to generate SARIF report.  **Default**: `false`  Note: SARIF reports can be generated for any configured branch; however, report generation is not supported in a PR/MR context. | Optional |
| `POLARIS_REPORTS_SARIF_FILE_PATH` | File path (including file name) where SARIF report is created. Only `.sarif` or `.sarif.json` files will be uploaded. All other formats are excluded.  Note: The Custom SARIF file path will always be prefixed with `$(Build.SourcesDirectory)`  - When the bridge version is lower than 3.5.0, the **default** SARIF file path will be:   - `.bridge/Polaris SARIF Generator/report.sarif.json` - When the bridge version is greater than 3.5.0, then the **default** SARIF file path will be:   - `.blackduck/integrations/polaris/sarif/report.sarif.json` | Optional |
| `POLARIS_REPORTS_SARIF_SEVERITIES` | Comma-separated list of SAST/SCA issue severities to include in SARIF file report. Valid severities are `Critical`, `High`, `Medium`, `Low`, and `Informational`.  **Default**: All severities are included. | Optional |
| `POLARIS_REPORTS_SARIF_ISSUE_TYPES` | Indicates which assessment issues type to include in SARIF file report | Optional |
| `POLARIS_REPORTS_SARIF_GROUPSCAISSUES` | When set to true, SCA issues are grouped by component. Set this to false to list SCA issues by vulnerability.  **Default**: `true` | Optional |
| `PROJECT_DIRECTORY` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `PROJECT_SOURCE_ARCHIVE` | The zipped source file path. It overrides the project directory. | Optional |
| `POLARIS_ASSESSMENT_MODE` | The test mode type of the Polaris scan. Supported values: `SOURCE_UPLOAD`, `CI` **NOTE:** This parameter is deprecated. Use `POLARIS_TEST_SAST_LOCATION=remote` and/or `POLARIS_TEST_SCA_LOCATION=remote` for source upload scans instead.  **BREAKING CHANGE**: Please update existing classic editor pipelines that use `Polaris Assessment Mode=SOURCE_UPLOAD` to use `SAST Test Location=remote` and/or `SCA Test Location=remote` instead. When making this change, ensure that you re-enter values for dependent UI fields as required, e.g. `Upload Archive Instead Of Directory`, `Project Source Excludes`, and `Project Source Preserve SymLinks`.  **Default:** `CI` | Optional (deprecated) |
| `POLARIS_TEST_SAST_LOCATION` | Configure the location of source code capture and SAST analysis. Supported values are `hybrid`, `local` and `remote`.  **Default**:`hybrid`  In `hybrid` mode Bridge downloads tools for local capture and uploads artifacts (idir) for analysis on Polaris.  In `local` mode Bridge downloads tools for local capture and performs a full analysis in the local CI/CD environment, with results uploaded to Polaris.  In `remote` mode Bridge zips source code and uploads to Polaris for full capture and analysis.  Note: When Fix PRs are enabled and `POLARIS_ASSESSMENT_TYPES` includes `SAST` then valid values are `hybrid` or `remote`. If `local` is specified, Fix PRs will be skipped and a warning will be logged. | Optional. Required for Source Code Upload for SAST assessment type. |
| `POLARIS_TEST_SCA_LOCATION` | Configure location of source code capture and SCA analysis. Supported values are `hybrid` and `remote`.  **Default**: `hybrid`  In `hybrid` mode Bridge downloads tools for local capture and uploads artifacts (BDIO) for analysis on Polaris.  In `remote` mode Bridge zips source code and uploads to Polaris for full capture and analysis. | Optional. Required for Source Code Upload for SCA assessment type. |
| `PROJECT_SOURCE_EXCLUDES` | A list of git ignore pattern strings that indicate the files that should to be excluded from the zip file. | Optional |
| `POLARIS_TEST_SAST_TYPE` | Polaris test type to trigger sigma rapid scan or full scan. Supported values: `SAST_FULL` or `SAST_RAPID`  **Default**: `SAST_FULL` | Optional |
| `POLARIS_TEST_SCA_TYPE` | Polaris test type to trigger signature scan, package manager scan, container scan or binary scan. **Default value**: `SCA-PACKAGE` **Supported values**:  - `SCA-BINARY` - `SCA-CONTAINER` - `SCA-PACKAGE` - `SCA-SIGNATURE` - `SCA-PACKAGE, SCA-SIGNATURE`   Note: `SCA-BINARY` and `SCA-CONTAINER` can only be used stand-alone. Those parameter values cannot be combined with `SCA-PACKAGE` or `SCA-SIGNATURE` in the same run. Attempting to mix scan types results in a validation error. | Optional |
| `POLARIS_ARTIFACTTOUPLOAD` | Path to an artifact file to be uploaded for analysis. Use this parameter when `polaris_test_sca_type` is set to `SCA-BINARY` or `SCA-CONTAINER`.  - For `SCA-BINARY`, specify the path to the binary or archive file to analyze. - For `SCA-CONTAINER`, specify the path to a valid container image archive (`tar`, `zip`, `gz`, or `tgz`). The archive must contain a container image, such as one created using `docker save`.   Note: The file must be accessible from the execution environment. If the parameter is not specified, the scan fails validation.  **Default:**None | Optional. Required when `POLARIS_TEST_SCA_TYPE` is set to `SCA-BINARY` or `SCA-CONTAINER`. |
| `POLARIS_CONTAINER_NAME` | A name to associate with the container image. The container name will be listed in the containers section of the project in the Polaris web UI and can also be used as a filter.   **Default:** None | Optional. Required when `POLARIS_TEST_SCA_TYPE` is set to `SCA-CONTAINER`. |
| `POLARIS_WAITFORSCAN` | Specifies if the workflow should wait for the analysis to complete.  **Default** : `true`  If set to false, post scan workflows like PR comment, Fix PR, SARIF etc. will not be applicable. | Optional |

Table 2. List of optional parameters for Polaris client scan tools

| Scan tool | Input parameter | Description |
| --- | --- | --- |
| Coverity | `COVERITY_ARGS` | Pass generic arguments to Coverity CLI. |
| `COVERITY_BUILD_COMMAND` | Build command for the project to be passed to Coverity. |
| `COVERITY_CLEAN_COMMAND` | Clean command for the project to be passed to Coverity. |
| `COVERITY_CONFIG_PATH` | Path to coverity.yml file to be passed to Coverity. |
| `COVERITY_VERSION` | Select the Coverity version to use for SAST local and SAST hybrid scans (full and rapid) Important: SAST remote scans use default version from Polaris Web UI.  **Default**: Bridge uses the version configured on Polaris Web UI for the application, project or branch being scanned. **Acceptable Values**: Versions of Coverity that are supported on Polaris (including deprecated versions). **Example**: `2025.6.2`  **Classic Editor UI**: The Coverity Version field exists within  `Coverity (SAST) Tool Options` |
| Detect | `DETECT_ARGS` | Pass any argument to Detect. |
| `DETECT_CONFIG_PATH` | Path to configuration file - to be passed to Detect. |
| `DETECT_SEARCH_PATH` | Search Depth to be passed to Black Duck-Detect. |
