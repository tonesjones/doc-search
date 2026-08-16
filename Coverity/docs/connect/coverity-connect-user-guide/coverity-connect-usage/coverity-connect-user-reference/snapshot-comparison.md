---
title: "Snapshot comparison"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/snapshot-comparison.html"
content_id: "keL1qePGuOsRrHE~WSvBoA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:29.434008+00:00"
---

# Snapshot comparison

Snapshot comparison is a filtering mechanism that allows you to construct a scope by
using the snapshot selection
grammar to compare snapshots to the scope defined in the Show field. From the
comparison results, you can then apply filters to create views that list the CIDs in
which you are interested. For example, you can create views that list:

- Issues introduced in the latest analysis run
- Issues fixed in the latest analysis run
- Issues introduced in the last <number_of> days
- Issues introduced since the last release
- Issues that are have not been fixed since the last release

This feature is not a required operation. It is intended as an "advanced" option to
determine a CID's absence or presence in a given scope of snapshot (as displayed in the
Comparison column):

- present - The CID exists in the snapshot(s) defined in
  Show and at least in one of the comparison
  snapshots.
- absent - The CID exists in the snapshots defined in
  Show, but not in any of the comparison
  snapshots.

Note: Use the Comparison filter to list
only the CIDs that are present or absent from the results of the comparison
scope.

The comparison scope is available to the following view types:

- Issues: By snapshot - Located in the Snapshot scope filter of the
  Edit Settings window.

- Snapshots - When you click on a snapshot, the
  Snapshot Comparison filter is available in the right
  hand panel. After you apply the filter, the CIDs that match the comparison scope
  are opened as an Unsaved view in 
  Issues: By Snapshots
  . To create a new view from this unsaved view, click the Save
  as Copy option and rename, apply filters, and save the copied
  view.
