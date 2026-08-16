---
title: "Configuration parameters"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuration-parameters.html"
content_id: "WApkyZM0_1Bbc9txTDdjnw"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:03.635624+00:00"
---

# Configuration parameters

The following tables list the configurable parameters of the Black Duck chart and their
default values.

- Common configuration
- Authentication pod
- Binary scanner pod
- BOM engine pod
- CFSSL pod
- Integration pod
- Job runner pod
- Logstash pod
- Match engine pod
- PostgreSQL pod
- PostgreSQL
  readiness init container
- PostgreSQL upgrade
  job
- RabbitMQ pod
- Redis pod
- Registration pod
- Scan pod
- Storage pod
- Webapp pod
- Webserver pod

Note: Do not set the following parameters in the environs flag. Instead, use their
respective flags.

```
Use dataRetentionInDays, enableSourceCodeUpload and maxTotalSourceSizeinMB for the following:
* DATA_RETENTION_IN_DAYS
* ENABLE_SOURCE_UPLOADS
* MAX_TOTAL_SOURCE_SIZE_MB

Use enableAlert, alertName and alertNamespace for the following:
* USE_ALERT
* HUB_ALERT_HOST
* HUB_ALERT_PORT

Use exposedNodePort and exposedServiceType for the following:
* PUBLIC_HUB_WEBSERVER_PORT

Use postgres.isExternal and postgres.ssl for the following:
* HUB_POSTGRES_ENABLE_SSL
* HUB_POSTGRES_ENABLE_SSL_CERT_AUTH

Use enableIPV6 for the following:
* IPV4_ONLY
```
