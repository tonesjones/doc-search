---
title: "Installing the chart"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/installing-the-chart.html"
content_id: "a0bt3Ry~6HLYsFqND8sJwA"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:01.960755+00:00"
---

# Installing the chart

To install the Black Duck chart, run the following command:

```
$ BD_NAME="bd" && BD_SIZE="sizes-gen04/120sph" && BD_INSTALL_DIR="<DESTINATION_FOLDER>/blackduck/"
$ helm install ${BD_NAME} ${BD_INSTALL_DIR} --namespace ${BD_NAME} -f ${BD_INSTALL_DIR}/values.yaml -f ${BD_INSTALL_DIR}/${BD_SIZE}.yaml
```

Tip: List all releases using `helm list` and list all specified
values using `helm get values RELEASE_NAME`.

You must not use the `--wait` flag when you install the Helm Chart. The
`--wait` flags waits for all pods to become Ready before marking the
**Install** as done. However the pods will not become Ready until the
postgres-init job is run during the **Post-Install**. Therefore the **Install**
will never finish.

Alternatively, Black Duck can be deployed using `kubectl
apply` by generating a dry run manifest from Helm:

```
$ BD_NAME="bd" && BD_SIZE="sizes-gen04/120sph" && BD_INSTALL_DIR="<DESTINATION_FOLDER>/blackduck/"
$ helm install ${BD_NAME} ${BD_INSTALL_DIR} --namespace ${BD_NAME} -f ${BD_INSTALL_DIR}/values.yaml -f ${BD_INSTALL_DIR}/${BD_SIZE}.yaml --dry-run=client > ${BD_NAME}.yaml

# install the manifest
$ kubectl apply -f ${BD_NAME}.yaml --validate=false
```
