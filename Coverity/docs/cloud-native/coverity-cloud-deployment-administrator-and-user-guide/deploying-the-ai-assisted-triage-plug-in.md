---
title: "Deploying the AI-Assisted Triage Plug-in"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deploying-the-ai-assisted-triage-plug-in.html"
content_id: "u3~nrmSqCus~298OH0vHtA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:30.540104+00:00"
---

# Deploying the AI-Assisted Triage Plug-in

Important: The AI-Assisted Triage Plug-in is a Beta
release feature.

Note: While working within this chapter, see also:

- For upgrade information: Upgrading to 2026.6 and Performing an upgrade.
- For `triage-suggestion-service` Helm keys in the
  `cnc` chart: triage-suggestion-service: Helm keys
- For the `triage-suggestion-service` Helm subchart: triage-suggestion-service Helm subchart
- For `triage-suggestion-service` container images: Coverity container images
- For configuring LLM API keys and shared secret/public key: Deploying and configuring the AI-Assisted Triage Plug-in

This section describes Coverity cloud deployment of AI-Assisted Triage Plug-in API and
Worker services with external PostgreSQL and RabbitMQ for high availability and
scalability. This deployment consists of:

- **API Service**: Handles HTTP requests and queue publishing
- **Worker Service**: Processes triage requests from queue, invokes CLI
- **PostgreSQL**: Persistent database for request/result storage
- **RabbitMQ**: Message broker for async job distribution

## Prerequisites

- **Kubernetes Cluster**: v1.34+ with Helm 3.12+
- **PostgreSQL**: 14+ (managed or self-hosted)
- **RabbitMQ**: 3.9+ (managed or self-hosted)
- **AI Triage CLI Binary**: Available in Docker images
- **LLM API Key**: Stored as Kubernetes secret
- **Docker Images**: Available from registry or built locally

## **Security considerations**

The data shared with the configured LLM is limited to what is required to explain and
triage the selected issues. However the data collected includes unredacted source
files and issue data. By enabling the feature, you are automatically consenting to
send the data as needed for the triage. Ensure that your organization’s policies
allow sharing the required data with the configured LLM.

Important: You are responsible for securing the service, the logs, and the
network environment.

## Deploying the AI-Assisted Triage Plug-in via the Helm chart

**Distributed deployment (Helm)**

Distributed mode is intended for production deployments that need horizontal scaling,
high availability, or volume beyond what a single standalone process can sustain. It
separates the service into an API tier and a worker tier that communicate through
RabbitMQ, with PostgreSQL as the metadata and result store, and GCS, S3, Azure Blob, or
MinIO for scan artifacts.

Before running helm upgrade `--install`, create the Kubernetes Secrets the
chart expects:

- Authentication secrets
- Key
  pair

Add the following to your Coverity Cloud umbrella chart values file. Replace placeholder
hostnames, secret names, and bucket names with values appropriate for your environment.

```
triage-suggestion-service:
  enabled: true

  # LLM endpoint reachable from Worker pods.
  llm:
    url: "https://llm.example.com/v1"
    name: "gpt-4"

  # Key pair
  llmKeyEncryption:
    existingSecret: "triage-suggestion-service-llm-key-encryption"
    secretKey: "llm-key-private.pem"

  # Cloud artifact store. Choose one of: s3, gcs, azure, minio.
  artifactStorage:
    storageType: "s3"
    s3:
      bucket: "my-triage-artifacts"
      region: "us-east-1"
      secret:
        name: "triage-s3-credentials"   # keys: aws_access_key, aws_secret_key

  # PostgreSQL — point at your managed Postgres or the bundled subchart.
  postgres:
    enabled: true
    host: "postgres.coverity.svc.cluster.local"
    port: "5432"
    database: "triage_suggestion_service"
    existingSecret: "triage-postgres-credentials"   # keys: username, password

  # RabbitMQ — bundled subchart shown; for an external broker use externalRabbitmq.
  rabbitmq:
    enabled: true

  # API tier
  deployment:
    replicaCount: 3
    autoscaling:
      enabled: true
  hpa:
    enabled: true
    minReplicas: 3
    maxReplicas: 10

  workerDeployment:
    replicaCount: 5
    autoscaling:
      enabled: true
  workerHpa:
    enabled: true
    minReplicas: 5
    maxReplicas: 20
```

After `helm upgrade` completes and pods report Ready, verify connectivity
from inside the
cluster:

```
kubectl -n <namespace> exec deploy/cnc -- \
  curl -fsS http://triage-suggestion-service-api:8080/liveness
```

The expected
response is: `{"status":"ok","message":"service is alive"}`.

**Network requirements**

Kubernetes
:   No additional firewall rules are needed for in-cluster communication. If
    Coverity Cloud is external to the cluster, expose the service through an Ingress
    or LoadBalancer.

**Network requirements**

Standalone
:   Open the port set in the yaml file for HTTP or HTTPS on the triage service
    host. Allow inbound connections from the Coverity Cloud server.

**TLS/HTTPS**

To enable TLS, apply the following settings (the specified location is an example,
specify the path to your crt and key files):

```
tls_enabled: true
tls_cert_file: /etc/tls/server.crt
tls_key_file: /etc/tls/server.key
```

Update the Coverity Cloud configuration to use HTTPS. If you use self-signed
certificates, add the cert to the Coverity Cloud trust store in both of the
following:

- The `truststore.jks` (found in `<platform install
  dir>/config`) using the `cov-import-cert` tool
  (found in `<platform install dir>/bin`).
- Cacerts (found in `<platform install
  dir>/jre/lib/security/cacerts`) using keytool.

## Configuration reference

The service uses a hierarchical configuration system. The following list shows the
order of priority, from highest to lowest.

1. Environment variables
2. Configuration file in YAML or JSON format
3. Built-in defaults

The service searches for configuration files in the following order.

1. Path set with the `--config` or `-c` command-line
   flag
2. Path set with the `TRIAGE_SERVICE_CONFIG_FILE` environment
   variable
3. `triage-suggestion-service.yaml` or
   `triage-suggestion-service.json` in the current
   directory

**Service settings**

| Option | Environment variable | Default | Description |
| --- | --- | --- | --- |
| service_mode | SERVICE_MODE | standalone | Deployment mode. Options are `standalone`, `api`, or `worker`. |

**HTTP server settings**

| Option | Environment variable | Default | Description |
| --- | --- | --- | --- |
| http_port | HTTP_PORT | 8080 | HTTP/HTTPS server port |
| metrics_port | METRICS_PORT | 9090 | Prometheus metrics endpoint port |
| base_url | BASE_URL | Auto-generated | Public base URL for the service. If empty, the service generates `http(s)://localhost:port` automatically. |

**TLS settings**

| Option | Environment variable | Default | Description |
| --- | --- | --- | --- |
| tls_enabled | TLS_ENABLED | false | Enable HTTPS. Requires a certificate and key. |
| tls_cert_file | TLS_CERT_FILE | (none) | Path to TLS certificate file in PEM format |
| tls_key_file | TLS_KEY_FILE | (none) | Path to TLS private key file in PEM format |

**Worker settings**

| Option | Environment variable | Default | Description |
| --- | --- | --- | --- |
| worker_count | WORKER_COUNT | 5 for standalone/default, 3 for Helm/Docker distributed | Number of concurrent workers. Must be 1 in distributed mode for data isolation. |

**CLI settings**

| Option | Environment variable | Default | Description |
| --- | --- | --- | --- |
| cli_path | CLI_PATH | /opt/cov-triage-issue-linux64-main/bin/cov-triage-issue | Path to AI triage CLI binary |
| cli_timeout | CLI_TIMEOUT | 600s (10 minutes) | CLI execution timeout |
| work_dirs | WORK_DIRS | ./work_dirs | Directory for artifact extraction and processing |
| cleanup_work_dirs | CLEANUP_WORK_DIRS | true | Clean up working directories after processing |

**LLM settings**

See Configuring LLM API keys.

**Storage settings**

| Option | Environment variable | Default | Description |
| --- | --- | --- | --- |
| storage_type | STORAGE_TYPE | memory | Storage backend. Use `memory` for standalone or `postgres` for distributed. |
| request_retention | REQUEST_RETENTION | 1h | How long to keep request metadata |
| results_retention | RESULTS_RETENTION | 10m | How long to keep triage results |
| artifact_retention | ARTIFACT_RETENTION | 15m | How long to keep uploaded artifacts |

**Artifact storage settings**

| Option | Environment variable | Default | Description |
| --- | --- | --- | --- |
| artifact_storage_type | ARTIFACT_STORAGE_TYPE | local | Artifact storage backend. Options are `local`, `s3`, or `azure`. |
| artifact_storage_path | ARTIFACT_STORAGE_PATH | ./artifacts | Local filesystem path for artifacts |
| artifact_max_size | ARTIFACT_MAX_SIZE | 104857600, which is 100 MB | Maximum artifact size in bytes |

## Health check endpoints

**GET /liveness**

Liveness probe. Use as a Kubernetes liveness probe to determine whether to restart
the pod.

```
{"status":"ok","message":"service is alive"}
```

**GET /readiness**

Readiness probe. Use as a Kubernetes readiness probe to determine whether the pod can
receive traffic.

```
# Healthy
{"status":"ready","checks":{"storage":"healthy"}}

# Unhealthy (503)
{"status":"not ready","checks":{"storage":"unhealthy: connection failed"}}
```

## Prometheus metrics

The service exposes Prometheus-compatible metrics on the metrics port (default 9090)
at `/metrics`.

## Logging

The service uses structured logging. The default format is JSON. You can change the
format to text with `log_format`.

Log levels are `debug`, `info`, `warn`,
and `error`. The default log level is `info`.

## Troubleshooting

**Coverity Cloud cannot reach the triage service**

- Verify the service is running with `curl
  http://triage-suggestion-service-host:8080/liveness`.
- Check network connectivity from the Coverity Cloud server with `telnet
  triage-suggestion-service-host 8080`.
- Verify firewall rules and security groups allow the connection.
- In Kubernetes, check NetworkPolicies with `kubectl get networkpolicies -n
  triage-suggestion-service`.

**Triage requests failing**

- Check service logs.

  ```
  # Standalone
  journalctl -u triage-suggestion-service -f

  # Kubernetes
  kubectl logs -f deployment/triage-suggestion-service-worker -n triage-suggestion-service
  ```
- Verify the CLI binary is accessible with `ls -l
  /opt/cov-triage-issue/bin/cov-triage-issue`.
- Verify LLM connectivity with `curl -v
  https://llm-endpoint.com`.
- Check worker pod resources, including CPU and memory limits.

**Requests stuck in queued or processing status**

- Check that worker pods are running and consuming from the queue.
- Verify RabbitMQ connectivity in distributed mode.
- Check the CLI timeout setting. Increase `cli_timeout` if the LLM
  is slow to respond.
- Verify the LLM API key file is readable and the key is valid.

**Service readiness check failing**

- Check the `/readiness` endpoint for specific check failures.
- In distributed mode, verify PostgreSQL connectivity and credentials.
- Check that the storage backend is accessible and has sufficient disk space.

**Requests timing out**

cli_timeout is set to 10 minutes by default. If a request times out, consider
triaging fewer issues or increasing the cli_timeout setting.

**AI triage returns an error for MISRA issues**

MISRA-related checkers are not supported in the 2026.6.0 release. When AI triage is
run on a MISRA issue, the following error is returned:

```
[ERROR] Triage of MISRA issues is not supported in this context for legal compliance
```

This is expected behavior. No action is required.

## Scaling a deployment

Scale API pods for increased request capacity:

```
kubectl scale deployment triage-suggestion-service-api --replicas=5 -n triage-suggestion-service
```

Scale Worker pods for increased processing capacity:

```
kubectl scale deployment triage-suggestion-service-worker --replicas=10 -n triage-suggestion-service
```

Important: Each worker pod processes one request at a
time (`WORKER_COUNT=1`, `MQ_WORKER_CONCURRENCY=1`) to
ensure customer data isolation. Scale horizontally by adding more pods, NOT by
increasing worker concurrency.

## Global artifact storage inheritance

The `cnc` chart supports a `global.artifactStorage`
block. When set at the global level, `triage-suggestion-service`
automatically inherits the storage type and provider credentials without needing to
configure subcharts:

```
global:
  artifactStorage:
    storageType: "gcs"       # "gcs", "s3", "azure", or "minio"
    gcs:
      bucket: "my-artifacts"
      secret:
        name: "gcs-creds"    # k8s secret with GCP service account JSON
        key: "sa.json"
```

If both `global.artifactStorage` and
`triage-suggestion-service.artifactStorage` are set, the
subchart-level values take precedence.

## Artifact storage provider examples

The following illustrate `triage-suggestion-service` subchart values
for each supported cloud storage platform:

AWS S3 storage example:

```
triage-suggestion-service:
  artifactStorage:
    storageType: "s3"
    s3:
      bucket: "my-triage-artifacts"
      region: "us-east-1"
      secret:
        name: "aws-s3-creds"  # keys: aws_access_key, aws_secret_key
      # Or use IRSA:
      # serviceAccount: "triage-suggestion-service"
```

Google Cloud storage example:

```
triage-suggestion-service:
  artifactStorage:
    storageType: "gcs"
    gcs:
      bucket: "my-triage-artifacts"
      secret:
        name: "gcs-sa-key"    # secret containing service account JSON
        key: "credentials.json"
```

Azure Blob storage example:

```
triage-suggestion-service:
  artifactStorage:
    storageType: "azure"
    azure:
      container: "triage-artifacts"
      storageAccountName: "mystorageaccount"
      secret:
        name: "azure-storage-creds"  # key: azure_storage_key
```

MinIO S3-compatible storage example:

```
triage-suggestion-service:
  artifactStorage:
    storageType: "minio"
    minio:
      bucket: "triage-artifacts"
      endpoint: "minio.minio-system.svc.cluster.local:9000"
      secure: false
      pathStyle: true
      secret:
        name: "minio-creds"   # keys: root-user, root-password
```

## Monitoring - Prometheus metrics

The `triage-suggestion-service` exposes Prometheus metrics on port
9090:

```
# ServiceMonitor for Prometheus Operator
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: triage-suggestion-service
  namespace: triage-suggestion-service
spec:
  selector:
    matchLabels:
      app: triage-suggestion-service-api
  endpoints:
  - port: metrics
    path: /metrics
    interval: 30s
```

## Helm key values

The following table identifies cnc chart and
`triage-suggestion-service` subchart values. The first key,
`triage-suggestion-service. enabled:` is in the
`cnc` chart. All other keys in the table are in the
`triage-suggestion-service:` subchart.

Note: For information on these and other
`triage-suggestion-service` Helm keys, see:

- For `triage-suggestion-service` Helm keys in the
  `cnc` chart: triage-suggestion-service: Helm keys
- For the `triage-suggestion-service` Helm subchart keys: triage-suggestion-service Helm subchart

| Key | Default value | Description |
| --- | --- | --- |
| ``` triage-suggestion-service:   enabled: ``` | `false` | This Helm key is in the `cnc` chart. See triage-suggestion-service: Helm keys.  To enable `triage-suggestion-service` deployment, change this value to `true`. |
| ``` triage-suggestion-service:   global:     artifactStorage:       storageType: ``` | (none) | Cloud storage backend: `s3`, `gcs`, `azure`, or `minio`. |
| ``` triage-suggestion-service:   artifactStorage:     maxSize: ``` | `209715200` (200MB) | Maximum artifact upload size in bytes. |
| ``` triage-suggestion-service:   artifactStorage:     uploadUrlExpiration: ``` | `1h` | Presigned upload URL validity duration. |
| ``` triage-suggestion-service:   deployment:     replicaCount: ``` | `3` | Number of API pod replicas. |
| ``` triage-suggestion-service:   workerDeployment:     replicaCount: ``` | `5` | Number of Worker pod replicas. |
| ``` triage-suggestion-service:   hpa:     enabled: ``` | `true` | Enable Horizontal Pod Autoscaler for API. |
| ``` triage-suggestion-service:   hpa:     minReplicas: ``` | `3` | API autoscaling range. |
| ``` triage-suggestion-service:   hpa:     maxReplicas: ``` | `10` |
| ``` triage-suggestion-service:   workerHpa:     enabled: ``` | `true` | Enable Horizontal Pod Autoscaler for Workers. |
| ``` triage-suggestion-service:   workerHpa:     minReplicas: ``` | `5` | Worker autoscaling range. |
| ``` triage-suggestion-service:   workerHpa:     maxReplicas: ``` | `20` |
| ``` triage-suggestion-service:   postgres:     enabled: ``` | `false` | Enable PostgreSQL config injection. |
| ``` triage-suggestion-service:   postgres:     database: ``` | `triage-suggestion-service` | PostgreSQL database name. |
| ``` triage-suggestion-service:   vault:     enabled: ``` | `false` | Enable Vault-based dynamic database credentials. |
| ``` triage-suggestion-service:   ingress:     triage-suggestion-service-ingress:       enabled: ``` | `true` | Enable Kubernetes ingress for API service. |
| ``` triage-suggestion-service:   securityContext:     runAsUsersecurityContext.runAsUser ``` | `5000` | User ID for container processes. |
