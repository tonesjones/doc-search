---
title: "Client settings policy"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/client-settings-policy.html"
content_id: "BTT1xDOj7IoN77m_hTRohw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:39.435766+00:00"
---

# Client settings policy

Use `clientSettings.body.maxSize` to raise the maximum request body size
at the Gateway. This is the equivalent of the
`nginx.ingress.kubernetes.io/proxy-body-size` annotation.

```
cim:
  gateway:
    clientSettings:
      body:
        maxSize: "500m"   # default NGF limit applies when not set
```

**When to set this:** If users uploading large Coverity scan results receive
`413 Request Entity Too Large` from the Gateway, increase
`maxSize` to match or exceed the expected upload size.

**What gets created:** A `ClientSettingsPolicy` resource named
`<release>-client-settings` targeting the Gateway. It is only
rendered when `maxSize` is set — no resource is created by default.

**Verification:**

```
kubectl get clientsettingspolicy <release>-client-settings -n <namespace>

kubectl describe clientsettingspolicy <release>-client-settings -n <namespace>
```
