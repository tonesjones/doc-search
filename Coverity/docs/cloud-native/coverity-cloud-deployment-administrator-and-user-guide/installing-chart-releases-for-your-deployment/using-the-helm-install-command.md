---
title: "Using the helm install command"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-the-helm-install-command.html"
content_id: "4JdrHkOu8oRh_2BQ~hAcCg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:35.247421+00:00"
---

# Using the helm install command

The following command format identifies how you can structure helm install commands for
your deployment. The examples use the following flags:

- `--version` specifies the Coverity version.
- `--repo` is the Helm chart repository for Coverity cloud.
- `-n` specifies the Coverity namespace.
- `-f` specifies a `.yaml` file that overrides default
  chart values.

```
helm install ${chartName} \
    --version "${coverityVersion}"
    --repo ${repository-path} \
    -n "${NS}" \
    -f values.yaml \   **this used by default**
    -f "${overrideFile}.yaml"
```

In the command above, the `values.yaml` is used by default. Therefore the
following command does the same installation.

```
helm install ${chartName} \
    --version "${coverityVersion}" \
    --repo ${repository-path} \
    -n "${NS}" \
    -f ${overrideFile}.yaml
```

## Specifying a PostgreSQL secret

Optionally, if not provided in the `values.yaml` file, you can specify
an existing Kubernetes PostgreSQL secret using the `--set` command in
the `helm install` command. For example:

```
helm install ... \
--set postgres.existingSecret="my-postgres-secret"
```
