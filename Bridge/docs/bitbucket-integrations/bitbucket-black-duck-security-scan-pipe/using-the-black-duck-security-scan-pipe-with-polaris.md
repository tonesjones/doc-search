---
title: "Using the Black Duck Security Scan Pipe with Polaris"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-the-black-duck-security-scan-pipe-with-polaris.html"
content_id: "RRTcCxjLsVQRPmCI1qrONQ"
version: "latest"
section: "Bitbucket Integrations"
scraped_at: "2026-08-08T23:49:00.914442+00:00"
---

# Using the Black Duck Security Scan Pipe with Polaris

As a Bitbucket Pipe user, you can use Bridge CLI to automate Polaris scanning in your CI pipeline. You can use Bridge CLI with Polaris in the following ways:

- Automate SCA scans
- Automate SAST scans
- Add Pull Request comments to Bitbucket
- Raise Fix Pull Requests for SCA vulnerabilities
- Export SARIF files

**Before running a pipe with the Black Duck Security Scan Pipe, please read the Black Duck documentation on Bitbucket prerequisites.**

Client scan tools can be configured using the Bridge CLI environment variables within the Black Duck Security Scan Pipe. For SAST scans the Coverity version can be selected using the `BRIDGE_COVERITY_VERSION` environment variable. Please refer to Complete List Of Bridge Commands for further details.

For an overview about using PR Comments, please see the following documentation page: Pull request (PR) comments

For an overview about Fix Pull Requests, please see the following documentation page: Fix pull requests (Fix PRs).

After completing the prerequisites, you may add the following code blocks to your `bitbucket-pipelines.yml`, and then run your pipe. A list of mandatory and optional parameters is provided below the code examples.

- Simplified example:

  ```
  security-scan: &blackduck-security-scan
      step:
          name: Black Duck Security Scan
          script:
            - pipe: blackduck-inc/blackduck-security-scan:1.6.0
          variables:
              BRIDGE_POLARIS_SERVERURL: $POLARIS_SERVERURL
              BRIDGE_POLARIS_ACCESSTOKEN: $POLARIS_ACCESSTOKEN
              BRIDGE_POLARIS_ASSESSMENT_TYPES: 'SCA,SAST'
              
              ## Mandatory when BRIDGE_POLARIS_PRCOMMENT_ENABLED, BRIDGE_POLARIS_FIXPR_ENABLED or BRIDGE_POLARIS_REPORTS_SARIF_CREATE is set true.
              # BRIDGE_BITBUCKET_API_TOKEN: $BITBUCKET_REPO_ACCESS_TOKEN

              ## Pull Request Comments
              # BRIDGE_POLARIS_PRCOMMENT_ENABLED: 'true'

              ## Fix Pull Request Creation
              # BRIDGE_POLARIS_FIXPR_ENABLED: 'true'

              ## SARIF report generation
              # BRIDGE_POLARIS_REPORTS_SARIF_CREATE: 'true'

              ## Uncomment below configuration for signature scan
              # BRIDGE_POLARIS_TEST_SCA_TYPE: 'SCA-SIGNATURE'

              ## Uncomment below configuration for sigma rapid scan
              # BRIDGE_POLARIS_TEST_SAST_TYPE: 'SAST_RAPID'
              
              ## Mark build status if policy violating issues are found
              # MARK_BUILD_STATUS: 'success'

          ### Use below configuration for uploading artifacts if INCLUDE_DIAGNOSTICS or BRIDGE_POLARIS_REPORTS_SARIF_CREATE is enabled    
          artifacts:
            - '.blackduck/integrations/polaris/sarif/report.sarif.json' # Used when BRIDGE_POLARIS_REPORTS_SARIF_CREATE is enabled
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
                  # runs-on: # Use this to specify self-hosted runners
                  #   - linux # Name of your Bitbucket runner
                  script:
                    - pipe: blackduck-inc/blackduck-security-scan:1.6.0
                      variables:
                        BRIDGE_POLARIS_SERVERURL: $BRIDGE_POLARIS_SERVERURL
                        BRIDGE_POLARIS_ACCESSTOKEN: $BRIDGE_POLARIS_ACCESSTOKEN
                        BRIDGE_POLARIS_ASSESSMENT_TYPES: 'SCA,SAST'
                        BRIDGE_POLARIS_APPLICATION_NAME: $BRIDGE_POLARIS_APPLICATION_NAME
                        BRIDGE_POLARIS_PROJECT_NAME: $BRIDGE_POLARIS_PROJECT_NAME
                        BRIDGE_POLARIS_BRANCH_NAME: $BRIDGE_POLARIS_BRANCH_NAME
                      
                        ### Enable Polaris PR scan
                        BRIDGE_POLARIS_PRCOMMENT_ENABLED: 'true'
                        BRIDGE_BITBUCKET_API_TOKEN: $BRIDGE_BITBUCKET_API_TOKEN
                        ### BRIDGE_BITBUCKET_API_USER_NAME is required if App Password is set as BRIDGE_BITBUCKET_API_TOKEN
                        # BRIDGE_BITBUCKET_API_USER_NAME: $BRIDGE_BITBUCKET_API_USER_NAME
                        BRIDGE_POLARIS_PRCOMMENT_SEVERITIES: 'CRITICAL,HIGH'
                      
                        # BRIDGE_POLARIS_WAITFORSCAN: 'false'   # Used to support the async mode

                        ### Signature scan
                        # BRIDGE_POLARIS_TEST_SCA_TYPE: 'SCA-SIGNATURE'

                        ### Sigma rapid scan
                        # BRIDGE_POLARIS_TEST_SAST_TYPE: 'SAST_RAPID'
                        
                        ### Uncomment this to use Source Upload method. Default value is hybrid (build based)
                        # BRIDGE_POLARIS_TEST_SAST_LOCATION: 'remote'
                        # BRIDGE_POLARIS_TEST_SCA_LOCATION: 'remote'
                        # BRIDGE_PROJECT_SOURCE_ARCHIVE: $PROJECT_ARCHIVE
                        # BRIDGE_PROJECT_SOURCE_EXCLUDES: $PROJECT_SOURCE_EXCLUDES
                        
                        #### Uncomment this to use Local Analysis feature
                        # Please use Local Analysis or Source Upload exclusively
                        # BRIDGE_POLARIS_TEST_SAST_LOCATION: 'local'
      
                        ### Enable Bridge CLI diagnostics
                        INCLUDE_DIAGNOSTICS: 'true'
                      
                        ### Mark build status if policy violating issues are found
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

                        ## Coverity (SAST) Tools Settings
                        # BRIDGE_COVERITY_CLEAN_COMMAND: 'mvn clean'
                        # BRIDGE_COVERITY_BUILD_COMMAND: 'mvn clean install'
                        # BRIDGE_COVERITY_CONFIG_PATH: '/usr/local/config/coverity.yml'
                        # BRIDGE_COVERITY_ARGS: '-c /usr/local/config/coverity.yml -o capture.build.clean-command="mvn clean" -- mvn clean install'
                        # BRIDGE_COVERITY_VERSION: '2025.9.0'

                        ## Detect Tool Settings
                        # BRIDGE_DETECT_SEARCH_DEPTH: 2
                        # BRIDGE_DETECT_ARGS: '--detect.diagnostic=true'
                        # BRIDGE_DETECT_CONFIG_PATH: '/usr/local/config/application.properties'

                  ### Use below configuration for uploading artifacts if INCLUDE_DIAGNOSTICS is enabled
                  artifacts:
                    - '.bridge/**'
   
      branches:
          '{main,master,develop,stage,release}':
            - step:
                  # runs-on: # Use this to specify self-hosted runners
                  #   - linux # Name of your Bitbucket runner
                  script:
                    - pipe: blackduck-inc/blackduck-security-scan:1.6.0
                      variables:
                        BRIDGE_POLARIS_SERVERURL: $BRIDGE_POLARIS_SERVERURL
                        BRIDGE_POLARIS_ACCESSTOKEN: $BRIDGE_POLARIS_ACCESSTOKEN
                        BRIDGE_POLARIS_ASSESSMENT_TYPES: 'SCA,SAST'
                        BRIDGE_POLARIS_APPLICATION_NAME: $BRIDGE_POLARIS_APPLICATION_NAME
                        BRIDGE_POLARIS_PROJECT_NAME: $BRIDGE_POLARIS_PROJECT_NAME
                        BRIDGE_POLARIS_BRANCH_NAME: $BRIDGE_POLARIS_BRANCH_NAME

                        ### Fix PR - generates automated fixable PRs 
                        BRIDGE_POLARIS_FIXPR_ENABLED: 'true'
                        BRIDGE_POLARIS_FIXPR_MAXCOUNT: '5'
                        BRIDGE_POLARIS_FIXPR_USEUPGRADEGUIDANCE: 'SHORT_TERM,LONG_TERM'
                        BRIDGE_POLARIS_FIXPR_FILTER_SEVERITIES: 'CRITICAL,HIGH'   
                        
  				   ### Upload Polaris SARIF report as job artifact
                        BRIDGE_POLARIS_REPORTS_SARIF_CREATE: 'true'
                        BRIDGE_POLARIS_REPORTS_SARIF_FILE_PATH: '/usr/local/report/report.sarif.json'
                        BRIDGE_POLARIS_REPORTS_SARIF_ISSUE_TYPES: 'SCA,SAST'
                        BRIDGE_POLARIS_REPORTS_SARIF_SEVERITIES: 'CRITICAL,HIGH'
                        BRIDGE_POLARIS_REPORTS_SARIF_GROUPSCAISSUES: 'true'
                      
                        # BRIDGE_POLARIS_WAITFORSCAN: 'false'   # Used to support the async mode

                        ### Signature scan
                        # BRIDGE_POLARIS_TEST_SCA_TYPE: 'SCA-SIGNATURE'

                        ### Sigma full scan
                        # BRIDGE_POLARIS_TEST_SAST_TYPE: 'SAST_FULL'
                        
                        ### Uncomment this to use Source Upload method. Default value is hybrid (build based)
                        # BRIDGE_POLARIS_TEST_SAST_LOCATION: 'remote'
                        # BRIDGE_POLARIS_TEST_SCA_LOCATION: 'remote'
                        # BRIDGE_PROJECT_SOURCE_ARCHIVE: $PROJECT_ARCHIVE
                        # BRIDGE_PROJECT_SOURCE_EXCLUDES: $PROJECT_SOURCE_EXCLUDES
                        
                        #### Uncomment this to use Local Analysis feature
                        # Please use Local Analysis or Source Upload exclusively
                        # BRIDGE_POLARIS_TEST_SAST_LOCATION: 'local'

                        ### Enable Bridge CLI diagnostics
                        # INCLUDE_DIAGNOSTICS: 'true'

                        ### BRIDGE_BITBUCKET_API_TOKEN is required to upload SARIF report and diagnostics in the Bitbucket downloads section, otherwise configure SARIF and diagnostics as artifacts in the bitbucket-pipelines.yml 
                        # BRIDGE_BITBUCKET_API_TOKEN: $BRIDGE_BITBUCKET_API_TOKEN
                        ### BRIDGE_BITBUCKET_API_USER_NAME is required if App Password is set as BRIDGE_BITBUCKET_API_TOKEN
                        # BRIDGE_BITBUCKET_API_USER_NAME: $BRIDGE_BITBUCKET_API_USER_NAME

                        ### Mark build status if policy violating issues are found
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

                        ## Polaris SCA Binary Scan
                        # BRIDGE_POLARIS_TEST_SCA_TYPE: 'SCA-BINARY'
                        # BRIDGE_POLARIS_ARTIFACTTOUPLOAD: '/path/to/artifact.zip'

                        ## Coverity (SAST) Tools Settings
                        # BRIDGE_COVERITY_CLEAN_COMMAND: 'mvn clean'
                        # BRIDGE_COVERITY_BUILD_COMMAND: 'mvn clean install'
                        # BRIDGE_COVERITY_CONFIG_PATH: '/usr/local/config/coverity.yml'
                        # BRIDGE_COVERITY_ARGS: '-c /usr/local/config/coverity.yml -o capture.build.clean-command="mvn clean" -- mvn clean install'
                        # BRIDGE_COVERITY_VERSION: '2025.9.0'

                        ## Detect Tool Settings
                        # BRIDGE_DETECT_SEARCH_DEPTH: 2
                        # BRIDGE_DETECT_ARGS: '--detect.diagnostic=true'
                        # BRIDGE_DETECT_CONFIG_PATH: '/usr/local/config/application.properties'

                  ### Use below configuration for uploading artifacts if INCLUDE_DIAGNOSTICS or BRIDGE_POLARIS_REPORTS_SARIF_CREATE is enabled    
                  artifacts:
                    - '/usr/local/report/report.sarif.json' # Used when BRIDGE_POLARIS_REPORTS_SARIF_CREATE is enabled
                    - '.bridge/**' # Used when INCLUDE_DIAGNOSTICS is enabled
  ```

**List of mandatory and optional parameters for Polaris**

Table 1. List of mandatory and optional parameters for Polaris

| **Input parameter** | Description | **Mandatory / optional** |
| --- | --- | --- |
| `BRIDGE_POLARIS_ACCESSTOKEN` | Polaris access token. You can use either a user access token (created in the Polaris UI) or a service account token here. | Mandatory |
| `BRIDGE_POLARIS_APPLICATION_NAME` | Application name in Polaris. The Default Value is `CI_PROJECT_NAME` | Optional |
| `BRIDGE_POLARIS_ASSESSMENT_TYPES` | Polaris assessment types  Accepted values:   - `DAST` - `SAST` - `SCA` - `SAST,SCA`   For DAST configuration requirements, see Using Bridge CLI With Polaris. | Mandatory |
| `BRIDGE_POLARIS_BRANCH_NAME` | Branch name on the Polaris Server. The branch is created if it doesn't already exist. | Optional |
| `BRIDGE_POLARIS_BRANCH_PARENT_NAME` | Parent branch name on the Polaris Server. Parent branch name is used by the PR comments feature. | Optional |
| `BRIDGE_POLARIS_PROJECT_NAME` | Project name in Polaris. The Default Value is `$BITBUCKET_REPO_SLUG` | Optional |
| `BRIDGE_POLARIS_SERVERURL` | Polaris server URL | Mandatory |
| `BRIDGE_BITBUCKET_API_TOKEN` | Bitbucket User Access Token. Example: `BRIDGE_BITBUCKET_API_TOKEN: $BRIDGE_BITBUCKET_API_TOKEN` | Mandatory when `BRIDGE_POLARIS_PRCOMMENT_ENABLED` is set as `true`. |
| `BRIDGE_BITBUCKET_API_USER_NAME` | Specify your Bitbucket User Name to use features like PR Comments, SARIF upload and diagnostics upload. This works in conjunction with your Bitbucket API token. | Mandatory when `BRIDGE_POLARIS_PRCOMMENT_ENABLED` is set as `true`. |
| `BRIDGE_PROJECT_DIRECTORY` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `BRIDGE_POLARIS_REPORTS_SARIF_CREATE` | Set this to true to generate SARIF report. **Default:** `false` Note: SARIF reports can be generated for any configured branch; however, report generation is not supported in a merge request context. | Optional |
| `BRIDGE_POLARIS_REPORTS_SARIF_FILE_PATH` | File path (including file name) where SARIF report is created. Only `.sarif` or `.sarif.json` files will be uploaded. All other formats are excluded.  **Default:** `.blackduck/integrations/polaris/sarif/report.sarif.json` | Optional |
| `BRIDGE_POLARIS_REPORTS_SARIF_ISSUE_TYPES` | Lists which assessment issues types to include in SARIF file report. Example: `'SCA,SAST'` | Optional |
| `BRIDGE_POLARIS_REPORTS_SARIF_SEVERITIES` | Comma-separated list of SAST/SCA issue severities to include in SARIF file report. Valid severities are `Critical`, `High`, `Medium`, `Low`, and `Informational`.  **Default:** All severities are included. | Optional |
| `BRIDGE_POLARIS_REPORTS_SARIF_GROUPSCAISSUES` | When set to true, SCA issues are grouped by component. Set this to false to list SCA issues by vulnerability. **Default:** `true` | Optional |
| `BRIDGE_POLARIS_PRCOMMENT_ENABLED` | Option to enable automatic creation pull request comments for new issues found in the merge request.  Note: The merge request from the feature branch to the main branch must exist for this feature to work.  **Default:** `false` | Optional |
| `BRIDGE_POLARIS_PRCOMMENT_SEVERITIES` | The value should be a comma-separated list of severities. Comments are created for issues where the issue severity matches one of the values specified using this option.  Valid severities are `Critical`, `High`, `Medium`, `Low`, and `Informational`.  **Default:** `CRITICAL,HIGH` | Optional |
| `BRIDGE_POLARIS_FIXPR_ENABLED` | Enable Fix Pull Request creation for SCA vulnerabilities. Creates Pull Requests with dependency upgrades to fix security issues. Only runs on push and workflow_dispatch events.  **Default** : `false`. | Optional |
| `BRIDGE_POLARIS_FIXPR_MAXCOUNT` | Maximum number of Fix Pull Requests to create per scan/workflow run. This limits the number of Pull Requests generated to avoid overwhelming the repository with too many automated Pull Requests at once. **Default** : `5`. | Optional |
| `BRIDGE_POLARIS_FIXPR_USEUPGRADEGUIDANCE` | Allows the user to specify short-term or long-term upgrade guidance, or both. If both values are provided, the first takes priority, and the second value is used only if the first returns no results. If upgrade guidance is not available, the Fix Pull Request is not created.  **Accepted Values**:  - `SHORT_TERM` - `LONG_TERM` - `SHORT_TERM,LONG_TERM` - `LONG_TERM,SHORT_TERM`  **Default**: : `SHORT_TERM,LONG_TERM`. | Optional |
| `BRIDGE_POLARIS_FIXPR_FILTER_SEVERITIES` | Comma-separated list of severity levels for which Fix PRs should be created. Filters SCA vulnerabilities by severity to control which security issues generate automated Fix Pull requests.  **Accepted values**: One or more of the following (comma-separated, case-insensitive):   - CRITICAL - HIGH - MEDIUM - LOW   **Default**: CRITICAL,HIGH | Optional |
| `BRIDGE_POLARIS_ASSESSMENT_MODE` | The test mode type of the Polaris scan. Supported values: `SOURCE_UPLOAD`, `CI` **Default:**`CI`  **Note**: `BRIDGE_POLARIS_ASSESSMENT_MODE=SOURCE_UPLOAD` is scheduled for deprecation. Please use `remote` for `BRIDGE_POLARIS_TEST_SAST_LOCATION` and/or `BRIDGE_POLARIS_TEST_SCA_LOCATION` instead. | Optional |
| `BRIDGE_POLARIS_TEST_SAST_LOCATION` | Configure location of source code capture and SAST analysis. Supported values are `hybrid`, `local` and `remote`.   **Default**: `hybrid`    In `hybrid` mode Bridge downloads tools for local capture and uploads artifacts (idir) for analysis on Polaris.    In `local` mode Bridge downloads tools for local capture and performs a full analysis in the local CI/CD environment, with results uploaded to Polaris.    In `remote` mode Bridge zips source code and uploads to Polaris for full capture and analysis. | Optional |
| `BRIDGE_POLARIS_TEST_SCA_LOCATION` | Configure location of source code capture and SCA analysis. Supported values are `hybrid` and `remote`.   **Default**: `hybrid`    In `hybrid` mode Bridge downloads tools for local capture and uploads artifacts (BDIO) for analysis on Polaris.    In `remote` mode Bridge zips source code and uploads to Polaris for full capture and analysis. | Optional |
| `BRIDGE_PROJECT_SOURCE_EXCLUDES` | A list of git ignore pattern strings that indicate the files need to be excluded from the zip file. | Optional |
| `BRIDGE_PROJECT_SOURCE_ARCHIVE` | The zipped source file path. It overrides the project directory. | Optional |
| `BRIDGE_POLARIS_TEST_SCA_TYPE` | `SCA-PACKAGE`  Polaris SCA test type to trigger signature scan, package manager scan or binary scan.  **Default**: SCA-PACKAGE  **Supported values**:  - `SCA-BINARY` - `SCA-PACKAGE` - `SCA-SIGNATURE` - `SCA-PACKAGE, SCA-SIGNATURE`  Note: `SCA-BINARY` can only be used stand-alone. It cannot be combined with `SCA-PACKAGE` or `SCA-SIGNATURE`. | Optional |
| `BRIDGE_POLARIS_ARTIFACTTOUPLOAD` | Path to a binary or archive file to analyze. | Optional. Required when using ​ `SCA-BINARY` ​as the SCA Test Type. |
| `BRIDGE_POLARIS_TEST_SAST_TYPE` | Polaris test type to trigger sigma rapid scan or full scan. Supported values: `SAST_RAPID` or `SAST_FULL`  **Default**: `SAST_FULL` | Optional |
| `BRIDGE_POLARIS_WAITFORSCAN` | Specifies whether or not the workflow should wait for the analysis to complete.  **Default:** `true`  If set to `false`, post scan workflows like PR comment, Fix PR, SARIF etc. will not be applicable. | Optional |
