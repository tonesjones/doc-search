---
title: "Using the Black Duck Security Scan Template with Polaris"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-template-with-polaris.html"
content_id: "f2zGV_v5_yTOMY8WeMUeyw"
version: "latest"
section: "GitLab Integrations"
scraped_at: "2026-08-08T23:48:05.437177+00:00"
---

# Using the Black Duck Security Scan Template with Polaris

Before running a pipeline using the Black Duck Security Scan Template with Polaris, you must set the appropriate applications and entitlements in your Polaris environment.

Using the Black Duck Security Scan Template, you can perform scans on push events to main branches.

Client scan tools can be configured using the Bridge CLI environment variables within the Black Duck Security Scan Template. For SAST scans the Coverity version can be selected using the `BRIDGE_COVERITY_VERSION` environment variable. Please refer to Complete List Of Bridge Commands for further details.

It is recommended that you configure sensitive information such as access tokens and URLs using GitLab secrets.

A Polaris Project is created as necessary. If you don't want the project to be created, set `polaris.onboarding` to `false`.

For an overview about using PR Comments, please see the following documentation page: Pull request (PR) comments.

For an overview about using Fix Pull Requests, please see the following documentation page: Fix pull requests (Fix PRs).

To use the GitLab Template, add `.gitlab-ci.yml` to your project by using an `include` entry, as shown in the examples below.

Simplified example

```
include:
  - project: blackduck-inc/black-duck-security-scan
    ref: v2
    file: templates/security_scan.yml
  ### Use below configuration for accessing blackduck-security-scan in Gitlab self-managed
  # - remote: 'https://gitlab.com/blackduck-inc/black-duck-security-scan/-/raw/main/templates/security_scan.yml'

stages:
  - security

variables:
  SCAN_BRANCHES: "/^(main|master|develop|stage|release|feature_branch)$/" # Add branches where you want to run Black Duck scan

Polaris:
  stage: security
  extends: .run-black-duck-tools # Used for bash.
  # extends: .run-black-duck-tools-powershell # Used for powershell
  variables:
    BRIDGE_POLARIS_SERVERURL: $POLARIS_SERVERURL
    BRIDGE_POLARIS_ACCESSTOKEN: $POLARIS_ACCESSTOKEN
    BRIDGE_POLARIS_ASSESSMENT_TYPES: 'SAST,SCA'

    ### Uncomment below to run SCA Binary Scan
    ### Requires that BRIDGE_POLARIS_ASSESSMENT_TYPES is set to SCA only
    #BRIDGE_POLARIS_TEST_SCA_TYPE: 'SCA-BINARY'
    #BRIDGE_POLARIS_ARTIFACTTOUPLOAD: '/path/to/source.zip'

    ### Uncomment below to run SCA Container Scan
    ### Requires that BRIDGE_POLARIS_ASSESSMENT_TYPES is set to SCA only
    #BRIDGE_POLARIS_TEST_SCA_TYPE: 'SCA-CONTAINER'
    #BRIDGE_POLARIS_ARTIFACTTOUPLOAD: '/path/to/container.tar.gz'
    #BRIDGE_POLARIS_CONTAINER_NAME: 'unique-container-name' # use for filtering

    ### Required When PR comments or Fix PR enabled
    # BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN 

    ### Pull Request Comments
    # BRIDGE_POLARIS_PRCOMMENT_ENABLED: 'true'
  
    ### Fix Pull Request Creation
    # BRIDGE_POLARIS_FIXPR_ENABLED: 'true'
  
    ### SARIF Report Creation
    # BRIDGE_POLARIS_REPORTS_SARIF_CREATE: 'true'
  
    ### Create and Upload GitLab Security Report
    # BRIDGE_POLARIS_REPORTS_GITLAB_CREATE: 'true'

    ### Enable Bridge CLI diagnostics
    # INCLUDE_DIAGNOSTICS: 'true'
  rules:
    - if: ($CI_COMMIT_REF_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event')
    - if: ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event')
  before_script:
    - apt-get -qq update && apt-get install -y curl unzip
  artifacts:
    name: "bridge-logs"
    when: always
    ### Uncomment to Upload Gitlab Security Report
    # reports:
      # sast: $CI_PROJECT_DIR/.blackduck/integrations/polaris/gitlab_report/sast.json
      # dependency_scanning: $CI_PROJECT_DIR/.blackduck/integrations/polaris/gitlab_report/sca.json
    ### Uncomment to Upload Diagnostics or SARIF Report
    # paths:
      # - .bridge  # Upload bridge diagnostics to artifact
      # - .blackduck/integrations/polaris/sarif/report.sarif.json # Used when BRIDGE_POLARIS_REPORTS_SARIF_CREATE is enabled
    # expire_in: 30 days
```

Note: SARIF report creation is only supported for non-merge request scans.

Once you push the changes above, an active runner will pick up the job and initiate the pipeline.

Detailed example

```
include:
  - project: blackduck-inc/black-duck-security-scan
    ref: v2
    file: templates/security_scan.yml
  ### Use below configuration for accessing blackduck-security-scan in Gitlab self-managed
  # - remote: 'https://gitlab.com/blackduck-inc/black-duck-security-scan/-/raw/main/templates/security_scan.yml'

stages:
  - polaris_scan

variables:
  SCAN_BRANCHES: "/^(main|master|develop|stage|release|feature_branch)$/" # Add branches where you want to run Polaris scan
blackduck_security_scan_execution:
  stage: polaris_scan
  variables:
    BRIDGE_POLARIS_SERVERURL: $POLARIS_SERVER_URL
    BRIDGE_POLARIS_ACCESSTOKEN: $POLARIS_ACCESS_TOKEN
    BRIDGE_POLARIS_APPLICATION_NAME: $CI_PROJECT_NAME
    BRIDGE_POLARIS_PROJECT_NAME: $CI_PROJECT_NAME
    BRIDGE_POLARIS_BRANCH_NAME: $CI_COMMIT_REF_NAME
    BRIDGE_POLARIS_ASSESSMENT_TYPES: 'SCA,SAST'

    ### Uncomment to specify the directory to scan. Default value is repository root
    #BRIDGE_PROJECT_DIRECTORY: $PROJECT_DIRECTORY

    ### Uncomment below to add arbitrary CL parameters
    #BRIDGE_COVERITY_BUILD_COMMAND: 'mvn clean install'
    #BRIDGE_COVERITY_CLEAN_COMMAND: 'mvn clean'
    #BRIDGE_COVERITY_CONFIG_PATH: '/USERS/USER/coverity.yml'
    #BRIDGE_COVERITY_ARGS: '-c /USERS/USER/coverity.yml -o capture.build.clean-command="mvn clean" -- mvn clean install'
    #BRIDGE_COVERITY_VERSION: '2025.6.2'
    #BRIDGE_DETECT_SEARCH_DEPTH: 1
    #BRIDGE_DETECT_CONFIG_PATH: '/USERS/USER/application.properties'
    #BRIDGE_DETECT_ARGS: '--detect.diagnostic=true'

    ### Uncomment this to use Source Upload method. Default value is hybrid (build based)
    #BRIDGE_POLARIS_TEST_SAST_LOCATION: 'remote'
    #BRIDGE_POLARIS_TEST_SCA_LOCATION: 'remote'
    #BRIDGE_PROJECT_SOURCE_ARCHIVE: $PROJECT_ARCHIVE
    #BRIDGE_PROJECT_SOURCE_EXCLUDES: $PROJECT_SOURCE_EXCLUDES

    #### Uncomment this to use Local Analysis feature
    #Please use Local Analysis or Source Upload exclusively
    #BRIDGE_POLARIS_TEST_SAST_LOCATION: 'local'

    ### Enable Bridge CLI diagnostics
    INCLUDE_DIAGNOSTICS: 'true'

    ### Mark build status if policy violating issues are found
    #MARK_BUILD_STATUS: 'success'

  rules:
    ### Post scan options for push events to main, develop, staging or release branches,  
    - if: ($CI_COMMIT_BRANCH =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event')
      variables:
        ### Fix PR configuration
        # Creates Fix PRs for the assessment types configured in
        # BRIDGE_POLARIS_ASSESSMENT_TYPES (SAST, SCA, or both).
        # Requires BRIDGE_GITLAB_USER_TOKEN.
        BRIDGE_POLARIS_FIXPR_ENABLED: 'true'
        # Maximum number of Fix PRs across SAST and SCA combined.
        BRIDGE_POLARIS_FIXPR_MAXCOUNT: '5'
        # Upgrade guidance applies to SCA Fix PRs only.
        BRIDGE_POLARIS_FIXPR_USEUPGRADEGUIDANCE: 'SHORT_TERM,LONG_TERM'
        # Matching severities generate SAST and/or SCA Fix PRs,
        # depending on BRIDGE_POLARIS_ASSESSMENT_TYPES.
        BRIDGE_POLARIS_FIXPR_FILTER_SEVERITIES: 'CRITICAL,HIGH'

        BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN
  
        ### SARIF report configurations
        BRIDGE_POLARIS_REPORTS_SARIF_CREATE: 'true'
        BRIDGE_POLARIS_REPORTS_SARIF_FILE_PATH: $CI_PROJECT_DIR/report.sarif.json
        BRIDGE_POLARIS_REPORTS_SARIF_ISSUE_TYPES: 'SCA,SAST'
        BRIDGE_POLARIS_REPORTS_SARIF_SEVERITIES: 'CRITICAL,HIGH'
        BRIDGE_POLARIS_REPORTS_SARIF_GROUPSCAISSUES: 'true'

        ### Uncomment this to use Gitlab Security Report
        #BRIDGE_POLARIS_REPORTS_GITLAB_CREATE: 'true'
        #BRIDGE_POLARIS_REPORTS_GITLAB_DIR_PATH: $CI_PROJECT_DIR
        #BRIDGE_POLARIS_REPORTS_GITLAB_ISSUE_TYPES: 'SCA,SAST'
        #BRIDGE_POLARIS_REPORTS_GITLAB_SEVERITIES: 'CRITICAL,HIGH'
        #BRIDGE_POLARIS_REPORTS_GITLAB_GROUPSCAISSUES: 'true'

        #BRIDGE_POLARIS_WAITFORSCAN: 'false'   # Used to support the async mode

        ### Signature scan
        #BRIDGE_POLARIS_TEST_SCA_TYPE:'SCA-SIGNATURE'

        ### Uncomment below to run SCA Binary Scan
        ### Requires that POLARIS_ASSESSMENT_TYPES is set to SCA only
        #BRIDGE_POLARIS_TEST_SCA_TYPE: 'SCA-BINARY'
        #BRIDGE_POLARIS_ARTIFACTTOUPLOAD: '/path/to/source.zip'

        ### Uncomment below to run SCA Container Scan
        ### Requires that POLARIS_ASSESSMENT_TYPES is set to SCA only
        #BRIDGE_POLARIS_TEST_SCA_TYPE: 'SCA-CONTAINER'
        #BRIDGE_POLARIS_ARTIFACTTOUPLOAD: '/path/to/container.tar.gz'
        #BRIDGE_POLARIS_CONTAINER_NAME: 'unique-container-name' # use for filtering

    ### Polaris PR scan
    - if: ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event')
      variables:
        BRIDGE_POLARIS_PRCOMMENT_ENABLED: 'true'    # When PR comments is enabled $GITLAB_USER_TOKEN is mandatory
        BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN
        BRIDGE_POLARIS_PRCOMMENT_SEVERITIES: 'CRITICAL,HIGH'
  tags:
    - linux # Name of your Gitlab runner
  extends: .run-black-duck-tools # Used for bash.
  # extends: .run-black-duck-tools-powershell # Used for powershell
  ### Use below configuration for uploading job artifacts if you have enabled INCLUDE_DIAGNOSTICS or BRIDGE_POLARIS_REPORTS_SARIF_CREATE
  artifacts:
    when: always
    ### Uncomment this to use Gitlab Security Report
    #reports:
      #sast: $CI_PROJECT_DIR/.blackduck/integrations/polaris/gitlab_report/sast.json # BRIDGE_POLARIS_REPORTS_GITLAB_CREATE enabled and BRIDGE_POLARIS_REPORTS_GITLAB_DIR_PATH path is set
      #dependency_scanning: $CI_PROJECT_DIR/.blackduck/integrations/polaris/gitlab_report/sca.json # BRIDGE_POLARIS_REPORTS_GITLAB_CREATE enabled and BRIDGE_POLARIS_REPORTS_GITLAB_DIR_PATH path is set
    paths:
      - .bridge  # Upload bridge diagnostics to artifact
      - .blackduck/integrations/polaris/sarif/report.sarif.json # Used when BRIDGE_POLARIS_REPORTS_SARIF_CREATE is enabled
      - $CI_PROJECT_DIR/report.sarif.json # Used when BRIDGE_POLARIS_REPORTS_SARIF_CREATE is enabled and BRIDGE_POLARIS_REPORTS_SARIF_FILE_PATH is set

  ### Uncomment below configuration to add custom logic based on return status
  #after_script : |
  #  echo "Polaris Scan exit status - $status"
```

Table 1. **List of mandatory and optional parameters for Polaris**

| Input Parameter | Description | Mandatory / Optional |
| --- | --- | --- |
| `BRIDGE_POLARIS_ACCESSTOKEN` | Polaris access token. You can use either a user access token (created in the Polaris UI) or a service account token here. | Mandatory |
| `BRIDGE_POLARIS_APPLICATION_NAME` | Application name in Polaris The Default Value is `CI_PROJECT_NAME` | Optional |
| `BRIDGE_POLARIS_ASSESSMENT_TYPES` | Polaris assessment types  Accepted values:   - `DAST` - `SAST` - `SCA` - `SAST,SCA`   For DAST configuration requirements, see Using Bridge CLI With Polaris. | Mandatory |
| `BRIDGE_POLARIS_BRANCH_NAME` | Branch name on the Polaris Server. The branch is created if it doesn't already exist. | Optional |
| `BRIDGE_POLARIS_BRANCH_PARENT_NAME` | Parent branch name on the Polaris Server. Parent branch name is used by the PR comments feature. | Optional |
| `BRIDGE_POLARIS_PROJECT_NAME` | Project name in PolarisThe Default Value is`$CI_PROJECT_NAME` | Optional |
| `BRIDGE_POLARIS_SERVERURL` | Polaris server URL | Mandatory |
| `BRIDGE_GITLAB_USER_TOKEN` | GitLab User Access Token  Example: `BRIDGE_GITLAB_USER_TOKEN: $GITLAB_ACCESS_TOKEN` | Mandatory when `BRIDGE_POLARIS_PRCOMMENT_ENABLED` is set as `true`. |
| `BRIDGE_POLARIS_REPORTS_SARIF_CREATE` | Set this to `true` to generate SARIF report.  **Default**: `false`  Note: SARIF reports can be generated for any configured branch; however, report generation is not supported in a merge request context. | Optional |
| `BRIDGE_POLARIS_REPORTS_SARIF_FILE_PATH` | File path (including file name) where SARIF report is created.  Note: GitLab is only able to package artifacts found in the `$CI_PROJECT_DIR` directory. If `BRIDGE_POLARIS_REPORTS_SARIF_FILE_PATH` is set outside `$CI_PROJECT_DIR`, SARIF report will not be uploaded.  **Default**: `.blackduck/integrations/polaris/sarif/report.sarif.json` | Optional |
| `BRIDGE_POLARIS_REPORTS_SARIF_ISSUE_TYPES` | Lists which assessment issues types to include in SARIF file report.  Example: `'SCA,SAST'` | Optional |
| `BRIDGE_POLARIS_REPORTS_SARIF_SEVERITIES` | Comma-separated list of SAST/SCA issue severities to include in SARIF file report. Valid severities are `Critical`, `High`, `Medium`, `Low`, and `Informational`.  **Default**: All severities are included. | Optional |
| `BRIDGE_POLARIS_REPORTS_SARIF_GROUPSCAISSUES` | When set to true, SCA issues are grouped by component. Set this to false to list SCA issues by vulnerability.  **Default**: `true` | Optional |
| `BRIDGE_POLARIS_REPORTS_GITLAB_CREATE` | Set this to `true` to generate Polaris SCA/SAST report.  Note: Gitlab reports can be generated for any configured branch; however, report generation is not supported in a merge request context.  **Default**: `false` | Optional |
| `BRIDGE_POLARIS_REPORTS_GITLAB_DIR_PATH` | Directory path (excluding file name) where Gitlab report is created.  Note: GitLab is only able to package artifacts found in the `$CI_PROJECT_DIR` directory. If `BRIDGE_POLARIS_REPORTS_GITLAB_DIR_PATH` is set outside `$CI_PROJECT_DIR`, Gitlab report will not be uploaded.  **Default**:  - `$CI_PROJECT_DIR/.blackduck/integrations/polaris/gitlab_report/sca.json` - `$CI_PROJECT_DIR/.blackduck/integrations/polaris/gitlab_report/sast.json` | Optional |
| `BRIDGE_POLARIS_REPORTS_GITLAB_ISSUE_TYPES` | Lists which assessment issues types to create in Giltab file reports.  **Example**: `'SCA,SAST'` | Optional |
| `BRIDGE_POLARIS_REPORTS_GITLAB_SEVERITIES` | Comma-separated list of SAST/SCA issue severities to include in Gitlab file report. Valid severities are `Critical`, `High`, `Medium`, `Low`, and `Informational`.  **Default**: `All severities are included.` | Optional |
| `BRIDGE_POLARIS_REPORTS_GITLAB_GROUPSCAISSUES` | When set to true, SCA issues are grouped by component. Set this to false to list SCA issues by vulnerability.  **Default**: `true` | Optional |
| `BRIDGE_POLARIS_PRCOMMENT_ENABLED` | Option to enable automatic creation pull request comments for new issues found in the merge request.  Note: The merge request from the feature branch to the main branch must exist for this feature to work.  **Default**: `false` | Optional |
| `BRIDGE_POLARIS_PRCOMMENT_SEVERITIES` | The value should be a comma-separated list of severities. Comments are created for issues where the issue severity matches one of the values specified using this option.  Valid severities are: `Critical`, `High`, `Medium`, `Low`, and `Informational`.  **Default**: `CRITICAL,HIGH` | Optional |
| `BRIDGE_POLARIS_FIXPR_ENABLED` | Enable automatic Fix Pull Request creation for eligible SAST and/or SCA issues. Creates Pull Requests containing dependency upgrades for SCA issues and/or AI-generated code fixes for SAST vulnerabilities, based on the configured assessment types. Only runs on push and workflow_dispatch events.  **Default**: `false` | Optional |
| `BRIDGE_POLARIS_FIXPR_MAXCOUNT` | Maximum number of Fix Pull Requests to create per scan/workflow run. This limits the number of Pull Requests generated to avoid overwhelming the repository with too many automated Pull Requests at once. By default, a maximum count of five Fix PRs can be raised across both SAST and SCA scans, with SAST evaluated first. Dismissed issues are excluded, then the `polaris.fixPR.filter.severities` allow list is applied. Only the first `maxCount` results are selected.  **Default**: `5` | Optional |
| `BRIDGE_POLARIS_FIXPR_USEUPGRADEGUIDANCE` | For SCA Fix PRs, this allows the user to specify short-term or long-term upgrade guidance, or both. If both values are provided, the first takes priority, and the second value is used only if the first returns no results. If upgrade guidance is not available, the Fix Pull Request is not created.  **Accepted Values**:  - `SHORT_TERM` - `LONG_TERM` - `SHORT_TERM,LONG_TERM` - `LONG_TERM,SHORT_TERM`  **Default**:`SHORT_TERM,LONG_TERM` | Optional |
| `BRIDGE_POLARIS_FIXPR_FILTER_SEVERITIES` | Creates Fix PRs only for issues with a severity matching a filter. The value is a comma-separated list. If both SAST and SCA assessments types are enabled, the specified severities are applied to issues from both assessment types.  **Accepted values**: One or more of the following (comma-separated, case-insensitive):   - CRITICAL - HIGH - MEDIUM - LOW   **Default**: `CRITICAL,HIGH` | Optional |
| `BRIDGE_POLARIS_ASSESSMENT_MODE` | The test mode type of the Polaris scan. Supported values: `SOURCE_UPLOAD`, `CI` **Default:**`CI`  **Note**: `BRIDGE_POLARIS_ASSESSMENT_MODE=SOURCE_UPLOAD` is scheduled for deprecation. Please use `remote` for `BRIDGE_POLARIS_TEST_SAST_LOCATION` and/or `BRIDGE_POLARIS_TEST_SCA_LOCATION` instead. | Optional |
| `BRIDGE_POLARIS_TEST_SAST_LOCATION` | Configure the location of source code capture and SAST analysis. Supported values are `hybrid`, `local` and `remote`.   **Default**: `hybrid`    In `hybrid` mode Bridge downloads tools for local capture and uploads artifacts (idir) for analysis on Polaris.    In `local` mode Bridge downloads tools for local capture and performs a full analysis in the local CI/CD environment, with results uploaded to Polaris.    In `remote` mode Bridge zips source code and uploads to Polaris for full capture and analysis. Note: When Fix PRs are enabled and `BRIDGE_POLARIS_ASSESSMENT_TYPES` includes `SAST` then valid values are `hybrid` or `remote`. If `local` is specified, Fix PRs will be skipped and a warning will be logged. | Optional |
| `BRIDGE_POLARIS_TEST_SCA_LOCATION` | Configure location of source code capture and SCA analysis. Supported values are `hybrid` and `remote`.   **Default**: `hybrid`    In `hybrid` mode Bridge downloads tools for local capture and uploads artifacts (BDIO) for analysis on Polaris.    In `remote` mode Bridge zips source code and uploads to Polaris for full capture and analysis. | Optional |
| `BRIDGE_PROJECT_DIRECTORY` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `BRIDGE_PROJECT_SOURCE_ARCHIVE` | The zipped source file path. It overrides the project directory. | Optional |
| `BRIDGE_PROJECT_SOURCE_EXCLUDES` | A list of git ignore pattern strings that indicate the files need to be excluded from the zip file. | Optional |
| `BRIDGE_POLARIS_TEST_SAST_TYPE` | Polaris test type to trigger sigma rapid scan or full scan. Supported values: `SAST_FULL` or `SAST_RAPID`  **Default:**`SAST-FULL` | Optional |
| `BRIDGE_POLARIS_TEST_SCA_TYPE` | Polaris SCA test type to trigger signature scan, package manager scan, container scan or binary scan.  **Default**: SCA-PACKAGE  **Supported values**:  - `SCA-BINARY` - `SCA-CONTAINER` - `SCA-PACKAGE` - `SCA-SIGNATURE` - `SCA-PACKAGE, SCA-SIGNATURE` Note: `SCA-BINARY` and `SCA-CONTAINER`  can only be used stand-alone. Those parameter values cannot be combined with `SCA-PACKAGE` or `SCA-SIGNATURE` in the same run. Attempting to mix scan types results in a validation error. | Optional |
| `BRIDGE_POLARIS_ARTIFACTTOUPLOAD` | Path to an artifact file to be uploaded for analysis. Use this parameter when `BRIDGE_POLARIS_TEST_SCA_TYPE` is set to `SCA-BINARY` or `SCA-CONTAINER`.  - For `SCA-BINARY`, specify the path to the binary or archive file to analyze. - For `SCA-CONTAINER`, specify the path to a valid container image archive (`tar`, `zip`, `gz`, or `tgz`). The archive must contain a container image, such as one created using `docker save`.   Note: The file must be accessible from the execution environment. If the parameter is not specified, the scan fails validation.  **Default:**None | Optional. Required when `BRIDGE_POLARIS_TEST_SCA_TYPE`  is set to ​ `SCA-BINARY` or `SCA-CONTAINER`​. |
| `BRIDGE_POLARIS_CONTAINER_NAME` | A name to associate with the container image. The container name will be listed in the containers section of the project in the Polaris web UI and can also be used as a filter.   **Default:** None | Optional. Required when `BRIDGE_POLARIS_TEST_SCA_TYPE` is set to `SCA-CONTAINER`. |
| `BRIDGE_POLARIS_WAITFORSCAN` | Specifies if the workflow should wait for the analysis to complete.  **Default** : `true`  If set to false, post scan workflows like PR comment, Fix PR, SARIF etc. will not be applicable. | Optional |
