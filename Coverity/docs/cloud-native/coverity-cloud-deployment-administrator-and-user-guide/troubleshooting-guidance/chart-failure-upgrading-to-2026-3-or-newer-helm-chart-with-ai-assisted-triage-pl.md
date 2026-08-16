---
title: "Chart failure upgrading to 2026.3 or newer Helm chart with AI-Assisted Triage Plug-in enabled"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/chart-failure-upgrading-to-2026.3-or-newer-helm-chart-with-ai-assisted-triage-plug-in-enabled.html"
content_id: "izlM5wwBqswGw9sS78EySg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:38.136210+00:00"
---

# Chart failure upgrading to 2026.3 or newer Helm chart with AI-Assisted Triage Plug-in enabled

If you upgrade from 2025.12 or older to a 2026.3 or newer Helm chart, with AI-Assisted
Triage Plug-in enabled, using the `helm upgrade --reuse-values` command,
the Helm upgrade might fail with the following error:

```
Error: UPGRADE FAILED: execution error at (cnc/charts/triage-suggestion-service/charts/rabbitmq/templates/statefulset.yaml:39:28):
PASSWORDS ERROR: You must provide your current passwords when upgrading the release.
                 Note that even after reinstallation, old credentials may be needed as they may be kept in persistent volume claims.
                 Further information can be obtained at https://docs.bitnami.com/general/how-to/troubleshoot-helm-chart-issues/#credential-errors-while-upgrading-chart-releases
    'auth.password' must not be empty, please add '--set auth.password=$RABBITMQ_PASSWORD' to the command. To get the current value:
        export RABBITMQ_PASSWORD=$(kubectl get secret --namespace "cnc" triage-rabbitmq -o jsonpath="{.data.rabbitmq-password}" | base64 -d)
Troubleshoot Bitnami Helm chart issues
```

Important: When upgrading from a 2025.12 or older release,
do **not** use the `--reuse-values` option if AI-Assisted Triage
Plug-in will remain disabled (`triage-suggestion-service.enabled=false`).
See the subsection below.

If you encounter this error, to resolve it, either:

- Disable RabbitMQ, perform the upgrade, then re-enable RabbitMQ. You can enable it
  in the `cnc` chart `values.yaml` file.
- Keep RabbitMQ enabled and hardcode either the `password` or the
  `passwordSecretName`. For example:

  ```
  rabbitmq:
   enabled: true
   auth:
     password: "p@$$w0rd" 
     existingPasswordSecret: "<passwordSecretName>"
  ```

  If RabbitMQ is enabled and you do not set the password, the upgrade will fail and
  return the error described above.

Note: Do not load RabbitMQ unless the
`triage-suggestion-service` is loaded. When the
`triage-suggestion-service` is loaded, RabbitMQ must be
enabled.

## Using the --reset-then-reuse-values option

The `--reuse-values` option reuses stored release values and can
unintentionally enable AI-Assisted Triage Plug-in even though the new chart default
value might disable this service. This is normal Helm behavior. To avoid enabling
the AI-Assisted Triage Plug-in feature when it is configured as disabled,
either:

Important: If AI-Assisted Triage Plug-in service is
not used and must remain disabled, we recommend that you explicitly set
`triage-suggestion-service.enabled=false` during the
upgrade.

- Use `--reset-then-reuse-values` to ensure that the new chart
  default values are applied correctly. We suggest that you use the following
  command to upgrade with AI-Assisted Triage Plug-in disabled:

  ```
  helm upgrade -n <namespace> <release> <chart> --reset-then-reuse-values --debug
  ```

  Note: Using the `--reset-then-reuse-values`
  option does the following: applies the new chart defaults > overlays
  existing release values > applies command-line or file overrides. This
  preserves environment-specific overrides while respecting new chart
  defaults, including keeping optional components disabled unless
  enabled.
- Export, review, and clean existing release values before upgrading.
