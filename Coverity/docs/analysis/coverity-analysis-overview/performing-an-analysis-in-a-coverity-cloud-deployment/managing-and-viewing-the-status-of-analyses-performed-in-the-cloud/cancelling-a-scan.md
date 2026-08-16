---
title: "Cancelling a scan"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cancelling-a-scan.html"
content_id: "hwDvu~ZqKMRyb6WkU7a80w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:40.539421+00:00"
---

# Cancelling a scan

Using the Coverity Connect UI, you can cancel a scan if the status of the scan is
`QUEUED` or `RUNNING`.

You cannot cancel a scan if the status is `COMPLETED`,
`FAILED`, or `CANCELLED`.

To cancel a scan in the Coverity Connect UI:

1. Log into the cloud-native Coverity Connect UI.
2. Open the Scan List view. To open the view, click the View icon [image: image] , then select
   Scan List > All Scans. The
   Scan List view opens for all scans.
3. Scroll and find the scan that you need to cancel.
4. In the `Actions` column and on the scan row to cancel, click
   [image: image] and in the drop-down, click
   Cancel.

   [image: image]

   Upon cancelling a scan, you will see a banner message such
   as:

   - For a successful cancel, green text: `'Scan cancelled
     successfully.'`
   - For a failed cancel, red text. For example, `'Scan reached state
     FAILED, cannot cancel.'`

   Click X in the banner to close the banner.

   Note: The `Cancel` option is disabled if the scan
   status is `COMPLETED`, `FAILED` or
   `CANCELLED`.
