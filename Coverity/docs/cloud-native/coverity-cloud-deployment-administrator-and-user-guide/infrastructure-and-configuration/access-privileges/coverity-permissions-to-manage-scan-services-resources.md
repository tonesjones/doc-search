---
title: "Coverity permissions to manage Scan Services resources"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-permissions-to-manage-scan-services-resources.html"
content_id: "wDhwmoYTZh1vIBMgj50ahw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:51.081555+00:00"
---

# Coverity permissions to manage Scan Services resources

If you deploy Coverity Scan Services in a Kubernetes cluster, the administrator who is
installing Coverity cloud Scan Services needs privileges to be able to access, delete,
update, and deploy the following resources in the Coverity cloud namespace:

- jobs
- pods
- pod logs
- secrets
- config maps

For information on Kubernetes access control, refer to the Kubernetes documentation, <https://kubernetes.io/docs/reference/access-authn-authz/authorization/>.
