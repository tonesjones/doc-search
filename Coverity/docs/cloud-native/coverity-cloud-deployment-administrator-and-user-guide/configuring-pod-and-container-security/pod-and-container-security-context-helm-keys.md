---
title: "Pod and container security context Helm keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/pod-and-container-security-context-helm-keys.html"
content_id: "HbJQKHIG_gVZzFpisIlTdw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:01.688777+00:00"
---

# Pod and container security context Helm keys

Pod-level security context extends to containers within the pod, resulting in pod
constraints being inherited by all containers that run within the pod. To avoid these
constraints for specific containers, you can set contexts for the containers using the
`containerSecurityContext` Helm keys.

See also the Kubernetes document, [Configure a Security Context for a Pod or
Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/).

You can set security context constraints for pods using the following pod security
context Helm keys:

Table 1. Pod security context

| Chart | Keys | Notes/Links |
| --- | --- | --- |
| `cnc` | ``` cim:   podSecurityContext: {} ``` | - Continue with this chapter for information on security   context constraints and using them within the Helm keys to   manage pod and container security. - For `cim.podSecurityContext: {}` Helm key   information, see cim Helm keys for pod security and node affinity. |
| `scan-services` | ``` cache-service:   podSecurityContext: {}  common-infra:   podSecurityContext: {}  scan-service:   podSecurityContext: {}  storage-service:   podSecurityContext: {} ``` | - Continue with this chapter for information on security   context constraints and using them within the Helm keys to   manage pod and container security. - For `scan-services` subchart Helm key   information, see also scan-services Helm subchart: Helm keys |

Using pod security context values for containers within the pod enforces the pod
constraints on all containers that run within the pod. To avoid these constraints, you
can set constraints at the container-level by using the
`containerSecurityContext` Helm keys.

If you do not define security context in the `containerSecurityContext`
Helm keys, the containers will inherit security context from the
`podSecurityContext` keys. Values defined in the
`containerSecurityContext` keys override the related
`podSecurityContext` key values.

You can set security context constraints for containers using the following container
security context Helm keys:

Table 2. Container security context

| Chart | Keys | Notes/links |
| --- | --- | --- |
| `cnc` | ``` cim:   cimdownloads:     containerSecurityContext: {}    cimtools:     containerSecurityContext: {}    cimweb:     containerSecurityContext: {}    cimweb:     tlsSidecar:       containerSecurityContext: {}    pgpool:     containerSecurityContext: {}    setupJob:     containerSecurityContext: {} ``` | - Continue with this chapter for information on security   context constraints and using them within the Helm keys to   manage pod and container security. - cnc Helm chart: Helm keys   Note: To perform a write operation in either a `cim-tools` pod or a `cnc-db-admin` pod, use the `/data` path. See also:  - To create a `/data` persistent volume, see   Create and mount a /data persistent volume - Read-only file system error |
| ``` cnc-db-admin:   containerSecurityContext: {} ``` | See also cnc-db-admin Helm keys.  Note: To perform a write operation in either a `cim-tools` pod or a `cnc-db-admin` pod, use the `/data` path. See also:  - To create a `/data` persistent volume, see   Create and mount a /data persistent volume - Read-only file system error |
| `scan-services` | ``` cache-service:   containerSecurityContext: {}    common-infra:     containerSecurityContext: {}    scan-service:     containerSecurityContext: {}    scan-service:     migrateJob:       containerSecurityContext: {}    storage-service:     containerSecurityContext: {}    storage-service.migrateJob:     containerSecurityContext: {} ``` | - Continue with this chapter for information on security   context constraints and using them within the Helm keys to   manage pod and container security. - For `scan-services` subchart Helm key   information, see also scan-services Helm subchart: Helm keys |
