---
title: "containerSecurityContext and scan jobs"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/containersecuritycontext-and-scan-jobs.html"
content_id: "m_ig7CiiPhkIuHNN9c0tvw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:03.088145+00:00"
---

# containerSecurityContext and scan jobs

As noted in Security context constraints, for scan jobs, the
following default `containerSecurityContext` is used.

```
containerSecuritycontext {
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  runAsUser: 5000
}
```

If any scan service security context is configured, the configured
`containerSecurityContext` will be applied to the scan-service pods,
and the same variables will be updated for the scan jobs.

## Example

With the following context, the scan service pod mounts the container's root
filesystem as read-only, and the scan job pod(s) inherit the environment setting
`readOnlyRootFilesystem: true`.

```
scan-service:
  containerSecurityContext: {
    readOnlyRootfileSystem: true
  }
```
