---
title: "Using a forward proxy"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-a-forward-proxy.html"
content_id: "eYUTJo1z0_auFHfMwvNVPA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:12.531589+00:00"
---

# Using a forward proxy

This section describes how to use a forward proxy when you commit analysis data to
Coverity Connect. Only fully supported protocols and command options are discussed.
These are the HTTP and HTTPS protocols and the `--url` command option.
The Commit protocol has been deprecated, as well as the `--dataport`,
`--https-port`, and `--port` command options. These
deprecated features are not discussed in this section. If you require information on how
to configure a forward proxy using these deprecated features, refer to the Knowledge
Base article [Using a forward proxy with commands that access
Coverity Connect](https://community.blackduck.com/s/article/Using-a-forward-proxy-with-commands-that-access-Coverity-Connect).

You can configure `cov-commit-defects` to use a forward proxy when
transmitting data to the Coverity Connect server by setting one or more environment
variables. When the command executes, it first examines a set of environment variables
to determine whether to use a forward proxy and to acquire the proxy's URL.

The set of environment variables examined depends on which protocol is used to transmit
the data (either HTTPS or HTTP). The protocol is determined by whether you use the
`https` or the `http` URL scheme in the 
`--url` command option (note that the `commit`
scheme is deprecated).

Table 1 lists
the possible data transmission protocols and the corresponding sets of environment
variables you can use to specify the forward proxy URL. The URL must use one of the
schemes listed in the table.

You can also use environment variables to disallow proxying to specified hosts, as shown
in Table 2.

In each table, the environment variables within each set are listed in the order in which
they are examined. The value of the first environment variable with a value other than
the empty string is used. (Note that setting one of these environment variables to the
empty string is functionally equivalent to leaving it unset.)

Environment variables in Table 2 take precedence
over those in Table 1. For
example, if `no_proxy` is set to `*`, requests will not be
proxied, regardless of how any other environment variable is set.

Table 1. Environment variables used to specify the forward proxy URL

| Data transmission protocol | Proxy URL environment variables (in order examined) | Valid schemes for proxy URL |
| --- | --- | --- |
| HTTPS | `https_proxy  HTTPS_PROXY  all_proxy  ALL_PROXY` | `http  https  socks4  socks4a  socks5  socks5h` |
| HTTP | `http_proxy  all_proxy  ALL_PROXY` |

Table 2. Environment variables used to limit or disallow proxying

| Data transmission protocol | Proxy-limiting environment variables (in order examined) | Valid values |
| --- | --- | --- |
| HTTPS | `no_proxy  NO_PROXY` | - Set to `*` to disallow proxying to all   hosts. - Leave unset or set to the empty string to allow proxying to   any host. - Set to a comma-separated list of host names to disallow   proxying to those hosts (including their subdomains).  **Note:** A leading period (for   example, `.my_host.com`) allows proxying to   the primary domain but disallows proxying to all subdomains   of the host. In this example, communication with   `my_subdomain.my_host.com` would not be   proxied, but communication with `my_host.com`   would be proxied. |
| HTTP | `no_proxy  NO_PROXY` |
