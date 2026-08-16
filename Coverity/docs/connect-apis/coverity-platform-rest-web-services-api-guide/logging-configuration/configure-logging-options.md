---
title: "Configure logging options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-logging-options.html"
content_id: "7TWaWjoWHNIjzYbX4H98aw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:17.855743+00:00"
---

# Configure logging options

Example PUT request to configure logging options.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/loggingConfiguration?locale=en_us" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "accessControlLogging": true,
  "backgroundLogging": true,
  "bugTrackingSystemLogging": true,
  "commitLogging": false,
  "configurationLogging": false,
  "databaseLogging": false,
  "frameworkLogging": false,
  "internalLogging": false,
  "kerberosLogging": true,
  "metricsAndHistoryLogging": false,
  "notificationLogging": false,
  "performanceLogging": false,
  "policyManagerLogging": false,
  "remoteConfigLogging": false,
  "requestPerformanceLogging": false,
  "skeletonizationLogging": false,
  "triageLogging": false,
  "triageSynchLogging": false,
  "webLogging": false,
  "webServicesLogging": false
}'
```
