---
title: "Simple type: deleteSnapshotJobStatus"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/simple-type-deletesnapshotjobstatus.html"
content_id: "22NqBNJ5aIptd7GonFJeHA"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:25.260436+00:00"
---

# Simple type: deleteSnapshotJobStatus

## Description

Returns the status of a preceeding deleteSnaphot() request.

## Derived by

Restricting string

## Enumeration

| Value | Description |
| --- | --- |
| QUEUED | Queued for deletion. |
| RUNNING | Deletion in progress. |
| SUCCEEDED | Deleted successfully. |
| FAILED | Deletion failed. |

## Remarks

See getDeleteSnapshotJobInfo().
