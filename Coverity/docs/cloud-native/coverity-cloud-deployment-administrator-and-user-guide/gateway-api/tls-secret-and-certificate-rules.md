---
title: "TLS secret and certificate rules"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tls-secret-and-certificate-rules.html"
content_id: "Ixu4ENKl3FQmE_zmrwYviw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:34.889000+00:00"
---

# TLS secret and certificate rules

**1. The Secret must be in the same namespace as the Gateway.**

The Gateway API spec requires `certificateRefs` to be in the same
namespace as the Gateway itself. If the Secret is somewhere else, the Gateway will
refuse to use it and show `ResolvedRefs: False` in its status.

```
# Check: Gateway and Secret must be in the same namespace

kubectl get secret coverity-tls -n <release-namespace>

kubectl get gateway <release>-gateway -n <release-namespace>
```

**2. The Secret must have exactly the keys `tls.crt` and
`tls.key`.**

These are the standard keys Kubernetes expects in a TLS Secret. If you create the
Secret manually using files, `kubectl create secret tls` sets these
keys automatically.

**3. The certificate must cover the hostname you set in
`cim.gateway.hostnames`.**

If the cert is for `coverity.example` but `hostnames`
is `["coverity.mycompany.com"]`, browsers will show a certificate
mismatch warning and requests will fail.

## How to verify it is working

```
# 1. Check the Gateway accepted the cert (look for ResolvedRefs: True)
kubectl describe gateway <release>-gateway -n <namespace>

# 2. Check the cert the Gateway is presenting matches what you expect
echo | openssl s_client -connect coverity.example:443 -servername coverity.example 2>/dev/null \
  | openssl x509 -noout -subject -dates

# 3. Quick HTTP test — expect 200
curl -sk -o /dev/null -w "%{http_code}\n" https://coverity.example/login/login.htm
```

If step 1 shows `ResolvedRefs: False`, the most common causes are:

- Secret does not exist in the release namespace
- Secret name in `tlsSecretName` is misspelled
- Secret is missing the `tls.crt` or `tls.key`
  keys
