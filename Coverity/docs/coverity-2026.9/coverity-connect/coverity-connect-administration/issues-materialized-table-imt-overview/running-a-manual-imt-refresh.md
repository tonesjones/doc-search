---
title: "Running a manual IMT refresh"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/running-a-manual-imt-refresh.html"
content_id: "9KgFCCtGGp_jFbF4sbZpfg"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:07.534904+00:00"
---

# Running a manual IMT refresh

Trigger an on-demand refresh of all stale streams by calling the admin REST API
endpoint.

- You must have Coverity Connect administrator credentials.
- IMT must be enabled (`issue-view.imt.enabled=true`).
- You must have network access to the Connect server REST API.

Use a manual refresh when:

- You have toggled `imt.enabled` from `false` back to
  `true` and want to catch up stale streams immediately.
- Support is troubleshooting and needs to verify that a specific installation is
  current.

1. Send a POST request to the IMT nightly-prefill endpoint on the Connect server:

   ```
   curl -X POST \
     'http://<HOST>:<PORT>/api/v1/admin/imt/nightly-prefill/run' \
     -H 'accept: application/json' \
     -u '<ADMIN_USERNAME>:<ADMIN_PASSWORD>'
   ```

   Replace `<HOST>`, `<PORT>`,
   `<ADMIN_USERNAME>`, and
   `<ADMIN_PASSWORD>` with values appropriate for your
   environment.
2. Review the JSON response to confirm the refresh completed successfully.

   A successful response:

   ```
   {
     "skipped": false,
     "foundStale": 42,
     "refreshed": 42,
     "failed": 0,
     "elapsedMs": 31500
   }
   ```

   If another refresh is already running (nightly cron or another admin invocation), the
   response includes `"skipped": true`. This is expected and safe. Wait for
   the running refresh to complete and retry if necessary.

All stale streams are refreshed and subsequent Issue View requests for those streams use the
fast IMT query path.
