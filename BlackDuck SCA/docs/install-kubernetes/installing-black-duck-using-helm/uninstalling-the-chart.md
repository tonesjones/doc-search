---
title: "Uninstalling the chart"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/uninstalling-the-chart.html"
content_id: "sH5aWKOxP5jfACzZvVpU6g"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:22.616082+00:00"
content_hash: "3b3cb6283c05afa472abca2297e5b234d2e9da31130bec38b111173676f27e9a"
---

# Uninstalling the chart

To uninstall/delete the deployment:

```
$ helm uninstall ${BD_NAME} --namespace ${BD_NAME}
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

If you have used `kubectl` to install from a dry-run as shown above, the following command will remove the install:

```
$ kubectl delete -f ${BD_NAME}.yaml
```
