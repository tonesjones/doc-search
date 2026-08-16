---
title: "Azure flexible server IsSSD property"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/azure-flexible-server-isssd-property.html"
content_id: "ZnpyLOW7KiW2PpvjBP62Fg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:22.579200+00:00"
---

# Azure flexible server IsSSD property

For the Azure flexible server, there is no way to find out if it is SSD. In the tuning
yaml file, set `isSSD` as `false` to make sure no
discrepancies occur.

For further information, as per this document, disk type is not available for Azure:
<https://learn.microsoft.com/en-us/answers/questions/1108533/fetch-hardware-detailsdisk-type-of-a-azure-postgre.html>
