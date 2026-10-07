---
title: "Authentication preferences"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/authentication-preferences.html"
content_id: "ZfWnxWcuAiuTYXHnoBxG4Q"
version: "2026.9.0"
section: "Code Sight: Preferences and Troubleshooting"
scraped_at: "2026-10-06T23:39:56.346317+00:00"
---

# Authentication preferences

The Authentication preferences panel lets you change the credentials
for Coverity Analysis, Black Duck Source Code Analysis, or both.
For IntelliJ and other JetBrains IDEs, Microsoft Visual Studio, and VS Code, you can also configure networked products for Team View: see
Viewing Polaris issues on the server and
Viewing Software Risk Manager issues on the server.

## Eclipse

Figure 1. Authentication preferences for Eclipse
  
 [image: Authentication preferences panel for Eclipse]

Note:
This panel also links to the Proxy Settings panel.

## Visual Studio

Figure 2. Authentication preferences for Visual Studio
  
 [image: Authentication preferences panel for Visual Studio]

In Visual Studio, the Authentication panel consists of four tabs:

- Polaris
- Software Risk Manager
- Coverity on Polaris / Coverity Connect
- Black Duck SCA

These tabs also include the Export Logs control.

Troubleshooting
:   The Export Logs button appears in this group.
    See Troubleshooting / Export Logs.

## IntelliJ

In IntelliJ, the Authentication panel consists of four tabs:

- Polaris
- Software Risk Manager
- Coverity on Polaris / Coverity Connect
- Black Duck SCA

## Visual Studio Code

VS Code has separate authentication panels for Coverity Connect, Black Duck SCA, and server-based software-integrity products.
To see these settings, click one of the links beneath the “Server Connections” label in the STATUS view.

Figure 3. Links to server-authentication controls in VS Code
  
 [image: Links to open an auth panel for scan-engine authorizations and configurations]
