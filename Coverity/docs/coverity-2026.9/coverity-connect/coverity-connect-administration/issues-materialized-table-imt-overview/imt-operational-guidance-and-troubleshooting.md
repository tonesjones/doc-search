---
title: "IMT operational guidance and troubleshooting"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/imt-operational-guidance-and-troubleshooting.html"
content_id: "PxdkUhtArYbsNM_UJDiKCw"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:07.623428+00:00"
---

# IMT operational guidance and troubleshooting

Quick-reference for common scenarios related to the Issues Materialized Table (IMT),
with recommended actions and expected outcomes.

## Common scenarios

| Scenario | Recommended action | Expected outcome |
| --- | --- | --- |
| Issue View is slow after upgrade | Verify that `issue-view.imt.enabled=true` in cim.properties. If IMT is enabled, run a manual refresh via the REST API to ensure all streams are materialized. If the upgrade-time prefill did not complete, the nightly job or manual API will catch up. | Issue View latency drops to sub-second for latest-snapshot queries once streams are materialized. |
| Issue View shows unexpected results | As a diagnostic step, set `issue-view.imt.enabled=false` and restart the server to revert to the legacy query path. If results are correct with IMT disabled, file a support case with details of the discrepancy. | Issue View reverts to legacy query behavior. Performance returns to pre-IMT levels. |
| Streams are stale after re-enabling IMT | Run a manual refresh via the REST API (`POST /api/v1/admin/imt/nightly-prefill/run`) or wait for the nightly prefill job to catch up. | All stale streams are refreshed and the fast IMT query path resumes. |
| Component map rules were modified | No manual action is required. All streams using the modified component map are automatically marked stale. Issue View falls back to the legacy query until the nightly prefill or manual API refresh completes. | Correct component assignments are displayed immediately via fallback. After refresh, the fast IMT path resumes with updated component data. |
| Commit times increased after upgrade | This is expected behavior. IMT adds 10–30 seconds of commit latency per stream (proportional to stream size) because commit-refresh is synchronous. No action is needed unless latency is significantly higher than expected, in which case contact Support. | Commit-time overhead is proportional to stream size and stabilizes after the initial commit with IMT enabled. |
| Manual refresh returns `"skipped": true` | Another refresh is already running (nightly cron or another admin invocation). Wait for it to complete and retry if necessary. | The currently running refresh continues. No data is lost or corrupted. |
