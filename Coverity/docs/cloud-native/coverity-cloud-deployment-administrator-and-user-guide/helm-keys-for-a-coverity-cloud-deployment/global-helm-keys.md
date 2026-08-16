---
title: "Global Helm keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/global-helm-keys.html"
content_id: "OxmLQCYu_bcdvrX9S3rsdg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:46:02.411772+00:00"
---

# Global Helm keys

In Coverity cloud, global Helm keys are global values that are used by both the parent
cnc chart and its scan-services subchart. The following Helm keys are global. values
that can be accessed from the `cnc` chart and the
`scan-services` subchart.

Important: Provide global Helm keys in any custom
`.yaml` file or Helm command using the global syntax specified in the
Helm chart.

The following categories of global Helm keys, described in the sections and tables that
follow, are available in both the `cnc` chart and the
`scan-services` chart:

- `global` - See global root Helm keys.
- `global.ingress` - See global.ingress Helm keys.
- `global.postgres` - See global.postgres Helm keys.
- `global.proxy` - See global.proxy Helm keys.
- `global.redis` - See global.redis Helm keys.
- `global.trust-stores` - See global.trust-stores Helm keys.

If you are deploying the `scan-services` chart, we recommend that you
configure the global key values to pass values to both the `cnc` chart
and the `scan-services` chart.

Refer to the following documentation for further information on global keys and global
chart values and how to use them in Coverity cloud:

- For Helm documentation, see: <https://helm.sh/docs/chart_template_guide/subcharts_and_globals/#global-chart-values>.
- For Coverity Cloud deployment information, see also: About the cnc chart and scan-services subchart.

## global root Helm keys

Table 1. Global root Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` global:   extraVolumeMounts: ``` | `[]` | Use this Helm key to mount volumes created in the `extraVolumes` Helm key. This mounts volumes for Connect admin tools and Connect database tools.  `scan-services` subchart: In the scan-services subchart, this key adds additional volume mounts to all containers and jobs except AnalysisJob and cleanUpJob.  `cnc` chart: This key is not in the `cnc` chart. |
| ``` global:   extraVolumes: ``` | [] | Common additional volumes to add to All `cnc` and `scan-services` pods and jobs except AnalysisJob and cleanUpJob.  If you want to set different additional volumes for `cnc` and `scan-services` pods and jobs, set `global.extraVolumes` to attach additional volumes to your CNC pods. Set `scan-services.extraVolumes` to attach additional volumes to your scan-services pods.  This single Helm key, if configured, provides additional volumes for the following Coverity Connect pods: Connect webapp, Connect admin tools, and Connect database tools. See the `extraVolumeMounts` Helm key to mount these volumes. |
| ``` global:   imagePullPolicy: ``` | `"IfNotPresent"` | See the Kubernetes page: <https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy>. This is set on each Coverity cloud deployment pod to control its image pull policy. Valid values are:   - `"IfNotPresent"` - Kubernetes checks if the   image exists on the node. If it does, it uses the cached   copy; otherwise, it pulls the image from the registry. With   imagePullPolicy set to ifNotPresent, the container images   are good for the life of the node. Numerous pods can be spun   up and down from the cached image(s). - `"Always"` - Kubernetes always attempts to   pull the image from the registry to ensure the latest   version is used. - `"Never"` - Kubernetes never pulls images.   The images must already be locally available. If an image is   not available locally, pod creation fails.  See the Kubernetes page: [Kubernetes documents](https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy). |
| ``` global:   imagePullSecret: ``` | `""` | Specify the name of the secret that contains the credentials needed to connect to the registry that contains the container images and client images used to deploy the Coverity cloud containers and jobs. This must be set for images that are pulled from a registry that requires authentication. The Coverity images must be kept in a private Docker registry requiring credentials to access. Also, the secret must exist in the same namespace.  For information on creating an image pull secret, refer to:   - Create a container image pull secret - <https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod> |
| ``` global:   imageRegistry: ``` | `"COVERITY_IMAGE_​REGISTRY"` | The registry from which Kubernetes nodes pull Black Duck Coverity cloud container images from. While these images can be pulled from the Black Duck registry, using your own private registry provides much faster image pulls. If you use multiple registries, this key can be overridden by the chart-level `imageRegistry` keys. |
| ``` global:   imageTagSuffix: ``` | `""` | If you are installing Coverity on OpenShift, you need to specify a `-ubi` suffix in the Coverity image name using this Helm key.  Valid values for this key are:   - `"-ubi"` - use this value for an image you   will install in Red Hat OpenShift. For example, if you are   deploying Coverity cloud version 2026.6.0   in OpenShift, you need to use image version `2026.6.0-ubi`. - `""` - this is the default value for   Kubernetes images. For example, if you are deploying   Coverity cloud version 2026.6.0 in   Kubernetes, you need to use image version `2026.6.0`. |
| ``` global:   imageVersion: ``` | `""` | The container image tag used for all Black Duck images. This can be overridden for each chart by the root `imageVersion` Helm key available in the respective `cnc` or `scan-services` chart. |
| ``` global:   keygen:     enabled: ``` | `false` | Important: Keygen is Black Duck internal use only. Do NOT enable Keygen. |
| ``` global:   licenseSecretName: ``` | `""` | This Helm key specifies the name of a Coverity license secret. This license is used by both Coverity Connect and Coverity Analysis. The secret, which is in the Connect namespace, must contain a valid and active Connect license. The name of the license key stored in the license secret must be `license.dat`.  Important: The Helm chart contains references to Keygen and a `license.json` license secret. Do NOT use Keygen or `license.json`. They are Black Duck internal use only.  Refer to:   - Specify the name of the Connect license secret - Create a Connect license secret   `global.licenseSecretName` can be used for both Coverity Connect and Coverity Analysis licenses.   - If you have a license that is valid for both Coverity   Connect and Coverity Analysis, set only   `global.licenseSecretName`. You do not   need to set   `scan-service.licenseSecretName`. - If you are not using Scan Service, set only the   `licenseSecretName` Helm key. - If you are using Scan Service and have two separate   licenses for Connect and Analysis, then:   - Set `global.licenseSecretName` for     your Connect license.   - Set `scan-service.licenseSecretName`     for your Analysis license. |
| ``` global:   tolerations: ``` | [] | This is a global tolerations parameter that sets the tolerations on all of the Coverity cloud pods.  By default, Coverity is deployed on AMD pods. To deploy on only ARM64 pods, you would provide the following toleration:   ``` global:   tolerations:     - key: "kubernetes.io/arch"       operator: "Equal"       value: "arm64"       effect: "NoSchedule" ```   Note: Refer to:  - Setting up ARM64 support - <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/> |

## global.artifactStorage Helm keys

The following `global.artifactStorage` Helm keys enable Coverity cloud
access and security for artifact storage that exists in AWS, s3, Azure, or GCP. For
any of these storage types, you need to specify the storage type, then specify the
secret to access the storage.

Subcharts that read `Values.global.artifactStorage` values (for
example, the `triage-suggestion-service`) automatically inherit the
storage type and provider credentials.

Table 2. `global.artifactStorage` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` global:   artifactStorage:     storageType: "" ``` | `""` | If you are using cloud storage, specify one of the following storage types: `"gcs"`, `"s3"`, `"azure"`, or `"minio"`  For gcs, s3, and azure, you also need to configure the secret keys |
| ``` global:   artifactStorage:     gcs:       bucket: ""       secret:         name: ""         key: "key.json" ``` |  | `required when storageType is "gcs"`  `...secret.name:` - Kubernetes secret containing GCP service account JSON key.  `...secret.key: "key.json"` - Key inside the secret. |
| ``` global:   artifactStorage:     s3:       bucket: ""       region: ""       secret:         name: "" ``` |  | The default ingress controller is NGINX, therefore the default value points to the `kubernetes.io/ingress.class` annotation key. If you use a different ingress controller, update the value in this field. |
| ``` global:   artifactStorage:     azure:       container: ""       storageAccountName: ""       secret:         name: "" ``` |  | Set to `true` to create a Kubernetes ingress object. |

## global.ingress Helm keys

The following Helm keys configure the ingress controller. If TLS sidecar NGINX
reverse proxy is enabled, this will forward to `https/8443`;
otherwise it will forward to `http/8080`.

Important: Do NOT enable TLS sidecar if you are
deploying only Coverity Connect in the cloud.

Table 3. `global.ingress` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` global:   ingress:     annotations: ``` |  | Additional annotations to provide to the ingress object.  You can use the following annotation syntax to specify the maximum file size to allow through the ingress port: `nginx.ingress.kubernetes.io/proxy-body-size: <fileSize>` For example, to be able to upload a 7.6 GB Coverity toolkit tar file from a client to Connect:   ``` global:   ingress:     annotations:       nginx.ingress.kubernetes.io/proxy-body-size: 8g ```   See also Set NGINX proxy-body-size for Coverity toolkit tar file upload to Connect. |
| ``` global:   ingress:     ccdPath: ``` | ``` "/ccd" ``` | `cnc` chart: This Helm key is used in the `cnc` chart.  If `commit-server` pods are deployed, the ingress controller directs commits to the commit servers (CCD servers). Also refer to cim.commit-server Helm keys. |
| ``` global:   ingress:     class: ``` | `"nginx"` | The default ingress controller is NGINX, therefore the default value points to the `kubernetes.io/ingress.class` annotation key. If you use a different ingress controller, update the value in this field. |
| ``` global:   ingress:     enabled: ``` | `false` | Set to `true` to create a Kubernetes ingress object. |
| ``` global:   ingress:     hosts: ``` | `[]` | Array of allowed host names.  Important: The Connect (cim) hostname that you specify in `global.ingress.hosts` must not exceed 46 characters in length. This restriction excludes the `https://` characters that are used when you specify the URL, as well as any port specification. |
| ``` global:   ingress:     path: ``` | `"/"` | The ingress rule path.   - You might need to set this to `"/*"` for   AWS ALB ingress controllers. - You might need to set this to `"/*"` for   GCE ingress controllers. - You might need to add a path if you are using a context   path. |
| ``` global:   ingress:     tls: ``` | `[]` | Array of object with schema to select the TLS secret for https:   ``` global:   ingress:     tls:       - secretName: ""         hosts: [] ``` |

## global.keygen Helm key

By default, Keygen is disabled.

Important: Keygen is Black Duck internal use only. Do NOT enable
`global.keygen.enabled`.

Table 4. `global.keygen` Helm key

| Key | Default value | Description |
| --- | --- | --- |
| ``` global:   keygen:     enabled: ``` | ``` false ``` | Important: Keygen is Black Duck internal use only. Do NOT use Keygen. |

## global.postgres Helm keys

The following PostgreSQL Helm keys can be used to set PostgreSQL database connection
parameters for all services (Connect, Scan Service, and Storage Service) connected
to a single PostgreSQL database. If any service has its own Postgres database, the
Postgres Helm keys for that service can override the global parameters for that
service.

The following services can override the `global.postgres` keys as
needed:

- Coverity Connect (`cnc` chart, `cim.postgres` Helm
  keys): See cim.postgres Helm keys - create Connect cim PostgreSQL access job.
- Scan Service (`scan-services` chart,
  `scan-service.postgres` Helm keys) See scan-service.postgres Helm keys - configure access to a Scan Service PostgreSQL database.
- Storage Service (`scan-services` chart,
  `storage-service.postgres` Helm keys) See storage-service.postgres Helm keys - configure access to a Storage Service PostgreSQL database.

Table 5. `global.postgres` Helm keys

| Key | Default Value | Description |
| --- | --- | --- |
| ``` global:   postgres:     existingSecret: ``` | `""` | This Helm key enables you to specify an existing Kubernetes PostgreSQL secret name to be used for all services unless overridden by specific services. The secret must contain the following values:   - `host` - `port` - `username` - `password` |
| ``` global:   postgres:     host: ``` | `""` | Specifies the PostgreSQL host. For example, "cim".  Use this key if you have not created a secret. |
| ``` global:   postgres:     jobSidecars: ``` | [] | You can use this Helm key to specify sidecar containers to add within pods that require a PostgreSQL database connection. This sidecar is added to the native sidecar, which is an init container with `restartPolicy:Always`; you must set `restartPolicy:Always`.  Native sidecar containers require Kubernetes 1.28 or later.  For example:   ``` global:   postgres:     jobSidecars:       - name: cloud-sql-proxy         image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.1.0-buster         restartPolicy: Always         command: ["/bin/sh","-ec"]         args: ["/cloud-sql-proxy              --structured-logs              --port=5432 <gcp-project>:<region>:testgcp-zirw98              --credentials-file=/secrets/key.json              --max-sigterm-delay=100s "]         securityContext:           runAsUser: 5000     volumeMounts:       - name: gcp-sa-secret         mountPath: /secrets/         readOnly: true     resources:       requests:         memory: "500Mi"         cpu: "500m" ```   For further information on using this and related Helm keys, refer to Attaching a Cloud SQL proxy native sidecar container in GCP.  See also: <https://kubernetes.io/blog/2023/08/25/native-sidecar-containers/>. |
| ``` global:   postgres:     password: ``` | `""` | Specifies the password to connect to the PostgreSQL host for a Connect instance.  Use this key if you have not created a secret. |
| ``` global:   postgres:     port: ``` | `"5432"` | Use port 5432 for all instances of PostgreSQL.  Use this key if you have not created a secret. |
| ``` global:   postgres:     sidecars: ``` | [] | The sidecar container specification to attach for pods that require a database connection. The sidecar is added as a native sidecar, which is an init container with `restartPolicy:Always`; you must set`restartPolicy:Always`. You must have Kubernetes 1.28 or later to support native-sidecar.  For further information on using this and related Helm keys, refer to Attaching a Cloud SQL proxy native sidecar container in GCP.  See also: <https://kubernetes.io/blog/2023/08/25/native-sidecar-containers/>.  For example:   ``` global:   postgres:     sidecars:       - name: cloud-sql-proxy         image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.1.0-buster         restartPolicy: Always            args:           #- "--private-ip"           - "--structured-logs"           - "--port=5432"           - "<gcp-project>:<region>:testgcp-zirw98"           - "--max-sigterm-delay=2s"           - "--credentials-file=/secrets/key.json"         securityContext:           runAsUser: 5000         volumeMounts:           - name: gcp-sa-secret             mountPath: /secrets/             readOnly: true         resources:           requests:             memory: "500Mi"             cpu: "500m" ```   where the `args:` are:   - `--private-ip` If you are connecting from   a VPC-native GKE cluster, you can use this flag to have   the proxy connect over private IP. - `--structured-logs` Enable structured   logging with LogEntry format. - `--port=5432` Replace   `DB_PORT` with the port the that the   proxy should listen on. - `<gcp-project>:<region>:testgcp-zirw98`   cloudsql instance name - `--max-sigterm-delay=2s` Allow for   connections to close - `--credentials-file=/secrets/key.json"   securityContext:` This flag specifies where   the service account key can be found |
| ``` global:   postgres:     sslmode: ``` | `"verify-ca"` | The PostgreSQL SSL mode must be one of the following values:   - `"disable"` - `"allow"` - `"prefer"` - `"require"` - `"verify-ca"` - `"verify-full"`   The default value is `"verify-ca"`.  For further information, see Select the PostgreSQL sslmode and find the PostgreSQL root certificate for TLS.  For value definitions, see Table 1. |
| ``` global:   postgres:     user: ``` | "" | The username to connect to the PostgreSQL host.  Use this key if you have not created a secret. |

## global.proxy Helm keys

Set this value at the global level if you want to pass the same configmap for both
`cnc` and `scan-services`.

To use a different configmap for `cnc` and
`scan-services`:

- Set `proxy.<parameter(s)>` to configure it for
  `cnc` services.
- Set `scan-services.proxy.<parameter(s)>` to configure it
  for `scan-services`
- Set only `proxy.<parameters>` if you are NOT using
  `scan-services`.

The following Helm keys define TLS forward proxy values that apply to both the
`cnc` chart and the `scan-services` subchart,
except where overridden. The following proxy parameters configure forward proxy,
which acts as a Man-In-The-Middle.

See also:

- To configure TLS forward proxy, see Configuring TLS forward proxy
- To define chart-level TLS forward proxy keys, see proxy Helm keys

Table 6. `global.proxy` Helm keys

| Key | Default Value | Description |
| --- | --- | --- |
| ``` global:   proxy:     enabled: ``` | `false` | This boolean Helm key enables or disables TLS forward proxy globally within the cluster.   - `true` - Enables TLS forward proxy. - `false` - Disables TLS forward proxy. |
| ``` global:   proxy:     host: ``` | `""` | This string Helm key specifies the proxy host server. |
| ``` global:   proxy:     port: ``` | 3128 | Specifies the proxy port that the host server listens on. |
| ``` global:   proxy:     tlsmode: ``` | `"tls"` | The TLS proxy mode must be one of the following values:   - `"insecure"` = Specifies TLS insecure proxy.   This mode enables you to communicate over http instead of   https.. This is an insecure mode. - `"tls"` = specifies TLS proxy, where the   client authenticates the server. - `"mtls"` = specifies mutual TLS mode, where   the client and server authenticate each other.   The default value is `"tls"`.  When TLS mode is set to either tls or mtls, the proxy server CA certificate must be included in the trust-stores ConfigMap with key name `"proxy-server.pem"`.  The file names of other server CA certificates (excluding postgres, proxy server) are not important.  For example: The Black Duck artifactory server CA certificate can be named `artifactory.pem` in the trust-stores ConfigMap. |
| ``` global:   proxy:     existingSecret: ``` | `""` | If proxy is enabled with `tlsmode` set to `"mtls",` this secret must be contain the following keys: `"client-cert"` and `"client-key"`.  If proxy is enabled with `tlsmode` set to `"insecure"` or `"tls"`, an `existingSecret` is not needed. |

## global.redis Helm keys

The following Helm keys define global Redis related variables needed by the Cache
Service.

Table 7. `global.redis` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` global:   redis:     authEnabled: ``` | `false` | Enable Redis authentication.   - `false` disables authentication - `true` enables authentication   If `true`, you must provide the `redis.passwordSecret`. |
| ``` global:   redis:     cacertSecret: ``` | `""` | If TLS is enabled, specifies the secret that contains the CA certificate to be used for Redis communication. This secret must contain the `ca.crt` key.  To create the secret, see Create a Cache Service CA certificate secret for Redis.  For further Redis Helm key information, see Redis keys. |
| ``` global:   redis:     host: ``` | `""` | Redis host. |
| ``` global:   redis:     passwordSecret: ``` | `""` | Redis password. |
| ``` global:   redis:     port: ``` | `6379` | An integer value that specifies the Redis port. |
| ``` global:   redis:     secure: ``` | `true` | Specifies if TLS is enabled for secure communication with Redis.  - `true` = Enable TLS for secure communication   with Redis. - `false` = Disable TLS. |
| ``` global:   redis:     verifyHostName: ``` | `false` | Specifies whether or not the host name needs to be verified for Redis communication, if TLS is enabled.  - `true` = If TLS is enabled, verify the host   name for Redis communication. - `false` = Do not verify the host name. This   is the default value. |

## global.trust-stores Helm keys

The following `global.trust-stores` Helm key specifies the name of the
ConfigMap that contains the Connect truststore certificates.

Table 8. `global.trust-stores` Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` global:   trust-stores:     configmapName: ``` | `"connect-trust-stores"` | This Helm key specifies the name of the ConfigMap that contains the Connect truststore certificates. The default name is `connect-trust-stores`.  Example of the `connect-trust-stores` ConfigMap for the Connect pod:   ``` kubectl create configmap connect-trust-stores \      --from-file=postgres-root.pem=<postgres-root.pem> \      --from-file=proxy-server.pem=<proxy-server.pem> \      --from-file=<LDAP-root-cert> \      --from-file=<Jira-root-cert> \      --from-file=<Bugzilla-root-cert> \      --namespace "$NS" ```   Important: The PostgreSQL root certificate must be named `postgres-root.pem`.  The names of all files except PostgreSQL root certificate are not important; they are mounted into the same directory. All files in that directory are treated as certificates and loaded into the Coverity Connect truststore.  For further information on creating Connect ConfigMaps, refer to the appropriate section(s) for your deployment:   - For a Connect instance, see Create a truststore ConfigMap for Connect communication over TLS and Creating a truststore ConfigMap for a Connect instance |
| ``` global:   trust-stores:     enabled: ``` | `false` | - `true` = enable importing certificates into   the Coverity Connect truststore. - `false` = disable importing certificates into   the Coverity Connect truststore. |
