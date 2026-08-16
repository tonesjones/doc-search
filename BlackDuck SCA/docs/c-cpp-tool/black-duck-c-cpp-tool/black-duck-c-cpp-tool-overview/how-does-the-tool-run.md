---
title: "How does the tool run?"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/how-does-the-tool-run-.html"
content_id: "y8V_SQ48DovNtm3pFlg3HA"
version: "latest"
section: "Black Duck C/CPP Tool"
scraped_at: "2026-08-13T16:16:52.941441+00:00"
---

# How does the tool run?

[image: image]

The Black Duck C/CPP tool first starts by running a [Coverity](https://documentation.blackduck.com/bundle/coverity-docs/page/webhelp-files/help_center_start.html) build which will
compile your code and package it for the scanning process. The scan is
not limited to a single directory, it will use linker and header files
to gather all necessary data for the scan.

It will then run a package manager scan on the compiled code.

Once the package manager
scan is complete and if you are licensed for BDBA scanning, the tool
will then take any files not matched in the package manager scan and
run an integrated BDBA scan on them. If you are not licensed for
BDBA use, this step is skipped.

Following the BDBA scan, the
tool will run a signature scan on any remaining unmatched
files.

Finally, the tool with run a snippet scan on any
further unmatched files, provided you have snippet scans enabled in
your environment. Click [here](https://documentation.blackduck.com/bundle/bd-hub/page/ComponentDiscovery/Snippets.html) for more information
on snippets.

These results are then sent to Black Duck so that
you can view the
results.
