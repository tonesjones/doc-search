---
title: "Stream lock metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/stream-lock-metrics.html"
content_id: "VKKB3Y04rsUqT92YKxy21Q"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:12.658528+00:00"
---

# Stream lock metrics

The following table describes stream lock metrics.

Table 1. Stream lock metrics

| Metric | Description | Metric type | Examples: PromQL queries |
| --- | --- | --- | --- |
| `lock_cache_size` | **JDBC locks cache size**  This metric is a gauge that represents JDBC locks cache capacity.  There is an upper limit of 100000 for JDBC locks cache capacity in the Connect application by default. This is specified by the `locks.jdbc.​cacheCapacity` cim property. If the metric reaches a value near this upper limit, increase the limit using the `locks.jdbc.​cacheCapacity` property. | Gauge | `lock_cache_size` |
| **Interpreting the metric**  If the JDBC Locks Cache size is reaching or approaching the upper limit (100,000 by default) then the locks.jdbc.cacheCapacity property should be increased. | | |
| `no_of_commits_​queued_for_a_​stream` | Track no of commits queued for a particular stream. | Gauge | `no_of_commits_queued_for_a_stream` |
| `stream_locked` | **Is stream locked**  This metric is a boolean gauge that tracks whether a particular stream is currently locked or unlocked, as follows:   - `1.0` indicates that the stream is locked. - `0.0` indicates that the stream is unlocked.   This metric comes with the `streamname` label where:   - `streamname` represents the name of stream. | Gauge | `sum by (streamname) ​(stream_locked)` This example presents a graph of the `stream_locked` app metric by listing values for all streams.  Additionally, the following Grafana variables can be added to the dashboard to help specify `streamname` and pod data.   - `label_values(stream_locked,​streamname)`   gets `streamname` data. - `label_values(stream_locked)` gets pod   data. |
| **Interpreting the metric**  If there are commits that are waiting in the queue but there appears to be available executers for the commit, then it can be helpful to verify if the stream in question is locked. If a stream is locked, it is an indication that there is a commit in progress on the stream and the system limits commits to just one per stream. | | |
