---
title: "Authenticating users with LDAP"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/authenticating-users-with-ldap.html"
content_id: "HCsbjvZlUfUqtTbF6yer8g"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:19.833947+00:00"
content_hash: "15ebcef9c3000d74c97f6fa0f1c6c67bdf6db32487ef68a6ed7bfb964f15298e"
---

# Authenticating users with LDAP

Authenticating users through an existing LDAP corporate directory helps to facilitate:

- The creation of user accounts. If the user account does not exist, upon successful authentication, the Black Duck SCA user account is created.
- Centralized management of user account details. Each time a user logs in to Black Duck SCA, Black Duck SCA synchronizes with the directory server. If changes were made to mapped attributes, Black Duck SCA updates the user account information.
- (Optional) The creation of groups. If a user is a member of an LDAP group, upon successful authentication, a Black Duck SCA user account, as well as a Black Duck SCA group, is created. The group is populated with the new user.

Note: If the Black Duck SCA group already exists, the Black Duck SCA user account is created, and the group is populated.

Tip: All hosted customers should secure access to their Black Duck SCA application by leveraging out-of-the-box support for single sign-on (SSO) via SAML or LDAP. For information on enabling and configuring these security features, see the installation guides. Customers using a SAML SSO provider that offers two-factor authentication are also encouraged to enable that technology to further secure access to their Black Duck SCA application. For more information, see Configuring SAML for Single Sign-On.

## Before starting

Contact your LDAP administrator and gather the following information:

- **LDAP server details**

  This is the information that Black Duck SCA uses to connect to the directory server.

  - **Server URL** (required): The host name or IP address of the directory server, including the protocol scheme and port, on which the instance is listening.

    *Example:*`ldap://<server_name>.<domain_name>.com:389`

    For more information, see Configuring secure LDAP.
  - **Authentication Type**: If credentials are required for LDAP access, the authentication type to use: Simple, None, or Digest-MD5.
  - **Manager DN** (optional): If your organization does not use anonymous authentication, and requires credentials for LDAP access, the password and either the LDAP name or the absolute LDAP distinguished name (DN) of a user that has permission to read the directory server.

    *Example of an absolute LDAP DN:*`uid=ldapmanager,ou=employees,dc=company,dc=com`

    *Example of an LDAP name:*`jdoe`
- **LDAP user attributes and LDAP attribute mappings**

  This is the information that Black Duck SCA uses to locate users in the directory server:

  - **User Search Base** (required): The absolute base DN under which users can be located.

    *Example:*`dc=example,dc=com`
  - **User Search Filter** (required): The attribute used to match a specific, unique user. The value of this attribute personalizes the user profile icon with the name of the user.

    *Example:*`uid={0}`
  - **User DN Pattern** (optional): If some of your users are not located under the absolute base DN for the user search, the user DN pattern is used to match a specific, unique user.

    *Example:*`cn={0},ou=contractors`
  - **First Name, Last Name, Email** (optional): The attributes that map to the first name, last name, and email address of users.
- **LDAP groups**

  If you are enabling LDAP group synchronization, this is the required information that Black Duck SCA uses to locate user groups in the directory server:

  - **Group Search Base** (required): The absolute base DN under which groups can be located.

    *Example:*`ou=groups,dc=example,dc=com`
  - **Group Filter** (required): The attribute used to match a unique user member within a given group.

    *Example:*`uniquemember={0}`
  - **Group Name Attribute** (required): The attribute that identifies a specific, unique group name.

    *Example:*`cn`

## Configuring LDAP

To configure LDAP:

1. Log in to Black Duck SCA as a system administrator.
2. Click [image: Administration icon] .
3. Select **Integrations** → **External Authentication**.
4. Click **Lightweight Directory Access Protocol (LDAP)**.
5. Check the **Enable LDAP Configuration** checkbox.
6. In the **LDAP Server Details** section, enter the server connection and authentication details that Black Duck SCA is to use to connect to the directory server.
7. In the **LDAP User Attributes** section, enter the user attribute values that Black Duck SCA is to use to locate users.

   Optionally, clear the **Create user accounts automatically in Black Duck SCA** check box to turn off the automatic creation of users when they authenticate with LDAP. This check box is selected by default so that users who do not exist in Black Duck SCA are created automatically when they log in using LDAP. This applies to new installs and upgrades.
8. (Optional) Enter the attributes that map to user-specific information in the **LDAP Attribute Mappings** section.
9. (Optional) Select **Synchronize LDAP groups** and enter the group attribute values that Black Duck SCA is to use to locate groups in the **LDAP Groups** section.
10. (Optional) Enter user credentials in the **Test Connection, User Authentication and Field Mapping** section and click **Test Connection** to test the connection to the directory server.

    If LDAP group synchronization is enabled and configured, the user's first name, last name, email address, and LDAP groups are displayed for successful connections.
11. Click **Save**.
