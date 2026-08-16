---
title: "Detect usage metrics collection"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-usage-metrics-collection.html"
content_id: "H0kDTMSyogGSN4xhJCv~Ag"
version: "11.5.1"
section: "Troubleshooting"
scraped_at: "2026-08-08T23:45:54.022398+00:00"
---

# Detect usage metrics collection

Black Duck® Detect uses Google Analytics to collect anonymized usage metrics through a mechanism called *phone home*.
Black Duck Software, Inc. uses this data to help set engineering priorities.

In a network where access to outside servers is limited, this mechanism may fail, and those failures
may be visible in the log. These are harmless failures; Detect will continue to function
normally.

To disable this mechanism for Detect runs executed from one environment,
set the environment variable *BLACKDUCK_SKIP_PHONE_HOME* to *true*.
To disable this mechanism for all Detect runs against a specific Black Duck SCA
server, refer to the Black Duck SCA documentation for information on disabling analytics.
