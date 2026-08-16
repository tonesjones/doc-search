---
title: "Configuring Coverity Connect to use SAML"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-coverity-connect-to-use-saml.html"
content_id: "5knLapA2lNmf2T1zaQfRow"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:46.593388+00:00"
---

# Configuring Coverity Connect to use SAML

SAML (Security Assertion Markup Language) is an open standard for authenticating and
authorizing exchanges between an *identity provider* (IdP) and a *service
provider* (SP). In particular, SAML 2.0 is often used to implement single sign-on
(SSO) to Web sites, and that is how it is used in Coverity Connect.

Attention:
The Coverity Connect SAML implementation will work with any multi-factor authentication (MFA) that has been set up on the IdP.

Important: If TLS/SSL has not been enabled, then for successful single sign-on
the identity provider (IdP) and the metadata should specify a plain HTTP (non-secure)
Web connection.

See Configuring Coverity Connect for TLS/SSL.
