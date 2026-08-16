---
title: "Installing the chart release for a single Coverity instance"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/installing-the-chart-release-for-a-single-coverity-instance.html"
content_id: "uHrK8aHLEAHkg3EUqucg1w"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:36.846792+00:00"
---

# Installing the chart release for a single Coverity instance

For some installs, you might create a modified values.yaml file that provides all
overrides needed for the installation. For example, you might create a new modified
values file to install a single instance of Connect in a specified namespace in the
Kubernetes cluster.

```
helm install ${chartName} \
    --version "${coverityVersion}" \
    --repo ${repository-path} \
    -n "${NS}" \
    -f ${modifiedValuesFile}.yaml
```

For example, to deploy a single instance of Coverity Connect using:

- a chart release named `connect`
- for Coverity version 2026.6.0
- located in a private registry `cov-registry/cnc`
- to namespace `cnc-connect`
- using a modified `connect.yaml` values file that overrides default
  chart values

the command is:

```
helm install connect \
--version 2026.6.0 cov-registry/cnc \
-n cnc-connect
-f connect.yaml
```

You can use this command to install either Connect-only or Connect and Scan Service chart
releases. Your settings in the override file, `connect.yaml` in this
example, define the deployment.
