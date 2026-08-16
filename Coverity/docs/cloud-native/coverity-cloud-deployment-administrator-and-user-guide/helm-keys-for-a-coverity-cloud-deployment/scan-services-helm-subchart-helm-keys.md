---
title: "scan-services Helm subchart: Helm keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scan-services-helm-subchart-helm-keys.html"
content_id: "V79hPihhSOnTedK6eV_ZWQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:46:05.465221+00:00"
---

# scan-services Helm subchart: Helm keys

This section describes Helm keys in the scan-services subchart.

Important: When you either create a custom
`.yaml` file or set a Helm key within a command such as `helm
install`, you must prepend any keys from a subchart with the subchart name.
Therefore, you must prepend scan-services chart Helm keys with
`scan-services` to identify them as scan-services chart keys.

Important: The scan-services Helm subchart is not used
with a Connect-only deployment.

Important: Unless otherwise noted, the Helm keys in this
section are in the `scan-services` subchart.

Important:

When overriding any `scan-services` Helm subchart key from outside the
`scan-services` subchart `values.yaml` file, you
must precede the key name with `scan-services` to identify the key as
a `scan-services` chart key:

```
scan-services:
  cache-service:
    #overrides
  scan-service:
    #overrides
  storage-service:
    #overrides
```

For information on subcharts and overrides, see scan-services Helm subchart and [Subcharts and Global Values](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/).

The `scan-services` chart keys include the following categories:

- `cache-service`
- `common-infra`
- `ingress`
- `postgres`
- `proxy`
- `scan-service`
- `storage-service`
- `trust-stores`

## Global Helm keys

For `global` Helm key information, see: Global Helm keys.

## Root Helm keys

For root Helm key information, see: Root Helm keys.

## cache-service Helm keys

The following Helm keys define Cache Service variables. Cache Service provides
analysis caching capabilities.

Table 1. `cache-service` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cache-service:   affinity: ``` | `{}` | Sets the affinity. |
| ``` cache-service:   annotations: ``` | `{}` | Annotation for the cache service. |
| ``` cache-service:   automountServiceAccountToken: ``` | `false` | This Helm key determines whether or not the service account (SA) token is automatically mounted into the `cache-service` pod.   - `false`: The SA token is not automatically   mounted in the `cache-service` pod. - `true`: The SA token is automatically mounted   in the `cache-service` pod.   Mounting the SA token in a pod provides authentication for the pod and enables the pod to access resources.  See also Configuring pod and container security.  To create the SA token, see Generate a Connect SA admin user token. |
| ``` cache-service:   bucketName: ``` | `""` | Specifies the name of the storage bucket or blob container used by the Cache Service. Amazon AWS, Google GCP, and MinIO call the storage a bucket. Microsoft Azure uses the term blob container for the cache storage within the storage account. |
| ``` cache-service:   containerSecurityContext: ``` | `{}` | Set the container security context.  For details, see Configuring pod and container security. |
| ``` cache-service:   enabled: ``` | `true` | Enable the cache service:   - `true` = cache service is enabled for capture   and analysis. - `false` or no value = capture and analysis   will run without caching. |
| ``` cache-service:   exposeMetrics: ``` | `true` | - `true` = Expose time series metrics in   Prometheus format. - `false` = Do not expose time series   metrics. |
| ``` cache-service:   extraVolumes: ``` | `[]` | Specifies additional volumes to add to the Cache Service pod. For further information, see:   - for generic custom storage, see Storage service custom domains. - for Dell ECS S3 storage, see Configure Dell ECS storage support. |
| ``` cache-service:   extraVolumeMounts: ``` | `[]` | Use annotations in this Helm key to specify additional volume mounts to add to the Cache Service pod.  The syntax is::   ``` cache-service:   extraVolumeMounts:     - name: <cacheServiceSecretVolumeName>       secret:         secretName: <secretName> ```   For example, to mount in a cache service pod, an OTel agent that collects telemetry data from the pod and forwards it to a backend for analysis and visualization, including performance metrics, traces, and logs :   ``` scan-services:   cache-service:     javaOpts: "-javaagent:/coverity/otel/opentelemetry-javaagent.jar -Dotel.metrics.exporter=none                 -Dotel.service.name=cache-service -Dotel.traces.exporter=jaeger                 -Dotel.exporter.jaeger.endpoint=http://my-hunter-jaeger-collector.metrics.svc.cluster.local:14250"     storageProvider: "minio"     extraVolumes:       - name: otel-agent         emptyDir: {}     extraVolumeMounts:       - name: otel-agent         mountPath: /coverity/otel ```   For Dell ECS S3 storage, see Configure Dell ECS storage support. |
| ``` cache-service:   image: ``` | `"cache-service"` | The name of the Cache Service container image. Do not override this value. |
| ``` cache-service:   initContainers: ``` | `[]` | This Helm key specifies init containers to inject into the Cache Service pod.  You might specify init containers when attaching a Cloud SQL proxy native sidecar container in GCP. See:   - Attaching a Cloud SQL proxy native sidecar container in GCP - <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/> |
| ``` cache-service:   javaOpts: ``` | `""` | Additional options to add to Java invocation. |
| ``` cache-service:   logLevel: ``` | `"INFO"` | Specifies the minimum logging level used to generate logs. Valid values include:   - ALL - TRACE - INFO This is the default value. INFO presents all log   levels from informational through the highest level. - WARN - ERROR - FATAL - OFF Not recommended. Disables logging.   Note: The log levels can be all uppercase or all lowercase, and can be encased in double-quotes for string value.  See also Specifying logging levels. |
| ``` cache-service:   nodeSelector: ``` | `{}` | Sets the node selector. |
| ``` cache-service:   podAnnotations: ``` | `{}` | Additional annotations to add to the pod metadata. This is a dictionary. |
| ``` cache-service:   podSecurityContext: ``` | `{}` | Sets the Cache Service pod security context. |
| ``` cache-service:   registry: ``` | `""` | The container image registry to use. Use this only if this container is not in the registry specified by the `imageRegistry` Helm key. |
| ``` cache-service:   storageProvider: ``` | `"minio"` | Specifies which cloud platform is used by the Cache Service. Valid values are:  - `aws` - `azure` - `gcp` - `minio` |
| ``` cache-service:   tolerations: ``` | `[]` | Sets tolerations for cache service. If you are deploying Coverity on ARM64 nodes, and if a global toleration is not used, this toleration must be configured.  For example, to deploy cache service on ARM64 nodes only:   ``` cache-service:     tolerations:         - key: "kubernetes.io/arch"           operator: "Equal"           value: "arm64"           effect: "NoSchedule" ```   Note: Refer to:  - Setting up ARM64 support - <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/> |
| ``` cache-service:   version: ``` | `"CACHE_SERVICE_​VERSION"` | The image version. Use this only if this container image is not the version specified by the `imageVersion` Helm key. |

## cache-service.aws Helm keys

If the `cache-service.​storageProvider` is `aws`, then
the keys below need to be set.

Important: For further information on configuring
`cache-service.aws` Helm keys, see Configuring Helm keys to support AWS using S3 or S3 Express within the section Amazon AWS infrastructure and configuration.

Table 2. `cache-service.aws` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cache-service:   aws:     region: ``` | `""` | Region of AWS S3 bucket. |
| ``` cache-service:   aws:     secret: ``` | `""` | The name of the AWS secret that contains the AWS access keys:   - aws_access_key - aws_secret_key   Refer to Create an AWS storage service secret. |
| ``` cache-service:   aws:     serviceAccount: ``` | `""` | For IAM roles, you can specify the name of a role-based AWS service account. To create a role-based AWS service account refer to Using a role-based AWS service account for Storage Service and Cache Service. If a service account is specified in this key, AWS credentials (access_keys) specified in the `cache-service.​aws.secret` Helm key will not be used. |
| The following `enabled` and `ttlDays` keys are S3 Express (Directory) bucket variables needed by the cache service. For Helm key overrides, see also Configure AWS S3 Express Helm keys. | | |
| ``` cache-service:   aws:     enabled: ``` | `false` | Do NOT enable AWS S3 Express cache service if the general purpose bucket is configured.  This key must be set to `true` when S3Express (Directory) bucket is configured. |
| ``` cache-service:   aws:     s3Express:       ttlDays: ``` | `90` | Indicates the number of days to retain cached objects. Helps the cache service delete old or expired objects from the cache bucket. |

## cache-service.azure Helm keys

If the `cache-service.​storageProvider` is `azure`, you
need to set the following key.

Important: For further information on configuring
`cache-service.azure` Helm keys, see Configure Helm keys to support Azure using Azure blob within the section Microsoft Azure infrastructure and configuration.

Table 3. `cache-service.azure` Helm key

| Key | Default value | Description |
| --- | --- | --- |
| ``` cache-service:   azure:     secret: ``` | `""` | Specifies the Kubernetes Azure secret that contains the following Azure credentials:   - `azure_client_id` - `azure_client_secret` - `azure_endpoint` - `azure_resource_group` - `azure_subscription_id` - `azure_tenant_id` |

## cache-service.environment Helm keys

The `cache-service.​environment` block of Helm keys provides
environment variables that, when configured and enabled, inject the values
configured in the Helm chart into the container environment.

Troubleshooting: If the cache service fails due to unsupported or unclear
storageProvider options, you might use these keys to specify an endpoint and
certificates.

The following Helm keys enable you to use external S3-compatible st orage with the
cache service.

Environment variables to set when `CUSTOM_CACERT_ENABLED` is
`true`:

Note: If
`cache-service.environment.CUSTOM_CACERT_ENABLED`: is
`true`, to mount custom certificate files, configure the
`cache-service.extraVolumes:` and
`cache-service.extraVolumeMounts:` Helm keys.

Table 4. `cache-service.environment` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cache-service:   environment:     CERT_STORE_PATH: ``` | `"/cache/truststore.jks"` | Specifies the path to where the trust store is or will be located. You can use any mounted path. |
| ``` cache-service:   environment:     CERT_STORE_TYPE: ``` | `"JKS"` | Specifies the type of trust store. Use the default value, `"JKS"`. |
| ``` cache-service:   environment:     CUSTOM_CACERT_PATH: ``` | `""` | Specifies the path and folder that contains the custom certificate file.  Also, you need to mount the location using `cache-service.extraVolumeMounts`. |
| ``` cache-service:   environment:     AWS_ENDPOINT: ``` | `""` | Specify the URL that points to the S3-compatible storage. |
| ``` cache-service:   environment:     CUSTOM_CACERT_ENABLED: ``` | `false` | - `false` disabes custom CA certificate   processing. Default value. - `true` enables custom CA certificate   processing. |

## cache-service.gcp Helm keys

If the `cache-service.​storageProvider` is `gcp`, then
the keys below need to be set.

Important: For further information on configuring
`cache-service.gcp` Helm keys, see Configure Helm keys to support GCP using GCS within the section Google GCP infrastructure and configuration.

Table 5. `cache-service.gcp` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cache-service:   gcp:     project: ``` | `""` | GCP project name. |
| ``` cache-service:   gcp:     secret: ``` | `""` | GCP credential secret. The key name must be `key.json`. |

## cache-service.livenessProbe Helm keys

Liveness Probe, used with Kubernetes, indicates whether or not a container is
running. The following Helm keys define liveness probe variables for the Cache
Service.

Table 6. `cache-service.livenessProbe` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cache-service:   livenessProbe:     failureThreshold: ``` | `3` |  |
| ``` cache-service:   livenessProbe:     initialDelaySeconds: ``` | `30` |  |
| ``` cache-service:   livenessProbe:     periodSeconds: ``` | `180` |  |
| ``` cache-service:   livenessProbe:     timeoutSeconds: ``` | `60` |  |

## cache-service.minio Helm keys

The following Helm keys define MinIO related variables needed by the Cache
Service.

Important: For further information on configuring
`cache-service.minio` Helm keys, see Configuring Helm keys to support onPrem or non-platform-specific deployments using Redis and Minio within the section Infrastructure and configuration.

Table 7. `cache-service.minio` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cache-service:   minio:     cacert: ``` | `""` | If TLS is enabled, specifies the CA certificate to be used for MinIO communications. |
| ``` cache-service:   minio:     host: ``` | `""` | Specifies the MinIO host. |
| ``` cache-service:   minio:     port: ``` | `9000` | An integer that specifies the MinIO port. Accept the default value. |
| ``` cache-service:   minio:     secret: ``` | `""` | Specifies the MinIO secret that contains the following keys:   - `root-user` - `root-password` |
| ``` cache-service:   minio:     secure: ``` | `true` | Specifies if TLS is enabled for communication with MinIO.   - `true` = enabled - `false` = disabled |
| ``` cache-service:   minio:     verifyHostName: ``` | `true` | Specifies whether or not the host name needs to be verified for MinIO communication if TLS is enabled.   - `true` = verify host name - `false` = do not verify host name |

## cache-service.readinessProbe Helm keys

Readiness Probe, used with Kubernetes, indicates whether or not a container is ready
to accept traffic. The following Helm keys define readiness probe variables for the
Cache Service.

Table 8. `cache-service.readinessProbe` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cache-service:   readinessProbe:     failureThreshold: ``` | `3` |  |
| ``` cache-service:   readinessProbe:     initialDelaySeconds: ``` | `30` |  |
| ``` cache-service:   readinessProbe:     periodSeconds: ``` | `180` |  |
| ``` cache-service:   readinessProbe:     timeoutSeconds: ``` | `60` |  |

## cache-service.redis Helm keys

The following Helm keys define Redis related variables needed by the Cache
Service.

Important: For further information on configuring
`cache-service.redis` Helm keys, see Configuring Helm keys to support onPrem or non-platform-specific deployments using Redis and Minio within the section Infrastructure and configuration.

Table 9. `cache-service.redis` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cache-service:   redis:     authEnabled: ``` |  | Enable Redis authentication.   - `false` disables authentication - `true` enables authentication   If `true`, you must provide the `redis.passwordSecret`. |
| ``` cache-service:   redis:     cacertSecret: ``` | `""` | If TLS is enabled, specifies the secret that contains the CA certificate to be used for Redis communication. This secret must contain the `ca.crt` key.  To create the secret, see Create a Cache Service CA certificate secret for Redis.  For further Redis Helm key information, see Redis keys. |
| ``` cache-service:   redis:     database: ``` | `"1"` | Redis database. |
| ``` cache-service:   redis:     host: ``` | `""` | Redis host. |
| ``` cache-service:   redis:     passwordSecret: ``` | `""` | Redis password. |
| ``` cache-service:   redis:     port: ``` |  | An integer value that specifies the Redis port. |
| ``` cache-service:   redis:     secure: ``` |  | Specifies if TLS is enabled for secure communication with Redis.  - `true` = Enable TLS for secure communication   with Redis. - `false` = Disable TLS. |
| ``` cache-service:   redis:     verifyHostName: ``` |  | Specifies whether or not the host name needs to be verified for Redis communication, if TLS is enabled.  - `true` = If TLS is enabled, verify the host   name for Redis communication. - `false` = Do not verify the host name. |

## cache-service.resources Helm keys

The Kubernetes resource requests and limits.

Table 10. `cache-service.resources` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` cache-service:   resources:     limits:       cpu: ``` | `"0.5"` | Kubernetes Cache Service CPU limit. |
| ``` cache-service:   resources:     limits:       memory: ``` | `"1Gi"` | Kubernetes Cache Service memory limit. |
| ``` cache-service:   resources:     requests:       cpu: ``` | `"0.5"` | Kubernetes Cache Service CPU request. |
| ``` cache-service:   resources:     requests:       memory: ``` | `"1Gi"` | Kubernetes Cache Service memory request. |

## common-infra Helm keys

The following Helm keys set common infrastructure configurations in a Coverity cloud
deployment.

Table 11. `common-infra` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` common-infra:   affinity: ``` | `{}` | Sets the affinity. |
| ``` common-infra:   automountServiceAccountToken: ``` | `false` | This Helm key determines whether or not the service account (SA) token is automatically mounted into the `common-infra` pod.   - `false`: The SA token is not automatically   mounted in the `common-infra` pod. - `true`: The SA token is automatically mounted   in the `common-infra` pod.   Mounting the SA token in a pod provides authentication for the pod and enables the pod to access resources.  See also Configuring pod and container security.  To create the SA token, see Generate a Connect SA admin user token. |
| ``` common-infra:   cleanupSchedule: ``` | `*/5 * * * *` | Defines a cleanup cronjob schedule. This must be a valid schedule for a Kubernetes cronjob. The default value performs a cleanup cronjob every five minutes. |
| ``` common-infra:   containerSecurityContext: ``` | `{}` | Set the container security context.  For details, see Configuring pod and container security. |
| ``` common-infra:   image: ``` | `"common-infra"` | The name of the common infrastructure container image. Do not override this value. |
| ``` common-infra:   nodeSelector: ``` | `{}` | Sets the node selector |
| ``` common-infra:   podSecurityContext: ``` | `{}` | Sets the common infrastructure pod security context. |
| ``` common-infra:   registry: ``` | `""` | The container image registry to use. Use this only if this container is not in the registry specified by the `imageRegistry` Helm key. |
| ``` common-infra:   tolerations: ``` | `[]` | Sets tolerations for common infrastructure. If you are deploying Coverity on ARM64 nodes, and if a global toleration is not used, this toleration must be configured.  For example, to deploy this service on ARM64 nodes only:   ``` common-infra:     tolerations:         - key: "kubernetes.io/arch"           operator: "Equal"           value: "arm64"           effect: "NoSchedule" ```   Note: Refer to:  - Setting up ARM64 support - <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/> |
| ``` common-infra:   version: ``` | `"COMMON_INFRA_​VERSION"` | The image version. Use this only if this container image is not the version specified by the `imageVersion` Helm key. |

## ingress Helm keys

The following Helm keys configure the ingress controller. If TLS sidecar NGINX
reverse proxy is enabled, this will forward to `https/8443`;
otherwise it will forward to `http/8080`.

Important: Do NOT enable TLS sidecar if you are
deploying only Connect (not deploying Scan Service).

Table 12. `ingress` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` ingress:   annotations: ``` | `{}` | Additional annotations to provide to the ingress object.  You can use the following annotation syntax to specify the maximum file size to allow through the ingress port: `nginx.ingress.kubernetes.io/proxy-body-size: <fileSize>` See also Set NGINX proxy-body-size for Coverity toolkit tar file upload to Connect. |
| ``` ingress:   class: ``` | `""` | The default ingress controller is NGINX, therefore the default value points to the `kubernetes.io/ingress.class` annotation key. If you use a different ingress controller, update the value in this field. |
| ``` ingress:   enabled: ``` | `false` | Set to `true` to create a Kubernetes ingress object. |
| ``` ingress:   hosts: ``` | `[]` | Array of allowed host names. |
| ``` ingress:   path: ``` | `""` | The ingress rule path.   - You might need to set this to `"/*"` for   AWS ALB ingress controllers. - You might need to set this to `"/*"` for   GCE ingress controllers. - You might need to add a path if you are using a context   path. |
| ``` ingress:   tls: ``` | `[]` | Array of object with schema to select the TLS secret for https:   ``` ingress:   tls:     - secretName: ""       hosts: [] ``` |

## postgres Helm keys - configure Scan Service and Storage Service access to a PostgreSQL database

The following `​​postgres` keys create jobs that that enable the Scan
Service and Storage Service to access a PostgreSQL database created for use by the
Scan and Storage services. This database can be separate from the Connect PostgreSQL
database. These keys can be used by both the Scan Service and the Storage Service,
or they can be overridden as needed by either service.

The `postgres` Helm keys below can be overridden by either the
`scan-service.postgres` keys or
`storage-service.postgres` keys. Overrides are effective for only
the service that contains the overrides. See:

- Scan Service (`scan-service.postgres`) See scan-service.postgres Helm keys - configure access to a Scan Service PostgreSQL database.
- Storage Service (`storage-service.postgres`) See storage-service.postgres Helm keys - configure access to a Storage Service PostgreSQL database.

Table 13. `postgres` Helm keys

| Key | Default Value | Description |
| --- | --- | --- |
| ``` postgres:   database: ``` | `"postgres"` | The name of the database in which to run `create db` statements. The database must already exist and cannot be created by this job. |
| ``` postgres:   existingSecret: ``` | `""` | This Helm key enables you to specify an existing Kubernetes PostgreSQL secret name to be used for all services unless overridden by specific services. The secret must contain the following values:   - `host` - `port` - `username` - `password` |
| ``` postgres:   host: ``` | `""` | Specifies the PostgreSQL host. For example, "cim".  Use this key if you have not created a secret. |
| ``` postgres:   jobSidecars: ``` | [] | You can use this Helm key to specify sidecar containers to add within pods that require a PostgreSQL database connection. This sidecar is a native sidecar, which is an init container with `restartPolicy:Always`; you must set `restartPolicy:Always`.  Native sidecar containers require Kubernetes 1.28 or later.  For example:   ``` postgres:   jobSidecars:     - name: cloud-sql-proxy       image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.1.0-buster       restartPolicy: Always       command: ["/bin/sh","-ec"]       args: ["/cloud-sql-proxy                --structured-logs                --port=5432 <gcp-project>:<region>:testgcp-zirw98                --credentials-file=/secrets/key.json                --max-sigterm-delay=100s "]       securityContext:         runAsUser: 5000       volumeMounts:         - name: gcp-sa-secret           mountPath: /secrets/           readOnly: true       resources:         requests:           memory: "500Mi"           cpu: "500m" ```   For further information on using this and related Helm keys, refer to Attaching a Cloud SQL proxy native sidecar container in GCP.  See also: <https://kubernetes.io/blog/2023/08/25/native-sidecar-containers/>. |
| ``` postgres:   password: ``` | `""` | Specifies the password to connect to the PostgreSQL host for a Connect instance.  Use this key if you have not created a secret. |
| ``` postgres:   port: ``` |  | Use port 5432 for all instances of PostgreSQL.  Use this key if you have not created a secret. |
| ``` postgres:   sidecars: ``` | [] | The sidecar container specification to attach for pods that require a database connection. The sidecar is added as a native sidecar, which is an init container with `restartPolicy:Always`; you must set`restartPolicy:Always`. You must have Kubernetes 1.28 or later to support native-sidecar.  For further information on using this and related Helm keys, refer to Attaching a Cloud SQL proxy native sidecar container in GCP.  See also: <https://kubernetes.io/blog/2023/08/25/native-sidecar-containers/>. |
| ``` postgres:   sslmode: ``` | `""` | The PostgreSQL SSL mode must be one of the following values:   - `"disable"` - `"allow"` - `"prefer"` - `"require"` - `"verify-ca"` - `"verify-full"`   The default value is `"verify-ca"`.  For further information, see Select the PostgreSQL sslmode and find the PostgreSQL root certificate for TLS.  For value definitions, see Table 1. |
| ``` postgres:   user: ``` | "" | The username to connect to the PostgreSQL host.  Use this key if you have not created a secret. |

## proxy Helm keys

The following Helm keys define TLS forward proxy values that apply to the
`scan-services` subchart. The following proxy parameters
configure forward proxy, which acts as a Man-In-The-Middle. The keys within this
group can be used to override global key values for this
`scan-services` subchart.

See also:

- To configure TLS forward proxy, see Configuring TLS forward proxy
- To define global TLS forward proxy keys, see cnc_global_chart_values.html#cnc_global_chart_values__section_uwy_ftp_jdc

Table 14. `proxy` Helm keys

| Key | Default Value | Description |
| --- | --- | --- |
| ``` proxy:   enabled: ``` | `false` | This boolean Helm key enables or disables TLS forward proxy for Connect services.   - `true` - Enables TLS forward proxy. - `false` - Disables TLS forward proxy. |
| ``` proxy:   host: ``` | `""` | This string Helm key specifies the proxy host server. |
| ``` proxy:   port: ``` | 3128 | Specifies the proxy port that the host server listens on. |
| ``` proxy:   tlsmode: ``` | `"tls"` | The TLS proxy mode must be one of the following values:   - `"insecure"` = Specifies TLS insecure proxy.   This mode enables you to communicate over http instead of   https.. This is an insecure mode. - `"tls"` = specifies TLS proxy, where the   client authenticates the server. - `"mtls"` = specifies mutual TLS mode, where   the client and server authenticate each other.   The default value is `"tls"`.  When TLS mode is set to either tls or mtls, the proxy server CA certificate must be included in the trust-stores ConfigMap with key name `"proxy-server.pem"`.  The file names of other server CA certificates (excluding postgres, proxy server) are not important.  For example: The Black Duck artifactory server CA certificate can be named `artifactory.pem` in the trust-stores ConfigMap. |
| ``` proxy:   existingSecret: ``` | `""` | If proxy is enabled with `tlsmode` set to `"mtls",` this secret must be contain the following keys: `"client-cert"` and `"client-key"`.  If proxy is enabled with `tlsmode` set to `"insecure"` or `"tls"`, an `existingSecret` is not needed. |

## scan-service Helm keys

The `scan-service` Helm keys create a cloud deployment which manages
scans: scheduling, failures, resources, retries.

Table 15. `scan-service` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   ​affinity: ``` | `{}` | Sets the affinity. |
| ``` scan-service:   annotations: ``` | `{}` | Additional annotations to add to the deployment metadata. This is a dictionary. |
| ``` scan-service:   automountServiceAccountToken: ``` | `false` | This Helm key determines whether or not the service account (SA) token is automatically mounted into the `scan-service` pod.   - `false`: The SA token is not automatically   mounted in the `scan-service` pod. - `true`: The SA token is automatically mounted   in the `scan-service` pod.   Mounting the SA token in a pod provides authentication for the pod and enables the pod to access resources.  See also Configuring pod and container security.  To create the SA token, see Generate a Connect SA admin user token. |
| ``` scan-service:   containerSecurityContext: ``` | `{}` | Set the container security context.  For details, see Configuring pod and container security. |
| ``` scan-service:   extraVolumes: ``` | `[]` | This Helm key specifies additional volumes to add to the Scan Service pod. For example:   ``` scan-service:   extraVolumes:     - name: scan-service-secret       secret:         secretName: scansvc-secret ``` |
| ``` scan-service:   extraVolumeMounts: ``` | `[]` | This Helm key specifies additional Scan Service volumes to mount to the Scan Service pod.  For example:   ``` scan-service:   extraVolumeMounts:     - name: scan-service-secret       secret:         secretName: scansvc-secret ```   For further information, see:   - for generic custom storage, see Storage service custom domains. - for Dell ECS S3 storage, see Configure Dell ECS storage support. |
| ``` scan-service:   image: ``` | `"scan-service"` | The name of the Scan Service container image. Do not override this value. |
| ``` scan-service:   ​initContainers: ``` | `[]` | This Helm key specifies init containers to inject into the Scan Service pod.  You might specify init containers when attaching a Cloud SQL proxy native sidecar container in GCP. See:   - Attaching a Cloud SQL proxy native sidecar container in GCP - <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/>   For example:   ``` scan-service:   initContainers:     - name: init-container       image: busybox       command: ["sh", "-c", "echo 'Init container is running';                  sleep 10; echo 'Init container completed'"] ``` |
| ``` scan-service:   ​licenseSecretName: ``` | `""` | The name of a secret, in the same namespace, containing a valid and active Coverity Analysis license. This license is used only by Scan Services.   - The secret key must be named   `license.dat`. |
| ``` scan-service:   ​logLevel: ``` | `"INFO"` | Specifies the minimum logging level used to generate logs. Valid values include:   - ALL - TRACE - INFO This is the default value. INFO presents all log   levels from informational through the highest level. - WARN - ERROR - FATAL - OFF Not recommended. Disables logging.   Note: The log levels can be all uppercase or all lowercase, and can be encased in double-quotes for string value.  See also Specifying logging levels. |
| ``` scan-service:   ​nodeSelector: ``` | `{}` | Sets the node selector. |
| ``` scan-service:   podAnnotations​: ``` | `{}` | Additional annotations to add to the pod metadata. This is a dictionary. |
| ``` scan-service:   ​podSecurityContext: ``` | `{}` | Sets the Scan Service pod security context. |
| ``` scan-service:   ​registry: ``` | `""` | The container image registry to use. Use this only if this container is not in the registry specified by the `imageRegistry` Helm key. |
| ``` scan-service:   ​tolerations: ``` | `[]` | Sets tolerations for scan service. If you are deploying Coverity on ARM64 nodes, and if a global toleration is not used, this toleration must be configured.  For example, to deploy scan service on ARM64 nodes only:   ``` scan-service:   tolerations:     - key: "kubernetes.io/arch"       operator: "Equal"       value: "arm64"       effect: "NoSchedule" ```   Note: Refer to:  - Setting up ARM64 support - <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/> |
| ``` scan-service:   ​version: ``` | `"SCAN_SERVICE_​VERSION"` | The image version. Use this only if this container image is not the version specified by the `imageVersion` Helm key. |

## scan-service.api Helm keys

This key sets the
pagination limit for the scan API. The default value Defaults is 500.

Table 16. `scan-service.api.pagination` Helm key

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   ​api:     pagination:       limi: ``` | 500 | Set the pagination limit for the scan API. |

## scan-service.cleanupJob Helm keys

Table 17. `scan-service.cleanupJob` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   cleanupJob​:     resources:       limits:         cpu: ``` | "100m" |  |
| ``` scan-service:   cleanupJob​:     resources:       limits:         memory: ``` | "128Mi" |  |
| ``` scan-service:   cleanupJob​:     resources:       requests:         cpu: ``` | "100m" |  |
| ``` scan-service:   cleanupJob​:     resources:       requests:         memory: ``` | "128Mi" |  |

## scan-service.dispatcher Helm keys

The dispatcher is third-party software that schedules analysis jobs for
Kubernetes.

Table 18. `scan-service.dispatcher` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   ​dispatcher:     ​imagePullPolicy: ``` | `"IfNotPresent"` |  |
| ``` scan-service:   ​dispatcher:     ​interval: ``` | `5` |  |
| ``` scan-service:   ​dispatcher:     ​schedulerName: ``` | `"default-scheduler"` | Sets the scheduler for Kubernetes to use for analysis jobs. |

## scan-service.environment Helm keys

The `scan-service.environment` Helm keys define the node pool in which
to run scan jobs.

Define the values for these keys when you plan and create a scan jobs node pool. Also
refer to the following sections:

- For information on planning, sizing, and creating scan job node pools, and
  for information deploying and scheduling scan jobs on one or more nodes,
  refer to Creating scan job node pools and scheduling scan jobs.

Table 19. `scan-service.environment` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   ​environment:     ​COVANALYSIS_​DEFAULTPOOLTYPE: ``` | `"small"` | You can create one of each of the following types of node pools. Specify the type of node pool:   - `"small"` (default value) - `"medium"` - `"large"` - `"extra large`" - `"custom"`: Enter the value that you assign   when you create the custom node pool. The value that you   enter here and in the `CUSTOMNODEPOOL_LABEL`   key must be exactly the same value.   If you specify a custom node pool, you must also set the following keys defined below:   - `CUSTOMNODEPOOL_CPU` - `CUSTOMNODEPOOL_LABEL` - `CUSTOMNODEPOOL_MEM` |
| ``` scan-service:   ​environment:     ​CUSTOMNODEPOOL_CPU: ``` | `0` | Specify the number of vCPUs in *thousandth of a core* that support the custom node pool. For example, 5000 (*thousandth of a core*) = 5 core vCPUs. |
| ``` scan-service:   ​environment:     ​CUSTOMNODEPOOL_LABEL: ``` | `""` | Specify a name (label) for the custom node pool. Enter the value that you assign when you create the custom node pool. This value must be exactly the same as the `COVANALYSIS__​DEFAULTPOOLTYPE` value. |
| ``` scan-service:   ​environment:     ​CUSTOMNODEPOOL_MEM: ``` | `0` | Specify the amount of memory in megabytes available for the custom node pool. For example, `scan-service.​environment.​CUSTOMNODEPOOL_MEM 15000` = 15 GB RAM. |
| ``` scan-service:   ​environment:     ​​EXTRALARGENODEPOOL_ENABLE: ``` | `false` | An extra large node pool contains:   - 58500 (*thousandth of a core*) = 58.5 core vCPUs. - 222000 MB (222 GB) memory  - `true` = Create an extra large node   pool. - `false` = Do not create an extra large node   pool. |
| ``` scan-service:   ​environment:     ​LARGENODEPOOL_ENABLE: ``` | `false` | A large node pool contains:   - 28500 (*thousandth of a core*) = 28.5 core vCPUs. - 108000 MB (108 GB) memory  - `true` = Create a large node pool. - `false` = Do not create a large node   pool. |
| ``` scan-service:   ​environment:     ​MAXNODEPOOLSIZE​: ``` | `50` | Specify the maximum number of nodes allowed in the node pool. |
| ``` scan-service:   ​environment:     ​MEDIUMNODEPOOL_ENABLE: ``` | `false` | A medium node pool contains:   - 14500 (*thousandth of a core*) = 14.5 core vCPUs. - 56000 MB (56 GB) memory  - `true` = Create a medium node pool. - `false` = Do not create a medium node   pool. |
| ``` scan-service:   ​environment:     SMALLNODEPOOL_ENABLE​: ``` | `true` | A small node pool contains:   - 6500 (*thousandth of a core*) = 6.5 core vCPUs. - 26000 MB (26 GB) memory  - `true` = Create a small node pool. - `false` = Do not create a small node   pool. |
| ``` scan-service:   ​environment:     ​MULTIPLEJOBSPERNODE_ENABLE: ``` | `false` | This Helm key enables either of the following methods of scheduling scan (analysis) jobs on node(s):   - `false` = Schedule each scan job on its own   node. - `true` = Schedule multiple scan jobs   concurrently on a single node.   See also Creating scan job node pools and scheduling scan jobs |
| ``` scan-service:   ​environment:     ​TLS_CUSTOM_ENABLED: ``` | `false` | - `false` Disable custom TLS. - `true` Enable custom TLS. If enabled, you   need to create a custom TLS certificate and configure the   path to the certificate (see   `scan-service.​environment.​TLS_CUSTOM_CERT_PATH`).   For further information, see:   - for generic custom storage, see Storage service custom domains. - for Dell ECS S3 storage, see Configure Dell ECS storage support. - for the Helm keys, see scan-service Helm keys in the chapter: scan-services Helm subchart: Helm keys. |
| ``` scan-service:   ​environment:     ​TLS_CUSTOM_CERT_PATH: ``` | `""` | Path where the custom TLS certificate file is stored. You need to configure this key if custom TLS is enabled (see `scan-service.​environment.​TLS_CUSTOM_ENABLED`).  For further information, see:   - for generic custom storage, see Storage service custom domains. - for Dell ECS S3 storage, see Configure Dell ECS storage support. - for the Helm keys, see scan-service Helm keys in the chart chapter scan-services Helm subchart: Helm keys. |

## scan-service.jobRunner Helm keys

The Scan Service job runner runs the appropriate version of the Thin Client analysis
job and manages uploading of artifacts to the storage bucket. The following
jobRunner Helm keys:

- specify the container image, and
- specify whether or not analysis artifacts are uploaded to the storage
  bucket.

Table 20. `scan-service.jobRunner` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   ​jobRunner:     ​image: ``` | `"job-runner"` | The image to use. |
| ``` scan-service:   ​jobRunner:     registry​: ``` | `""` | The image registry to use. You can specify your own private Docker registry here for the jobRunner container image. |
| ``` scan-service:   ​jobRunner:     ​version: ``` | `"RUNNER_VERSION"` | The image version to use. |
| ``` scan-service:   ​jobRunner:     ​uploadArtifacts: ``` | `All` | Use this key to specify whether or not analysis artifacts are uploaded to the storage bucket.  Within the Kubernetes cluster, a job runner performs the analysis and generates all of the following artifacts:   - analyzed-idir.zip - Contains both the analysis output and   the analyzed idir. - analysis-output.zip - Contains the analysis output. - execLog.zip - Contains the execution logs.   You can choose when and which artifacts are uploaded to the storage bucket. The artifact upload options are:   - `All` - Default value. Upload all scan   artifacts (`analyzed-idir.zip`,   `analysis-output.zip`, and   `execLog.zip`) to the storage bucket, in   both success and failure scenarios. - `OnFailure` - If a scan completes   without failure, do NOT upload any artifacts to the storage   bucket. If a scan failure occurs, upload the artifacts   `analyzed-idir.zip` and   `execLog.zip` to the storage bucket. - `LogsOnly` - Upload the execution   logs, `execLog.zip`, and analysis output,   `analysis-output.zip`, to the storage   service storage (bucket, blob) in both success and failure   scenarios. - `None` - Upload nothing to the storage   bucket. This option saves time, However, it does not provide   any information to help troubleshoot a potential scan   issue.   See also Managing artifact upload to storage. |

## scan-service.livenessProbe Helm keys

Liveness Probe, used with Kubernetes, indicates whether or not a container is
running. The following Helm keys define liveness probe variables for the Scan
Service.

Table 21. `scan-service.livenessProbe` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   ​livenessProbe:     failureThreshold​: ``` | `3` |  |
| ``` scan-service:   ​livenessProbe:     ​initialDelaySeconds: ``` | `30` |  |
| ``` scan-service:   ​livenessProbe:     ​periodSeconds: ``` | `180` |  |
| ``` scan-service:   ​livenessProbe:     ​timeoutSeconds: ``` | `60` |  |

## scan-service.migrateJob Helm keys

The following Helm keys control a job which either creates a scan database schema if
none exists or upgrades the scan database schema to the latest. This operation is
idempotent and can be safely run many times, even if not necessary.

Table 22. `scan-service.migrateJob` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   migrateJob:     ​containerSecurityContext: ``` | `{}` | Set the container security context.  For details, see Configuring pod and container security. |
| ``` scan-service:   ​migrateJob:     enabled​: ``` | `true` | - `true` = Update the scan database   schema. - `false` = Do not update the scan database   schema. |
| ``` scan-service:   migrateJob:     ​extraVolumeMounts: ``` | `[]` | Specify additional storage volumes to mount to the scan service migration job pod. |
| ``` scan-service:   ​migrateJob:     extraVolumes​: ``` | [] | Specify additional storage volumes created for the scan service migration job pod. For example:   ``` scan-service:   migrateJob:     extraVolumes:     - name: <storage-volume-name>       secret:         secretName: <storage-volume-secret-name> ```   You need to create a secret and provide the name of the secret to access the extra storage volume.  You need to mount the storage volume to the scan service migration job pod using `scan-service:.migrateJob.extraVolumeMounts:`. |
| ``` scan-service:   ​migrateJob:     ​image: ``` | `"scan-service-migration"` | The name of the Scan Service migration job container image. Do not override this value. |
| ``` scan-service:   ​migrateJob:     ​initContainers: ``` | [] | This Helm key specifies init containers to inject into the Scan Service migrate job pod.  You might specify init containers when attaching a Cloud SQL proxy native sidecar container in GCP. See:   - Attaching a Cloud SQL proxy native sidecar container in GCP - <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/> |
| ``` scan-service:   ​migrateJob:     ​registry: ``` | `""` | The container image registry to use. Use this only if this container is not in the registry specified by the `imageRegistry` Helm key. Refer to Root Helm keys. |
| ``` scan-service:   ​migrateJob:     ​version: ``` | `"SCAN_SERVICE_VERSION"` | The image version. Use this only if this container image is not the version specified by the `imageVersion` Helm key. Refer to Root Helm keys. |

## scan-service.migrateJob.resources Helm keys

The following Helm keys configure Kubernetes resource limits.

Table 23. `scan-service.migrateJob.resources.limits` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   ​migrateJob:     resources:       limits:         cpu​: ``` | `"500m"` |  |
| ``` scan-service:   ​migrateJob:     ​resources:       limits:         memory: ``` | `"1Gi"` |  |

The following Helm keys configure Kubernetes resource requests.

Table 24. `scan-service.migrateJob.resources.requests` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   ​migrateJob:     ​resources.:       requests:         cpu: ``` | `"250m"` |  |
| ``` scan-service:   ​migrateJob:     ​resources:       requests:         memory: ``` | `"256Mi"` |  |

## scan-service.observability Helm keys

The following Helm keys set up Scan Service metrics data observability.

Table 25. scan-service.observability Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   ​observability:     ​exposeMetrics: ``` | `true` | If `true`, exposes time series metrics in Prometheus format.  - `true` = Expose Scan Service time series   metrics in Prometheus format. - `false` = Do not expose Scan Service time   series metrics. |
| ``` scan-service:   ​observability:     ​jaegerURL: ``` | `""` | Specifies a Jaeger instance to push distributed tracing data to. Either   - Enter a Jaeger instance. - To disable, set value to `""` (empty). This   will use a no-op tracer. |

## scan-service.postgres Helm keys - configure access to a Scan Service PostgreSQL database

If you created a PostgreSQL database instance for use by the Scan Service, you need
to configure these `scan-service.postgres` Helm keys to create jobs
that that enable the Scan Service to access its' own PostgreSQL database, for
example, a database named "scan".

If needed, for Scan Service you can override PostgreSQL Helm keys using the
`scan-service.postgres` keys identified in this section. The
`scan-service.postgres` Helm keys below are Scan Service-specific
keys that override parameters configured in the `postgres` Helm keys
within the `scan-services` chart, and
`global.postgres` Helm keys.

Note:

For `scan-service.postgres` info in the Helm chart chapter, see
Configuring postgres Helm keys for Scan Service and Storage Service databases.

For information on `postgres` Helm keys within the
`scan-services` chart, see postgres Helm keys - configure Scan Service and Storage Service access to a PostgreSQL database.

For information on `global.postgres` Helm keys, see Global Helm keys.

For information on precedence, see About the cnc chart and scan-services subchart.

Table 26. `scan-service.postgres` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   ​postgres:     ​createDatabase: ``` | `true` | - `true` enables the creation of a scan service   job that provides scan service access to the Connect   PostgreSQL database. This is the default value. - `false` denies scan service access to the   Connect PostgreSQL database   The PostgreSQL database resources must already exist; they cannot be created by this job. |
| ``` scan-service:   ​postgres:     ​database: ``` | `"scan"` | The name of the PostgreSQL database that is created specifically for the Scan Service. For example, `"scan"`.  If configured, this value overrides the `postgres.​database` Helm key for only the Scan Service PostgreSQL database. The `postgres.​database` key has a default value `"postgres"`. |
| ``` scan-service:   ​postgres:     ​existingSecret: ``` | `""` | This Helm key enables you to specify an existing Kubernetes PostgreSQL secret name specifically for Scan Service that contains the keys:   - `host` - `port` - `username` - `password` |
| ``` scan-service:   ​postgres:     ​host: ``` | `""` | The PostgreSQL host path and username.  Use this key if you have not created a secret. |
| ``` scan-service:   ​postgres:     ​password: ``` | `""` | Specify the password for PostgreSQL access.  Use this key if you have not created a secret.  See also `scan-service.postgres.user` to provide the username. |
| ``` scan-service:   ​postgres:     port​: ``` |  | - If `scan-service.postgres.port` has no value   (default), Scan Service uses the PostgreSQL port defined in   the `postgres.port` key (default =   5432). - If a port value is set in   `scan-service.postgres.port` that value   overrides the value in `postgres.port` for   Scan Service.   Use this key if you have not created a secret. |
| ``` scan-service:   ​postgres:     ​sslmode: ``` | `""` | The PostgreSQL SSL mode for Scan Service can be overridden using one of the following values:   - `""` (no override) - `"disable"` - `"allow"` - `"prefer"` - `"require"` - `"verify-ca"` - `"verify-full"`   The default value is `""` which inherits the value set in the `postgres.sslmode` key. For the current SSL value, refer to the `postgres.sslmode` key and any overrides.  For value definitions, see Table 1. |
| ``` scan-service:   ​postgres:     ​user: ``` | `""` | Specify a username for PostgreSQL access. See also `scan-service.postgres.password` to provide the password.  Use this key if you have not created a secret. |

## scan-service.resources Helm keys

The following Helm keys set Kubernetes resource limits for Coverity Scan Service.

Table 27. `scan-service.resources.limits` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   ​resources:     ​limits:       cpu: ``` | `"250m"` |  |
| ``` scan-service:   ​resources:     ​limits:       memory: ``` | `"512Mi"` |  |

The following Helm keys set Kubernetes resource requests for Coverity Scan
Service.

Table 28. `scan-service.resources.requests` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   ​resources:     ​requests:       cpu: ``` | `"100m"` |  |
| ``` scan-service:   ​resources:     ​requests:       memory: ``` | `"128Mi"` |  |

## scan-service.retention Helm keys

The following Helm keys enable and set the retention period on the Scan Service
storage.

Table 29. `scan-service.retention` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   ​retention:     ​enabled: ``` | `true` | This controls whether or not scans and indirectly storage objects are deleted, where:  - `true` = enabled - `false` = disabled |
| ``` scan-service:   ​retention:     ​minutes: ``` | `"43200"` | Scan Service storage retention period enables you to control how long scan artifacts are kept in the Scan Service storage. The default value is `43200` minutes = 30 days. The minimum retention period is 3 days (4320 minutes). This value can be any positive integer, however Black Duck recommends 30 days and the minimum is 3 days. |

## scan-service.tools.sync Helm keys

The following `scan-service.tools.sync` Helm keys enable and configure
the scan tool synchronization.

Note: This feature works only with the Black Duck private docker registry; it does not work with
your own private registry.

Enable synchronization using the `scan-service.tools.sync.enabled:
true` Helm key and provide the scan tool synchronization secret name in
the `scan-service.tools.sync.existingSecret: ””` Helm key.

Refer to:

- For the secret: Create a scan tool synchronization secret
- For the Helm keys: Set Helm keys to enable scan tool synchronization

Table 30. `scan-service.tools.sync` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` scan-service:   ​tools:     ​sync:       enabled: ``` | `false` | - `false` disables automatic downloads. - `true` enables automatic downloads.   Set to `true` to automatically download tools from the Black Duck registry. |
| ``` scan-service:   ​tools:     ​sync:       existingSecret: ``` | `""` | The name of the secret that contains the `username` and `password` keys needed for Black Duck private Docker registry authentication for scan tool synchronization.  Refer to:   - For secret: Create a scan tool synchronization secret - For Helm key: Set Helm keys to enable scan tool synchronization   The scan tool synchronization secret must be created and this Helm key must be configured with the name of the secret for scan tool synchronization to work. |

## srm Helm keys

Do not use the following `srm` Helm keys for Coverity cloud
deployment.

Table 31. `srm` Helm key

| Key | Default value | Description |
| --- | --- | --- |
| ``` srm:   ​url: ``` | `""` | This is a Software Risk Manager (SRM) configuration. Specifies the in-cluster URL of the SRM server. Do NOT use for Coverity cloud deployment (`cnc`). |
| ``` srm:   ​codesight:     url: ``` | `""` | URL of the codesight server. This is a Software Risk Manager (SRM) configuration. Do NOT use for Coverity cloud deployment (`cnc`). |

## storage-service Helm keys

The following Helm keys create a Kubernetes deployment which manages the storage of
uploaded installation directories, and provides the Coverity cloud components access
to the directories for analysis jobs.

Table 32. `storage-service` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   ​affinity: ``` | `{}` | Sets the affinity. |
| ``` storage-service:   ​annotations: ``` | `{}` | Additional annotations to add to the deployment metadata. This is a dictionary. |
| ``` storage-service:   ​automountServiceAccountToken: ``` | `false` | This Helm key determines whether or not the service account (SA) token is automatically mounted into the `storage-service` pod.   - `false`: The SA token is not automatically   mounted in the `storage-service` pod. - `true`: The SA token is automatically mounted   in the `storage-service` pod.   Mounting the SA token in a pod provides authentication for the pod and enables the pod to access resources.  See also Configuring pod and container security.  To create the SA token, see Generate a Connect SA admin user token. |
| ``` storage-service:   ​containerSecurityContext: ``` | `{}` | Set the container security context.  For details, see Configuring pod and container security. |
| ``` storage-service:   ​environment: ``` | `{}` | Additional environment variables injected into the container environment. |
| ``` storage-service:   ​extraVolumeMounts: ``` | `[]` | Specify additional storage service volumes to mount to the storage service pod. |
| ``` storage-service:   ​extraVolumes: ``` | `[]` | Specify additional volumes created for the storage service pod. For example:   ``` storage-service:   extraVolumes:     - name: <storage-volume-name>       secret:         secretName: <storage-volume-secret-name> ```   You need to create a secret and provide the name of the secret to access the extra storage volume. |
| ``` storage-service:   ​fileUploadSizeLimitBytes: ``` | `"10737418240"` | Specify the maximum file size allowed to upload to the intermediate directory (IDIR). The default is 10 GB. |
| ``` storage-service:   ​image: ``` | `"storage-service"` | The name of the Storage Service container image. Do not override this value. |
| ``` storage-service:   initContainers​: ``` | `[]` | This Helm key specifies init containers to inject into the Storage Service pod.  See:   - <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/> |
| ``` storage-service:   ​logLevel: ``` | `"INFO"` | Specifies the minimum logging level used to generate logs. Valid values include:   - ALL - TRACE - INFO This is the default value. INFO presents all log levels   from informational through the highest level. - WARN - ERROR - FATAL - OFF Not recommended. Disables logging.   Note: The log levels can be all uppercase or all lowercase, and can be encased in double-quotes for string value.  See also Specifying logging levels. |
| ``` storage-service:   ​nodeSelector: ``` | `{}` | Sets the node selector. |
| ``` storage-service:   podAnnotations​: ``` | `{}` | Additional annotations to add to the pod metadata. This is a dictionary. |
| ``` storage-service:   ​podSecurityContext: ``` | `{}` | Sets the Storage Service pod security context. |
| ``` storage-service:   ​registry: ``` | `""` | The container image registry to use. Use this only if this container is not in the registry specified by the `imageRegistry` Helm key. |
| ``` storage-service:   ​storageType: ``` | `""` | The name of the backing storage type. This must be one of: `"s3"`, `"s3Express"`, `"gcs"`, `"azure"`, or `"minio"`. |
| ``` storage-service:   ​tolerations: ``` | `[]` | Sets tolerations for storage service. If you are deploying Coverity on ARM64 nodes, and if a global toleration is not used, this toleration must be configured.  For example, to deploy storage service on ARM64 nodes only:   ``` storage-service:   tolerations:     - key: "kubernetes.io/arch"       operator: "Equal"       value: "arm64"       effect: "NoSchedule" ```   Note: Refer to:  - Setting up ARM64 support - <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/> |
| ``` storage-service:   ​version: ``` | `"STORAGE_SERVICE_​VERSION"` | The image version. Use this only if this container image is not the version specified by the `imageVersion` Helm key. |

## storage-service.azure Helm keys

For a deployment on Microsoft Azure, the following Helm keys to specify and enable
Azure Entra ID (formerly known as Azure Active Directory, Azure AD, or AAD) in the
Coverity cloud deployment to enable access to Azure storage blob. For information on
creating secrets and configuring related Helm keys, see also: .

- Configure Storage Service access to the storage blob

Note: Use these keys for Storage Service on Azure only.

Important: For further information on configuring
`storage-service.azure` Helm keys, see Configure Helm keys to support Azure using Azure blob within the section Microsoft Azure infrastructure and configuration.

Important: Azure Entra ID is formerly known as Azure
Active Directory, Azure AD or AAD.

Table 33. `storage-service.azure` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   azure:     ​​authMode: ``` | `"sharedKey"` | Specify one of the following Azure authentication modes as needed:  Important: Even though it is the default authentication mode, we do not recommend using a shared key secret for storage blob access. We recommend that you use an Azure Entra ID client secret because it is much more secure.   - `sharedKey` (default, not recommended):   Uses the `azure_account_key` from the   Kubernetes secret for authentication. - `aadClientSecret` (recommended, more   secure): Uses Azure Entra ID (formerly known as Azure   Active Directory, Azure AD, or AAD) credentials that are   created and stored within an Azure Entra ID client   secret. The secret must contain:    - azure_endpoint   - azure_tenant_id   - azure_client_id   - azure_client_secret |
| ``` storage-service:   ​​azure;     container: ``` | `""` | Specify the name of the Azure blob storage container to use. This is required if you are using Azure storage. |
| ``` storage-service:   ​​azure:     secret:       name: ``` | `""` | Specify the name of the Kubernetes secret that contains either the Azure account key for SharedKey, or a set of keys for Azure Entra ID (formerly known as Azure Active Directory, Azure AD, or AAD) credentials for Azure Entra ID.  The Kubernetes secret must include the required keys based on the selected authentication mode:   - For Shared Key, `sharedKey` authentication   must contain:    - The `azure_account_key` for     authentication. - For Azure Entra ID, `aadClientSecret`   authentication must include the following keys:    - `azure_endpoint` The endpoint URL     This can be either:     - a storage service storage account blob URL.       For example:       `https://mystorageaccount.blob.core.windows.net`.     - a custom domain as the endpoint when providing       the secret name. For example:       `https://<customDomain>` Important: If you are       using a custom domain, see also Storage service custom domains.   - `azure_tenant_id` - The Azure Active     Directory tenant ID.   - `azure_client_id` - The client ID     for the Azure application.   - `azure_client_secret` - The client     secret for the Azure application. To find (view) your storage account access key, see [Manage storage   account access keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json&tabs=azure-portal). |
| ``` storage-service:   ​​azure:     storageAccountName: ``` | `""` | Specify the Storage Account name. You must provide this for both authentication types: `sharedKey` or `aadClientSecret`. |

## storage-service.endpoint Helm keys

The `storage-service.endpoint` Helm keys provide information used by
clients to access backing storage.

The following Helm keys provide information for clients outside the cluster.

Table 34. `storage-service.endpoint.external` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   ​​endpoint:     external:       proxyPath: ``` | `""` | This is needed when the bucket is behind a load balancer or proxy. |
| ``` storage-service:   ​​endpoint:     external:       url: ``` | `""` | The URL of the backing storage. |

The following Helm key provides information for clients inside the cluster.

Table 35. `storage-service.endpoint.internal` Helm key

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   ​​endpoint:     internal:       url: ``` | `""` | The URL of the backing storage. |

## storage-service.gcs Helm keys

The following Helm key provides credentials used to access storage when on GCP.

Important: For further information on configuring
`storage-service.gcs` Helm keys, see Configure Helm keys to support GCP using GCS within the section Google GCP infrastructure and configuration.

Note: This key is required for Google GCP. Do not use it for other
cloud provider platforms.

Table 36. `storage-service.gcs` Helm key

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   ​​gcs:     bucket: ``` | `""` | The GCS bucket name. |

The following Helm keys provide information for the secret that contains the Google
GCP service account.

Table 37. `storage-service.gcs.secret` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   ​​gcs:     secret:       key: ``` | `""` | The key inside the secret. |
| ``` storage-service:   ​​gcs:     secret:       name: ``` | `""` | The name of the secret. |

## storage-service.livenessProbe Helm keys

Liveness Probe, used with Kubernetes, indicates whether or not a container is
running. The following Helm keys define liveness probe variables for the Scan
Service.

Table 38. `storage-service.livenessProbe` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   ​​livenessProbe:     failureThreshold: ``` | `3` |  |
| ``` storage-service:   ​​livenessProbe:     initialDelaySeconds: ``` | `30` |  |
| ``` storage-service:   ​​livenessProbe:     periodSeconds: ``` | `180` |  |
| ``` storage-service:   ​​livenessProbe:     timeoutSeconds: ``` | `60` |  |

## storage-service.migrateJob Helm keys

The following Helm keys control a job which either creates a storage database schema
if none exists or upgrades the scan database schema to the latest. This operation is
idempotent and can be safely run many times, even if not necessary.

The following Helm keys control a job which upgrades the storage database schema to
the latest version.

Table 39. `storage-service.migrateJob` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   migrateJob:     ​containerSecurityContext: ``` | `{}` | Set the container security context.  For details, see Configuring pod and container security. |
| ``` storage-service:   ​​migrateJob:     enabled: ``` | `true` | If `true`, update the storage database schema. Otherwise, do not update the storage database schema.  - `true` = Update the storage database   schema. - `false` = Do not update the storage database   schema. |
| ``` storage-service:   ​​migrateJob:     extraVolumes: ``` | `[]` | Additional volumes to add to the storage service migration job. |
| ``` storage-service:   migrateJob:     ​extraVolumeMounts: ``` | `[]` | Additional volume mounts to add to the storage service migration job. |
| ``` storage-service:   ​​migrateJob:     image: ``` | `"storage-service-​migration"` | The name of the Storage Service migrate job container image. Do not override this value. |
| ``` storage-service:   ​​migrateJob:     initContainers: ``` | `[]` | This Helm key specifies init containers to inject into the Storage Service migrate job pod.  See:   - <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/> |
| ``` storage-service:   ​​migrateJob:     registry: ``` | `""` | The container image registry to use. Use this only if this container is not in the registry specified by the `imageRegistry` Helm key. |
| ``` storage-service:   ​​migrateJob:     version: ``` | `"STORAGE_SERVICE-​VERSION"` | The image version. Use this only if this container image is not the version specified by the `imageVersion` Helm key. |

## storage-service.migrateJob.resources Helm keys

The following Helm keys can be used to override Kubernetes resource requests and
limits.

Table 40. `storage-service.migrateJob.resources.limits` Helm
keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   ​​migrateJob:     ​resources:       limits:         cpu: ``` | `"500m"` |  |
| ``` storage-service:   ​​migrateJob:     resources.:       limits:         memory: ``` | `"1Gi"` |  |

Table 41. `storage-service.migrateJob.resources.requests` Helm
keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   ​​migrateJob:     resources:       requests:         cpu: ``` | `"250m"` |  |
| ``` storage-service:   ​​migrateJob:     resources:       requests:         memory: ``` | `"256Mi"` |  |

## storage-service.minio Helm keys

The following credentials are used by the Storage Service to access storage on MinIO.
These are required if the Storage Service storage type is MinIO. See also Setting MinIO storage type Helm keys.

Set these parameters only if you are using MinIO with Storage Service. Otherwise, do
not enter any values in these parameters.

Important: For further information on configuring
`storage-service.minio` Helm keys, see Configuring Helm keys to support onPrem or non-platform-specific deployments using Redis and Minio within the section Infrastructure and configuration.

Important: If you are using custom domains for storage
service, you must also configure the storage service custom domain properties as
described in Storage service custom domains.

Table 42. storage-service.minio Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   ​​minio:     bucket: ``` | `""` | Specifies the MinIO Storage Service bucket name. |
| ``` storage-service:   ​​minio:     region: ``` | `""` | Specifies the Storage Service bucket region. |
| ``` storage-service:   ​​minio:     secret:       name: ``` | `""` | Specifies the MinIO Storage Service bucket secret name. The MinIO Kubernetes secret must contain the following keys: `root-user` and `root-password.` |

## storage-service.observability Helm keys

The following Helm keys set up Storage Service metrics data observability.

Table 43. storage-service.observability Helm keys

| Key | Default value |  |
| --- | --- | --- |
| ``` storage-service:   ​​observability:     exposeMetrics: ``` | `true` | If `true`, exposes time series metrics in Prometheus format.  - `true` = Expose Storage Service time series   metrics in Prometheus format. - `false` = Do not expose Storage Service time   series metrics. |
| ``` storage-service:   ​​observability:     jaegerURL: ``` | `""` | Specifies a Jaeger instance to push distributed tracing data to. Either   - Enter a Jaeger instance. - To disable, set value to `""` (empty). This   will use a no-op tracer. |

## storage-service.postgres Helm keys - configure access to a Storage Service PostgreSQL database

If you created a PostgreSQL database instance for use by the Storage Service, you
need to configure these `storage-service.​​postgres` Helm keys to
create jobs that that enable the Storage Service to access the its' PostgreSQL
database.

If needed, for Storage Service you can override PostgreSQL Helm keys using the
`storage-service.​​postgres` keys identified in this section. The
`storage-service.​​postgres` Helm keys below are Storage
Service-specific keys that override parameters configured in the
`postgres` Helm keys within the `scan-services`
chart, and `global.postgres` Helm keys.

Note:

For `storage-service.postgres` info in the Helm chart chapter, see
Configuring postgres Helm keys for Scan Service and Storage Service databases.

For information on `postgres` Helm keys within the
`scan-services` chart, see postgres Helm keys - configure Scan Service and Storage Service access to a PostgreSQL database.

For information on `global.postgres` Helm keys, see Global Helm keys.

For information on precedence, see About the cnc chart and scan-services subchart.

Table 44. `storage-service.postgres` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   ​​postgres:     createDatabase: ``` | true | - `true` enables the creation of a storage   service job that provides storage service access to the   PostgreSQL database. This is the default value. - `false` denies storage service access to the   Connect PostgreSQL database   The PostgreSQL database resources must already exist; they are not created by this job. |
| ``` storage-service:   ​​postgres:     database: ``` | `"storage"` | The name of the PostgreSQL database that is created specifically for the Storage Service. For example, `"storage"`.  If configured, this value overrides the `postgres.​database` Helm key for only the Storage Service PostgreSQL database. The `postgres.​database` key has a default value `"postgres"`. |
| ``` storage-service:   ​​postgres:     existingSecret: ``` | `""` | This Helm key enables you to specify an existing Kubernetes PostgreSQL secret name specifically for Storage Service that contains the keys:   - `host` - `port` - `username` - `password` |
| ``` storage-service:   ​​postgres:     host: ``` | `""` | Specify the path and hostname of the PostgreSQL database host.  Use this key if you have not created a secret. |
| ``` storage-service:   ​​postgres:     password: ``` | `""` | Specify the password for PostgreSQL access.  Use this key if you have not created a secret.  See also `storage-service.postgres.user` to provide the username. |
| ``` storage-service:   ​​postgres:     port: ``` |  | - If `storage-service.postgres.port` has no   value (default), Storage Service uses the PostgreSQL port   defined in the `postgres.port` key (default =   5432). - If a port value is set in   `storage-service.postgres.port` that   value overrides the value in `postgres.port`   for Storage Service.   Use this key if you have not created a secret. |
| ``` storage-service:   ​​postgres:     sslmode: ``` | `""` | The PostgreSQL SSL mode for Storage Service can be overridden using one of the following values:   - `""` (no override) - `"disable"` - `"allow"` - `"prefer"` - `"require"` - `"verify-ca"` - `"verify-full"`   The default value is `""` which inherits the value set in the `postgres.sslmode` key. For the current SSL value, refer to the `postgres.sslmode` key and any overrides.  For value definitions, see Table 1. |
| ``` storage-service:   ​​postgres:     user: ``` | `""` | Specify the username for PostgreSQL access. See also `storage-service.postgres.password` to provide the password.  Use this key if you have not created a secret. |

## storage-service.resources Helm keys

The following Helm keys set Kubernetes resource requests and limits for storage
service.

Table 45. `storage-service.resources.limits` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   ​​resources:     limits:       cou: ``` | `"250m"` |  |
| ``` storage-service:   ​​resources:     limits:       memory: ``` | `"512Mi"` |  |

Table 46. `storage-service.resources.requests` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   ​​resources:     requests:       cpu: ``` | `"100m"` |  |
| ``` storage-service:   ​​resources:     requests:       memory: ``` | `"128Mi"` |  |

## storage-service.s3 Helm keys

The following Helm keys configure credentials used to access storage when on Amazon
AWS or with MinIO. These keys are required with AWS or MinIO.

Important: For further information on configuring
`storage-service.s3` Helm keys, see Configuring Helm keys to support AWS using S3 or S3 Express within the section Amazon AWS infrastructure and configuration.

Note: Do not use these options for other cloud provider
platforms.

Table 47. `storage-service.s3` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   ​​s3:     bucket: ``` | `""` | The bucket name. |
| ``` storage-service:   ​​s3:     region: ``` | `""` | The bucket region. |
| ``` storage-service:   ​​s3:     secret:       name: ``` | `""` | Specifies the name of the AWS service account secret that contains the following AWS access keys `aws_secret_key` and `aws_access_key`. For information on the secret, see Create an AWS storage service secret. |
| ``` storage-service:   ​​s3:     serviceAccount: ``` | `""` | For IAM roles, you can specify the name of a role-based AWS service account. To create a role-based AWS service account refer to Using a role-based AWS service account for Storage Service and Cache Service. If a service account is specified in this key, AWS credentials (access_keys) specified in the `storage-service.​s3.secret.name` Helm key will not be used. |

## storage-service.s3Express Helm keys

The following Helm keys configure credentials used to access storage when on Amazon
AWS. These keys are required with AWS when the S3Express (Directory) bucket is
configured.

Important: For further information on configuring
`storage-service.s3Express` Helm keys, see Configuring Helm keys to support AWS using S3 or S3 Express within the section Amazon AWS infrastructure and configuration.

Note: `storage-service.storageType: ""` must be set
to `"s3Express"`.

Note: Also see the following cache service s3Express Helm keys
within the `scan-services` Helm subchart:
`cache-service.aws.s3Express.enabled:` and
`cache-service.aws.s3Express.ttlDays:`.

Note: Do not use these options for other cloud provider
platforms.

Note: With an AWS S3 Express bucket configured, you can NOT upload
a `coverity-all-platforms-<version>.tar.gz` file from the
Connect UI. See Uploading Coverity Tools artifacts to the Connect UI.

Table 48. `storage-service.s3Express` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` storage-service:   ​​s3Express:     bucket: ``` | `""` | The S3 Express bucket name. Required with S3 Express. |
| ``` storage-service:   ​​s3Express:     region: ``` | `""` | The S3 Express bucket region. Required with S3 Express. S3 Express storage is available in the following regions:   - ap-northeast-1 - eu-north-1 - us-east-1 - us-west-2 |
| ``` storage-service:   ​​s3Express:     secret:       name: ``` |  | Specifies the name of the AWS service account secret that contains the following AWS access keys `aws_secret_key` and `aws_access_key`. For information on the secret, see Create an AWS storage service secret. |
| ``` storage-service:   ​​s3Express:     serviceAccount: ``` | `""` | Enter the name of the AWS instance profile service account that contains IAM roles (IRSA) that enable EC2 instances to access AWS services. If you provide a serviceAccount value, the IRSA will be used and any AWS credentials (aws_secret_key and aws_access_key) provided in the secret will be ignored.  See also <https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html>. |

## trust-stores Helm keys

The following `trust-stores` Helm keys can be used to override the
`global.trust-stores.confignapName` value if needed for only
scan-services.

Table 49. `trust-stores` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` trust-stores:   ​configmapName: ``` | `""` | This Helm key specifies the name of the configmap that contains the Connect truststore certificates.  The default name is `connect-trust-stores` as defined in the `global.trust-stores.​configmapName` Helm key.  Example of the `connect-trust-stores` configmap for the Connect pod:   ``` kubectl create configmap connect-trust-stores \      --from-file=postgres-root.pem \      --from-file=LDAP-root-cert \      --from-file=Jira-root-cert \      --from-file=Bugzilla-root-cert \      --namespace "$NS" ```   Important: The PostgreSQL root certificate must be named `postgres-root.pem`.  The names of all files except PostgreSQL root certificate are not important; they are mounted into the same directory. All files in that directory are treated as certificates and loaded into the Coverity Connect truststore.  For further information on creating Connect configmaps, refer to the appropriate section(s) for your deployment:   - For a single Connect instance: Creating a truststore ConfigMap for a Connect instance |
| ``` trust-stores:   ​enabled: ``` |  | - `true` = enable importing certificates into   the Coverity Connect truststore. - `false` = disable importing certificates into   the Coverity Connect truststore. |
