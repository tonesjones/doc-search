---
title: "Black Duck Alert Quickstart (Helm)"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/black-duck-alert-quickstart-helm-.html"
content_id: "0qzZc7amGzukkIi_2SuClw"
version: "8.4.0"
section: "Installing and Upgrading Alert"
scraped_at: "2026-08-08T23:46:25.544151+00:00"
---

# Black Duck Alert Quickstart (Helm)

Note: This quickstart guide will focus on a deployment within the same namespace as Black Duck SCA with an internally deployed database.
We will download the charts, however, it is also possible to use `helm install` with `--set` commands for the deployment.

## Prerequsites

- A Kubernetes cluster (1.9+) with enough free resources to deploy Alert.
- Helm 3
- An existing Black Duck SCA installation (stopped).
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

- Replace <STORAGE_CLASS_NAME> with an appropriate provisioner (see vendor considerations)

### Disable standalone mode

(This instructs the chart not to deploy CFSSL, as this will already exist)

```
enableStandalone: false
```

### Enable deployment with Black Duck by setting 'deployAlertWithBlackDuck'

```
deployAlertWithBlackDuck: true
```

### Configure the Black Duck release name by setting 'blackDuckName'

```
blackDuckName: "<BLACKDUCK_RELEASE_NAME>"
```

- Replace <BLACKDUCK_RELEASE_NAME> with the name of the release of Black
  Duck

### Configure the Black Duck namespace by setting 'blackDuckNamespace'

```
blackDuckNamespace: "<BLACK_DUCK_NAMESPACE>"
```

- Replace <BLACK_DUCK_NAMESPACE> with the namespace where the Black Duck SCA instance is deployed

### Disable exposing Alert via the NodePort Service

```
exposeui: false
```

- The most common deployment method is to configure NGINX ingress to expose the service via an ingress as shown below.

## Configuring Environment Variables

Configuration of the Alert application such as configuring authentication, database,
providers, and channels can be performed using environment variables. Environment
variable values are only used if there is no configuration data for the
corresponding component in the database. These will be read in at startup and are
typically configured in the values.yml file. See Helm Chart
Configuration. There are a number of different configuration options
which can be statically set. For the purpose of this quick start guide, we will
configure these within the UI after deployment.

## Black Duck SCA configuration

Black Duck SCA also needs to be made aware of Alerts presence. Within the values.yml for
your Black Duck SCA install, set the following properties. As this deployment is going
into the same namespace as Black Duck SCA, the `alertNamespace` property
has a default value of `Release.Namespace`.

```
enableAlert: true
```

```
alertName: "<ALERT_RELEASE_NAME>"
```

- Replace <ALERT_RELEASE_NAME> with the name of the release of Alert

## Deploying

### Deploy the Black Duck chart with the updated Alert parameters

```
helm install <BLACK_DUCK_RELEASE_NAME> . -f values.yaml -f sizes-gen03\<SPH_SIZE>.yaml -n <BLACK_DUCK_NAMESPACE>
```

### Deploy the Alert chart into the same namespace above

```
helm install <ALERT_RELEASE_NAME> . -f values.yaml -n <BLACK_DUCK_NAMESPACE>
```

### Verify that all pods have fully started and there are no errors

```
kubectl get pods -n <BLACK_DUCK_NAMESPACE>
```

- For example, with a Black Duck SCA 2022.2.0 release with Alert 6.10.0, you should see a
  total of 17 pods for a `10sph` deployment.
- For this quickstart, we are using the internal postgres containers. For
  production workloads, external databases are advised. In that
  configuration, there will be 15 pods for Black Duck SCA 2022.2.0.

## Configuring NGINX ingress

Assuming that Black Duck SCA is already exposed via an Ingress Controller, we will now
modify the routes so that the application is available at
`https://<BLACKDUCK_SERVER>/alert`

```
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: blackduck-exposed
  namespace: <BLACK_DUCK_NAMESPACE>
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
        - path: /
          backend:
            serviceName: <BLACK_DUCK_RELEASE_NAME>-blackduck-webserver
            servicePort: 443
        - path: /alert
          backend:
            serviceName: <ALERT_RELEASE_NAME>
            servicePort: 8443
```

Apply the manifest and verify that the ingress has been successfully created

```
kubectl get ing -n <BLACK_DUCK_NAMESPACE>
```

Once created, your Black Duck SCA install will be available at
`https://<BLACKDUCK_SERVER>`. Alert will be available at
`https://<BLACKDUCK_SERVER>/alert`

At this point, you will be presented with a login screen.

Figure 1. Alert login screen
[image: Alert login with SAML]

| Default USERNAME | Default PASSWORD |
| --- | --- |
| sysadmin | blackduck |

Note: The sysadmin username and password are not related to the sysadmin account of your Black Duck SCA installation.
