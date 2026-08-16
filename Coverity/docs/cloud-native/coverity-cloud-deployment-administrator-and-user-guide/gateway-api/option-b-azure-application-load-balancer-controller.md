---
title: "Option B: Azure Application Load Balancer controller"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/option-b-azure-application-load-balancer-controller.html"
content_id: "DNOORlid896QckYTjyR5ig"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:45.646932+00:00"
---

# Option B: Azure Application Load Balancer controller

The Azure Application Gateway for Containers (AGfC) is a fully managed Azure service that
implements the Kubernetes Gateway API. The ALB Controller installed in AKS provisions
and manages two GatewayClasses: `azure-alb-external` (internet-facing)
and `azure-alb-internal` (VNet-internal). The chart auto-detects either
via the `azure-alb` prefix and renders the required
`HealthCheckPolicy` resources accordingly.

**NGF-only resources are skipped.**
`SnippetsFilter`, `SnippetsPolicy`, and
`ClientSettingsPolicy` are not rendered when
`gatewayClassName` does not start with `nginx`. Use
Azure-native equivalents (WAF, NSGs, AGfC routing rules) instead.

## Prerequisites

| Requirement | Notes |
| --- | --- |
| Kubernetes | **1.34–1.36** (supported AKS GA versions). Microsoft does not publish a separate floor for the ALB Controller — the [AKS support matrix](https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions) is the source of truth. |
| AKS networking | **Azure CNI** or **Azure CNI Overlay**. Kubenet will not work — pod IPs are not routable from the ALB subnet, requests silently return 502. |
| Workload identity | OIDC issuer and workload identity must be enabled on the cluster (`--enable-oidc-issuer --enable-workload-identity`). |
| Region | Must be in a [region where Application Gateway for Containers is available](https://learn.microsoft.com/en-us/azure/application-gateway/for-containers/overview#supported-regions). |
| Azure CLI | With `alb` and `aks-preview` extensions installed |
| Azure subscription providers | `Microsoft.ContainerService`, `Microsoft.Network`, `Microsoft.NetworkFunction`, `Microsoft.ServiceNetworking` registered |

Register providers and install extensions:

```
az provider register --namespace Microsoft.ContainerService
az provider register --namespace Microsoft.Network
az provider register --namespace Microsoft.NetworkFunction
az provider register --namespace Microsoft.ServiceNetworking

az extension add --name alb
az extension add --name aks-preview

az feature register --namespace "Microsoft.ContainerService" --name "ManagedGatewayAPIPreview"
az feature register --namespace "Microsoft.ContainerService" --name "ApplicationLoadBalancerPreview"
```

1. Set up the AKS cluster with the ALB controller

   **New cluster** — include
   `--enable-gateway-api` and
   `--enable-application-load-balancer` to install the ALB
   controller at creation
   time:

   ```
   az aks create \
     --resource-group <RESOURCE_GROUP> \
     --name <CLUSTER_NAME> \
     --location <LOCATION> \
     --network-plugin azure \
     --network-plugin-mode overlay \
     --pod-cidr 192.168.0.0/16 \
     --vnet-subnet-id <AKS_SUBNET_RESOURCE_ID> \
     --enable-oidc-issuer \
     --enable-workload-identity \
     --enable-gateway-api \
     --enable-application-load-balancer \
     --generate-ssh-keys
   ```

   **Existing cluster** — enable the ALB
   controller in
   place:

   ```
   az aks update -g <RESOURCE_GROUP> -n <CLUSTER_NAME> --enable-oidc-issuer --enable-workload-identity --no-wait

   az aks update \
     --name <CLUSTER_NAME> \
     --resource-group <RESOURCE_GROUP> \
     --enable-gateway-api \
     --enable-application-load-balancer
   ```

   > **Terraform users — Kubenet + system-assigned identity blocker:** If your
   > existing cluster was created with `network_plugin =
   > "kubenet"` and `identity { type = "SystemAssigned"
   > }`, you will hit two compounding problems when trying to
   > migrate:
   >
   > 1. AGfC requires **Azure CNI** (or Azure CNI Overlay). Azure will block
   >    the in-place CNI migration and require the cluster to use a
   >    **user-assigned managed identity** instead of a system-assigned
   >    one.
   > 2. In Terraform, changing both `network_plugin` and
   >    `identity.type` in the same apply typically forces a
   >    **cluster recreation** (destroy + create) rather than an in-place
   >    update — there is no safe in-place path from system-assigned to
   >    user-assigned identity on an existing cluster.
   >
   > The safest approach is to **provision a new cluster** with
   > `network_plugin = "azure"` (or
   > `network_plugin_mode = "overlay"`) and a user-assigned
   > identity from the start, then migrate workloads to it. Attempting to patch
   > the existing cluster in place risks data loss and extended downtime.

   Get credentials and verify the controller and
   GatewayClass:

   ```
   az aks get-credentials \
     --resource-group <RESOURCE_GROUP> \
     --name <CLUSTER_NAME> \
     --overwrite-existing

   kubectl get pods -n kube-system | grep alb-controller
   # Expected: two alb-controller pods in Running state

   kubectl get gatewayclass azure-alb-external
   # Expected: ACCEPTED = True
   ```

   For full cluster setup details,
   including BYO VNet permission grants, see the official [Deploy Application Gateway for Containers ALB
   Controller](https://learn.microsoft.com/en-us/azure/application-gateway/for-containers/quickstart-deploy-application-gateway-for-containers-alb-controller) guide.
2. Locate the ALB subnet and assign permissions

   Enabling
   `--enable-application-load-balancer` provisions a subnet
   named `aks-appgateway` (with delegation to
   `Microsoft.ServiceNetworking/TrafficController`). Microsoft's
   documentation states this subnet is always created in the `MC_*`
   managed resource group, but in practice it may be created in your own resource
   group instead if you supplied a BYO VNet. Check both
   locations:

   ```
   # Try the AKS-managed resource group first
   az network vnet subnet show \
     --resource-group MC_<RESOURCE_GROUP>_<CLUSTER_NAME>_<LOCATION> \
     --vnet-name <VNET_NAME> \
     --name aks-appgateway \
     --query id -o tsv

   # If not found there, check your own resource group
   az network vnet subnet show \
     --resource-group <RESOURCE_GROUP> \
     --vnet-name <VNET_NAME> \
     --name aks-appgateway \
     --query id -o tsv
   ```

   Export the result for use in the next
   step:

   ```
   export AKS_APPGATEWAY_SUBNET_RESOURCE_ID=<id-from-above>
   ```

   **BYO
   VNet only:** If your VNet lives outside the AKS-managed
   `MC_*` group, you must grant the ALB controller's managed
   identity `Network Contributor` access to the subnet. Skip this
   block if you are using the AKS-managed
   VNet.

   ```
   IDENTITY_PRINCIPAL_ID=$(az identity show \
     --resource-group MC_<RESOURCE_GROUP>_<CLUSTER_NAME>_<LOCATION> \
     --name "applicationloadbalancer-<CLUSTER_NAME>" \
     --query principalId -o tsv)

   az role assignment create \
     --assignee-object-id $IDENTITY_PRINCIPAL_ID \
     --assignee-principal-type ServicePrincipal \
     --scope $AKS_APPGATEWAY_SUBNET_RESOURCE_ID \
     --role "Network Contributor"
   ```

   Requires Owner or User Access
   Administrator permissions on the subscription.
3. Create the `ApplicationLoadBalancer` CR

   The chart does **not**
   create this resource automatically — it must exist before deploying CNC. The
   chart's Gateway will bind to it via annotations in Step 5.

   The CR can live
   in any namespace. The example below colocates it with the CNC release; the [Microsoft quickstart](https://learn.microsoft.com/en-us/azure/application-gateway/for-containers/quickstart-deploy-application-gateway-for-containers-alb-controller) puts it in a
   dedicated `azure-alb-system` namespace owned by the platform
   team. Either works — the namespace just has to match the
   `alb.networking.azure.io/alb-namespace` annotation set on the
   Gateway in Step
   5.

   ```
   kubectl apply -f - <<EOF
   apiVersion: alb.networking.azure.io/v1
   kind: ApplicationLoadBalancer
   metadata:
     name: coverity-alb
     namespace: <release-namespace>
   spec:
     associations:
     - $AKS_APPGATEWAY_SUBNET_RESOURCE_ID
   EOF
   ```

   Wait for it to provision (typically 2–5
   minutes):

   ```
   kubectl get applicationloadbalancer coverity-alb -n <release-namespace> -w
   # Wait until status shows Provisioned
   ```
4. Create the TLS
   Secret

   ```
   kubectl create secret tls coverity-tls \
     --cert=path/to/tls.crt \
     --key=path/to/tls.key \
     -n <release-namespace>
   ```
5. Configure the CNC Helm Chart

   The `annotations` block binds the
   chart-managed Gateway to the `ApplicationLoadBalancer` CR created
   in Step 3. Both values must match the CR name and namespace
   exactly.

   ```
   global:
     ingress:
       enabled: false

   cim:
     ingress:
       enabled: false

     gateway:
       create: true
       enabled: true
       gatewayClassName: "azure-alb-external"   # or "azure-alb-internal" for VNet-only access
       hostnames:
         - "coverity.example.com"
       annotations:
         alb.networking.azure.io/alb-name: "coverity-alb"
         alb.networking.azure.io/alb-namespace: "<release-namespace>"
       listeners:
         http:
           enabled: true
           port: 80
           redirect: true
         https:
           enabled: true
           port: 443
           tlsSecretName: "coverity-tls"
       # healthCheck.requestPath defaults to /login/login.htm — override only if using a custom context path
       # healthCheck:
       #   requestPath: "/login/login.htm"
       #   commitServerRequestPath: "/login/login.htm"
   ```

   > The chart automatically renders Azure ALB `HealthCheckPolicy`
   > resources for the CIM service (and commit-server when deployed) targeting
   > `/login/login.htm` on port 8080. AGfC rejects CIM's HTTP
   > 302 response on `/`, so this custom health check is required
   > — without it, all requests return `no healthy upstream`.

   Deploy:

   ```
   helm upgrade --install <release-name> charts/cnc/ -f values.yaml -n <release-namespace>
   ```
6. Retrieve the Gateway address

   AGfC publishes an Azure-managed FQDN (e.g.
   `<id>.alb.azure.com`) on the Gateway resource — not an IP.
   Allow 2–5 minutes after deploy for AGfC to program the
   listener.

   ```
   kubectl get gateway <release-name>-cim-gateway -n <release-namespace>
   # ADDRESS column shows the AGfC frontend FQDN

   export GATEWAY_FQDN=$(kubectl get gateway <release-name>-cim-gateway -n <release-namespace> \
     -o jsonpath='{.status.addresses[0].value}')
   echo "Gateway FQDN: $GATEWAY_FQDN"
   ```
7. Update DNS

   Create a **CNAME** record (not an A record) pointing
   `coverity.example.com` to `$GATEWAY_FQDN`. For
   zone-apex domains, use an Alias record pointing to the same FQDN.

   For
   local testing without DNS, resolve the FQDN to an IP and add it to
   `/etc/hosts`:

   ```
   echo "$(dig +short $GATEWAY_FQDN | head -1) coverity.example.com" | sudo tee -a /etc/hosts
   ```
8. Verify

   ```
   # Gateway must show PROGRAMMED = True and an Azure FQDN address
   kubectl get gateway <release-name>-cim-gateway -n <release-namespace> -o wide

   # HTTPRoutes must show Accepted: True, ResolvedRefs: True
   kubectl get httproute -n <release-namespace>

   # Verify the Gateway annotations the chart added
   kubectl get gateway <release-name>-cim-gateway -n <release-namespace> \
     -o jsonpath='{.metadata.annotations}' | jq
   # Expected: alb-name and alb-namespace annotations present

   # HealthCheckPolicy auto-created by the chart
   kubectl get healthcheckpolicy -n <release-namespace>
   # Expected: <release-name>-cim-healthcheck (always)
   #           <release-name>-commit-server-healthcheck (when commit-server is deployed)

   # Test HTTPS (expect 200)
   curl -sk -o /dev/null -w "%{http_code}\n" https://coverity.example.com/login/login.htm

   # Test HTTP redirect (expect 301)
   curl -sk -o /dev/null -w "%{http_code} → %{redirect_url}\n" http://coverity.example.com
   ```
