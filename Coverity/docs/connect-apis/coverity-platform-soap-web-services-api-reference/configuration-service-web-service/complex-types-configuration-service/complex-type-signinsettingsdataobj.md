---
title: "Complex type: signInSettingsDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-signinsettingsdataobj.html"
content_id: "_NvMt1MMNV0Spah8g1fO7Q"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:49.935298+00:00"
---

# Complex type: signInSettingsDataObj

## Description

Specification for Coverity Connect sign-in settings.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| allowPasswordRecovery | boolean | If set to true, users who are locked out due to incorrect password attempts can request their password through email. Requires previous email configuration. |
| authenticationMethod | string | Sets the sign-in authentication method. You can specify one of these strings: LDAP, KERBEROS, or REVERSE_PROXY. |
| disableLocalPasswordAuth | boolean | If set to true, disables local account access and uses LDAP for authentication. Requires previous LDAP configuration. |
| enableLdapAuth | boolean | If set to true, access for any user in LDAP (including Active Directory users) is allowed. To work, the setting requires an LDAP configuration. Coverity Connect uses local accounts by default. |
| ldapUserAutoCreate | boolean | If set to true, allows creation of users in Coverity Connect upon successful authentication with the LDAP server. Requires an LDAP configuration and that enableLdapAuth is also true. |
| limitFailedSignIns | boolean | If set to true, a specified number of failed name-password sign-in attempts (exceeding maxFailedSignInAttempts) will lock out a user. Once this happens, unless password recovery is enabled, the administrator must reset the password for this user. |
| maxFailedSignInAttempts | int | Number of failed name-password sign-in attempts that are allowed before locking out a user. See limitFailedSignins. |
| maxSessionIdleTime | int | Maximum period of inactivity allowed before the session times out. Default value is `120` mins. |
| requireLdapGroupMembership | boolean | If true, only allows the creation of LDAP users that are members of imported LDAP groups. This setting provides for backward compatibility with Microsoft Azure Entra ID products that require LDAP users to be members of an LDAP group. |
