---
title: "Testing WebSocket connectivity"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/testing-websocket-connectivity.html"
content_id: "OCS2uOttwbR~xrSyMqgThg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:27.872960+00:00"
---

# Testing WebSocket connectivity

The `cov-commit-defects` command provides the option of committing
analysis data over HTTPS using a WebSocket connection. To ensure that the Coverity
Connect server's WebSocket connection is functioning properly, perform the following
test:

1. In the Coverity Connect GUI, select System Diagnostics from
   the Help menu.

   The Coverity
   Diagnostics page is displayed.
2. Click the WebSocket Connectivity tab.
3. Click the Test Connectivity button.

   The page displays the
   following message if the server's WebSocket connectivity is functioning
   properly.

   Figure 1. Successful test of WebSocket connectivity
     
    [image: image]
