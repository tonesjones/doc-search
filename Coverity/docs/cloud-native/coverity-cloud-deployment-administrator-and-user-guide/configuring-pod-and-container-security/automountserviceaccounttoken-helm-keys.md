---
title: "automountServiceAccountToken Helm keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/automountserviceaccounttoken-helm-keys.html"
content_id: "TZcSKpTZiytfLbqdXDWlgQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:03.754643+00:00"
---

# automountServiceAccountToken Helm keys

The `automountServiceAccountToken` parameters in determines whether each
service pod's filesystem automatically mounts a service account (SA) token. The token is
used to authenticate the service and authorize access to resources.

In the `values.yaml` files for the `cnc` chart and
`scan-services` chart, the default value for all instances of
`automountServiceAccountToken` is `false`:

```
automountServiceAccountToken: false
```

This Helm key appears in the Helm chart for each of the following services/pods.

In the `cnc` chart:

- In the `cnc` chart:
  - `cim.automountServiceAccountToken`
  - `cim.cimtools.automountServiceAccountToken`
  - `cim.pgpool.automountServiceAccountToken`
  - `cim.setupJob.automountServiceAccountToken`
  - `cnc-db-admin.automountServiceAccountToken`

    Note: Refer to the reference section, cnc Helm chart: Helm keys.
- In the `scan-services` subchart:

  - `cache-service.automountServiceAccountToken`
  - `common-infra.automountServiceAccountToken`
  - `scan-service.automountServiceAccountToken`
  - `storage-service.automountServiceAccountToken`

    Note: Refer to the reference section, scan-services Helm subchart: Helm keys.

The SA token is used to authenticate services and authorize access to resources.

You can retain the default `automountServiceAccountToken: false` values or
set then to `true` to mount the SA token for the related service(s). If
you set any key to `true`, you must create the SA token as described in
Generate a Connect SA admin user token. The single SA token supports
authentication and resource access for all services.

See also the Kubernetes document, [Configure Service Accounts for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/).
