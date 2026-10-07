---
title: "Upgrading the chart"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/upgrading-the-chart.html"
content_id: "h2c56MJ1s1UGxX2c7AZH3g"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:22.636711+00:00"
content_hash: "6ef01fa1727895c65defaa15ddd75a3b850e31b325a14b0f208d9d183fcffabf"
---

# Upgrading the chart

Before upgrading to new version, please make sure to run the following command to pull the latest version of charts from chart museum:

```
$ helm repo update
$ helm pull blackduck/blackduck -d <DESTINATION_FOLDER> --untar
```

To update the deployment:

```
$ BD_NAME="bd" && BD_SIZE="sizes-gen04/120sph"
$ helm upgrade ${BD_NAME} ${BD_INSTALL_DIR} --namespace ${BD_NAME} -f ${BD_INSTALL_DIR}/values.yaml -f ${BD_INSTALL_DIR}/${BD_SIZE}.yaml
```
