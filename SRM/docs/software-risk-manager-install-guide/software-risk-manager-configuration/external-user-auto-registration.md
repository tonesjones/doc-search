---
title: "External User Auto-Registration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/external-user-auto-registration.html"
content_id: "OwBytfpDQVozKctGjrgXew"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:24.905552+00:00"
content_hash: "13f24a7e2d3fe6c94a0ef328878447fe5cb64c88e7d131216c2f56434921945e"
---

# External User Auto-Registration

Software Risk Manager supports auto-registration of users that sign in through external
methods such as LDAP and SAML. This can include automatic creation, enabling, and
disabling of users based on their properties. This is particularly useful when managing
an installation using third-party authentication, where there may be many users in your
organization that need to be maintained.

Note: User auto-registration respects the user limit of your license; if a new user attempts
to sign in without any seats available, they will receive an error message regarding
license limitations.

## Auto-Registration with LDAP

Auto-registration can be configured in your `codedx.props` file with
the following settings:

- `auth.auto-create.ldap.enabled` – set whether to auto-create
  LDAP users that don't exist yet in Software Risk Manager [default: false].
  (This setting was previously exposed as
  `auth.auto-create.enabled` which will be deprecated in an
  upcoming release.)
- `auth.auto-create.ldap.group-names = foo, bar` – a
  comma-separated list of group names, where an LDAP user must be a member of
  at least one of those groups to allow auto-creation [default: none].
- `auth.auto-create.ldap.auto-toggle-enabled` – set whether to
  automatically enable/disable LDAP registered users based on their membership
  in the provided LDAP group names (no effect if `group-names`
  is unassigned or empty) [default: false].

When using auto-registration with LDAP, we recommend using both the
`group-names` and `auto-toggle-enabled` options.
Without `group-names`, any LDAP user can sign in to Software Risk
Manager. Without `auto-toggle-enabled`, a user leaving one of those
required groups would still be allowed to sign in to Software Risk Manager.

**Note:** LDAP group membership checks are only available for LDAP providers that
maintain an attribute on users listing their memberships (e.g., Active Directory and
its `memberOf` attribute).

Auto-registration with LDAP requires a valid LDAP configuration in your
`codedx.props` file, and Software Risk Manager must have
permission to read the necessary LDAP objects and attributes to check for group
membership. This depends on your LDAP server configuration, but typically requires
that you've assigned a `systemUser` and
`systemPassword` and set `authenticationMechanism =
simple` in your `codedx.props` file.

**Note:** Automatic enable/disable of users occurs when logging in. Changing the
user's LDAP group membership will not sign the user out or disable them. If
necessary, you can disable or delete the user manually. Configuring session durations in
Software Risk Manager may also be useful.

Also note that LDAP group names in the `group-names` property does not
need to match any LDAP group mappings in your Software Risk Manager user groups,
though there may be some overlap.

## Auto-Registration with SAML

Auto-registration can be configured in your `codedx.props` file with
the following settings:

- `auth.auto-create.saml.enabled` – set whether or not to
  automatically create SRM users when a SAML user signs in (optionally gated
  by `group-names`) [default: false].
- `auth.auto-create.saml.group-names` – a comma-separated list
  of group names used as a requirement on auto-create and auto-toggle behavior
  [default: none].
- `auth.auto-create.saml.auto-toggle-enabled` – set whether or
  not to automatically enable/disable SRM SAML users depending on their group
  membership (requires `group-names` be set) [default: false].

When using auto-registration with SAML, using both the `group-names`
and `auto-toggle-enabled` options is recommended.

Auto-registration with SAML requires a valid SAML and SAML Groups configuration in
your codedx.props file.
