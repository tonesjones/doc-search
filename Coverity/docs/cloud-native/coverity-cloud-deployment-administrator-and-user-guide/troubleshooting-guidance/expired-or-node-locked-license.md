---
title: "Expired or node-locked license"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/expired-or-node-locked-license.html"
content_id: "EKyBE4f4GgcrOzubGaPosQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:40.783613+00:00"
---

# Expired or node-locked license

If your license has expired or is node-locked, the Helm chart will fail to deploy and
will return a timeout message. To validate that this is the issue, inspect the logs for
the `cim-update-license` pod. If the license has expired or is
node-locked, you should see a license related error message in the log.
