---
title: "Create OpenShift Helm overrides"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-openshift-helm-overrides.html"
content_id: "gDb8yjvqxm8WuNwVSSLXNw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:34.540499+00:00"
---

# Create OpenShift Helm overrides

In addition to other Helm chart setup considerations, if you are deploying Coverity in
Red Hat OpenShift, you must configure the Helm keys described in this section. Set Helm
keys to:

- Specify the Coverity installer image version and `-ubi` type.
- Disable the ingress controller installation if you will not use it.
- Create a project.
