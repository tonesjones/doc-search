---
title: "TLS flow"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tls-flow.html"
content_id: "e~3~Fy~5TsbPVPTkxb91XQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:33.571879+00:00"
---

# TLS flow

```
1. Browser connects to https://coverity.example (port 443)
         │
         ▼
2. Gateway does TLS handshake using the cert from "coverity-tls" Secret
   ← presents tls.crt to the browser
   ← uses tls.key to prove ownership
   ← browser verifies the cert is trusted
         │
         ▼ connection is now encrypted between browser and Gateway
         │
3. Gateway decrypts the request
         │
         ▼
4. Gateway forwards plain HTTP to CIM pod on port 8080 (inside the cluster)
         │
         ▼
5. CIM processes the request and responds
         │
         ▼
6. Gateway encrypts the response and sends it back to the browser
```

The cert never reaches the CIM pod. CIM only ever sees plain HTTP from the Gateway — it
has no knowledge of TLS at this layer.
