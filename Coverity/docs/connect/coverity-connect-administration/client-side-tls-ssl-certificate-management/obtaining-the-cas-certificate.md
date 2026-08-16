---
title: "Obtaining the CA's certificate"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/obtaining-the-ca-s-certificate.html"
content_id: "51DGn_0ctYTws4uDgL4Rag"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:27.064715+00:00"
---

# Obtaining the CA's certificate

You can obtain the CA's certificate from the .pem file on the
server.

To obtain the certificate, on the Coverity Connect host, use `keytool` to
export the CA's certificate in PEM format (`-rfc`) to a file. For
example, where the CA's certificate's alias is "root" in the CC keystore:

```
<CC_host>$ <CC_install_dir>/jre/bin/keytool \ 
-keystore <CC_install_dir>/server/base/conf/keystore.jks -storepass changeit \ 
-exportcert -rfc -alias root -file root-CA-cert.pem 
Certificate stored in file root-CA-cert.pem
```
