---
title: "Coverity Connect properties"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-properties.html"
content_id: "wIVU2X5jkNit3Ln0n5WTQw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:30.602003+00:00"
---

# Coverity Connect properties

You can provide properties to Connect through the
`cim.cimweb.extraProperties` Helm key in the `cnc`
Helm chart.

```
cim:
  cimweb:
    extraProperties: {}
```

The `extraProperties` are added as `cim.properties` when you
deploy the `cnc` Helm chart `values.yaml` file that
contains the extra properties. You can apply `<property>:
<value>` pairs as needed for your use case. For example:

```
cim:
  cimweb:
    extraProperties:
      login.auth.check.failed.reset.delay.minutes: 1
      login.auth.check.failed.peruser.count: 10
```
