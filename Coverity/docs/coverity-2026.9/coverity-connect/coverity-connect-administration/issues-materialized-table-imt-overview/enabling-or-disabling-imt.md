---
title: "Enabling or disabling IMT"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/enabling-or-disabling-imt.html"
content_id: "RVgWnzd2V9nQty0MAvikRQ"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:07.491085+00:00"
---

# Enabling or disabling IMT

Enable or disable the Issues Materialized Table (IMT) performance path by setting the
`issue-view.imt.enabled` property in the Connect server configuration
file.

- You must have administrator access to the Coverity Connect server.
- You must be able to restart the Connect server process.

IMT is enabled by default in the 2026.9.0 release. Disable IMT only as a temporary
diagnostic step if Issue View returns unexpected results after an upgrade. Report the issue
to Support because IMT is the recommended path and disabling it is a workaround, not a
permanent state.

1. Open the cim.properties file on the Connect server in a text
   editor.
2. Locate or add the `issue-view.imt.enabled` property.
3. Set the value:

   | Option | Description |
   | --- | --- |
   | To enable IMT | Set `issue-view.imt.enabled=true` |
   | To disable IMT | Set `issue-view.imt.enabled=false` |
4. Save and close the file.
5. Restart the Coverity Connect server for the change to take effect.

When IMT is enabled, eligible Issue View queries for the latest snapshot are served from the
pre-materialized table. When IMT is disabled, Connect reverts to the legacy Issue View query
(the behavior of all prior releases).

If you re-enable IMT after it was disabled, consider running a manual IMT refresh to catch
up stale streams immediately rather than waiting for the nightly prefill schedule.
