---
title: "Configuring HTML report download size"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-html-report-download-size.html"
content_id: "mUPXeQwLAAyZqGyP1eoLqQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:25.285693+00:00"
content_hash: "4a8e467eb88af7be36c82e316a0108eea53fe7c6b75cd40439a7910f5ebc31ca"
---

# Configuring HTML report download size

You can configure your environment to allow for larger or smaller HTML report downloads. The default size is 3000 KB. Reports exceeding this limit will return a 503 Service Unavailable error message.

To change this limit, change the value of the `HUB_MAX_HTML_REPORT_SIZE_KB` property in your `blackduck-config.env` file.
