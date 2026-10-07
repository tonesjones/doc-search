---
title: "Proxy settings"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/proxy-settings.html"
content_id: "_Vc1W~1kDp00Mhd2BWazXw"
version: "2026.9.0"
section: "Code Sight: Preferences and Troubleshooting"
scraped_at: "2026-10-06T23:39:56.957641+00:00"
---

# Proxy settings

If your system runs behind a proxy server, these settings enable Code Sight
to run using the proxy.

Figure 1. Proxy preferences
  
 [image: Controls for enabling proxies]

- Use System Proxy (the default)

  When chosen, Code Sight reads the proxy configuration from OS settings and uses this proxy configuration to when making HTTP requests.
  For detailed information, see System proxy management.

  Attention:
  If you are upgrading to Code Sight 2022.6.0 or a later release from a release of Code Sight prior to 2022.6.0, the resulting proxy choice depends on
  the preferences in your previous installation.
  For more information, please see
  Proxy settings when upgrading to Code Sight 2022.6.0 or later.
- No Proxy

  When chosen, Code Sight uses no proxy.
- Manual Proxy

  When chosen, Code Sight uses the proxy information that you manually enter here.

Note:
For Code Sight running in Eclipse, in a JetBrains IDE (including IntelliJ), or in Visual Studio, there is also a shortcut link to this panel from the
Products and Licenses panel.

## Order of precedence

Code Sight determines which proxy configuration to use according to the following sequence:

1. No Proxy

   No proxy is used, not even if one has been set up at the system level.
2. Manual Proxy

   Code Sight uses the proxy settings specified in the Preferences dialog.
3. Use System Proxy

   Code Sight obtains proxy settings by inspecting system proxy settings in the following order:

   1. Environment variables

      If these specify a proxy server, Code Sight uses them.
   2. WPAD configuration

      Not supported. If a WPAD configuration is present, Code Sight does not use a proxy at all.
   3. PAC configuration

      If a PAC configuration is present, Code Sight uses that.
      See “Proxy Auto Configuration (PAC) Support” in System proxy management.
   4. Manual proxy

      If the platform’s manual proxy controls have specified a proxy server, Code Sight uses this.

## Settings for manual proxy

HTTP and HTTPS:
You can enable proxy for HTTP and HTTPS URLs independently.
HTTP specifies an HTTP proxy
and HTTPS specifies an HTTPS proxy.
The controls for each kind of server are the same, as described in this section.

Host Name
:   The name of the proxy server.
    Whether you specify HTTP or HTTPS,
    this choice should match the protocol used by the Coverity Connect server.

    The host name does not need to be prefixed with a protocol.
    If it is not, then `http://` is used.

    Specify a protocol if the protocol used by the proxy server *is different from*
    the protocol used by the Coverity Connect server: If it is, the protocol string in this
    field should match the proxy server.

    If the host name is prefixed with `http://` or `https://`,
    Code Sight will only communicate with the proxy using the specified protocol.

    Do not include a port-number suffix (see the next field).

Port Number
:   The port number that the proxy uses.

Proxy Authentication
:   Turn on to enable credentials for Code Sight to use when it accesses the proxy.

    Only Basic authentication is supported at this time.

Login
:   The username value for the proxy.

Password
:   The password associated with the username.

No proxy for

This field lists systems for which the proxy *will not* be used.

Entries in the list must be separated by commas.
The following rules apply:

- Each system is represented by an IP address prefix (1.2.3.4), an IP address prefix in CIDR notation (1.2.3.4/8),
  a domain name (URL), or a special DNS label (*).
- An IP address prefix and domain name can also include a literal port number (1.2.3.4:80).
- A domain name matches that domain and all subdomains.
- A domain name with a leading dot ( . ) matches subdomains only.
  For example test.com matches both test.com
  and play.test.com;
  .y.com matches x.y.com but
  *does not* match y.com.
- Domain names can use the asterisk wildcard character ( * ).
  IP addresses cannot use wildcards.
