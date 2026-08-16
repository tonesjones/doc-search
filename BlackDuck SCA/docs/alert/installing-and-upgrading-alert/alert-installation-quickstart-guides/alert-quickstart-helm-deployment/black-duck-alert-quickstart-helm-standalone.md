---
title: "Black Duck Alert Quickstart (Helm - Standalone)"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-quickstart-helm-standalone-.html"
content_id: "vASt5IAQL5RZ~SrRE~f5Gg"
version: "8.4.0"
section: "Installing and Upgrading Alert"
scraped_at: "2026-08-08T23:46:26.226510+00:00"
---

# Black Duck Alert Quickstart (Helm - Standalone)

Note: This quickstart guide will focus on a *standalone* deployment. We will also download the charts, however, it is also possible to use `helm install` with `--set` commands for the deployment.

## Prerequsites

- A Kubernetes cluster (1.9+) with enough free resources to deploy Alert.
- Helm 3
- NGINX Ingress controller installed.

See Installation Requirements for more information.

## Downloading the chart

To download the Alert charts, run the following commands:

```
helm repo add blackduck https://repo.blackduck.com/artifactory/cloudnative/
helm repo update
```

Verify that the Alert charts are available:

```
helm search repo blackduck/blackduck-alert
```

Download the chart to the local machine:

```
helm pull blackduck/blackduck-alert --untar
```

This will create a folder named `blackduck-alert` within the directory where the above command was executed.

## Alert configuration

Next, configure the values.yaml file. There are several fields to change for the purpose of this quickstart.

Important: The values.yaml settings are only used to
initialize the DB when Alert starts for the first time. If the Alert DB already
exists, configuration values added here, such as adding a provider, will not be
reflected in the configuration.

### Configure the storage class to be used

```
storageClass: <STORAGE_CLASS_NAME>
```

- Replace <STORAGE_CLASS_NAME> with an appropriate provisioner (see
  vendor considerations)

### Disable exposing Alert via the NodePort Service

```
exposeui: false
```

- We will configure NGINX ingress to expose the service via an ingress below.
  This is the most typical deployment method.

## Configuring Environment Variables

Configuration of the Alert application such as configuring authentication, database,
providers, and channels can be performed using environment variables. Environment
variable values are only used if there is no configuration data for the
corresponding component in the database. These will be read in at startup and are
typically configured in the values.yml file. See Helm Chart
Configuration. There are a number of different configuration options
which can be statically set. For the purpose of this quick start guide, we will
configure these within the UI after deployment.

## Deploying

### Deploy the Alert chart

```
helm install <ALERT_RELEASE_NAME> . -f values.yml -n <ALERT_NAMESPACE> --create-namespace
```

### Verify that all pods have fully started and there are no errors

```
kubectl get po -n <ALERT_NAMESPACE>
```

## Configuring NGINX ingress

We will now create an ingress resource so that the application is available at
`https://<ALERT_SERVER>/alert`

```
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: alert-exposed
  namespace: <ALERT_NAMESPACE>
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/proxy-body-size: 1024m
    nginx.ingress.kubernetes.io/proxy-buffer-size: 8k
    nginx.ingress.kubernetes.io/secure-backends:  "true"
    nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
    nginx.ingress.kubernetes.io/proxy-connect-timeout: "300"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "300"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "300"
    nginx.ingress.kubernetes.io/send-timeout: "300"
spec:
  rules:
  - http:
      paths:
        - path: /alert
          backend:
            serviceName: <ALERT_RELEASE_NAME>
            servicePort: 8443
```

Apply the manifest and verify that the ingress has been successfully created

```
kubectl get ing -n <ALERT_NAMESPACE>
```

Once created, Alert will be available at `https://<ALERT_SERVER>/alert`

At this point, you will be presented with a login screen.

Figure 1. Alert login screen
[image: Alert login with SAML]

| Default USERNAME | Default PASSWORD |
| --- | --- |
| sysadmin | blackduck |

Note: The sysadmin username and password are not related to the sysadmin account of your Black Duck SCA installation.
