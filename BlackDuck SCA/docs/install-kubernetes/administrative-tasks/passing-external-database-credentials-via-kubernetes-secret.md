---
title: "Passing external database credentials via Kubernetes secret"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/passing-external-database-credentials-via-kubernetes-secret.html"
content_id: "T062aoFBQQCjXkD0Rzsucg"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:19.214640+00:00"
---

# Passing external database credentials via Kubernetes secret

When configuring Black Duck to use an external PostgreSQL database,
you can choose to supply the database credentials via a Kubernetes secret rather than
storing them directly in the `values.yaml` file. This approach enhances
security by avoiding plaintext credentials in configuration files.

## Using the default behavior (Helm-managed secret)

By default, the Helm chart will generate a secret named
`<name>-blackduck-db-creds` using the values set from
`adminPassword` and `userPassword` in your
`values.yaml` file. This behavior is controlled by the
`useHelmChartDbCreds` flag, which is enabled by default:

```
useHelmChartDbCreds: true
```

No additional steps are needed if you choose to continue using this method.

## Providing your own database credentials secret

If you prefer to manage the credentials yourself, set
`useHelmChartDbCreds` to `false` in your
`values.yaml` file:

```
useHelmChartDbCreds: false
```

You must then create a Kubernetes secret named
`<name>-blackduck-db-creds` in the same namespace as your Black Duck deployment. The secret must include the following
keys:

- `HUB_POSTGRES_ADMIN_PASSWORD_FILE`
- `HUB_POSTGRES_USER_PASSWORD_FILE`

Each key should point to a file containing the corresponding password. For
example:

```
kubectl create secret generic -n <namespace> <name>-blackduck-db-creds \
    --from-file=HUB_POSTGRES_ADMIN_PASSWORD_FILE=pg_admin_password_file \
    --from-file=HUB_POSTGRES_USER_PASSWORD_FILE=pg_user_password_file
```

Important: If the custom secret is invalid or missing, the deployment will
fail. Helm will not fall back to using the credentials specified in
`values.yaml`.
