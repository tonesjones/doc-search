---
title: "Header-Based Authentication"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/header-based-authentication.html"
content_id: "3C3ujw0yT7V~g~i83byt0g"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:24.296250+00:00"
content_hash: "9819aa20f51531b99265aad341e75e1ea1cc4dc9e84d28a66af22789e772689c"
---

# Header-Based Authentication

Software Risk Manager allows you to authenticate users via a request header. Requests to
the Software Risk Manager server which provide the configured header with a username as
its value will be treated as "logged in" as that user. You can optionally restrict the
IP addresses from which such requests can originate. For example, if you put Software
Risk Manager behind a proxy server that manages its own authentication and adds the
header only to authenticated requests, you would specify the proxy server's IP address
as the only "allowed" IP address.

The name of the request header and the set of allowed IP addresses are configured by the
following keys in the `codedx.props` file:

```
codedx.header-authentication.header = My-Magic-Authentication-Header
codedx.header-authentication.allowed-ips = 172.1.1.1, 127.0.0.1, 0:0:0:0:0:0:0:1
```

There is no default value for `header` key. If omitted, header-based
authentication will be disabled. If the `allowed-ips` key is not
specified, all IP addresses will be considered "allowed." This will also cause a warning
in your log, as it is not recommended to configure a `header` without an
`allowed-ips` whitelist.

Once configured, header-based authentication and username/password logins will be
mutually-exclusive; you cannot log in via header while already logged in via
username/password, and vice versa. There is no "log out" functionality for a
header-based session. Instead, you need to stop sending the header with your
requests.

Header-based authentication may be used to log in as *any* enabled user that has
been added to Software Risk Manager. This includes the super-admin user, all local
users, and all LDAP users. Because of this, it is highly recommended to provide an
`allowed-ips` whitelist and hide the Software Risk Manager server
behind a proxy that can manage the header.
