---
title: "Microsoft Azure Kubernetes Service (AKS)"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/microsoft-azure-kubernetes-service-aks-.html"
content_id: "0V7Ckx0P4Ql5aNq1vBjvcg"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:28.599607+00:00"
---

# Microsoft Azure Kubernetes Service (AKS)

Two options are available on AKS: NGINX Gateway Fabric and the Azure Application Load
Balancer (ALB) Controller (Application Gateway for Containers). Choose based on your
organizational requirements and existing Azure infrastructure.

| Dimension | Option A: NGINX Gateway Fabric | Option B: Azure ALB Controller |
| --- | --- | --- |
| Gateway implementation | NGF controller pod in cluster | Azure-managed Application Gateway for Containers |
| Load balancer type | Azure Standard Load Balancer | Azure Application Gateway for Containers (AGfC) |
| L7 features | NGF-native (SnippetsFilter, ClientSettingsPolicy) | Azure-native (WAF, AGfC routing) |
| IP allowlisting | `SnippetsPolicy` / `SnippetsFilter` | Azure Application Gateway WAF / NSG rules |
| GatewayClass | `nginx` | `azure-alb-external` (or `azure-alb-internal`) |
| Managed service | No (NGF runs in your cluster) | Yes (AGfC is a fully managed Azure service) |
