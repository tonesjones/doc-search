---
title: "Switching to the modern UI"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/switching-to-the-modern-ui.html"
content_id: "Sst3tRbMYO90jleXSf5tsw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:01.480757+00:00"
---

# Switching to the modern UI

## Enabling the modern UI preview button

The Preview Modern UI button does not appear in the classic
interface unless the modern UI preview is enabled in the server configuration.
To enable it, add or set the following line in the
cim.properties configuration file:

```
show.modern.ui.preview.button=true
```

To verify this setting, navigate in the classic interface to Help > System Diagnostics > Config Files.

## Switching to the modern UI

Note: Localization support for non-English languages will be addressed in a future release.

You can switch to the modern UI to access updated features and improved workflows.
The switch takes effect immediately and work done in the modern UI persists
across sessions.

1. Sign in to Coverity Connect. The classic interface
   Projects page appears.
2. Click Preview Modern UI in the header bar.

The modern UI opens in a new browser tab. Your classic interface remains available in the original tab.

To return to the classic interface, switch to the original browser tab.

## Logging in to the modern UI

You can access the modern UI directly without using the classic interface by navigating to the
Modern UI login URL.

Enter the following URL in your browser:

```
https://your-coverity-server:8080/ui/login
```

Replace `your-coverity-server` with the hostname or IP address of your Coverity Connect server. If your server uses HTTPS, use
`https://` instead of `http://`. SAML and LDAP are
recognized.

When the Disable all sign in types except for SAML checkbox is selected
and the authentication method is set to SAML, the Sign in with
SSO button appears on the login screen with no username and password
fields. Next to the SSO button is a local admin sign-in link. Only the built-in
admin account can sign in locally. For more information, see Creating a SAML SSO configuration.

After signing in, you will land directly on the modern UI Projects page.
