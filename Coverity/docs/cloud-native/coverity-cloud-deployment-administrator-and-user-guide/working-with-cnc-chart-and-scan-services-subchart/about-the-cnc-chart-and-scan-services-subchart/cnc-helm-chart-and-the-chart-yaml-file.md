---
title: "cnc Helm chart and the Chart.yaml file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cnc-helm-chart-and-the-chart.yaml-file.html"
content_id: "3Sqoy9mWU_nZZ_aEhQG4PA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:14.169823+00:00"
---

# cnc Helm chart and the Chart.yaml file

The `cnc` Helm chart is a top-level parent chart that contains one
dependency subchart, the `scan-services` subchart. You can see this
dependency within the `cnc` chart's `Chart.yaml` file. The
following example illustrates the `scan-services` chart dependency under
`dependencies`:

```
apiVersion: v2
name: cnc
description: Cloud Native Coverity
type: application
version: 0.0.1
appVersion: "CNC_APP_VERSION"
keywords:
  - Coverity
dependencies:
  - name: minio
    condition: onPrem.minio
    version: "17.0.21"
    repository: oci://registry-1.docker.io/bitnamicharts
  - name: redis
    version: "23.1.3"
    condition: onPrem.redis
    repository: oci://registry-1.docker.io/bitnamicharts
  - name: scan-services
    version: "SCANSERVICES_CHART_VERSION"
    repository: "COVERITY_GAR_HELM_REPO"
    condition: scan-services.enabled
```

Under `dependencies:` in `Chart.yaml`, the
`cnc` chart contains a `scan-services` dependency that
deploys scan-services if the `scan-services.enabled` value in the
`cnc` chart is `true`. If
`scan-services.enabled` is `false`, the dependency is
invalid and scan-services is not deployed. See also scan-services.enabled Helm key.

The chart also contains the following dependencies:

- minio: Specifies on-prem MinIO. Refer to Setting up onPrem OCI Redis, MinIO, and PostgreSQL for Scan Service.
- redis: Specifies on-prem Redis. Refer to Setting up onPrem OCI Redis, MinIO, and PostgreSQL for Scan Service.

Important: If you either create a custom
`.yaml` file or set a Helm key value within a command such as
`helm install`, include cnc chart Helm keys using the syntax defined
in the cnc chart's `values.yaml` file.
