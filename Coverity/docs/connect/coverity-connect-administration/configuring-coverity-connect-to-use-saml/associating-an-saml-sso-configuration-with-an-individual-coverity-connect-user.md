---
title: "Associating an SAML SSO configuration with an individual Coverity Connect user"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/associating-an-saml-sso-configuration-with-an-individual-coverity-connect-user.html"
content_id: "zXUvGeQTCyrQNn~Z6owvqQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:51.640251+00:00"
---

# Associating an SAML SSO configuration with an individual Coverity Connect user

Important: SAML SSO requires an SSO user name and the corresponding Coverity
Connect user name to be the same.

**To set up SAML SSO for an individual Coverity Connect user:**

Typically it is easiest to configure users within the identity provider, and then in
Coverity Connect, to turn on the Create SAML users
automatically on sign in option. If for some reason it is convenient to
configure one user at a time, from within Coverity Connect, these steps describe how to
do so.

Note: For the `admin` user, logging in with SAML SSO is not
allowed.

1. On the Coverity Connect menu bar, choose Configuration > Users & Groups.
2. On the Users tab, click to highlight a particular
   user.

   Note: Enabling SAML is not available at the Group level.
3. In the User Details area, click Edit
4. In the dialog for this particular user, open the SAML:
   drop-down list, and choose the current SAML configuration.

   The SAML choice enables the administrator to create a user
   account without having to specify a password.

     
    [image: image]
5. Click OK.
6. Click Done.
