---
title: "Active Directory/LDAP Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/active-directory/ldap-configuration.html"
content_id: "PNCMNzkqZgcy~7_vHffooA"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:21.618812+00:00"
content_hash: "77842b5e19ebe48b63f552e36949b9578a2b8ba6c45ff1126154db6326d3281a"
---

# Active Directory/LDAP Configuration

Software Risk Manager allows you to create and deactivate new users that are only known
to the Software Risk Manager system. You may, however, want to let users use the same
credentials as they do for your organization. To facilitate this, you may provide an
LDAP or Active Directory configuration in the properties file
(`codedx.props`). The available settings are as follows:

- `auth.ldap.url = ldap://127.0.0.1:389/` – sets the LDAP URL to
  connect to; this setting is *required* for LDAP usage.
- `auth.ldap.systemUsername =
  sAMAccountName=admin,ou=users,dc=codedx,dc=com` – sets the system
  username (full account DN) that is used when connecting to the LDAP server for
  authorization queries; this setting is not required if the LDAP server accepts
  anonymous queries.
- `auth.ldap.systemPassword = secret` – sets the password
  corresponding with the system username (above) that is used when connecting to
  the LDAP server for authorization queries; this setting is not required if the
  LDAP server accepts anonymous queries.
- `auth.ldap.authenticationMechanism = simple` – sets LDAP
  authentication mechanism for authorization queries; accepted values are
  *none* (anonymous) and *simple* [default: none].
- `auth.ldap.userSearchTemplate =
  sAMAccountName={0},ou=users,dc=codedx,dc=com` – controls the
  template to generate the user search query for authorization; more information
  can be found here [default: `<direct user
  input>`].
- `auth.ldap.useAsDnTemplate = false` – whether to use the provided
  search template(s) as DN templates instead [default: false].
- `auth.ldap.useStartTLS = false` – enable or disable the use of
  StartTLS after establishing an LDAP connection [default: false].
- `auth.ldap.legacyMode = false` – enable or disable the legacy Code
  Dx LDAP implementation [default: false].
- `auth.ldap.user.groupAttribute = memberOf` – set the name of the
  LDAP attribute on a user that lists their groups [default: memberOf].
- `auth.ldap.group.nameAttribute = cn` – set the name of the LDAP
  attribute on a group that indicates their readable name (leave blank for
  pass-through) [default: cn].
- `auth.ldap.user.displayNameAttribute = cn` – set the
  comma-separated list of LDAP attributes names on a user indicating their display
  name; see the relevantsections below for syntax [default: cn, userPrincipalName,
  sAMAccountName].
- `auth.ldap.sync.autoUpdate = false` – set whether or not to
  automatically schedule LDAP group membership updates [default: false].
- `auth.ldap.sync.refreshInterval = 5 minutes` – set the refresh
  interval for automatic LDAP group membership updates in readable text [default:
  "5 minutes"].
- `auth.ldap.searchSubTree = true` – sets whether or not to search
  sub-trees for users with the provided userSearchTemplate(s) [default:
  true].

Note: LDAP property names were changed in Code Dx version 3.5.4. The previous
names may still be used.

You may be able to get by with only setting the `auth.ldap.url` property,
depending on the complexity of your LDAP setup. It may be necessary to use a
fully-qualified username (e.g., `john.doe@example.com` rather than just
`john.doe`) when adding the user to Software Risk Manager.

The `systemUsername`, `systemPassword`, and
`authenticationMechanism` properties don't need to be set for a
secure LDAP configuration, due to the fact that they are not used during user
authentication, but for querying user information that will be used during their
authentication. Read the section below for more details.

## User Search Template

The user DN is the fully qualified LDAP identifier for the user when logging in. In
some LDAP systems, the user DN may require an attribute that the actual user isn't
aware of, such as an integer ID. Rather than asking the user for this hidden
attribute, the user provides a different unique identifier (such as their account
name) and Software Risk Manager will insert that into the given query to find a
matching user with that attribute. The text they enter as their username is used to
replace the `{0}` part of the template.

In the example above (`sAMAccountName={0},ou=users,dc=codedx,dc=com`),
when the user attempts to log in, a query will be run on
`sAMAccountName=test,ou=users,dc=codedx,dc=com` to retrieve the
user DN, which may give something like
`uid=12345,ou=users,dc=codedx,dc=com`. This user DN is then used
to bind an LDAP connection using the discovered DN and the user's given
password.

**Note:** In order to make this query, Software Risk Manager needs to be able to
authenticate against the LDAP server without the user's credentials. If the LDAP
server supports anonymous queries, this won't be an issue. If the LDAP server
requires authentication, assign `auth.ldap.authenticationMechanism =
simple` and assign
`auth.ldap.systemUsername`/`auth.ldap.systemPassword`
to the credentials to use when making these queries. The
`systemUsername` should be the full, bindable DN for the
user.

If no template is provided, the username entered by the user will be directly used,
which may not map to what your LDAP server is expecting. When specifying a user
search template, the `{0}` placeholder must be present. If it is
missing, an error will be logged at Software Risk Manager startup, and LDAP
authentication will be disabled until the template is corrected. After correcting
the LDAP authentication, restart the Software Risk Manager Tomcat server.

### Using as a DN Template

If performing a user search before binding is untenable in your environment, you
can set Software Risk Manager to treat the search templates as direct DN
templates instead by assigning `auth.ldap.useAsDnTemplate =
true`. This means that each authentication performs only one bind, using
the resolved DN and the provided user password.

While this may provide slightly better performance, it is mostly useful when
anonymous binds are unsupported and there is no system user account available to
perform a search.

**Note:** Enabling this option will disable LDAP connection pooling, so a new
connection will be made and bound for each authentication attempt. Also note
that this option cannot be enabled when using multiple templates.

### Multiple Templates

Multiple search templates can be used by adding multiple, uniquely named
properties, starting with `auth.ldap.userSearchTemplate`. For
example,

```
auth.ldap.userSearchTemplate-A = sAMAccountName={0},ou=users,dc=codedx,dc=com
auth.ldap.userSearchTemplate.B = cn={0},ou=customers,dc=codedx,dc=com
```

With the above properties, both of those search templates will be used to resolve
a user DN when signing in. The property names can be anything, as long as they
start with `auth.ldap.userSearchTemplate` and are unique. If
`auth.ldap.userSearchTemplate-A` was used twice in the above
example, the second assignment would overwrite the first.

**Note:** Make sure that any LDAP user added to Software Risk Manager can be
resolved by only *one* of the registered search templates.

## Sign-in with Multiple Names

When multiple search templates are provided, it is possible for the same LDAP user to
sign in using different names. Software Risk Manager resolves each LDAP user to
their DN and stores that as their identity, allowing the user to sign into the same
Software Risk Manager account regardless of the name used.

This DN resolution occurs when a user signs in and not when a user is manually
registered through the User Admin page. For their first sign-in, they must use the
name that has been registered. This causes their DN to be properly resolved and
stored, allowing sign-in under different names.

### User Merging

In rare cases, it is possible for two LDAP user entries to exist in Software Risk
Manager that refer to the same LDAP user. If two separate accounts resolve to
the same DN during authentication, Software Risk Manager will automatically
merge the users. This merge creates a new user with the same name that is being
authenticated, reassigns all content from matching users to the new user,
deletes those previous users, and then authenticates with that new user. This
invalidates any active sessions using either of the two previous LDAP users.

**Note:** Any user merging will be accompanied by an entry in the Software
Risk Manager server logs, as well as the Visual Log, with appropriate
details.

## Display Names

The LDAP attribute used for display names can be set with
`auth.ldap.user.displayNameAttribute`, which is a comma-separated
list of attribute names. Each attribute is checked in order, and the first received
value is used. If unassigned, Software Risk Manager will attempt to use their CN,
UPN, and SAN, in that order.

Display names are automatically updated when a user signs in. Changes to the
`displayNameAttribute` property won't affect users until they
sign in again.

Single-value LDAP attributes will be used as-is, if available. Multi-value attributes
will have their first entry selected by default. You can choose a specific index in
the list, if needed, by using the syntax `myAttribute{n}`, where
`n` is the 0-based index in the attribute list. For example, you
can select the second value in a list while falling back to another attribute with
the following:

```
auth.ldap.user.displayNameAttribute = myAttribute{1}, someOtherAttribute
```

You could also prioritize a second value while falling back to the first with:

```
auth.ldap.user.displayNameAttribute = myAttribute{1}, myAttribute{0}
```

**Note:**
`myAttribute{0}` and `myAttribute` are equivalent;
they both select the first value available from the attribute.

## LDAP Group Mapping

LDAP groups for your users can be mapped to Software Risk Manager groups within the
application. This requires connection to an LDAP server that provides a user
attribute listing its groups, such as Active Directory and its
`memberOf` attribute.

This group mapping requires a valid `groupAttribute` and
`nameAttribute` to be assigned in your
`codedx.props` file. The defaults are suitable for use with an
Active Directory server and can be left unassigned if using Active Directory.

The `auth.ldap.user.groupAttribute` is the name of the attribute on
your *user objects* that lists the groups that the user is a member of. This is
typically a multi-value attribute containing the full DN paths for a user's
groups.

The `auth.ldap.group.nameAttribute` is the name of the attribute on
your *group objects* that determine how you refer to those groups in Software
Risk Manager. When defining what a Software Risk Manager group will map to, you will
use the values provided by that attribute. This is used to pull a readable name from
the `groupAttribute` of any authenticated users.
