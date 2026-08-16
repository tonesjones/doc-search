---
title: "LDAP security"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ldap-security.html"
content_id: "Uh3RVisLw1daQS1~p3~neA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:40.366926+00:00"
---

# LDAP security

For security reasons, LDAP authentication tokens (passwords) are never stored in the
Coverity Connect database, except for the special case of the bind DN/password. The
bind/DN password is encrypted in the database for security.

In addition to setting the security type during LDAP configuration, Coverity
Connect requires certificates to connect to an SSL or TLS-enabled LDAP server. For
information on creating certificates and enabling your LDAP server for SSL or TLS, refer
to your server's documentation.

Interoperability with SSL/TLS-capable LDAP servers is provided, but only simple
authentication is supported. The SASL framework is not supported.

For LDAP SSL/TLS integration, Coverity Connect must be able to find the root CA
(certificate authority) public keys (certificates) to verify the signature of the LDAP
SSL or TLS server certificate. Coverity Connect uses the Java Secure Socket Extension
(JSSE) format to manage certificates and key stores. The J2SE SDK ships with the
`keytool` utility, which enables you to set up and work with JSSE
digital certificates.

There are two scenarios for certificates for setting up SSL/TLS: LDAP server authentication and client authentication, in which Coverity
Connect is the client. In both scenarios, a truststore is required. A basic set of steps
for accessing an LDAP server via SSL is outlined below, with additional details
available in the subsequent sections:

Note: The examples in the following section use Linux-based syntax. The Windows syntax is
different. For example in Linux, the following
configuration:

```
-Djavax.net.ssl.trustStore=<install_dir>/config/LDAP_cers.jks
```

Would
be represented in Windows as the
following:

```
-Djavax.net.ssl.trustStore=drive\:install_dir\\config\\LDAP_cers.jks
```

A backslash is required in front of the colon (:) and each of the path
separators.

1. Set up your certificates,
   1. If a truststore is not provided for you, use the `keytool` utility to create the
      truststore; it may be a randomly chosen file and location. For example:

      ```
      export trst=<install_dir>/config/LDAP_cers.jks
      export kt=<install_dir>/jre/bin/keytool
      $kt -genkeypair -keyalg key_algorithm -dname "CN=some_user, OU=People, DC=somedom, DC=com" -keystore
      $trst -storepass store_password -keypass key_password -alias some_user-keypair
      ```

      See "Using a truststore" for more information.
   2. Import the some_user client certificate.

      ```
      $kt -importcert -trustcacerts -file some_user_client.cer -keystore $trst -storepass store_password -alias some_user_client_key
      ```
   3. Import the LDAP server Root CA.

      ```
      $kt -importcert -trustcacerts -file LDAP_Root_CA.cer -keystore $trst -storepass store_password -alias LDAP_Root_CA_key
      ```
   4. Set the needed info in the system.properties file, located in
      <install_dir>/config.

      ```
      java_opts_post=-Djavax.net.ssl.trustStoreType=jks \
      -Djavax.net.ssl.trustStore=<install_dir>/config/LDAP_cers.jks \
      -Djavax.net.ssl.trustStorePassword=store_password
      ```

      See "Client authentication" for more details.
2. Restart Coverity Connect.
3. Create a new LDAP configuration and set the needed login option for the LDAP. See
   Configuring LDAP server settings for more
   information.

## Using a truststore

Both server authentication and client authentication can use the default JSSE truststore.
The truststore is in a JKS format file and contains the root or intermediate CA
certificates. These CA certificates determine which endpoints are allowed for
communication.

Coverity Connect connects to the LDAP server, which presents a certificate that is signed
by one of the truststore's CA certificates. Using this truststore, Coverity Connect
attempts an SSL handshake with all LDAP servers that present a certificate signed by the
CA. JSSE looks for the truststore as follows:

1. If the javax.net.ssl.trustStore system property is defined,
   then the value of this property is used as the truststore's location.
2. If the lib/security/jssecacerts file is defined in the
   java.home directory, then the
   jssecacerts file is used as the truststore.
3. If the file lib/security/cacerts file is defined in the
   java.home directory, then the
   cacerts file is used as the truststore.

You can also use a custom truststore in the Coverity Connect server to accept a generated
certificate. To do so:

1. Use the `keytool` utility to generate the truststore. For more
   information, see the `keytool` documentation at <http://download.oracle.com/javase/6/docs/technotes/tools/windows/keytool.html>.
2. Import the certificate into the newly created truststore.
3. Edit the java_opts_post property in the Coverity Connect
   system.properties file to define the location of the
   truststore. By default, system.properties is located at
   <install_dir>/config. For example:

   ```
   java_opts_post=-Djavax.net.ssl.trustStoreType=jks \
   -Djavax.net.ssl.trustStore=/openldap-cert/truststore.jks \
   -Djavax.net.ssl.trustStorePassword=adminadmin
   ```

   Note: Do not use quotation marks (" ") to specify a full
   path or other multiple string values. If a path contains spaces (for
   example, Program Files), use an equivalent path without
   spaces (for example, Progra~1) or change to a location
   that does not contain spaces.
4. Stop and restart Coverity Connect.

   For more information, see Stopping and starting Coverity Connect.

## LDAP server authentication

With server authentication, client certificate authentication is not enforced, meaning the
LDAP server does not expect to receive a certificate from Coverity Connect for authentication. Coverity Connect
verifies that any SSL/TLS-enabled LDAP server is valid. The truststore must be
available, as specified in "Using a truststore."

## Client authentication

With client authentication, Coverity Connect must provide a certificate for
authentication. The truststore needs to have the Certificate Authority certificate
available in it. Through this truststore, Coverity Connect verifies the server that is
responding to the request. Coverity Connect must have a keystore, which contains the
private and public key pair.

The separation of the truststore and keystore is not mandatory, but it is recommended.
They can be the same physical file.

1. Use the `keytool` utility to create the keystore.
2. Import the certificate into the keystore.
3. Edit the java_opts_post property in the Coverity Connect
   system.properties file to define the location of the
   keystore. By default, system.properties is located at
   <install_dir>/config. For example:

   ```
   java_opts_post=-Djavax.net.ssl.keyStoreType=jks \
   -Djavax.net.ssl.keyStore=/openldap-cert/keystore.jks \
   -Djavax.net.ssl.keyStorePassword=adminadmin
   ```

   Note: Do not use quotation marks (" ") to specify a full
   path or other multiple string values.
4. Stop and restart Coverity Connect.

   For more information, see Stopping and starting Coverity Connect.
