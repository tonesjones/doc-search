---
title: "SAML Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/saml-configuration.html"
content_id: "err~NNCc4CeaGLOrEcrUgQ"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:22.467518+00:00"
content_hash: "cccd2dec3bcc2a63e5b207d7976769d87611a470fc5a81d6aa48409417040005"
---

# SAML Configuration

Software Risk Manager can also be configured to authenticate against a SAML 2.0 IdP
(Identity Provider). This can be done by using the settings below.

Note: SAML authentication isn’t currently supported for Software Risk Manager
plugins.

- `auth.saml2.identityProviderMetadataPath` – [required] Sets the file
  path to the XML metadata for your SAML IdP (file must exist on the Software Risk
  Manager host).
- `auth.saml2.keystorePath` [default: internal Software Risk Manager
  path] – Sets the signing key for SAML requests by Software Risk Manager; must be JKS
  format with the appropriate cert, private key, and an assigned password for both the
  JKS key store and private key; will be auto-generated at an internal Software Risk
  Manager location if unassigned.
- `auth.saml2.keystorePassword` – [required] Sets the password used to
  open the assigned JKS file.
- `auth.saml2.privateKeyPassword` – [required] Sets the password to use
  with the private key stored in the assigned JKS file.
- `auth.saml2.uniqueNameAttribute` [default: user's Name Id] – Sets the
  specific attribute to use as the unique username ID; the value of this attribute is
  used as the user's login ID and display name, unless the
  `auth.saml2.displayNameAttribute` setting (see below) is defined.
- `auth.saml2.displayNameAttribute` [default: value of
  `auth.saml2.uniqueNameAttribute`] – Sets the specific attribute to use
  as the user's display name; if not set, the value of
  `auth.saml2.uniqueNameAttribute` (default: user's Name Id) is used instead.
- `auth.saml2.namePolicyFormat` default: from IdP XML – Sets the
  accepted/required format of the Name Id.
- `auth.saml2.entityId` default: https://codedx.com – Sets the entity
  ID used to identify Software Risk Manager as a service provider when registering
  with your IdP.
- `auth.saml2.responseBindingType` [default:
  `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST`] – Sets the
  Assertion Consumer Service (ACS) binding type for Software Risk Manager.
- `auth.saml2.authnRequestBindingType` [default: from IdP XML] – Sets
  the binding type to use when Software Risk Manager submits Authn requests to your
  IdP (must be supported by your IdP's SSO service endpoint).
- `auth.saml2.maximumAuthenticationLifetime` [default: 3600] – Sets the
  maximum allowed age (in seconds) of the `AuthnInstant` specified in
  an Authn Response from the IdP. This is an additional (but not entirely necessary)
  validation step performed by Software Risk Manager. If rolling session lifetimes are
  in place from your IdP, this may be disabled by setting to `-1`
  (which sets the max lifetime to 10 years).
- `auth.saml2.maxSkewSeconds` [default: 120] – Sets the maximum
  allowable difference in UTC time between the Software Risk Manager server and an IdP
  server (loosens the window of maximumAuthenticationLifetime).
- `auth.saml2.passive` [default: `false`] – Sets whether
  or not to use passive authentication against your IdP.
- `auth.saml2.forceAuth` [default: `false`] – Sets
  whether or not to force re-authentication with your IdP when the user attempts to
  start a new Software Risk Manager session (this re-authentication may start a new
  session and invalidate existing SAML sessions with other applications).
- `auth.saml2.requireSignedAssertions` [default:
  `false`] – Sets whether or not Software Risk Manager should require
  signed assertions from your IdP (regardless of whether the message as a whole was
  signed).
- `auth.saml2.requireSignedResponses` [default:
  `false`] – Sets whether or not Software Risk Manager should require
  signatures on all responses from your IdP.
- `auth.saml2.signAuthenticationRequests` [default:
  `false`] – Sets whether or not Software Risk Manager should sign
  authentication requests to your IdP.
- `auth.saml2.useNameQualifier` [default: `false`] –
  Sets whether or not Software Risk Manager should include a name qualifier in Authn
  requests to your IdP.
- `auth.autoExternalRedirect` [default: `true`] – Sets
  whether or not to automatically redirect unauthenticated users to your IdP login
  portal.
- `ui.auth.samlLabel` [default: SAML] – Sets the label for SAML-related
  operations within the Software Risk Manager interface; this will be displayed when
  signing in to Software Risk Manager or when creating new user.

## Supported Profiles

Software Risk Manager adheres only to the Web SSO Profile. (Software Risk Manager
also does not make use of RelayState.) Other profiles, including Single Logout
(SLO), are unsupported.

## Basic Configuration

Upon successful configuration and after navigating to the Software Risk Manager Login
page, your `codedx.log` file should contain the message "Successfully
configured SAML authentication." Otherwise, it will contain "SAML authentication was
either incomplete or missing, skipping." A minimal configuration looks like the
following:

```
    auth.saml2.identityProviderMetadataPath = C:/idp-metadata.xml
    auth.saml2.keystorePassword = jkspassword
    auth.saml2.privateKeyPassword = pkpassword
```

The IdP XML should have a root element of
`<*:EntitiesDescriptor>`. with
`<*:EntityDescriptor>` elements inside. The recommended
location for this file is in the Software Risk Manager appdata folder, but this is not in a requirement. Ensure that Software
Risk Manager has the necessary permissions to read the XML file.

The keystore is used by Software Risk Manager to sign requests to your IdP. This
keystore will be created automatically unless `keystorePath` is
assigned and a file exists at the assigned path. The passwords for the keystore and
its private key must be set manually through the `keystorePassword`
and `privateKeyPassword` properties. The assigned passwords will be
used to create the keystore if necessary. The default path for the keystore is in
Software Risk Manager appdata directory, at
`.../codedx_appdata/keystore/codedx-saml.jks`. If a custom
keystore is provided, this folder is the recommended location. Ensure that Software
Risk Manager has the necessary permissions to read the keystore file.

Software Risk Manager has no inherent requirements for the IdP it authenticates
against. Requests from Software Risk Manager can be configured as necessary using
the properties listed above to meet the needs of your IdP.

Navigating to Software Risk Manager will redirect you to your IdP Login Portal, which
you may sign into but will not provide access to Software Risk Manager. You must
first add your SAML account as a user recognized by Software Risk Manager. See the
*Software
Risk Manager User Guide* for more information. By default,
Software Risk Manager will redirect you to your IdP, but you can sign in using the
Software Risk Manager *Login* page by navigating to
`/login?local`. Here you can enter the default Software Risk
Manager admin and password to sign in and add yourself and others as
SAML-authenticated users.

If you get a generic error page after signing in with SAML, you may need to
explicitly assign the Software Risk Manager base path. This should match what you
have registered with your IdP. See the section on Multiple Hosts below for
more information.

### SP Metadata

The full XML Metadata for Software Risk Manager as an SP can be downloaded from
the Users
page if SAML has been configured (see figure below). Notable details
are provided below.

[image: image]

The Software Risk Manager Assertion Consumer Service (ACS) endpoint is at
`/login/callback/saml`, relative to your Software Risk
Manager URL. For example, if hosting at `https://localhost/srm`,
the ACS will be `https://localhost/srm/login/callback/saml`.

The metadata XML will list the ACS binding type as `HTTP-POST`,
regardless of the binding type set in `codedx.props`. This can be
ignored. Software Risk Manager will use the binding type specified in
`codedx.props`. You can change the binding type in that XML
if necessary.

### Callback URL, Proxies, and Multiple Hosts

Software Risk Manager can be accessed through a variety of hosts (such as machine
name, FQDN, IP address, reverse proxy), but only one will be recognized by
Software Risk Manager as its ACS. The Software Risk Manager ACS is built
dynamically when the first request is made, and it is based on the first URL
requested from Software Risk Manager. If you access Software Risk Manager
through `https://192.168.1.10/srm`, the ACS URL will be at
`https://192.168.1.10/srm/login/callback/saml` and Software
Risk Manager will only respond to SAML requests to that endpoint. SP metadata
will also be based on this URL.

In this case, SAML authentication will fail unless your IdP has the Software Risk
Manager ACS at the `https://192.168.1.10/...` endpoint. The
downloaded SP metadata will have your SAML IdP redirect using the Software Risk
Manager IP, when you may want it to point to a reverse proxy instead.

You can assign the `auth.hostBasePath` property in your
`codedx.props` file to force a consistent ACS URL. This
affects the endpoint that Software Risk Manager will listen to, along with the
SP metadata that it generates. If Software Risk Manager is accessible at
`https://myhost/srm`, you can add the following:

```
    auth.hostBasePath = https://myhost/srm
```

This will force a consistent ACS URL to `https://myhost/srm`.
(**Note:** This only affects authentication; it will not change the base
path of Software Risk Manager itself.)

## Single Log-Out and Ensuring Active Sessions

Software Risk Manager currently does not support any of the capabilities specified in
the SAML Single Logout (SLO) Profile.

If a user signs out from their SAML session, this logout will not automatically
propagate to Software Risk Manager.

To prevent the use of expired SAML sessions, we strongly recommend configuring Session Lifetimes within Software Risk
Manager to ensure the SAML session is validated frequently.

## Automatic SAML Authentication

Once SAML is configured within Software Risk Manager, all login requests will be
redirected to your IdP authentication portal. Authenticated users will be redirected
back to Software Risk Manager, where they can view the *Projects* page if they
are registered with Software Risk Manager. Otherwise, they will be redirected to the
Software Risk Manager *Login* page, where they can log in as a local user or
retry authentication with your IdP. Software Risk Manager does not perform any
single sign-out; signing in with a different SAML user will require signing out
through your IdP portal and re-authenticating with the new user information.

You can disable the automatic redirect to your IdP by setting
`auth.autoExternalRedirect = false` in your
`codedx.props`.

## Multiple Software Risk Manager Deployments with the Same IdP

Authenticating multiple Software Risk Manager instances against the same IdP requires
setting a unique Service Provider Entity ID for each deployment. Assign the
`auth.saml.entityId` property to different values for each
deployment, and register each new Entity ID with your IdP using the appropriate ACS
for the associated deployment.

For example, consider the following: Two Software Risk Manager deployments are hosted
at `https://foo.com/srm` and `https://bar.com/srm`.
Modify `auth.saml.entityId` for both; in this case they are assigned
to `https://codedx-foo.com` and
`https://codedx-bar.com`, respectively. Software Risk Manager
places no restrictions on Entity IDs; you can assign them as appropriate for your
case.

Restart both Software Risk Manager deployments and register them with your IdP as
follows:

- Register entity `https://codedx-foo.com` with its ACS
  `https://foo.com/srm/login/callback/saml`
- Register entity `https://codedx-bar.com` with its ACS
  `https://bar.com/srm/login/callback/saml`

Both deployments will authenticate against your SAML provider. Note that users
registered with one Software Risk Manager deployment will not be registered with
another, even if they authenticate against the same IdP. Accessing both deployments
with SAML user "John Doe" will require registering them with each Software Risk
Manager deployment individually.

While multiple Software Risk Manager installations are supported, it is discouraged
to run them on the same machine. This will likely lead to resource contention,
resulting in performance degradation in those installations.

## Forcing Local Sign-in

Software Risk Manager does not validate that the configured IdP is available before
attempting to authenticate. If your SAML IdP becomes unavailable or you need to sign
in through a local account, there are two options:

1. Set `auth.autoExternalRedirect = false` in your
   `codedx.props`. Unauthenticated users will be redirected to
   the Software Risk Manager *Login* page instead of your IdP portal, where
   they can sign in with a local account or attempt to sign in through your IdP
   portal through a link below the sign in form.
2. Manually navigate to `/login?local`, relative to your Software
   Risk Manager hosting path. This will force the Software Risk Manager
   *Login* page to display regardless of the value of
   `auth.autoExternalRedirect`.

Note: You may not be able to sign in as a SAML user while your IdP is offline, even if
you had been previously authenticated.

## IdP-Specific SAML Instructions

Identity Providers with known special considerations are discussed below. Presence
(or non-presence) of a particular IdP does not reflect which IdPs are "supported" or
"preferred"; the list of IdPs and known issues may not be comprehensive.

## Microsoft Entra ID (formerly Azure AD)

Software Risk Manager can use Microsoft Entra ID for SAML authentication by registering Software
Risk Manager as an "Enterprise application." To do this, click "Create your own
application," enter a name, and then select "Non-gallery" from the available
options.

Once created, open the newly created application, select "Single sign-on," and then
select "SAML."

Only two properties must be specified: the app's Identifier and Reply URL. The
Identifier should be `https://codedx.com`, unless
`auth.saml2.entityId` was changed to a different value in the
properties file. The Reply URL should be the Software Risk Manager ACS URL as
described in the SP Metadata
section.

**Note:** Software Risk Manager does not support Relay State or Single Logout.
Sign-on URL may be blank or set to the `/srm/login` page.

After editing "Basic SAML Configuration" as described, save your changes and confirm
that the Identifier field was set with the expected value.

There are two locations to confirm: Within the "Single sign-on" page for your
Enterprise registration, and the "Expose an API" page in the associated App
registration.

The Identifier from the "Enterprise registration -> Single sign-on" page should
match the "Application ID URI" from the "App registration -> Expose an API" page;
both should match the entity ID for Software Risk Manager.

### Important Properties Settings

Configuration of Software Risk Manager for Entra ID only requires the basic
mandatory settings: `auth.saml2.identityProviderMetadataPath`,
`auth.saml2.keystorePassword`, and
`auth.saml2.privateKeyPassword`.

The `maximumAuthenticationLifetime` must also be configured
properly for a reliable integration. The section below discusses this in more
detail.

### Session Lifetime Considerations

Integrations with Entra ID must pay attention to the maximum lifetime of a
session. At the time of writing, Entra ID's default lifetime is a "rolling
window" of 90 days. Typically the 90 days would be converted to seconds and used
as the value for the Software Risk Manager property
`auth.saml2.maximumAuthenticationLifetime`.

Synchronizing this setting between Software Risk Manager and Entra ID (or any
IdP) is important: If Software Risk Manager receives an authentication response
containing a session older than the maximum allowed lifetime, the response will
be rejected with an error message.

If a policy with a rolling window is applied, there is effectively no single
"maximum" age Software Risk Manager can expect. In this case, we recommend
disabling the sliding window within Entra ID, or disabling the Software Risk
Manager SAML session lifetime limit by setting
`auth.saml2.maximumAuthenticationLifetime` to
`-1`.

The original 90-day value (`7776000` seconds) may be used
regardless of the rolling window. In this case, users attempting to authenticate
with Software Risk Manager must manually start a new session with their IdP once
their session exceeds that age.

Behavior in Entra ID may be viewed or customized with the ["Conditional Access"](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/howto-conditional-access-session-lifetime) policies
available.

## SAML Group Mapping

Software Risk Manager can detect SAML group information during authentication, which
can then be used to auto-create SAML users and enable mapping between SAML and SRM
groups to automatically add/remove users from SRM
groups.

- The `auth.saml2.groupMappingMethod` option in
  `codedx.props` specifies which method to use. For more information,
  see the Single SAML Attribute
   and 
  Multiple SAML Attributes sections below.
- The `auth.saml2.groupNameMatcher` property lets you define a
  regular expression with a required capture group to extract group names from
  SAML attributes. Only the part of the attribute matched by the capture group
  is used as the group name. If the pattern is invalid or does not include a
  capture group, authentication will fail.

  This is particularly useful when your group names are formatted like LDAP DNs.
  For example: if your group name is

  ```
  cn=TESTGROUP1,ou=groups,o=org
  ```

  and you want to authenticate based on whether the user is part of the
  `TESTGROUP1` group, then you may set

  ```
  auth.saml2.groupNameMatcher = cn=(\w+),ou=groups,o=org
  ```

  to
  successfully authenticate such users.

Software Risk Manager can read group information for a SAML user through either of
the following methods:

- **Method 1:** A single SAML attribute containing a list of user groups
  (`string-list`)
- **Method 2:** Multiple SAML attributes, each indicating membership of one
  user group (`multi-attr`)

Selecting the appropriate mapping method will depend on your SAML IdP and how it is
configured to provide user group information. (These methods cannot be used together
at the same time.)

Note: SRM does not support the Assertion Query/Request SAML profile and can only access
user SAML groups during authentication. Enabling Session Lifetimes is recommended to
ensure users are regularly signed back in and updated (see Session Expiration).

### Method 1: Single SAML Attribute

For single SAML attribute mapping, add the following to the properties file:
`auth.saml2.groupMappingMethod = string-list`. This method
also requires setting the `auth.saml2.groupAttribute` property to
the name of the SAML attribute containing the list of user groups (this
attribute name is case-sensitive).

This attribute will be interpreted as a comma-separated string, where each entry
is a group that the user is a member of.

This method supports both single-value and multi-value attributes. For
multi-value attributes, each value is interpreted as an additional
comma-separated list and is combined with the others for the final list of user
groups.

### Method 2: Multiple SAML Attributes

For multiple SAML attribute mapping, add the following to
the properties file: `auth.saml2.groupMappingMethod =
multi-attr`. This method also requires adding at least one prop,
beginning with `auth.saml2.groupAttributePattern`. (The prop
`groupAttributePattern` acts as a template for extracting
groups from a user's list of attributes.)

The value of
`groupAttributePattern` should match the format of the
relevant attribute names and use `{group}` as a placeholder for
the part containing the group name. For example, given an attribute named
`is-secops-group`, you would use the pattern
`is-{group}-group`.

You can handle multiple patterns by
adding additional `groupAttributePattern` props, such as in the
following example:

```
auth.saml2.groupAttributePattern = is-{group}-group
auth.saml2.groupAttributePattern-other = member-of-{group}
```

Note: A pattern value must contain exactly one occurrence of the text
`{group}`.)

All patterns described by props starting
with `auth.saml2.groupAttributePattern` will be used together to
detect the list of user groups. (This is unaffected by whether one pattern
detects a match or all patterns have a match—if any pattern matches an attribute
name, it will be recognized as a group name, regardless of whether other
patterns match that attribute.)

With `groupMappingMethod =
multi-attr` and `groupAttributePattern*` set, a user
will be considered a member of any group that matches the specified pattern.

You can also have Software Risk Manager check the value of the attribute using
`auth.saml2.membershipAttributeValues` and/or
`auth.saml2.nonMembershipGroupAttributeValues`. These options can
be set to comma-separated lists of values that are used to determine
membership/non-membership:

- If `membershipAttributeValues` is set, a user will only be
  considered a member of a group if the attribute contains one of the values
  assigned to the prop. Any other value will be interpreted as
  “non-membership.”
- If `nonMembershipAttributeValues` is set, a user will be
  considered as not a member of the group if the attribute contains one of the
  assigned values. If not set, or if the attribute value does not match, group
  membership is determined by `membershipAttributeValues`
  behavior.
