---
title: "Scenario 3. No existing keystore"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-3.-no-existing-keystore.html"
content_id: "QEZUiopu4MWmmbsACIIkxQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:32.545927+00:00"
---

# Scenario 3. No existing keystore

Use this scenario if your Certificate Authority (CA), or your organization's IT security team has given you a certificate file and a private key file, but not a Java keystore.

This situation can arise if the Certificat Signing Request (CSR) was generated outside of the Coverity server—for example, by using OpenSSL on a different machine
To accomplish this, we'll use OpenSSL and Java Keytool.

## Prerequisites

You should have the following items:

- The server certificate file, such as yourserver.crt or yourserver.pem.

  If you have not yet obtained your new certification, please look at the next section, "Steps", which describes how to generate a
  Certificate Signing Request (CSR),
- The private key file that corresponds to the certificate: for example, yourserver.key or perhaps a .pem that contains the key.

  This key is sensitive data. *Keep it secure.* If it was provided by your Certificate Authority or your IT team, they should have delivered it in a secure manner.
- The intermediate CA certificate file, if the Certificate Authority (CA) uses one.

  Sometimes this is named CABundle.pem or has a similar name.
- An [OpenSSL](https://www.openssl.org/docs/manmaster/man1/openssl-x509.html) installation.

  On a Linux system, this is typically installed by default.

  On a Windows system, you might need to install it.
  See Before you begin to update the TLS/SSL certificate: Preparation and essential concepts for more details.

## Steps

1. **Generate a Certificate Signing Request (CSR):**

   You can skip this step if you have already obtained a certificate or a request for one.

   The CSR is a file that you send to the Certificate Authority so they can issue a certificate for your server.

   1. To generate the CSR, run the following command, adjusting the paths and
      the alias as needed:

      ```
      keytool -certreq -alias tomcat -keystore "<Coverity_install_dir>/server/base/conf/keystore.jks" -file coverity.csr
      ```

      When prompted, enter the keystore password.

      This generates coverity.csr in the current
      directory. The CSR file contains your public key and the information
      needed for the CA to issue a certificate.
2. **Send the request to your CA:**

   Use the process your authority prefers: either a web site or email.

   Before you submit, make sure the Common Name (CN) in the CSR corresponds to the domain name
   or server name used to access Coverity (for example, coverity.yourcompany.com).
   If you used keytool without specifying a DN (Distinguished Name), it likely prompted you to enter First and Last Name—this should be
   *the server’s domain name* and not actually your personal name.

   Wait for the CA to provide the new certificate files.

   Once you have the new certificate from the CA, proceed to step 3.
3. **If the new certificate is a binary file, convert it to text format:**

   By default, many Certificate Authorities provide the certificate in
   .PEM format. If the file is in
   .PEM format, it will be readable by a text editor
   and begin with the line, `-----BEGIN CERTIFICATE-----`. The
   certificate might be a .CRT file that also is readable
   by a text editor and begins with `-----BEGIN
   CERTIFICATE-----`. If your new certificate is already in a text
   format, you can skip ahead to step 4. Otherwise, if the certificate is a
   binary file (for example, a .CER file that a text
   ediitor can't open, you need to convert it to a .PEM
   file.

   Note: The binary encoding of a certificate is also known as DER, for
   *Distinguished Encoding Rules*.

   1. Use the OpenSSL utility to convert the .CER file
      to .PEM format. For example:

      ```
      openssl x509 -inform DER -in <yourserver>.cer -out <yourserver>.pem
      ```
   2. Make sure that the <yourserver>.pem file is
      a text file: Open it with a text editor and confirm that the first line
      is `-----BEGIN CERTIFICATE-----`.
   3. If your Certificate Authority provided an intermediate certificate,
      convert it to .PEM format in the same way.
   4. Make sure that your private key is also in .PEM
      format: Open it with a text editor and confirm that the first line is
      either `-----BEGIN PRIVATE KEY-----` or
      `-----BEGIN RSA PRIVATE KEY-----`.

      Sometimes the
      private key is sent in a binary format. This is uncommon, but if
      your private key is not text, use the OpenSSL utility to convert it
      to .PEM format as well.

   At this point, you should have the following components:

   - <yourserver>.pem
   - intermediate.pem (if you received an intermediate
     certificate)
   - <privatekey>.pem

   All of them are in .PEM text format.
4. **Combine the server and intermediate certificate into a single file (a full chain):**

   Note:
   This step is not strictly required, but it simplifies use of the OpenSSL utility.

   Concatenate the certificate and the intermediate certificate into a single file, fullchain.pem.
   If you were not given an intermediate certificate, skip ahead and use <yourserver>.pem
   as the input to step 5.

   - **On Linux:**

     Enter the following at a command prompt:

     ```
     cat <yourserver>.pem intermediate.pem > fullchain.pem
     ```
   - **On Windows:**

     Enter the following at a command prompt:

     ```
     <yourserver>.pem intermediate.pem > fullchain.pem
     ```

   Make sure that in fullchain.pem, the server's certificate comes first, followed by the intermediate certificate's block of text.
5. **Create a PKCS#12 keystore that contains both your key and your certificate:**

   Create a .P12 keystore using OpenSSL.

   A PKCS#12 file (usually having a filename extension of .p12 or .pfx)
   can hold a private key and a certificate together, and Apache Tomcat can use this format.

   Run the following OpenSSL command:

   ```
   openssl pkcs12 -export -in fullchain.pem -inkey <yourserver>.key -out coverity.p12 -name tomcat
   ```

   Here is an explanation of the various arguments to `openssl`:

   `pkcs12`
   :   Specifies creation of a keystore in PKS#12 format.

   `-export`
   :   Specifies creation of an export file.

   `-in fullchain.pem`
   :   Imports the certificate or certificate chain that you created in step #4.

   `-inkey <yourserver>.key`
   :   Specifies the private key to include in the keystore.

   `-out coverity.p12`
   :   The name of the keystore to create.

   `-name tomcat`
   :   The alias of the key contained in the new keystore.

   `openssl` prompts you to create an export password for the new .P12 file.
   Choose a strong password and remember it. This password will be needed whenever you import into a Java keystore ,
   and will be needed by Tomcat if you use the `.P12` directly.

   For simplicity, you might use the same password as your old keystore or the default (`Coverity`),
   but because this is a new file, using a stronger custom password is a good idea—just be sure to update the Tomcat configuration accordingly.

   1. The new keystore, coverity.p12, should contain your key and your certificates.

      Double-check this by listing its contents:

      ```
      openssl pkcs12 -info -in coverity.p12 -nomacver
      ```

      OpenSSL prompts for the password you just set and then shows the certificates and the alias inside, without showing the private key in plaintext.

      If all appears correct, proceed to step 6.
6. **Convert the new keystore into a Java KeyStore (JKS) file:**

   Apache Tomcat can use a PKCS#12 file directly. But to align with the default
   Coverity setup, which expects a JKS file named
   keystore.jks, convert the new keystore to JKS
   format.

   - Use the `keytool` command to convert the keystore:

     ```
     keytool -importkeystore -srckeystore coverity.p12 -srcstoretype PKCS12 -destkeystore keystore.jks -deststoretype JKS
     ```

     The `keytool` command will prompt for some passwords:

     - The source keystore password:

       Enter the export password you
       set for coverity.p12 in step 4.
     - A destination keystore password.

       Choose a password for the
       new JKS (you can use `Coverity` for
       consistency or choose a new one. If the password is new,
       you'll need to add that to your Tomcat configuration.

       The `keytool` ommand might ask you to confirm
       the new password.
     - If `keytool` asks for an alias, it should carry
       over the alias `tomcat` automatically, because we
       set `-name tomcat` when exporting the
       .P12 file.

       In most cases, you will
       see a message that says one entry with the alias
       `tomcat` was imported successfully.

   The new keystore.jks file has now been saved in the
   current directory. Move or copy keystore.jks to the
   Coverity
   server/base/conf directory.

   If you need to, you may replace the keystore. For example, you may replace a prior keystore by moving a new one to
   <cc_install_dir>/server/base/conf/keystore.jks.
7. **Verify the new keystore contents:**

   After importing, it is also a good idea to check that the keystore has the new certificate in place.
   Use the following command line to list the keystore entries:

   ```
   keytool -list -v -keystore "<Coverity_install_dir>/server/base/conf/keystore.jks"
   ```

   When prompted, enter the keystore password.

   In the output, find the entry for your alias (for example, `tomcat`).
   The entry should show the `Subject` of your new certificate (your server’s name) and the `Valid from` dates
   that correspond to the new certificate's validity period.
   You should also see the certificate chain details (the issuer, possibly including the intermediate CA you imported, and so on).
   This confirms that the new certificate is in place.

   If everything looks correct (new expiration date, correct issuer), you have successfully updated the keystore.
8. **Update the Apache Tomcat configuration for the new keystore:**

   Attention:
   For Scenario 3, the steps to configure Apache *are considerably different,* and more complicated, than they
   are for Scenarios 1 and 2. Please follow the steps that follow carefully.

   Once your keystore has been prepared with the new certificate, you must ensure that Apache Tomcat,
   which powers Coverity Connect, is configured to use the updated keystore.
   This involves editing the server.xml file so that it points to the keystore file, setting the password,
   and enabling the SSL connector if it is not already enabled.

   1. In a text editor, open server.xml.

      This file is stored at <cc_install_dir>/server/base/conf/server.xml.

      - On Linux, use `sudo`; for example,

        ```
        sudo nano server.xml
        ```
      - On Windows, you might need to open the file as Administrator, so that you can save your changes.
   2. Find the HTTPS Connector configuration:

      Search within server.xml for a line that contains `8443` or `SSLEnabled`.

      For example, look for `<Connector port="8443"`.
      This is the default HTTPS port for Coverity Connect
      (some installations might use port 443 or another port value, but 8443 is typical).

      You should find a block that looks similar to the following code:

      ```
      <!-- Define a secure SSL/TLS HTTP/1.1 Connector on port 8443 -->
      <Connector port="8443" protocol="HTTP/1.1" SSLEnabled="true" \
      keystoreFile="conf/keystore.jks" keystorePass="changeit" keystoreType="JKS" keyAlias="tomcat" \ 
      secure="true" scheme="https" clientAuth="false" sslProtocol="TLS"/>
      ```

      Note:
      If TLS/SSL had not been enabled previously, this block might be commented out.
      If it is, remove the comment delimiters.
   3. Update the Connector settings:

      Edit the `Connector port` line to match the details of the new keystore.
      In particular:

      - Make sure that the `Connector port` port value is correct.

        On a Linux system, using a port value of 443 might require special permissions:
      - The path in `keystoreFile` must point to the new keystore file location.
        This path can be either absolute or relative.
        For example:

        ```
        keystoreFile="<cc_install_dir>\server\base\conf\keystore.jks"
        ```
      - Set the value of `keystorePass` to the password for your keystore file.
        For example, if you used the default or kept it the same, the setting might be `keystorePass="changeit"`.
        If you chose a new password (or if the CA provided a .P12 file with a password chosen by you), enter that here.

        Make sure the password value is enclosed in quotes and matches exactly; otherwise, Tomcat won't be able to open the keystore.

        This file includes the password as plain text.
        Make sure that the file is accessible only to the Coverity service account.
      - `keystoreType="JKS"`: This is the default value.
      - `keyAlias`: By default, Tomcat uses the first key entry in the keystore.
        Often this is the only entry.
        A keystore can contain multiple entries: If this is the case, this option *must* specify which alias to use.
        This value is case-sensitive.
   4. Save server.xml and then close the editor.

      Double-check that your updates were saved, and that there are no XML syntax errors, which can prevent
      Tomcat from opening the file.

   At this point, Coverity Connect is configured to use your new keystore and certificate.
   Now is the time to restart the service and verify that everything works:
   See Restarting Coverity Connect and verifying the new certificate.
