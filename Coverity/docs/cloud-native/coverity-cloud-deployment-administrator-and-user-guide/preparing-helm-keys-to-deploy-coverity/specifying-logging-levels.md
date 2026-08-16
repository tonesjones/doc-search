---
title: "Specifying logging levels"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specifying-logging-levels.html"
content_id: "DCmoFVlZb5OWvcNbtsNw_A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:37.109112+00:00"
---

# Specifying logging levels

All Coverity cloud containers write logs. Through the Helm chart, you can specify the
granularity of the information presented to the logs. In the Helm keys that follow,
`logLevel` is the minimum log level required before events are
logged.

Note: "INFO" presents all log levels from informational through the
highest level. The log levels can be alll uppercase or all lowercase with the values:
ALL, TRACE, INFO, WARN, ERROR, FATAL, OFF.

In the `cnc` chart, the `cim.cimweb.logLevel` Helm key
specifies a cimweb log level, and.the `cim.commit-server.logLevel` Helm
key specifies the commit server log level (see Optimizing commit performance vs throughput using commit-server pods). Either accept the default log level (INFO) or specify a log level for cimweb. The
keys and default value are:

```
cim:
  cimweb:
    logLevel: "INFO"

cim:
  commit-server:
    logLevel: "INFO"
```

See cnc Helm chart: Helm keys.

The following Helm keys in the `scan-services` chart specify the logging
level for scan services. minimum log levels required before events are logged. These
logged events are also available through metrics, if metrics is enabled and
configured.

```
cache-service:
  logLevel: "INFO"
 
scan-service:
  logLevel: "info"
 
storage-service:
  logLevel: "info"
```

See scan-services Helm subchart: Helm keys.
