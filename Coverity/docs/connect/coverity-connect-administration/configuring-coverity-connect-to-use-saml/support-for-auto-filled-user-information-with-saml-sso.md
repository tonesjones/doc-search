---
title: "Support for auto-filled user information with SAML SSO"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/support-for-auto-filled-user-information-with-saml-sso.html"
content_id: "fhCnlBSbJYFo5ftWPiUpbQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:52.892707+00:00"
---

# Support for auto-filled user information with SAML SSO

Starting with Coverity 2022.9, Coverity Connect offers the possibility to consume user
information (first name, last name, and email) from the identity provider (IdP) for SAML
users.

In order for Connect to autofill your first name, last name and/or email when logging in with
SAML SSO, you need to add an attribute for each desired information in the IdP. The
attributes must **not** set a namespace, and have to use the following names:

- **firstName** for first name
- **lastName** for last name
- **email** for email

You should use the appropriate source attributes for first name/last name/email given in the
IdP. After adding the desired attributes in the IdP, your user information will be
updated in Connect upon sign in.
