---
title: "Upgrading LDAP server configuration settings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-ldap-server-configuration-settings.html"
content_id: "LzXbQkl6RyLFhwKX7L6kuw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:40.980440+00:00"
---

# Upgrading LDAP server configuration settings

If you upgrade from a version of Coverity Connect earlier than 5.3, it is possible that
your LDAP server configuration settings will not successfully upgrade due to your user
and group objectClass settings.

In previous versions, the LDAP server configuration screen contained the User
Search filter and Group Search Filter fields
which required you to define the respective objectClass as part of the filter
definition. As of 5.3, these fields are removed. Coverity Connect now automatically
builds the user search filter and group search filter based on the values set in the
User objectClass and Group objectClass
fields. The defaults for these values are:

- User objectClass: inetOrgPerson
  (OpenLDAP), user (Azure Entra ID)
- Group objectClass: groupofnames
  (OpenLDAP), group (Azure Entra ID)

If your objectClass definitions from a previous Coverity Connect version match the
defaults listed above, your LDAP server configuration settings should successfully
upgrade. If the objectClass definition do not match, configuration settings will not
update successfully. In this case, you will have to manually set User objectClass and
Group ObjectClass to your desired value after you upgrade your Coverity Connect
server.

To aid you in locating possible mismatches, Coverity Connect writes your LDAP
configuration settings to the upgrade log before you upgrade and after the upgrade is
finished. If there are conflicts, Coverity Connect alerts you. You can use the upgrade
log to locate the mismatch and make the appropriate changes.
