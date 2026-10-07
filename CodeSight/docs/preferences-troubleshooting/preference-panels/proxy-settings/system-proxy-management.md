---
title: "System proxy management"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/system-proxy-management.html"
content_id: "rEhw5ir9840yJmGt4cMbOg"
version: "2026.9.0"
section: "Code Sight: Preferences and Troubleshooting"
scraped_at: "2026-10-06T23:39:57.022644+00:00"
---

# System proxy management

Operating systems support a variety of ways to configure proxies.
This section describes how the Code Sight Use System Proxy setting
interacts with those configuration options.

These are common ways to configure a proxy at the system level:

- Proxy Auto Configuration (PAC)

  This is implemented by a PAC file, which can be local or can reside on a server.
  Code Sight uses this configuration when Use System Proxy is chosen.
  See the following section, “Proxy Auto Configuration (PAC) Support”.
- Web Proxy Auto Discovery (WPAD)

  Not supported by Code Sight. If WPAD is the
  operating system’s current proxy configuration, no proxy will be
  used.
- Manual proxy settings

  These are user-specified proxy settings at the operating system level.
- Environment variables

  The environment variables `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY`
  can specify a proxy configuration.

The section “Order of Precedence” in Proxy settings describes how Code Sight chooses which proxy configuration to use.

## Proxy Auto Configuration (PAC) support

The following requirements apply to obtaining a PAC file:

- If the file is hosted on a secure (`https`) server, a valid SSL certificate is required for Code Sight to download the PAC file.
- If the file is hosted on a nonsecure (`http`) server, the `Content-Type` header of the PAC file should be
  either `application/x-ns-proxy-autoconfig` or `application/x-javascript-config`.
- The HTTP response to download the PAC file should have the `Content-Length` header set. The size of the PAC file must be less than 1MB.

For a request URL, the PAC file might return a string; for example, `"PROXY w3.proxy.com:8080; PROXY w2.proxy.com:8081; DIRECT"`.
Code Sight interprets this string by traversing the systems it names: it first tries w3.proxy.com:8080, if that server is not online,
Code Sight then tries w2.proxy.com:8081, and if that is offline as well, Code Sight connects to the Net without using a proxy.

The following list explains how Code Sight processes the proxy servers obtained from the PAC file:

1. Code Sight maintains a list of all the proxy servers retrieved from the PAC file.
2. A periodic status check is made for each proxy server, to see whether the server is online or not.
   The interval betweem status checks is 60 minutes by default, and the minimum interval is 30 minutes.
   This can be configured by an environment variable,  `CODESIGHT_PAC_PROXY_SERVERS_REFRESH_INTERVAL`.

   If set, the value of `CODESIGHT_PAC_PROXY_SERVERS_REFRESH_INTERVAL` overrides the default refresh interval.
   The value must end in with a time-unit specification: either `m` for minutes or `h` for hours.
3. If a preferred proxy server is offline, Code Sight tries to use the next server in the list, and so on.
4. If all the listed proxy servers are unreachable and the string returned by the PAC file doesn’t have `DIRECT` at its end,
   the request will fail.
5. If the status of the proxy server was online the last time it was checked, but the proxy server is not reachable when the request is processed,
   the request fails and Code Sight *does not retry* the request on its own.

## System-specific proxy support

Windows
:   There is no support for authenticated manual proxies.

    There is no support for a separate `https` manual proxy.
    The specified `http` proxy is used for `https` URLs as well.

Linux
:   All the GNU-based Linux variants, such as Ubuntu and CentOS™, are supported.

    There is no support for authenticated manual proxies.

    The Ignore Hosts list is not supported.

macOS
:   For authenticated manual proxies (that is, for the HTTP and HTTPS settings),
    Code Sight needs read access to the Internet Passwords store of the Keychain.

    If you are using a virtual private network (VPN) and the virtual interface created for the VPN does not appear in the macOS
    Network preferences, then Code Sight will not be able to read the configured proxy settings.
    This is because Code Sight cannot figure out which network device (Wi-Fi adapter, Ethernet, and so on) to use with the virtual interface
    and read the proxy settings. macOSX allows different proxy settings for different network devices: knowing the network device name is essential.

    In the Advanced Network preferences panel → Proxies tab, the
    Bypass proxy settings for these Hosts & Domains list applies only to the manual proxy
    HTTP and HTTPS settings.
