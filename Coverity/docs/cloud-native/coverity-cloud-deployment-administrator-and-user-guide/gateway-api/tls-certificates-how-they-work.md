---
title: "TLS certificates — how they work"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tls-certificates-how-they-work.html"
content_id: "OTa_6Y62OGrISxjsKptgtw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:32.924107+00:00"
---

# TLS certificates — how they work

A TLS Secret is a standard Kubernetes Secret that holds two things:

| Key | What it is |
| --- | --- |
| `tls.crt` | Your certificate — the public file you get from your CA (plus any intermediate chain) |
| `tls.key` | Your private key — the matching private file you generated locally |

You create it once with `kubectl`:

```
kubectl create secret tls coverity-tls \
  --cert=path/to/tls.crt \
  --key=path/to/tls.key \
  -n <release-namespace>
```

Then you tell the chart its name:

```
cim:
  gateway:
    listeners:
      https:
        tlsSecretName: "coverity-tls"   # ← the Secret you just created
```

The chart places it into the Gateway resource:

```
# rendered by gateway-resource.yaml
spec:
  listeners:
  - name: https
    port: 443
    protocol: HTTPS
    tls:
      certificateRefs:
      - name: coverity-tls   # ← from tlsSecretName
        kind: Secret
```

The Gateway (NGF or GKE LB) reads this Secret and uses it to perform the TLS handshake
with every browser or client that connects on port 443.
