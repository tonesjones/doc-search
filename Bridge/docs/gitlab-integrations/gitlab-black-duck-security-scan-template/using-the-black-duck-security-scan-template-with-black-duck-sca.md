---
title: "Using the Black Duck Security Scan Template with Black Duck SCA"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-template-with-black-duck-sca.html"
content_id: "chYvhUEMaCkHVaZETnX1cw"
version: "latest"
section: "GitLab Integrations"
scraped_at: "2026-08-08T23:48:07.154703+00:00"
---

# Using the Black Duck Security Scan Template with Black Duck SCA

Black Duck Security Scan Template supports both self-hosted (on-prem) and Black Duck hosted Black Duck® SCA Hub instances.

In the default Black Duck® SCA Hub permission model, projects and project versions are created on the fly as needed. Ensure that permissions needed to create projects and project versions are granted on Black Duck® SCA Hub.

Black Duck Security Template requires that you run full “intelligent” Black Duck® SCA scans for SCM push events and “rapid” ephemeral scans for SCM pull request events as shown in the example below.

For an overview about using PR Comments, please see the following documentation page: Pull request (PR) comments

To use Black Duck Security Scan Template with Black Duck® SCA, add `.gitlab-ci.yml` to your project using an `include` entry as shown in the examples below.

Simplified example

```
include:
  - project: blackduck-inc/black-duck-security-scan
    ref: v2
    file: templates/security_scan.yml
  ### Use below configuration for accessing blackduck-security-scan in Gitlab self-managed
  # - remote: 'https://gitlab.com/blackduck-inc/black-duck-security-scan/-/raw/main/templates/security_scan.yml'

stages:
  - blackduck_scan
  
variables:
  SCAN_BRANCHES: "/^(main|master|develop|stage|release|feature_branch)$/" # Add branches where you want to run Black Duck scan

blackduck_security_scan_execution:
  stage: blackduck_scan
  extends: .run-black-duck-tools # Used for bash.
  #extends: .run-black-duck-tools-powershell # Used for powershell
  variables:
    BRIDGE_BLACKDUCKSCA_URL: $BLACKDUCKSCA_URL
    BRIDGE_BLACKDUCKSCA_TOKEN: $BLACKDUCKSCA_API_TOKEN

    ### Required When PR comments or Fix PR enabled
    # BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN

    ### Pull Request Comments
    # BRIDGE_BLACKDUCKSCA_PRCOMMENT_ENABLED: 'true'
  
    ### Fix Pull Request Creation
    # BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED: 'true'

    ### SARIF Report Generation
    # BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE: 'true'

    ### Uncomment this to use Gitlab Security Report
    # BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_CREATE: 'true'

    ### Enable Bridge CLI diagnostics
    # INCLUDE_DIAGNOSTICS: 'true'
  rules:
    - if: ($CI_COMMIT_REF_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event')
    - if: ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event')
  artifacts:
    when: always
    ### Uncomment this to use Gitlab Security Report
    # reports:
    #  dependency_scanning: $CI_PROJECT_DIR/.blackduck/integrations/blackducksca/gitlab_report/sca.json
    ### Uncomment to upload diagnsotics or SARIF report
    # paths:
    #   - .bridge  # Upload bridge diagnostics to artifact
    #   - .blackduck/integrations/blackducksca/sarif/report.sarif.json # Used when INCLUDE_DIAGNOSTICS is enabled and BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE is enabled
```

Note: SARIF report creation is only supported for non-merge request scans.

Detailed example

```
include:
  - project: blackduck-inc/black-duck-security-scan
    ref: v2
    file: templates/security_scan.yml
  ### Use below configuration for accessing blackduck-security-scan in Gitlab self-managed
  # - remote: 'https://gitlab.com/blackduck-inc/black-duck-security-scan/-/raw/main/templates/security_scan.yml'

stages:
  - blackduck_scan
variables:
  SCAN_BRANCHES: "/^(main|master|develop|stage|release|feature_branch)$/" # Add branches where you want to run Black Duck scan

blackduck_security_scan_execution:
  stage: blackduck_scan
  variables:
    BRIDGE_BLACKDUCKSCA_URL: $BLACKDUCKSCA_URL
    BRIDGE_BLACKDUCKSCA_TOKEN: $BLACKDUCKSCA_API_TOKEN

    ### Use below configuration to set specific detect environment variables
    DETECT_PROJECT_NAME: $CI_PROJECT_NAME

    ### Uncomment to specify the directory to scan. Default value is repository root
    # BRIDGE_PROJECT_DIRECTORY: $PROJECT_DIRECTORY

    ### Uncomment below to add arbitrary CL parameters
    # BRIDGE_DETECT_SEARCH_DEPTH: 1
    # BRIDGE_DETECT_CONFIG_PATH: '/USERS/USER/application.properties'
    # BRIDGE_DETECT_ARGS: '--detect.diagnostic=true'

    ### Enable Bridge-CLI diagnostics
    INCLUDE_DIAGNOSTICS: 'true'
    
    ### To enable the use of self-signed certificates
    # BRIDGE_NETWORK_SSL_TRUSTALL: true

    ### Mark build status if policy violating issues are found
    #MARK_BUILD_STATUS: 'success'

  rules:
    ### Use below configuration to run Black Duck full scan
    - if: ($CI_COMMIT_BRANCH =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event')
      variables:
        BRIDGE_BLACKDUCKSCA_SCAN_FULL: 'true'
        BRIDGE_BLACKDUCKSCA_SCAN_FAILURE_SEVERITIES: 'BLOCKER,CRITICAL'
        #BRIDGE_BLACKDUCKSCA_WAITFORSCAN: 'false'   # Used to support the async mode

        ### FIX PULL REQUEST CREATION
        BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED: 'true'
        BRIDGE_BLACKDUCKSCA_FIXPR_MAXCOUNT: 5
        BRIDGE_BLACKDUCKSCA_FIXPR_FILTER_SEVERITIES: 'CRITICAL,HIGH'
        BRIDGE_BLACKDUCKSCA_FIXPR_USEUPGRADEGUIDANCE: 'LONG_TERM,SHORT_TERM'
        BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN # Mandatory when BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED is set to 'true'

        ### SARIF Report Generation
        BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE: 'true'
        BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_FILE_PATH: $CI_PROJECT_DIR/report.sarif.json
        BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_SEVERITIES: 'CRITICAL,HIGH'
        BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_GROUPSCAISSUES: 'true'

        ### Uncomment this to use Gitlab Security Report
        #BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_CREATE: 'true'
        #BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_DIR_PATH: $CI_PROJECT_DIR
        #BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_ISSUE_TYPES: 'SCA,SAST'
        #BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_SEVERITIES: 'CRITICAL,HIGH'
        #BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_GROUPSCAISSUES: 'true'

    ### Use below configuration to run Black Duck PR scan
    - if: ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event')
      variables:
        BRIDGE_BLACKDUCKSCA_SCAN_FULL: 'false'
        BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT: 'true'
        BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN
  tags:
    - macOS # Name of your Gitlab runner
  extends: .run-black-duck-tools # Used for bash.
  #extends: .run-black-duck-tools-powershell # Used for powershell
  ### Uncomment below configuration for uploading job artifacts if you have enabled INCLUDE_DIAGNOSTICS or BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE
  artifacts:
    when: always
    ### Uncomment this to use Gitlab Security Report
    #reports:
    #  dependency_scanning: $CI_PROJECT_DIR/sca.json # Used when BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_CREATE is enabled and BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_DIR_PATH is set
    #  dependency_scanning: $CI_PROJECT_DIR/sast.json
    paths:
      - .blackduck/integrations/blackducksca/sarif/report.sarif.json # Used when INCLUDE_DIAGNOSTICS is enabled and BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE is enabled
      - $CI_PROJECT_DIR/report.sarif.json # Used when BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE is enabled and BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_FILE_PATH is set

    ### Uncomment below configuration to add custom logic based on return status
    #after_script : |
    #  echo "Black Duck Security Scan exit status - $status"
```

Table 1. **List of mandatory and optional parameters for Black Duck**

| Input Parameter | Description | Mandatory/Optional |
| --- | --- | --- |
| `BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT` | Option to enable automatic creation of pull request comments for new issues found in the pull request.  Note: The merge request from the feature branch to the main branch must exist for this feature to work.  **Default**: `false` | Optional |
| `BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED` | Enables or disables the automated creation of fix pull request for Black Duck® SCA.  **Default**: false. | Optional |
| `BRIDGE_BLACKDUCKSCA_FIXPR_FILTER_SEVERITIES` | Creates Fix PRs only for issues with the severity level specified. If the value is "HIGH", only issues with that severity will have Fix PRs. The value is a comma-separated list.  Supported severities: CRITICAL, HIGH, MEDIUM, LOW  **Default**: "CRITICAL, HIGH" | Optional |
| `BRIDGE_BLACKDUCKSCA_FIXPR_MAXCOUNT` | Maximum number of pull requests allowed on a branch when policies are violated. A PR is created for each vulnerable component. | Optional |
| `BRIDGE_BLACKDUCKSCA_FIXPR_USEUPGRADEGUIDANCE` | Black Duck® SCA Hub upgrade guidance values.  **Default**:"SHORT_TERM, LONG_TERM" | Optional |
| `BRIDGE_DETECT_INSTALL_DIRECTORY` | Installation directory for Detect | Optional |
| `BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE` | Set this to `true` to generate SARIF report. **Default:**`false`  Note: SARIF reports can be generated for any configured branch; however, report generation is not supported in a merge request context. | Optional |
| `BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_FILE_PATH` | File path (including file name) where SARIF report is created.  Note: GitLab is only able to package artifacts found in the `$CI_PROJECT_DIR` directory. If `BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_FILE_PATH` is set outside `$CI_PROJECT_DIR`, SARIF report will not be uploaded.  **Default:**`.blackduck/integrations/blackducksca/sarif/report.sarif.json` | Optional |
| `BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_GROUPSCAISSUES` | When set to `true`, SCA issues are grouped by component. Set this to `false` to list SCA issues by vulnerability. **Default:**`true` | Optional |
| `BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_SEVERITIES` | Comma-separated list of SAST/SCA issue severities to include in SARIF file report. Valid severities are `Critical`, `High`, `Medium`, `Low`, and `Informational`. **Default:** All severities are included. | Optional |
| `BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_CREATE` | Set this to `true` to generate Black Duck SCA report.  Note: Gitlab reports can be generated for any configured branch; however, report generation is not supported in a merge request context.  **Default**: `false` | Optional |
| `BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_DIR_PATH` | Directory path (excluding file name) where Gitlab report is created.  Note: GitLab is only able to package artifacts found in the `$CI_PROJECT_DIR` directory. If `BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_DIR_PATH` is set outside `$CI_PROJECT_DIR`, Gitlab report will not be uploaded.  **Default**: `$CI_PROJECT_DIR/.blackduck/integrations/blackducksca/gitlab_report/sca.json` | Optional |
| `BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_SEVERITIES` | Comma-separated list of SCA issue severities to include in Gitlab file report. Valid severities are `Critical`, `High`, `Medium`, `Low`, and `Informational`.  **Default**: `All severities are included.` | Optional |
| `BRIDGE_BLACKDUCKSCA_REPORTS_GITLAB_GROUPSCAISSUES` | When set to true, SCA issues are grouped by component. Set this to false to list SCA issues by vulnerability.  **Default**: `true` | Optional |
| `BRIDGE_BLACKDUCKSCA_SCAN_FAILURE_SEVERITIES` | Black Duck® SCA scan failure severities used to decide if build should be broken.  Supported values: `ALL`, `NONE`, `BLOCKER`, `CRITICAL`,`MAJOR`, `MINOR`, `OK`, `TRIVIAL`, `UNSPECIFIED` | Optional |
| `BRIDGE_BLACKDUCKSCA_SCAN_FULL` | Specifies whether full scan is required or not.  Must be set to `true` for push events and `false` for pull request events.  **Default**: `false` | Optional |
| `BRIDGE_BLACKDUCKSCA_TOKEN` | Black Duck® SCA API token | Mandatory |
| `BRIDGE_BLACKDUCKSCA_URL` | Black Duck® SCA server URL | Mandatory |
| `BRIDGE_GITLAB_USER_TOKEN` | GitLab User Access Token  Example: `BRIDGE_GITLAB_USER_TOKEN: $GITLAB_ACCESS_TOKEN` | Mandatory when `BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT` or `BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED` is set as `true`. |
| `BRIDGE_PROJECT_DIRECTORY` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `BRIDGE_DETECT_SEARCH_DEPTH` | Number indicating the search depth in the source directory. | Optional |
| `BRIDGE_DETECT_CONFIG_PATH` | Detect config file path location. | Optional |
| `BRIDGE_DETECT_ARGS` | Additional arguments for Detect. | Optional |
| `BRIDGE_BLACKDUCKSCA_WAITFORSCAN` | Specifies if the workflow should wait for the analysis to complete.  **Default** : `true`  If set to false, post scan workflows like PR comment, Fix PR, SARIF etc will not be applicable. | Optional |

Note: Detect specific options can be passed through Detect environment variables.

Table 2. List of network parameters

| **Input Parameter** | **Description** | **Mandatory/Optional** |
| --- | --- | --- |
| `BRIDGE_NETWORK_SSL_TRUSTALL` | Disables SSL certificate verification. Use with caution.  **Default**: false | Optional |
