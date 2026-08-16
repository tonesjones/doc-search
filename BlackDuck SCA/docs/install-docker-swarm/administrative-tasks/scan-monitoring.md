---
title: "Scan monitoring"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/scan-monitoring.html"
content_id: "uDNaNCOeZ_W77j2ikHkGQQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:03.146676+00:00"
---

# Scan monitoring

The default period where information is gathered for the scan monitoring endpoint is
1 hour. This can be configured to a different value by using the
following property:

`HUB_SCAN_MONITOR_ROLLUP_WINDOW_SECONDS`

The API will only be able to provide information if the system has at least a specific
number of scans to analyse in the last time period configured above (default period is 1
hour). If the scans are less than the threshold value, a level 1 request will return a
**OK** response by default. The number of scans can be configured to a different
value by using the following property:

`HUB_SCAN_MONITOR_MINIMUM_SCAN_COUNT`

A level 1 request returns a response of "OK" or "NOT OK" based on the failure rate
thresholds, where a result greater than the upper limit will return a "NOT OK" response.
The upper (default 30%) and lower (default 10%) limits are set as a percentage and can
be configured with the following properties:

`HUB_SCAN_MONITOR_ERROR_RATE_LOWER_THRESHOLD_PERCENT`

`HUB_SCAN_MONITOR_ERROR_RATE_HIGHER_THRESHOLD_PERCENT`

For more information on the scan monitoring API request, please refer to the REST API
Developers Guide in Black Duck.
