---
title: "Configuring Coverity Connect with an SSL-enabled Email server"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-coverity-connect-with-an-ssl-enabled-email-server.html"
content_id: "T_kF19~Zc2Vd9XoLC44oHg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:59.593835+00:00"
---

# Configuring Coverity Connect with an SSL-enabled Email server

Note: If Coverity Connect is deployed in the cloud, refer to "Setting up TLS and certificates for analysis in the cloud" in
the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide for information on importing a Coverity
Connect SSL/TLS certificate.

If the mail server used by Coverity Connect is protected with SSL authentication, then
the mail server's SSL certificate must be added to the Coverity Connect keystore.

1. Obtain the certificate (for example, exportedCert.cer) from
   the mail server administrator.
2. In the Coverity Connect installation folder, run the following command:

   `jre/bin/keytool -import -alias "mailserver" -file exportedCert.cer
   -keystore jre/lib/security/cacert`
3. Restart Coverity Connect.
