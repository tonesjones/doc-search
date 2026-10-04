---
title: "IMT configuration properties"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/imt-configuration-properties.html"
content_id: "oZU5ofYmaVAcKFagUaeItw"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:07.580634+00:00"
---

# IMT configuration properties

Reference for the three cim.properties parameters that control the
Issues Materialized Table (IMT) feature. All properties require a server restart to take
effect.

## Properties

| Property | Default | Values | Description |
| --- | --- | --- | --- |
| `issue-view.imt.enabled` | `true` | `true` / `false` | Master switch for the IMT performance path. When `true`, eligible Issue View queries are served from the pre-materialized table instead of the full SQL query. When `false`, Connect reverts to the legacy Issue View query (the behavior of all prior releases). Disable only as a temporary guardrail if Issue View returns unexpected results after upgrade. Report the issue to Support. |
| `issue-view.imt.nightly-prefill.enabled` | `false` | `true` / `false` | Enables the nightly background job that catches up any streams whose materialized data is missing or out of date. Recommended to enable on production deployments. |
| `issue-view.imt.nightly-prefill.cron` | `0 0 2 * * ?` (2:00 AM local time) | Quartz 6-field cron expression | Schedule for the nightly prefill job. Adjust if your maintenance window conflicts with 2:00 AM. Example: `0 30 3 * * ?` runs at 3:30 AM. |

## Notes

- All three properties are set in cim.properties on the Coverity
  Connect server.
- A server restart is required after changing any of these properties.
- The nightly prefill cron property has no effect unless
  `issue-view.imt.nightly-prefill.enabled` is set to
  `true`.
