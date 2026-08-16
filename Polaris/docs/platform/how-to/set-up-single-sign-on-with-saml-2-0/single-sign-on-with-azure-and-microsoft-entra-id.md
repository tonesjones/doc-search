---
title: "Single sign-on with Azure and Microsoft Entra ID"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/single-sign-on-with-azure-and-microsoft-entra-id.html"
content_id: "Z4HAT06MGp0wdqET710bLg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:02.176629+00:00"
content_hash: "2732e3f1b4b64763f94ee687623e573382ecf108f7ae9201f1b3bf5f68097d62"
---

# Single sign-on with Azure and Microsoft Entra ID

Integrate Polaris with Azure's SAML 2.0 single sign-on identity provider (IDP).

After you download a SAML metadata file in Polaris (described here: Generate SAML metadata in Polaris), follow these steps to set up a SAML integration in Azure:

Note: Azure Active Directory (Azure AD) is now Microsoft Entra ID. See [New name for Azure Active Directory](https://learn.microsoft.com/en-us/entra/fundamentals/new-name) for more information.

## Create an enterprise application, set up single sign-on

1. Sign in to the Microsoft Azure portal and create a new enterprise application:
   1. From the Home page, go to Microsoft Entra ID > Enterprise applications > New applications and select Create your own application.
   2. Enter an application name in the What's the name of your app? field (`Polaris`, for example).
   3. Select Integrate any other application you don't find in the gallery (Non-gallery).
   4. Select Create.

      When Azure creates the application, the application's Overview page opens.
2. Enable single sign-on, and upload the SAML metadata you generated in Polaris (`sso_saml_metadata.xml`):
   1. Select Get started in the 2. Set up single sign on box.
   2. Select SAML.
   3. Select Upload metadata file and upload the `sso_saml_metadata.xml` file you downloaded from Polaris.

      Azure extracts the Identifier (Entity ID), Reply URL (Assertion Consumer Service URL), and Logout URL (Optional) values from the file.
   4. Select Save.
3. Update the application's attributes and claims:
   1. Select Edit in the Attributes & Claims box.

      The Attributes & Claims page opens.
   2. Open the Unique User Identifier (Name ID) claim. Ensure its Name identifier format is set to `Email address`.
   3. Open the claim with user.mail in the Value column. Change its Name identifier format to `user.email` (case-sensitive). Delete any text in the Namespace field and select Save.
   4. Open the claim with user.givenname in the Value column. Change its Name to `user.firstName` (case-sensitive). Delete any text in the Namespace field and select Save.
   5. Open the claim with the user.surname in the Value column. Change its Name to `user.lastName` (case-sensitive). Delete any text in the Namespace field and select Save.
   6. Add a group claim:

      Note: Adding a group claim is required to synchronize groups in your IDP with Polaris, but can be skipped if you prefer to assign Polaris access to users directly.

      1. Select Add a group claim. The Group Claims window open.
      2. Under Which groups associated with the user should be returned in the claim, select Groups assigned to the application.
      3. Ensure Source Attribute is set to Cloud-only group display names.
      4. Expand Advanced options, select Customize the name of the group claim, and enter `groups` in the Name (required) field.

         Note: You can use a different Name value, if necessary. This value is case-sensitive.
      5. Select Save.
   7. Verify your claims are set correctly, using the image below as a reference:

      [image: saml azure claims]
   8. Select SAML-based Sign-on (in the breadcrumbs near the top of the page) to return to the SAML setup page.
4. Under SAML Certificates, select Download next to Certificate (Base64).

   CAUTION:

   The certificate's expiration date (Expiration) is listed near the Download button. Plan to update your SAML signing certificate accordingly.

## Complete the SAML setup in Polaris

Use the SAML metadata Azure generates, along with the Base64 certificate you downloaded to complete the setup in Polaris:

1. Using the table below as a reference, copy values from Azure and paste them into the Add SAML Metadata tab in Polaris. Adjust other settings, as required.

   Important: If you're signed out of Polaris during the setup procedure, don't generate new SAML metadata. Instead, after you sign in, go to My Organization > Authentication > Change Authentication method to SSO > Next.

   | Field or option | Description |
   | --- | --- |
   | Single Sign On URL | Copy and paste the Login URL from Azure (found under **Set Up *<Enterprise Application Name>***) into this field. |
   | Single Log Out URL (Optional) | Copy and paste the Logout URL from Azure (found under **Set Up *<Enterprise Application Name>***) into this field. |
   | Organization Email Domain | Your organization's email domain (`company.com`, for example). If you use multiple email domains, separate entries with commas (`company.com,company.org`, for example). Note: Email domains cannot be reused across Polaris tenants. If an email domain is already being used for one Polaris tenant, it cannot be used for a different one. |
   | Signature Algorithm | In Azure, select Edit in the SAML Certificates box. Your algorithm appears in the Signing Algorithm dropdown menu. Tip: The default signing algorithm for Microsoft Entra ID is SHA-256 (RSA\_SHA256 in Polaris). |
   | Public Vendor Certificate | Open the Base64 certificate you downloaded from Azure in a text editor. Copy and paste the certificate (excluding the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines) into this field. |
   | Configuration Name | A name (up to 255 characters long, that can include special characters) used to identify the SAML integration in Polaris. Tip: After you set up single sign-on (and only while local authentication is permitted), the Configuration Name appears on the sign in page, on the button used to start the single sign-on process. This button only appears for Organization Administrators. To make this button easier to identify, we recommend using a name like `Sign in with <IDP Name>`. |
   | Manage Polaris groups through your Identity Provider (Optional) | Enable this setting to synchronize groups in your IDP with Polaris. To use this feature, you must provide: - Attribute Name: Enter the custom name you used for your group claim (`groups` is used in these instructions). - When duplicate group names are found: Specify what Polaris will do when the name of a group in Polaris (a local group) matches the name of a group in your IDP.   - Merge With Local Group (Recommended): The local group's membership is overwritten to match the IDP group's membership, and it's permissions are preserved. The group's membership becomes read only in Polaris, and can only be managed in your IDP.   - Rename Local Group: Polaris preserves the local group (without modifying its membership or permissions) and changes its name. Then, Polaris creates a new group with the original name. The new group's membership matches membership in your IDP, and no permissions are assigned to the new group. Note: See Manage Polaris groups through your identity provider for more information. |
   | Disable automatic user provisioning (Optional) | When you disable automatic user provisioning, an Organization Administrator must create each user's account in Polaris (in addition to provisioning users in your organization's IDP) before they can sign into Polaris. |
   | Disable local user authentication (Optional) | When you disable local user authentication, users can only sign into Polaris using single sign-on. CAUTION:  To avoid getting locked out of Polaris, we strongly recommend you complete the SAML setup process (and verify single sign-on is functioning as expected) before you disable local user authentication. |
2. Select Done.

## Grant users and groups access to Polaris

To give users and groups access to Polaris, follow these steps:

1. After you open the enterprise application you created for Polaris, go to Users and groups.
2. Select Add user/group.
3. Select None Selected under Users and groups.
4. Choose the users and/or groups you wish to add to Polaris, and then select Select.

   Important: The names of groups used to manage access to Polaris must be 255 characters or less.
5. Select Assign.

   The users and group members you assigned to the enterprise application can sign into Polaris using single sign-on.

   Note: Polaris does not automatically retrieve user or group information from your IDP when you enable single sign-on. Instead, Polaris only retrieves a user's information from your IDP (which may include groups they belong to that have access to Polaris) when they sign into Polaris using single sign-on successfully.

   Important: To ensure links to Black Duck Community (found on the Help page in Polaris) function as expected, English characters should be used for each user's first and last names.

Users with access to Polaris must access Polaris directly to start the authentication process.

Important: Identity provider-initiated authentication (starting the sign-in process from the Apps dashboard) is not supported.

## Additional information

Find more information on SAML in the Microsoft Entra documentation:

- [Tutorial: Microsoft Entra SSO integration with Microsoft Entra SAML Toolkit](https://learn.microsoft.com/en-us/entra/identity/saas-apps/saml-toolkit-tutorial)
