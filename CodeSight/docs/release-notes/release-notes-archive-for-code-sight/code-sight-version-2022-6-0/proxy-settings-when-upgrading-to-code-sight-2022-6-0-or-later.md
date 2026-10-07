---
title: "Proxy settings when upgrading to Code Sight 2022.6.0 or later"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/proxy-settings-when-upgrading-to-code-sight-2022.6.0-or-later.html"
content_id: "L1CXcNFGA8kZzg4K8zVjmQ"
version: "2026.9.0"
section: "Code Sight Release Notes and Known Issues"
scraped_at: "2026-10-06T23:39:59.888869+00:00"
---

# Proxy settings when upgrading to Code Sight 2022.6.0 or later

Although Use System Proxy is now the default choice,
if you are upgrading from a previous version of Code Sight, the resulting proxy choice
depends on the preferences in your previous installation.

- If your previous choice was No Proxy, then in release 2022.6.0
  the choice will remain No Proxy.
- If your previous choice was Manual Proxy, then in release 2022.6.0
  the choice will remain Manual Proxy.
  The manually chosen protocol, host name, port, and authentication information will remain in effect.

  If, after upgrading, you want to use Use System Proxy instead of the
  manual settings, you will need to choose Use System Proxy yourself.
- If you *did not specify* a proxy setting prior to upgrading, then in release 2022.6.0
  the choice is automatically changed to Use System Proxy.

For more information, see Proxy settings.
