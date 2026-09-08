---
title: "Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/configuration.html"
content_id: "JWEPitY0xJIj~unwd61X5w"
version: "latest"
section: "Software Risk Manager Plugins Guide"
scraped_at: "2026-09-08T20:06:02.442030+00:00"
content_hash: "1430f440a874283feecf7afe15ccb7088b285caea3bf6f43407036adb32035f5"
---

# Configuration

To configure the Burp Suite plugin, navigate to the Code Dx tab.

The *Server URL* and *API Key* are required fields for sending data to Software
Risk Manager. Ask your Software Risk Manager administrator to generate the server API key with
the `create`
role for the project(s) which the plugin must interact with.

  
 [image: image]   

Once the *Server URL* and *API Key* fields are populated, click the
*Refresh* button to list the projects available to the API key in the
*Project* dropdown. It is highly recommended that you specify an HTTPS URL,
since using HTTP is insecure.

  
 [image: image]   

If you receive a warning regarding an invalid certificate, you will be prompted to
*Reject*, *Accept Temporarily*, or *Accept Permanently*. Accepting
temporarily will remember the exception until the session ends. Accepting permanently
will create a .usertrust directory containing the truststore information. On Windows
this will be in your appdata directory, on Mac it will be in the Application Support
folder, and on Linux it will be in the .codedx folder in the home directory.

  
 [image: image]
