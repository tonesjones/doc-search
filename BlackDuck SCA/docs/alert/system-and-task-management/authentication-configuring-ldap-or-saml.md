---
title: "Authentication - Configuring LDAP or SAML"
source_url: "https://docs.blackduck.com/r/alert/8.4.0/black-duck-alert-user-guide/authentication-configuring-ldap-or-saml.html"
content_id: "ZZZpUyc0s6cA6uaA~7Fdfw"
version: "8.4.0"
section: "System and Task Management"
scraped_at: "2026-08-08T23:46:42.029317+00:00"
---

# Authentication - Configuring LDAP or SAML

In addition to the Alert applications built-in username/password authentication method,
both SAML and LDAP can be used to authenticate users. Before users can authenticate
using SAML or LDAP, you must configure both the external system Identity Provider (IdP)
and the Alert application.

When LDAP is configured and enabled, the login prompt will ask for a Username and
Password which will first be checked against internal system users. If the Username is
not found internally, the LDAP instance will be consulted. If SAML is enabled, the login
prompt will also display a **Login with SAML** button, that when selected will prompt
for provider login.

Figure 1. Alert login screen
[image: Alert login with SAML]

## LDAP or SAML user authentication workflow

The following is a high-level overview of the workflow for LDAP and SAML user
authentication.

1. The LDAP or SAML provider has a list of authenticated/authorized users.
2. You configure Alert to authenticate by using LDAP and/or SAML.
3. You configure Alert with the Identity Provider (IdP) details.
4. The user logs in to Alert using LDAP or SAML authentication. By default, LDAP
   and SAML users log in with the most restrictive permissions (ALERT_USER).
5. The external system (IdP) validates or fails to validate the user.
6. The user is created in Alert upon successful authentication.
7. An Alert system administrator can assign roles after a successful login by the
   user.

When users authenticate through LDAP or SAML to log into Alert for the first time,
they are added to the Alert database. The Alert administrator can assign roles for
the users on the User Management page. LDAP and SAML users that login into Alert now
have the `ALERT_USER` role assigned to them on first login, by
default.

## How LDAP and SAML work in Alert

**LDAP**

Users log into Alert where they are added to the Alert system with the most
restricted access to Alert. After the user has logged in initially to Alert, a
System Administrator can assign the user roles. The next time the user logs in they
will have their access privileges based on the roles assigned to them.

**SAML**

SAML works the same as LDAP for non-admin users of Alert. They must log in initially
and an administrator grants them privileges afterwards.

The difference with SAML is in the administrative user.

Since the SAML login redirects the user to another site to login, an Alert
administrative user must have the Attribute containing their
`ALERT_ADMIN` role assigned. This will add them to Alert as a
user with administrative access when they log in to Alert that first time, which
enables them to assign roles to other users.

## LDAP Configuration

If you are configuring Alert with environment variables, see the Environment Variables page, which provides the equivalent LDAP
variables.

To configure Alert with your LDAP server:

1. Navigate to **Authentication**
2. Click on the **LDAP** tab.

Figure 2. LDAP configuration
[image: LDAP configuration]

Complete the following LDAP configuration fields.

Table 1. LDAP configuration fields

| Field Name | Description | Notes |
| --- | --- | --- |
| LDAP Enabled | Select the checkbox to enable LDAP authentication | |
| LDAP Server URL | URL and port of the LDAP server | |
| LDAP Distinguished Manager Name | Distinguished name of the LDAP manager | |
| LDAP Manager Password | The password of the LDAP manager | |
| LDAP Authentication Type | The type of authentication required by the LDAP server | `simple` – Send the fully qualified user and clear-text password. Supported in LDAP v2 and v3. `none` – Anonymous authentication `Digest-MD5` – Required for LDAP v3. “In Digest-MD5, the LDAP server sends data that includes various authentication options that it is willing to support plus a special token to the LDAP client. The client responds by sending an encrypted response that indicates the authentication options that it has selected.” |
| LDAP Referral | The method to use when handling referrals | `ignore` – Ignore any referrals `follow` - Follow any referrals `throw` - Throw an exception for each referral |
| LDAP User Search Base | Where in the LDAP directory User searches should be performed | Alert supports a single OU for User search |
| LDAP User Search Filter | The filter used for group membership | |
| LDAP User DN Patterns | The pattern used to supply a DN for a user. This should be the name relative to the root DN | |
| LDAP User Attributes | What attributes to retrieve for a user | |
| LDAP Group Search Base | Where in the LDAP directory Group searches should be performed | LDAP group settings are a way to import Alert related role information in LDAP, into Alert. If these are not set you will see a stack trace in the logs and users may have restricted permissions. |
| LDAP Group Search Filter | The filter used to search for user membership in a group | |
| LDAP Group Role Attribute | The ID of the attribute which contains the role name used for group membership | |

To test your LDAP configuration:

1. Click **Test LDAP Configuration** and enter an existing user name and
   password for your LDAP instance.
2. Click **Test User Connection** to test the authentication.

Figure 3. Testing the LDAP configuration
[image: Testing the LDAP configuration]

To save your LDAP configuration.

1. Click **Save LDAP Configuration**

To delete your LDAP configuration:

1. Click **Delete LDAP Configuration**
2. Click **Yes** to confirm the deletion.

## SAML Configuration

If you are configuring Alert with environment variables, see the Environment Variables page, which provides the equivalent SAML
variables.

Alert supports Security Assertion Markup Language (SAML) authentication. Only one
SAML application can be connected to Alert at any given time.

### Set up your IdP Roles for Alert

For Alert to work properly, roles must be assigned to SAML attributes. Each
identity provider is different regarding the assignment of SAML attributes and
Alert requires the SAML attribute *AlertRoles*.

The *AlertRoles* must be a list of roles that Alert recognizes, with
`ALERT_ADMIN` role required for configuration.

See a sample of Role configuration in Okta below. Note that only the
*AlertRoles* attribute, shown in this example, is mandatory.

Tip: For specifying multiple values in Okta, use expressions such as
Arrays.flatten({“ALERT_USER”},“ALERT_ADMIN”). See [okta reference
documentation](https://developer.okta.com/docs/reference/okta-expression-language/)

Figure 4. Sample: Okta SAML Role Configuration
[image: Okta SAML Role configuration sample]

### Set up your IdP SSO URL and Audience URI

Configure the Alert specific SSO URL and Audience URI via your IdP's
configuration interface.

Table 2. SSO configuration fields

| Field Name | Value | Notes |
| --- | --- | --- |
| Single sign-on URL | https​://<localhost:8443>/alert/login/saml2/sso/default | Replace the hostname and port with that of your environment |
| Audience URI | https​://<localhost:8443>/alert/saml2/service-provider-metadata/default | Replace the hostname and port with that of your environment |

See a sample SSO URL and Audience URI configuration in Okta below.

Figure 5. Sample: Okta SAML SSO URL & Authentication URI Configuration
[image: Okta SAML SSO URL and Auth URI configuration sample]

Note: Only one SAML IdP can be connected to Alert at any given time.

To configure Alert with your SAML IdP Complete the following general configuration fields, noting that settings
available will change depending on which method is selected for providing SAML Identity Provider Metadata.

1. Navigate to **Authentication**.
2. Click on the **SAML** tab.

Figure 6. SAML SSO Configuration
[image: SAML SSO configuration]

Table 3. SAML configuration entries

| Field Name | Description | Notes |
| --- | --- | --- |
| SAML Enabled | Select the checkbox to enable or disable SAML authentication |  |
| SAML Identity Provider | Select one of URL or XML File for providing the Metadata from your IdP | This can be populated automatically by using the **Fill Form** button to retrieve Black Duck SAML Configuration values from your Black Duck instance if it is configured for SAML |
| Identity Provider Metadata URL | The Metadata URL provided by your IdP for retrieving configuration values | This can be populated automatically by using the **Fill Form** button to retrieve Black Duck SAML Configuration values from your Black Duck instance if it is configured for SAML |
| Identity Provider Metadata File | The file to upload to the server containing your IdP Metadata | Selecting **XML File** for provisioning the SAML Identity Provider toggles this file selection functionality on |
| Retrieve Black Duck SAML Configuration | This button connects to the Black Duck provider to retrieve the IdP metadata URL automatically | Select the "Fill Form** button lauches a pop-up for selecting the Black Duck instance |
| Force Auth | When checked, the forceAuthn flag is set in the payload to the IdP | Check that this is supported by your IdP |

To complete any required SSL related configuration, select the **Advanced SAML Configuration** link.

Select and upload the appropriate files.

Figure 7. Advanced SAML Configuration
[image: Advanced SAML Configuration]

Table 4. Files and descriptions

| File Type | Description |
| --- | --- |
| Encryption Certificate File | Select and upload the encryption type certificate file to configure SAML |
| Encryption Cert Private Key File | Select and upload the PKCS8 Encryption private key file associated with the encryption certificate |
| Signing Certificate File | Select and upload the signing type certificate file to configure SAML |
| Signing Cert Private Key File | Select and upload the PKCS8 Encryption private key file associated with the signing certificate |
| Verification Certificate File | Select and upload the verification type certificate file to configure SAML |

To test your SAML configuration:

1. Click **Validate SAML Configuration**.
2. Validation will occur in the background and return with any issues.

To save your SAML configuration.

1. Click **Save SAML Configuration**

To delete your SAML configuration:

1. Click **Delete SAML Configuration**
2. Click **Yes** to confirm the deletion.
