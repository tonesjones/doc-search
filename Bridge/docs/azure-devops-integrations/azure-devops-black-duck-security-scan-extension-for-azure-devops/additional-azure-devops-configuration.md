---
title: "Additional Azure DevOps configuration"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/additional-azure-devops-configuration.html"
content_id: "wsA8K_vVwdOSxGJalg6c3A"
version: "latest"
section: "Azure DevOps Integrations"
scraped_at: "2026-08-08T23:48:30.870685+00:00"
---

# Additional Azure DevOps configuration

Here are some additional optional configurations that can be used with Black Duck Security Scan Extension for Azure DevOps:

- `BRIDGECLI_INSTALL_DIRECTORY`: Use this to specify the path to Bridge CLI.

  Note: If this is not explicitly specified, then the integration defaults to `$HOME/bridge-cli`. If the installed version of Bridge CLI is not the latest, then the latest version of Bridge CLI is downloaded unless you specify the version to use explicitly (as documented below).
- `BRIDGECLI_DOWNLOAD_URL`: Use this to specify the URL to Bridge CLI zip file to be downloaded and used. Examples: `BRIDGECLI_DOWNLOAD_URL:
  https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/bridge-cli-bundle-win64.zip` or `BRIDGECLI_DOWNLOAD_URL:
  https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/3.11.0/bridge-cli-bundle-3.11.0-win64.zip`.

  Note: If `BRIDGECLI_DOWNLOAD_URL` is not provided, Black Duck Security Scan Extension downloads the latest version of Bridge CLI from [repo.blackduck.com](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/latest/).
- `BRIDGECLI_DOWNLOAD_VERSION`: Use this to specify the Bridge CLI version to use. If provided, the specified version of Bridge CLI is automatically downloaded from [repo.blackduck.com](https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/bridge/binaries/bridge-cli-bundle/) and used. If not, the latest version is downloaded and used. Example: `BRIDGECLI_DOWNLOAD_VERSION: "3.8.1"`.

  Note: If both `BRIDGECLI_DOWNLOAD_VERSION` and `BRIDGECLI_DOWNLOAD_URL` are provided,`BRIDGECLI_DOWNLOAD_URL` takes precedence.
- `NETWORK_AIRGAP`: If the `NETWORK_AIRGAP` is set to `true`, Black Duck Security Scan Extension for Azure DevOps does not download the Bridge CLI but instead uses the pre-configured Bridge CLI. If the Bridge CLI is configured at a specific location, provide the path through `BRIDGECLI_INSTALL_DIRECTORY`. The Black Duck Security Scan Extension for Azure DevOps looks for the Bridge CLI in the `BRIDGECLI_INSTALL_DIRECTORY` path. If that is not present, it looks for Bridge CLI in the default path (`$HOME/bridge-cli`).

  Note: If you use Black Duck SCA, download and set up an airgapped version of Detect under `$HOME/.bridge/blackduck`. To use a custom location, set `DETECT_INSTALL_DIRECTORY` to point to the Detect installation directory.

  Note: If `NETWORK_AIRGAP` is enabled, `BRIDGECLI_DOWNLOAD_VERSION` and `BRIDGECLI_DOWNLOAD_URL` are ignored.

  `INCLUDE_DIAGNOSTICS`: When set to `true,` Bridge CLI diagnostic files are created. Azure DevOps no longer supports per-pipeline retention rules. The only way to configure retention policies for YAML and classic pipelines is through the project settings. For more details, see [Set run retention policies](https://learn.microsoft.com/en-us/azure/devops/pipelines/policies/retention?view=azure-devops&tabs=yaml#set-run-retention-policies).
- `MARK_BUILD_STATUS`: Mark build status to use if policy violating issues are found. Default value: `Failed`. Supported values are: `Failed`, `SucceededWithIssues` and `Succeeded`.

  Note: `MARK_BUILD_STATUS` is applicable only for return status 8. For any other return value, mark build status is ignored.
- **Black Duck SCA scan mode in Classic Editor:** Auto Mode is the default and recommended scan mode. Auto Mode runs a full scan in non-PR (Pull Request) contexts, and it runs a rapid scan in PR (Pull Request) contexts. If needed, you may change the scan mode to Full Mode or Rapid Mode. In Full Mode, a full scan will be run for both PR and non-PR contexts. In Rapid Mode, a rapid scan will be run for both PR and non-PR contexts.

  Note: *Auto Mode is recommended for PR Comment scenarios to ensure the correct scan mode is executed by bridge-cli.*
- **Using a proxy through Azure DevOps environment:**

  For Classic Editor
  - Go to **Pipelines → Edit pipeline → Variables.**
  - Under **Pipeline variables** add:
    - `HTTP_PROXY` = `http://proxy.example.com:8080`
    - `HTTPS_PROXY` = `http://proxy.example.com:8080`
    - `NO_PROXY` = `example.com,myserver.local:443,example.org`
  - Click **Save**.

  For YAML pipelines: Define proxy variables in the YAML file:

  ```
  variables:
      - name: HTTP_PROXY
      value: http://proxy.example.com:8080
      - name: HTTPS_PROXY
      value: http://proxy.example.com:8080
      - name: NO_PROXY
      value: example.com,myserver.local:443,example.org
  ```

  Supported proxy variables for Azure DevOps

  Table 1. Proxy parameters

  | **Variable** | Description | **Example** |
  | --- | --- | --- |
  | `HTTPS_PROXY` / `https_proxy` | Proxy URL for HTTPS traffic. You can include basic authentication if required. Use this when target URL is HTTPS. | - `https://proxy.com` - `https://192.168.1.1:8080` - `https://username:password@proxy.com` |
  | `HTTP_PROXY` / `http_proxy` | Proxy URL for HTTP traffic. You can include basic authentication if required. Use this when target URL is HTTP. | - `http://proxy.com` - `http://192.168.1.1:8080` - `http://username:password@proxy.com` |
  | `NO_PROXY` / `no_proxy` | A comma-separated list of hosts or IP addresses that should bypass the proxy. Some clients only honor IP addresses when connections are made directly to the IP rather than a hostname. | - `example.com` - `example.com,myserver.local:443,example.org` |

  Note: Currently Coverity Local Scan is not supported with Proxy configuration.

  If you are using a proxy with authentication, follow these guidelines:
  - Proxy with auth: Users need to pass a username and password for authentication.

    Example: **http://user:password@proxyIP:proxyPort/**
  - Proxy with no auth: Users do not need to pass credentials for authentication.

    Example: **http://proxyIP:proxyPort/**
