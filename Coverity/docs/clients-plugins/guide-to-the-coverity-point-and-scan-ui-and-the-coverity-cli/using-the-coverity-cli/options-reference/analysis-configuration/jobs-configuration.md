---
title: "Jobs configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/jobs-configuration.html"
content_id: "o1Ikr50JDGdNS5M7r8mh9g"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:14.566766+00:00"
---

# Jobs configuration

These keys configure worker parallelism during analysis.

| Key | Type | Description |
| --- | --- | --- |
| `auto` | Boolean | If `true`, the number of analysis workers to run in parallel is based on the amount of memory and the number of logical processors in the machine. This is the default for a license that is not a FlexNet license. This key is mutually exclusive with the `count` and `max` keys. |
| `count` | integer | The number of analysis workers to run in parallel. This key is mutually exclusive with the `auto` and `max` keys. |
| `max` | integer | The maximum number of analysis workers to run in parallel, subject to limits on the amount of memory and the number of logical processors in the machine. A value of `8` is the default for a FlexNet license. This key is mutually exclusive with the `auto` and `count` keys. |
| `override-worker-limit` | Boolean | When `true`, allows the number of analysis workers to exceed the recommended value. This key must be used only with the `count` key. |
