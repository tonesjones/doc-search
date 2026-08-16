---
title: "Creating secret(s) for PostgreSQL access"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-secret-s-for-postgresql-access.html"
content_id: "y66PUbGZEE6X6CXavv~ppw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:04.116228+00:00"
---

# Creating secret(s) for PostgreSQL access

You can either create one secret to support PostgreSQL access by all services, or create
a secret for each service (Connect, Scan Service, Storage Service). Create Kubernetes
PostgreSQL secret(s) using the kubectl command. Each secret must
contain the `host`, `port`, `password` and
`username` keys. Use the following command syntax to create the
secret:

```
kubectl create secret generic "${secretName}" \
 --from-literal=host="${host}" \
 --from-literal=port="${port}" \
 --from-literal=password="${password]" \
 --from-literal=username="${username}"
```

For example, for a secret named postgres-secret, connecting to a PostgreSQL server named
cim, using default port 5432 and configured PostgreSQL credentials user=postgres and
password=postgres.

```
kubectl create secret generic postgres-secret \
 --from-literal=host=cim \
 --from-literal=port=5432 \
 --from-literal=password=postgres \
 --from-literal=username=postgres
```

For each PostgreSQL secret that you create, you need to provide the name of the secret in
the corresponding Helm key in the `values.yaml` file:

For port support, see Ports.

Refer to Specify PostgreSQL credentials using secrets.

Alternatively, you can specify an existing Kubernetes PostgreSQL secret using the
`--set` option in the `helm install` command as
described in Using the helm install command.
