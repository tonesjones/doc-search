---
title: "Disabling collection of use and compliance data"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/disabling-collection-of-use-and-compliance-data.html"
content_id: "h7k22LRTcp6k9NBUSmDAgQ"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:06.296851+00:00"
---

# Disabling collection of use and compliance data

To disable the collection of use and compliance data (UDC), add the following property to
the `cim.properties` file:

```
udc.data.collection.disable=true
```

The `cim.properties` file is located in the
<coverityConnectInstallDir>/config/ directory.
