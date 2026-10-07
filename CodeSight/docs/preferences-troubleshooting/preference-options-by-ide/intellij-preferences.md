---
title: "IntelliJ Preferences"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/intellij-preferences.html"
content_id: "krBDdGDiJ_gQirfIaEIzaQ"
version: "2026.9.0"
section: "Code Sight: Preferences and Troubleshooting"
scraped_at: "2026-10-06T23:39:56.014788+00:00"
---

# IntelliJ Preferences

In Code Sight, IntelliJ (and the other JetBrains IDEs) provides several kinds of preference settings.

[image: Clickable Preferences icon in the Code Sight interface for IntelliJ] To access the preferences for IntelliJ, click the icon that appears above the Code Sight views, or go to the system toolbar and choose IntelliJ IDEA → Settings. IntelliJ displays its Preferences dialog.

Figure 1. Preference choices for IntelliJ  
 [image: Preference choices for Code Sight running in IntelliJ]

General Settings
:   The General Settings panel includes a check box for enabling or disabling Telemetry in Code Sight, as well as two further choices for customizing the IDE interface.

Server Settings
:   Authentication
    :   This panel has tabs for authenticating servers and scan engines.

        - Polaris

          Displays authentication controls for a Polaris server.
        - Software Risk Manager

          Displays authentication controls for a Software Risk Manager server.
        - Coverity on Polaris / Coverity Connect

          Displays authentication controls for a Coverity server.
        - Black Duck

          Displays authentication controls for a Black Duck server.

    Sources
    :   Displays the servers currently configured for remote (Team View) issues, and lets you edit the configuration.

Analysis Settings
:   Let you configure a system-local location for the Rapid Scan Static and Rapid Scan SCA engines. This choice displays a panel that links to a panel for each engine.

    Rapid Scan Static
    :   Takes you to the Rapid Scan Static panel.

    Rapid Scan SCA
    :   Takes you to the Rapid Scan SCA panel.

Proxy Settings
:   Enable Code Sight to run with a proxy server.

Troubleshooting
:   Displays a button for saving the Code Sight log, for debugging purposes.

Environment Variables
:   Configure environment variables in your IDE.
