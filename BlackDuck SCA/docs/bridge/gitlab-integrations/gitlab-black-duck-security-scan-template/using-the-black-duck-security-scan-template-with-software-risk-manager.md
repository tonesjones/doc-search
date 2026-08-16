---
title: "Using the Black Duck Security Scan Template with Software Risk Manager"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-template-with-software-risk-manager.html"
content_id: "sOLCcTu0DQmnYQnzok7Zag"
version: "latest"
section: "GitLab Integrations"
scraped_at: "2026-08-08T23:48:10.386197+00:00"
---

# Using the Black Duck Security Scan Template with Software Risk Manager

As a Software Risk Manager (SRM) customer, you can use Black Duck Security Scan Template to automate SCA and SAST scanning in your CI pipeline.

To use Black Duck Security Scan Template with SRM, add .gitlab-ci.yml to your project using an include entry as shown in the examples below.

Simplified example

```
include:
  - project: blackduck-inc/black-duck-security-scan
    ref: v2
    file: templates/security_scan.yml
  ### Configuration for accessing blackduck-security-scan in Gitlab self-managed
  # - remote: 'https://gitlab.com/blackduck-inc/black-duck-security-scan/-/raw/main/templates/security_scan.yml'
stages:
  - srm_scan
variables:
  SCAN_BRANCHES: "/^(main|master|develop|stage|release|feature_branch)$/" # Branches to run scan
blackduck_template_execution:
  stage: srm_scan
  extends: .run-black-duck-tools # Used for bash.        
  #extends: .run-black-duck-tools-powershell # Used for powershell
  tags:
    - linux
  rules: # For push and merge request events
    - if: (($CI_COMMIT_BRANCH =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE != 'merge_request_event') ||
 ( $CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ $SCAN_BRANCHES && $CI_PIPELINE_SOURCE == 'merge_request_event') )
      when: always
  variables:
    BRIDGE_SRM_URL: $SRM_URL
    BRIDGE_SRM_APIKEY: $SRM_APIKEY
    BRIDGE_SRM_ASSESSMENT_TYPES: "SCA,SAST"
    
    ##Enable Bridge diagnostics
    # INCLUDE_DIAGNOSTICS: 'true'

  artifacts:
    when: always
    paths:
    - .bridge # Used when INCLUDE_DIAGNOSTICS is enabled
```

Detailed example

```
include:
  - project: blackduck-inc/black-duck-security-scan
    ref: v2
    file: templates/security_scan.yml
  ### Configuration for accessing blackduck-security-scan in Gitlab self-managed
  # - remote: 'https://gitlab.com/blackduck-inc/black-duck-security-scan/-/raw/main/templates/security_scan.yml' 

stages:
  - srm_scan

variables:
  SCAN_BRANCHES: "/^(main|master|develop|stage|release|feature_branch)$/" # Add branches where you want to run Coverity scan

blackduck_template_execution:
  stage: srm_scan
  variables:
    BRIDGE_SRM_URL: $SRM_URL
    BRIDGE_SRM_APIKEY: $SRM_APIKEY
    BRIDGE_SRM_ASSESSMENT_TYPES: "SCA,SAST"
    BRIDGE_SRM_PROJECT_NAME: $CI_PROJECT_NAME
    ## Project id in SRM Server
    ### Uncomment below configuration if SRM_PROJECT_NAME didn't specified
    #BRIDGE_SRM_PROJECT_ID: $SRM_PROJECT_ID

    #BRIDGE_SRM_WAITFORSCAN: 'false'   # Used to support the async mode
    
    ## Branch name in the SRM Server
    BRIDGE_SRM_BRANCH_NAME: $SRM_BRANCH_NAME
    ## Parent Branch name in SRM server
    BRIDGE_SRM_BRANCH_PARENT: $SRM_BRANCH_PARENT
    ## Path to Coverity CLI
    BRIDGE_COVERITY_EXECUTION_PATH: "/Users/johndoe/bridge-install-dir/srm-coverity/cov-thin-client-macosx-2023.6.1/bin/coverity"
    ## Path to the Black Duck Detect jar file to use
    BRIDGE_DETECT_EXECUTION_PATH: "/Users/johndoe/bridge-install-dir/srm-blackduck/tools/blackduck-detect/10.0.0/detect-10.0.0.jar"
    ## Uncomment to specify the directory to scan. Default value is repository root
    # BRIDGE_PROJECT_DIRECTORY: $PROJECT_DIRECTORY
        
    ### Uncomment below to add arbitrary CL parameters       
    # BRIDGE_COVERITY_BUILD_COMMAND: 'mvn clean install'
    # BRIDGE_COVERITY_CLEAN_COMMAND: 'mvn clean'
    # BRIDGE_COVERITY_CONFIG_PATH: '/USERS/USER/coverity.yml'
    # BRIDGE_COVERITY_ARGS: '-c /USERS/USER/coverity.yml -o capture.build.clean-command="mvn clean" -- mvn clean install'    
    # BRIDGE_DETECT_SEARCH_DEPTH: 1
    # BRIDGE_DETECT_CONFIG_PATH: '/USERS/USER/application.properties'
    # BRIDGE_DETECT_ARGS: '--detect.diagnostic=true'
    
    ## Enable Bridge diagnostics
    # INCLUDE_DIAGNOSTICS: 'true'

  tags: 
    - linux # Name of your Gitlab runner
  extends: .run-black-duck-tools # Used for bash.        
  #extends: .run-black-duck-tools-powershell # Used for powershell
  artifacts:
    when: always
    paths:
      - .bridge # Used when INCLUDE_DIAGNOSTICS is enabled
```

Table 1. **List of mandatory and optional parameters for SRM**

| Input Parameter | Description | Mandatory/Optional |
| --- | --- | --- |
| `BRIDGE_SRM_URL` | SRM Server URL | Mandatory |
| `BRIDGE_SRM_APIKEY` | SRM API KEY | Mandatory |
| `BRIDGE_SRM_ASSESSMENT_TYPES` | SRM Assessment Types separated by comma. Accepted values: `SAST` or `SCA` or `SAST, SCA` | Mandatory |
| `BRIDGE_SRM_PROJECT_NAME` | Project name in SRM Server. The Default Value is `$CI_PROJECT_NAME` | Optional |
| `BRIDGE_SRM_PROJECT_ID` | Project id in SRM Server | Optional |
| `BRIDGE_SRM_BRANCH_NAME` | Branch name on the SRM Server. The branch is created if it doesn't already exist If a new branch name is passed to `BRIDGE_SRM_BRANCH_NAME` parameter, `BRIDGE_SRM_BRANCH_PARENT` should also be passed. otherwise error message will be displayed to the user.  If an existing branch name is passed to `BRIDGE_SRM_BRANCH_NAME` parameter, `BRIDGE_SRM_BRANCH_PARENT` is not required. | Optional |
| `BRIDGE_SRM_BRANCH_PARENT` | Parent Branch name in SRM server | Optional |
| `BRIDGE_COVERITY_EXECUTION_PATH` | Path to Coverity CLI | Optional |
| `BRIDGE_DETECT_EXECUTION_PATH` | Path to the Black Duck Detect jar file to use | Optional |
| `BRIDGE_PROJECT_DIRECTORY` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `BRIDGE_SRM_WAITFORSCAN` | Specifies if the workflow should wait for the analysis to complete.  **Default** : `true`  If set to false, post scan workflows like PR comment, Fix PR, SARIF etc. will not be applicable. | Optional |
