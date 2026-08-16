---
title: "Set up single sign-on (with SAML 2.0)"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/set-up-single-sign-on-with-saml-2.0-.html"
content_id: "IbW_MspIJgjCYNDx3IKCSw"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:00.585502+00:00"
content_hash: "a6db475be201ec9f8495b0967e85e5d1b63ede783effdbe2e87c3a164c21c98a"
---

# Set up single sign-on (with SAML 2.0)

Integrate your SAML 2.0 identity provider (IDP) with Polaris to use single sign-on (SSO) and manage access to Polaris from your IDP.

## Overview

Security Assertion Markup Language (SAML) is a single sign-on (SSO) standard for messages between service providers (like Polaris) and IDPs (like Okta) to support user authentication. After you enable single sign-on in Polaris:

- You can manage access to Polaris using your IDP.
- Your users don't have to maintain a separate password for Polaris. Instead, users sign in using credentials managed by your IDP.

Polaris does not automatically retrieve user or group information from your IDP when you enable single sign-on. Instead, Polaris only retrieves a user's information from your IDP (which may include groups they belong to that have access to Polaris) when they sign into Polaris using single sign-on successfully.

None of the actions you perform in Polaris can modify a user or group's settings in your IDP.

### Tutorials: Setting up single sign-on for Polaris

Before you proceed, consider reviewing the interactive tutorials here: Single sign-on tutorials.

### Service provider-initiated authentication

Polaris supports service provider-initiated authentication. After you enable single sign-on in Polaris, users must access Polaris directly to start the authentication process.

Important: Identity provider-initiated authentication (starting the sign-in process from your IDP's portal) is not supported. Ensure you configure your IDP to use service provider-initiated authentication for Polaris.

### Manage Polaris groups through your identity provider

Optionally, you can synchronize groups in your IDP with Polaris. This allows you to manage Polaris groups and group membership in your IDP, and manage each group's permissions in Polaris. After you enable this setting, Polaris retrieves a user's groups (limited to groups the user belongs to that are provisioned with Polaris access) each time they sign in to Polaris using single sign-on successfully, and updates their group membership accordingly. This can include:

- Adding groups to Polaris that aren't already synchronized.
- Adding the user to (or removing the user from) groups that are already synchronized with Polaris.

Note: Enabling this feature won't prevent you from creating new groups in Polaris (groups that only exist in Polaris, or local groups).

Group names in Polaris must be unique, and only use lowercase characters. If a group's name includes uppercase characters in your IDP (**GroupName**), the group's name will only use lowercase characters in Polaris (**groupname**). To use an IDP group with Polaris, the group's name (in your IDP) must be 255 characters or less. When you synchronize groups in your IDP with Polaris, you need to specify what Polaris will do when the name of a local group matches the name of a group in your IDP. Polaris can either merge groups with matching names, or automatically rename local groups to preserve them.

If you choose to merge groups, the group's permissions do not change. The group's membership is overwritten to match membership in your IDP. For example:

Table 1. Merge IDP group with local group, example

| Groups before merge | Groups after merge |
| --- | --- |
| **Polaris Developers** (IDP group)  - Membership includes User 1 and User 2. | **Polaris Developers** (IDP group)  - *No change.* Membership includes User 1 and User 2. |
| **polaris developers** (local group)  - Membership includes User 1 and User 3. - Members have contributor access to 5 applications. - Group membership can be modified in Polaris. | **polaris developers** (synchronized group)  - *Gradually, membership is overwritten to match IDP.* Membership includes User 1 and User 2; User 3 is removed. Note: The group's membership changes gradually, as users 1, 2, and 3 sign into Polaris using single sign-on. - *Polaris permissions do not change.* Members have contributor access to 5 applications. - *Group membership cannot be modified in Polaris.* Group membership is synchronized with your IDP (and read only in Polaris). |

If you choose to rename local groups, Polaris appends a number to the end of the local group's name (for example, **polaris developers** becomes **polaris developers-1**). The local group's permissions and membership do not change. Then, Polaris creates a new group with the original name (**polaris developers**). The new group's membership matches membership in your IDP, and no permissions are mapped to the new group. For example:

Table 2. Rename local group, example

| Groups before rename | Groups after rename |
| --- | --- |
| **Polaris Developers** (IDP group)  - Membership includes User 1 and User 2. | **Polaris Developers** (IDP group)  - *No change.* Membership includes User 1 and User 2. |
| **polaris developers** (local group)  - Membership includes User 1 and User 3. - Members have contributor access to 5 applications. - Group membership can be modified in Polaris. | **polaris developers-1** (local group, renamed).  - *No change.* Membership includes User 1 and User 3. - *No change.* Members have contributor access to 5 applications. - *No change.* Group membership can be modified in Polaris. |
|  | **polaris developers** (synchronized group)  - *Gradually, membership is overwritten to match IDP.* Membership includes User 1 and User 2. Note: The group's membership changes gradually, as users 1, 2, and 3 sign into Polaris using single sign-on. - *No Polaris permissions are applied to the group.* - *Group membership cannot be modified in Polaris.* Group membership is synchronized with your IDP (and read only in Polaris). |

### Disable automatic user provisioning

Normally, after you grant a new user access to Polaris using your IDP, Polaris automatically creates the user's account (using attributes retrieved from your IDP) when they first sign into Polaris. This can be disabled for added security. When disabled, in addition to granting each new user access to Polaris in your IDP, an Organization Administrator must create each user's Polaris account manually (via My Organization > Users > Add User) before they can sign in.

### Disable local authentication

By default, after you enable single sign-on, Organization Administrators can sign into Polaris with their Polaris username and password (local credentials) in addition to their IDP credentials. When you disable local user authentication, Organization Administrators can only access Polaris using single sign-on.

CAUTION:

To avoid getting locked out of Polaris, we strongly recommend you complete the single sign-on setup process (and verify single sign-on is functioning as expected) before you disable local user authentication.

## Prerequisites

Setting up single sign-on requires the following:

- Organization Administrator permissions in Polaris. Only Organization Administrators can generate SAML metadata and configure single sign-on in Polaris.
- An IDP that supports SAML 2.0.
- Sufficient permissions to create an integration with Polaris in your IDP.

## Generate SAML metadata in Polaris

Organization Administrators can generate metadata for a SAML integration on the My Organization page. Follow these steps:

1. Go to My Organization > Authentication.
2. Select Change Authentication method to SSO.
3. Select Download.

   Polaris generates a `sso_saml_metadata.xml` file that contains essential values to set up a SAML integration.

   Important: Until you complete the setup procedure (and save your single sign-on settings in Polaris), values in each `sso_saml_metadata.xml` file you create are unique. Each time you (or other Organization Administrators in your organization) select Download, Polaris invalidates values in previously-generated `sso_saml_metadata.xml` files.

   ```
   <md:EntityDescriptor xmlns="urn:oasis:names:tc:SAML:2.0:metadata" 
       xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" 
       xmlns:ds="http://www.w3.org/2000/09/xmldsig#" entityID="https://polaris.blackduck.com/auth/realms/DOCS" 
       ID="ID_05b6872b-16b4-470a-ac2e-f9533113095d">
       <md:SPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol" AuthnRequestsSigned="true" 
           WantAssertionsSigned="true">
           <md:KeyDescriptor use="signing">
               <ds:KeyInfo>
                   <ds:KeyName>KeyName</ds:KeyName>
                   <ds:X509Data>
                       <ds:X509Certificate>CertificateString</ds:X509Certificate>
                   </ds:X509Data>
               </ds:KeyInfo>
           </md:KeyDescriptor>
           <md:SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" 
               Location="https://polaris.blackduck.com/auth/realms/DOCS/broker/sso/endpoint" />
           <md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat>
           <md:AssertionConsumerService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" 
               Location="https://polaris.blackduck.com/auth/realms/DOCS/broker/sso/endpoint" isDefault="true" index="1" />
           <md:AttributeConsumingService isDefault="true" index="1">
               <md:ServiceName xml:lang="en">DOCS</md:ServiceName>
               <md:RequestedAttribute Name="user.email" FriendlyName="email" 
                   NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" />
               <md:RequestedAttribute Name="user.lastName" FriendlyName="lastName" 
                   NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" />
               <md:RequestedAttribute Name="user.firstName" FriendlyName="firstName" 
                   NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" />
           </md:AttributeConsumingService>
       </md:SPSSODescriptor>
   </md:EntityDescriptor>
   ```
4. Click Next.

   The Add SAML Metadata tab opens.

   Tip: You'll come back to this page after you Add SAML metadata from Polaris to your IDP.

   [image: saml polaris form]

## Add SAML metadata from Polaris to your IDP

Use values in the `sso_saml_metadata.xml` file to set up mappings in your IDP. The steps to complete this vary from IDP to IDP.

Note: Instructions for Azure (via Microsoft Entra ID) and Okta customers are included for reference:

- Single sign-on with Okta
- Single sign-on with Azure and Microsoft Entra ID

Minimally, you must create claims for three user attributes:

- Email (`user.email`)
- First name (`user.firstName`)
- Last name (`user.lastName`)

Note: To synchronize groups in your IDP with Polaris, you must also create a group claim. This can be skipped if you prefer to assign Polaris access to users directly.

When you complete this step, your IDP generates the SAML metadata you need to complete the setup in Polaris.

## Complete the SAML setup in Polaris

Use the SAML metadata your IDP generates to complete the setup in Polaris:

1. Find the SAML metadata your IDP generates.
2. Using the table below as a reference, copy values from your IDP and paste them into the Add SAML Metadata tab in Polaris. Adjust other settings, as required.

   Important: If you're signed out of Polaris during the setup procedure, don't generate new SAML metadata. Instead, after you sign in, go to My Organization > Authentication > Change Authentication method to SSO > Next.

   | Field or option | Description |
   | --- | --- |
   | Single Sign On URL | Retrieve this value from your IDP. |
   | Single Log Out URL (Optional) | Retrieve this value from your IDP. |
   | Organization Email Domain | Your organization's email domain (`company.com`, for example). If you use multiple email domains, separate entries with commas (`company.com,company.org`, for example). Note: Email domains cannot be reused across Polaris tenants. If an email domain is already being used for one Polaris tenant, it cannot be used for a different one. |
   | Signature Algorithm | Retrieve this value from your IDP. |
   | Public Vendor Certificate | Retrieve this value from your IDP. |
   | Configuration Name | A name (up to 255 characters long, that can include special characters) used to identify the SAML integration in Polaris. Tip: After you set up single sign-on (and only while local authentication is permitted), the Configuration Name appears on the sign in page, on the button used to start the single sign-on process. This button only appears for Organization Administrators. To make this button easier to identify, we recommend using a name like `Sign in with <IDP Name>`. |
   | Manage Polaris groups through your Identity Provider (Optional) | Enable this setting to synchronize groups in your IDP with Polaris. To use this feature, you must provide: - Attribute Name: The attribute your IDP uses to identify groups in SAML assertions. Retrieve this value from your IDP. - When duplicate group names are found: Specify what Polaris will do when the name of a group in Polaris (a local group) matches the name of a group in your IDP.   - Merge With Local Group (Recommended): The local group's membership is overwritten to match the IDP group's membership, and it's permissions are preserved. The group's membership becomes read only in Polaris, and can only be managed in your IDP.   - Rename Local Group: Polaris preserves the local group (without modifying its membership or permissions) and changes its name. Then, Polaris creates a new group with the original name. The new group's membership matches membership in your IDP, and no permissions are assigned to the new group. Note: See Manage Polaris groups through your identity provider for more information. |
   | Disable automatic user provisioning (Optional) | When you disable automatic user provisioning, an Organization Administrator must create each user's account in Polaris (in addition to provisioning users in your organization's IDP) before they can sign into Polaris. |
   | Disable local user authentication (Optional) | When you disable local user authentication, users can only sign into Polaris using single sign-on. CAUTION:  To avoid getting locked out of Polaris, we strongly recommend you complete the SAML setup process (and verify single sign-on is functioning as expected) before you disable local user authentication. |
3. Select Done.

## Grant users and groups access to Polaris

Now, grant users and groups access to Polaris in your IDP. The steps to complete this vary from IDP to IDP.

Note: Polaris does not automatically retrieve user or group information from your IDP when you enable single sign-on. Instead, Polaris only retrieves a user's information from your IDP (which may include groups they belong to that have access to Polaris) when they sign into Polaris using single sign-on successfully.

Important: To ensure links to Black Duck Community (found on the Help page in Polaris) function as expected, English characters should be used for each user's first and last names.

Users with access to Polaris must access Polaris directly to start the authentication process.

Important: Identity provider-initiated authentication (starting the sign-in process from your IDP's portal) is not supported.

## Update your single sign-on settings

To modify your single sign-on settings, follow these steps:

1. Go to My Organization > Authentication.
2. Select Edit > Next.
3. Update your single sign-on settings, as required, and select Done.
