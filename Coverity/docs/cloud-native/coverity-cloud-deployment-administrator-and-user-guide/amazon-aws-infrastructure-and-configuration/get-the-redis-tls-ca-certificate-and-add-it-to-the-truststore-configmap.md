---
title: "Get the Redis TLS CA certificate and add it to the truststore ConfigMap"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/get-the-redis-tls-ca-certificate-and-add-it-to-the-truststore-configmap.html"
content_id: "h2AeuyfB_0nzpW0CMPfSNQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:18.024235+00:00"
---

# Get the Redis TLS CA certificate and add it to the truststore ConfigMap

1. Get the Redis TLS CA certificate. For example, you can add and manage
   certificates using AWS Certificate Manager. See <https://docs.aws.amazon.com/acm/latest/userguide/gs.html>.
2. Add the Redis CA certificate to the truststore as described in the following
   section within this document: Create a truststore ConfigMap for Connect communication over TLS
