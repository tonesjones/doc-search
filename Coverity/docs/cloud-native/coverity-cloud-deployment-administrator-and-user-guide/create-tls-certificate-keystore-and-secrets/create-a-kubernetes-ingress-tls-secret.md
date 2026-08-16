---
title: "Create a Kubernetes ingress TLS secret"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-kubernetes-ingress-tls-secret.html"
content_id: "x0NG5QPtQ4m6QTe5gXnyNg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:01.528741+00:00"
---

# Create a Kubernetes ingress TLS secret

To secure network communication between the client and the cluster, you must provide a
Kubernetes TLS secret key. The ingress controller uses this secret for traffic entering
the cluster bound for Connect. For information on generating the certificates that are
included within this secret, see Generating a Connect TLS certificate.

Create a secret for a Connect instance using the `kubectl` command. For
example:

```
kubectl create secret tls "${ingressSecretName}" \
  --namespace "${NS}" \
  --key tls.key \
  --cert tls.crt
```

When you create Helm overrides, you will need to provide the name of this secret in the
Helm key:
`cim.ingress.tls[0].secretName=ingressSecretName`
as described in cnc Helm chart: Helm keys.
