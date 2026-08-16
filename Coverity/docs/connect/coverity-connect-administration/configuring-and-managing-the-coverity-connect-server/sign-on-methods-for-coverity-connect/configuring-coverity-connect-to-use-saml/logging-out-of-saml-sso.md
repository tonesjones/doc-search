---
title: "Logging out of SAML SSO"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/logging-out-of-saml-sso.html"
content_id: "xVfD6MxPr~5ImqwLI1UZKg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:48.371865+00:00"
---

# Logging out of SAML SSO

Coverity Connect does not implement single sign-out.

In other words, signing out of Coverity Connect signs you out locally, but *does
not* end your SAML SSO session. You are still logged in to other applications or
services that use the same identity provider, and you can log back in to Coverity
Connect, without reentering your ID and password, by simply clicking the Sign
in with saml instead link.

To terminate your SAML SSO session, in addition to logging out of Coverity Connect you
also need to log out of one of the other applications or services associated with SAML
SSO on the same identity provider.
