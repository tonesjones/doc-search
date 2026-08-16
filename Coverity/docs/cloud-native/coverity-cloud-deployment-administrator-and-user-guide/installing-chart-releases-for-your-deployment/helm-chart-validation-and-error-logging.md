---
title: "Helm chart validation and error logging"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/helm-chart-validation-and-error-logging.html"
content_id: "kXL3tK1ymZwK5zx3CRPmDw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:36.198642+00:00"
---

# Helm chart validation and error logging

During a `helm install`, Helm chart validation verifies that all required
minimum Helm values are set. This makes sure that the Helm chart satisfies the minimum
Helm key value requirements. If a value is missing, an error message is returned to the
commmand line, indicating the Helm key value that must be set. This will help you verify
that required Helm values are set before proceeding to install the chart.

Helm chart validation helps you identify Helm overrides that can cause deployment issues.
Helm chart validation fails an invalid deployment and logs an error message for each
invalid Helm value found. This message(s) help you verify Helm overrides and update
missing Helm values.

To debug and return errors for invalid Yaml, add the `--debug` option to
the `helm install` command and run the command. For example:

```
helm install "$cnc_app_name" "{$cnc_chart_location: -"../../charts/cnc"}" \
--wait \
--timeout 60m0s \
--debug \
--namespace "$CNC_NS" \
--set global.postgres.host="${CNC_PGHOST}" \
...
```

The following example indicates that in the `cnc` chart
`values.yaml` file, the `cim.cimweb.weburl` key needs
a valid value:

[image: image]

The following example indicates that in the `cnc` chart
`values.yaml` file, the `cim.postgres.database` key
needs a valid value:

[image: image]
