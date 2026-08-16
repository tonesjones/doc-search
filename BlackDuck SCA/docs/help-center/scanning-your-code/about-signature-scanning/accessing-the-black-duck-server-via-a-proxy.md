---
title: "Accessing the Black Duck server via a proxy"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/accessing-the-black-duck-server-via-a-proxy.html"
content_id: "fOcyzYzu8K4tdyWwla53AQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:37.343720+00:00"
---

# Accessing the Black Duck server via a proxy

[HUB-7480 -CHANGE NAME]If the client
running the component scans communicates with Black Duck via a proxy
server, for example, the Black Duck instance is located outside of your
company and your company policy requires a proxy server, you must set a SCAN_CLI_OPTS
environment variable prior to running the client. If this environment variable is not
configured, scans will fail.

The Black Duck scan client supports Digest, Basic, and NTLM
authentication.

For an HTTP proxy server:

```
SCAN_CLI_OPTS=-Dhttp.proxyHost=<ProxyHostName> -Dhttp.proxyPort=<ProxyPort> -Dhttp.nonProxyHosts=<NonProxyHostName> -Dhttp.proxyUser=<Username> -Dhttp.proxyPassword=<Password>
```

For an HTTPS proxy server:

```
SCAN_CLI_OPTS=-Dhttps.proxyHost=<ProxyHostName> -Dhttps.proxyPort=<ProxyPort> -Dhttp.nonProxyHosts=<NonProxyHostName> -Dhttp.proxyUser=<Username> -Dhttp.proxyPassword=<Password>
```

For NTLM authentication:

```
SCAN_CLI_OPTS=-Dhttp.proxyHost=<ProxyHostName> -Dhttp.proxyPort=<ProxyPort> -Dhttp.proxyUser=<Username> -Dhttp.proxyPassword=<Password> -Dhttp.auth.ntlm.domain=<ntlmDomain> -Dblackduck.http.auth.ntlm.workstation=<ntlmWorkstation>
```

where

- (required) **<ProxyHostName>** The name of the proxy server host.
- (required)**<ProxyPort>** The port on which the proxy server host is
  listening.
- (optional)**<NonProxyHostName>** The name of any non-proxy hosts. These are
  servers that are trusted and do not need to go through the proxy server.
- (optional)**<Username>** Username to access the proxy server.
- (optional)**<Password>** Password to access the proxy server.
- (if required by proxy server for NTLM authentication) **<ntlmDomain>** The
  domain to authenticate within.
- (if required by proxy server for NTLM authentication) **<ntlmWorkstation>**
  The workstation the authentication request is originating from. Essentially, the
  computer name for this machine.

To configure the SCAN_CLI_OPTS environment variable in Linux or Mac OS X:

1. Start a terminal session.
2. At the command line, type

   ```
   export SCAN_CLI_OPTS="<variable values>"
   ```
3. Close the terminal session.

To configure the SCAN_CLI_OPTS environment variable in Windows:

1. Access the System Properties dialog box. For example, from the Control Panel,
   click  **System > Advanced System Settings**.
2. Select the **Advanced** tab and click **Environment Variables**.
3. In the Environment Variables dialog box, under **System Variables**, click
   **New**.
4. Enter the following information:

   **Variable Name**: SCAN_CLI_OPTS

   **Variable value**: `<Variable Values>`
5. Click **OK**.

For information on resolving proxy errors in ,Black Duck refer to Resolving Proxy
Errors.
