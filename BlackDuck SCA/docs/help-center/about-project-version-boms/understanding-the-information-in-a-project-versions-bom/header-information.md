---
title: "Header information"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/header-information.html"
content_id: "NHRDcy~R_SaHkt~RMj~Mkg"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:27.055091+00:00"
---

# Header information

Black Duck displays information in the header about the project version (such as the
phase) along with the status of scans and the BOM.

  
 [image: Header]   

**Scans** provides the status of the scans being processed for this BOM. Once the
scan completes successfully, an [image: Up to Date] status appears. Select the link to view the **Scans** tab of the
*Project Name*
*Version Name*
**Settings** tab. Use this page to manage the scans for this project version.

  
 [image: Project Version Scans tab]   

**Status** provides the current status of the BOM. It has these possible
values:

- [image: Processing text] . The Black Duck system is processing events to create or update the
  BOM.
- [image: Up to Date text] . The BOM is up-to-date; there are no errors.
- [image: Error text] . An error has occurred while processing an event or the Black Duck
  system is currently not processing any events and is up-to-date, however an
  error has occurred.

For [image: Processing text] and [image: Error text] statuses, select the link to open the BOM Processing Status dialog box.

  
 [image: BOM Process Status dialog box]   

This dialog box lists each event, who submitted it, including the date and time, the
time the event started, elapsed time, and current status.

Use this dialog box to see which events are pending or taking a long time to
complete. If errors occurred during processing, the BOM Processing Status dialog box
notifies you as to which event failed.

  
 [image: BOM Process Status dialog box]   

Click > located next to failed events to view the error message. Click [image: Delete icon] to dismiss individual errors or dismiss all errors.

If left open, the dialog box updates the information shown in the table every 30
seconds, otherwise close and reopen the BOM Processing Status dialog box for a fresh
update on the status of events.

Refer to the installation guide for information on configuring the frequency of the
BOM event cleanup job (VersionBomEventCleanupJob) which clears BOM events that might
be stuck because of processing errors or topology changes.
