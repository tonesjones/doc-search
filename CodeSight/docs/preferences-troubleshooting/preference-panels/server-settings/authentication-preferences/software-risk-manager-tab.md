---
title: "Software Risk Manager tab"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/software-risk-manager-tab.html"
content_id: "4YD5Eap1w9UkjxPUMJXlSA"
version: "2026.9.0"
section: "Code Sight: Preferences and Troubleshooting"
scraped_at: "2026-10-06T23:39:56.452899+00:00"
---

# Software Risk Manager tab

Displays controls for configuring a Software Risk Manager server whose detected issues will display in Team View;
see Viewing Software Risk Manager issues on the server.

Figure 1. Authentication controls for Software Risk Manager in IntelliJ
  
 [image: IntelliJ: SRM authentication panel]

Figure 2. Authentication controls for Software Risk Manager in VS Code
  
 [image: VS Code: SRM authentication panel]

## Authentication

SRM URL
:   Enter the URL of the Software Risk Manager instance that you use.

Token
:   Enter the token for the chosen instance of Software Risk Manager.

    As the dialog explains, you can obtain the token value while running the Software Risk Manager itself.

Proxy
:   Configure Proxy
    :   Click to display and use the Proxy settings.

Test Connection
:   After you have chosen a Software Risk Manager instance and entered its token, click this button to verify that the connection is good.

    If the connection is good, Code Sight displays a message that confirms that the connection succeeded.

      
     [image: SRM: Successful connection]

Once you have set up the connection to the Software Risk Manager, then click Apply (in IntelliJ) or Save Settings (in VS Code)
to save these preference settings.

## Configure Source

Configure Source
:   Once you have a working connection to your Software Risk Manager server, click Configure Source to
    display the Sources panel and choose the Software Risk Manager Project and Branch whose issues you want to
    see displayed in Team View.
