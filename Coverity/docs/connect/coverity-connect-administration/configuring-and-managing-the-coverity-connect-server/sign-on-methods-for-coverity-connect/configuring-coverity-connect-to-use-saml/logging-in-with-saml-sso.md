---
title: "Logging in with SAML SSO"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/logging-in-with-saml-sso.html"
content_id: "UHO7HWVNU8UjMBZMNAVJtA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:47.318189+00:00"
---

# Logging in with SAML SSO

Once SAML 2.0 SSO is configured, the Coverity Connect login page shows a button that says
Sign in with <saml config display name> instead,
where <saml config display name> refers to the Display Name specified when SAML was configured.

  
 [image: image]   

A user that the Coverity Connect server recognizes, and who has already signed in to a
different app using SAML SSO, can click this link and then begin using the Coverity
Connect interface without having to retype their user name and password.

In the modern UI, when the Disable all sign in
types except for SAML checkbox is selected and the authentication method
is set to SAML, the Sign in with SSO button appears on the login
screen with no username and password fields. For more information, see Creating a SAML SSO configuration.
