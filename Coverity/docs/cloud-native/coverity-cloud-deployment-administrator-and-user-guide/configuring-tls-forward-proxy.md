---
title: "Configuring TLS forward proxy"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-tls-forward-proxy.html"
content_id: "mkkBDaZguh8nGq5ddPY0UA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:58.088013+00:00"
---

# Configuring TLS forward proxy

To provide secure connections between the CNC cluster and remote clients, you can use TLS
(Transport Layer Security) forward proxy, where TLS acts as a Man-In-The-Middle between
Coverity cloud and the Internet.

You can configure forward proxy for the following TLS modes:

- TLS: The client authenticates the server.
- mTLS (mutual TLS): Both the client and the server authenticate each other.
- insecure TLS: Enables you to communicate through HTTP rather than HTTPS. Note that
  this mode exposes you to security risks.

In the procedures that follow, you will need to configure Helm keys to:

- Enable TLS proxy.
- Specify the proxy host (server).
- Specify the proxy port.
- Select the TLS proxy mode.

Note: For further information on the proxy Helm keys identified in
this section, see the following sections within this document:

- For `global.proxy` Helm keys which are in the
  `cnc` chart and `scan-services` Helm subchart,
  see cnc_global_chart_values.html#cnc_global_chart_values__section_uwy_ftp_jdc.
- For chart and root `proxy` Helm keys which are in the
  `scan-services` Helm subchart, see proxy Helm keys.
