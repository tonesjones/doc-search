---
title: "Create a Connect UI server keystore"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-connect-ui-server-keystore.html"
content_id: "DjFNZ8v6r22G60XDzoqCOg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:00.840979+00:00"
---

# Create a Connect UI server keystore

Each Coverity Connect instance must have a keystore to store private keys, certificates
with public keys, or secret keys used for secure communication and data encryption
within the Kubernetes cluster. Private keys can sign or decrypt data, while public keys
can verify or encrypt data.

The Connect UI server keystore is used by a Coverity client to authenticate the Connect
UI server. During a TLS/SSL handshake, the server searches the keystore for the private
key, then forwards the corresponding public key and certificate to the client.

To configure the Connect UI server keystore:

1. If you have not already done so, generate a certificate secret. See Generating a Coverity Connect TLS certificate signed by a Certificate Authority.
2. In the `cnc` Helm chart, enter the name of the secret into the
   `cim.cimweb.keystore.certificateSecret: ""` Helm key.
3. Set the following key as `true` to mount the keystore:
   `cim.cimweb.keystore.enabled: true`.

   For example, to specify a certificate secret named coverity-tls and mount the
   keystore:

   ```
   cim:
     cimweb:
       keystore:
         certificateSecret: "coverity-tls"
         enabled: true
   ```

For keystore Helm key information, refer to cim.cimweb.keystore Helm keys.
