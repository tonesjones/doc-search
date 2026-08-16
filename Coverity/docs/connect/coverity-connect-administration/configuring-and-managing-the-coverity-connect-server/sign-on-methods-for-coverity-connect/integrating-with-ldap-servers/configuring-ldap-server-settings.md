---
title: "Configuring LDAP server settings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-ldap-server-settings.html"
content_id: "KwxFoDOve1bDqDxSWlpMmA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:39.700096+00:00"
---

# Configuring LDAP server settings

You configure LDAP server settings for Coverity Connect in Configuration > System > LDAP Configuration.

Warning: Some LDAP server implementations do not allow spaces in configuration
settings. To avoid possible problems, do not use spaces in your Base DN, User Search
Base DN, and Group Search Base DN settings.

**To configure LDAP server settings:**

1. Create or edit the LDAP server settings.

   - Click Add from the LDAP Configuration screen to
     create a new configuration.

     This action opens configuration pane.

     Note: If your instance of Coverity Connect is configured as a subscriber in
     a clustered Coverity Connect environment, you can not configure the LDAP
     settings (the Add button will be disabled). The
     coordinator is the only Coverity Connect instance in a clustered
     environment that can configure these settings. For more information, see
     Synchronizing multiple Coverity Connect instances.
   - Click the name of an existing LDAP configuration to open its
     configuration pane.
2. Provide a display name.

   This is used to identify an instance in a multi-server setup.
3. If there are multiple LDAP server configurations, indicate whether this one is
   the Primary server.

   If checked, this configuration is treated as the primary configuration.

   Note: When a user logs in with their username only, Coverity Connect attempts to
   authenticate the username against the LDAP server specified as
   Primary in the LDAP
   Configuration pane. If the username is not found in the Primary
   LDAP server, authentication fails. To log in with a username set in a
   non-primary LDAP server, the user must log in as
   `username@other_ldap_server`.
4. Complete the configuration.

   For information about the configuration pane, see the subsections in Configuring LDAP server settings.
5. Click Done to finalize your changes and exit the
   screen.

   You must set all required LDAP server configuration values before you can save them.

## Connection settings

The connection settings are:

Host Name
:   The host name or the IP address of the LDAP server.
    The host name must be resolvable from the Coverity Connect host.

Port
:   The TCP port number where the LDAP server listens for connections (defaults
    to 389).

Base DN
:   The LDAP domain name in host format, such as domain.com or
    corp.domain.com, or base DN such
    as `ou=corp` .

    Note: If you specify the domain as a hostname, it is translated into DN
    (distinguished name) format, where each element of the hostname becomes a
    domain component (DC) in the DN. For example, 
    corp.domain.com becomes
    `dc=corp,dc=domain,dc=com`.

    If this does not match your LDAP directory structure, use DN
    format.

Security
:   Specify one of the following security protocols:

    - SSL
    - TLS

    Select None if you do not want to use SSL or TLS
    security.

    For more information, see LDAP security.

Use anonymous bind
:   Specify this option to use an anonymous LDAP connection. If Use
    anonymous bind is enabled, Bind DN
    and Password are disabled.

    If Use anonymous bind is not enabled, you must provide
    a value for Bind DN for an unauthenticated bind
    request, or you must provide a value for both Bind DN
    and Password for an authenticated bind
    request.

Bind DN
:   The username needed to access the LDAP server.

    You can specify the user in username@domain or LDAP DN
    format.

Bind Password
:   Bind user password for LDAP user queries. This field is required for
    authenticated binding requests.

    If you do not enter a password, and if your LDAP server is configured to
    accept unauthenticated binding requests, Coverity Connect will attempt to
    gain unauthenticated access to the LDAP server.

    If an unauthenticated LDAP connection fails, Coverity Connect will display an
    `LDAP Server Configuration failed` message and an
    explanation of the failure. You can find more information about the failure
    in the cim.log file.

Test Connection Settings
:   Click Connect to LDAP Server to test the
    connection.

    If the connection fails, there might be a problem with your configuration.
    You can find more information about the failure in the
    cim.log file.

## Pre-fill settings

If you are using Microsoft Azure Entra ID or OpenLDAP servers, you can use the
following links to automatically populate standard user and group search settings for
these servers:

- Pre-Fill Microsoft Azure Entra ID Settings
- Pre-Fill OpenLDAP Settings

Make sure that you use the correct auto-fill form for your server type.

If you are using an LDAP server type other than Microsoft Azure Entra ID or OpenLDAP,
it might require custom configuration values for the User and Group search
settings.

## User search settings

The user search configuration settings are:

User Search Base DN
:   A user search base DN to prepend to the base DN. Used to limit user
    search.

    Note: The base DN is configured as Domain as part of the
    basic LDAP settings.

    For example:

    ```
    cn=users,ou=corp
    ```

    If the search base is incorrectly set and an LDAP user attempts sign in, the
    sign in will fail and the user will receive the following error:

    ```
    Error during sign in.
    ```

    You can find more information about the failure in the
    cim.log file.

User ObjectClass
:   The LDAP ObjectClass associated with users on your LDAP server. For OpenLDAP,
    the default is `inetOrgPerson` and for Azure Entra ID, the
    default is `user.`

Username Attribute
:   LDAP attribute that maps to the Coverity Connect username.

Given Name Attribute
:   LDAP attribute that maps to the given name.

Surname Attribute
:   LDAP attribute that maps to the surname.

Email Attribute
:   LDAP attribute that maps to the email.

Test User Search Settings
:   Coverity Connect will attempt to connect to the LDAP server and will test the
    filter based on a valid LDAP username that you are required to enter. Click
    Connect to LDAP Server to test the connection. If
    the connection fails, or if authentication fails, there might be a problem
    with your configuration.

    Username
    :   Enter a known LDAP username from your LDAP server. Coverity
        Connect searches for this user when you click Test
        User Search Settings.

The group search configuration settings are:

Group Search Base DN
:   The group search base DN to prepend to the base DN. Used for group searches.
    The base DN is configured as Domain as part of the
    basic LDAP settings.

    For example:

    ```
    cn=groups,ou=corp
    ```

Groups ObjectClass
:   The LDAP objectClass value that identifies user groups.
    For OpenLDAP, the default is `groupofnames`. For
    Active Directory (now Azure Entra ID), the default is `group`.
    This field defines a component of the LDAP user group search query that Coverity Connect
    creates.

Group Name Attribute
:   The name attribute for the group, for example `cn`.

Member Attribute
:   The LDAP attribute that defines the members of a group. Group members can be
    referred to by their DN or username.

Members stored by
:   Setting that indicates whether members of your LDAP groups are stored by
    their full DN or by the username attribute.

Additional Search Filter
:   Additional filter arguments to include certain entries in the subtree and to
    exclude others. This filter supports standard LDAP query syntax.

    For example, the following entry limits the search to all groups where the
    name is either dev, or starts with
    eng-:

    `(|(name=eng-*)(name=dev))`

    In this case, the group search filter that Coverity Connect creates is:

    ```
    (&(objectClass=group)(|(name=eng-*)(name=dev)))
    ```

Test Group Search Settings
:   Coverity Connect will attempt to connect to the LDAP server and retrieve the
    list of groups. Click Retrieve Groups to test the
    connection. If the connection fails, or the list of groups is empty, there
    might be a problem with your configuration. You can find more information
    about the failure in the cim.log file. If the number of
    groups returned is greater than 1000, you need to use an additional group
    search filter to reduce the number of groups.
