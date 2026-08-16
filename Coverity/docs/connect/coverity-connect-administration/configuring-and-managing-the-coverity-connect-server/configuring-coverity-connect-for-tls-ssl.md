---
title: "Configuring Coverity Connect for TLS/SSL"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-coverity-connect-for-tls/ssl.html"
content_id: "5Gza9oD5zDmkTvS19u~nYg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:28.504308+00:00"
---

# Configuring Coverity Connect for TLS/SSL

You can configure Coverity Connect to encrypt communications using TLS/SSL.

Note:
If Coverity is deployed in the cloud, refer to
"Setting up TLS and certificates for analysis in the cloud"
in the document, Coverity 2026.6.0 Cloud Deployment Administrator and User Guide for information on configuring Coverity Connect SSL/TLS.

This process summarizes steps described in the
[Tomcat documentation](http://tomcat.apache.org/tomcat-8.0-doc/ssl-howto.html),
as well as the [Java keytool](http://docs.oracle.com/javase/6/docs/technotes/tools/solaris/keytool.html) command.
You can refer to this documentation for more in-depth information on configuring the embedded Apache Tomcat server
and managing a Java keystore. Refer to the appropriate keytool documentation for the JDK or JRE version that you are using.
See Commit encryption use cases for information on committing over TLS/SSL use cases.

Encryption for Coverity Connect works in tandem with the Coverity Analysis client, and some
configuration by the user might be necessary.
For information on client-side configuration (including the ca-certs.pem file) and authentication,
see "Using TLS/SSL with Coverity Analysis" in the Coverity Analysis 2026.6.0 User and Administrator Guide.

Remember:
For general information, you can refer to
<http://tomcat.apache.org/tomcat-8.0-doc/ssl-howto.html> for information on setting up TLS/SSL
for Tomcat servers such as Coverity Connect.
In addition, see <http://en.wikipedia.org/wiki/X.509> for background on digital certificates,
and <https://www.openssl.org/docs/manmaster/man1/openssl-x509.html> for information on working with certificates using OpenSSL.

The sections that follow should provide the information that is required to set up Coverity Connect.

Updating an expired TLS/SSL certificate for Coverity Connect
