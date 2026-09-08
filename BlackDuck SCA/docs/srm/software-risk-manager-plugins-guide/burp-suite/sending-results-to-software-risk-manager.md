---
title: "Sending Results to Software Risk Manager"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/sending-results-to-software-risk-manager.html"
content_id: "_en70~QDXq15gSX6c1TEcg"
version: "latest"
section: "Software Risk Manager Plugins Guide"
scraped_at: "2026-09-08T20:06:03.282242+00:00"
content_hash: "33880aa43d3b8dff59d857d54bcc42f489b3a3de7b57913f711d46bf2d35709e"
---

# Sending Results to Software Risk Manager

After scanning with Burp Suite, there are two ways you can send the results to Software
Risk Manager. The first is to choose a *Target URL* from the list in the Software
Risk Manager Settings in Burp Suite. After performing a scan, click the *refresh*
button to list all of the available targets. Multiple targets can be selected from the
list using *Ctrl + Click*.

Select the project you would like to use, then click the *Send to Code Dx* button to
send the results.

  
 [image: image]   

You will receive a message indicating whether or not the action was successful.

  
 [image: image]   

The second method to send the results is to use the context menu in the Issues panel of
the Target view. To do this, open the Target view and select your target or targets from
the Site map.

  
 [image: image]   

Select the issues that you want to analyze and right click in the Issues panel. Click the
*Send to Code Dx* button at the bottom of the context menu.

  
 [image: image]   

A menu will pop up and will ask you to select the Software Risk Manager project. Note
that this option is independent of the project and target settings from the Software
Risk Manager view.

  
 [image: image]   

As with the previous method, you will receive a message indicating whether or not the
action was successful.
