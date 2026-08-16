---
title: "Using Custom SSL Certificates"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/using-custom-ssl-certificates.html"
content_id: "abrwTWGPq~wlyr17LpjZ0A"
version: "8.4.0"
section: "Installation References"
scraped_at: "2026-08-08T23:46:31.432642+00:00"
---

# Using Custom SSL Certificates

This section describes how to configure the Alert webserver with custom certificates for
both the UI and Database.

## Alert UI SSL Certificates

### Create Certificate Secret

Execute the follwing command:

```
 $ kubectl create secret generic <SECRET_NAME> -n <ALERT_NAMESPACE> \
 --from-file=WEBSERVER_CUSTOM_CERT_FILE=<PATH_TO_CERTIFICATE_FILE> \
 --from-file=WEBSERVER_CUSTOM_KEY_FILE=<PATH_TO_CERTIFICATE_KEY_FILE>
```

- Replace `<SECRET_NAME>` with the desired name for the
  secret.
- Replace `<ALERT_NAMESPACE>` with the namespace being
  used for Alert.
- Replace `<PATH_TO_CERTIFICATE_FILE>` to the path on the
  current file system to your `.crt` file.
- Replace `<PATH_TO_CERTIFICATE_KEY_FILE>` to the path on
  the current file system to the `.key` file corresponding to
  your `.crt` file.

Tip: The keys `WEBSERVER_CUSTOM_CERT_FILE` and
`WEBSERVER_CUSTOM_KEY_FILE` must be included in the
`--from-file=[key=]<FILE_NAME>` arguments in order
for Alert to correctly consume the certificate.

For more information about managing secrets, please see: [Managing secret using kubectl](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl).

### Configure Certificate Secret

Once you have created the certificate secret with the correct keys, you must then
tell alert the name of the secret the certificate corresponds to. In the
'values.yaml' file, set

```
webserverCustomCertificatesSecretName: "<SECRET_NAME>"
```

- Replace `<SECRET_NAME>` with the name of the secret
  created in the step Create Certificate Secret.

  Note: This will not automatically enable the use of the custom certificate.
  To do that, follow the instructions in Enable Custom
  Certificate.

### Enable Custom Certificate

In the 'values.yaml' file, set

```
enableCertificateSecret: true
```

This will instruct Alert to use the secret specified by the
`webserverCustomCertificatesSecretName` configuration
parameter as the custom certificate.

## External Database SSL Certificates

### Create Certificate Secret

External Postgres certificates are created in a similar fashion as the examples
above. The certificate names for Postgres SSL are as follows:

| Secret Name | Description |
| --- | --- |
| ALERT_DB_SSL_KEY_PATH | The certificate key |
| ALERT_DB_SSL_CERT_PATH | The certificate file |
| ALERT_DB_SSL_ROOT_CERT_PATH | The root certificate |

```
 $ kubectl create secret generic <SECRET_NAME> -n <ALERT_NAMESPACE> \
 --from-file=ALERT_DB_SSL_KEY_PATH=<PATH_TO_CERTIFICATE_KEY_FILE> \
 --from-file=ALERT_DB_SSL_CERT_PATH=<PATH_TO_CERTIFICATE_CERT_FILE> \
 --from-file=ALERT_DB_SSL_ROOT_CERT_PATH=<PATH_TO_ROOT_CERTIFICATE>
```

### Configure And Enable Certificate Secret

In the values.yaml file, the following values need to be set:

```
  ssl: true # If true, Alert uses SSL for external Postgres connection
  sslUseFiles: true # If true, Alert will expect to find ssl certs for communicating with the External Postgres database
  sslSecrets: # Secret that contains all the ssl file paths
    secretName: "<SECRET_NAME>"
```

Replace `SECRET_NAME` with the appropriate value created in the
previous step. When alert starts, the application will communicate with the
database using a certificate, key and root certificate.
