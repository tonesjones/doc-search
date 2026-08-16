---
title: "Authenticating users with LDAP"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/authenticating-users-with-ldap.html"
content_id: "T2dcV0o6EMXDX2AxJ~mhVw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:57.975809+00:00"
---

# Authenticating users with LDAP

Authenticating users through an existing LDAP corporate directory helps to
facilitate:

- The creation of user accounts. If the user account does not exist, upon
  successful authentication, the Black Duck user account is
  created.
- Centralized management of user account details. Each time a user logs in to Black Duck, Black Duck synchronizes with the
  directory server. If changes were made to mapped attributes, Black Duck updates the user account information.
- (Optional) The creation of groups. If a user is a member of an LDAP group, upon
  successful authentication, a Black Duck user account, as well
  as a Black Duck group, is created. The group is populated with
  the new user.

Note: Note: If the Black Duck group already exists, the Black Duck user account is created, and the group is populated.

## Before starting

Contact your LDAP administrator and gather the following information:

- **LDAP server details**

  This is the information that Black Duck uses to connect to the
  directory server.
- **Server URL** (required): The host name or IP address of the
  directory server, including the protocol scheme and port, on which the
  instance is listening.

  *Example:*
  `ldap://<server_name>.<domain_name>.com:339`

  Click here for
  more information on configuring secure LDAP.
- **Authentication Type**: If credentials are required for LDAP access,
  the authentication type to use: Simple, None, or Digest-MD5.
- **Manager DN** (optional): If your organization does not use anonymous
  authentication, and requires credentials for LDAP access, the password
  and either the LDAP name or the absolute LDAP distinguished name (DN) of
  a user that has permission to read the directory server.

  *Example of an absolute LDAP DN:*
  `uid=ldapmanager,ou=employees,dc=company,dc=com`

  *Example of an LDAP name:*
  `jdoe`
- **LDAP users attributes and LDAP attribute mappings**

  This is the information that the Black Duck uses to locate users
  in the directory server:

  - **User Search Base** (required): The absolute base DN under which
    users can be located.

    *Example:*
    `dc=example,dc=com`
  - **User Search Filter** (required) The attribute used to match a
    specific, unique user. The value of this attribute personalizes the user
    profile icon with the name of the user.

    *Example:*
    `uid={0}`
  - **User DN Pattern** (optional): If some of your users are not located
    under the absolute base DN for the user search, the user DN pattern is
    used to match a specific, unique user.

    *Example:*
    `cn={0},ou=contractors`
  - **First Name, Last Name, Email** (optional) The attributes that map to
    the first name, last name, and email address of users.
- **LDAP groups**

  If you are enabling LDAP group synchronization, this is the required information
  that Black Duck uses to locate user groups in the directory
  server:

  - **Group Search Base** (required): The absolute base DN under which
    groups can be located.

    *Example:*
    `ou=groups,dc=example,dc=com`
  - **Group Filter** (required) The attribute used to match a unique user
    member within a given group.

    *Example:*
    `uniquemember={0}`
  - **Group Name Attribute** (required) The attribute that identifies a
    specific, unique group name.

    *Example:*
    `cn`

## Configuring LDAP

To configure LDAP:

1. Log in to Black Duck as a system administrator.
2. Click [image: Administration icon] .
3. Select **Integrations** → **External Authentication**.
4. Click **Lightweight Directory Access Protocol (LDAP)**.
5. Check the **Enable LDAP Configuration** checkbox.
6. In the **LDAP Server Details** section, Enter the server connection and authentication
   details that Black Duck is to use to connect to the directory server,
7. In the **LDAP User Attributes** section, enter the user attributes values Black Duck is to use to locate users.

   Optionally, clear the **Create user accounts automatically in Black Duck**
   check box to turn off the automatic creation of users when they authenticate
   with LDAP. This check box is selected by default so users that do not exist in
   Black Duck are created automatically when they log into Black Duck using LDAP.
   This applies to new installs and upgrades.
8. (Optional) Enter the attributes that map to user-specific information in the
   **LDAP Attribute Mappings** section.
9. (Optional) Select **Synchronize LDAP groups** and enter the group attribute
   values Black Duck is to use to locate groups in the **LDAP
   Groups** section.
10. (Optional) Enter user credentials in the **Test Connection, User Authentication
    and Field Mapping** section and click **Test Connection** to test the
    connection to the directory server.

    If the LDAP group synchronization is enabled and configured, the user's first
    name, last name, email address, and user's LDAP groups are displayed for
    successful connections.
11. Click **Save.**
