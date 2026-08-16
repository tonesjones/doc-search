---
title: "Retrieve logging configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-logging-configuration.html"
content_id: "9tinbczc0oxz7X7DkY8DpQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:17.194512+00:00"
---

# Retrieve logging configuration

Example GET request to retrieve the logging configuration.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/loggingConfiguration?locale=en_us" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "accessControlLogging": false,
  "backgroundLogging": false,
  "bugTrackingSystemLogging": false,
  "commitLogging": false,
  "configurationLogging": false,
  "databaseLogging": false,
  "frameworkLogging": false,
  "internalLogging": false,
  "kerberosLogging": false,
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
  "webServicesLogging": false,
  "code": null,
  "message": null
}
```
