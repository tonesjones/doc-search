---
title: "Coverity Connect: get the Connect configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-get-the-connect-configuration.html"
content_id: "cgfDuiczriiQIAmrpYm5Sg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:18.049578+00:00"
---

# Coverity Connect: get the Connect configuration

The following command returns Coverity Connect configuration information.

```
kubectl cp -c cim-webapp \
  "${NS}/${POD}":/config/cim/cim.properties \
  ./cim.properties
 
cat ./cim.properties
```

"$NS" is the namespace name and "${POD}" is the pod (node) name.
