---
title: "Generating a Coverity Connect TLS certificate signed by a Certificate Authority"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generating-a-coverity-connect-tls-certificate-signed-by-a-certificate-authority.html"
content_id: "FS~T3dppUJQMEl55raIyMA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:59.511302+00:00"
---

# Generating a Coverity Connect TLS certificate signed by a Certificate Authority

In order to enable a TLS-SSL connection to the Coverity cloud cluster, you need to
generate a CA certificate for each Coverity Connect instance. You can optionally use a
certificate authority (CA) to generate needed certificates.

To generate TLS-SSL certificates signed by a Certificate Authority (CA):

1. Request a CA signed certificate. For instructions to request a CA signed
   certificate:

   - In Google Cloud, refer to <https://cloud.google.com/certificate-authority-service/docs/requesting-certificates>
   - In AWS, refer to <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains-prerequisites.html>
   - In Azure, refer to <https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-certificate?tabs=apex>
   - In OpenShift, refer to <https://www.redhat.com/sysadmin/cert-manager-operator-openshift>
   - For any specific CA, refer to the CA documentation. For example:
     - <https://www.digicert.com/>
     - <https://www.comodoca.com/>
2. Generate the following certificates:

   - `rootCA.pem` - root CA cert (self signed)
   - `intermediateCA.pem` - (intermediate certificate signed by
     root CA)
   - `server.pem` - server certificate (signed by intermediate CA)
   - `proxy-server.pem` - for TLS and mTLS forward proxy server.
     See also Configuring TLS forward proxy.
   - `repo.blackduck.com.pem` - The Black Duck artifactory CA
     certificate is a Black Duck server certificate that contains the public
     key and it helps to establish connection with the Black Duck server when
     the proxy TLS mode is set to either `tls` or
     `mtls`.

     To generate the `repo.blackduck.com.pem` file:

     ```
     curl -w %{certs} https://repo.blackduck.com | awk '/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/' > repo.blackduck.com.pem
     ```
3. Create an intermediate file (server-chain.pem) that contains all three
   certificates. For example:

   ```
   cp server.pem server-chain.pem
   cat intermediateCA.pem >> server-chain.pem 
   cat rootCA.pem >> server-chain.pem
   ```
4. Verify that server-chain.pem contains all three pem files:

   ```
   cat server-chain.pem
   ```
5. Create a TLS secret named `coverity-tls`, specifying the
   intermediate file:

   ```
   kubectl create secret tls "coverity-tls"
     --namespace "coverity"
     --cert=server-chain.pem
     --key=server.key
   ```
6. In the `cnc` Helm chart:
   1. Update the name of the TLS secret:

      ```
      cim:
        tls:
          - secretName: "coverity-tls"
      ```
   2. For ingress, provide the name of the TLS secret and the name of the
      ingress host. This is an array which is formatted with a dash for each
      host. For example:

      ```
      cim:
        ingress:
          tls:
            - secretName: "coverity-tls"
          hosts:
            - coverity01.company.com
      ```

      Important: The Connect (cim) hostname that
      you specify in `cim.ingress.hosts` must not exceed 46
      characters in length. This restriction excludes the
      `https://` characters that are used when you specify
      the URL, as well as any port specification.
   3. For the cimweb keystore, provide the name of the TLS certificate secret,
      and enable the cimweb keystore. For example, for a secret named
      coverity-tls, and enabled = true:

      ```
      cim:
        cimweb:
          keystore:
            certificateSecret: "coverity-tls"
            enabled: true
      ```

      For keystore Helm key information, refer to cim.cimweb.keystore Helm keys.
7. In a browser window, connect to the Coverity Connect UI, and in the Certificate
   Viewer window within ther browser, verify that all three Coverity certificate
   chain layers are listed: root > intermediate > server.
