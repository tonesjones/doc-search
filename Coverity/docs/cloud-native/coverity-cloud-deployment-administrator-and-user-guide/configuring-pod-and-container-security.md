---
title: "Configuring pod and container security"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-pod-and-container-security.html"
content_id: "Jp7tESYh~Za9iYqr4tdzOA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:00.950886+00:00"
---

# Configuring pod and container security

For container security in a Kubernetes cluster, you should run containers with read-only
immutable root file systems. Immutable file systems prevent malicious binaries from being
added to PATH at run-time. The features listed in the following table and in this chapter
provide container security that reduces container risks and increases security.

Table 1. Key values for pod and container security

| Security condition | Key value | Refer to |
| --- | --- | --- |
| Avoid running containers as root. | ``` containerSecuritycontext {   runAsNonRoot: true } ``` | Pod and container security context Helm keys |
| Avoid privilege escalation in containers. | ``` containerSecuritycontext {   allowPrivilegeEscalation: false } ``` | Pod and container security context Helm keys |
| Enforce immutable (read-only) root filesystems for containers. | ``` containerSecuritycontext {   readOnlyRootFilesystem: true } ``` | Pod and container security context Helm keys |
| Disable automounting API credentials in Kubernetes clusters. | `automountServiceAccountToken: false` | automountServiceAccountToken Helm keys |

This chapter introduces the following pod and container security elements:

- For `podSecurityContext` and
  `containerSecurityContext` Helm keys, see
  Pod and container security context Helm keys.
- For `automountServiceAccountToken` Helm keys. See automountServiceAccountToken Helm keys.
- To generate a Connect service account admin user token. See Generate a Connect SA admin user token.
