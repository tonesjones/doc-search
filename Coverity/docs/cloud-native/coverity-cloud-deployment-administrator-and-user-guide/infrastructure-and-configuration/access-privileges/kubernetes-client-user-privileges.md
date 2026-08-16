---
title: "Kubernetes client user privileges"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/kubernetes-client-user-privileges.html"
content_id: "KQSuW61cWAhLVhCTkYUmnQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:50.424518+00:00"
---

# Kubernetes client user privileges

The administrator who is installing Coverity cloud needs privilege to be able to access,
delete, update, and deploy the following resources in the Coverity cloud namespace:

- configmap
- cronjob
- deployment
- ingress
- job
- role
- rolebinding
- secret
- service
- serviceaccount
- statefulset

Other roles such as upgrading and managing might require different privileges to manage
the resources. You can set up attribute-based access control (ABAC) or role-based access
control (RBAC) depending on your needs. Configure privileges with attention to
security.

For information on Kubernetes access control, refer to the Kubernetes documentation,
<https://kubernetes.io/docs/reference/access-authn-authz/authorization/>.
