---
title: "Coverity on Polaris / Coverity Connect tab"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/coverity-on-polaris/coverity-connect-tab.html"
content_id: "fHB_It0uYaIk3wq_78A4kw"
version: "2026.9.0"
section: "Code Sight: Preferences and Troubleshooting"
scraped_at: "2026-10-06T23:39:56.530408+00:00"
---

# Coverity on Polaris / Coverity Connect tab

Displays controls for configuring a Coverity (Code Analysis) server.

Note:
The Coverity server can be either a Coverity on Polaris server or a Coverity Connect server:
For more information, see Setting up Coverity for Code Sight.

## Email / User Name panel

Figure 1. Coverity server authentication tab for IntelliJ: Email / User Name panel
  
 [image: Coverity authentication tab showing Email / User Name panel]

Email / User Name
:   Enter the name you use to log in to the Coverity server that you use.

Server URL
:   Enter the URL of the Coverity server that you use.

Configure Proxy
:   Click to display the Proxy Settings panel and update the proxy for Code Sight to use, if any.

Change Credentials
:   When you have updated other settings on this tab, click Change Credentials
    to display the Auth Key / Password panel, where you enter the authorization key or password for the Coverity server you chose.

## Auth Key / Password panel

Figure 2. Coverity server authentication tab for IntelliJ: Auth Key / Password panel
  
 [image: Coverity authentication tab showing Auth Key / Password panel]

1. Use controls on this panel to enter either an authentication key or a password for your Coverity server.
2. When you have done so, click Change Credentials once again.

   If the credentials are valid, Code Sight says so, and displays a thumbs-up icon.
3. Click Done to complete the setup.

## Configure Souce section (both panels)

This section contains a Configure Source link.
If you wish to view remote issues from a Coverity server in Team View,
click this to display the Sources configuration panel, where you can
choose one or more Coverity projects and streams to report on.
