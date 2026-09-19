---
title: "Using Black Duck Security Scan Pipe for Coverity"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/using-black-duck-security-scan-pipe-for-coverity.html"
content_id: "GssxTBFDd10pv2sxg1Nonw"
version: "latest"
section: "Bitbucket Integrations"
scraped_at: "2026-08-08T23:49:05.495927+00:00"
---

# Using Black Duck Security Scan Pipe for Coverity

As a Bitbucket Pipe user, you can use Bridge CLI to automate Coverity scanning in your CI pipeline. You can use Bridge CLI with SRM in the following ways:

- Automate SAST scans
- Add pull-request comments to Bitbucket

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
              BRIDGE_COVERITY_CONNECT_URL: $COVERITY_URL
              BRIDGE_COVERITY_CONNECT_USER_NAME: $COVERITY_USER
              BRIDGE_COVERITY_CONNECT_USER_PASSWORD: $COVERITY_PASSWORD
                      
              ## Pull Request Comments
              # BRIDGE_COVERITY_PRCOMMENT_ENABLED: 'true'
              # BRIDGE_BITBUCKET_API_TOKEN: $BITBUCKET_REPO_ACCESS_TOKEN

              ### To enable the use of self-signed certificates
              # BRIDGE_NETWORK_SSL_TRUSTALL: true
              # BRIDGE_NETWORK_SSL_CERT_FILE: '/Users/Config/cert.pem'
                      
              ## Mark build status if policy violating issues are found
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
      pull-requests:
          '**':
              - step:
                    #runs-on: # Use this to specify self-hosted runners
                    # - linux # Name of your Bitbucket runner
                    script:
                        - pipe: blackduck-inc/blackduck-security-scan:1.6.0
                          variables:
                              BRIDGE_COVERITY_CONNECT_URL: $COVERITY_URL
                              BRIDGE_COVERITY_CONNECT_USER_NAME: $COVERITY_USER
                              BRIDGE_COVERITY_CONNECT_USER_PASSWORD: $COVERITY_PASSWORD
                              BRIDGE_COVERITY_CONNECT_PROJECT_NAME: $BITBUCKET_REPO_SLUG

                              BRIDGE_COVERITY_CONNECT_STREAM_NAME: $BITBUCKET_REPO_SLUG-$BITBUCKET_BRANCH

                              ## Pull Request Comments
                              # BRIDGE_COVERITY_PRCOMMENT_ENABLED: 'true'
                              # BRIDGE_COVERITY_PRCOMMENT_IMPACTS: 'HIGH,MEDIUM'
                              # BRIDGE_BITBUCKET_API_TOKEN : $BRIDGE_BITBUCKET_API_TOKEN

                              ## Or use the combination of Bitbucket App Password and Bitbucket User Name for authentication
                              # BRIDGE_BITBUCKET_API_TOKEN: $BITBUCKET_APP_PASSWORD
                              # BRIDGE_BITBUCKET_API_USER_NAME: $BITBUCKET_USER_NAME

                              ## Enable Bridge-CLI diagnostics
                              # INCLUDE_DIAGNOSTICS: 'true'

                              ## Mark build status if policy violating issues are found
                              # MARK_BUILD_STATUS: 'success'

                              ## Use custom image to configure paths and tools     
                              # CUSTOM_IMAGE: 'user/custom-blackduck-security-scan:maven'

                              ## Uncomment to specify the directory to scan. Default value is repository root
                              # BRIDGE_PROJECT_DIRECTORY: '/usr/local/my-project'

                              # NETWORK_AIRGAP: true
                              # BRIDGECLI_INSTALL_DIRECTORY:'/usr/local/bridge-cli-bundle'

                              ## Coverity (SAST) Tools Settings
                              # BRIDGE_COVERITY_CLEAN_COMMAND: 'mvn clean'
                              # BRIDGE_COVERITY_BUILD_COMMAND: 'mvn clean install'
                              # BRIDGE_COVERITY_CONFIG_PATH: '/usr/local/config/coverity.yml'
                              # BRIDGE_COVERITY_ARGS: '-c /usr/local/config/coverity.yml -o capture.build.clean-command="mvn clean" -- mvn clean install'
                              # BRIDGE_COVERITY_INSTALL_DIRECTORY: '/usr/local/cov-thin-client'

                    ### Use below configuration for uploading artifacts if INCLUDE_DIAGNOSTICS is enabled        
                    artifacts:
                        - '.bridge/**'

      branches:
          '{main,master,develop,stage,release}':
              - step:
                    #runs-on: # Use this to specify self-hosted runners
                    # - linux # Name of your Bitbucket runner
                    script:
                        - pipe: blackduck-inc/blackduck-security-scan:1.5.0
                          variables:
                              BRIDGE_COVERITY_CONNECT_URL: $COVERITY_URL
                              BRIDGE_COVERITY_CONNECT_USER_NAME: $COVERITY_USER
                              BRIDGE_COVERITY_CONNECT_USER_PASSWORD: $COVERITY_PASSWORD
                              BRIDGE_COVERITY_CONNECT_PROJECT_NAME: $BITBUCKET_REPO_SLUG

                              BRIDGE_COVERITY_CONNECT_STREAM_NAME: $BITBUCKET_REPO_SLUG-$BITBUCKET_BRANCH
                              BRIDGE_COVERITY_CONNECT_POLICY_VIEW: 'Outstanding Issues'
                              # BRIDGE_COVERITY_WAITFORSCAN: 'false'   # Used to support the async mode

                              ### Enable Bridge-CLI diagnostics
                              # INCLUDE_DIAGNOSTICS: 'true'

                              ### BRIDGE_BITBUCKET_API_TOKEN is required to upload diagnostics in the Bitbucket downloads section, otherwise diagnostics as artifact in the bitbucket-pipelines.yml
                              # BRIDGE_BITBUCKET_API_TOKEN : $BRIDGE_BITBUCKET_API_TOKEN

                              ## Or use the combination of Bitbucket App Password and Bitbucket User Name for authentication
                              # BRIDGE_BITBUCKET_API_TOKEN: $BITBUCKET_APP_PASSWORD
                              # BRIDGE_BITBUCKET_API_USER_NAME: $BITBUCKET_USER_NAME

                              ## Mark build status if policy violating issues are found
                              # MARK_BUILD_STATUS: 'success'

                              ## Use custom image to configure paths and tools     
                              # CUSTOM_IMAGE: 'user/custom-blackduck-security-scan:maven'

                              ## Uncomment to specify the directory to scan. Default value is repository root
                              # BRIDGE_PROJECT_DIRECTORY: '/usr/local/my-project'

                              # NETWORK_AIRGAP: true
                              # BRIDGECLI_INSTALL_DIRECTORY:'/usr/local/bridge-cli-bundle'

                              ## Coverity (SAST) Tools Settings
                              # BRIDGE_COVERITY_CLEAN_COMMAND: 'mvn clean'
                              # BRIDGE_COVERITY_BUILD_COMMAND: 'mvn clean install'
                              # BRIDGE_COVERITY_CONFIG_PATH: '/usr/local/config/coverity.yml'
                              # BRIDGE_COVERITY_ARGS: '-c /usr/local/config/coverity.yml -o capture.build.clean-command="mvn clean" -- mvn clean install'
                              # BRIDGE_COVERITY_INSTALL_DIRECTORY: '/usr/local/cov-thin-client'

                    ### Use below configuration for uploading artifacts if INCLUDE_DIAGNOSTICS is enabled   
                    artifacts:
                        - '.bridge/**'
  ```

Table 1. List of mandatory and optional parameters for Coverity

| **Input parameter** | Description | **Mandatory / optional** |
| --- | --- | --- |
| `BRIDGE_COVERITY_PRCOMMENT_ENABLED` | When set to `true`, pull request comments are created automatically for new issues found in the pull request. This feature requires a full scan to exist on the server prior to use. Once you have completed a full scan, it will serve as a baseline, and then you may set `BRIDGE_COVERITY_PRCOMMENT_ENABLED=true`.  Additionally, the merge request from your feature branch to your main branch must exist for this feature to work.  **Default:**`false`  Note: When both `BRIDGE_COVERITY_PRCOMMENT_ENABLED` and `BRIDGE_COVERITY_CONNECT_POLICY_VIEW` are configured for a Coverity PR scan, the `BRIDGE_COVERITY_CONNECT_POLICY_VIEW` setting will be ignored and PR comments will be generated only for new issues that match the specified impact filter (`BRIDGE_COVERITY_PRCOMMENT_IMPACTS`). Further details can be found here. | Optional |
| `BRIDGE_COVERITY_PRCOMMENT_IMPACTS` | Comma-separated list of impacts that will cause Pull Request scans to fail.  Issues detected in the Pull Request that match any of the listed impact levels will be uploaded to Coverity, added as Pull Request comments and trigger build failure.    Valid impacts are: `HIGH`, `MEDIUM`, `LOW` and `AUDIT`.    **Default**: `HIGH` | Optional |
| `BRIDGE_COVERITY_CONNECT_POLICY_VIEW` | ID or name of policy view to be used to enforce the “break the build” policy.  If issues are found in the specified this view, build will be failed.  Example: `coverity_policy_view: '100001'` or `coverity_policy_view: 'Outstanding Issues'` | Optional |
| `BRIDGE_COVERITY_CONNECT_PROJECT_NAME` | Project name in Coverity. The Default value is `$BITBUCKET_REPO_SLUG` | Optional |
| `BRIDGE_COVERITY_CONNECT_STREAM_NAME` | Stream name in Coverity. The Default value for PR context is `$BITBUCKET_REPO_SLUG-$BITBUCKET_PR_DESTINATION_BRANCH`  Default value for NON PR context is `$BITBUCKET_REPO_SLUG-$BITBUCKET_BRANCH` | Optional |
| `BRIDGE_COVERITY_CONNECT_URL` | Coverity server URL | Mandatory |
| `BRIDGE_COVERITY_CONNECT_USER_NAME` | Coverity username | Mandatory |
| `BRIDGE_COVERITY_CONNECT_USER_PASSWORD` | Coverity passphrase | Mandatory |
| `BRIDGE_COVERITY_LOCAL` | Set to `false` if using Coverity cloud deployment. Black Duck Security Scan Pipe will install Coverity Thin Client as necessary.  Set to `true` if you are using on-prem Coverity Connect. When set to `true`, Black Duck Security Pipe will install Coverity Analysis on the local system in order to execute the scan.  **Default:** `false`  Usage example: `BRIDGE_COVERITY_LOCAL: true` | Optional |
| `BRIDGE_COVERITY_VERSION` | The version of Coverity that Bridge should use. | Optional |
| `BRIDGE_BITBUCKET_API_TOKEN` | Bitbucket User Access Token  Example: `BRIDGE_BITBUCKET_API_TOKEN: $BRIDGE_BITBUCKET_API_TOKEN` | Mandatory when `BRIDGE_COVERITY_AUTOMATION_PRCOMMENT` is set as `true`. |
| `BRIDGE_BITBUCKET_API_USER_NAME` | Specify your Bitbucket User Name to use features like PR Comments, SARIF upload and diagnostics upload. This works in conjunction with your Bitbucket API token. | Mandatory when `BRIDGE_POLARIS_PRCOMMENT_ENABLED` is set as `true`. |
| `BRIDGE_COVERITY_INSTALL_DIRECTORY` | Installation directory of Coverity. This should be a valid empty directory. | Optional |
| `BRIDGE_PROJECT_DIRECTORY` | The project source directory. Defaults to the repository root directory. Set this to specify a custom folder that is other than repository root. | Optional |
| `BRIDGE_COVERITY_CONFIG_PATH` | Coverity config file path location. | Optional |
| `BRIDGE_COVERITY_WAITFORSCAN` | Specifies if the workflow should wait for the analysis to complete.  **Default:** `true`  If set to `false`, post scan workflows like PR comment, Fix PR, SARIF etc will not be applicable. | Optional |
| `BRIDGE_COVERITY_BUILD_COMMAND` | Build command for Coverity. | Optional |
| `BRIDGE_COVERITY_CLEAN_COMMAND` | Clean command for Coverity. | Optional |
| `BRIDGE_COVERITY_ARGS` | Additional arguments for Coverity. | Optional |

Table 2. List of network parameters

| **Input parameter** | Description | **Mandatory / optional** |
| --- | --- | --- |
| `BRIDGE_NETWORK_SSL_TRUSTALL` | Disables SSL certificate verification. Use with caution.  **Default**: false | Optional |
| `BRIDGE_NETWORK_SSL_CERT_FILE` | File path to configure the HTTPS calls to accept a self-signed certificate. | Optional |

- `BRIDGE_NETWORK_SSL_TRUSTALL` and `BRIDGE_NETWORK_SSL_CERT_FILE` cannot both be specified at the same time.
