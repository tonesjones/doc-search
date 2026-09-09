---
title: "Proxies"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/proxies.html"
content_id: "cn0GUfzZ5jAU2mWsGMt8PQ"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:33.054710+00:00"
content_hash: "f5dca9df3a179d53db5f6454b96171023699e28ad4aa48b2f1f5bf7e97c2fa26"
---

# Proxies

Some features, like JIRA Integration and Tool
Connectors, reach out to third-party programs via HTTP(S). If your Software
Risk Manager server is running behind a proxy, you can configure Software Risk Manager
to use that proxy for communications with these programs by setting the appropriate
properties:

- `proxy.host` - The hostname, or address, of the proxy server,
  e.g., `1.2.3.4` or
  `myproxy.mydomain.com`.
- `proxy.port` - The port number of the proxy server (default:
  80).
- `proxy.username` - The username for authentication, if
  necessary.
- `proxy.password` - The password for authentication, if
  necessary.
- `proxy.nonProxyHosts` - A `|`-separated list of
  hosts that should be accessed without going through the proxy. (default:
  `localhost|127.*|[::1]`)

A typical proxy configuration in your `codedx.props` file would resemble
the following:

```
proxy.host = 123.234.156.178
proxy.port = 3128
proxy.username = myproxyuser
proxy.password = myproxypassword
```
