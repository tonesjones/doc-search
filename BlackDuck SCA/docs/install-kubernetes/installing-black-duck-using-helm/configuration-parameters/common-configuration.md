---
title: "Common configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/common-configuration.html"
content_id: "HIMBsAztkbWjeltFP34_Zw"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:04.265862+00:00"
---

# Common configuration

| Parameter | Description | Default |
| --- | --- | --- |
| `registry` | Image repository | `docker.io/blackducksoftware` |
| `imageTag` | Version of Black Duck | `2024.7.1` |
| `imagePullSecrets` | Reference to one or more secrets to be used when pulling images | `[]` |
| `tlsCertSecretName` | Name of Webserver TLS Secret containing Certificates (if not provided Certificates will be generated) |  |
| `exposeui` | Enable Black Duck Web Server User Interface (UI) | `true` |
| `exposedServiceType` | Expose Black Duck Web Server Service Type | `NodePort` |
| `enablePersistentStorage` | If true, Black Duck will have persistent storage | `true` |
| `storageClass` | Global storage class to be used in all Persistent Volume Claim |  |
| `enableLivenessProbe` | If true, Black Duck will have liveness probe | `true` |
| `enableInitContainer` | If true, Black Duck will initialize the required databases | `true` |
| `enableSourceCodeUpload` | If true, source code upload will be enabled by setting in the environment variable (this takes priority over environs flag values) | `false` |
| `dataRetentionInDays` | Source code upload's data retention in days | `180` |
| `maxTotalSourceSizeinMB` | Source code upload's maximum total source size in MB | `4000` |
| `enableBinaryScanner` | If true, binary analysis will be enabled by deploying the binary scan worker | `false` |
| `enableIntegration` | If true, blackduck integration will be enabled by setting in the environment variable (this takes priority over environs flag values) | `false` |
| `enableAlert` | If true, the Black Duck Alert service will be added to the nginx configuration with the environ `"HUB_ALERT_HOST:<blackduck_name>-alert.<blackduck_name>.svc` | `false` |
| `enableIPV6` | If true, IPV6 support will be enabled by setting in the environment variable (this takes priority over environs flag values) | `true` |
| `certAuthCACertSecretName` | Own Certificate Authority (CA) for Black Duck Certificate Authentication | ``` run this command "kubectl create secret generic -n <namespace>                                 <name>-blackduck-auth-custom-ca --from-file=AUTH_CUSTOM_CA=ca.crt" and provide the                                 secret name ``` |
| `proxyCertSecretName` | Black Duck proxy server’s Certificate Authority (CA) | ``` run this command "kubectl create secret generic -n <namespace>                                 <name>-blackduck-proxy-certificate --from-file=HUB_PROXY_CERT_FILE=proxy.crt" and                                 provide the secret name ``` |
| `proxyPasswordSecretName` | Black Duck proxy password secret | ``` run this command "kubectl create secret generic -n <namespace>                                 <name>-blackduck-proxy-password                                 --from-file=HUB_PROXY_PASSWORD_FILE=proxy_password_file" and provide the secret                                 name ``` |
| `ldapPasswordSecretName` | Black Duck LDAP password secret | ``` run this command "kubectl create secret generic -n <namespace>                                 <name>-blackduck-ldap-password                                 --from-file=LDAP_TRUST_STORE_PASSWORD_FILE=ldap_password_file" and provide the secret                                 name ``` |
| `environs` | environment variables that need to be added to Black Duck configuration | ``` map e.g. if you want to set PUBLIC_HUB_WEBSERVER_PORT, then it should be --set                                 environs.PUBLIC_HUB_WEBSERVER_PORT=30269 ``` |
