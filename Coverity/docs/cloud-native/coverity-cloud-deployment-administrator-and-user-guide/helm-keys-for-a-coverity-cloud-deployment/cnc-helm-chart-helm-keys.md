---
title: "cnc Helm chart: Helm keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cnc-helm-chart-helm-keys.html"
content_id: "Sk5NhTJcBlVTIG4GsN7Uqg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:46:04.303897+00:00"
---

# cnc Helm chart: Helm keys

The following Helm keys begin with `cim.` and define Coverity Connect
configurations used when deploying Coverity Connect in a Kubernetes cloud environment.
The `cim.` keys configure Coverity Connect admin tools, database tools,
and web applications.

This following sections describe `cnc` chart Helm Keys.

Important: If you either create a custom
`.yaml` file or set a Helm key value within a command such as
`helm install`, include cnc chart Helm keys using the syntax defined
in the cnc chart's `values.yaml` file.

Important: When referring to any `cnc` Helm
key from outside the chart, you must precede the key name with `cnc` For
example, the syntax for `cim.cimtools.enabled` must be
`cnc.cim.cimtools.enabled`

## cim.gateway Helm keys

Use following Helm keys to configure the ingress gateway API.

Table 1. `global.gateway` and `cim.gateway` Helm
keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` global:   gateway:     hostnames: ``` | `[]` | Array of gateway hostnames:  ``` global:   gateway:     hostnames:     - host1     - host2 ``` |
| ``` cim:   gateway:     create: ``` | `false` | - `true` — Set to `true` to have   Helm create the kind:Gateway resource in the cluster. - `false` - the Gateway is managed externally   (default). |
| ``` cim:   gateway:     enabled: ``` | `false` | - `true` - HTTP route objects are created for   CIM. - `false` - HTTP route objects are not created   for CIM. |
| ``` cim:   gateway:     gatewayClassName: ``` | `"nginx"` | Set the `GatewayClassName` value to the installed gateway class. For example:   - `"nginx"` - NGINX gateway fabric (default   value) - `"gke-l7-global-external-managed"` - GKE   Global External Application Load Balancer: - `"gke-l7-regional-external-managed"` - GKE   Regional External Application Load Balancer: - `"gke-l7-rilb"` - GKE Regional Internal   Application Load Balancer - `"azure-alb-external"` - Azure Application   Load Balancer controller - `"amazon-alb"` - AWS Application Load   Balancer (requires AWS Load Balancer Controller)   When the class name starts with "gke-", NGF-specific resources (SnippetsFilter, SnippetsPolicy, ClientSettingsPolicy) are skipped and GKE HealthCheckPolicy resources # are created. GKE Gateway API provisions NEGs automatically — no annotation needed. # When the class name is "amazon-alb" or starts with "amazon-", AWS TargetGroupConfiguration # resources are created for health checks. LoadBalancerConfiguration must be created manually # and referenced via infrastructure.parametersRef.name. |
| ``` cim:   gateway:     name: ``` | `""` | Name of the Gateway resource. When empty, defaults to <release-name>-gateway (e.g. "coverity-gateway" for release "coverity"). Override only when pointing to an external Gateway with a different name. |
| ``` cim:   gateway:     namespace: ``` | `""` | If you supply a value here, that value is the namespace where the Gateway resource exists. With this field empty `""`, the default is the name of the release namespace, for example, "cim". |
| ``` cim:   gateway:     hostnames: ``` | `[]` | Array of allowed host names for the HTTP route and gateway listeners. |
| ``` cim:   gateway:     path: ``` | `"/"` | The route path for CIM. |
| ``` cim:   gateway:     pathType: ``` | `"PathPrefix"` | Path matching type: Exact, PathPrefix, or RegularExpression |
| ``` cim:   gateway:     ccdPath: ``` | `"/ccd"` | The route path for commit-server (CCD). Used by `commit-server-httproute.yaml`. |
| ``` cim:   gateway:     sectionName: ``` | `""` | Optional. Specific listener section name to attach to. For multiple listeners. |
| ``` cim:   gateway:     backendWeight: ``` | `null` | Optional. Traffic weight for canary deployments. |
| ``` cim:   gateway:     filters: [] ``` | `[]` | Optional. You can provide raw HTTP route filters that are applied to every route rule.  These filters are useful for NGF SnippetsFilter proxy directives not yet covered. For example: `proxy_connect_timeout`, `proxy_next_upstream`, `proxy_next_upstream_tries`, etc. |
| ``` cim:   gateway:     allowedSourceRanges: [] ``` | `[]` | IP allowlisting  Optional: IP allowlist  The per-route IP allowlist via SnippetsFilter + ExtensionRef on each HTTP route rule.  Requires NGINX Gateway Fabric installed using:  `--set nginxGateway.snippets.enable=true`  Example: ["10.0.0.0/8", "192.168.1.0/24"] |
| ``` cim:   gateway:     gatewayAllowedSourceRanges: [] ``` | `[]` | Optional: gateway-level IP allowlist via SnippetsPolicy targeting the Gateway. # Applies to ALL routes — no per-route config needed. Recommended for dev clusters. # Requires NGINX Gateway Fabric installed with --set nginxGateway.snippets.enable=true. # Example: ["10.0.0.0/8", "192.168.1.0/24"] |
| ``` cim:   gateway:     clientSettings:       body:         maxSize: "" ``` | `""` | NGF ClientSettingsPolicy  Maximum request body size enforced at the Gateway (client_max_body_size). Set this if you need to allow uploads larger than the NGF default (e.g. large scan results). For example: `"500m", "1g"` |
| ``` cim:   gateway:     healthCheck:       requestPath: "/login/login.htm"       commitServerRequestPath: "/login/login.htm" ``` | `"/login/login.htm"` | Health Check Configuration  Health check paths for target services. Used by GKE HealthCheckPolicy and AWS TargetGroupConfiguration resources. Both GKE and AWS ALB accept only 2xx responses as healthy. CIM returns 302 on "/" so a custom health check path is required. Defaults to /login/login.htm.  `requestPath:` Health check path for the CIM service.  `commitServerRequestPath:` Health check path for the commit-server (CCD) service. |
| ``` cim:   gateway:     annotations: {} ``` | `{}` | Optional: Gateway annotations: Use this key to create annotations to add to the Gateway resource. |
| ``` cim:   gateway:     lbConfigName: "" ``` | `""` | Load Balancer Configuration name. For AWS only. |
| ``` cim:   gateway:     listeners:        http:         enabled: true         port: 80         shared: false         redirect: true        https:         enabled: true         # listener port         port: 443         tlsSecretName: ""         shared: false ``` |  | Listener configuration - Use only if `cim.gateway.create: true`  HTTP:   - `enabled` - if `true`, create   an HTTP listener on the gateway. - `port` - listener port. - `shared` - if `true`, allow   HTTP routes from any namespace (from: All);   `false` = same namespace only (from:   Same) - `redirect` - if `true`, render   an HTTP→HTTPS redirect HTTPRoute (301) on the HTTP   listener.   HTTPS:   - `enabled` - if `true`, create   an HTTPS listener on the gateway. - `port` - listener port. - `tlsSecretName` - name of the TLS secret in   the release.namespace containing `tls.crt`   and `tls.key`. Required when`https.enabled=true` and   `create=true`. - `shared` - if `true`, allow   HTTP routes from any namespace (from: All);   `false` = same namespace only (from:   Same). |

## cim.route Helm keys for OpenShift

OpenShift Route configuration. Automatically uses ingress settings.

Table 2. `cim:route:` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   route:     enabled: ``` | `false` | Enable route creation using the existing ingress configuration.   - `true` - an OpenShift Route object is   created. - `false` - an OpenShift Route object is not   created. |
| ``` cim:   route:     annotations: ``` | `{}` | Additional annotations to provide to the route object. |
| ``` cim:   route:     hosts: ``` | `[]` | Array of allowed host names. If empty, will use hosts from ingress configuration. |
| ``` cim:   route:     targetPort: ``` | `8080` | The target port for the route. |
| ``` cim:   route:     tls:       enabled: ``` | `true` | Use the next few `cim.route.tls` keys to configurate the route.  Enable TLS for the route:   - `"true"` TLS is enabled for the route. - `"false"` TLS is not enabled for the   route. |
| ``` cim:   route:     tls:       termination: ``` | `"edge"` | TLS termination type:   - `"edge"` - `"passthrough"` - `"reencrypt"` |
| ``` cim:   route:     tls:       secrets: ``` | `[]` | Array of TLS secrets with schema (same as ingress). For example:   ``` cim:   route:     tls:       secrets:       - secretName: "tls-secret-name"         hosts: ["example.com"] ```   Note: if empty, will inherit from ingress.tls configuration: |
| ``` cim:   route:      tls:       insecureEdgeTerminationPolicy: ``` | `""` | Policy for handling insecure connections: Allow, Disable, or Redirect   - `"Allow"` - `"Disable"` - `"Redirect"` |
| ``` cim:   route:     wildCardPolicy: ``` | `"None"` | Route wildcard policy:   - `"None"` - `"Subdomain"` |

## cim.ingress Helm keys

The following Helm keys provide for further ingress configuration.

Table 3. `ingress` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   ingress:     annotations: ``` | `{}` | Additional annotations to provide to the ingress object. |
| ``` cim:   ingress:     class: ``` | `"nginx"` | Value for "kubernetes.io/ingress.class" annotation key. |
| ``` cim:   ingress:     enabled: ``` | `false` | If `true`, a Kubernetes ingress object is created. |
| ``` cim:   ingress:     hosts: ``` | `[]` | Array of allowed host names. |
| ``` cim:   ingress:     patrh: ``` | `"/"` | The ingress rule path. # notes: # - you may need to set this to "/*" for gce ingress controller # - you may need to add a path on this if using a context path |
| ``` cim:   ingress:     ccdPath: ``` | `"/ccd"` | When `cim.commit-server.replicas` is greater than 0, only this ingress rule path is used to redirect the commit traffic into commit server. |
| ``` cim:   ingress:     tls: ``` | `[]` | Array of object with schema. Used to choose tls secret for https: # - secretName: "" # hosts: [] |

## cim.cimweb.triage-suggestion-service Helm keys

The `cim.cimweb.triage-suggestion-service` Helm keys can be used to
override global values. For service-level overrides of global values, you can
configure `cim.cimweb.triage-suggestion-service` Helm keys to
override global triage suggestion keys for `cim`-specific needs.

For information on these Helm keys, see the
`cim.cimweb.triage-suggestion-service` Helm chart as well as the
equivalent keys in triage-suggestion-service Helm subchart.

## Global Helm keys

For `global` Helm key information, see: Global Helm keys.

## Root Helm keys

You can find information on root Helm keys here: Root Helm keys.

## cim Helm keys for pod security and node affinity

The following Helm keys describe Helm keys for:

- Coverity Connect `cim` pod security
- Coverity Connect node affinity, selector, and toleration.

Table 4. `cim` Helm keys for pod security and node affinity

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   affinity: ``` | `{}` | Sets the node affinity on the Coverity Connect deployment. |
| ``` cim:   automountServiceAccountToken: ``` | `false` | This Helm key determines whether or not the service account (SA) token is automatically mounted into the `cim` pod.   - `false`: The SA token is not automatically   mounted in the `cim` pod. - `true`: The SA token is automatically mounted   in the `cim` pod.   Mounting the SA token in a pod provides authentication for the pod and enables the pod to access resources.  See also Configuring pod and container security.  To create the SA token, see Generate a Connect SA admin user token. |
| ``` cim:   nodeSelector: ``` | `{}` | Sets the node selector on the Connect deployment. |
| ``` cim:   podSecurityContext: ``` | `{}` | Sets the Connect (cim) pod security context. |
| ``` cim:   serviceAnnotations: ``` | `{}` | Additional annotations to add to the `cim/commit-server` service metadata. This is a dictionary. |
| ``` cim:   tolerations: ``` |  | Sets tolerations on the Connect deployment. If you are deploying Coverity on ARM64 nodes, if a global toleration is not used, this toleration must be configured.  For example, to deploy this service on ARM64 nodes only:   ``` cim:   tolerations:     - key: "kubernetes.io/arch"       operator: "Equal"       value: "arm64"       effect: "NoSchedule" ```   Note: Refer to:  - Setting up ARM64 support - <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/> |

## cim.cimdownloads Helm keys

The following preconfigured Helm keys specify a container image that provides static
files for downloads from the Coverity Connect UI (user interface).

Table 5. `cim.cimdownloads` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   cimdownloads:     containerSecurityContext: ``` | `{}` | Set the container security context.  For details, see Configuring pod and container security. |
| ``` cim:   cimdownloads:     enabled: ``` | `true` | - `true` = enable the init container. - `false` = disable the init container. |
| ``` cim:   cimdownloads:     image: ``` | `"cim-downloads"` | The name of the CIM downloads container image. Do not override this value. |
| ``` cim:   cimdownloads:     registry: ``` | `""` | The container image registry. Use this only if this container is not in the registry specified by the `imageRegistry` Helm key. |
| ``` cim:   cimdownloads:     version: ``` | `"CIM_VERSION"` | The image version. Use this only if this container image is not the version specified by the `imageVersion` Helm key. |

## cim.cimtools Helm keys

The following preconfigured Helm keys specify a container image that creates a
Kubernetes stateful set which provides administrator functionality:

- cov-archive
- reset-admin-password (cov-admin-db)

The stateful set is initially set to replica count 0. It must first be scaled up to 1
to create a pod before use.

Note: If you encounter an error related to the read-only file
system while executing any of our scripts or binaries within Connect pods, you can
set the file system to `readOnly: false`. See also Read-only file system error.

Note: To perform a write operation in either a
`cim-tools` pod or a `db-admin` pod, use the
`/data` path.. See also cim.cimtools.volume Helm keys: create and mount a /data volume.

Table 6. `cim.cimtools` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   cimtools:     automountServiceAccountToken: ``` | `false` | This Helm key determines whether or not the service account (SA) token is automatically mounted into the `cimtools` pod.   - `false`: The SA token is not automatically   mounted in the `cimtools` pod. - `true`: The SA token is automatically mounted   in the `cimtools` pod.   Mounting the SA token in a pod provides authentication for the pod and enables the pod to access resources.  See also Configuring pod and container security.  To create the SA token, see Generate a Connect SA admin user token. |
| ``` cim:   cimtools:     containerSecurityContext: ``` | `{}` | Set the container security context.  For details, see Configuring pod and container security. |
| ``` cim:   cimtools:     enabled: ``` | `true` | - `true` = Create a stateful set. - `false` = Do not create a stateful set. |
| ``` cim:   cimtools:     extraVolumes: ``` | [] | Additional volumes to add to the All pods and jobs except syncJob, AnalysisJob, and cleanUpJob. |
| ``` cim:   cimtools:     image: ``` | `"cim-tools"` | The name of the container image to deploy the CIM Tools. Use the default value unless you have changed the name. |
| ``` cim:   cimtools:     initContainers: ``` | [] | This Helm key specifies init containers to inject into the cim-tools pod.  You might specify init containers when attaching a Cloud SQL proxy native sidecar container in GCP. See:   - Attaching a Cloud SQL proxy native sidecar container in GCP - <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/> |
| ``` cim:   cimtools:     registry: ``` | `""` | The container image registry. Use this only if this container is not in the registry specified by the `imageRegistry` Helm key. |
| ``` cim:   cimtools:     version: ``` | `"CIM_VERSION"` | The CIM tools container image version. Use this only if this container image is not the version specified by the `imageVersion` Helm key. |

## cim.cimtools.resources Helm keys

The following Helm keys specify Kubernetes resource requests and limits for Coverity
Connect tools.

## cim.cimtools.resources.limits Helm keys

The following Helm keys specify Kubernetes resource limits for Connect tools.

Table 7. `cim.cimtools.resources.limits` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   cimtools:     resources:       limits:         cpu: ``` | `"0.5"` |  |
| ``` cim:   cimtools:     resources:       limits:         memory: ``` | `"1Gi"` |  |

## cim.cimtools.resources.requests Helm keys

The following Helm keys specify Kubernetes resource requests for Connect tools.

Table 8. `cim.cimtools.resources.requests` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   cimtools:     resources:       requests:         cpu: ``` | `"0.5"` |  |
| ``` cim:   cimtools:     resources:       requests:         memory: ``` | `"1Gi"` |  |

## cim.cimtools.volume Helm keys: create and mount a /data volume

The Coverity Connect (`cim`) tools run in the
`cim-tools` pod. To store tools data between sessions, you need
to create a `/data` persistent volume and mount that volume to the
`cim-tools` pod. The following table describes the
`cim.cimtools.volume` Helm keys you will use when you create a
persistent `/data` volume and mount it to the
`cim-tools` pod for coverity Connect tools.

Table 9. `cim.cimtools.volume` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   cimtools:     volume:       accessMode: ``` | `"ReadWriteOnce"` | Creates a `/data` volume that can be written by the Coverity tools scripts. |
| ``` cim:   cimtools:     volume:       enabled: ``` | `false` | Determines whether or not the`/data` volume is mounted to the `cim-tools` pod:   - `true` - Mounts the `/data`   volume to the `cim-tools` pod. - `false` - The `/data` volume   is NOT mounted to the `cim-tools` pod. |
| ``` cim:   cimtools:     volume:       mountPath: ``` | `/data` | For the cim tools to be able to write and persist data, a persistent `/data` volume needs to be mounted to the `cim-tools` pod. This Helm key defines the `/data` path used by the cim tools. |
| ``` cim:   cimtools:     volume:       storage: ``` | `"1Gi"` | Specifies the amount of memory assigned to the `/data` volume. |
| ``` cim:   cimtools:     volume:       storageClass: ``` |  |  |

## cim.cimweb Helm keys

The `cim.cimweb.` Helm keys create a Kubernetes cloud deployment which
runs the Connect web application. It also includes:

- An init container to set up configuration.
- An init container to set up documentation.
- An init container to set up downloads of client-side utilities.
- (optional) an NGINX reverse proxy as a sidecar to provide TLS termination.

The keys in the following `cim.cimweb` table set up various Connect
web characteristics such as enabling Connect web deployment in the cloud, selecting
the port to commit defects, image information, and log levels, etc.

Table 10. `cim.cimweb` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   cimweb:     adminPasswordSecret: ``` | "" | Provide the name of the secret that contains the Connect Web UI administrator password. This secret must contain a key named `password`.  Alternatively, you can use the following option in a Helm command to set this secret in a new or existing deployment:   ``` --set cim.cimweb.adminPasswordSecret=”<secretName>” ```   See also:   - Create a Connect Web application administator password secret - Set the cim.cimweb.adminPasswordSecret Helm key |
| ``` cim:   cimweb:     annotations: ``` | `{}` | Additional annotations to add to the deployment metadata. This is a dictionary. |
| ``` cim:   cimweb:     commitPort: ``` | `9090` | An integer that specifies the data port for committing defects. |
| ``` cim:   cimweb:     containerSecurityContext: ``` | `{}` | Set the container security context.  For details, see Configuring pod and container security. |
| ``` cim:   cimweb:     contextPath: ``` | `""` | Add a context routing path under a Coverity host.  For example, if `contextPath` is set to `$CONTEXT_PATH`, and the `webUrl` key is set to `https://$HOST/$CONTEXT_PATH`, traffic to the context path is routed to the context path at the host.  If no context path is desired, set this to `""` (empty string). |
| ``` cim:   cimweb:     enabled: ``` | `true` | - `true` = Create a cloud deployment. - `false` = Do not create a cloud   deployment. |
| ``` cim:   cimweb:     environment: ``` | `{}` | Additional environment variables injected into the container environment. |
| ``` cim:   cimweb:     exposeCommitPort: ``` | `false` | - `true` = Open a commit port on the container   and service. - `false` = Do not open a commit port on the   container and service. |
| ``` cim:   cimweb:     exposeMetrics: ``` | `true` | - `true` = expose time series metrics in   Prometheus format. - `false` = Do not expose time series   metrics. |
| ``` cim:   cimweb:     extraProperties: ``` | `{}` | You can use this key to provide additional properties to Connect, including the following.   - **Metrics**. The `connect.enable.metrics`   property hides metrics or makes metrics available at the   /metrics endpoins as follows:   - `connect.enable.metrics: false`     disables metrics presentation to the /metrics     endpoint. This is the defaut value.   - `connect.enable.metrics: true`     enables metrics presentation to the /metrics     endpoint. - **Storage service custom domains**. Configure storage   service custom domains using an   annotation:    ```   storage.service.custom.domains: storage.example.com   ```     Note: When using a *, ?, &, # within   a value in a Helm chart, encase the value within quotes.   Other requirements exist.  For further   information, including default values, see Storage service custom domains. |
| ``` cim:   cimweb:     extraVolumeMounts: ``` | `[]` | Additional volume mounts to add to the cim-webapp container. The volumes must be listed under `cim.cimweb.extraVolumes`. |
| ``` cim:   cimweb:     extraVolumes: ``` | `[]` | Additional volumes to add to the cim-webapp container. |
| ``` cim:   cimweb:     image: ``` | `"cim-web"` | The name of the container image to deploy CIM web. Do not override this value. |
| ``` cim:   cimweb:     initContainers: ``` | `[]` | This Helm key specifies init containers to inject into the cim-webapp pod.  You might specify init containers when attaching a Cloud SQL proxy native sidecar container in GCP. See:   - Attaching a Cloud SQL proxy native sidecar container in GCP - <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/> |
| ``` cim:   cimweb:     javaOpts: ``` | `""` | Additional Java options to add to the Connect invocation.  For Coverity Connect tuning, you can set the JVM option `-Xms512m` here.  To see the default options: `docker run --rm -ti cimweb_registry /cim-web: cimweb_version cat cim.sh` See also Java options. |
| ``` cim:   cimweb:     logLevel: ``` | `"INFO"` | Specifies the minimum logging level used to generate logs. Valid values include:   - ALL - TRACE - INFO This is the default value. INFO presents all log   levels from informational through the highest level. - WARN - ERROR - FATAL - OFF Not recommended. Disables logging.   Note: The log levels can be all uppercase or all lowercase, and can be encased in double-quotes for string value.  See also Specifying logging levels. |
| ``` cim:   cimweb:     podAnnotations: ``` | `{}` | Additional annotations to add to the pod metadata. This is a dictionary. |
| ``` cim:   cimweb:     registry: ``` | `""` | The container image registry. Use this only if this container is not in the registry specified by the `imageRegistry` Helm key. |
| ``` cim:   cimweb:     replicas: ``` | 1 | This Helm key determines the number of Connect web application (cimweb) pod instances (replicas) that are created and maintained within the cluster. This value can be scaled up and down to meet user demands and maintain throughput. Valid values are:   - `0`: No Coverity Connect web application   software instances. For example, if you need to run   `helm install`. - `1`: Creates a single Coverity Connect web   application software instance (pod). This does not provide   high availability. - `2`+: Creates and maintains multiple Coverity   Connect web application software instances (pods). This   provides high availability.   For further information on high availability (HA) and scaling Connect web app pods, refer to Connect Web application high availability.  If you deploy cimweb HA, you should also configure the `commit-server` Helm keys to increase cache performance. |
| ``` cim:   cimweb:     version: ``` | `"CIM_VERSION"` | The CIM web container image version. Use this only if this container image is not the version specified by the `imageVersion` Helm key. |
| ``` cim:   cimweb:     webUrl: ``` | `""` | This is used as the web.URL property in web.properties. It is important to set this property correctly; otherwise integrations such as Jira, Bugzilla, SAML and any other integrations will not work correctly. The default value is `""`.  Important: The Connect (cim) hostname portion of the URL that you specify in `cim.cimweb.webURL` must not exceed 46 characters in length. This restriction excludes the `https://` characters that are used when you specify the URL, as well as any port specification. |

## cim.cimweb.keystore Helm keys

The `cim.cimweb.keystore` keys specify properties that define a Java
keystore (JKS) file (keystore) that contains a TLS private key certificate. You must
create keystores for TLS-SSL communication in the Coverity cloud environment between
Coverity Connect instances. This is especially important for commit over commit port
deployments.

See also Create a truststore ConfigMap for Connect communication over TLS and Preparing cim.cimweb Helm keys.

Table 11. `cim.cimweb.keystore` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   cimweb:     keystore:       certificateSecret: ``` | "" | Specify the name of the secret that contains the TLS certificate. Refer to Create a truststore ConfigMap for Connect communication over TLS. |
| ``` cim:   cimweb:     keystore:       enabled: ``` | `false` | Enables or disables keystore mounting:   - `true`: The keystore is mounted in the   specified path. Make sure that the following key is set:   - `cim.cimweb.keystore.certificateSecret` - `false`: The keystore cannot be mounted. |

## cim.cimweb.loadBalancer Helm keys

A load balancer or reverse proxy is commonly put in front of a CIM installation in
order to handle TLS termination. Most load balancers and proxies add a set of
headers to provide information about the original request (see <https://datatracker.ietf.org/doc/html/rfc7239.html>).

To protect against forged requests, configure CIM to trust the IP address of its load
balancer(s). Therefore, an escaped regular expression is provided to validate the
proxy request's IP addresses. This is especially important for SAML, which requires
extra validation for the request.

Table 12. `cim.cimweb.loadBalancer` Helm key

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   cimweb:     loadBalancer:       trustedRegex: ``` | `".*"` | Used as the `trusted_proxy.regex` property in `cim.properties`. |

## cim.cimweb.resources Helm keys

The following Helm keys specify Kubernetes resource requests and limits for Coverity
Connect.

## cim.cimweb.resources.limits Helm keys

The following Helm keys specify Kubernetes resource limits for Coverity Connect.

Table 13. `cim.cimweb.resources.limits` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   cimweb:     resources:       limits:         cpu: ``` | `"2"` | Specifies the maximum number of Connect CPUs. |
| ``` cim:   cimweb:     resources:       limits:         memory: ``` | `"8Gi"` | Specifies the maximum Connect memory. |

## cim.cimweb.resources.requests Helm keys

The following Helm keys specify Kubernetes resource requests for Coverity
Connect.

Table 14. `cim.cimweb.resources.requests` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   cimweb:     resources:       requests:         cpu: ``` | `"0.25"` |  |
| ``` cim:   cimweb:     resources:       requests:         memory: ``` | `"1Gi"` | Specifies the amount of Connect memory. |

## cim.cimweb.tlsSidecar Helm keys

The following Helm keys create a sidecar container to provide TLS termination.

Important: Do NOT enable TLS sidecar if you are
deploying only Coverity Connect in the cloud.

Table 15. `cim.cimweb.tlsSidecar` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   cimweb:     tlsSidecar:       containerSecurityContext: ``` | `{}` | Set the container security context.  For details, see Configuring pod and container security. |
| ``` cim:   cimweb:     tlsSidecar:       enabled: ``` | `false` | Disable (default value) or enable TLS sidecar:   - `false` disables TLS sidecar. - `true` enables TLS sidecar.  Important: Do NOT enable   TLS sidecar if you are deploying only Coverity Connect   in the cloud. |
| ``` cim:   cimweb:     tlsSidecar:       image: ``` | `"nginx"` | The container image name. If you are not using an NGINX ingress controller, replace this with the appropriate value. |
| ``` cim:   cimweb:     tlsSidecar:       registry: ``` | `""` | The container image registry. |
| ``` cim:   cimweb:     tlsSidecar:       version: ``` | `"1.27.4"` | The container image version. The default value is the supported `nginx` version. |
| ``` cim:   cimweb:     tlsSidecar:       nginxConfig:         # Core nginx settings         worker_processes: 1         worker_connections: 1024         keepalive_timeout: 65         client_max_body_size: "100m"          # SSL/TLS settings         ssl_protocols: "TLSv1.2 TLSv1.3"         ssl_ciphers: "AESGCM:CHACHA20:-kRSA:-aNULL"         ssl_prefer_server_ciphers: "on"         ssl_ecdh_curve: "X25519:prime256v1"          # Proxy timeout settings (with units)         proxy_connect_timeout: "60s"         proxy_read_timeout: "60s"         proxy_send_timeout: "60s" ``` | Core nginx default values:   ``` worker_processes: 1 worker_connections: 1024 keepalive_timeout: 65 client_max_body_size: "100m" ```   SSL/TLS default values:   ``` ssl_protocols: "TLSv1.2 TLSv1.3" ssl_ciphers: "AESGCM:CHACHA20:-kRSA:-aNULL" ssl_prefer_server_ciphers: "on" ssl_ecdh_curve: "X25519:prime256v1" ```   Proxy timeout default values:   ``` proxy_connect_timeout: "60s" proxy_read_timeout: "60s" proxy_send_timeout: "60s" ``` | The NGINX configuration key-value pairs represented by these Helm keys change NGINX configuration values in the NGINX ConfigMap.  For information on how to change these NGINX ConfigMap values using these Helm keys, see Working with nginxConfig Helm keys.  The keys are distributed in the following categories:  Note: For information on the meaning of each configuration key, see the NGINX document page [Alphabetical index of directives](https://nginx.org/en/docs/dirindex.html).   - **Core NGINX settings**: You can use these Helm keys   to change the related core configuration values in the   NGINX ConfigMap. - **SSL/TLS settings**: You can use these Helm keys to   change the related SSL/TLS values in the NGINX   ConfigMap. - **Proxy timeout settings**: These can be used to   change proxy timeout values; for example, to solve an   Error 504 gateway timeout issue. For information on   using these Helm keys and resolving an Error 504 gateway   timeout, see NGINX HTTP error 504: Gateway Timeout.  Important: You must follow these conventions when setting NGINX   ingress proxy timeout values:    - Valid units of measure are: s (seconds     (default)) | m (minutes) | h (hours) | d     (days)   - You must use a single unit of measure (90s, not     1m30s).   - The value must be a positive integer,   - The unit of measure must immediately follow the     value; no space. For example, the following have the same value:     ```   ..._timeout: "3600s"   ..._timeout: "60m"   ..._timeout: "1h"   ```   Important: To apply an `nginxConfig` value change, you must perform either a `helm upgrade` or a `helm install`. Refer to Working with nginxConfig Helm keys. |

## cim.cimweb.updateLicense Helm keys

The following Helm keys create a Kubernetes job which updates the license record in
the database using the license from the secret named in
`licenseSecretName`.

Table 16. `cim.cimweb.updateLicense` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   cimweb:     updateLicense:       enabled: ``` | `false` | - `true` = Create the updateLicense job. - `false` = Do not create the updateLicense   job. |
| ``` cim:   cimweb:     updateLicense:       force: ``` | `false` | - `true` = Always update the license. - `false` = Update the license if   necessary. |

## cim.commit-server Helm keys

When implementing high availability (HA), you can deploy one or more commit-server
pods which manage commits and caching to improve single-commit performance or
multiple-commit throughput. Using commit servers, also called Coverity commit
defects (CCD) servers, directs ingress traffic to the commit servers.

The following table describes the `cim.commit-server` Helm keys that
you use to deploy commit-server pods and configure commit-server logging.

See also Optimizing commit performance vs throughput using commit-server pods.

Table 17. `cim.commit-server` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   commit-server:     logLevel: ``` | "INFO" | Specifies the minimum logging level used to generate logs. Valid values include: See also Optimizing commit performance vs throughput using commit-server pods.   - ALL - TRACE - INFO This is the default value. INFO presents all log levels   from informational through the highest level. - WARN - ERROR - FATAL - OFF Not recommended. Disables logging.   Note: The log levels can be all uppercase or all lowercase, and can be encased in double-quotes for string value.  See also Specifying logging levels. |
| ``` cim:   commit-server:     replicas: ``` | 1 | Specifies the number of commit server replicas to deploy: See also Optimizing commit performance vs throughput using commit-server pods.   - `1`: Requires cimweb HA:Deploys a single   commit server. This is the default value. Performance   profile; this mode provides greater performance for a single   commit, however it has lower throughput for multiple   commits. - `2` or greater: Requires cimweb HA. Deploys 2   or more commit servers as configured. Throughput profile;   this configuration increases total commit throughput while   degrading single-commit performance. |

## cim.ingress Helm keys

The following Helm keys configure the ingress controller. If TLS sidecar NGINX
reverse proxy is enabled, this will forward to `https/8443`;
otherwise it will forward to `http/8080`.

Important: Do NOT enable TLS sidecar if you are
deploying only Coverity Connect in the cloud.

Table 18. `cim.ingress` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   ingress:     annotations: ``` | `{}` | Additional annotations to provide to the ingress object.  You can use the following annotation syntax to specify the maximum file size to allow through the ingress port: `nginx.ingress.kubernetes.io/proxy-body-size: <fileSize>` For example, to be able to upload a 7.6 GB Coverity toolkit tar file from a client to Connect:   ``` cim:   ingress:     annotations:       nginx.ingress.kubernetes.io/proxy-body-size: 8g ```   See also Set NGINX proxy-body-size for Coverity toolkit tar file upload to Connect. |
| ``` cim:   ingress:     ccdPath: ``` | ``` "" ``` | Important: Do not change this value.  If `commit-server` is deployed, this Helm key directs the ingress controller to forward commits to the commit-server (CCD server). |
| ``` cim:   ingress:     class: ``` | `""` | The default ingress controller is NGINX, therefore the default value points to the `kubernetes.io/ingress.class` annotation key. If you use a different ingress controller, update the value in this field. |
| ``` cim:   ingress:     enabled: ``` | `false` | Set to `true` to create a Kubernetes ingress object. |
| ``` cim:   ingress:     hosts: ``` | `[]` | Array of allowed host names.  Important: The `cim.ingress.hosts` hostname must not exceed 46 characters in length. This excludes the https:// characters that are used when you specify the URL. |
| ``` cim:   ingress:     path: ``` | `""` | The ingress rule path.   - You might need to set this to `"/*"` for   AWS ALB ingress controllers. - You might need to set this to `"/*"` for   GCE ingress controllers. - You might need to add a path if you are using a context   path. |
| ``` cim:   ingress:     tls: ``` | `[]` | Array of object with schema to select the TLS secret for https:   ``` cim:   ingress:     tls:       - secretName: ""         hosts: [] ``` |

## cim.ldap Helm keys

The following Helm keys enable you to update the Coverity Connect LDAP configuration
during Helm chart deployment. During an initial deployment, you need to configure
LDAP using the Connect UI, For subsequent deployments, you can use the following
Helm keys to change related LDAP configuration values as needed.

Important: If you are deploying Coverity cloud for the
first time, you must configure LDAP using the Coverity Connect UI as described in
the section Integrating with LDAP servers in the Coverity Platform 2026.6.0 User and Administrator Guide.

For the following additional LDAP configuration information, see Configure LDAP.

- link to the procedure to perform an initial LDAP configuration,
- procedure to change a value in an existing LDAP configuration using the Helm
  chart.
- link to procedure to add the LDAP certificate to the Connect truststore
  ConfigMap

Table 19. `cim.ldap` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   ldap:     baseDN: ``` | `""` | The `cim.ldap.baseDN` key specifies the Base Distinguished Name (DN) for the LDAP configuration.  The `cim.ldap.baseDN` key defines the starting point (or base DN) in the LDAP directory tree from which the LDAP search operations will begin. This is crucial for locating user entries, group entries, and other relevant data in the LDAP directory.  If `cim.ldap.updateConfig` is `true`, entering a value in `cim.ldap.baseDN` will update the configured Base DN next time you install or upgrade the Helm chart.  See also Change configured LDAP values. |
| ``` cim:   ldap:     bindDN: ``` | `""` | The `cim.ldap.bindDN` key specifies the Bind Distinguished Name (DN) used for authenticating to the LDAP server. This is essential for performing LDAP operations, such as searching for users and groups.  For example:   ``` cim:   ldap:     bindDN: "cn=admin,dc=example,dc=com" ```   If `cim.ldap.updateConfig` is `true`, entering a value in `cim.ldap.bindDN` will update the configured Bind DN next time you install or upgrade the Helm chart.  See also Change configured LDAP values. |
| ``` cim:   ldap:     bindPassword: ``` | `""` | The `cim.ldap.bindPassword` key specifies the password used for the Bind Distinguished Name (DN) when authenticating to the LDAP server.  For example:   ``` cim:   ldap:     bindPassword: "LDAPpasswordSecret" ```   Important: The bind password is sensitive information. To securely manage it, use a Kubernetes secret to store the password and enter the name of the secret in this Helm key. Do not hardcode the password in the `values.yaml` file.  If `cim.ldap.updateConfig` is `true`, entering a value in `cim.ldap.bindPassword` will update the configured Bind password next time you install or upgrade the Helm chart.  See also Change configured LDAP values. |
| ``` cim:   ldap:     cimKey:       value: ``` | ``` "fLXz3H9yLoe+/ xJCMZlVicOXE5fj bpm9zDNOi/tzCs4=" ``` | Specifies the value of a Coverity Connect LDAP key. If specified, this must be well-formed base64 encoding of an arbitrary 16, 24, or 32 byte string. You can generate a key using a command such as: `head -c 32 /dev/urandom`. |
| ``` cim:   ldap:     displayName: ``` | `""` | The `cim.ldap.displayName` key is used to define which LDAP attribute should be treated as the user's display name within the Coverity environment. This is important for user identification and representation.  For example:   ``` cim:   ldap:     displayName: "displayName" ```   If `cim.ldap.updateConfig` is `true`, entering a value in `cim.ldap.displayName` will update the configured display name next time you install or upgrade the Helm chart.  See also Change configured LDAP values. |
| ``` cim:   ldap:     hostName: ``` | `""` | The `cim.ldap.hostName` key specifies the hostname of the LDAP server that the Coverity application will connect to for authentication and user management.  For example:   ``` cim:   ldap:     hostName: "ldap.example.com" ```   If `cim.ldap.updateConfig` is `true`, entering a value in `cim.ldap.hostName` will update the configured host name next time you install or upgrade the Helm chart.  See also Change configured LDAP values. |
| ``` cim:   ldap:     updateConfig: ``` | `false` | This key allows you to specify whether the LDAP configuration should be updated during the deployment of the Helm chart.. Set to `true` to enable an LDAP configuration.   - `false` (default) the LDAP configuration will   not be updated. - `true` enables the Helm chart to apply the   specified LDAP configurations during deployment.   See also Change configured LDAP values.  Note: During an initial deployment, you need to configure LDAP using the Connect UI, therefore, this Helm key needs to be `false`. |

## cim.pgpool Helm keys - PostgreSQL read replicas

`cim.pgpool` contains many keys that will be available in a future
release to deploy multiple PostgreSQL database read replicas.

The following table describes the `cim.pgpool` Helm keys

Note: For information on the PostgreSQL database read replication
feature and using Pgpool II Helm keys to configure the replica feature, see Using PostgreSQL read replicas and Pgpool to balance database loads.

Important:

Except for the following Helm keys, you should not change or set values for any
other pgpool Helm keys:

- `cim.pgpool.enable`
- `cim.pgpool.replicadb:`
- `cim.pgpool.maxConnections`

Contact Black Duck support before changing any other pgpool Helm keys.

Important: We do NOT recommend enabling read-only file
system for Pgpool.

Table 20. `cim.pgpool` Helm keys

|  |  |  |
| --- | --- | --- |
| **Key** | **Default value** | **Description** |
| ``` cim:   pgpool:     affinity: ``` | `{}` | Set affinities. |
| ``` cim:   pgpool:     annotations: ``` | `{}` | Additional annotations to add to the deployment metadata. This is a dictionary. |
| ``` cim:   pgpool:     automountServiceAccountToken: ``` | `false` | This Helm key determines whether or not the service account (SA) token is automatically mounted into the `pgpool` pod.   - `false`: The SA token is not automatically   mounted in the `pgpool` pod. - `true`: The SA token is automatically mounted   in the `pgpool` pod.   Mounting the SA token in a pod provides authentication for the pod and enables the pod to access resources.  See also Configuring pod and container security.  To create the SA token, see Generate a Connect SA admin user token. |
| ``` cim:   pgpool:     containerSecurityContext: ``` | `{}` | Set the container security context.  For details, see Configuring pod and container security. |
| ``` cim:   pgpool:     enabled: ``` | `false` | This is not needed to run Connect.   - false: Disable pgpool. Do not create a Pgpool container.  - true: Install pgpool. Create a Pgpool container. Make   sure that at least one database read-replica is   available.   **Note:** Enabling pgpool enables the commit server and redirects all commit-defect traffic to the commit server. |
| ``` cim:   pgpool:     image: ``` | `"pgpool"` | The image name to use. |
| ``` cim:   pgpool:     registry: ``` | `""` | Obtain the Pgpool image from your own registry. |
| ``` cim:   pgpool:     replicadb: ``` | `[]` | Specify the replica databases. By default, `cim.pgpool.replicadb: []` is empty. |
| ``` cim:   pgpool:     replicas: ``` | `1` | Sets the number of Pgpool pod replicas; if Pgpool fails, another Pgpool pod is running and available to take over. Set `cim.pgpool.replicas` greater than 1 for a horizontally scaled deployment. |
| ``` cim:   pgpool:     tolerations: ``` | `[]` | Set tolerations. |
| ``` cim:   pgpool:     version: ``` | `"4.5.4"` | Specifies the image version to use. |

The cim.pgpool.resources Helm keys specify Kubernetes CPU and memory resource limits
and requests.

The following table describes the `cim.pgpool.resources` Helm keys

Table 21. `cim.pgpool.resources` Helm keys

|  |  |  |
| --- | --- | --- |
| **Key** | **Default value** | **Description** |
| ``` cim:   pgpool     resources:       limits:         cpu: ``` | `"2"` |  |
| ``` cim:   pgpool:     resources:       limits:         memory: ``` | `2Gi` |  |
| ``` cim:   pgpool     resources:       limits:         cpu: ``` | `250m` |  |
| ``` cim:   pgpool     resources:       requests:         memory: ``` | `1Gi` |  |

The following `cim.pgpool` Helm keys set Pgpool properties. They are
used with PostgreSQL database read replicas and can be left at their existing
default values as defined in the `cnc` Helm chart.

Table 22. `cim.pgpool` properties Helm keys

|  |  |  |
| --- | --- | --- |
| **Key** | **Default value** | **Description** |
| ``` cim:   pgpool:     childLifeTime: ``` | `300` | Specify the time in seconds to terminate a Pgpool-II child process if it remains idle. The default value is 300 seconds (5 minutes). Setting it to 0 disables the feature. |
| ``` cim:   pgpool:     childMaxConnections: ``` | `0` | Specify the lifetime of a Pgpool-II child process in terms of the number of client connections it can receive. |
| ``` cim:   pgpool:     clientIdleLimit: ``` | `0` | Specify the time in seconds to disconnect a client if it remains idle since the last query. Use this key to prevent Pgpool children from being occupied by lazy clients, or prevent a broken TCP/IP connection between the client and Pgpool-II. The default value is `0`, which turns off the feature.  This parameter can be changed by reloading the Pgpool-II configurations. You can also use the [PGPOOL SET](https://www.pgpool.net/docs/42/en/html/sql-pgpool-set.html) command to alter the value of this parameter for a current session. |
| ``` cim:   pgpool:     connectionCache: ``` | `"on"` | When set to `“on”`, caches connections to backends. The default value is `"on"`.  If you change this value, you need to restart Pgpool-II.  See [Connection Pooling](https://www.pgpool.net/docs/43/en/html/runtime-config-connection-pooling.html) in the pgpool documentation. |
| ``` cim:   pgpool:     connectionLifeTime: ``` | `0` | Specify the time in seconds to terminate cached connections to the PostgreSQL backend. |
| ``` cim:   pgpool:     maxConnections: ``` | `“”` | Specify the maximum number of connections set for the database. maxConnections must be equal to or less than the PostgreSQL max_connections parameter; it must never exceed it. |

## cim.postgres Helm keys - create Connect cim PostgreSQL access job

This section describes `cim.​​postgres` Helm keys that create a job
which enables Coverity Connect to access the Connect PostgreSQL database. You can
use these Helm keys to override values in the `global.postgres` Helm
keys or the `postgres` Helm keys for only this Connect service.
Changing values here does not impact Scan Service or Storage Service values.

For information on the `postgres` Helm keys, see postgres Helm keys - create Connect cim PostgreSQL access job.

Note: These Helm keys do not create the database; the database
must already exist.

Table 23. `cim.postgres` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   postgres:     database: ``` | `"cim"` | The name of the database in which to run the `create db` statements. The database must already exist and cannot be created by this job.  The default value specified in the `postgres.​database` Helm key is "postgres". |
| ``` cim:   postgres:     existingSecret: ``` | `""` | This Helm key enables you to specify an existing Kubernetes PostgreSQL secret name specifically for Coverity Connect that contains the keys:   - `host` - `port` - `username` - `password` |
| ``` cim:   postgres:     host: ``` | `""` | Specify the path and hostname of the PostgreSQL database host. |
| ``` cim:   postgres:     password: ``` | `""` | Specify the password for PostgreSQL access. Encode the password using base64. For example:   ``` % echo -n <password> | base64 ```   Provide the encrypted version of the password.  See also `cim.postgres.user` to provide the username. |
| ``` cim:   postgres:     port: ``` |  | Specify the PostgreSQL SQL server port. TCP port 5432 is used for PostgreSQL. |
| ``` cim:   postgres:     sslmode: ``` | `""` | The PostgreSQL SSL mode for Coverity Connect can be overridden using one of the following values:   - `""` (no override) - `"disable"` - `"allow"` - `"prefer"` - `"require"` - `"verify-ca"` - `"verify-full"`   The default value is `""` which inherits the value set in the `postgres.sslmode` key. For the current SSL value, refer to the `postgres.sslmode` key and any overrides.  For value definitions, see Table 1. |
| ``` cim:   postgres:     user: ``` | `""` | Specify a username for PostgreSQL access.  See also `cim.postgres.password` to provide the password. |

## cim.route Helm keys for Red Hat OpenShift route creation

The `cim.route` Helm keys enable you to define Red Hat OpenShift route
configurations using the cnc Helm chart. In addition to the syntax and definitions
below, for information on OpenShift routing in Coverity cloud, see OpenShift routing - exposing the Coverity cloud instance outside an OpenShift cluster.

Note: If `cim.route.enabled` is
`false`, the ingress controller uses its existing ingress
settings, or values that you can set using the OpenShift UI. To change values using
the Helm chart, you need to change `cim.route.enabled` to
`true`.

Table 24. `cim.route` Helm keys for OpenShift route creation

|  |  |  |
| --- | --- | --- |
| **Key** | **Default value** | **Description** |
| ``` cim:   route:     enabled: ``` | `false` | Enable to create a route using your existing ingress configuration.   - `true` - Enables OpenShift route object   creation using the `cim.route` Helm key   values and annotations. - `false` - Disables OpenShift route object   creation. |
| ``` cim:   route:     annotations: ``` | `{}` | Use this Helm key to provide annotations to the route object. You can create annotations that define route characteristics such as TLS and ingress controller settings, load balancer behavior, selecting a router, etc. |
| ``` cim:   route:     hosts: ``` | `[]` | Create an array of allowed host names. If empty, the router will use host names from the ingress configuration. |
| ``` cim:   route:     targetPort: ``` | `8080` | The target port for the route. |
| ``` cim:   route:     tls:       enabled: ``` | `true` | Defines whether or not TLS termination is enabled for the route.   - `true` - TLS is enabled for the route. - `false` - TLS is disabled for the route. |
| ``` cim:   route:     tls:       termination: ``` | `"edge"` | Specify the TLS termination type:   - `"edge"` - The Ingress controller decrypts   incoming TLS traffic. - `"passthrough"` - The Ingress controller   forwards the encrypted TLS traffic directly to the backend   service. It does not terminate the TLS connection. - `"reencrypt"` - The Ingress controller   terminates the client-side TLS connection, decrypts the   traffic, and then re-encrypts it before forwarding it to the   backend service |
| ``` cim:   route:     tls:       secrets: ``` | `[]` | Array of TLS secrets with schema (same as ingress):   - secretName: "tls-secret-name" - `hosts: ["example.com"]` - `reencrypt`   Note: If this value is empty, the router will inherit TLS secrets from the ingress.TLS configuration. |
| ``` cim:   route:     tls:       insecureEdgeTerminationPolicy: ``` | `""` | Policy for handling insecure connections. `insecureEdgeTerminationPolicy` is a field within the `tls` section of an OpenShift route object, specifically used with "Edge" terminated routes. It defines how the OpenShift router handles insecure (HTTP) traffic when a secure (HTTPS) route is configured.   - `"None"` or `""`- Default   value. HTTP requests to the route are blocked or   rejected. - `"Allow"` - Allow both secure (HTTPS) and   insecure (HTTP) traffic to reach the route. - `"Redirect"` - Redirect insecure (HTTP)   traffic to the secure (HTTPS) scheme. |
| ``` cim:   route:     wildcardPolicy: ``` | `"None"` | Route wildcard policy, which controls how wildcard DNS hostnames are handled:   - `"None"` - Default value. Allow only the   exact hostname specified in the route. - `"Subdomain"` - Allow all subdomains of the   specified host. |

## cim.setupJob Helm keys

The following Helm keys create a job which creates a database. The
`.resources.` keys specify job resource limits and requests.

Table 25. `cim.setupJob` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cim:   setupJob:     activeDeadlineSeconds: ``` | `3600` | The time limit to allow a job to run. |
| ``` cim:   setupJob:     automountServiceAccountToken: ``` | `false` | This Helm key determines whether or not the service account (SA) token is automatically mounted into the `setupJob` pod.   - `false`: The SA token is not automatically   mounted in the `setupJob` pod. - `true`: The SA token is automatically mounted   in the `setupJob` pod.   Mounting the SA token in a pod provides authentication for the pod and enables the pod to access resources.  See also Configuring pod and container security.  To create the SA token, see Generate a Connect SA admin user token. |
| ``` cim:   setupJob:     containerSecurityContext: ``` | `{}` | Set the container security context.  For details, see Configuring pod and container security. |
| ``` cim:   setupJob:     createDatabases: ``` | `true` | - `true` runs a job which creates a database   and optionally a database user. - `false` does not create a database. |
| ``` cim:   setupJob:     enabled: ``` | `true` | - `true` enables the database setup job. - `false` disables the database setup job. |
| ``` cim:   setupJob:     extraVolumes: ``` | [] | Use this Helm key to specify additional volumes to add to the the cim.setup job. |
| ``` cim:   setupJob:     initContainers: ``` | [] | Use this Helm key to specify init containers to inject into the the cim.setup job.  You might specify init containers when attaching a Cloud SQL proxy native sidecar container in GCP. See:   - Attaching a Cloud SQL proxy native sidecar container in GCP - <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/> |
| ``` cim:   setupJob:     resources:       limits:         cpu: ``` | `"0.5"` | Specifies the maximum number of CPUs for the cim.setup job. |
| ``` cim:   setupJob:     resources:       limits:         memory: ``` | `"1Gi"` | Specifies the maximum amount of memory for the cim.setup job. |
| ``` cim:   setupJob:     resources:       requests:         cpu: ``` | `"0.5"` | Specifies the requested number of CPUs for the cim.setup job. |
| ``` cim:   setupJob:     resources:       requests:         memory: ``` | `"1Gi"` | Specifies the requested amount of memory for the cim.setup job |

## cnc-db-admin Helm keys

The following Helm keys provide a utility container, which can be shelled into for
database administration tools.

Table 26. `cnc-db-admin` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cnc-db-admin:   automountServiceAccountToken: ``` | `false` | This Helm key determines whether or not the service account (SA) token is automatically mounted into the `cnc-db-admin` pod.   - `false`: The SA token is not automatically   mounted in the `cnc-db-admin` pod. - `true`: The SA token is automatically mounted   in the `cnc-db-admin` pod.   Mounting the SA token in a pod provides authentication for the pod and enables the pod to access resources.  See also Configuring pod and container security.  To create the SA token, see Generate a Connect SA admin user token. |
| ``` cnc-db-admin:   containerSecurityContext: ``` | `{}` | Set the container security context.  For details, see Configuring pod and container security. |
| ``` cnc-db-admin:   enabled: ``` | `true` | - `true` = Deploy a cnc-db-admin container with   a replica count of 0. The deployment will need to be scaled   up to 1 replica. - `false` = Do not deploy a cnc-db-admin   container. |
| ``` cnc-db-admin:   extraVolumes: ``` | [] | Additional volumes to add to the `cnc-db-admin` pod. |
| ``` cnc-db-admin:   initContainers: ``` | [] | Init containers to inject into the `cnc-db-admin` pod. |

## minioGateway Helm keys

The following MinIO gateway configuration Helm keys map the MinIO gateway used by
templates.

Table 27. `minioGateway` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` minioGateway:   fullnameOverride: ``` | ``` "" ``` | Important: The `minioGateway.fullnameOverride:` key value must match the `minio.fullnameOverride` key value set in the MinIO sub-chart. |
| ``` minioGateway:   gateway:     enabled: ``` | ``` false ``` | Set to `true` to create HTTP route + NGF policies for MinIO upload routing.  Set to `false` to disable `minio.ingress.enabled` when using Gateway API (they are mutually exclusive). |
| ``` minioGateway:   gateway:     namespace: ""     name: "" ``` | ``` "" ``` | Gateway resource name and namespace. |
| ``` minioGateway:   gateway:     hostnames: ``` | ``` [] ``` | Optional hostname for the HTTP route. |
| ``` minioGateway:   gateway:     path: ``` | ``` "/upload" ``` | MinIO upload path. |
| ``` minioGateway:   gateway:     pathType: ``` | ``` "PathPrefix" ``` | Path matching type. |
| ``` minioGateway:   gateway:     backendPort: ``` |  | Backend port for MinIO service. |
| ``` minioGateway:   gateway:     sectionName: ``` | ``` "" ``` | Optional section name for the listener. |
| ``` minioGateway:   gateway:     backendWeight: ``` | ``` null ``` | Optional backend weight for canary deployments. |
| ``` minioGateway:   gateway:     filters: ``` | ``` [] ``` | Optional filters for the HTTP route. |
| minioGateway: gateway: policies: clientSettings: enabled: false body: maxSize: "" timeout: "" keepAlive: requests: timeout: server: "" header: "" |  | ClientSettingsPolicy — request body size + keep-alive for upload connections.  `clientSettings:` policy — request body size + keep-alive for upload connections.  `enabled:` - Enable ClientSettingsPolicy  `body.maxSize:` - Maximum allowed request body size for MinIO uploads (e.g. "8g", "500m").  `body.timeout:` - Body receive timeout.  `keepAlive.requests:` - Maximum keep-alive requests per connection.  `keepAlive.requests:server:`Keep alivet imeout on the server side.  `keepAlive.requests:header:`Keep alive header timeout sent to clients. |
| ``` minioGateway:   gateway:     policies:       upstreamSettings:         enabled: false         keepAlive:           connections:           requests:           time: ""           timeout: "" ``` |  | `upstreamSettings:` policy — Connection pooling to the MinIO backend service.  `upstreamSettings.enabled:` — Enable upstreamSettings policy. `keepalive.connections:` — Maximum number of idle keep-alive connections to MinIO. `keepalive.requests:` — Maximum requests per keep-alive connection before it is closed.  `keepalive.time:` — How long a keep-alive connection stays open.  `keepalive.timeout:` — Idle timeout before closing a keep-alive connection. |
| ``` minioGateway:   gateway:     policies:       snippetsFilter:         enabled: false         connectTimeout: ""         nextUpstream: ""         nextUpstreamTimeout: ""         nextUpstreamTries: ""         readTimeout: ""         sendTimeout: ""         proxyBuffering: "" ``` |  | `snippetsFilter:` policies — NGINX proxy directives injected into the MinIO route location.  `snippetsFilter.enabled:` — Set to true only when NGF is running with snippets enabled.  `snippetsFilter.connectTimeout:` — Time to wait for a connection to MinIO to be established.  `snippetsFilter.nextUpstream:` — Conditions under which the request is passed to the next upstream.  `snippetsFilter.nextUpstreamTimeout:` — Timeout for passing the request to the next upstream.  `snippetsFilter.nextUpstreamTries:` — Number of next-upstream retries.  `snippetsFilter.readTimeout:` — Timeout for reading a response from MinIO.  `snippetsFilter.sendTimeout:` — Timeout for sending a request to MinIO.  `snippetsFilter.proxyBuffering:` — Disable response buffering for large file uploads/downloads. |

## onPrem Helm keys

Use these keys to enable onPrem OCI MinIO, Redis, and PostgreSQL. See also:

- Enabling OCI Redis, MinIO, and PostgreSQL

Note: You can enable any or all of onPrem OCI MinIO, Redis, and
PostgreSQL.

Table 28. `onPrem` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` onPrem:   minio: ``` | `false` | To enable onPrem OCI MinIO, override this Helm key value with `true`. You must then uncomment the `cnc` chart `onPrem.minio:` Helm keys identified below in onPrem.minio: Helm keys. |
| ``` onPrem:   redis: ``` | `false` | To enable onPrem OCI Redis, override this Helm key value with `true`. You must then uncomment the `cnc` chart `onPrem.redis:` Helm keys identified below in onPrem.redis: Helm keys. |
| ``` onPrem:   postgres: ``` | `false` | To enable onPrem PostgreSQL, override this Helm key value with `true`. You must then uncomment the `cnc` chart `onPrem.postgresql:`: Helm keys identified in onPrem.postgresql: Helm keys. |

## onPrem.minio: Helm keys

If you enable onPrem OCI using the Helm override `onPrem.minio: true`
(see onPrem Helm keys above), you must uncomment these Helm
keys for them to be available to deploy `onPrem.minio:`. For
additional information, refer to Enabling OCI Redis, MinIO, and PostgreSQL.

```
# minio:
#   global:
#     security:
#       allowInsecureImages: true
#   fullnameOverride: "cnc-minio"
#   # MinIO Server - July 23rd, 2025
#   image:
#     registry: registry-1.docker.io
#     repository: bitnamilegacy/minio
#     tag: "2025.7.23-debian-12-r3"
#     debug: true
#   # MinIO Client - July 21st, 2025
#   clientImage:
#     registry: registry-1.docker.io
#     repository: bitnamilegacy/minio-client
#     tag: "2025.7.21-debian-12-r2"
#   # Default Init Containers Volume Permissions
#   defaultInitContainers:
#     volumePermissions:
#       image:
#         registry: registry-1.docker.io
#         repository: bitnamilegacy/os-shell
#         tag: "12-debian-12-r51"
#   # Console/Gateway Image
#   console:
#     image:
#       registry: registry-1.docker.io
#       repository: bitnamilegacy/minio-object-browser
#       tag: "2.0.2-debian-12-r3"
#   ingress:
#     enabled: true
#     ingressClassName: nginx
#     hostname: local.connect.example.com
#     extraTls:
#     - hosts:
#         - local.connect.example.com
#       secretName: cnc-cim-tls-nginx
#     path: "/upload(/|$)(.*)"
#     annotations:
#       ingress.kubernetes.io/hsts: "true"
#       ingress.kubernetes.io/ssl-redirect: "true"
#       nginx.ingress.kubernetes.io/enable-access-log: "true"
#       nginx.ingress.kubernetes.io/proxy-body-size: 8g
#       nginx.ingress.kubernetes.io/proxy-connect-timeout: "5"
#       nginx.ingress.kubernetes.io/proxy-next-upstream: error timeout
#       nginx.ingress.kubernetes.io/proxy-next-upstream-timeout: "0"
#       nginx.ingress.kubernetes.io/proxy-next-upstream-tries: "3"
#       nginx.ingress.kubernetes.io/rewrite-target: /$2

#   podAnnotations:
#     prometheus.io/scrape: "true"
#     prometheus.io/path: "/minio/v2/metrics/cluster"
#     prometheus.io/port: "9000"
#   persistence:
#     size: 50Gi

#   # This sidecar is needed when the cache-service is enabled which will set the lifecycle configuration for the cache-service bucket
#   #   This sidecar needs a secret with key minio-access-key, minio-secret-key which will be created by minio helm chart itself with minio release name
#   #   Please update the cache_bucket_name, retention-days and other env's accordingly
#   sidecars:
#     - name: minio-lifecycle
#       image: registry-1.docker.io/bitnamilegacy/minio-client:2025.7.21-debian-12-r2
#       imagePullPolicy: IfNotPresent
#       env:
#         - name: cache_bucket_name
#           value: coverity-cache
#         - name: cache-retention-limit
#           value: "30"
#         - name: minio-host
#           value: cnc-minio
#         - name: minio-port
#           value: "9000"
#         - name: minio-access-key
#           valueFrom:
#             secretKeyRef:
#               name: cnc-minio
#               key: root-user
#         - name: minio-secret-key
#           valueFrom:
#             secretKeyRef:
#               name: cnc-minio
#               key: root-password
#       command: ["/bin/bash","-c"]
#       args:
#         - |
#           echo "waiting for minio..."

#           until (mc alias set cnc http://$(minio-host):$(minio-port) $(minio-access-key) $(minio-secret-key) && mc ls cnc/$(CACHE_BUCKET_NAME))
#           do sleep 5;
#           done;
#           mc ilm add --expiry-days $(cache-retention-limit) cnc/$(cache_bucket_name);
#           tail -f /dev/null;
```

## onPrem.redis: Helm keys

If you enable onPrem OCI using the Helm override `onPrem.redis: true`
(see onPrem Helm keys above), you must uncomment these Helm
keys for them to be available to deploy `onPrem.redis:`. For
additional information, refer to Enabling OCI Redis, MinIO, and PostgreSQL.

```
# onPrem helm overrides for open-source sub-charts
# redis:
#   global:
#     security:
#       allowInsecureImages: true
#   fullnameOverride: "cache-redis"
#   architecture: standalone
#   # Redis bitnami legacy images - Aug 22nd, 2025
#   image:
#     registry: registry-1.docker.io
#     repository: bitnamilegacy/redis
#     tag: "8.2.1-debian-12-r0"
#   # Redis Sentinel - Aug 19th, 2025
#   sentinel:
#     image:
#       registry: registry-1.docker.io
#       repository: bitnamilegacy/redis-sentinel
#       tag: "8.2.1-debian-12-r0"
#   metrics:
#     enabled: true
#     # Redis Exporter - Aug 24th, 2025
#     image:
#       registry: registry-1.docker.io
#       repository: bitnamilegacy/redis-exporter
#       tag: "1.76.0-debian-12-r0"
#   # Volume Permissions - Aug 19th, 2025
#   volumePermissions:
#     image:
#       registry: registry-1.docker.io
#       repository: bitnamilegacy/os-shell
#       tag: "12-debian-12-r51"
#   # Kubectl - Aug 23rd, 2025
#   kubectl:
#     image:
#       registry: registry-1.docker.io
#       repository: bitnamilegacy/kubectl
#       tag: "1.33.4-debian-12-r0"
#   # Sysctl - Aug 19th, 2025
#   sysctl:
#     image:
#       registry: registry-1.docker.io
#       repository: bitnamilegacy/os-shell
#       tag: "12-debian-12-r51"
#   master:
#     persistence:
#       enabled: false
#     resources:
#       limits:
#         cpu: "0.5"
#         memory: 1.1Gi
#       requests:
#         cpu: "0.5"
#         memory: 1.1Gi
#   tls:
#     enabled: true
#     autoGenerated: true
#     certFilename: "certificate.pem"
#     certKeyFilename: "key.pem"
#     certCAFilename: "ca.crt"
#     authClients: false
#   # please modify/override below configurations to increase the maxmemory for redis
#   commonConfiguration: |-
#     save ""
#     appendonly no
#     maxmemory 1gb
#     maxmemory-policy noeviction
```

## onPrem.postgresql: Helm keys

If you enable onPrem OCI using the Helm override `onPrem.postgres:
true` (see onPrem Helm keys above), you must
uncomment these Helm keys for them to be available to deploy
`onPrem.postgresql:`. For additional information, refer to Enabling OCI Redis, MinIO, and PostgreSQL.

```
# postgresql:
#   primary:
#     pgHbaConfiguration: |
#       local   all             all                               md5
#       host    all             all             0.0.0.0/0         md5
#       host    all             all             ::/0              md5
#       host    all             all             127.0.0.1/32      md5
#       host    all             all             ::1/128           md5
#     args:
#       - "-c"
#       - "hba_file=/bitnami/postgresql/conf/pg_hba.conf"
#       # Comment these if TLS is to be disabled. Ensure the certificate filenames
#       # in ssl_cert_file and ssl_key_file match the certFilename and certKeyFilename
#       # specified in the tls section below if tls is enabled (currently: certificate.pem and key.pem)
#       - "-c"
#       - "ssl=on"
#       - "-c"
#       - "ssl_cert_file=/opt/bitnami/postgresql/certs/certificate.pem"
#       - "-c"
#       - "ssl_key_file=/opt/bitnami/postgresql/certs/key.pem"
#     extraVolumes:
#       - name: postgres-run
#         emptyDir: { }
#     extraVolumeMounts:
#       - name: postgres-run
#         mountPath: /var/run/postgresql
#   commonAnnotations:
#     helm.sh/hook: "pre-install, pre-upgrade, pre-rollback"
#     helm.sh/hook-weight: "-13"
#   fullnameOverride: "cim-pg-postgresql"
#   auth:
#     database: "postgres"
#     postgresPassword: "postgres"
#   image:
#     registry: registry-1.docker.io
#     repository: "postgres"
#     tag: "18.4"
#     pullSecrets: ["gar-key"]
#   metrics:
#     enabled: true
#     image:
#       registry: registry-1.docker.io
#       repository: "prometheuscommunity/postgres-exporter"
#       tag: "v0.19.1"
#   volumePermissions:
#     enabled: true
#     image:
#       registry: registry-1.docker.io
#       repository: "alpine"
#       tag: "3.21.7"
#   tls:
#     enabled: true
#     certFilename: "certificate.pem"
#     certKeyFilename: "key.pem"
#     certificatesSecret: "postgres-certificates-tls-secret"
```

## postgres Helm keys - create Connect cim PostgreSQL access job

The following `​postgres` Helm keys create jobs that that enable the
Connect (cim) Service to access the Connect PostgreSQL database. These keys can be
used by the Connect (cim) service, or they can be overridden as needed by the
Connect (`cim.postgres`) Helm keys. See cim.postgres Helm keys - create Connect cim PostgreSQL access job.

Table 29. `postgres` Helm keys

| Key | Default Value | Description |
| --- | --- | --- |
| ``` postgres:   database: ``` | `"postgres"` | The name of the database in which to run the `create db` statements. The database must already exist and cannot be created by this job. This parameter is required. |
| ``` postgres:   existingSecret: ``` | `""` | This Helm key enables you to specify an existing Kubernetes PostgreSQL secret name to be used for all services unless overridden by specific services. The secret must contain the following values:   - `host` - `port` - `username` - `password` |
| ``` postgres:   host: ``` | `""` | Specifies the PostgreSQL host. For example, "cim".  Use this key if you have not created a secret. |
| ``` postgres:   jobSidecars: ``` | [] | You can use this Helm key to specify sidecar containers to add within pods that require a PostgreSQL database connection. This sidecar is a native sidecar, which is an init container with `restartPolicy:Always`; you must set `restartPolicy:Always`.  Native sidecar containers require Kubernetes 1.28 or later.  For example, for gcp:   ``` postgres:   jobSidecars:     - name: cloud-sql-proxy       image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.1.0-buster       restartPolicy: Always       command: ["/bin/sh","-ec"]       args: ["/cloud-sql-proxy              --structured-logs              --port=5432 <gcp-project>:<region>:testgcp-zirw98              --credentials-file=/secrets/key.json              --max-sigterm-delay=100s "]       securityContext:         runAsUser: 5000       volumeMounts:         - name: gcp-sa-secret           mountPath: /secrets/           readOnly: true       resources:         requests:           memory: "500Mi"           cpu: "500m" ```   For further information on using this and related Helm keys, refer to Attaching a Cloud SQL proxy native sidecar container in GCP.  See also: <https://kubernetes.io/blog/2023/08/25/native-sidecar-containers/>. |
| ``` postgres:   password: ``` | `""` | Specifies the password to connect to the PostgreSQL host for a Connect instance.  Use this key if you have not created a secret. |
| ``` postgres:   port: ``` |  | Use port 5432 for all instances of PostgreSQL.  Use this key if you have not created a secret. |
| ``` postgres:   sidecars: ``` | [] | The sidecar container specification to attach for pods that require a database connection. The sidecar is added as a native sidecar, which is an init container with `restartPolicy:Always`; you must set`restartPolicy:Always`. You must have Kubernetes 1.28 or later to support native-sidecar.  For further information on using this and related Helm keys, refer to Attaching a Cloud SQL proxy native sidecar container in GCP.  See also: <https://kubernetes.io/blog/2023/08/25/native-sidecar-containers/>.  For example:   ``` postgres:   sidecars:     - name: cloud-sql-proxy       image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.1.0-buster       restartPolicy: Always          args:         #- "--private-ip"         - "--structured-logs"         - "--port=5432"         - "<gcp-project>:<region>:testgcp-zirw98"         - "--max-sigterm-delay=2s"         - "--credentials-file=/secrets/key.json"       securityContext:         runAsUser: 5000     volumeMounts:       - name: gcp-sa-secret         mountPath: /secrets/         readOnly: true     resources:       requests:         memory: "500Mi"         cpu: "500m" ```   where the `args:` are:   - `--private-ip` If you are connecting from   a VPC-native GKE cluster, you can use this flag to have   the proxy connect over private IP. - `--structured-logs` Enable structured   logging with LogEntry format. - `--port=5432` Replace   `DB_PORT` with the port the that the   proxy should listen on. - `<gcp-project>:<region>:testgcp-zirw98`   cloudsql instance name - `--max-sigterm-delay=2s` Allow for   connections to close - `--credentials-file=/secrets/key.json"   securityContext:` This flag specifies where   the service account key can be found |
| ``` postgres:   sslmode: ``` | `""` | The PostgreSQL SSL mode must be one of the following values:   - `"disable"` - `"allow"` - `"prefer"` - `"require"` - `"verify-ca"` - `"verify-full"`   The default value is `"verify-ca"`.  For further information, see Select the PostgreSQL sslmode and find the PostgreSQL root certificate for TLS.  For value definitions, see Table 1. |
| ``` postgres:   user: ``` | "" | The username to connect to the PostgreSQL host.  Use this key if you have not created a secret. |

## proxy Helm keys

The following Helm keys define TLS forward proxy values that apply to the
`cnc` chart. The following proxy parameters configure forward
proxy, which acts as a Man-In-The-Middle. The keys within this group can be used to
override global key values for this `cnc` chart.

See also:

- To configure TLS forward proxy, see Configuring TLS forward proxy

Table 30. `proxy` Helm keys

| Key | Default Value | Description |
| --- | --- | --- |
| ``` proxy:   enabled: ``` | `false` | This boolean Helm key enables or disables TLS forward proxy globally within the cluster.   - `true` - Enables TLS forward proxy. - `false` - Disables TLS forward proxy. |
| ``` proxy:   host: ``` | `""` | This string Helm key specifies the proxy host server. |
| ``` proxy:   port: ``` | 3128 | Specifies the proxy port that the host server listens on. |
| ``` proxy:   tlsmode: ``` | `"tls"` | The TLS proxy mode must be one of the following values:   - `"insecure"` = Specifies TLS insecure proxy.   This mode enables you to communicate over http instead of   https.. This is an insecure mode. - `"tls"` = specifies TLS proxy, where the   client authenticates the server. - `"mtls"` = specifies mutual TLS mode, where   the client and server authenticate each other.   The default value is `"tls"`.  When TLS mode is set to either tls or mtls, the proxy server CA certificate must be included in the trust-stores ConfigMap with key name `"proxy-server.pem"`.  The file names of other server CA certificates (excluding postgres, proxy server) are not important.  For example: The Black Duck artifactory server CA certificate can be named `artifactory.pem` in the trust-stores ConfigMap. |
| ``` proxy:   existingSecret: ``` | `""` | If proxy is enabled with `tlsmode` set to `"mtls",` this secret must be contain the following keys: `"client-cert"` and `"client-key"`.  If proxy is enabled with `tlsmode` set to `"insecure"` or `"tls"`, an `existingSecret` is not needed. |

## scan-services.enabled Helm key

This Helm key defines whether or not the `scan-services` Helm subchart
becomes part of the Docker manifest, and therefore determines if Scan Services can
be deployed in the Coverity Kubernetes cluster.

Table 31. `scan-services.enabled` Helm key

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-services:   enabled: ``` | `false` | Defines if the `scan-services` Helm subchart becomes part of the Docker manifest, and therefore determines if Scan Services can be deployed in the Coverity Kubernetes cluster. The value is either `true` or `false` as follows:   - `true` = Enables use of the   `scan-services` Helm chart which defines   deployment of Scan Services within the Kubernetes Coverity   cluster. the `scan-services` Helm chart   becomes part of the Docker manifest. - `false` = For a Connect-only deployment in   Kubernetes. This option disables use of the   `scan-services` Helm chart.   See also:   - cnc Helm chart and the Chart.yaml file - Disabling the scan-services Helm subchart for a Connect-only deployment - Enabling the scan-services Helm subchart |

## triage-suggestion-service: Helm keys

AI-Assisted Triage Plug-in is AI-powered microservice that provides intelligent
triage suggestions for security findings. This is an optional component that can be
enabled independently.

Important: AI-Assisted Triage Plug-in is a Beta
release feature.

Note: See also:

- For deployment and configuration information: Deploying the AI-Assisted Triage Plug-in
- For upgrade information: Upgrading to 2026.3 and Performing an upgrade.
- For the `triage-suggestion-service` Helm subchart: triage-suggestion-service Helm subchart
- For `triage-suggestion-service` container images: Coverity container images

Table 32. `triage-suggestion-service:` Helm
keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` triage-suggestion-service:   enabled: ``` | `false` | Set to true to deploy the triage-suggestion-service along with CNC. Valid values:   - `true` = deploy   `triage-suggestion-service` in Coverity   cloud. - `false` = do not deploy   `triage-suggestion-service` in Coverity   cloud. |
| ``` triage-suggestion-service: ``` |  | In this field, you can override `triage-suggestion-service`Helm chart values.  You can enter Helm keys from the `triage-suggestion-service` Helm chart to customize the AI-Assisted Triage Plug-in deployment in Coverity cloud. The values you configure here will override the values in the `triage-suggestion-service` Helm chart.  See triage-suggestion-service Helm subchart |

## trust-stores: ConfigMap Helm keys - Connect cim specific

The following `trust-stores:` ConfigMap Helm keys add truststore
ConfigMap certificates to a single Coverity Connect instance.

These keys can override the `global.trust-stores:` keys for the
Connect cim service.

Table 33. `trust-stores` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` trust-stores:   configmapName: ``` | `""` Note: The global default value is `global.trust-stores.configmapName: "connect-trust-stores"`. | This Helm key specifies the name of the truststore ConfigMap that contains the Connect truststore certificates. The default name is `connect-trust-stores` as defined in the `global.trust-stores.​configmapName` key.  Example of the `connect-trust-stores` ConfigMap for the Connect pod:   ``` kubectl create configmap connect-trust-stores \      --from-file=postgres-root.pem=<postgres-root.pem> \      --from-file=proxy-server.pem=<proxy-server.pem> \      --from-file=<LDAP-root-cert> \      --from-file=<Jira-root-cert> \      --from-file=<Bugzilla-root-cert> \      --namespace "$NS" ```   Important: The PostgreSQL root certificate must be named `postgres-root.pem`.  The names of all files except PostgreSQL root certificate are not important; they are mounted into the same directory. All files in that directory are treated as certificates and loaded into the Coverity Connect truststore.  For further information on creating ConfigMaps, refer to the appropriate section(s) for your deployment:   - For a Connect instance: Creating a truststore ConfigMap for a Connect instance |
| ``` trust-stores:   enabled: ``` | Note: The global default value is `global.trust-stores.enabled: false`. | - `true` = enable importing certificates into   the Coverity Connect truststore. - `false` = disable importing certificates into   the Coverity Connect truststore. |
