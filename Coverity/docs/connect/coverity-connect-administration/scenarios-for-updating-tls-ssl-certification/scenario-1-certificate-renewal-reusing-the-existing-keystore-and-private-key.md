---
title: "Scenario 1. Certificate renewal: Reusing the existing keystore and private key"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-1.-certificate-renewal-reusing-the-existing-keystore-and-private-key.html"
content_id: "Xp7vNu0_UjtsspUVA5s4mQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:31.125678+00:00"
---

# Scenario 1. Certificate renewal: Reusing the existing keystore and private key

Use this scenario if you want to continue using the same private key and keystore file as before.
This is a common scenario when renewing an expiring certificate that can use the same key.
In this scenario, your keystore already contains the private key:
You just need to import the new certificate (signed by the Certificate Authority) that matches that key.

## Prerequisites

Per the steps in Before you begin to update the TLS/SSL certificate: Preparation and essential concepts, you should have the existing keystore
(the keystore.jks file), and know its password.
Ideally, you will already have received the new certificate from the Certificate Authority (CA).

If you have not yet obtained your new certification, please look at the next section, "Steps", which describes how to generate a
Certificate Signing Request (CSR),

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
   2. Send the request to your CA.

      Use the process your authority prefers: either a web site or email.

      Before you submit, make sure the Common Name (CN) in the CSR corresponds to the domain name
      or server name used to access Coverity (for example, coverity.yourcompany.com).
      If you used keytool without specifying a DN (Distinguished Name), it likely prompted you to enter First and Last Name—this should be
      *the server’s domain name* and not actually your personal name.
   3. Wait for the CA to provide the new certificate files.

      The Certificate Authority might give you a .cer/.crt certificate,
      and possibly an intermediate certificate or a bundle.

      For example, you might receive a ZIP file that contains your_domain.crt and
      your_domain.ca-bundle or something similar. Once you have the new certificate from the CA, proceed to step 2.
2. **Import the new CA certificate chain into the keystore:**

   Before you import the new certificate, it is a good practice to make sure that the keystore trusts the intermediate certificates
   (if there are any). Many public intermediate certificates are already trusted by Java, but if your Certificate Authority provided an intermediate certificate, import it first as a trusted cert:

   If an intermediate CA certificate file was provided (for example, IntermediateCA.crt or IntermediateCA.pem),
   import it into the keystore with a distinct alias; for example:

   ```
   keytool -importcert -alias intermediateCA -keystore "<Coverity_install_dir>/server/base/conf/keystore.jks" -file IntermediateCA.crt -noprompt -trustcacerts
   ```

   Use a descriptive alias such as intermediateCA.
   The `-trustcacerts` flag tells keytool to treat it as a trusted certificate.

   If the intermediate certificate is already in the keystore or is known, `keytool` will warn you or prompt you to overwrite it.
   Usually you can proceed with trust. If your Certificate Authority provides multiple intermediates, import each one, using a unique alias for each.
3. **Import the new server certificate into the keystore:**

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
4. **Verify the keystore content:**

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
5. **Update the Apache Tomcat configuration for the new keystore:**

   Since you have reused the same keystore file and alias, it is not likely that you need to change the server.xml configuration
   (it already points to this keystore).On the other hand, it is wise to double-check the Tomcat settings.

   In Apache Tomcat, go to **Configuring Tomcat** → **Use the New Keystore (server.xml)** and verify
   the server.xml **Connector** settings, especially if you changed the keystore password
   or if the alias is not the default.

   Once you verify the configuration, you can continue with the steps in
   Restarting Coverity Connect and verifying the new certificate.
