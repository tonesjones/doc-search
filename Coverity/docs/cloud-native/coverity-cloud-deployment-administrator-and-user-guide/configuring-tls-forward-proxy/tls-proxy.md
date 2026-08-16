---
title: "TLS proxy"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tls-proxy.html"
content_id: "xxSXg~2SpvYUH_Ih4PG72Q"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:58.944227+00:00"
---

# TLS proxy

With TLS, the client authenticates the server. You will generate and use the following
ceretificates:

- Proxy server CA certificate, `proxy-server.pem`.
- Black Duck artifactory CA certificate, `repo.blackduck.com.pem`.

Configure TLS proxy as follows:

1. In the Helm chart, set the following Helm keys:

   - Set the TLS host using either the `global.proxy.host` Helm
     key or the `proxy.host` Helm key.
   - Set the TLS port using either the `global.proxy.port` Helm
     key or the `proxy.port` Helm key. The default port is
     `3128`.
   - Set the TLS mode using either the `global.proxy.tlsmode`
     Helm key or the `proxy.tlsmode` Helm key. Use the default
     value, `tls`.

   For Helm key descriptions, see:

   - For `global.proxy` Helm keys which are in the
     `cnc` chart and `scan-services` Helm
     subchart, see cnc_global_chart_values.html#cnc_global_chart_values__section_uwy_ftp_jdc.
   - For chart and root `proxy` Helm keys which are in the
     `scan-services` Helm subchart, see proxy Helm keys.
2. Obtain or generate the following CA certificate(s):

   - Proxy server CA certificate, which must contain the
     `proxy-server.pem` key to establish connection with
     the proxy server from any of the scan services.

     Note: The key name or file name in the truststore
     configmap is important.
   - `repo.blackduck.com.pem` - The Black Duck artifactory CA
     certificate is a Black Duck server certificate that contains the public
     key and it helps to establish connection with the Black Duck server when
     the proxy TLS mode is set to either `tls` or
     `mtls`. Also, if Tool Synchronization is enabled, the
     `scan-service.tools.sync.enabled` Helm key value is
     `true`, add the
     `repo.blackduck.com.pem` certificate. See also Generating a Coverity Connect TLS certificate signed by a Certificate Authority.

     To generate the `repo.blackduck.com.pem` certificate
     file:

     ```
     curl -w %{certs} https://repo.blackduck.com | awk '/-----BEGIN CERTIFICATE-----/, 
     /-----END CERTIFICATE-----/' > repo.blackduck.com.pem
     ```
3. Add the generated CA certificates to the truststore configmap file. See also Create a truststore ConfigMap for Connect communication over TLS.
4. Make sure that the name of the truststore configmap is set in either the
   `global.trust-stores.configmapName` Helm key or the
   `trust-stores.configmapName` Helm key.
