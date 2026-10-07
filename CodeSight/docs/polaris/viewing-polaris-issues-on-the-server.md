---
title: "Viewing Polaris issues on the server"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/viewing-polaris-issues-on-the-server.html"
content_id: "BNFDVJlVglR792mV2EIUew"
version: "2026.9.0"
section: "Polaris with Code Sight"
scraped_at: "2026-10-06T23:39:55.092698+00:00"
---

# Viewing Polaris issues on the server

Issues reported by Polaris appear in Local
View when detected in a local project; otherwise, they appear in
Team View.

Figure 1. Issues detected by Polaris displayed in Team
View
  
 [image: Team view displaying Polaris issues]

Note:
Issues in a scan from a server might report severities that differ from the severities reported by locally run scans.

“Issues from” drop-down list
:   Use this list to choose one of the source servers you have configured.

    **Configure a new source:**
    You can also choose Configure sources to display the Sources panel and configure a new one.

[image: image]
:   Click the Refresh icon to refresh the current list.

    Issues in the list do not refresh automatically. They do refresh when you click this icon or you choose a
    different software-integrity product from the Issues From (IntelliJ) or the Source (VS Code) drop-down list.

To configure a Polaris server for your Code Sight installation, see Polaris tab.

## Issue Details

Details about issues in Team View can vary, depending on the currently chosen server and product.
For more information, please see the documentation for that particular product.
