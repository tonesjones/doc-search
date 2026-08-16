---
title: "IP allowlisting on Azure ALB"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ip-allowlisting-on-azure-alb.html"
content_id: "sGcOukwdgV1Da4EHOTtVyw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:46.305413+00:00"
---

# IP allowlisting on Azure ALB

`allowedSourceRanges` and `gatewayAllowedSourceRanges` are
NGF-only. The chart does not render `SnippetsFilter` or
`SnippetsPolicy` resources when `gatewayClassName`
starts with `azure-alb`, so setting these values has no effect on Azure
deployments. Use Azure-native controls instead:

- **Azure WAF policy** — attach a WAF policy to the AGfC for L7 IP filtering.
- **Network Security Group** — restrict inbound traffic to the
  `aks-appgateway` subnet.

**Troubleshooting (Azure ALB)**

| Symptom | Cause | Fix |
| --- | --- | --- |
| Gateway shows `PROGRAMMED = False` after 5+ min | `ApplicationLoadBalancer` CR missing or still provisioning | `kubectl get applicationloadbalancer -n <ns>` — wait for `Provisioned` status. |
| Gateway has no annotations / not bound to ALB | `cim.gateway.annotations` not set in values | Set both `alb.networking.azure.io/alb-name` and `alb.networking.azure.io/alb-namespace` to match the CR. |
| All requests return 502 — Gateway and HTTPRoutes show `Programmed`/`Accepted` | Cluster uses Kubenet networking | Pod IPs are not routable from the ALB subnet on Kubenet, so requests silently fail even though the control plane looks healthy. Recreate the cluster with `--network-plugin azure` (classic Azure CNI) or `--network-plugin azure --network-plugin-mode overlay` (Azure CNI Overlay — matches Step 1). |
| `no healthy upstream` from AGfC | `HealthCheckPolicy` missing or wrong path | The chart auto-creates it for `azure-alb*` GatewayClasses — check `kubectl get healthcheckpolicy -n <ns>`. If using a custom context path, set `cim.gateway.healthCheck.requestPath`. |
| `kubectl get gatewayclass azure-alb` returns nothing | Wrong class name | The installed classes are `azure-alb-external` and `azure-alb-internal`, not `azure-alb`. |
| DNS A record returns NXDOMAIN | Used an A record instead of CNAME | AGfC publishes an FQDN, not an IP. Use a CNAME record. |
| Terraform blocks CNI migration with an error about managed identity | Cluster has system-assigned identity; Azure requires user-assigned for in-place CNI migration | There is no safe in-place path. Provision a new cluster with Azure CNI and a user-assigned identity, then migrate workloads. See the warning note in the existing-cluster update step above. |
| Gateway has no address after deploy | ALB still provisioning | `ApplicationLoadBalancer` CR provisioning takes 2–5 minutes. Watch with `kubectl get applicationloadbalancer -n <ns> -w` and wait for `Provisioned` status before checking the Gateway address. |
