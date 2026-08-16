---
title: "Operation: updateLdapConfiguration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-updateldapconfiguration.html"
content_id: "3GAW5CDs1A7bg6ss3AJUrQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:12.178215+00:00"
---

# Operation: updateLdapConfiguration

## Name

updateLdapConfiguration

## Description

Update an LDAP configuration.

## Parameters

serverDomainIdDataObj
:   **Type:** 
    serverDomainIdDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Name of the LDAP server domain. |

ldapConfigurationSpec
:   **Type:** 
    ldapConfigurationSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | anonymousBind | boolean | Value of *true* if using an anonymous bind; otherwise, *false* to indicate a general bind with a shared bind DN. |
    | baseDN | string | LDAP domain name in host format, such as <domain>.com or <corp.domain>.<com>, or base DN such as *ou=corp.* |
    | bindName | string | The username needed to access the LDAP server. You can specify the user in username@domain or LDAP DN format. |
    | bindPassword | string | Bind user password for LDAP user queries. Required for authenticated binding requests.If you do not enter a password, and if your LDAP server is configured to accept unauthenticated binding requests, Coverity Connect will attempt to gain unauthenticated access to the LDAP server.If an unauthenticated LDAP connection fails, Coverity Connect will display an LDAP Server Configuration failed message and an explanation of the failure. You can find more information about the failure in the *cim.log* file. |
    | displayName | string | Name that identifies the LDAP server in a multi-server setup. Appears in the UI. |
    | groupFilter | string | Optional filter to use when importing LDAP groups. Takes a valid RFC format. Example: cn=eng* |
    | groupFullName | boolean | If *false*, group members are stored by userName. If *true*, members are stored by their full DN. Defaults to *true*. |
    | groupMember | string | LDAP attribute that defines the members of a group. Group members can be referred to by their DN or username. |
    | groupName | string | Name attribute for the group. For Example: *cn* |
    | groupObjectClass | string | LDAP *objectClass* value that identifies user groups. For OpenLDAP, the default is *groupofnames*. For Azure Entra ID, the default is *group*. This field defines a component of the LDAP user group search query that Coverity Connect creates. |
    | groupSearchBase | string | The group search base DN to prepend to the base DN. Used for group searches. The base DN is configured as *Domain* as part of basic LDAP settings. For example: *cn=groups, ou=corp* |
    | primary | boolean | Value of *true* if this configuration is the primary one. Defaults to *false*. |
    | secureConnection | boolean | Value of *true* if using a secure connection. SSL or TLS protocol required. For information about LDAP server requirements, secure connections, importing LDAP users and groups, and other details about LDAP, refer to *Coverity Connect Usage and Administration Guide*. |
    | serverDomain | string | The host name or host IP of the LDAP server. The name must be resolvable from the Coverity Connect host. |
    | serverPort | long | The TCP port number where the LDAP server listens for connections. |
    | tlsEnabled | boolean | Value of *true* if TLS security protocol is used. |
    | userEmail | string | LDAP attribute that maps to the email address of the user. |
    | userFirstName | string | LDAP attribute that maps to the first name (given name) of the user. |
    | userLastName | string | LDAP attribute that maps to the last name (surname) of the user. |
    | userName | string | Username for testing user search settings. Maps to the username in the database. |
    | userObjectClass | string | LDAP *objectClass* associated with users on the LDAP server. For OpenLDAP, the default is *inetOrgPerson*. For Azure Entra ID, the default is *user*. |
    | userSearchBase | string | Relative DN to prepend to base DN to limit a user search. For example, ou=Users will search in ou=Users, dc=ad, dc=coverity, *dc=com*. |
