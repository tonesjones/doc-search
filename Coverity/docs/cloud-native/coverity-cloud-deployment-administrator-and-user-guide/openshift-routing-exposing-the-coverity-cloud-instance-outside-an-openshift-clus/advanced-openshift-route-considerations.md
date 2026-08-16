---
title: "Advanced OpenShift route considerations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/advanced-openshift-route-considerations.html"
content_id: "Hrq4uSs2OTiNHTnWM5yUqg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:55.872331+00:00"
---

# Advanced OpenShift route considerations

This section provides information on security, performance, and routing features to
assist in configuring OpenShift routes within Coverity cloud.

## Security considerations

- TLS Termination: Use `edge` termination for most scenarios.
- Insecure connections: To force HTTPS, set insecureEdgeTerminationPolicy to
  "Redirect". Fo example, in the `cnc` Helm
  chart:

  ```
  insecureEdgeTerminationPolicy: "Redirect"
  ```
- Certificate Management: Store certificates in Kubernetes secrets with proper
  RBAC
- Network Policies: Ensure that OpenShift network policies allow route
  traffic

## Performance considerations

- Route vs Ingress: Routes are OpenShift-native and might offer better
  performance.
- TLS Termination: Edge termination provides better performance than
  passthrough.
- Keep-Alive: Configure route timeouts based on application requirements.

## OpenShift route configuration inheritance

Routes use intelligent inheritance to minimize configuration duplication:

Table 1. OpenShift route configuration inheritance

| Inheritance type | Inherited values | Description |
| --- | --- | --- |
| Host name inheritance | - `cim.route.hosts` - `cim.ingress.hosts` - `global.ingress.hosts` |  |
| TLS certificate inheritance | - `cim.route.tls.secrets` - `cim.ingress.tls` - `global.ingress.tls` | Important: When using configuration inheritance, create your TLS secrets with the standard `tls.crt` and `tls.key` keys. These secrets can be referenced in both ingress and route configurations, allowing routes to automatically inherit TLS certificates from your existing ingress setup without requiring separate certificate management. |
| Annotation inheritance | Route annotations | - Route annotations are service-specific   (`cim.route.annotations`) - No inheritance to avoid conflicts with ingress   annotations |

## Setting up TLS certificates for automatic route extraction

Routes can automatically extract TLS certificates from Kubernetes secrets. The
following template example creates a secret named `cnc-tls-secret`
that contains the generated TLS certificate and private key.

```
apiVersion: v1
kind: Secret
metadata:
  name: cnc-tls-secret
type: kubernetes.io/tls
data:
  tls.crt: <base64-encoded-certificate>
  tls.key: <base64-encoded-private-key>
```

The following `cnc` Helm chart example identifies the TLS secret
(`cnc-tls-secret` as configured in the template example above) to
be used in the enabled route:

```
cim:
  route:
    enabled: true
    tls:
      secrets:
        - secretName: "cnc-tls-secret"
          hosts: ["cnc.example.com"]
```

## Supported certificate formats

The route template supports the following certificate key formats:

- `tls.crt`
- `tls.key`

## Migrating from ingress-only to OpenShift routing

If you currently use only ingress resources and need to migrate to OpenShift
routing:

1. Review the current ingress configuration:

   ```
   cim:
     ingress:
       enabled: true
       hosts: ["cnc.example.com"]
       tls: [...]
   ```
2. Enable routes with inheritance:

   ```
   cim:
     ingress:
       enabled: true  # Keep existing ingress
       hosts: ["cnc.example.com"]
       tls: [...]

     route:
       enabled: true  # Add route with same config
   ```
3. Test the route functionality: Verify route creation and TLS termination.
4. Optional: Disable ingress if only routes are needed:

   ```
   cim:
     ingress:
       enabled: false
     route:
       enabled: true
       hosts: ["cnc.example.com"]  # Must specify explicitly
       tls: [...]  # Must specify explicitly
   ```
