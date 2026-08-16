---
title: "Scenario 2. Replacing the keystore"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-2.-replacing-the-keystore.html"
content_id: "d1L7OhDSboDNk9RvRb6euw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:31.846456+00:00"
---

# Scenario 2. Replacing the keystore

Use this scenario to generate a new private key and keystore: For example, if the old key
should not be reused because of security policy or because the key was compromised),
or if you are switching to a new certificate without retaining any old keystore data.

This scenario also applies if you are enabling SSL for the first time on Coverity Connect,
and you need to create a keystore from scratch.

## Prerequisites

Scenario 2 has no prerequisites except that the [Java keytool](http://docs.oracle.com/javase/6/docs/technotes/tools/solaris/keytool.html) must be available.

## Steps

1. **Back up the old keystore and then remove it:**

   If there was no existing keystore file (if TSL/SSL wasn’t set up yet), you can skip this step,
   but do make sure that the conf/ directory is ready to receive a new keystore.

   As noted in the preparation section, rename or
   move the old keystore file (keystore.jks) so it won't be overwritten accidentally and so that you start fresh.

   For example:

   - On Windows, open a Command Prompt and navigate to the conf\ directory,
     then rename keystore.jks to keystore.jks.bak.
   - On Linux, in the conf/ directory, run `mv keystore.jks keystore.jks.bak`.
2. **Create a new Java Keystore:**

   The new keystore must have a new private key.

   Use the `keytool -genkeypair` option to generate a new key pair (a private key plus a self-signed certificate) in the new keystore.

   This step also creates the keystore file. For example:

   ```
   keytool -genkeypair -alias tomcat -keyalg RSA -keysize 2048 -keystore "<cc_install_dir>/server/base/conf/keystore.jks" \
       -validity 365 -storepass changeit -keypass changeit
   ```

   Here is an explanation of the various arguments to `keytool`:

   `-genkeypair`
   :   Creates a key pair and a self-signed certificate.

   `-alias tomcat`
   :   Sets the alias for this key entry as `tomcat`.

       Using `tomcat` is a common choice for Tomcat servers, but you can choose another alias if you
       so desire—just be sure to remember the new alies for use in later steps.

   `-keyalg RSA -keysize 2048`
   :   Specifies an RSA key of 2048 bits, which is a standard secure key size.

   `-keystore <...>keystore.jks`
   :   Is the path to the keystore file to create.

       This example creates it directly in the Coverity conf/ directory for convenience.

   `-validity 365`
   :   Sets the self-signed certificate to be valid for 365 days.

       The duration of the self-signed cert is not a critical value if you are planning to replace the certificate with a CA-signed certificate,
       but this value can be useful if you end up using the self-signed certificate for a certain period of time.

   `-storepass changeit`
   :   Sets the keystore password to `changeit`.

       After you have run `keytool` to create the key pair and the key store,
       choose a different, stronger password and then update the Tomcat configiratop to use that one.

   `-keypass changeit`
   :   Sets the private key's password (key entry password).

       It is simplest to use the same password as the keystore password:
       By default, Tomcat expects the key password to be the same as the keystore password unless you specify otherwise.

   After you invoke `keytool` in this way, it prompts you to provide some information to include in the certificate
   (since at the outset it is generating a self-signed certificate).
   You will see prompts such as, `Enter your first and last name [Unknown]:`.

   Important:
   For `first and last name`, *enter the host name (domain) that the certificate will secure* (this is the Common Name).
   For example, if users access Coverity at coverity.company.com, enter that.
   If you don't have a DNS name and use an IP (we do not recommended using an IP for certificates), you might enter the IP.

   The `keytool` also prompts you to enter organizational information: **Organizational Unit**, **Organization**, **City**,
   **State**, **Country**.
   Fill these out as appropriate for your company or use the defaults if this is just for a temporary certificate.
   These details will appear in the CSR and the certificate.

   Finally, `keytool` asks you to confirm that the information is correct.
   Type `yes` and then press `Enter`.

   As the result of invoking `keytool` as just described, it creates a new file named keystore.jks.
   The new file is saved in the conf/ directory.
   It contains a single entry: a private key and a self-signed certificate that has the alias `tomcat`.

   Note:
   The self-signed certificate is just a placeholder used to populate the keytstore.
   In subsequent steps, we will replace it with the CA-signed certificate.
3. **Create a Certificate Signing Request (CSR) for the new key:**

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
   2. Send the request to your CA.

      Use the process your authority prefers: either a web site or email.

      Before you submit, make sure the Common Name (CN) in the CSR corresponds to the domain name
      or server name used to access Coverity (for example, coverity.yourcompany.com).
      If you used keytool without specifying a DN (Distinguished Name), it likely prompted you to enter First and Last Name—this should be
      *the server’s domain name* and not actually your personal name.
   3. Wait for the CA to provide the new certificate files.

      The Certificate Authority might give you a .cer/.crt certificate,
      and possibly an intermediate certificate or a bundle.

      For example, you might receive a ZIP that contains your_domain.crt and
      your_domain.ca-bundle or something similar. Once you have the new certificate from the CA, proceed to step 4.
4. **Import the Certificate Authority's certificates into your new keystore:**

   Before you import the new certificate, it is a good practice to make sure that the keystore trusts the intermediate certificates
   (if there are any). Many public intermediate certificates are already trusted by Java, but if your Certificate Authority provided an intermediate certificate, import it first as a trusted cert:

   If an intermediate CA certificate file was provided (for example, IntermediateCA.crt or IntermediateCA.pem),
   import it into the keystore with a distinct alias; for example:

   ```
   keytool -importcert -alias intermediateCA -keystore "<Coverity_install_dir>/server/base/conf/keystore.jks" -file IntermediateCA.crt \
       -noprompt -trustcacerts
   ```

   Use a descriptive alias such as intermediateCA.
   The `-trustcacerts` flag tells keytool to treat it as a trusted certificate.

   If the intermediate certificate is already in the keystore or is known, `keytool` will warn you or prompt you to overwrite it.
   Usually you can proceed with trust. If your Certificate Authority provides multiple intermediates, import each one, using a unique alias for each.
5. **Import the new server certificate into the keystore:**

   Now import the actual certificate for the Coverity Connect server: the one issued to your server's name.

   This step replaces the old certificate while keeping the existing private key in place.

   Important:
   When you run `cov-import-cert`, *use the same alias that your private key uses*.
   This is critical: The new certificate must be imported to exactly the same alias entry as the existing key;
   otherwise, it won't match the original key.

   For example, if your alias is `tomcat` (which is likely to be the case if you followed the default Tomcat setup), use that.
   For example:

   ```
   keytool -importcert -alias tomcat -keystore "<Coverity_install_dir>/server/base/conf/keystore.jks" -file YourNewCert.crt
   ```

   This command tells `keytool` to import the certificate from YourNewCert.crt into the keystore.
   The `keytool` will try to match it to an existing key that has the alias `tomcat`.

   - The `keytool` might display the prompt `"Certificate already exists, overwrite? [no]:"`.
     If it does, type `yes` and then press `Enter` to overwrite the old certificate with the new one.
     (The private key remains in the keystore.)
   - If the `keytool` prompts `"Trust this certificate?"` that means it doesn't recognize the issuer.
     If you imported the intermediates as above, or if the certificate is self-signed, you need to confirm trust by typing `yes`.
   - If your intermediate was properly imported first, and the certificate links to it, the `keytool>` should report,
     `"Certificate reply was installed in keystore"` without asking for trust.

   After importing, you should see a message that says, `"Certificate reply was installed in keystore"`.
   This indicates success.

   Note:
   If your CA provided the certificate in a PKCS#7 (.p7b) bundle or a single file containing the full chain,
   you can use that file in the `-file` option.
   A .p7b file often contains the entire chain;
   `keytool` will import the chain automatically in that case.

   Here is an example of importing a bundle:

   ```
   keytool -importcert -alias tomcat -keystore keystore.jks -file YourCertBundle.p7b
   ```

   The process is similar to the previous steps: Just make sure that the alias matches the existing key.
6. **Verify the new keystore contents:**

   After importing, it is also a good idea to check that the keystore has the
   new certificate in place. Use the following command line to list the
   keystore entries:

   ```
   keytool -list -v -keystore "<Coverity_install_dir>/server/base/conf/keystore.jks"
   ```

   When prompted, enter the keystore password.

   In the output, find the entry for your alias (for example,
   `tomcat`). The entry should show the
   `Subject` of your new certificate (your server’s name)
   and the `Valid from` dates that correspond to the new
   certificate's validity period. You should also see the certificate chain
   details (the issuer, possibly including the intermediate CA you imported,
   and so on). This confirms that the new certificate is in place.

   If everything looks correct (new expiration date, correct issuer), you have
   successfully updated the keystore.
7. **Update the Apache Tomcat configuration for the new keystore:**

   Since you have reused the same keystore file and alias, it is not likely that you need to change the server.xml configuration
   (it already points to this keystore).On the other hand, it is wise to double-check the Tomcat settings.

   In Apache Tomcat, go to **Configuring Tomcat** → **Use the New Keystore (server.xml)** and verify
   the server.xml **Connector** settings, especially if you changed the keystore password
   or if the alias is not the default.

   Once you verify the configuration, you can continue with the steps in
   Restarting Coverity Connect and verifying the new certificate.
