---
title: "Switching between single vs multiple scan jobs per node"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/switching-between-single-vs-multiple-scan-jobs-per-node.html"
content_id: "lKy3AKmWcPvuArYnGQKLgA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:13.612184+00:00"
---

# Switching between single vs multiple scan jobs per node

If you need to switch from one method to another, in addition to setting the
`MULTIPLEJOBSPERNODE_ENABLE` boolean
(`true`|`false`) Helm key value, you need to make sure
that all node pools and resources exist and are enabled or disabled for the method you
are switching to.

For example, if you switch from multiple jobs per node to single job per node, in
addition to setting `MULTIPLEJOBSPERNODE_ENABLE: false` you might also
need to enable multiple node pools.

Subsequently, before you can switch back to multiple jobs per node, you will need to
enable only one scan job node pool (disable all other scan job node pools), then set
`MULTIPLEJOBSPERNODE_ENABLE: true`.
