---
title: "Getting started"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/getting-started.html"
content_id: "_x5QKJ_Wgonabj9vkltB3Q"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:00.254014+00:00"
---

# Getting started

## Save the chart locally

To save the chart on your machine, run the following command:

```
$ helm pull blackduck/blackduck -d <DESTINATION_FOLDER> --untar
```

This will extract the charts to the specified folder (as denoted by the
`-d` flag in the above command), which contains the necessary
files to deploy the application.

## Create a namespace

Create a namespace by running the commands below. The example uses
`bd`, but you can replace it with any name of your choice.

```
$ BD_NAME="bd"
$ kubectl create ns ${BD_NAME}
```

## Create a custom TLS secret (optional)

It's common to provide a custom web server TLS secret before installing the Black Duck Helm chart. Create the secret with the command below:

```
$ BD_NAME="bd"
$ kubectl create secret generic ${BD_NAME}-blackduck-webserver-certificate -n ${BD_NAME} --from-file=WEBSERVER_CUSTOM_CERT_FILE=tls.crt --from-file=WEBSERVER_CUSTOM_KEY_FILE=tls.key
```

Next, update the `TLS certificate for Black Duck` block in
`values.yaml`, ensuring to uncomment the
`tlsCertSecretName` value (tls.crt and tls.key files are
required). If the value `tlsCertSecretName` is not provided then Black Duck will generate its own certificates.

```
tlsCertSecretName: ${BD_NAME}-blackduck-webserver-certificate
```

Note: This step is not required where TLS termination is being handled upstream from the application (i.e. via an ingress resource).
