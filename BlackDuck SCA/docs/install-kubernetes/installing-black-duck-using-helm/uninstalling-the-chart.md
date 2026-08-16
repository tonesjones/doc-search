---
title: "Uninstalling the chart"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/uninstalling-the-chart.html"
content_id: "HqCuRC27Vwnd7~bO9YCHHg"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:02.527042+00:00"
---

# Uninstalling the chart

To uninstall/delete the deployment:

```
$ helm uninstall ${BD_NAME} --namespace ${BD_NAME}
```

The command removes all the Kubernetes components associated with the chart
and deletes the release.

If you have used `kubectl` to install from a dry-run as shown above, the
following command will remove the install:

```
$ kubectl delete -f ${BD_NAME}.yaml
```
