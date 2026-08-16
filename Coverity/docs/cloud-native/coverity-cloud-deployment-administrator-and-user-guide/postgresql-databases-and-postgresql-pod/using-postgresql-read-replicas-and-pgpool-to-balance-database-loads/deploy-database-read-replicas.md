---
title: "Deploy database read replicas"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deploy-database-read-replicas.html"
content_id: "i6RG_YPlcm1FdKgtbg~7Mg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:14.084409+00:00"
---

# Deploy database read replicas

After setting the Helm overrides, perform an upgrade using the `helm
upgrade` command:

```
helm upgrade cnc <chartPath> -f cnc-values.yaml -f dbreadreplica-values.yaml -n <namespace>
```

See also Installing chart releases for your deployment.

For an upgrade, see also Upgrading a Coverity cloud deployment.
