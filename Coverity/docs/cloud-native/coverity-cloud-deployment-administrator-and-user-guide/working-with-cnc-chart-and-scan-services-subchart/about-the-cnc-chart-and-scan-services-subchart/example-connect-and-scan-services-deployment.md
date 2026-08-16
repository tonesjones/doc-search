---
title: "Example: Connect and Scan Services deployment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/example-connect-and-scan-services-deployment.html"
content_id: "FRXOEj~xCAUAVRI95qAHAQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:17.435032+00:00"
---

# Example: Connect and Scan Services deployment

To set a Helm `<key>=: <value>` property in the scan-services
subchart, you can set the `<key>=: <value>` in the scan-services
`values.yaml` file, a custom yaml file, or in the `helm
install` command using `--set` commands.

The following example illustrates a full deployment, with override values for
`cnc` and `scan-services` charts provided within one file.
This example file includes `global`, `cim`, and
`scan-services` values:

```
global:
  imageRegistry: "gcr.io/coverity-cloud-sandbox-dev"
  imagePullPolicy: "Always"
  postgres:
    host: "cim-pg-postgresql"
    password: "postgres"
    port: 5432
    user: "postgres"
    sslmode: "verify-ca"
  redis:
    host: cache-redis-master
    verifyHostName: false
    secure: true
    port: 6379
  trust-stores:
    enabled: true
  ingress:
    enabled: true
    annotations: {}
    hosts:
      - local.connect.example.com
    tls:
      - secretName: "cnc-cim-tls-nginx"
        hosts:
          - local.connect.example.com
cim:
  cimweb:
    keystore:
      enabled: true
    javaOpts: "-javaagent:/coverity/otel/opentelemetry-javaagent.jar -Dotel.metrics.exporter=none 
               -Dotel.service.name=connect -Dotel.traces.exporter=jaeger 
               -Dotel.exporter.jaeger.endpoint=http://my-hunter-jaeger-collector.metrics.svc.cluster.local:14250"
    extraVolumes:
      - name: otel-agent
        emptyDir: {}
    extraVolumeMounts:
      - name: otel-agent
        mountPath: /coverity/otel
    initContainers:
      - name: otel-agent
        command: ["sh", "-c", "cp -r /otel/opentelemetry-javaagent.jar /cimweb/opentelemetry-javaagent.jar"]
        image: "gcr.io/coverity-cloud-sandbox-dev/public/open-telemetry/java-agent:1.20.2"
        volumeMounts:
          - name: otel-agent
            mountPath: /cimweb
    updateLicense:
        enabled: true
        force: true
    loadBalancer:
      trustedRegex: ".*"
  setupJob:
    activeDeadlineSeconds: 240
  postgres:
    database: "cim"
scan-services:
  enabled: true
  scan-service:
    observability:
      jaegerURL: "http://my-hunter-jaeger-collector.metrics.svc.cluster.local:14268/api/traces"
    postgres:
      database: "cim-scan"
    environment:
      CUSTOMNODEPOOL_CPU: 1000
      CUSTOMNODEPOOL_MEM: 500
  storage-service:
    observability:
      jaegerURL: "http://my-hunter-jaeger-collector.metrics.svc.cluster.local:14268/api/traces"
    storageType: minio
    minio:
      region: "us-east-1"
    endpoint:
      internal:
        url: "http://cnc-minio:9000"
      external:
        url: "https://local.connect.example.com"
        proxyPath: "upload"
    postgres:
      database: "cim-storage"
  cache-service:
    javaOpts: "-javaagent:/coverity/otel/opentelemetry-javaagent.jar -Dotel.metrics.exporter=none 
               -Dotel.service.name=cache-service -Dotel.traces.exporter=jaeger 
               -Dotel.exporter.jaeger.endpoint=http://my-hunter-jaeger-collector.metrics.svc.cluster.local:14250"
    storageProvider: "minio"
    extraVolumes:
      - name: otel-agent
        emptyDir: {}
    extraVolumeMounts:
      - name: otel-agent
        mountPath: /coverity/otel
    initContainers:
      - name: otel-agent
        command: ["sh", "-c", "cp -r /otel/opentelemetry-javaagent.jar /cache/opentelemetry-javaagent.jar"]
        image: "gcr.io/coverity-cloud-sandbox-dev/public/open-telemetry/java-agent:1.20.2"
        volumeMounts:
          - name: otel-agent
            mountPath: /cache
    minio:
      host: cnc-minio
      secure: false
      verifyHostName: false
    redis:
      verifyHostName: false
```

Important:

The scan services subchart Helm keys are all prepended with `scan-services`
to identify them as `scan-services` subchart values.

Note: The `scan-services.enabled:` Helm key, whose value
determines whether or not the `scan-services` subchart is deployed, is located
within the `cnc` chart.

Alternatively, you can deploy Connect and scan-services in Kubernetes using a `helm
install` command with `--set` commands to provide overrides.
For example:

```
helm install "$CNC_APP_NAME" "${CNC_CHART_LOCATION:-"../../charts/cnc"}" \
  -f values.yaml  \
  --wait \
  --timeout 60m0s \
  --debug \
  --namespace "$CNC_NS" \
  --set global.imagePullSecret="$CNC_IMAGE_PULL_SECRET" \
  --set imagePullSecret="$CNC_IMAGE_PULL_SECRET" \
  --set global.postgres.host="${CNC_PGHOST}" \
  --set global.postgres.user="${CNC_PGUSER}" \ 
  --set global.postgres.password="${CNC_PGPASSWORD}" \
  --set global.licenseSecretName="${CNC_LICENSE_SECRET_NAME}" \
  --set global.trust-stores.configmapName="$CNC_TRUST_STORES_CONFIGMAP_NAME" \
  --set cim.cimweb.exposeCommitPort="${EXPOSE_COMMIT_PORT}" \
  --set cim.cimweb.keystore.certificateSecret="${CNC_CERT_SECRET}" \
  --set cim.cimweb.webUrl="https://${HOST_ADDRESS}" \
  --set cim.cimweb.replicas="${CNC_CIM_REPLICAS:-1}" \
  --set cim.postgres.database="${CNC_CIM_DATABASE}" \
  --set scan-services.enabled="${SCANFARM_ENABLED}" \
  --set scan-services.storage-service.minio.bucket="${CNC_NS}-uploads-bucket" \
  --set scan-services.cache-service.bucketName="${CACHE_BUCKET_NAME}" \
  --set scan-services.cache-service.enabled="${ENABLE_CACHE_SERVICE}" \
  --set scan-services.storage-service.minio.secret.name="$CNC_MINIO_SECRET_NAME" \
  --set scan-services.cache-service.minio.secret="${CNC_MINIO_SECRET_NAME}" \
  --set global.redis.passwordSecret="${REDIS_PASSWORD_SECRET_NAME}" \
  --set global.redis.cacertSecret="${REDIS_CERTS_SECRET}" \
  --set global.redis.authEnabled="${REDIS_AUTH_ENABLED}" \
  --set scan-services.scan-service.environment.CUSTOMNODEPOOL_LABEL="${CNC_SCAN_FARM_NODE_LABEL}" \
  --set scan-services.scan-service.environment.COVANALYSIS_DEFAULTPOOLTYPE="${CNC_SCAN_FARM_NODE_LABEL}" \
  --set scan-services.scan-service.api.pagination.limit="${SCAN_SVC_LIST_SCAN_PAGINATION_LIMIT}" \
  "$@"
```

Note:

The following options help you manage the installation:

- `--wait` tells Helm to wait until all resources are fully deployed and in
  a ready state before considering the installation successful.
- `--timeout` specifies the maximum amount of time to wait for the
  installation process to complete.
- `--debug` enables debug output during the installation process.
