---
title: "Connecting to a Bugzilla instance using SSL"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/connecting-to-a-bugzilla-instance-using-ssl.html"
content_id: "XFhjEAIYhX~ljVM3vs8A_g"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:23.592184+00:00"
---

# Connecting to a Bugzilla instance using SSL

Note: If Coverity is deployed in the cloud, refer to "Add certificates to the Coverity Connect truststore" in the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide for information on connecting to
Bugzilla.

If the Bugzilla instance uses SSL, it is necessary to import the SSL certificate to
Coverity Connect. The following example is shown for Windows.

1. Access the Bugzilla instance through a browser.
2. In the Address bar, click the "lock" icon and save the certificate.
3. Double-click the certificate and click Install certificate. Follow the
   instructions to add the certificate to the Trusted Root Certificate
   Authorities store.
4. On the command line, launch `certmgr.msc`.
5. Navigate to the Trusted Root Certificate Authorities
   store.
6. Expand the tree and click Certificates.
7. Find the certificate saved previously.
8. Right-click on the certificate and choose All tasks and
   Export.
9. Navigate to the Coverity Connect installation directory.
10. Execute the command:

    ```
    <installationfolder>/jre/bin/keytool -import -alias "bugzilla" -file exportedCert.cer -keystore <installationfolder>/jre/lib/security/cacert
    ```
11. Restart Coverity Connect.

The following procedure is for Linux:

1. Obtain the Bugzilla certificate (for example,
   bugzilla-cert.crt) and copy it to the following
   directory:

   ```
   $ sudo cp bugzilla-cert.crt /usr/local/share/ca-certificates/bugzilla-cert.crt
   $ sudo update-ca-certificates
   ```
2. Import the Bugzilla certificate into Coverity Connect:

   ```
   $ keytool -importcert -file bugzilla-cert.crt -keystore ~/<install-dir>/jre/lib/security/cacerts
   ```

   The default passphrase is: `changeit`
3. Restart Coverity Connect.

Note: If the SSL handshake fails, take the following action, depending on the reason:

- If it leaves an "unrecognized_name" error in cim.log, then set the
  following parameter in the
  <install-dir>/config/system.properties
  file:

  ```
  java_opts_pre=-Djsse.enableSNIExtension=false
  ```

  (The
  parameter `java_opts_post=-Djsse.enableSNIExtension=false`
  also works.)
- If it leaves a "No name matching" error in cim.log, then the long name
  of the certificate must be used. For example, if the full certificate name is
  bugzilla-cert.company.com, using the short name will
  cause the SSL handshake to fail.
