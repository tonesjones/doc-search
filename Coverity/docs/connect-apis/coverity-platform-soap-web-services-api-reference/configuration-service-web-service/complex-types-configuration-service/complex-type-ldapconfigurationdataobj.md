---
title: "Complex type: ldapConfigurationDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-ldapconfigurationdataobj.html"
content_id: "WlHdnaqpoeVEZPe7mBKgDA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:37.365545+00:00"
---

# Complex type: ldapConfigurationDataObj

## Description

Returns LDAP configuration data.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| anonymousBind | boolean | Value of *true* if using an anonymous bind; otherwise, *false* to indicate a general bind with a shared bind DN. |
| baseDN | string | LDAP domain name in host format, such as <domain>.com or <corp.domain>.<com>, or base DN such as *ou=corp.* |
| bindName | string | The username needed to access the LDAP server. Can be specified in username@domain or LDAP DN format. |
| bindPassword | string | Bind user password for LDAP user queries. Required for authenticated binding requests.If there is no password, and if your LDAP server is configured to accept unauthenticated binding requests, Coverity Connect will attempt to gain unauthenticated access to the LDAP server.If an unauthenticated LDAP connection fails, Coverity Connect will display an LDAP Server Configuration failed message and an explanation of the failure. You can find more information about the failure in the *cim.log* file. |
| groupFilter | string | Optional filter used when importing LDAP groups. Takes a valid RFC format. Example: cn=eng* |
| groupFullName | boolean | Members stored by full DN or Username. |
| groupMember | string | If *false*, group members are stored by userName. If *true*, members are stored by their full DN. Defaults to *true*. |
| groupName | string | Name attribute for the group. For Example: *cn* |
| groupObjectClass | string | LDAP *objectClass* value that identifies user groups. For OpenLDAP, the default is *groupofnames*. For Azure Entra ID, the default is *group*. This field defines a component of the LDAP user group search query that Coverity Connect creates. |
| groupSearchBase | string | The group search base DN to prepend to the base DN. Used for group searches. The base DN is configured as *Domain* as part of basic LDAP settings. For example: *cn=groups, ou=corp* |
| primary | boolean | Indicates whether this LDAP configuration is used. Note that multiple LDAP configurations are possible. |
| secureConnection | boolean | Value of *true* if using a secure connection. SSL or TLS protocol required. |
| serverDomain | string | The host name or host IP of the LDAP server. The name must be resolvable from the Coverity Connect host. |
| serverDomainIdDataObj | serverDomainIdDataObj | Identifier for the LDAP server domain. |
| serverPort | long | The TCP port number where the LDAP server listens for connections (default is *389*). |
| tlsEnabled | boolean | Value of *true* if TLS security protocol is used. |
| userEmail | string | LDAP attribute that maps to the email address of the user. |
| userFirstName | string | LDAP attribute that maps to the first name (given name) of the user. |
| userLastName | string | LDAP attribute that maps to the last name (surname) of the user. |
| userName | string | Username for testing user search settings. Maps to the username in the database. |
| userObjectClass | string | LDAP *objectClass* associated with users on the LDAP server. For OpenLDAP, the default is *inetOrgPerson*. For Active Directory, the default is *user*. |
| userSearchBase | string | Relative DN to prepend to base DN to limit a user search. For example, ou=Users will search in ou=Users, dc=ad, dc=coverity, *dc=com*. |
