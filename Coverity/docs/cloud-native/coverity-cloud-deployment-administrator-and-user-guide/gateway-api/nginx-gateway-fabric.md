---
title: "NGINX gateway fabric"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/nginx-gateway-fabric.html"
content_id: "VWUJEssRKrqo1DX9i2zEew"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:32.272077+00:00"
---

# NGINX gateway fabric

Client ──HTTPS──► NGINX Gateway Fabric ──HTTP──► CIM pod :8080

(TLS terminated here) (plain HTTP listener) │ HTTP :80 → 301 redirect → HTTPS

**Which backend port does the Gateway use?**

It depends on whether scan-services is enabled:

The Gateway **always uses port 8080**, regardless of whether scan-services is
enabled.

| `scan-services.enabled` | Gateway backend port | Why |
| --- | --- | --- |
| `false` (default) | **8080** | TLS terminated at the Gateway listener; plain HTTP forwarded to CIM pod |
| `true` | **8080** | Same — the HTTPRoute templates hardcode `port: 8080`; mTLS between scan-services and cimweb is a pod-to-pod concern that does not involve the Gateway |

NGINX Gateway Fabric terminates TLS at the listener and always forwards plain HTTP to
port 8080 on the CIM pod. The `cim-httproute.yaml` template hardcodes
`port: 8080` unconditionally — there is no automatic switch to 8443.
The mTLS requirement between scan-services and cimweb operates at the pod level and is
independent of the Gateway backend port.

**Security comparison: Gateway vs Ingress**

| Traffic leg | NGINX Ingress (old) | Gateway API (new) |
| --- | --- | --- |
| Client → load balancer | TLS — encrypted | TLS — encrypted |
| Load balancer → CIM pod | **HTTPS re-encrypted → port 8443** (when scan-services on) / plain HTTP → port 8080 (off) | **Plain HTTP → port 8080 always** |
| scan-services → CIM pod | mTLS → port 8443 | mTLS → port 8443 (unchanged) |

The only traffic leg that changed is load balancer → CIM pod. With Ingress +
scan-services enabled, that leg was TLS-encrypted (the Ingress re-encrypted to the TLS
sidecar on port 8443 via `backend-protocol: HTTPS`). With Gateway it is
always plain HTTP to port 8080.

**Was the Ingress double-TLS a deliberate security feature?**

No. It was a side effect of the scan-services architecture: scan-services required a TLS
sidecar on port 8443 for pod-to-pod mTLS, and since that sidecar was already present,
the Ingress was configured to use it too. When scan-services was disabled the Ingress
already used plain HTTP to port 8080 — the same as Gateway always does.

**Is the Gateway pattern safe?**

Yes for most deployments. AWS ALB, GCP Load Balancer, and Azure Application Gateway all
use this same pattern — terminate TLS at the edge, forward plain HTTP to the backend.
The CIM Service is ClusterIP and never reachable from outside the cluster. To intercept
the Gateway → CIM leg an attacker would already need to have compromised a node or be
running a rogue pod inside the cluster.

| Leg | Protocol |
| --- | --- |
| Client → Gateway (port 443) | TLS 1.2/1.3 — fully encrypted |
| HTTP requests (port 80) | Redirected to HTTPS via 301 |
| Gateway → CIM pod (port 8080) | Plain HTTP — ClusterIP, never leaves cluster |
| scan-services → cimweb (port 8443) | mTLS — encrypted pod-to-pod (unchanged) |

**Compliance-sensitive environments (PCI-DSS, HIPAA, FedRAMP)**

If your compliance framework requires encryption of all in-transit data including
intra-cluster traffic, the plain HTTP leg may need to be addressed. Recommended
mitigations in order of increasing overhead:

| Mitigation | What it does |
| --- | --- |
| Kubernetes `NetworkPolicy` | Restricts which pods can reach CIM on port 8080 — limits blast radius |
| CNI encryption (Calico WireGuard / Cilium) | Encrypts all node-to-node traffic at the network layer transparently — plain HTTP becomes encrypted on the wire without any app changes |
| Service mesh (Istio / Linkerd) | mTLS for all pod-to-pod traffic — strongest guarantee, most operational overhead |
