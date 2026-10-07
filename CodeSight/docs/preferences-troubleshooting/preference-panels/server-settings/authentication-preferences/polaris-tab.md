---
title: "Polaris tab"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/polaris-tab.html"
content_id: "Rq8bafLILjmiEHR4n64anQ"
version: "2026.9.0"
section: "Code Sight: Preferences and Troubleshooting"
scraped_at: "2026-10-06T23:39:56.401213+00:00"
---

# Polaris tab

Displays controls for configuring a Polaris server whose detected issues will display in Team View; see Viewing Polaris issues on the server.

Figure 1. Authentication controls for Polaris (IntelliJ)
  
 [image: IntelliJ: Polaris authentication panel]

Figure 2. Authentication controls for Polaris (VS Code)
  
 [image: VS Code: Polaris authentication panel]

## Authentication

Polaris URL
:   Enter the URL of the Polaris instance that you use.

    Use default Polaris URL

    If you use the default instance of Polaris, click to turn on this option.
    Code Sight updates the Polaris URL field.

Token
:   Enter the token for the chosen instance of Polaris.

    As the dialog explains, you can obtain the token value while running Polaris itself.

Proxy
:   Configure Proxy
    :   Click to display and use the Proxy settings.

Test Connection
:   After you have chosen a Polaris instance and entered its token, click this button to verify that the connection is good.

    If the connection is good, Code Sight displays a message that confirms that the connection succeeded.

      
     [image: Polaris: Successful connection]

Once you have set up the connection to Polaris, then click Apply (in IntelliJ) or Save Settings (in VS Code)
to save these preference settings.

## Configure Source

Configure Source
:   Once you have a working connection to your Polaris server, click Configure Source to
    display the Sources panel and choose the Polaris Application and Project whose issues you want to
    see displayed in Team View.
