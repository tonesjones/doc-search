---
title: "Using the Black Duck Security Scan Pipe with Black Duck SCA"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-pipe-with-black-duck-sca.html"
content_id: "lGjG8IIJi6zlaZGr81COtw"
version: "latest"
section: "Bitbucket Integrations"
scraped_at: "2026-08-08T23:49:03.912093+00:00"
---

# Using the Black Duck Security Scan Pipe with Black Duck SCA

As a Bitbucket Pipe user, you can use Bridge CLI to automate Black Duck SCA scanning in your CI pipeline. You can use Bridge CLI with Black Duck SCA in the following ways:

- Automate SCA scans
- Add pull-request comments to Bitbucket
- Export SARIF files

**Before running a pipe with the Black Duck Security Scan Pipe, please read the Black Duck documentation on Bitbucket prerequisites.**

For an overview about using PR Comments, please see the following documentation page: Pull request (PR) comments

After completing the prerequisites, you may add the following code blocks to your `bitbucket-pipelines.yml`, and then run your pipe. A list of mandatory and optional parameters is provided below the code examples.

- Simplified example:

  ```
  security-scan: &blackduck-security-scan
      step:
          name: Black Duck Security Scan
          script:
              - pipe: blackduck-inc/blackduck-security-scan:1.6.0
                variables:
                    BRIDGE_BLACKDUCKSCA_URL: $BRIDGE_BLACKDUCKSCA_URL
                    BRIDGE_BLACKDUCKSCA_TOKEN: $BRIDGE_BLACKDUCKSCA_TOKEN

                    ## Mandatory when BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT or BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED or BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE is set true.
                    # BRIDGE_BITBUCKET_API_TOKEN: $BITBUCKET_REPO_ACCESS_TOKEN

                    ## Pull Request Comments
                    # BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT: 'true'

                    ## Fix Pull Request Creation
                    # BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED: 'true'

                    ## SARIF Report Generation
                    # BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE: 'true'

                    ### To enable the use of self-signed certificates
                    # BRIDGE_NETWORK_SSL_TRUSTALL: true

                    ## Mark build status if policy violating issues are found
                    # MARK_BUILD_STATUS: 'success'

      ### Use below configuration for uploading artifacts if INCLUDE_DIAGNOSTICS or BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE is enabled    
      artifacts:
          - '.blackduck/integrations/blackducksca/sarif/report.sarif.json' # Used when BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE is enabled
          - '.bridge/**' # Used when INCLUDE_DIAGNOSTICS is enabled

  pipelines:
      pull-requests:
          '**': # Matches all pull requests
              - <<: *blackduck-security-scan
      branches:
          '{main,master,develop,stage,release}':
              - <<: *blackduck-security-scan
  ```
- Detailed example:

  ```
  pipelines:
      pull-requests:
          '**':
            - step:
                  #runs-on: # Use this to specify self-hosted runners
                  # - linux # Name of your Bitbucket runner
                  script:
                    - pipe: blackduck-inc/blackduck-security-scan:1.6.0
                      variables:
                        BRIDGE_BLACKDUCKSCA_URL: $BRIDGE_BLACKDUCKSCA_URL
                        BRIDGE_BLACKDUCKSCA_TOKEN: $BRIDGE_BLACKDUCKSCA_TOKEN
                      
                        ## Use below configuration to set specific detect environment variables
                        DETECT_PROJECT_NAME: $DETECT_PROJECT_NAME
                      
                        ## Use below configuration to run Black Duck PR scan
                        BRIDGE_BLACKDUCKSCA_SCAN_FULL: 'false'
                        BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT: 'true'
                        BRIDGE_BITBUCKET_API_TOKEN: $BRIDGE_BITBUCKET_API_TOKEN
                        ### BRIDGE_BITBUCKET_API_USER_NAME is required if App Password is set as BRIDGE_BITBUCKET_API_TOKEN
                        # BRIDGE_BITBUCKET_API_USER_NAME: $BRIDGE_BITBUCKET_API_USER_NAME

                        ## Enable Bridge-CLI diagnostics
                        INCLUDE_DIAGNOSTICS: 'true'
                      
                        ### To enable the use of self-signed certificates
                        # BRIDGE_NETWORK_SSL_TRUSTALL: true
                              
                        ## Mark build status if policy violating issues are found
                        # MARK_BUILD_STATUS: 'success'

                        ## Use custom image to configure paths and tools     
                        # CUSTOM_IMAGE: 'user/custom-blackduck-security-scan:maven'
                        ## Use below parameters to authenticate private custom docker image
                        # DOCKER_USERNAME: $DOCKER_USERNAME
                        # DOCKER_PASSWORD: $DOCKER_PASSWORD # Supports Password and Personal Access Token
                        ## Use this if the private docker image is hosted in internal docker registry
                        # DOCKER_REGISTRY: $DOCKER_REGISTRY

                        # NETWORK_AIRGAP: true
                        # BRIDGECLI_INSTALL_DIRECTORY:'/usr/local/bridge-cli-bundle'

                        ## Uncomment to specify the directory to scan. Default value is repository root
                        # BRIDGE_PROJECT_DIRECTORY: '/usr/local/my-project'                

                        ## Detect Tool Settings
                        # BRIDGE_DETECT_INSTALL_DIRECTORY: '/usr/local/detect'
                        # BRIDGE_DETECT_SEARCH_DEPTH: 2
                        # BRIDGE_DETECT_ARGS: '--detect.diagnostic=true'
                        # BRIDGE_DETECT_CONFIG_PATH: '/usr/local/config/application.properties'

                  ### Use below configuration for uploading artifacts if INCLUDE_DIAGNOSTICS is enabled    
                  artifacts:
                    - '.bridge/**'

      branches:
          '{main,master,develop,stage,release}':
            - step:
                  #runs-on: # Use this to specify self-hosted runners
                  # - linux # Name of your Bitbucket runner
                  script:
                    - pipe: blackduck-inc/blackduck-security-scan:1.6.0
                      variables:
                        BRIDGE_BLACKDUCKSCA_URL: $BRIDGE_BLACKDUCKSCA_URL
                        BRIDGE_BLACKDUCKSCA_TOKEN: $BRIDGE_BLACKDUCKSCA_TOKEN
                      
                        ## Use below configuration to set specific detect environment variables
                        DETECT_PROJECT_NAME: $DETECT_PROJECT_NAME
                      
                        BRIDGE_BLACKDUCKSCA_SCAN_FULL: 'true'
                        BRIDGE_BLACKDUCKSCA_SCAN_FAILURE_SEVERITIES: 'BLOCKER,CRITICAL'
                        # BRIDGE_BLACKDUCKSCA_WAITFORSCAN: 'false'   # Used to support the async mode

                        ## FIX PULL REQUEST CREATION
                        BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED: 'true'
                        BRIDGE_BLACKDUCKSCA_FIXPR_MAXCOUNT: 5
                        BRIDGE_BLACKDUCKSCA_FIXPR_FILTER_SEVERITIES: 'CRITICAL,HIGH'
                        BRIDGE_BLACKDUCKSCA_FIXPR_USEUPGRADEGUIDANCE: 'LONG_TERM,SHORT_TERM'
                        BRIDGE_BITBUCKET_API_TOKEN: $BRIDGE_BITBUCKET_API_TOKEN # Mandatory when BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED is set to 'true'
                        ### BRIDGE_BITBUCKET_API_USER_NAME is required if App Password is set as BRIDGE_BITBUCKET_API_TOKEN
                        # BRIDGE_BITBUCKET_API_USER_NAME: $BRIDGE_BITBUCKET_API_USER_NAME

                        ## SARIF Report Generation
                        BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE: 'true'
                        BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_FILE_PATH: '/usr/local/report/report.sarif.json'
                        BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_SEVERITIES: 'CRITICAL,HIGH'
                        BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_GROUPSCAISSUES: 'true'
                      
                        ## Enable Bridge-CLI diagnostics
                        INCLUDE_DIAGNOSTICS: 'true'
                      
                        ### To enable the use of self-signed certificates
                        # BRIDGE_NETWORK_SSL_TRUSTALL: true
                              
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

                        ## Detect Tool Settings
                        # BRIDGE_DETECT_INSTALL_DIRECTORY: '/usr/local/detect'
                        # BRIDGE_DETECT_SEARCH_DEPTH: 2
                        # BRIDGE_DETECT_ARGS: '--detect.diagnostic=true'
                        # BRIDGE_DETECT_CONFIG_PATH: '/usr/local/config/application.properties'

                  ### Use below configuration for uploading artifacts if INCLUDE_DIAGNOSTICS or BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE is enabled    
                  artifacts:
                    - '/usr/local/report/report.sarif.json' # Used when BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE is enabled
                    - '.bridge/**' # Used when INCLUDE_DIAGNOSTICS is enabled
  ```

Table 1. List of mandatory and optional parameters for Black Duck SCA

| **Input Parameter** | Description | **Mandatory / Optional** |
| --- | --- | --- |
| `BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT` | Option to enable automatic creation of pull request comments for new issues found in the pull request.  Note: The merge request from the feature branch to the main branch must exist for this feature to work.  **Default:** `false` | Optional |
| `BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED` | Enables or disables the automated creation of fix pull request for Black Duck SCA.  **Default:** `false` | Optional |
| `BRIDGE_BLACKDUCKSCA_FIXPR_FILTER_SEVERITIES` | Creates Fix PRs only for issues with the severity level specified. If the value is `'HIGH'`, only issues with that severity will have Fix PRs. The value is a comma-separated list.  Supported severities: `'CRITICAL'`, `'HIGH'`, `'MEDIUM'`, `'LOW'`  **Deafult:** `'CRITICAL,HIGH'` | Optional |
| `BRIDGE_BLACKDUCKSCA_FIXPR_MAXCOUNT` | Maximum number of pull requests allowed on a branch when policies are violated. A PR is created for each vulnerable component. | Optional |
| `BRIDGE_BLACKDUCKSCA_FIXPR_USEUPGRADEGUIDANCE` | Black Duck SCA Hub upgrade guidance values.  **Default:** `'SHORT_TERM,LONG_TERM'` | Optional |
| `BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE` | Set this to `true` to generate SARIF report.  **Default:** `false`  Note: SARIF reports can be generated for any configured branch; however, report generation is not supported in a merge request context. | Optional |
| `BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_FILE_PATH` | File path (including file name) where SARIF report is created. Only `.sarif` or `.sarif.json` files will be uploaded. All other formats are excluded.  **Default:** `.blackduck/integrations/blackducksca/sarif/report.sarif.json` | Optional |
| `BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_GROUPSCAISSUES` | When set to `true`, SCA issues are grouped by component. Set this to `false` to list SCA issues by vulnerability.  **Default:** `true` | Optional |
| `BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_SEVERITIES` | Comma-separated list of SAST/SCA issue severities to include in SARIF file report. Valid severities are `Critical`, `High`, `Medium`, `Low`, and `Informational`.  **Default:** All severities are included. | Optional |
| `BRIDGE_BLACKDUCKSCA_SCAN_FAILURE_SEVERITIES` | Black Duck SCA scan failure severities used to decide if build should be broken.  Supported values: `ALL`, `NONE`, `BLOCKER`, `CRITICAL`, `MAJOR`, `MINOR`, `OK`, `TRIVIAL`, `UNSPECIFIED` | Optional |
| `BRIDGE_BLACKDUCKSCA_SCAN_FULL` | Specifies whether full scan is required or not.  Must be set to `true` for push events and `false` for pull request events.  **Default:** `false` | Optional |
| `BRIDGE_BLACKDUCKSCA_TOKEN` | Black Duck SCA API token | Mandatory |
| `BRIDGE_BLACKDUCKSCA_URL` | Black Duck SCA server URL | Mandatory |
| `BRIDGE_BITBUCKET_API_TOKEN` | Bitbucket User Access Token  Example: `BRIDGE_BITBUCKET_API_TOKEN: $BRIDGE_BITBUCKET_API_TOKEN` | Mandatory when `BRIDGE_BLACKDUCKSCA_AUTOMATION_PRCOMMENT` or `BRIDGE_BLACKDUCKSCA_FIXPR_ENABLED` is set as `true`. |
| `BRIDGE_BITBUCKET_API_USER_NAME` | Specify your Bitbucket User Name to use features like PR Comments, SARIF upload and diagnostics upload. This works in conjunction with your Bitbucket API token. | Mandatory when `BRIDGE_POLARIS_PRCOMMENT_ENABLED` is set as `true`. |
| `BRIDGE_PROJECT_DIRECTORY` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `BRIDGE_DETECT_INSTALL_DIRECTORY` | Installation directory for Detect. This should be a valid empty directory. | Optional |
| `BRIDGE_DETECT_CONFIG_PATH` | Detect config file path location. | Optional |
| `BRIDGE_DETECT_SEARCH_DEPTH` | Number indicating the search depth in the source directory. | Optional |
| `BRIDGE_DETECT_ARGS` | Additional arguments for Detect. | Optional |
| `BRIDGE_BLACKDUCKSCA_WAITFORSCAN` | Specifies if the workflow should wait for the analysis to complete.  **Default:** `true`  If set to `false`, post scan workflows like PR comment, Fix PR, SARIF etc will not be applicable. | Optional |

Note: Detect specific options can be passed through Detect environment variables.

Table 2. List of network parameters

| **Input Parameter** | **Description** | **Mandatory / Optional** |
| --- | --- | --- |
| `BRIDGE_NETWORK_SSL_TRUSTALL` | Disables SSL certificate verification. Use with caution.  **Default**: false | Optional |
