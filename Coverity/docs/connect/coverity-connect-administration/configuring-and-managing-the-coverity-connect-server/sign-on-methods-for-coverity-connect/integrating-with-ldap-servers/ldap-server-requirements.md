---
title: "LDAP server requirements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ldap-server-requirements.html"
content_id: "zJpUuUoBw~D~WJ~RUBEXKA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:37.076049+00:00"
---

# LDAP server requirements

Coverity Connect has the following requirements for LDAP server configuration:

- The LDAP server must support at least one of the following types of bind operations:

  general bind with shared bind DN
  :   In this type of bind operation, a shared DN (distinguished name)
      exists and is allowed to query the LDAP server for user records
      and group definitions. To use this type of bind operation, the
      DN's name and password must be defined in the LDAP server
      configuration screen.

  anonymous bind
  :   In this type of bind operation, the LDAP server allows the
      querying of users and groups without having to authenticate
      first. To use this type of bind operation, select Use
      anonymous bind in the LDAP server
      configuration screen.
- Your server must be configured to use case-insensitive user names. Imported LDAP
  usernames are normalized to lower case characters.
- Coverity Connect only imports first-level LDAP users and groups. For example:

  ```
  Group1
    -user1
    -user2
    -user3
    -Group1A
      --user4
      --user5
  ```

  In this case, Coverity Connect imports user1, user2, user3, and Group1A, but not
  user4 and user5.
- If an LDAP user and a local user have the same user name, the local user will
  need to append `@local` to their user name when logging
  in.
- The SASL (simple authentication and security layer) framework is not
  supported.
- If the LDAP server is unreachable and an LDAP user attempts to sign in, the sign
  in will fail and the user will receive the following error:

  ```
  Error during sign in.
  ```

  You can find more information about the failure in the
  cim.log file.
- LDAP usernames can only be between 1 and 32 characters long. User names can
  include unicode characters starting from U+0020 (space), and up to, but not
  including, U+007f (delete).
- All required LDAP configuration values must be set in the LDAP server configuration
  screen before you can save the configuration.

  The LDAP server configuration screen provides links that automatically populate
  common user and group search settings for Azure Entra ID and OpenLDAP
  servers.
