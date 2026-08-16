---
title: "Set Helm keys to enable scan tool synchronization"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/set-helm-keys-to-enable-scan-tool-synchronization.html"
content_id: "u7kk7dkETn54Gd4IDI1TeQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:40.368030+00:00"
---

# Set Helm keys to enable scan tool synchronization

With scan tool synchronization configured and enabled, when you perform a `helm
install`, the current release version of the Coverity Tools kits (Thin
Client and Analysis kits) is automatically downloaded from the Black Duck registry and uploaded to the cloud storage bucket.
The Thin Client installers for this version appear in the Connect UI Available
Thin Clients window and are available to download and run scans. If you
are using the same Thin Client version as the Coverity release version, scan tool
synchronization bypasses the need for the administrator to download Thin Client
installers from the Black Duck private Docker registry and
upload them to Connect.

Note: This feature works only with the Black Duck private docker registry; it does not work with your
own private registry.

To enable scan tool synchronization and provide Black Duck registry access credentials, in the
`scan-services` Helm chart, configure the following Helm keys:

- Enable synchronization: `scan-service.tools.sync.enabled=true`
- Specify the repository credentials secret name:
  `scan-service.tools.sync.existingSecret=$SECRET_NAME`

The Helm syntax for these keys is:

```
scan-service:
  tools:
    sync:
      enabled: true
      existingSecret: $SECRET_NAME
```

where: `$SECRET_NAME` is the name of the secret that contains the Black Duck registry credentials. For the name of the secret,
see Create a scan tool synchronization secret.

For example, for a Black Duck registry credentials secret
named `blackduck-repo`:

```
scan-service:
  tools:
    sync:
      enabled: true
      existingSecret: blackduck-repo
```

For Helm key information, see also scan-service.tools.sync Helm keys.
