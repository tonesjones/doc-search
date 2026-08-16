---
title: "Troubleshooting"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/troubleshooting.html"
content_id: "nbvRbMXKsFhabMztLRe30w"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:48.249287+00:00"
---

# Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| ``` 400 The plain               HTTP request was sent to HTTPS port ``` | HTTPRoute `backendRef` port was manually set to 8443 | The chart hardcodes port 8080. If you hand-edited the HTTPRoute, revert it — port 8443 is the TLS sidecar and rejects plain HTTP from the Gateway. |
| `400` on some requests only | HTTPRoute missing `sectionName` — HTTP traffic leaks to TLS backend | This is auto-set by the chart. Verify `sectionName` is present on the CIM HTTPRoute. |
| HTTPRoute status shows `Not Accepted` | Gateway `allowedRoutes.namespaces.from: Same` but route is in a different namespace | Set `listeners.http.shared: true` or `listeners.https.shared: true`. |
| Gateway status shows `Not Programmed` | GatewayClass `nginx` not found | Verify that the NGINX gateway fabric is installed: `kubectl get gatewayclass nginx`. |
| `helm template` fails with `no matches for kind Gateway` | Gateway API credentials not installed | Install the gateway API credentials. |
| IP allowlist not enforced | NGF snippets not enabled | Reinstall NGF with `--set nginxGateway.snippets.enable=true`. |
| commit-server HTTPRoute not created | `cimweb.replicas` is 1 | The commit-server HTTPRoute is only rendered when `cim.cimweb.replicas > 1`. |
| `SnippetsPolicy` not found | API version not installed | Verify NGF version supports `SnippetsPolicy`. Fallback: use `allowedSourceRanges` instead. |
| ``` 413 Request               Entity Too Large ``` | Gateway body size limit exceeded | Set `cim.gateway.clientSettings.body.maxSize` (e.g. `"500m"`). |
| GKE backend unhealthy / 503 | Health check hitting `/` or `/ccd` which return 302 | Chart deploys `HealthCheckPolicy` for CIM and commit-server automatically. Check:  ``` kubectl get healthcheckpolicy -n <ns> ```  Both should show `Reason: Attached`. Wait 2–5 min for LB reprogramming. |
| After switching from NGF to GKE, still hitting old IP | Orphaned NGF proxy pod + Service still running in namespace | Delete `<release>-gateway-nginx` pod and Service. Get new GKE Gateway IP: `kubectl get gateway <release>-gateway`. |
| 503 with `server: nginx` after switching to GKE | Testing old NGF LoadBalancer IP, not the GKE Gateway IP | Use `kubectl get gateway` for the correct IP — GKE does not use a proxy Service. |
