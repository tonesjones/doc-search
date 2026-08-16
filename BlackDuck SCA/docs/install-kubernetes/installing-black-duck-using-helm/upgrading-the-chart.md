---
title: "Upgrading the chart"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/upgrading-the-chart.html"
content_id: "w6xPhXqVCTsC0R2o0tEubw"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:03.075998+00:00"
---

# Upgrading the chart

Before upgrading to new version, please make sure to run the following command to pull
the latest version of charts from chart museum:

```
$ helm repo update
$ helm pull blackduck/blackduck -d <DESTINATION_FOLDER> --untar
```

To update the deployment:

```
$ BD_NAME="bd" && BD_SIZE="sizes-gen04/120sph"
$ helm upgrade ${BD_NAME} ${BD_INSTALL_DIR} --namespace ${BD_NAME} -f ${BD_INSTALL_DIR}/values.yaml -f ${BD_INSTALL_DIR}/${BD_SIZE}.yaml
```
