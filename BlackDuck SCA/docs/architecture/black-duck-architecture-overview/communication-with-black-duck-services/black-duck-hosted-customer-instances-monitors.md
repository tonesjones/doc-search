---
title: "Black Duck Hosted customer instances monitors"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/black-duck-hosted-customer-instances-monitors.html"
content_id: "yxqsaN6LMc~nLpayhgdXXQ"
version: "2026.7"
section: "Architecture and Network Communications"
scraped_at: "2026-08-08T15:32:45.745791+00:00"
---

# Black Duck Hosted customer instances monitors

In the Black Duck Black Duck Hosted environment, there are monitors and alerts enabled
for each instance.

For monitoring, we are gathering the data on this metric and store it for a period of
time. This data can be used for later analysis. There may be thresholds in which
informational messages are dispatched, but a response is not required or triggered
for these types of monitors.

Examples of scenarios we monitor are Daily Scans and Job Instances which provide
useful metrics when issue analysis is being investigate by CloudOps and/or
Support.

For alerting notifications, we are monitoring the metrics with thresholds. There are
low and high level thresholds which may be adjusted based on reviews of Black Duck
Performance Testing Lab or changes to Black Duck functionality. Low levels do not
require an immediate response. High levels require an immediate response. When a
certain threshold is crossed, the CloudOps team is paged via our paging system. A
technical support ticket MAY be opened depending on the alert, and how many times we
have notified technical support. The Technical Support team troubleshoots the issue
and informs the customer of the issue while it is being investigated.

Examples of types of alerts that trigger Support tickets are: Database CPU
utilization hitting the high threshold which usually indicates that the customer is
performing actions which are heavily impacting the database which could cause the
instance to require rebooting or resizing. Pod Readiness is monitored which
indicates that a pod has been running, but that it is not ready to process requests.
When it taken too long for it to come online an alert is triggered to check the
instance
