---
title: "Additional GitLab configuration"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/additional-gitlab-configuration.html"
content_id: "QaUepVRb9NsYmMamWxQvtg"
version: "latest"
section: "GitLab Integrations"
scraped_at: "2026-08-08T23:48:11.746184+00:00"
---

# Additional GitLab configuration

## Optional configurations

Here are some additional optional configurations that can be used with Black Duck Security Scan Template:

- **Install directory:**

  `BRIDGECLI_INSTALL_DIRECTORY`: Use this to specify the path to Bridge CLI.

  Note: If this is not explicitly specified, then the integration defaults to `$HOME/bridge-cli`. If the installed version of Bridge CLI is not the latest, then the latest version of Bridge CLI is downloaded unless you specify the version to use explicitly (as documented below).
- **Download URL:**

  `BRIDGECLI_DOWNLOAD_URL`: If provided, this specifies the URL to the Bridge CLI zip file to be downloaded from and used. Examples: `BRIDGECLI_DOWNLOAD_URL:
  https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-win64.zip` or `BRIDGECLI_DOWNLOAD_URL:
  https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/3.11.0/bridge-cli-bundle-3.11.0-win64.zip`

  Note: If `BRIDGECLI_DOWNLOAD_URL` is not provided, Black Duck Security Scan Template will download the latest version of Bridge CLI from [repo.blackduck.com](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/).
- **Download version:**

  `BRIDGECLI_DOWNLOAD_VERSION`: Use this to specify the Bridge CLI version to use. If provided, the specified version of Bridge CLI will be automatically downloaded from [repo.blackduck.com](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/) and used. If not, the latest version is downloaded and used. Example: `BRIDGECLI_DOWNLOAD_VERSION: "1.0.0"`

  Note: If both `BRIDGECLI_DOWNLOAD_VERSION` and `BRIDGECLI_DOWNLOAD_URL` are provided, `BRIDGECLI_DOWNLOAD_URL` takes precedence.

  Note: If `BRIDGE_NETWORK_AIRGAP` is enabled, `BRIDGECLI_DOWNLOAD_VERSION` and `BRIDGECLI_DOWNLOAD_URL` are ignored.
- **Network Airgap:**

  `BRIDGE_NETWORK_AIRGAP`: If `BRIDGE_NETWORK_AIRGAP` is set to `true`, GitLab Template will not download Bridge CLI, so you must download and set up Bridge CLI locally. The default Bridge CLI installation directory is `$HOME/bridge-cli`. To install Bridge CLI in a custom location, set `BRIDGE_NETWORK_AIRGAP` in your GitLab workflow to point to your custom Bridge installation directory.

  Note: : If you use Black Duck SCA, download and set up your airgapped version of Detect under `$HOME/.bridge/blackduck`. To use a custom location, set `BRIDGE_BLACKDUCK_INSTALL_DIRECTORY` to point to the Detect installation directory.
- **Using a proxy through GitLab Template's environment:**

  Black Duck Security Scan Template supports the following environment variables:

  Table 1. Proxy parameters

  | **Variable** | Description | **Example** |
  | --- | --- | --- |
  | `HTTPS_PROXY` / `https_proxy` | Proxy URL for HTTPS traffic. You can include basic authentication if required. Use this when target URL is HTTPS. | - `https://proxy.com` - `https://192.168.1.1:8080` - `https://username:password@proxy.com` |
  | `HTTP_PROXY` / `http_proxy` | Proxy URL for HTTP traffic. You can include basic authentication if required. Use this when target URL is HTTP. | - `http://proxy.com` - `http://192.168.1.1:8080` - `http://username:password@proxy.com` |
  | `NO_PROXY` / `no_proxy` | A comma-separated list of hosts or IP addresses that should bypass the proxy. Some clients only honor IP addresses when connections are made directly to the IP rather than a hostname. | - `example.com` - `example.com,myserver.local:443,example.org` |

  Note: Currently Coverity Local Scan is not supported with Proxy configuration.

  You may use the proxy parameters with secrets as shown here:

  ```
  variables:
      HTTPS_PROXY: $HTTPS_PROXY # Proxy URL for HTTPS traffic
      HTTP_PROXY: $HTTP_PROXY # Proxy URL for HTTP traffic
      NO_PROXY: $NO_PROXY_LIST # Comma-separated list of hosts or IP addresses that should bypass the proxy
  ```

  Note: Proxy variables in a GitLab pipeline can either be defined globally (available to all stages) or scoped to a single stage (available only within that stage).

  If you are using a proxy with authentication, follow these guidelines:
  - Proxy with auth: Users need to pass a username and password for authentication.

    Example: **http://user:password@proxyIP:proxyPort/**
  - Proxy with no auth: Users do not need to pass credentials for authentication.

    Example: **http://proxyIP:proxyPort/**
  - For further information: <https://docs.gitlab.com/runner/configuration/proxy/>
- **CURL Redirection limit:**

  `MAX_REDIRECTS`: Use this environment variable to specify the maximum number of times a request can be automatically redirected to a new URL before the process is aborted.

  Default: `30` (default curl behaviour)

  ```
  variables:
      MAX_REDIRECTS: 40
  ```
- **Include diagnostics:**

  `INCLUDE_DIAGNOSTICS`: When set to `true`, Bridge CLI diagnostic files are created.

  Note: While including Bridge CLI diagnostic files, default expiry time for uploaded artifacts is 30 days. Refer to SCM documentation for more details : <https://docs.gitlab.com/ee/ci/jobs/job_artifacts.html>.
- **Mark build status:**

  `MARK_BUILD_STATUS`: Defines the build status when policy-violating issues are detected.

  Default: `failed`.

  Supported values: `failed`, and `success`.

  Note: `MARK_BUILD_STATUS` is applicable only for return status `8`. For any other return value, `MARK_BUILD_STATUS` is ignored.
