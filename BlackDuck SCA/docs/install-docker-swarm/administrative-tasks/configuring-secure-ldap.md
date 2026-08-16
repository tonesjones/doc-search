---
title: "Configuring secure LDAP"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-secure-ldap.html"
content_id: "hM4EDEIDiM69nupB~ed2zw"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:46.647353+00:00"
---

# Configuring secure LDAP

If you see certificate issues when connecting your secure LDAP server to Black Duck, the most likely reason is that the Black Duck server has not set up a trust connection to the secure LDAP
server. This usually occurs if you are using a self-signed certificate.

To set up a trust connection to the secure LDAP server, import the server certificate
into the local Black Duck LDAP truststore by:

1. Obtaining your LDAP information.
2. Using the Black Duck UI to import the server certificate.

Note: All hosted customers should secure access to their Black Duck application by leveraging our
out-of-the-box support for single sign on (SSO) via SAML or LDAP. Information on how to
enable and configure these security features can be found in the installation guides. In
addition, we encourage customers that are using a SAML SSO provider that offers
two-factor authorization to also enable and leverage that technology to further secure
access to their Black Duck application.

## Obtaining your LDAP information

Contact your LDAP administrator and gather the following information:

**LDAP Server Details**

This is the information that Black Duck SCA uses to connect to the
directory server.

- (required) The host name or IP address of the directory server, including the
  protocol scheme and port, on which the instance is listening.

  **Example:**
  `ldaps://<server_name>.<domain_name>.com:339`

- (optional) If your organization does not use anonymous authentication, and
  requires credentials for LDAP access, the password and either the LDAP name or
  the absolute LDAP distinguished name (DN) of a user that has permission to read
  the directory server.

  **Example of an absolute LDAP DN:**
  `uid=ldapmanager,ou=employees,dc=company,dc=com`

  **Example
  of an LDAP name:**
  `jdoe`
- (optional) If credentials are required for LDAP access, the authentication
  type to use: simple or digest-MD5.

**LDAP Users Attributes**

This is the information that Black Duck uses to locate users in the
directory server:

- (required) The absolute base DN under which users can be located.

  **Example:**
  `dc=example,dc=com`
- (required) The attribute used to match a specific, unique user. The value of
  this attribute personalizes the user profile icon with the name of the user.

  **Example:**
  `uid={0}`

**Test Username and Password**

- (required) The user credentials to test the connection to the directory
  server.

## Importing the server certificate

To import the server certificate:

1. Log in to Black Duck as a system administrator.
2. Click [image: Administration icon] .
3. Select **Integrations** → **External Authentication**.
4. Click **Lightweight Directory Access Protocol (LDAP)**.
5. Check the **Enable LDAP Configuration** checkbox and complete the
   information in the **LDAP Server Details** section, as described above.
   In the **Server URL** field, ensure that you have configured the secure
   LDAP server: the protocol scheme is ldaps://.
6. Complete the information in the **LDAP User Attributes** section, as
   described above.

   Optionally, clear the **Create user accounts automatically in Black Duck**
   check box to turn off the automatic creation of users when they authenticate
   with LDAP. This check box is selected by default so users that do not exist
   in Black Duck are created automatically when they log into Black Duck using
   LDAP. This applies to new installs and upgrades.
7. Enter the user credentials in the **Test Connection, User Authentication and
   Field Mapping** section and click **Test Connection**.
8. If there are no issues with the certificate, it is automatically imported and
   the "Connection Test Succeeded" message appears:

     
    [image: image]
9. If there is an issue with the certificate, a dialog box listing details about
   the certificate will appear. Do one of the following:

   - Click **Cancel** to fix the certificate issues.

     Once fixed, retest the connection to verify that the certificate
     issues have been fixed and the certificate has been imported. If
     successful, the "Connection Test Succeeded" message appears.
   - Click **Save** to import this certificate.

     Verify that the certificate has been imported by clicking **Test
     Connection**. If successful, the "Connection Test Succeeded"
     message appears.
