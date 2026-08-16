---
title: "TLS insecure proxy"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tls-insecure-proxy.html"
content_id: "1NUYKSdiswNls3piN7K_qw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:00.278498+00:00"
---

# TLS insecure proxy

TLS insecure proxy is available for customers who need to use `http`,
not `https`; for example, customers who operate within a dark site.
Note that this mode exposes you to security risks.

Configure TLS insecure proxy as follows:

- Specify the TLS proxy host (server) using either Helm key:
  `global.proxy.host` or `proxy.host`.
- Specify the TLS proxy port that the server listens on using either Helm key:
  `global.proxy.port` or `proxy.port`. The
  default port is `3128`.
- Set the TLS mode using either the `global.proxy.tlsmode` Helm
  key or the `proxy.tlsmode` Helm key. Use the default value,
  `tls`. For TLS insecure mode, set the value to
  `insecure`. The default value is
  `tls`.

For Helm key descriptions, see:

- For `global.proxy` Helm keys which are in the
  `cnc` chart and `scan-services` Helm subchart,
  see cnc_global_chart_values.html#cnc_global_chart_values__section_uwy_ftp_jdc.
- For chart and root `proxy` Helm keys which are in the
  `scan-services` Helm subchart, see proxy Helm keys.
