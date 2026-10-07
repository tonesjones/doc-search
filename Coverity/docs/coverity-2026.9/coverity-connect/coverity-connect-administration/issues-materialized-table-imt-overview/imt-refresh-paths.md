---
title: "IMT refresh paths"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/imt-refresh-paths.html"
content_id: "ugvKQs~zbYBRKBKQhpKGng"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:07.409919+00:00"
---

# IMT refresh paths

Materialized data in the Issues Materialized Table is kept current through four
mechanisms. Operators do not normally need to intervene because the system handles refresh
automatically.

## Commit refresh (automatic, every commit)

Every time a `commit-defects` operation completes, Connect immediately
refreshes the materialized data for that stream. This is synchronous and occurs just after
the commit transaction finishes.

The refresh adds a few seconds to commit time. On typical customer hardware, expect 10–30
seconds of additional commit latency per stream. This time is proportional to the size of the
stream (number of issues).

If the refresh fails, the commit itself is not affected. Connect will serve Issue View for
that stream via the legacy query path until the next successful refresh.

## Nightly prefill (automatic, scheduled)

A background job runs at the configured schedule (default 2:00 AM local time) and refreshes
any streams whose materialized data is missing or out of date. This catches:

- Streams where a commit-refresh failed.
- Streams not yet materialized (for example, after upgrading from a prior release).
- Streams that became stale while `imt.enabled` was temporarily set to
  `false`.

Enable the nightly prefill job with
`issue-view.imt.nightly-prefill.enabled=true` for production
deployments.

## Manual refresh via REST API (on-demand)

Administrators can trigger a refresh of all stale streams on demand using the admin REST
endpoint. Use this method when:

- Upgrading from a prior release and wanting to pre-fill IMT without waiting for the
  nightly schedule.
- Toggling `imt.enabled` from `false` back to
  `true` and wanting to catch up stale streams immediately.
- Support is troubleshooting and needs to verify that a specific installation is
  current.

If another refresh is already running (nightly cron or another admin invocation), the
response includes `"skipped": true`. This is expected and safe.

## Upgrade-time prefill (automatic, runs during upgrade)

During an upgrade, a prefill step automatically materializes data for all existing streams
using a parallel job. Customers upgrading from a prior release will have IMT data populated
during their normal upgrade window.
