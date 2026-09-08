---
title: "Session Expiration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/session-expiration.html"
content_id: "1HP~3scYtKLGBWLdaoQHjw"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:26.222149+00:00"
content_hash: "59d5427bdb2fce261209820eda129841c0e796ab4ade722009c0d20b69af4b34"
---

# Session Expiration

You can set user sessions to expire after a period of inactivity using the settings
below:

- `session.lifetime` - sets the duration of inactivity required before
  automatically signing out a user; if set to 0, sessions will never expire [default: 20 minutes]
- `session.timeout-notice` - sets the point at which the user will be
  notified when their session will expire [default: 2 minutes]

Both of these properties use a readable duration format, that is, `1
hour`, `1 hour and 30 minutes`, `3 days`, and so
on.

Enabling session expiration requires assignment of `session.lifetime`, but
`session.timeout-notice` is optional. If left unassigned, the timeout
notice will be the shortest of either two minutes or 25% of the session expiration
period.

If session expiration is enabled, the user's session will be closed if it either times
out or if the user closes their browser.

**Note:** If combining session expiration with SAML authentication, make sure to set
`auth.saml2.forceAuth = true` so that the user always has to
re-authenticate with your IdP.

  
 [image: image]   

Sessions can also be invalidated if SRM is configured to only allow one user session at a time with the following setting:

- `srm.limit-sessions.enabled` - [default: false] Controls if user sessions should be limited to one at a time
