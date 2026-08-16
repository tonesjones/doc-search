---
title: "Before you begin to update the TLS/SSL certificate: Preparation and essential concepts"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/before-you-begin-to-update-the-tls/ssl-certificate-preparation-and-essential-concepts.html"
content_id: "C6DsVJNC9udFqvNj5jqvVw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:29.767734+00:00"
---

# Before you begin to update the TLS/SSL certificate: Preparation and essential concepts

1. **Plan for downtime:**

   Updating the certificate requires you to restart the Coverity Connect service.
   Plan a maintenance window to avoid user impact.
2. **Back up important files:**

   Before you make any changes, back up the existing keystore file and configuration, as follows:

   1. Locate the Coverity Connect installation directory.

      By default, for both Windows and Linux the keystore is at: <cc_install_dir>\server\base\conf\keystore.jks.
      (This path might vary on your local system.)
   2. Make a copy of keystore.jks (or which keystore file is in use) and store it in a safe location.

      For example, you might name the backup file keystore.jks.bak.
   3. Also back up the Apache Tomcat configuration file server.xml.

      With a backup, you can restore server.xml if something should go wrong.

      This file is located in the same conf\ directory as the keystore.
3. **Make sure you have the tools you will need:**

   The toools you will need are as follows:

   - [Java keytool](http://docs.oracle.com/javase/6/docs/technotes/tools/solaris/keytool.html)

     This is the Java utility for keystore and certificate management. It comes with any Java JDK/JRE installation.

     If Coverity is installed with a JRE, you can find Keytool in the JRE’s bin folder: for example, <cc_install_dir>/jre/bin/keytool.

     Be sure to run the commands with a user account that has permission to read and write the Keystore file
     (on Windows, running as Administrator; or on LInux, using `sudo`).
   - [OpenSSL](https://www.openssl.org/docs/manmaster/man1/openssl-x509.html)

     OpenSSL is a tool to manage certificates and keys.

     On Linux, it is often pre-installed.
     On Windows, it is not built-in: You can install it by using Windows OpenSSL binaries or by using Git Bash or
     WSL (Windows Subsystem for Linux).

     OpenSSL is especially useful for Scenario 3, in which you need to combine a separate key and certificate into a keystore.
4. **Know your current keystore password:**

   For the keystore to import new certificates or to create a new certificate, you will need to specify the password.
   You will also need the password when you follow the steps that follow in the scenarios.
5. **Obtain the new TSL/SSL certificate from your Certificate Authority (CA):**

   Make sure you have obtained the files for the new certificate. Typically, you will need the following items:

   - Your server certificate (a .pem file, which can be in either binary or text format).

     This is sometimes called the “SSL certificate” for your Coverity Connect server’s host name.
   - The intermediate certificate, if your Certificate Authority uses an intermediate.

     It’s important to have the intermediate certificate so that client browsers can trust the full chain.

     Some Certificate Authorities provide a combined "bundle": a .pem file that contains both the intermediate and root certificates.
   - (Possibly) a root certificate.

     For a publicly trusted Certificate Authority, usually you don’t need to install the root manually,
     but if the Certificate Authority is internal or private, you might have to include a root certificate as well.
   - (Possibly) a separate private key file that is provided or generated outside of Coverity.

     This is required by Scenario 3.
6. **Stop the Coverity Connect service:**

   Before you proceed with any changes, stop the Coverity Connect web server to avoid any file locks or active use of the old certificate.

   1. Use the `cov-stop-im` command to shut down the Coverity Connect server.
   2. Before you continue, verify that the web interface is no longer available.
