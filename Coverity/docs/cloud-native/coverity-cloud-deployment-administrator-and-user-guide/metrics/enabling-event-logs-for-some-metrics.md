---
title: "Enabling event logs for some metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enabling-event-logs-for-some-metrics.html"
content_id: "Bg68XjoPuYmx81IAnzZDGQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:00.985626+00:00"
---

# Enabling event logs for some metrics

Logging has been added for application metrics related to error and latency to help with
debugging.

If the `connect.enable.logging.metrics` cim property is
`enabled`, messages for the metrics listed below will appear as
needed in the log. Event status is saved in the logs for events that generate the
following metrics. These log entries provide event details and help clarify the
metrics.

- `com_coverity_ces_web_filter_CimInstrumentedFilter_errors_total`
- `com_coverity_ces_web_filter_CimInstrumentedFilter_requests_count`
- `com_coverity_ces_web_filter_CimInstrumentedFilter_responseCodes_badRequest_total`
- `com_coverity_ces_web_filter_CimInstrumentedFilter_responseCodes_notFound_total`
- `com_coverity_ces_web_filter_CimInstrumentedFilter_responseCodes_serverError_total`
- `com_coverity_ces_web_filter_CimInstrumentedFilter_timeouts_total`
- `connect_commit_error_histogram`
- `connect_commit_latency_bucket`
- `connect_http_latency_bucket`
- `connect_web_requests_per_second`
- `connect_ws_requests_per_second`

The entries are logged using the format `<metric-name>:
<message>`.

For information on these metrics and logging entries, see API metrics.
