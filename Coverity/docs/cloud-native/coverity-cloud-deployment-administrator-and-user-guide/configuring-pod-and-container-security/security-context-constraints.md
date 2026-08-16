---
title: "Security context constraints"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/security-context-constraints.html"
content_id: "3Q_4UEOXUthEjchv4m8k4Q"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:02.434896+00:00"
---

# Security context constraints

You can define container security using security context constraints in the various
SecurityContext Helm keys. A deployment automatically contains default constraints for
containers Default context constraints are A default container context value is
automatically applied for any `containerSecurityContext` key that is not
configured with a different constraint parameter=value pair. The following table
identifies a few context constraints with their default values, describes their use, and
identifies which containers they can be used within.

Table 1. Security context constraints

| Constraint | Default value | Description | Valid in containers |
| --- | --- | --- | --- |
| ``` allowPrivilegeEscalation: ``` | `false` | This constraint value `false` is the default for the containers noted. The:`false` prevents processes from gaining more privilege than its parent process. | `cnc` chart containers:   ``` cim cimdownloads cimtools cimweb cimweb > tlsSidecar pgpool setupJob ```   `scan-services` chart containers:   ``` cache-service common-infra scan-service scan-service > migrateJob storage-service storage-service > migrateJob ``` |
| ``` runAsNonRoot: ``` | `true` | This constraint value `true` prevents processes from running as root. |
| ``` runAsUser: ``` | `<uid>` | The constraint value `runAsUser: <uid>` specifies the user level that processes can run at. |
| `readOnlyRootFilesystem:` | `true` | The constraint value `true` mounts the container's root filesystem as read-only.  Important: A `readOnlyRootFilesystem` `true` value is not supported for Connect (cim) pods. | `scan-services` chart containers:   ``` cache-service common-infra scan-service scan-service > migrateJob storage-service storage-service > migrateJob ``` |

The default `containerSecuritycontext` Helm key constraints for containers
defined in the `cnc` chart are:

```
containerSecuritycontext {
  allowPrivilegeEscalation: false
  runAsNonRoot: true
  runAsUser: <uid>
}
```

The default `containerSecuritycontext` Helm key variables in the
`scan-services` chart are:

```
containerSecuritycontext {
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  runAsNonRoot: true
  runAsUser: 5000
}
```

You can override the default constraints or apply new constraints for pods or containers
as follows:

- You can apply constraints for a pod using the appropriate
  `podSecurityContext` Helm key. This value is inherited by all
  containers within that pod, except if a container has a different context
  value.
- You can apply constraints for a container using the appropriate
  `containerSecurityContext` Helm key.

Note: Parameters configured for the `scan-service` pod
are also applied to the `analysis` pods.

Important: The `scan-service` and
`analysis` pods must be configured with the same
`containerSecurityContext` settings.

For further information, you can refer to the following Kubernetes document: [Configure a Security Context for a Pod or Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/).

For information on managing security context constraints in Red Hat Open Shift, see [Managing security context constraints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.8/html/authentication_and_authorization/managing-pod-security-policies).

## runAsUser values

In a non-ubi environment, which is most of Coverity cloud,
`scan-services` pods and containers run as user 5000, except for
a few public images listed in the following table

Table 2. runAsUser values

| Container | `runAsUser` values |
| --- | --- |
| `cnc-crossbar` | `runAsUser: 242` |
| `cnc-temporal-service` | `runAsUser: 1000` Important: Future use. |
| `pgpool` | `runAsUser: 1001` |
| `temporaladmintools` | `runAsUser: 1000` Important: Future use. |
| all other containers | `runAsUser: 5000` |

To use another `userId` for `runAsUser,` ensure that
the `userId` is available.

## Example

For example, for a `pgpool` container:

```
containerSecuritycontext {
  allowPrivilegeEscalation: false
  runAsNonRoot: true
  runAsUser: 1001
}
```
