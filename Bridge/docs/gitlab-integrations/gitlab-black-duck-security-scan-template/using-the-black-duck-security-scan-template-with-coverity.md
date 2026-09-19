---
title: "Using the Black Duck Security Scan Template with Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-template-with-coverity.html"
content_id: "3QO4fKpI7QGppwJAdC_oUQ"
version: "latest"
section: "GitLab Integrations"
scraped_at: "2026-08-08T23:48:08.815839+00:00"
---

# Using the Black Duck Security Scan Template with Coverity

On push events, a full Coverity scan will be run and results are committed to the Coverity server database.

On pull request events, comments are added to pull requests for new issues found by the scan if `BRIDGE_COVERITY_PRCOMMENT_ENABLED` is set to `true` (see example below). New issues detected by the scan are uploaded to the Coverity server (CNC and Connect) as preview commits.

For an overview about using PR Comments, please see the following documentation page: Pull request (PR) comments

To use Black Duck Security Scan Template with Coverity Cloud Deployment, add `.gitlab-ci.yml` to your project using an `include` entry as shown the examples below.

Simplified example

```
include:
  - project: blackduck-inc/black-duck-security-scan
    ref: v2
    file: templates/security_scan.yml
  ### Configuration for accessing blackduck-security-scan in Gitlab self-managed
  # - remote: 'https://gitlab.com/blackduck-inc/black-duck-security-scan/-/raw/main/templates/security_scan.yml'
stages:
  - coverity_scan
variables:
  SCAN_BRANCHES: "/^(main|master|develop|stage|release|feature_branch)$/" # Branches to run scanblackduck_security_scan_execution:
  stage: coverity_scan
  extends: .run-black-duck-tools # Used for bash.
  #extends: .run-black-duck-tools-powershell # Used for powershell
  tags:
    - linux
  rules: # For push and merge request events
    - if: (($CI_COMMIT_BRANCH =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event') || ( $CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event') )
      when: always
  variables:
    BRIDGE_COVERITY_CONNECT_URL: $COVERITY_URL
    BRIDGE_COVERITY_CONNECT_USER_NAME: $COVERITY_USER
    BRIDGE_COVERITY_CONNECT_USER_PASSWORD: $COVERITY_PASSWORD
    
    ### Pull Request Comments
    #BRIDGE_COVERITY_PRCOMMENT_ENABLED: 'true'
    ## Use the parameter below to add comments for issues filtered 
    ## by impact. Default is High if unset
    ## NOTE: Issues matching BRIDGE_COVERITY_CONNECT_POLICY_VIEW are ignored if set
    #BRIDGE_COVERITY_PRCOMMENT_IMPACTS: 'High,Medium,Low,Audit'
    #BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN

    ### To enable the use of self-signed certificates
    # BRIDGE_NETWORK_SSL_TRUSTALL: true
    # BRIDGE_NETWORK_SSL_CERT_FILE: '/Users/Config/cert.pem'
    
    #INCLUDE_DIAGNOSTICS: 'true'

    ### Mark build status if policy violating issues are found
    #MARK_BUILD_STATUS: 'success'

  artifacts:
    when: always
    paths:
    - .bridge # Used when INCLUDE_DIAGNOSTICS is enabled

  ### Uncomment below configuration to add custom logic based on return status
  #after_script : |
  #  echo "Coverity Scan exit status - $status"
```

Detailed example

```
include:
  - project: blackduck-inc/black-duck-security-scan
    ref: v2
    file: templates/security_scan.yml
  ### Use below configuration for accessing blackduck-security-scan in Gitlab self-managed 
  # - remote: 'https://gitlab.com/blackduck-inc/black-duck-security-scan/-/raw/main/templates/security_scan.yml'  

stages:
  - coverity_scan

variables:
  SCAN_BRANCHES: "/^(main|master|develop|stage|release|feature_branch)$/" # Add branches where you want to run Coverity scan
blackduck_security_scan_execution:
  stage: coverity_scan
  variables:
    BRIDGE_COVERITY_CONNECT_URL: $COVERITY_URL
    BRIDGE_COVERITY_CONNECT_USER_NAME: $COVERITY_USER
    BRIDGE_COVERITY_CONNECT_USER_PASSWORD: $COVERITY_PASSWORD
    BRIDGE_COVERITY_CONNECT_PROJECT_NAME: $CI_PROJECT_NAME
    
    ### Uncomment to specify the directory to scan. Default value is repository root
    # BRIDGE_PROJECT_DIRECTORY: $PROJECT_DIRECTORY
    
    ### Uncomment below to add arbitrary CL parameters
    # BRIDGE_COVERITY_BUILD_COMMAND: 'mvn clean install'
    # BRIDGE_COVERITY_CLEAN_COMMAND: 'mvn clean'
    # BRIDGE_COVERITY_CONFIG_PATH: '/USERS/USER/coverity.yml'
    # BRIDGE_COVERITY_ARGS: '-c /USERS/USER/coverity.yml -o capture.build.clean-command="mvn clean" -- mvn clean install'
    
    ### Enable bridge-cli diagnostics
    # INCLUDE_DIAGNOSTICS: 'true'
  
    ### To enable the use of self-signed certificates
    # BRIDGE_NETWORK_SSL_TRUSTALL: true
    # BRIDGE_NETWORK_SSL_CERT_FILE: '/Users/Config/cert.pem'

    ### Mark build status if policy violating issues are found
    #MARK_BUILD_STATUS: 'success'

  rules:
    - if: ($CI_COMMIT_BRANCH =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event')
      variables:
        BRIDGE_COVERITY_CONNECT_STREAM_NAME: $CI_PROJECT_NAME-$CI_COMMIT_BRANCH
        BRIDGE_COVERITY_CONNECT_POLICY_VIEW: 'Outstanding Issues'
        #BRIDGE_COVERITY_WAITFORSCAN: 'false'   # Used to support the async mode
        
    ### Coverity PR Scan       
    - if: ($CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event')
      variables:
        BRIDGE_COVERITY_CONNECT_STREAM_NAME: $CI_PROJECT_NAME-$CI_MERGE_REQUEST_TARGET_BRANCH_NAME
        
        ### Pull Request Comments
        #BRIDGE_COVERITY_PRCOMMENT_ENABLED: 'true'
        ## Use the parameter below to add comments for issues filtered 
        ## by impact. Default is High if unset
        ## NOTE: Issues matching BRIDGE_COVERITY_CONNECT_POLICY_VIEW are ignored if set
        #BRIDGE_COVERITY_PRCOMMENT_IMPACTS: 'High,Medium,Low,Audit'
        #BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN # Mandatory when BRIDGE_COVERITY_AUTOMATION_PRCOMMENT is set to 'true'

  tags: 
    - linux # Name of your Gitlab runner
  extends: .run-black-duck-tools # Used for bash.        
  #extends: .run-black-duck-tools-powershell # Used for powershell
  artifacts:
    when: always
    paths:
      - .bridge # Used when INCLUDE_DIAGNOSTICS is enabled and BRIDGE_BLACKDUCK_REPORTS_SARIF_CREATE is enabled

  ### Uncomment below configuration to add custom logic based on return status
  #after_script : |
  #  echo "Coverity Scan exit status - $status"
```

Table 1. **List of mandatory and optional parameters for Coverity cloud**

| Input Parameter | Description | Mandatory/Optional |
| --- | --- | --- |
| `BRIDGE_COVERITY_PRCOMMENT_ENABLED` | Option to enable automatic creation pull request comments for new issues found in the pull request.    Baseline full scan results must exist on the server for this feature to work.    **Note**: The merge request from the feature branch to the main branch must exist for this feature to work.    **Default**: false   **Note**: When both `BRIDGE_COVERITY_PRCOMMENT_ENABLED` and `BRIDGE_COVERITY_CONNECT_POLICY_VIEW` are configured for a Coverity PR scan, the `BRIDGE_COVERITY_CONNECT_POLICY_VIEW` setting will be ignored, and PR comments will be generated only for new issues that match the specified impact filter (`BRIDGE_COVERITY_PRCOMMENT_IMPACTS`).  Further details can be found here.   Replaces deprecated `BRIDGE_COVERITY_AUTOMATION_PRCOMMENT` parameter. | Optional |
| `BRIDGE_COVERITY_PRCOMMENT_IMPACTS` | Comma-separated list of impacts that will cause Pull Request scans to fail.  Issues detected in the Pull Request that match any of the listed impact levels will be uploaded to Coverity, added as Pull Request comments and trigger build failure.  Valid impacts are: `High`, `Medium`, `Low` and `Audit`.  **Default**: `High` | Optional |
| `BRIDGE_COVERITY_INSTALL_DIRECTORY` | Installation directory of Coverity | Optional |
| `BRIDGE_COVERITY_CONNECT_POLICY_VIEW` | ID or name of policy view to be used to enforce the “break the build” policy.  If issues are found in the specified this view, build will be failed.  Example: `coverity_policy_view: '100001'` or `coverity_policy_view: 'Outstanding Issues'` | Optional |
| `BRIDGE_COVERITY_CONNECT_PROJECT_NAME` | Project name in CoverityThe Default value is `$CI_PROJECT_NAME` | Optional |
| `BRIDGE_COVERITY_CONNECT_STREAM_NAME` | Stream name in Coverity. The Default value for PR context is $`CI_PROJECT_NAME-$CI_MERGE_REQUEST_TARGET_BRANCH_NAME`The Default value for NON PR context is `$CI_PROJECT_NAME-$CI_COMMIT_BRANCH` | Optional |
| `BRIDGE_COVERITY_CONNECT_URL` | Coverity server URL | Mandatory |
| `BRIDGE_COVERITY_CONNECT_USER_NAME` | Coverity username | Mandatory |
| `BRIDGE_COVERITY_CONNECT_USER_PASSWORD` | Coverity passphrase | Mandatory |
| `BRIDGE_COVERITY_LOCAL` | Set to `false` if using Coverity cloud deployment. Black Duck Security Template will install Coverity Thin Client as necessary.  Set to true if you are using on-prem Coverity Connect. When set to `true`, Black Duck Security Template will install Coverity Analysis on the local system in order to execute the scan.  Note: You can use an existing installation of Coverity tools by setting the `coverity_install_directory` option.  Default is `false`.  Usage example: `BRIDGE_COVERITY_LOCAL: true` | Optional |
| `BRIDGE_COVERITY_VERSION` | The version of Coverity that Bridge should use. | Optional |
| `BRIDGE_GITLAB_USER_TOKEN` | Gitlab User Access Token  Example: `BRIDGE_GITLAB_USER_TOKEN: $GITLAB_USER_TOKEN` | Mandatory when `BRIDGE_COVERITY_AUTOMATION_PRCOMMENT` is set as `true`. |
| `BRIDGE_PROJECT_DIRECTORY` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `BRIDGE_COVERITY_BUILD_COMMAND` | Build command for Coverity. | Optional |
| `BRIDGE_COVERITY_CLEAN_COMMAND` | Clean command for Coverity. | Optional |
| `BRIDGE_COVERITY_CONFIG_PATH` | Coverity config file path location. | Optional |
| `BRIDGE_COVERITY_ARGS` | Additional arguments for Coverity. | Optional |
| `BRIDGE_COVERITY_WAITFORSCAN` | Specifies if the workflow should wait for the analysis to complete.  **Default** : `true`  If set to false, post scan workflows like PR comment, Fix PR, SARIF etc. will not be applicable. | Optional |

Table 2. List of network parameters

| **Input Parameter** | **Description** | **Mandatory/Optional** |
| --- | --- | --- |
| `BRIDGE_NETWORK_SSL_TRUSTALL` | Disables SSL certificate verification. Use with caution.  **Default**: false | Optional |
| `BRIDGE_NETWORK_SSL_CERT_FILE` | File path to configure the HTTPS calls to accept a self-signed certificate. Note: If you use the network parameter `BRIDGE_NETWORK_SSL_CERT_FILE`, you should run the agent in administrator mode | Optional |

- `BRIDGE_NETWORK_SSL_TRUSTALL` and `BRIDGE_NETWORK_SSL_CERT_FILE` cannot both be specified at the same time.
