---
title: "Using Black Duck Security Scan Pipe for Software Risk Manager"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-black-duck-security-scan-pipe-for-software-risk-manager.html"
content_id: "aFejma_DnSfQITYn34Up8w"
version: "latest"
section: "Bitbucket Integrations"
scraped_at: "2026-08-08T23:49:02.496365+00:00"
---

# Using Black Duck Security Scan Pipe for Software Risk Manager

As a Bitbucket Pipe user, you can use Bridge CLI to automate Software Risk Manager (SRM)
scanning in your CI pipeline. You can use Bridge CLI with SRM in the following ways:

- Automate SCA scans
- Automate SAST scans

**Before running a pipe with the Black Duck Security Scan Pipe, please read the Black Duck documentation on Bitbucket
prerequisites.**

After completing the prerequisites, you may add the following code blocks to your `bitbucket-pipelines.yml`, and then run your pipe.
A list of mandatory and optional parameters is provided below the code examples.

- Simplified example:

  ```
  security-scan: &blackduck-security-scan
      step:
          name: Black Duck Security Scan
          script:
              - pipe: blackduck-inc/blackduck-security-scan:1.6.0
          variables:
                      BRIDGE_SRM_URL: $SRM_URL
                      BRIDGE_SRM_APIKEY: $SRM_APIKEY
                      BRIDGE_SRM_ASSESSMENT_TYPES: 'SCA,SAST'
      
                      ### Mark build status if policy violating issues are found
                      # MARK_BUILD_STATUS: 'success'
                      
          ### Use below configuration for uploading artifacts if INCLUDE_DIAGNOSTICS is enabled
          artifacts:
              - '.bridge/**'
      
  pipelines:
      pull-requests:
          '**':  # Matches all pull requests
          - <<: *blackduck-security-scan
      branches:
          '{main,master,develop,stage,release}':
          - <<: *blackduck-security-scan
  ```
- Detailed example:

  ```
  pipelines:           
      branches:
          '{main,master,develop,stage,release}':
              - step:
                  #runs-on: # Use this to specify self-hosted runners
                  # - linux # Name of your Bitbucket runner
                  script:
                      - pipe: blackduck-inc/blackduck-security-scan:1.6.0
                  variables:
                              BRIDGE_SRM_URL: $SRM_URL
                              BRIDGE_SRM_APIKEY: $SRM_APIKEY
                              BRIDGE_SRM_ASSESSMENT_TYPES: 'SCA,SAST'
      
                              BRIDGE_SRM_PROJECT_NAME: $BITBUCKET_REPO_SLUG
                              ## Project id in SRM Server 
                              ### Uncomment below configuration if SRM_PROJECT_NAME didn't specified
                              # BRIDGE_SRM_PROJECT_ID: $SRM_PROJECT_ID
      
                              ## Branch name in the SRM Server
                              BRIDGE_SRM_BRANCH_NAME: $SRM_BRANCH_NAME
                              ## Parent Branch name in SRM server
                              BRIDGE_SRM_BRANCH_PARENT: $SRM_BRANCH_PARENT
      
                              ## Enable Bridge diagnostics
                              # INCLUDE_DIAGNOSTICS: 'true'
      
                              ## Mark build status if policy violating issues are found
                              # MARK_BUILD_STATUS: 'success'
      
                              ## Use custom image to configure paths and tools     
                              # CUSTOM_IMAGE: 'user/custom-blackduck-security-scan:maven'
                              ## Use below parameters to authenticate private custom docker image
                              # DOCKER_USERNAME: $DOCKER_USERNAME
                              # DOCKER_PASSWORD: $DOCKER_PASSWORD # Supports Password and Personal Access Token
                              ## Use this if the private docker image is hosted in internal docker registry
                              # DOCKER_REGISTRY: $DOCKER_REGISTRY
      
                              ## Uncomment to specify the directory to scan. Default value is repository root
                              # BRIDGE_PROJECT_DIRECTORY: '/usr/local/my-project'
      
                              # NETWORK_AIRGAP: true
                              # BRIDGECLI_INSTALL_DIRECTORY:'/usr/local/bridge-cli-bundle'
      
                              ## Path to Coverity CLI
                              # BRIDGE_DETECT_EXECUTION_PATH: '/usr/local/cov-thin-client/2024.12.0/coverity'
                              ## Path to the Black Duck Detect jar file to use
                              # BRIDGE_DETECT_EXECUTION_PATH: '/usr/local/detect/10.1.0/detect.jar'
      
                              ## Coverity (SAST) Tools Settings
                              # BRIDGE_COVERITY_CLEAN_COMMAND: 'mvn clean'
                              # BRIDGE_COVERITY_BUILD_COMMAND: 'mvn clean install'
                              # BRIDGE_COVERITY_CONFIG_PATH: '/usr/local/config/coverity.yml'
                              # BRIDGE_COVERITY_ARGS: '-c /usr/local/config/coverity.yml -o capture.build.clean-command="mvn clean" -- mvn clean install'
      
                              ## Detect Tool Settings
                              # BRIDGE_DETECT_SEARCH_DEPTH: 2
                              # BRIDGE_DETECT_ARGS: '--detect.diagnostic=true'
                              # BRIDGE_DETECT_CONFIG_PATH: '/usr/local/config/application.properties'
                              
              ### Use below configuration for uploading artifacts if INCLUDE_DIAGNOSTICS is enabled
              artifacts:
                  - '.bridge/**'
  ```

**List of mandatory and optional parameters for SRM**

Table 1. List of mandatory and optional parameters for SRM

| **Input parameter** | Description | **Mandatory / optional** |
| --- | --- | --- |
| `BRIDGE_SRM_URL` | SRM Server URL | Mandatory |
| `BRIDGE_SRM_APIKEY` | SRM API key | Mandatory |
| `BRIDGE_SRM_ASSESSMENT_TYPES` | SRM Assessment Types separated by comma. Accepted values: `SAST` or `SCA` or `SAST, SCA` | Mandatory |
| `BRIDGE_SRM_PROJECT_NAME` | Project name in SRM Server. The Default Value is `$BITBUCKET_REPO_SLUG` | Optional |
| `BRIDGE_SRM_PROJECT_ID` | Project id in SRM Server | Optional |
| `BRIDGE_SRM_BRANCH_NAME` | Branch name on the SRM Server. The branch is created if it doesn't already exist  If a new branch name is passed to the `BRIDGE_SRM_BRANCH_NAME` parameter, `BRIDGE_SRM_BRANCH_PARENT` should also be passed. Otherwise an error message will be displayed to the user.  If an existing branch name is passed to the `BRIDGE_SRM_BRANCH_NAME` parameter, `BRIDGE_SRM_BRANCH_PARENT` is not required. | Optional |
| `BRIDGE_SRM_BRANCH_PARENT` | Parent Branch name on the SRM server. | Optional |
| `BRIDGE_COVERITY_EXECUTION_PATH` | Path to the Coverity CLI. | Optional |
| `BRIDGE_DETECT_EXECUTION_PATH` | Path to the Detect jar file. | Optional |
| `BRIDGE_PROJECT_DIRECTORY` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `BRIDGE_SRM_WAITFORSCAN` | Specifies whether or not the workflow should wait for the analysis to complete.  **Default:** `true`  If set to `false`, post scan workflows like PR comment, Fix PR, SARIF etc. will not be applicable. | Optional |
