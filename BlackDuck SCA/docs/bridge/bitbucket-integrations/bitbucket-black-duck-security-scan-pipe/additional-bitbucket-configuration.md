---
title: "Additional Bitbucket configuration"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/additional-bitbucket-configuration.html"
content_id: "BkX4Uh9D8LPV41JBSU3jkQ"
version: "latest"
section: "Bitbucket Integrations"
scraped_at: "2026-08-08T23:49:07.068511+00:00"
---

# Additional Bitbucket configuration

Additional pipe configurations can be found here.
Instructions are also provided for further configurations related to artifacts (i.e. SARIF files and diagnostics).

## Additional Pipe configuration

Here are some additional optional configurations that can be used with Black Duck Security Scan Pipe:

- **Install directory:**

  `BRIDGECLI_INSTALL_DIRECTORY`: Use
  this to specify the custom Bridge CLI installation directory rather than the
  default `$HOME/bridge-cli` installation directory. You can
  specify a custom installation directory for `bridge-cli`
  using the `BRIDGECLI_INSTALL_DIRECTORY` variable with
  `CUSTOM_IMAGE` configuration (See details for custom
  image configuration in Prerequisite section).

  By default,
  `bridge-cli` is installed in the
  `$HOME/bridge-cli-bundle` directory. If you choose to use
  a custom directory, ensure that the directory already exists inside the
  custom image before running the pipeline.

  Example:
  `BRIDGECLI_INSTALL_DIRECTORY:
  '/usr/local/my-custom-directory'`
- **Download URL:**

  `BRIDGECLI_DOWNLOAD_URL`: If provided, this specifies the URL to the Bridge CLI
  zip file to be downloaded from and used. Examples:
  `BRIDGECLI_DOWNLOAD_URL:
  https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-linux64.zip`
  or `BRIDGECLI_DOWNLOAD_URL:
  https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/3.2.0/bridge-cli-bundle-3.2.0-linux64.zip`

  Note: Note: If `BRIDGECLI_DOWNLOAD_URL` is not provided,
  Black Duck Security Scan Pipe will download the latest version of Bridge
  CLI from [repo.blackduck.com](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/).
- **Download version:**

  `BRIDGECLI_DOWNLOAD_VERSION`: Use this
  to specify the Bridge CLI version to use. If provided, the specified version
  of Bridge CLI will be automatically downloaded from [repo.blackduck.com](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/) and used. If not, the latest
  version is downloaded and used.

  Example:
  `BRIDGECLI_DOWNLOAD_VERSION: "1.0.0"`

  Note: If both
  `BRIDGECLI_DOWNLOAD_VERSION` and
  `BRIDGECLI_DOWNLOAD_URL` are provided,
  `BRIDGECLI_DOWNLOAD_URL` takes precedence.
- **Network Airgap:**

  `BRIDGE_NETWORK_AIRGAP`: If the
  `BRIDGE_NETWORK_AIRGAP` is set to `true`,
  Black Duck Security Scan Pipe does not download the Bridge CLI. Instead it
  uses the pre-configured Bridge CLI. If the Bridge CLI is configured at a
  specific location, you must provide the path through
  `BRIDGECLI_INSTALL_DIRECTORY`. The Black Duck Security
  Scan Pipe looks for the Bridge CLI in the provided
  `BRIDGECLI_INSTALL_DIRECTORY`. If that parameter is not
  found, pipe will look for Bridge CLI in the default path
  (`$HOME/bridge-cli-bundle`).

  To use `BRIDGE_NETWORK_AIRGAP`, make sure to configure your
  `CUSTOM_IMAGE` correctly. (See details for custom image
  configuration in Prerequisite section.)

  If you use Black Duck SCA, download and set up an airgapped version of Detect
  under `$HOME/.bridge/blackduck`. To use a custom location,
  set `DETECT_INSTALL_DIRECTORY` to point to the Detect
  installation directory.

  Note: If `BRIDGE_NETWORK_AIRGAP` is enabled,
  `BRIDGECLI_DOWNLOAD_VERSION` and
  `BRIDGECLI_DOWNLOAD_URL` are ignored.
- **Using a proxy through Bitbucket's environment:**

  Black Duck Security Scan
  for Bitbucket supports the following variables:

  Table 1. Proxy parameters

  | **Variable** | Description | **Example** |
  | --- | --- | --- |
  | `HTTPS_PROXY` / `https_proxy` | Proxy URL for HTTPS traffic. You can include basic authentication if required. Use this when target URL is HTTPS. | - `https://proxy.com` - `https://192.168.1.1:8080` - `https://username:password@proxy.com` |
  | `HTTP_PROXY` / `http_proxy` | Proxy URL for HTTP traffic. You can include basic authentication if required. Use this when target URL is HTTP. | - `http://proxy.com` - `http://192.168.1.1:8080` - `http://username:password@proxy.com` |
  | `NO_PROXY` / `no_proxy` | A comma-separated list of hosts or IP addresses that should bypass the proxy. Some clients only honor IP addresses when connections are made directly to the IP rather than a hostname. | - `example.com` - `example.com,myserver.local:443,example.org` |

  Note: Currently Coverity Local Scan
  is not supported with Proxy configuration.

  You may use the proxy parameters with secrets as shown here:

  ```
  variables:
    HTTPS_PROXY: $HTTPS_PROXY # Proxy URL for HTTPS traffic
    HTTP_PROXY: $HTTP_PROXY # Proxy URL for HTTP traffic
    NO_PROXY: $NO_PROXY_LIST # Comma-separated list of hosts or IP addresses that should bypass the proxy
  ```

  Note: Proxy variables
  in a Bitbucket pipeline can either be defined globally (available to all
  steps) or scoped to a single step (available only within that
  step).

  If you are using a proxy with authentication, follow these guidelines:
  - Proxy with auth: Users need to pass a username and password for
    authentication.

    Example:
    **http://user:password@proxyIP:proxyPort/**
  - Proxy with no auth: Users do not need to pass credentials for
    authentication.

    Example: **http://proxyIP:proxyPort/**
  - For further information: <https://support.atlassian.com/bitbucket-cloud/docs/configure-a-runner-to-use-a-proxy/>
- **Mark build status:**

  `MARK_BUILD_STATUS`: Marks the build status to use if policy
  violating issues are found. The default value is `fail`. The
  supported values are `success` and `fail`.
- **Using a custom image:**

  `CUSTOM_IMAGE`: Use this to specify the custom docker image for
  the pipe execution. To learn more about user-defined custom image configuration,
  refer to the Black Duck
  documentation for Bitbucket Prerequisites.

## Configure artifacts in bitbucket-pipelines.yml for SARIF and diagnostics

Artifacts are files that are produced by a step. Once you've defined them in your pipeline configuration,
you can share them with a following step or export them (to keep the artifacts after a step completes).
For example, you may want to use reports or JAR files generated by a build step in a later deployment step.
You may also like to download an artifact generated by a step, or upload it to external storage.
The code blocks below provide examples of these tasks.

Note: Users must configure their pipelines to produce SARIF and diagnostics as artifacts, in order to perform these tasks.

There is a **limitation** that is important to know: Files that are in the `BITBUCKET_CLONE_DIR` at the end of a step can be configured as artifacts.
The `BITBUCKET_CLONE_DIR` is the directory in which the repository was initially cloned. Please see the code examples below. Details can be found in the Bitbucket documentation, at
[Pipeline Artifacts](https://support.atlassian.com/bitbucket-cloud/docs/use-artifacts-in-steps/).

**Example for a Polaris scan:**

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
            
                ## Mandatory when BRIDGE_POLARIS_PRCOMMENT_ENABLED or BRIDGE_POLARIS_REPORTS_SARIF_CREATE is set true.
                # BRIDGE_BITBUCKET_API_TOKEN: $BITBUCKET_REPO_ACCESS_TOKEN

                ## Pull Request Comments
                # BRIDGE_POLARIS_PRCOMMENT_ENABLED: 'true'

                ## SARIF report generation
                BRIDGE_POLARIS_REPORTS_SARIF_CREATE: 'true'
            
                ## Uncomment below configuration for signature scan
                # BRIDGE_POLARIS_TEST_SCA_TYPE: 'SCA-SIGNATURE'

                ## Mark build status if policy violating issues are found
                # MARK_BUILD_STATUS: 'success'

                INCLUDE_DIAGNOSTICS: 'true'

        artifacts:
          - '.blackduck/integrations/polaris/sarif/report.sarif.json'
          - '.bridge/**'

pipelines:
    pull-requests:
        '**': # Matches all pull requests
            - <<: *blackduck-security-scan
    branches:
        '{main,master,develop,stage,release}':
            - <<: *blackduck-security-scan
```

**Example for a Black Duck SCA scan:**

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

                ## Mark build status if policy violating issues are found
                # MARK_BUILD_STATUS: 'success'

                INCLUDE_DIAGNOSTICS: 'true'

        artifacts:
            - '.blackduck/integrations/blackducksca/sarif/report.sarif.json'
            - '.bridge/**'

pipelines:
    pull-requests:
        '**': # Matches all pull requests
          - <<: *blackduck-security-scan
    branches:
        '{main,master,develop,stage,release}':
          - <<: *blackduck-security-scan
```

Note:

**The Polaris example provided below will not work for generating artifacts from the pipeline.**

```
security-scan: &blackduck-security-scan
  step:
    name: Black Duck Security Scan
    script:
      - pipe: blackduck-inc/blackduck-security-scan:1.6.0
        variables:
          BRIDGE_POLARIS_SERVERURL: $BRIDGE_POLARIS_SERVERURL
          BRIDGE_POLARIS_ACCESSTOKEN: $BRIDGE_POLARIS_ACCESSTOKEN
          BRIDGE_POLARIS_ASSESSMENT_TYPES: 'SCA,SAST'
          BRIDGE_POLARIS_APPLICATION_NAME: $BRIDGE_POLARIS_APPLICATION_NAME
          BRIDGE_POLARIS_PROJECT_NAME: $BRIDGE_POLARIS_PROJECT_NAME
          BRIDGE_POLARIS_BRANCH_NAME: $BRIDGE_POLARIS_BRANCH_NAME
                    
          ### Upload Polaris SARIF report as job artifact
          BRIDGE_POLARIS_REPORTS_SARIF_CREATE: 'true'
          BRIDGE_POLARIS_REPORTS_SARIF_FILE_PATH: '/usr/local/report/report.sarif.json'
          BRIDGE_POLARIS_REPORTS_SARIF_ISSUE_TYPES: 'SCA,SAST'
          BRIDGE_POLARIS_REPORTS_SARIF_SEVERITIES: 'CRITICAL,HIGH'
          BRIDGE_POLARIS_REPORTS_SARIF_GROUPSCAISSUES: 'true'
                    
          # BRIDGE_POLARIS_WAITFORSCAN: 'false'   # Used to support the async mode
                    
          ### Enable Bridge CLI diagnostics
          # INCLUDE_DIAGNOSTICS: 'true'
                    
    artifacts:
      - '/usr/local/report/report.sarif.json'  # This is not going to work as the json file is outside BITBUCKET_CLONE_DIR 
      - '.bridge/**'                          # Diagnostics will be available as artifact

pipelines:
  pull-requests:
    '**':  # Matches all pull requests
      - <<: *blackduck-security-scan
  branches:
    '{main,master,develop,stage,release}':
      - <<: *blackduck-security-scan
```

**The Black Duck SCA example provided below will not work for generating artifacts from the pipeline.**

```
security-scan: &blackduck-security-scan
  step:
    name: Black Duck Security Scan
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
                    
          ## SARIF Report Generation
          BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_CREATE: 'true'
          BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_FILE_PATH: '/usr/local/report/report.sarif.json'
          BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_SEVERITIES: 'CRITICAL,HIGH'
          BRIDGE_BLACKDUCKSCA_REPORTS_SARIF_GROUPSCAISSUES: 'true'
                    
          ## Enable Bridge-CLI diagnostics
          INCLUDE_DIAGNOSTICS: 'true'
                    
          ## BRIDGE_BITBUCKET_API_TOKEN is required to upload SARIF and diagnostics in the Bitbucket downloads section, otherwise configure SARIF and diagnostics as artifacts in the bitbucket-pipelines.yml
          # BRIDGE_BITBUCKET_API_TOKEN : $BRIDGE_BITBUCKET_API_TOKEN
                    
          ## Mark build status if policy violating issues are found
          # MARK_BUILD_STATUS: 'success'
                    
          ## Use custom image to configure paths and tools     
          # CUSTOM_IMAGE: 'user/custom-blackduck-security-scan:maven'
          ## Uncomment below if custom docker image is private
          # DOCKER_USERNAME: $DOCKER_USERNAME
          # DOCKER_PASSWORD: $DOCKER_PASSWORD
          ## Use this for internal docker registry 
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
                    
    artifacts:
      - '/usr/local/report/report.sarif.json'   # This is not going to work as the json file is outside BITBUCKET_CLONE_DIR 
      - '.bridge/**'                            # Diagnostics will be available as artifact

pipelines:
  pull-requests:
    '**':  # Matches all pull requests
      - <<: *blackduck-security-scan
  branches:
    '{main,master,develop,stage,release}':
      - <<: *blackduck-security-scan
```
