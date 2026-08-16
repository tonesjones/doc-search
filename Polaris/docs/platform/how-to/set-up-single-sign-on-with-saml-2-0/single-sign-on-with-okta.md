---
title: "Single sign-on with Okta"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/single-sign-on-with-okta.html"
content_id: "FrhzzEk3hSwAcedEKf4HPg"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:01.327975+00:00"
content_hash: "dc28095931fb3650b75017d081816e27cc54058eea11a0ad36081d8f1ff070bd"
---

# Single sign-on with Okta

Integrate Polaris with Okta, a SAML 2.0 single sign-on identity provider (IDP).

After you download a SAML metadata file in Polaris, follow these steps to set up an app integration in Okta:

Note: See Generate SAML metadata in Polaris for more information.

## Create an app integration

To set up an Okta app integration, follow these steps:

1. Open the Okta Admin Dashboard and go to Applications > Applications.
2. Select Create App Integration.
3. Set the Sign-in method to SAML 2.0.
4. Select Next.
5. Enter an App name (`Polaris`, for example).
6. (Optional) Adjust the other General Settings, if necessary.
7. Select Next.
8. Enter the Single sign-on URL.

   Note: Find this URL in the `Location` attribute of `md:AssertionConsumerService` in the `sso_saml_metadata.xml` file.
9. Enter the Audience URI (SP Entity ID).

   Note: Find this value in the `entityID` attribute of `md:EntityDescriptor` in the `sso_saml_metadata.xml` file.
10. Change Application username to Email.
11. (Optional) Adjust the other settings in the General group (including advanced settings), if necessary.
12. Create three Attribute Statements. Map the attribute statements to the `Name` attribute of each `md:RequestedAttribute` element in the `sso_saml_metadata.xml` file.

    CAUTION:

    All three attribute statements are required, and case-sensitive. Failing to create these statements will cause errors.

    1. Enter `user.email` in the Name field, and select user.email with the Value dropdown menu.
    2. Enter `user.firstName` in the Name field, and select user.firstname with the Value dropdown menu.
    3. Enter `user.lastName` in the Name field, and select user.lastname with the Value dropdown menu.
13. Create a Group Attribute Statement. Enter `groups` in the Name field.

    Note: Adding a group attribute statement is required to synchronize groups in your IDP with Polaris, but can be skipped if you prefer to assign Polaris access to users directly. You can use a different Name value, if necessary. This value is case-sensitive.
14. Select Next.
15. Select I'm an Okta customer adding an internal app and then select Finish.
16. Select View Setup Instructions.

## Complete the SAML setup in Polaris

Use the SAML metadata Okta generates to complete the setup in Polaris:

1. Using the table below as a reference, copy values from Okta and paste them into the Add SAML Metadata tab in Polaris. Adjust other settings, as required.

   Important: If you're signed out of Polaris during the setup procedure, don't generate new SAML metadata. Instead, after you sign in, go to My Organization > Authentication > Change Authentication method to SSO > Next.

   | Field or option | Description |
   | --- | --- |
   | Single Sign On URL | Copy and paste the Identity Provider Single Sign-On URL from Okta into this field. |
   | Single Log Out URL (Optional) | If you set up a single logout URL in Okta, copy and paste the Identity Provider Single Logout URL from Okta into this field. |
   | Organization Email Domain | Your organization's email domain (`company.com`, for example). If you use multiple email domains, separate entries with commas (`company.com,company.org`, for example). Note: Email domains cannot be reused across Polaris tenants. If an email domain is already being used for one Polaris tenant, it cannot be used for a different one. |
   | Signature Algorithm | Retrieve this value from Okta. Tip: The default signature algorithm for an Okta SAML 2.0 app integrations is RSA\_SHA256. |
   | Public Vendor Certificate | Copy and paste the X.509 Certificate from Okta (omitting the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines) into this field. |
   | Configuration Name | A name (up to 255 characters long, that can include special characters) used to identify the SAML integration in Polaris. Tip: After you set up single sign-on (and only while local authentication is permitted), the Configuration Name appears on the sign in page, on the button used to start the single sign-on process. This button only appears for Organization Administrators. To make this button easier to identify, we recommend using a name like `Sign in with <IDP Name>`. |
   | Manage Polaris groups through your Identity Provider (Optional) | Enable this setting to synchronize groups in your IDP with Polaris. To use this feature, you must provide: - Attribute Name: Enter the name of your group attribute statement (`groups` is used in these instructions). - When duplicate group names are found: Specify what Polaris will do when the name of a group in Polaris (a local group) matches the name of a group in your IDP.   - Merge With Local Group (Recommended): The local group's membership is overwritten to match the IDP group's membership, and it's permissions are preserved. The group's membership becomes read only in Polaris, and can only be managed in your IDP.   - Rename Local Group: Polaris preserves the local group (without modifying its membership or permissions) and changes its name. Then, Polaris creates a new group with the original name. The new group's membership matches membership in your IDP, and no permissions are assigned to the new group. Note: See Manage Polaris groups through your identity provider for more information. |
   | Disable automatic user provisioning (Optional) | When you disable automatic user provisioning, an Organization Administrator must create each user's account in Polaris (in addition to provisioning users in your organization's IDP) before they can sign into Polaris. |
   | Disable local user authentication (Optional) | When you disable local user authentication, users can only sign into Polaris using single sign-on. CAUTION:  To avoid getting locked out of Polaris, we strongly recommend you complete the SAML setup process (and verify single sign-on is functioning as expected) before you disable local user authentication. |
2. Select Done.

## Grant users and groups access to Polaris

To give users and groups access to Polaris, follow these steps:

1. Open the Okta Admin Dashboard and go to Applications > Applications.
2. Select the app integration you created for Polaris.
3. Go to Assignments.
4. To grant a user access to Polaris:
   1. Select Assign > Assign to People.
   2. Select Assign next to the user(s) who require access to Polaris, and then select Save and Go Back.
   3. Select Done.
5. To grant a group access to Polaris:
   1. Select Assign > Assign to Groups.
   2. Select Assign next to the group(s) that require access to Polaris.
   3. Select Done.

   The users and group members you assigned to the application can sign into Polaris using single sign-on.

   Note: Polaris does not automatically retrieve user or group information from your IDP when you enable single sign-on. Instead, Polaris only retrieves a user's information from your IDP (which may include groups they belong to that have access to Polaris) when they sign into Polaris using single sign-on successfully.

   Important: To ensure links to Black Duck Community (found on the Help page in Polaris) function as expected, English characters should be used for each user's first and last names.

Users with access to Polaris must access Polaris directly to start the authentication process.

Important: Identity provider-initiated authentication (starting the sign-in process from the Okta portal) is not supported.

## Additional information

Find more information on Okta app integrations in the Okta documentation:

- [Create SAML app integrations](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_saml.htm)
- [Configure Single Logout in app integrations](https://help.okta.com/en-us/content/topics/apps/apps_single_logout.htm)
