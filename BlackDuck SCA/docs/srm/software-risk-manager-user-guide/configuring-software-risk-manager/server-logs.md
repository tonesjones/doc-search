---
title: "Server Logs"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/server-logs.html"
content_id: "Hon1wkuwNlnJPdlwlnBqGw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:02.278598+00:00"
content_hash: "4bddb4609f87b6f05494e53fc959d305f631ad5bfb892ea74b55b49a90480383"
---

# Server Logs

The Server Logs page displays the contents of the Web App log, which includes details
related to analysis progress, user changes, issue tracker updates, and warnings and
errors. The Web App log can be useful in troubleshooting issues within Software Risk
Manager as well as providing context when creating a support ticket.

Click the Settings icon in the navigation bar and select Server Logs from the top menu to
open the Server Logs page.

[image: image]

Software Risk Manager maintains additional log files that provide detailed information
about runtime operations for various other tools bundled with Software Risk Manager.
These files are located in the `log-files` folder in the Software Risk
Manager `appdata` directory.

(For more information about the appdata directory, see "Understanding the AppData
Directory" in the *Software Risk Manager Install Guide*.)

## Viewing and Downloading the Server Log

**To view and download the server log file:**

1. Click the settings icon in the navigation bar and select Server Logs from the
   left menu.

   [image: image]

   Use the Line Wrapping toggle for easier viewing.
2. Click the Download button and select one of the following options:
   - **Last WebApp Log.** Downloads the most current web app log. The WebApp
     Log is the most common server log used for troubleshooting.
   - **All Logs Zipped.** Downloads all of the server logs in one .zip
     file, including all webapp logs, ML_Triage logs, and logs with
     supporting data from analyses.

   [image: image]
