---
title: "triage-suggestion-service Helm subchart"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/triage-suggestion-service-helm-subchart.html"
content_id: "~MHVzGQtRSFqXiAClF0b8w"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:46:06.413676+00:00"
---

# triage-suggestion-service Helm subchart

`triage-suggestion-service` is an AI-powered microservice that provides
intelligent triage suggestions for security findings.
`triage-suggestion-service` is an optional service that needs to be enabled
to support AI-Assisted Triage. It deploys separate API and Worker services

This section identifies Helm keys within the `triage-suggestion-service`
Helm subchart. Use these and other keys to configure and deploy the
`triage-suggestion-service` in a Coverity cloud deployment.

This Helm chart is a dependency within the `cnc` chart
`Chart.yaml` file and this feature is deployed as part of the
`cnc` chart deployment. For deployment information, see Deploying the AI-Assisted Triage Plug-in.

Important: The AI-Assisted Triage Plug-in is a Beta release
feature.

Note: See also:

- For deployment and configuration information: Deploying the AI-Assisted Triage Plug-in
- For `triage-suggestion-service` Helm keys in the `cnc`
  chart: triage-suggestion-service: Helm keys
- For `triage-suggestion-service` container images: Coverity container images
- For upgrade information: Upgrading to 2026.3 and Performing an upgrade.

## LLM configuration

Use the LLM leys to specify the LLM and create or specify secrets for LLM access.

| Key | Default value | Description |
| --- | --- | --- |
| ``` llm:   url: "" ``` | `""` | LLM endpoint URL. For example, `https://llm.labs.blackduck.com` |
| ``` llm:   apiKey: "" ``` | `""` | If you provide an LLM API key value in this Helm key, when you run the `helm install` command, the chart will automatically create a Kubernetes Secret which contains the API key.  Alternatively, if you use the `kubectl` command to create the secret, see `llm.existingSecret`. |
| ``` llm:   name: "" ``` | `""` | LLM model name. For example, `"gpt-4"`. This key optional. |
| ``` llm:   existingSecret: ``` | `"triage-suggestion-service-secrets"` | This secret is created if you use the `kubectl` command to create a secret, you can name the secret using the default value `"triage-suggestion-service-secrets"`.  Alternatively, to create a secret when you issue the `helm install` command, see `llm.apiKey`. |
| ``` llm:   secretName: "" ``` | `"triage-suggestion-service-secrets"` | Name of the secret automatically generated if you provided a value in `llm. apiKey:`. |

## Global Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| ``` global:   imagePullPolicy: IfNotPresent   environmentName: production   imagePullSecret: ""   annotations: {}   environment:     APP_NAME: "triage-suggestion-service"     VAULT_CLOUD_FLAG: true   extraVolumes: []   extraVolumeMounts: [] ``` |  |  |
| ``` global:   imagePullPolicy: ``` | `IfNotPresent` |  |
| ``` global:   environmentName: ``` | `production` |  |
| ``` global:   imagePullSecret: ``` | `""` |  |
| ``` global:   annotations: ``` | `{}` |  |
| ``` global:   environment:     APP_NAME: ``` | `"triage-suggestion-service"` |  |
| ``` global:   environment:     VAULT_CLOUD_FLAG: true ``` | `true` |  |
| ``` global:   extraVolumes: []   extraVolumeMounts: [] ``` |  |  |
| ``` global:   resources:     limits:       cpu: "2"       memory: "2Gi"     requests:       cpu: "500m"       memory: "1Gi" ``` |  |  |
| ``` global:   postgres:     host: ""     port: ""     user: ""     password: ""     database: ""     sslmode: ""     existingSecret: "" ``` |  |  |
| ``` global:   trust-stores:     enabled: false     configmapName: "" ``` |  |  |
| ``` global:   artifactStorage:     storageType: "" ``` |  |  |

## Services configuration

The following Helm keys configure the following services:

- `triage-suggestion-service-api`
- `triage-suggestion-service-worker`

| Key | Default value | Description |
| --- | --- | --- |
| ``` services: - name: triage-suggestion-service-api   type: ClusterIP   specs:   - name: "http"     port: 8080     protocol: "TCP"     targetPort: 8080   - name: "metrics"     port: 9090     protocol: "TCP"     targetPort: 9090 - name: triage-suggestion-service-worker   type: ClusterIP   specs:   - name: "metrics"     port: 9090     protocol: "TCP"     targetPort: 9090 ``` |  |  |

## Volume configuration

| Key | Default value | Description |
| --- | --- | --- |
| ``` volumes:   enabled: ``` | `true` |  |
| ``` volumes:   pvc:     enabled: ``` | `false` | Workers use emptyDir for workdirs. |
| ``` volumes:   secrets:   - name: triage-suggestion-service-secrets     mountPath: /secrets     items:       - key: llm-api-key         path: llm-api-key ``` |  |  |
| ``` volumes:   secrets:   - name: triage-suggestion-service-tls     mountPath: /etc/tls     items:       - key: tls.crt         path: server.crt       - key: tls.key         path: server.key   - name: triage-suggestion-service-ca     mountPath: /etc/tls/ca     items:       - key: ca.crt         path: ca.crt ``` |  | Example: Mount TLS certificates for HTTPS (uncomment and configure as needed) |

## Artifact storage

Use these Helm keys to specify and configure scan artifact storage configuration for scan
artifacts (uploads/downloads)

Must be one of: `"s3"`, `"gcs"`, `"azure"`, or
`"minio"`.

| Key | Default value | Description |
| --- | --- | --- |
| ``` artifactStorage:   storageType: ``` | `""` Valid values:   - `"s3"` - `"gcs"` - `"azure"` - `"minio"` | Use this key to specify the storage configuration for scan artifacts (uploads and downloads). |
| ``` artifactStorage:   maxSize: ``` | `"209715200"` | Default value (shown) is 200 MB. |
| ``` artifactStorage:   uploadUrlExpiration: ``` | `"1h"` | Default value is 1 hour. |
| ``` artifactStorage:   s3:     bucket: ""     region: ""       name: ""     serviceAccount: "" ``` |  | AWS S3 configuration.  Configure these keys when `artifactStorage.storageType: "s3"`.  For `artifactStorage.s3.secret.name:`, specify the Kubernetes secret that contains `aws_access_key` and `aws_secret_key`.  For `artifactStorage.s3.serviceAccount:`, specify the AWS instance profile serviceAccount (IRSA). Setting this Helm key overrides other related access keys. |
| ``` artifactStorage:   gcs:     bucket: ""     secret:       key: ""       name: "" ``` |  | Google Cloud Storage configuration.  Configure these keys when `artifactStorage.storageType: "gcs"`.  For `artifactStorage.gcs.bucket:`, specify the name of the storage bucket.  In the `secret:` keys, specify the Kubernetes secret key and name as follows.  For `artifactStorage.gcs.secret.key:`, specify the GCP SA key. For example, `key.json`.  For `artifactStorage.gcs.secret.name:`, specify the name of the Kubernetes secret that contains the GCP service account credentials. |
| ``` artifactStorage:   azure:     container: ""     storageAccountName: ""     secret:       name: "" ``` |  | Azure Blob storage configuration.  Configure these keys when `artifactStorage.storageType: azure"`.  For `artifactStorage.azure.container:`, specify the name of the Azure storage container.  For `artifactStorage.azure.storageAccountName:`, specify the name of the storage account.  For `artifactStorage.azure.secret.name:`, specify the name of the Kubernetes secret that contains `azure_storage_key`. |
| ``` artifactStorage:   minio:     bucket: ""     region: ""     endpoint: ""     secure: false     pathStyle: true     secret:       name: "" ``` |  | MinIO configuration (S3-compatible).  Configure these keys when `artifactStorage.storageType: "minio"`.  For `artifactStorage.minio.bucket:`, specify the name of the storage bucket. Additionally, you can set the `region:` and `endpoint:`.  For `artifactStorage.minio.secret.name:`, specify the name of the Kubernetes secret that contains the minio keys `root-user` and `root-password`. |

## Image pull secrets

| Key | Default value | Description |
| --- | --- | --- |
| ``` imagePullSecrets: ``` | `null` | This Helm key overrides the `global.imagePullSecret:` Helm key for AI Triage Suggestion Service. |

## API deployment

These Helm keys configure the triage-suggestion-service-api service deployment.

| Key | Default value | Description |
| --- | --- | --- |
| ``` deployment:   imageRegistry: ""   image: "triage-suggestion-service-api"   version: "main.latest"   strategy: RollingUpdate   replicaCount: 3  # Production:   serviceAccount: triage-suggestion-service   annotations:     prometheus.io/scrape: "true"     prometheus.io/port: "9090"     prometheus.io/path: "/metrics" ``` |  | `imageRegistry: ""` (empty value) inherits from `global.imageRegistry`.  `replicaCount: 3` This value creates 3 replicas as needed for high availability (HA) in a production environment.# Production: 3 replicas for HA |
| ``` deployment:   environment:     # Service configuration     SERVICE_MODE: "api"     STORAGE_TYPE: "postgres"     QUEUE_TYPE: "rabbitmq"     LOG_LEVEL: "info"     LOG_FORMAT: "json"     HTTP_PORT: "8080"     METRICS_PORT: "9090" ``` |  | API service configuration. |
| ``` deployment:   environment:     # BASE_URL: ``` | `""` | PostgreSQL connection (`POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_DB` set by `postgresEnvVars` helper from `.Values.postgres` or `.Values.global.postgres`  Do NOT hardcode.  `BASE_URL: ""` is an optional public base URL. For example, `https://triage.polaris.blackduck.com`.  If the `BASE_URL: ""` value is empty, `http(s)://localhost:port` will be automatically generated. |
| ``` deployment:   environment:     # TLS/HTTPS configuration (optional)     # TLS_ENABLED: "false"     # TLS_CERT_FILE: "/etc/tls/server.crt"     # TLS_KEY_FILE: "/etc/tls/server.key"     # TLS_CA_FILE: "/etc/tls/ca/ca.crt" ``` |  | - `TLS/HTTPS` - Configuration (optional) - `TLS_ENABLED` - Enable HTTPS (default: false)   - "false" = Disable Enable HTTPS (default: false)   - "true = enable HTTPS - `TLS_CERT_FILE` - Path to TLS certificate file (PEM   format) - `TLS_KEY_FILE` - Path to TLS private key file (PEM format) - `TLS_CA_FILE` - Path to custom CA cert for verifying outgoing   HTTPS requests (optional) |
| ``` deployment:   environment:     # AI/Triage configuration     AI_TRIAGE_ENABLED: "true"     AI_CONFIDENCE_THRESHOLD: "70" ``` |  |  |
| ``` deployment:   environment:     CACHE_ENABLED: "true"     CACHE_TTL_HOURS: "48" ``` |  | Cache configuration |
| ``` deployment:   environment:     RATE_LIMIT_ENABLED: "true"     RATE_LIMIT_REQUESTS_PER_MINUTE: "1000" ``` |  | Rate limiting. |
| ``` deployment:   environment: ``` |  | PostgreSQL connection pool and SSL are configured via `.Values.postgres` and injected by the `postgresEnvVars` template helper.  Do NOT hardcode here. |
| ``` deployment:   environment:     MQ_USER: "triage_user"     MQ_VHOST: "/"     MQ_QUEUE_NAME: "triage-requests" ``` |  | Message Queue configuration (MQ_HOST, MQ_PORT, MQ_PASSWORD injected by template helpers) |
| ``` deployment:   environment:     # ARTIFACT_STORAGE_TYPE: ""      # For GCS:     #   GCS_BUCKET: ""      #   GCS_PROJECT_ID: ""      #   GCS_CREDENTIALS_FILE: ""      # For AWS S3:     #   S3_BUCKET: ""      #   S3_REGION: ""      #   S3_ACCESS_KEY_ID: ""     #   S3_SECRET_ACCESS_KEY: ""     # For Azure:     #   AZURE_STORAGE_ACCOUNT: ""     #   AZURE_STORAGE_CONTAINER: ""     #   AZURE_STORAGE_KEY: "" ``` |  | Artifact storage configuration (set by deployment pipeline)   - `ARTIFACT_STORAGE_TYPE` - Set by deployment pipeline: "gcs",   "s3", or "azure". - `GCS_BUCKET` - GCS bucket name. - `GCS_PROJECT_ID`  - GCP project ID. - `GCS_CREDENTIALS_FILE`  - Optional: service account key path   (or use Workload Identity). - `S3_BUCKET` - S3 bucket name. - `S3_REGION` - AWS region. - `S3_ACCESS_KEY_ID` - Optional: AWS access key (or use IAM   role). - `S3_SECRET_ACCESS_KEY` - Optional: AWS secret key (or use IAM   role). - `AZURE_STORAGE_ACCOUNT` - Azure storage account name. - `AZURE_STORAGE_CONTAINER` - Azure blob container name. - `AZURE_STORAGE_KEY` - Optional: storage account key (or use   Managed Identity). |
| ``` deployment:   environment:     UPLOAD_URL_EXPIRATION: "1h"     ARTIFACT_MAX_SIZE: "209715200"  # 200MB for production ``` |  | `ARTIFACT_MAX_SIZE` is 200MB for production environments. |
| ``` deployment:   environment:     # Observability     OBSERVABILITY_EXPOSEMETRICS: "true"     OBSERVABILITY_TELEMETRY_URL: "" ``` |  |  |
| ``` deployment:   environment:     VAULT_AUTH_METHOD: "kubernetes"     VAULT_AUTH_KUBERNETES_ROLE: "triage-suggestion-service"     VAULT_DBSECRETPATH: "database/creds/triage-suggestion-service" ``` | `"kubernetes"``"triage-suggestion-service"``"database/creds/triage-suggestion-service"` | Vault configuration. |
| ``` deployment:   autoscaling:     enabled: true ``` |  | Autoscaling  If `hpa.enabled: true`, the replicas field is omitted. |
| ``` deployment:   envVarsFromSecret: {} ``` |  |  |
| ``` deployment:   resources:     requests:       cpu: "500m"       memory: "512Mi"     limits:       cpu: "2000m"       memory: "2Gi" ``` |  |  |
| ``` deployment:   livenessProbe:     httpGet:       path: /liveness       port: 8080     initialDelaySeconds: 30     periodSeconds: 10     timeoutSeconds: 5     failureThreshold: 3 ``` |  |  |
| ``` deployment:   readinessProbe:     httpGet:       path: /readiness       port: 8080     initialDelaySeconds: 10     periodSeconds: 5     timeoutSeconds: 3     failureThreshold: 3 ``` |  |  |

## Worker deployment

| Key | Default value | Description |
| --- | --- | --- |
| ``` workerDeployment:   imageRegistry: ""  # Inherits from global.imageRegistry when empty   image: "triage-suggestion-service-worker"   version: "main.latest"   strategy: RollingUpdate   replicaCount: 5  # Production: 5 workers for processing capacity   serviceAccount: triage-suggestion-service ``` |  |  |
| ``` workerDeployment:   annotations:     prometheus.io/scrape: "true"     prometheus.io/port: "9090"     prometheus.io/path: "/metrics" ``` |  |  |
| ``` workerDeployment:   environment:     # Service configuration     SERVICE_MODE: "worker"     STORAGE_TYPE: "postgres"     QUEUE_TYPE: "rabbitmq"     LOG_LEVEL: "info"     LOG_FORMAT: "json"     METRICS_PORT: "9090" ``` |  |  |
| ``` workerDeployment:   environment:     # PostgreSQL connection (POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB set by postgresEnvVars helper     # from .Values.postgres or .Values.global.postgres — do NOT hardcode here) ``` |  |  |
| ``` workerDeployment:   environment:     # AI/Triage configuration     AI_TRIAGE_ENABLED: "true"     AI_CONFIDENCE_THRESHOLD: "70" ``` |  |  |
| ``` workerDeployment:   environment:     # CLI configuration     CLI_PATH: "/opt/cov-triage-issue/bin/cov-triage-issue"     CLI_TIMEOUT: "600s"  # 10 minutes for complex analysis     MAX_CONCURRENT_CLI: "10" ``` |  |  |
| ``` workerDeployment:   environment:     # Worker configuration     # IMPORTANT: WORKER_COUNT must be 1 for data separation     # Each pod processes only one request at a time to ensure customer data isolation     # Scale horizontally by increasing replicaCount instead of WORKER_COUNT     WORKER_COUNT: "1"     WORK_DIRS: "/tmp/workdirs"     RESULTS_DIR: ""  # Defaults to workdirs/$scanId/results/     CLEANUP_WORK_DIRS: "true"  # Clean up after processing ``` |  |  |
| ``` workerDeployment:   environment:     # Storage retention configuration     CLEANUP_INTERVAL: "5m"     REQUEST_RETENTION: "24h"     RESULTS_RETENTION: "6h"     ARTIFACT_RETENTION: "6h"     ARTIFACT_STORAGE_PATH: "/tmp/artifacts" ``` |  |  |
| ``` workerDeployment:   environment:     # Cache configuration     CACHE_ENABLED: "true"     CACHE_TTL_HOURS: "48" ``` |  |  |
| ``` workerDeployment:   environment:     # About PostgreSQL ``` |  | PostgreSQL connection pool and SSL are configured via `.Values.postgres` and injected by the `postgresEnvVars` template helper Do NOT hardcode here. |
| ``` workerDeployment:   environment:     MQ_USER: "triage_user"     MQ_VHOST: "/"     MQ_QUEUE_NAME: "triage-requests"     MQ_WORKER_CONCURRENCY: "1" ``` |  | - # Message Queue configuration. `MQ_HOST`,   `MQ_PORT`, and `MQ_PASSWORD` are injected by   template helpers. - `MQ_WORKER_CONCURRENCY` - IMPORTANT: Must be 1 for data   separation - only one message per pod at a time |
| ``` workerDeployment:   environment:     # Artifact storage configuration (set by deployment pipeline)     # ARTIFACT_STORAGE_TYPE: ""  # Set by deployment pipeline: "gcs", "s3", or "azure"     # Cloud storage credentials/config set by deployment pipeline. ``` |  | Artifact storage configuration, set by deployment pipeline.   - `ARTIFACT_STORAGE_TYPE` - "gcs", "s3", or "azure" Cloud storage   credentials/config, set by deployment pipeline. |
| ``` workerDeployment:   environment:     # Observability     OBSERVABILITY_EXPOSEMETRICS: "true"     OBSERVABILITY_TELEMETRY_URL: "" ``` |  |  |
| ``` workerDeployment:   environment:     # LLM configuration ``` |  | (LLM_URL, LLM_NAME, LLM_API_KEY_FILE injected by llmEnvVars helper from .Values.llm) # Do NOT hardcode LLM_URL or LLM_API_KEY_FILE here — set .Values.llm.url and .Values.llm.apiKey instead. |
| ``` workerDeployment:   environment:     VAULT_AUTH_METHOD: "kubernetes"     VAULT_AUTH_KUBERNETES_ROLE: "triage-suggestion-service"     VAULT_DBSECRETPATH: "database/creds/triage-suggestion-service" ``` |  | Vault configuration. |
| ``` workerDeployment:   autoscaling:     enabled: ``` | `true` | Autoscaling (when enabled with workerHpa.enabled, replicas field is omitted). |
| ``` workerDeployment:   envVarsFromSecret: {} ``` |  |  |
| ``` workerDeployment:   resources:     requests:       cpu: "1000m"       memory: "2Gi"     limits:       cpu: "4000m"       memory: "8Gi" ``` |  | Workers need more memory for CLI execution. |

## Service accounts

| Key | Default value | Description |
| --- | --- | --- |
| ``` serviceAccounts: - name: triage-suggestion-service - name: triage-suggestion-service-admin ``` |  |  |

## Security

| Key | Default value | Description |
| --- | --- | --- |
| ``` securityContext:   enabled: true   runAsUser: 5000   runAsGroup: 5000   fsGroup: 5000 ``` |  |  |

## Autoscaling

| Key | Default value | Description |
| --- | --- | --- |
| ``` hpa:   enabled: true   minReplicas: 3   maxReplicas: 10   targetCPUUtilizationPercentage: 70   targetMemoryUtilizationPercentage: 80 ``` | Enabled by default. | Horizontal Pod Autoscaler (HPA) |
| ``` workerHpa:   enabled: true   minReplicas: 5   maxReplicas: 20   targetCPUUtilizationPercentage: 80   # queueDepthMetric:   #   name: rabbitmq_queue_messages_ready   #   queue: triage-requests   #   targetAverageValue: "30" ``` | Enabled by default. | Worker Horizontal Pod Autoscaler (HPA)  `queueDepthMetric:`  Queue-based scaling (requires prometheus-adapter or KEDA). Uncomment when metrics adapter is configured. |

## Database

| Key | Default value | Description |
| --- | --- | --- |
| ``` postgres:   enabled: false   host: ""   port: "5432"   user: ""   password: ""   database: "triage-suggestion-service"   sslmode: ""   sslRootCert: "/opt/postgresql/ssl/postgres-root.pem"   maxOpenConns: "50"   maxIdleConns: "25"   connMaxLifetime: "600s"   existingSecret: "" ``` |  | If `postgres.enabled: false`, Postgres uses external Cloud SQL.  If `postgres.enabled: true` and `host:`, `port:`, `user:`, and `password:` are set, the corresponding `POSTGRES_*` environment variables are injected via the `postgresEnvVars` helper, overriding defaults in the deployment.environment.  For `existingSecret:`, use a pre-existing Kubernetes Secret for PostgreSQL credentials (keys: host, port, username, password). |
| ``` vault:   enabled: ``` | `false` | Vault integration (for dynamic database credentials) |

## Ingress

| Key | Default value | Description |
| --- | --- | --- |
| ``` ingress:   triage-suggestion-service-ingress:     enabled: ``` | `true` |  |
| ``` ingress:   triage-suggestion-service-ingress:     className: ``` | `""` |  |
| ``` ingress:   triage-suggestion-service-ingress:     annotations: ``` | `{}` |  |
| ``` ingress:   triage-suggestion-service-ingress:     tls:       host: ""       secretName: "" ``` |  |  |
| ``` ingress:   triage-suggestion-service-ingress:     rules:       paths:       - path: "/"         serviceName: "triage-suggestion-service-api"         servicePort: 8080 ``` |  |  |

## Monitoring and alerting

These Helm keys enable and configure Prometheus monitoring and alerting of the status of
the AI-Assisted Triage Plug-in environment.

| Key | Default value | Description |
| --- | --- | --- |
| ``` monitoring:   serviceMonitor:     enabled: false     interval: 30s     scrapeTimeout: 10s     additionalLabels: {} ``` |  | These Helm keys enable Prometheus monitoring and set monitoring intervals. |
| ``` monitoring:   prometheusRules:     enabled: ``` | `false` | Use this Helm key to enable the Prometheus rules defined in the following Helm key:   ``` monitoring   prometheusRules:     rules: ``` |
| ``` monitoring:   prometheusRules:     additionalLabels: ``` | `{}` |  |
| ``` monitoring:   prometheusRules:     rules:       - alert: HighAPIErrorRate         expr: |           rate(http_requests_total{status=~"5.."}[5m]) /           rate(http_requests_total[5m]) > 0.05         for: 5m         labels:           severity: warning         annotations:           summary: "API error rate > 5%"        - alert: APIHighLatency         expr: |           histogram_quantile(0.95,             rate(http_request_duration_seconds_bucket[5m])           ) > 2         for: 5m         labels:           severity: warning         annotations:           summary: "API p95 latency > 2s"        - alert: RabbitMQQueueBacklog         expr: rabbitmq_queue_messages_ready{queue="triage-requests"} > 500         for: 10m         labels:           severity: warning         annotations:           summary: "RabbitMQ backlog > 500 messages"        - alert: HighWorkerFailureRate         expr: |           rate(worker_jobs_failed_total[5m]) /           rate(worker_jobs_processed_total[5m]) > 0.1         for: 10m         labels:           severity: warning         annotations:           summary: "Worker failure rate > 10%" ``` |  | These Helm keys define Prometheus rules and messages that are reported for a few AI-Assisted Triage Plug-in environment conditions.  The annotations define messages returned.  To enable these rules, set:   ``` monitoring   prometheusRules:     rules: true ``` |

## Network policies

| Key | Default value | Description |
| --- | --- | --- |
| ``` networkPolicy:   enabled: false    api:     ingress:       - from:         - namespaceSelector:             matchLabels:               name: ingress-nginx         ports:         - protocol: TCP           port: 8080       - from:         - namespaceSelector:             matchLabels:               name: monitoring         ports:         - protocol: TCP           port: 9090     egress:       - to:         - namespaceSelector: {}         ports:         - protocol: TCP           port: 5432       - to:         - namespaceSelector: {}         ports:         - protocol: TCP           port: 5672       - to:         - namespaceSelector: {}         ports:         - protocol: UDP           port: 53       - to:         ports:         - protocol: TCP           port: 443    worker:     egress:       - to:         - namespaceSelector: {}         ports:         - protocol: TCP           port: 5432       - to:         - namespaceSelector: {}         ports:         - protocol: TCP           port: 5672       - to:         - namespaceSelector: {}         ports:         - protocol: UDP           port: 53       - to:         ports:         - protocol: TCP           port: 443 ``` |  |  |
| ``` networkPolicy:   enabled: false ``` |  |  |
| ``` networkPolicy:   api:     ingress:       - from:         - namespaceSelector:             matchLabels:               name: ingress-nginx         ports:         - protocol: TCP           port: 8080       - from:         - namespaceSelector:             matchLabels:               name: monitoring         ports:         - protocol: TCP           port: 9090 ``` |  |  |
| ``` networkPolicy:     egress:       - to:         - namespaceSelector: {}         ports:         - protocol: TCP           port: 5432       - to:         - namespaceSelector: {}         ports:         - protocol: TCP           port: 5672       - to:         - namespaceSelector: {}         ports:         - protocol: UDP           port: 53       - to:         ports:         - protocol: TCP           port: 443 ``` |  |  |
| ``` networkPolicy:   worker:     egress:       - to:         - namespaceSelector: {}         ports:         - protocol: TCP           port: 5432       - to:         - namespaceSelector: {}         ports:         - protocol: TCP           port: 5672       - to:         - namespaceSelector: {}         ports:         - protocol: UDP           port: 53       - to:         ports:         - protocol: TCP           port: 443 ``` |  |  |

## Pod disruption budget

| Key | Default value | Description |
| --- | --- | --- |
| ``` podDisruptionBudget:   api:     enabled: false     minAvailable: 2 ``` |  |  |
| ``` podDisruptionBudget:   worker:     enabled: false     minAvailable: 3 ``` |  |  |

## RabbitMQ

RabbitMQ is an open‑source message broker used to send, route, store and receive messages.
RabbitMQ is a bundled subchart that you enable by setting `rabbitmq.enabled:
true` within this `triage-suggestion-service` subchart.

| Key | Default value | Description |
| --- | --- | --- |
| ``` rabbitmq:   enabled: false ``` |  | - `false` - Disables the bundled RabbitMQ subchart. If you are   using an externally-managed instance of RabbitMQ, Disable this and configure   externalRabbitmq when using a managed/external RabbitMQ. - `true` - Enables RabbitMQ. When enabled, deploys a RabbitMQ   instance as a subchart dependency. |
| ``` rabbitmq:   fullnameOverride: ``` | `"triage-rabbitmq"` | The RabbitMQ instance name. |
| ``` rabbitmq:   global:     imageRegistry: "" ``` | `""` If empty, inherits the value from `global.imageRegistry`. | `allowInsecureImages` is inherited from the parent chart's `global.security.allowInsecureImages` Helm key, or can be set using the option:   ``` --set global.security.allowInsecureImages=true ``` |
| ``` rabbitmq:   auth:     username: triage_user     password: ""     erlangCookie: "" ``` |  | The `password`, if empty, is automatically generated by the Bitnami chart. |
| ``` rabbitmq:   persistence:     enabled: true     size: 8Gi ``` |  |  |
| ``` rabbitmq:   replicaCount: 1 ``` |  |  |
| ``` rabbitmq:   resources:     requests:       cpu: 100m       memory: 512Mi     limits:       cpu: 1000m       memory: 1Gi ``` |  |  |

## External RabbitMQ Helm keys

Configure the following Helm keys if you are using an external or managed instance of
RabbitMQ instead of the rabbitMQ subchart bundled within the
`triage-suggestion-service` subchart. To use external RabbitMQ, the
bundled RabbitMQ must be disabled with `rabbitmq.enabled: false`. You also
need to specify the external host and port as well as create and specify secrets for
access.

| Key | Default value | Description |
| --- | --- | --- |
| ``` externalRabbitmq:   host: ``` | `"rabbitmq.rabbitmq.svc.cluster.local"` |  |
| ``` externalRabbitmq:   port: ``` | `5672` |  |
| ``` externalRabbitmq:   existingSecret: ``` | `"triage-suggestion-service-secrets"` |  |
| ``` externalRabbitmq:   existingSecretKey: ``` | `"rabbitmq-password"` |  |
