---
title: "Configure the Connect web application TLS keystore"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-the-connect-web-application-tls-keystore.html"
content_id: "hAjOsW7eW5R5IATcrxJ5rA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:25.371120+00:00"
---

# Configure the Connect web application TLS keystore

In the `cnc` Helm chart, configure the
`cim.cimweb.keystore` Helm heys to specify the Connect web
application certificate secret and mount the keystore.

1. This procedure assumes that you have created a Connect TLS certificate secret as
   described in Generating a Coverity Connect TLS certificate signed by a Certificate Authority.

   The
   `keystore.jks` file must contain a public/private certificate
   pair used for the Connect instance.
2. In the `cim.cimweb.keystore.certificateSecret` Helm key, specify
   the name of the secret that contains the Connect TLS certificate. This key is
   used when the `cim.cimweb.keystore.enabled` key is
   `true`. For example, if the name of the secret is
   `coverity-tls`:

   ```
   cim:
     cimweb:
       keystore:
         certificateSecret: "coverity-tls"
   ```

   For Helm key reference information, see cim.cimweb.keystore Helm keys.
3. To mount the Connect keystore that you created for the TLS certificate set
   `cim.cimweb.keystore.enabled: true` as follows:

   ```
   cim:
     cimweb:
       keystore:
         certificateSecret: "coverity-tls"
         enabled: true
   ```
