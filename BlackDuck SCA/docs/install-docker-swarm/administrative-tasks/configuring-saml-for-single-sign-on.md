---
title: "Configuring SAML for Single Sign-On"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-saml-for-single-sign-on.html"
content_id: "T54iHpGPpyQoBWEPXjwBmA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:55.954706+00:00"
---

# Configuring SAML for Single Sign-On

Security Assertion Markup Language (SAML) is an XML-based, open-standard data format for
exchanging authentication and authorization data between parties. For example, between
an identity provider and a service provider. Black Duck SCA's SAML
implementation provides single sign-on (SSO) functionality, enabling Black Duck SCA users to be automatically signed-in to Black Duck SCA when SAML is enabled. Enabling SAML applies to all your
Black Duck SCA users and cannot be selectively applied to individual
users.

All hosted customers should secure access to their Black Duck SCA application by
leveraging our out-of-the-box support for single sign on (SSO) via SAML or LDAP.
Information on how to enable and configure these security features can be found in the
installation guides. In addition, we encourage customers that are using a SAML SSO
provider that offers two-factor authorization to also enable and leverage that
technology to further secure access to their Black Duck SCA application.

Note the following:

- It is not possible to configure both SAML and LDAP
  at the same time.
- To enable or disable SAML functionality, you must be a user with the system administrator
  role.
- Black Duck SCA is able to synchronize and obtain an
  external user's information (Name, FirstName, LastName and Email) if the
  information is provided in attribute statements. Note that the first and
  last name values are case-sensitive.

  Black Duck SCA is also able to synchronize an
  external user's group information if you enable group synchronization in Black Duck SCA.
- When logging in with SAML enabled, you are re-directed to your identity
  provider's login page, not Black Duck SCA's login page.
- When SSO users log out of Black Duck SCA, a logout page now
  appears notifying them that they successfully logged out of Black Duck SCA. This logout page includes a link to log back
  into Black Duck SCA; users may not need to provide their
  credentials to successfully log back in to Black Duck SCA.
- If there are issues with the SSO system and you need to disable the SSO configuration, you
  can enter the following URL to log in to Black Duck SCA:

  ```
  <Black Duck servername>/ui/login
  ```

## Enabling or disabling single sign-on using SAML

1. Click [image: Administration icon] .
2. Select **Integrations** → **External Authentication**.
3. Click **Security Assertion Markup Language (SAML)**, complete the following:

   1. Select the **Enable SAML configuration** check box.
   2. **Service Provider Entity ID** field: Enter the information for the
      Black Duck SCA server in your environment in the
      format **https://*host*** where *host* is your Black Duck SCA server.
   3. Select one of the following **Identity Provider Metadata**:

      - **URL** and enter the URL for your identity provider.
      - **XML File** and either drop the file or click in the area
        shown to open a dialog box from which you can select the XML
        file.
   4. **Service Provider Entity ID** field. Enter the information for
      the Black Duck SCA server in your environment in
      the format **https://*host*** where *host* is your Black Duck SCA server.
   5. **External Black Duck SCA URL** field. The URL of the public URL of
      the Black Duck SCA server.

      For example: https://blackduck-docker01.dc1.lan
   6. Optionally, select any of the following:

      - **Send Signed Authentication Request**: If this option is
        enabled, it indicates the asserting party's preference that
        relying parties should sign the authentication request
        before sending.
      - **Enable Group Synchronization**: If this option is
        enabled, upon login, groups from the Identity Provider (IDP)
        are created in Black Duck SCA and users
        will be assigned to those groups. Note that you must
        configure IDP to send groups in attribute statements with
        the attribute name of 'Groups'.
      - **Enable Local Logout Support**: If this option is enabled,
        after logging out of Black Duck SCA, the IDP's
        login page would appear. When local logout support is enabled,
        SAML requests are sent with ForceAuthn="true". Check with the
        IDP to confirm that this is supported.
      - **Create user accounts automatically in Black Duck SCA**: If a user logs in
        using the IdP and the user doesn't exist in Black Duck, we create a local user in
        Black Duck SCA's database if that
        option is selected.
4. Click **Save**.

After clicking **Save**, the **Black Duck SCA Metadata URL** field appears. You can copy the
link or directly download the SAML XML configuration information.

**To disable single sign-on using SAML**

1. Click [image: Administration icon] .
2. Select **Integrations** → **External Authentication**.
3. Click **Security Assertion Markup Language (SAML)**
4. Clear the **Enable SAML configuration** check box.
5. Click **Save**.

## Additional information

- Assertion Consumer Service (ACS): **https://<host>/saml/SSO**
- Recommended Service Provider Entity ID: **https://<host>** where *host* is your
  Black Duck SCA server location.

## Signed Authentication Certificates

Black Duck SCA supports SAML signed authentication certificates, enhancing
security by validating authentication requests against a trusted certificate.

To create a signed authentication certificate:

1. Click **+ Certificate**.
2. Enter or select an **Expiration Date** in the **Create SAML Certificate** modal.
3. Click **Create**.

Note: A maximum of two certificates can be created.

To activate, download, or delete a signed authentication certificate:

1. Click [image: Options button] for the desired certificate.
2. Select from the following options:

   - **Activate**. Specify this certificate to be used to validate SAML requests. Once
     activated, the certificate will be marked with the [image: Active icon] .
   - **Download**. Download the certificate as a CERT file.
   - **Delete**. Delete the certificate from the list of signed authentication certificates.
     Active certificates cannot be deleted.

You will be notified when a signed authentication certificate is nearing its expiration date.
Notifications include a banner at the top of the screen, a pop up message, as well
as an [image: Expiring Soon icon] icon on the certificate itself 30 days prior to the expiry date.
Notifications are triggered well in advance to provide time for system
administrators to update or replace the certificate.
