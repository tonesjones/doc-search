---
title: "Setting global Helm key values"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-global-helm-key-values.html"
content_id: "O6FFFpC40GxPTKmf~jBVig"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:15.489394+00:00"
---

# Setting global Helm key values

In Coverity cloud, global Helm keys are global values that are used by both the parent
`cnc` chart and its `scan-services` subchart. The
following Helm keys are global. values that can be accessed from the
`cnc` chart and the `scan-services` subchart.

We recommend that you configure the global key values to pass values to any subchart as
well as the top level chart.

Global Helm keys appear in both the `cnc` chart and the
`scan-services` subchart. Overriding any of these values applies to
both charts. See <https://helm.sh/docs/chart_template_guide/subcharts_and_globals/#global-chart-values>.

Important: Provide global Helm keys in any custom
`.yaml` file or Helm command using the global syntax specified in the
Helm chart.

Important: The methods of setting Helm keys is true for
all Helm keys, whether global or not.

You can override global Helm key values as you would override any other Helm key value.
Either:

- Create and pass a custom `.yaml` file that contains the needed
  global Helm key override values,. For example:

  ```
  global:
    imageRegistry: "gcr.io/example"
    imagePullPolicy: "Always"
    postgres:
      host: "pg-postgresql"
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
        - example.com
      tls:
        - secretName: "tls-nginx"
          hosts:
            - example.com
  ```
- Use `--set` options in a `helm install` command.
  For example:

  ```
  helm install "$CNC_APP_NAME" "${CNC_CHART_LOCATION:-"../../charts/cnc"}" \
    -f values.yaml \
    --wait \
    --timeout 60m0s \
    --debug \
    --namespace "$CNC_NS" \
    --set global.postgres.password="${CNC_PGPASSWORD}" \
    --set global.postgres.host="${CNC_PGHOST}" \
    --set "global.licenseSecretName=${CNC_LICENSE_SECRET_NAME}" \
    --set global.redis.passwordSecret="${REDIS_PASSWORD_SECRET_NAME}" \
  ```

In the `cnc` chart and `scan-services` subchart, you will
also find Helm keys that can be used to override global Helm keys for specific services.
If you set different values in both a global Helm key and the equivalent key for a
service, the service key value takes precedence for that service and overrides the
global key value for that service. The global value can still apply to other
services.
