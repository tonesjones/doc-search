---
title: "Configuring sign-in settings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-sign-in-settings.html"
content_id: "6tAkw_xK68MuE8nXdtz0QQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:26.342783+00:00"
---

# Configuring sign-in settings

To control user access to Coverity Connect, sign in to Coverity Connect using a Web
browser as the admin user. Then go to Configuration > System > Authentication and Sign In.

**To configure sign-in settings:**

  
 [image: image]   

1. Select from the sign-in options:

   Disable local password authentication
   :   Entirely disable local account access, and use LDAP for
       authentication. Requires previous LDAP configuration.

   Allow email password recovery
   :   If the user is locked out due to incorrect password attempts, the
       password can be requested using email. Requires previous email
       configuration.

   Time out signed in users after [N] minutes of inactivity
   :   Set the number of minutes of inactivity before requiring users to
       sign in again. Note that this option is permanently enabled. Its
       default setting is 120 minutes.
2. If you are using LDAP, select from the following options:

   Create LDAP users automatically on sign-in
   :   Creates users in Coverity Connect upon successful authentication with
       your LDAP server. Requires LDAP configuration.

       You can also choose to only create users that belong to imported LDAP
       groups.

   Only create users that are members of imported group(s)
   :   Provides for backward compatibility with Microsoft Azure Entra ID
       products that require LDAP users to be members of an LDAP
       group.
3. If you are using SAML SSO, you can choose the following option:

   Create SAML users automatically on sign-in
   :   Creates users in Coverity Connect automativally upon successful
       authentication. Requires SAML configuration.
4. Click Done to finalize your changes and exit the
   screen.

Sign In Log
:   The Sign In Log shows a history of user session
    activity.

Note: If you need to reset the Administrator password, use the
`reset-admin-password` option of the `cov-admin-db` command. For more information, see
the Coverity 2026.6.0 Command Reference.
