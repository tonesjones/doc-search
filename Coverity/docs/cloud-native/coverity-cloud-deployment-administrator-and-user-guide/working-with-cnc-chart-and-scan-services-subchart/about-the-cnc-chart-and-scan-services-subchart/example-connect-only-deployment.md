---
title: "Example: Connect-only deployment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/example-connect-only-deployment.html"
content_id: "JL~BAn_QTmbREwmEf8IZXQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:16.783650+00:00"
---

# Example: Connect-only deployment

The following example uses the cnc Helm chart to deploy only Coverity Connect in
Kubernetes, without deploying scan-services.

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
scan-services:
  enabled: false
```

Alternatively, you can deploy Connect in Kubernetes using a `helm install`
command with `--set` commands to provide overrides. For example:

```
helm install "$CNC_APP_NAME" "${CNC_CHART_LOCATION:-"../../charts/cnc"}" \
  -f values.yaml \
  --wait \
  --timeout 60m0s \
  --debug \
  --namespace "$CNC_NS" \
  --set global.postgres.password="${CNC_PGPASSWORD}" \
  --set global.postgres.host="${CNC_PGHOST}" \  
  --set global.postgres.user="${CNC_PGUSER}" \
  --set cim.postgres.database="${CNC_CIM_DATABASE}" \
  --set global.licenseSecretName="${CNC_LICENSE_SECRET_NAME}" \
  --set global.redis.passwordSecret="${REDIS_PASSWORD_SECRET_NAME}" \
  --set global.redis.cacertSecret="${REDIS_CERTS_SECRET}" \
  --set global.redis.authEnabled="${REDIS_AUTH_ENABLED}" \
  --set global.imagePullSecret="$CNC_IMAGE_PULL_SECRET" \
  --set cim.cimweb.keystore.certificateSecret="${CNC_CERT_SECRET}" \
  --set cim.cimweb.webUrl="https://${HOST_ADDRESS}" \
  --set cim.cimweb.replicas="${CNC_CIM_REPLICAS:-1}" \
  --set global.trust-stores.configmapName="$CNC_TRUST_STORES_CONFIGMAP_NAME" \
  --set scan-services.enabled=${SCANFARM_ENABLED}"
```
