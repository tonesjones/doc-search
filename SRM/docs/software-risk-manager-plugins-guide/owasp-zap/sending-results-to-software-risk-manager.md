---
title: "Sending Results to Software Risk Manager"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/sending-results-to-software-risk-manager.html"
content_id: "~uxQerGQPwR952On8wBXRg"
version: "latest"
section: "Software Risk Manager Plugins Guide"
scraped_at: "2026-09-08T20:06:05.407971+00:00"
content_hash: "2a6aa81266d9bbb7a4faf113ec91cf599d27c032e9f8aef5b176c14f5578bf27"
---

# Sending Results to Software Risk Manager

The OWASP ZAP plugin can generate a compatible XML file which can be uploaded manually,
or it can upload a report directly to Software Risk Manager.

To upload a report to Software Risk Manager, select the *Software Risk Manager: Upload Report*
option from the *Report* menu.

  
 [image: image]   

You will be prompted for the *Server URL*, *API Key* and *Project*. Your
settings will be remembered between sessions and are stored in the srm.properties
file located in the OWASP ZAP folder in your user directory.

  
 [image: image]   

After entering the *Server URL* and *API Key*, click the *Refresh* button
to populate the *Project* dropdown.

  
 [image: image]   

If you receive a warning regarding an invalid certificate, you will be prompted to
*Reject*, *Accept Temporarily*, or *Accept Permanently*. Accepting
temporarily will remember the exception until the session ends. Accepting permanently
will create a .usertrust directory containing the truststore information. On Windows
this will be in your appdata directory, on Mac it will be in the Application Support
folder, and on Linux it will be in the home directory.

  
 [image: image]   

You will receive a message indicating whether or not the action was successful.

  
 [image: image]   

You can generate an XML file for use with Software Risk Manager by selecting the *Software
Risk Manager: Generate XML Report* option from the *Report* menu.

  
 [image: image]
