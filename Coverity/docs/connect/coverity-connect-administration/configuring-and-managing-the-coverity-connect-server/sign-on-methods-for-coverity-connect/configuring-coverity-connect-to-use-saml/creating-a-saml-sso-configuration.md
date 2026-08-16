---
title: "Creating a SAML SSO configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-a-saml-sso-configuration.html"
content_id: "B0kKIBzksxKOkz3VR1XRow"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:50.861987+00:00"
---

# Creating a SAML SSO configuration

**Within Coverity Connect, name the configuration and begin SP setup:**

1. Choose a Display Name for this configuration, and enter
   it.
2. Choose an SP Entity ID, and enter it.

   The SP Entity ID should be unique to this Coverity Connect
   server.
3. Click Download SP Metadata, and save this XML file in a
   convenient directory, such as Downloads/. The default name
   of this file is spring_saml_metadata.xml

   If prompted, you can open the metadata file in an application, but be sure to
   save it to your system as well, and be sure that the file name you save has a
   .xml extension.

   CAUTION:

   The first time you click Download for a
   new configuration, the metadata is appropriate to the *previous* SAML SSO
   configuration, if any. You have to finish creating the configuration, and click
   Done, before the metdadata is completely up to
   date.

   While setting up the new configuration, the information you need
   from the SP metadata is the `Location` string, and this value
   should always remain the same.

**Within the IdP interface, identify Coverity Connect as the service provider, and
download IdP metadata:**

Note: The details of these steps might vary, depending on which IdP you use.

1. Open your identity provider application or Web page.
2. Open the SP metadata file in a text editor, and find the
   `Location` string. Usually this string appears near the
   bottom of the file. Copy the value of the string (do not include the
   quotes).

   The URL for the SP metadata has the format,
   `Location="https://<host>:<port>/login/saml2/sso/default_registration_id"`.
   For example, you might copy the string
   `https://testServer:2403/login/saml2/sso/default_registration_id`.
3. In the identity provider app, paste the `Location` string in the
   appropriate field.
4. Also in the identity provider, download the IdP metadata and save it to a
   convenient location such as the Desktop.

   For example, the name of this file might be
   oktaMetadata.xml.

   Note: If the identity provider allows, you might also download the certificate in
   the PEM format.
5. You can now close the identity provider app, unless you have more work you want
   to do, there.

**Back in Coverity Connect, complete the configuration:**

1. Return to the SAML Configuration page for Coverity
   Connect.
2. Open the IdP metadata file in a text editor, and find the
   `entityID` string. Usually this string appears near the top
   of the file. Copy the value of the string (do not include the quotes).

   For example, if the IdP metadata specifies
   `entityID="http://www.okta.com/exk11b1dcd8vf5O22577"`, copy
   the string
   `http://www.okta.com/exk11b1dcd8vf5O22577`.
3. Click the Browse button labeled IdP
   Metadata.

   Coverity Connect displays a file dialog. Navigate to the directory where you
   saved the IdP metadata, highlight its name, and then click
   Open.

   If loading this metadata is successful, the label below the
   Browse button changes from Metadata
   unavailable to Metadata
   available.
4. In the Coverity Connect SAML Configuration page, you can
   now click Done.

**Instruct Coverity Connect to begin using SAML SSO:**

1. Choose Configuration > System once again.
2. At the left of the Configuration > System dialog, click to highlight Authentication and Sign
   In.
3. Choose SAML from the Authenticate
   with: drop-down list.

     
    [image: image]   

   Single sign-on is not available to users until you have made this
   change.
4. (Optional) Click to turn on Create SAML users automatically on sign
   in.

   While this option is active, when a user firsts signs in, Coverity Connect links
   the SSO user to an existing Coverity Connect user, if there is a user-name
   match, or it creates a new Coverity Connect user to match the SSO user.

   Note: When a user's login is typically their email address
   (`alice@email.com`), then they can log in via SSL, and be
   recognized by Coverity Connect, using just the username portion of that address
   (`alice`).

   It is more time consuming, but also possible, to create individual users by hand
   within the Coverity Connect interface. See Associating an SAML SSO configuration with an individual Coverity Connect user
5. (Optional) Click to turn on Disable all sign in types except for
   SAML.

   When this option is active, users can still use the Coverity API,
   `cov-manage-im`, `cov-commit-defects`, and
   `cov-run-desktop`.

   When this option is active in the modern UI, the login page
   shows only a Sign in with SSO button with no username and
   password fields. Only the built-in admin account can log in locally, not all
   administrators.
6. Click Done once more.
