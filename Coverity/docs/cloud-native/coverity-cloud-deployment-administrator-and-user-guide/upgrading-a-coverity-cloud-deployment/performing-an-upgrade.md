---
title: "Performing an upgrade"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/performing-an-upgrade.html"
content_id: "k9pWed788vw6Coi15IjtdQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:25.947194+00:00"
---

# Performing an upgrade

The following sample Helm command upgrades a Coverity Connect instance.

```
helm upgrade "${CNC_APP_NAME}" \
  -n "${NS}"
  --install \
  --version "${VERSION}" \
  --repo "${REPOSITORY}" \
  --wait \
  --timeout 60ms
```

where:

- `"${NS}"` is the Connect namespace, for example, "cim".
- `"${VERSION}"` is the new Coverity version.
- `"${REPOSITORY}"` is the repository that contains the downloaded
  container images.
- Add overrides for any values which need to be changed from the previous
  installation or upgrade. You can create a yaml file containing the
  overrides.

## Consideration: Upgrading to 2026.3.0 or newer

The 2026.3.0 release introduces a new feature, AI-Assisted Triage Plug-in. If you
upgrade to a 2026.3 or newer Helm chart from a 2025.12.x or older Helm chart,you
need to consider the following when forming your upgrade command.

The `--reuse-values` option reuses stored release values and can
unintentionally enable AI-Assisted Triage Plug-in even though the new chart default
value might disable this service. This is normal Helm behavior. To avoid enabling
the AI-Assisted Triage Plug-in feature when it is configured as disabled,
either:

Important: When upgrading from a 2025.12 or older
release, do **not** use the `--reuse-values` option if AI-Assisted
Triage Plug-in will remain disabled.

Important: If AI-Assisted Triage Plug-in service is
not used and will remain disabled, we recommend that you explicitly set
`triage-suggestion-service.enabled=false` during the
upgrade.

- Use `--reset-then-reuse-values` to ensure that the new chart
  default values are applied correctly. Here is a suggested command to use for
  an upgrade if you need to disable AI-Assisted Triage Plug-in:

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
