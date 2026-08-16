---
title: "Preparing cim.cimweb Helm keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/preparing-cim.cimweb-helm-keys.html"
content_id: "P6sSsfxVWCvhjOJwPrPs9Q"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:27.346224+00:00"
---

# Preparing cim.cimweb Helm keys

The `cim.cimweb` Helm keys enable you to define Connect Web application
(cimweb) characteristics. These characteristics include:

- Enabling the Connect keystore.
- Specifying the Connect TLS certificate secret.
- Enable Kubernetes deployment
- Open and expose the commit port.
- Optional: Setting the `cim.cimweb.adminPasswordSecret` Helm key
- Optional: Specifying a context path.
- Optional: Configuring Connect Web environment variables.
- Optional: Configuring Connect properties.
- Optional: Configuring Java options.

For descriptions of the `cimweb` keys, refer to the
`cim.cimweb` keys in the `cnc` chart. See cnc Helm chart: Helm keys.
