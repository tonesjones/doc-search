---
title: "Viewing Software Risk Manager issues on the server"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/viewing-software-risk-manager-issues-on-the-server.html"
content_id: "KfXpo~Blol4Jhi7lnO6cDA"
version: "2026.9.0"
section: "Software Risk Manager with Code Sight"
scraped_at: "2026-10-06T23:39:55.356207+00:00"
---

# Viewing Software Risk Manager issues on the server

Issues reported by the Software Risk Manager appear in Team View.

The Team View panel appears in the Code Sight interface for the Android Studio, JetBrains (including IntelliJ),
Visual Studio, and VS Code editors.

Figure 1. Issues detected by Software Risk Manager displayed in Team View
  
 [image: Team view displaying Software Risk Manager issues]

(Example from IntelliJ)

Note:
Issues in a scan from a server might report severities that differ from the severities reported by locally run scans.

[image: image] In the IntelliJ and Visual Studio interfaces, policy violations reported by the Software Risk Manager
display an icon in the shape of a shield.

“Issues from” drop-down list
:   Use this list to choose one of the source servers you have configured.

    **Configure a new source:**
    You can also choose Configure sources to display the Sources panel and configure a new one.

[image: image]
:   Click the Refresh icon to refresh the current list.

    Issues in the list do not refresh automatically. They do refresh when you click this icon or you choose a
    different software-integrity product from the Issues From (IntelliJ and Visual Studio) or the Source (VS Code) drop-down list.

To configure an SRM server for your Code Sight installation, see Software Risk Manager tab.

Note:
Prior to 2023, the Software Risk Manager product was known as “Code Dx”.

## Issue Details

Details about issues in Team View can vary, depending on the currently chosen server and product.
For more information, please see the documentation for that particular product.
