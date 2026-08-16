---
title: "Configure Dell ECS storage support"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-dell-ecs-storage-support.html"
content_id: "kB5qHkrcxG_MIe0iDhHv8A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:44.431208+00:00"
---

# Configure Dell ECS storage support

custom certificate: A custom certificate is a user-defined SSL/TLS certificate that is
used to secure communications between services, applications, and users within the
Kubernetes cluster. Custom certificates are essential for ensuring secure data
transmission, authentication, and integrity in microservices architectures. Custom
certificates are used to establish secure connections using the HTTPS protocol, or for
mutual TLS (mTLS) to authenticate both the client and server,

custom truststore: The primary purpose of a custom truststore is to hold certificates
from Certificate Authorities (CAs) or specific certificates that your applications need
to trust. This ensures that the application can establish secure connections to other
services without encountering trust issues.

custom storage: Dell ECS (Elastic Cloud Storage) is a software-defined cloud storage
platform designed to provide scalable, secure, and resilient storage solutions for
unstructured data. Dell ECS is a custom storage backend which manages persistent storage
needs for the storage service.

If you are using Dell ECS storage, in addition to creating the storage, you need to
complete the following tasks. Except for

1. Create the Dell ECS storage as documented by Dell.
2. Mount the custom certificate files using the
   `cache-service.extraVolumes:` and
   `cache-service.extraVolumeMounts:` Helm keys. For information on
   these Helm keys, see cache-service Helm keys.
3. Create a truststore with a certificate to access the storage. You can use a CA
   certificate or a custom certificate
4. Create a truststore ConfigMap and enable a certificate for scan service as described
   below.
5. Configure MinIO for storage service as described below.
6. Mount the custom storage and configure the cache service as described below.
7. Install or apply changes to a running depoyment as described below.

## Dell ECS: Create a truststore ConfigMap and enable a certificate for scan service

Note: The examples that follow override
`scan-services` Helm chart values.

To add any needed truststore certificates to the scan-services, create the truststore
ConfigMap and make that ConfigMap available to the scan service as follows:

1. Create a truststore ConfigMap that contains the Dell ECS certificate
   (.crt).

   ```
   kubectl create configmap <truststoreConfigMapName> \          
                   --from-file=minio.crt=<cert-path>/minio.crt -n <namespace>
   ```

   Note: You can add the certificate to the default
   `"connect-trust-stores"` truststore ConfigMap.

   To
   add a certificate to an existing truststore ConfigMap, you can use
   `kubectl edit configmap <truststoreConfigMapName>` and
   manually add the certificate.
2. Enable the truststore and specify the truststore ConfigMap name in the
   `scan-services` Helm chart `values.yaml`
   file:

   ```
   trust-stores:
     configmapName: "<truststoreConfigMapName>"
     enabled: true
   ```

   Note: For the
   `configmapName` Helm key, if you added the Dell ECS
   certificate to the default Connect truststore ConfigMap, then use
   `configmapName: "connect-trust-stores"`.
3. Set the following environment variables in scan-service:

   ```
   scan-service:
     environment:
       TLS_CUSTOM_CERT_PATH: /opt/trust-stores/ssl/<your-custom-certificate>
       TLS_CUSTOM_ENABLED: true
   ```

   For example, to add `minio.crt` to the trust-stores
   configmap:

   ```
   TLS_CUSTOM_CERT_PATH: /opt/trust-stores/ssl/minio.crt
   ```

   For further information on these Helm keys, see scan-service.environment Helm keys in the chapter: scan-services Helm subchart: Helm keys.

## Dell ECS: Configure MinIO for storage service

Note: The examples that follow override
`scan-services` Helm chart values.

1. Set `storage-service.endpoint.external.url` and
   `storage-service.endpoint.internal.url` to the storage
   endpoint:

   ```
   storage-service:
     endpoint:
       external:
         url: <storage-endpoint-url>
       internal:
         url: <storage-endpoint-url>
   ```
2. Create an S3 storage bucket secret containing access credentials:

   ```
   kubectl create secret <name-of-secret> \
   --from-literal=aws_access_key=admin \
   --from-literal=aws_secret_key=synopsys \
   -n <namespace>
   ```

   For example:

   ```
   kubectl create secret generic cnc-minio-s3 \
   --from-literal=aws_access_key=admin \
   --from-literal=aws_secret_key=synopsys \
   -n minio-ns
   ```
3. In the `scan-services` chart `values.yaml`
   file, configure S3 storage bucket information:

   ```
   storage-service:
     s3: 
       bucket: <storage-bucket-name>
       region: <storage-bucket-region>
       secret:
         name: <storage-bucket-secret-name>
     storageType: s3
   ```

## Configure the cache service

To configure support for Dell ECS storage, in the `scan-services` Helm
subchart, configure the `cache-service.environment` Helm keys as
follows:

Note: For reference information on the
`cache-service.environment` Helm keys, see cache-service.environment Helm keys.

1. This procedure assumes that you have created and mounted custom certificate
   files using the `cache-service.extraVolumes:` and
   `cache-service.extraVolumeMounts:` Helm keys. For
   information on these Helm keys, see cache-service Helm keys.
2. Change the `CUSTOM_CACERT_ENABLED` environment parameter to
   `true`:

   ```
   cache-service:
     environment:
       CUSTOM_CACERT_ENABLED: true
   ```
3. Configure the AWS endpoint environment parameter for Dell ECS storage.

   ```
   cache-service:
     environment:
       AWS_ENDPOINT: ""
   ```

   For example: `"http://ecs<x>.<domain>.com:9020"`.
4. The following environment parameters are commented out in the Helm chart. To
   use these parameters, uncomment them, then either use the default values or
   override if needed.

   ```
   cache-service:
     environment:
       # CERT_STORE_PATH: "/cache/truststore.jks"
       # CERT_STORE_TYPE: "JKS"
       # CUSTOM_CACERT_PATH: ""
   ```

   where:
   - `CERT_STORE_PATH:` Specifies the path to where the
     truststore is or will be located. You can use any mounted path.
   - `CERT_STORE_TYPE:` Specifies the type of truststore.
     Use the default value, `"JKS"`.
   - `CUSTOM_CACERT_PATH:` Specifies the path and folder
     that contains the custom certificate file.
5. Add truststore certificate volume mounts.

   ```
   - name: import-trust-stores-certs
     mountPath: /tmp/certs
   ```

   ```
   - name: import-trust-stores-certs
     configMap:
       name: custom-minio-pem
       defaultMode: 420
   ```

## Apply changes to a running deployment

If you made any Helm chart changes (overrides, annotations, property values, etc) to
a running deployment, to apply the changes, you need to pass the Helm overrides to
the running deployment. For example, you can perform a `helm
upgrade`.
