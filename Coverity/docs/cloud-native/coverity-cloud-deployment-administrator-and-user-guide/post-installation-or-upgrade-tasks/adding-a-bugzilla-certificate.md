---
title: "Adding a Bugzilla certificate"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-a-bugzilla-certificate.html"
content_id: "hRMGKFsafhzseiw5OgaVVQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:41.661705+00:00"
---

# Adding a Bugzilla certificate

If you are using Bugzilla, you can configure Bugzilla in Connect as described in section
"Integrating with other (non-JIRA) bug tracking systems" in the Coverity Platform 2026.6.0 User and Administrator Guide.

To use TLS with Bugzilla, add the Bugzilla certificate to the
`connect-trust-stores` configmap as described in Creating a truststore ConfigMap for a Connect instance.
