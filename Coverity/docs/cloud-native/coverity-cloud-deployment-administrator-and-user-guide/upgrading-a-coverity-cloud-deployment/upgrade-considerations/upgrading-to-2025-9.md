---
title: "Upgrading to 2025.9"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-to-2025.9.html"
content_id: "2weyVT14sDk4jBMWHW2QrA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:32.040130+00:00"
---

# Upgrading to 2025.9

The 2025.9.0 release introduces the following changes that can impact the upgrade
process:

- This release establishes allowable units of measure for the NGINX HTTP gateway
  timeout configuration values when changing the values. These units apply whether
  creating annotations, configuring nginxConfig keys in the `cnc` Helm
  chart, or editing the NGINX ConfigMap. See NGINX HTTP error 504: Gateway Timeout and cim.cimweb.tlsSidecar Helm keys.
- This release introduces new Helm keys that enable customers to use the Helm chart to
  change values as needed for several NGINX configuration keys in the NGINX ConfigMap.
  See cim.cimweb.tlsSidecar Helm keys and Working with nginxConfig Helm keys.
- This release introduces a new set of `cache-service` environment
  variables in the `scan-services` Helm subchart, designed to address
  requirements for S3-compatible storage in a Dell ECS deployment. See Configure Dell ECS storage support and cache-service.environment Helm keys.
- This release introduces a new Coverity Connect property that you must provide when
  using custom domains for storage service configurations. See Storage service custom domains.
- With the Helm key `scan-service.jobRunner.uploadArtifacts` set to
  `"logsOnly"`, the Scan Service artifacts job runner now uploads
  analysis output, `analysis-output.zip`, in addition to logs,
  `execLog.zip`, to storage service storage (bucket, blob). This is
  true for successful and failed scans. Refer to Managing artifact upload to storage.
- Documentation: Organized documentation of scan services Helm keys into
  platform-specific sections, providing better guidance for each deployment platform,
  and linked the keys to the infrastructure creation and configuration. Refer to:
  Infrastructure and configuration, Amazon AWS infrastructure and configuration, Google GCP infrastructure and configuration, and Microsoft Azure infrastructure and configuration.
- Documentation: Improved descriptions, procedures amd Helm key descriptions for
  keystores and truststore ConfigMaps. Refer to Create a truststore ConfigMap for Connect communication over TLS.
- Documentation: Improved LDAP descriptions, emphasized the need to use the Connect
  UI to configure LDAP for the first time, described how to change LDAP
  configuration values using Helm keys, and documented the LDAP Helm keys. Refer
  to Configure LDAP and cim.ldap Helm keys.
- Documentation: Fixed an issue where a separator `–` was needed within
  a `kubectl exec -ti` command in two places. See Checking database integrity: check-integrity.sh and Resetting the Coverity Connect password: reset-admin-password.sh.
- Important:

  Do NOT USE or CHANGE ANY `cnc` Helm chart
  `cim.commitrcp4` Helm keys. These are Black Duck
  internal use only.

Additionally, consider the following.

- As recommended, copy all container images from the new Black Duck repository to a
  local repository and use your local repository to deploy Coverity cloud. To create
  your own private Coverity cloud repository, see Create your own private Docker registry.
- Download, modify as needed, and deploy the new Helm chart for the current
  release. See Downloading the Helm chart from the Black Duck public Docker registry.

The following table identifies new Helm keys in the 2025.9.0 release.

Table 1. New Helm keys in 2025.9.0

| Helm key | Notes |
| --- | --- |
| ``` cim:   cimweb:     tlsSidecar:       nginxConfig:         # Core nginx settings         worker_processes: 1         worker_connections: 1024         keepalive_timeout: 65         client_max_body_size: "100m"          # SSL/TLS settings         ssl_protocols: "TLSv1.2 TLSv1.3"         ssl_ciphers: "AESGCM:CHACHA20:-kRSA:-aNULL"         ssl_prefer_server_ciphers: "on"         ssl_ecdh_curve: "X25519:prime256v1"          # Proxy timeout settings (with units)         proxy_connect_timeout: "60s"         proxy_read_timeout: "60s"         proxy_send_timeout: "60s" ``` | `cnc` Helm chart:  These are new Helm keys that enable customers to use the Helm chart to change specific proxy timeout values in the ConfigMap.  See cim.cimweb.tlsSidecar Helm keys and Working with nginxConfig Helm keys. |

The following table identifies a Helm key whose functionality expanded in the 2025.9.0
release.

Table 2. Helm key with expanded functionality in 2025.9.0

| Helm key | Notes |
| --- | --- |
| ``` scan-service:   jobRunner:     uploadArtifacts: "" ``` | `scan-services` Helm subchart:  The default value remains "all". However, if you set the value to "logsOnly", in addition to storing logs, the job runner now also stores analysis output to the storage service storage (bucket, blob). This is true for successful and failed scans.  See Managing artifact upload to storage. |
