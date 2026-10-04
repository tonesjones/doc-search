---
title: "Installing the chart"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/installing-the-chart.html"
content_id: "sErY7bxrVipfCL7Wj3DLHg"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-10-04T23:32:22.594746+00:00"
content_hash: "eec1c7f79db8cdeb7052fe21244cb227124f317473c076543d688240b0f969ee"
---

# Installing the chart

To install the Black Duck chart, run the following command:

```
$ BD_NAME="bd" && BD_SIZE="sizes-gen04/120sph" && BD_INSTALL_DIR="<DESTINATION_FOLDER>/blackduck/"
$ helm install ${BD_NAME} ${BD_INSTALL_DIR} --namespace ${BD_NAME} -f ${BD_INSTALL_DIR}/values.yaml -f ${BD_INSTALL_DIR}/${BD_SIZE}.yaml
```

Tip: List all releases using `helm list` and list all specified values using `helm get values RELEASE_NAME`.

You must not use the `--wait` flag when you install the Helm Chart. The `--wait` flags waits for all pods to become Ready before marking the **Install** as done. However the pods will not become Ready until the postgres-init job is run during the **Post-Install**. Therefore the **Install** will never finish.

Alternatively, Black Duck can be deployed using `kubectl apply` by generating a dry run manifest from Helm:

```
$ BD_NAME="bd" && BD_SIZE="sizes-gen04/120sph" && BD_INSTALL_DIR="<DESTINATION_FOLDER>/blackduck/"
$ helm install ${BD_NAME} ${BD_INSTALL_DIR} --namespace ${BD_NAME} -f ${BD_INSTALL_DIR}/values.yaml -f ${BD_INSTALL_DIR}/${BD_SIZE}.yaml --dry-run=client > ${BD_NAME}.yaml

# install the manifest
$ kubectl apply -f ${BD_NAME}.yaml --validate=false
```
