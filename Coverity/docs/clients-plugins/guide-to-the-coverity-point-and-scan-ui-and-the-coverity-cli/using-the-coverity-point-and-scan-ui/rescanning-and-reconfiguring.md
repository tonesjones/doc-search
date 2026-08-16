---
title: "Rescanning and reconfiguring"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/rescanning-and-reconfiguring.html"
content_id: "gRCKUSd1bFzSNyI0b4gNhQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:48.150684+00:00"
---

# Rescanning and reconfiguring

You can use the drop-down list in the upper-right corner of the scan results dialog to quickly do
the following:

- Rescan to scan the current source. Do this if you change your source and want to
  rescan without having to reconfigure.
- Duplicate to create a new stream based on the current one, and be able to specify different
  configurations for different streams.
- Diagnostics to display the Diagnostics window.
- Delete to delete the current stream.
- Begin analysis to analyze source files that have already been captured
  (see the steps that follow).

When you rescan the source code, you can open an editor to alter the configuration to use
for the scan. To do this, do the following:

1. Choose the Rescan option, then click the edit icon on the right-hand side of the
   **Configuration File** text box.

   You can also choose a different configuration file to use for the rescan by clicking the folder icon located
   next to the edit icon at the right-hand side of the Configuration File text box.

   Coverity Point and Scan opens the configuration file using the default editor for your system.
2. Make any desired changes and then save the configuration file.
3. After you edit the existing configuration file or choose a new configuration file, click
   Begin Scan button to complete the scan.
